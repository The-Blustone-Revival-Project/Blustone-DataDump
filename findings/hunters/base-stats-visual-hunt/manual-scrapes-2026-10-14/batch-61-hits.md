# Batch 61 hits (idx 3001-3050)

Lane: `findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/`
Crops: `hits/batch-61-3008.png`, `hits/batch-61-3027.png`, `hits/batch-61-3028.png`, `hits/batch-61-3031.png`, `hits/batch-61-3050.png` (5 HITs).
Zooms (lane folder, provenance only): `z61_3008_zbadge`
(3-star gold), `z61_3024_zbadge` (3-star gold),
`z61_3027_zbadge` (4-star green ring), `z61_3028_zbadge`
(4-star green ring), `z61_3031_zbadge` (5-star blue),
`z61_3040_zbadge` (5-star blue), `z61_3050_zbadge` (4-star
green ring); `z61_*_badge/badge2/badge3/badge4`,
`z61_3031_leftband`, `z61_*_thumb` (orientation/work crops).
OCR (lane folder): `_tmp61_dims_ocr.json` (tesseract
`--tessdata-dir` `%TEMP%/opencode/tessdata`, `-l eng`,
full-frame). OCR is unreliable on the italic game font and
misses star shapes entirely (e.g. 3035 promo triangle-1600%
misread as "41600%"); visual zoom wins everywhere.
Write scripts: `_tmp61_dims_ocr.py`, `_tmp61_zoom.py`,
`_tmp61_hits.py`, `_tmp61_write.py` (kept in lane folder
per rules).

## HITs: 5/50

### idx 3008: Experienced Hunter Hermes, Lv.1, 3-star, HP 637 / ATK 507 / DEF 358 (catalog 023)
- File: `Screenshot_20190425-083832_Blustone-a584433502b194e8.jpg`
  (1080x874). Crop: `hits/batch-61-3008.png`.
- Card-detail; 3-star gold badge zoom-verified
  (`z61_3008_zbadge`, 2 small + 1 large); Attacking Speed 8;
  Train / Transcendence / Skill Training / Upgrade Equipment
  / Story; Offense + Fire icons.
- Title Experienced Hunter vs catalog 023 Elite Messenger =
  advancement tier title.

### idx 3027: The Prestigious Tailor Erise, Lv.1, 4-star (catalog 063)
- File: `Screenshot_20190506-005011_Blustone-9c6ad60e582cd02b.jpg`
  (1080x2280). Crop: `hits/batch-61-3027.png`.
- Recruited splash; 4-star green-ring badge + Lv.1 ribbon
  zoom-verified (`z61_3027_zbadge`); Defense + Electricity;
  +1000 coins bubble; Show off now!; See Details / Okay /
  Share.
- Title has "The" prefix vs catalog "Prestigious Tailor";
  element wording Electricity (= catalog Lightning).

### idx 3028: Windy Soul Windblade, Lv.1, 4-star (catalog 052)
- File: `Screenshot_20190506-200153_Blustone-bec5259200ca6542.jpg`
  (1080x2280). Crop: `hits/batch-61-3028.png`.
- Recruited splash; 4-star green-ring badge + Lv.1 ribbon
  zoom-verified (`z61_3028_zbadge`); Offense + Electricity;
  See Details / Okay (no +1000 bubble on frame).
- Title matches catalog 052; same hero/title as idx 3050
  (different timestamps, both fresh Lv.1 recruits).

### idx 3031: Elite Messenger / Master Hunter Hermes, Lv.30, 5-star, HP 3187 / ATK 1977 / DEF 1227 (catalog 023)
- File: `Screenshot_20190507-141420_Blustone-dd959f1edf001dd8.jpg`
  (1080x2220). Crop: `hits/batch-61-3031.png`.
- Train Teammate; 5-star blue badge zoom-verified (white
  stars: 2 small top + 1 large center + 2 small bottom,
  `z61_3031_zbadge`); badge ribbon Lv.MAX + red hand icon;
  Strength 30742; Attacking Speed 8; Attack details Crit
  Chance 35 / Crit Damage 235 / Armor Pen 0; Defense details
  Block 19 / DR Block 40 / Elem Enh 7 / Elem Res 18 /
  Regen 44; Advance / Transcendence / Skill Training /
  Upgrade Equipment / Story (greyed).
- Jewel screen idx 3033 confirms the naked base
  (3104+83=3187, 1657+320=1977, 1198+29=1227); tiny crop
  idx 3030 (Lv.MAX 30742) is the same hero.

### idx 3050: Windy Soul Windblade, Lv.1, 4-star (catalog 052)
- File: `Screenshot_20190519-023408_Blustone-5e3850cda6785108.jpg`
  (1080x2220). Crop: `hits/batch-61-3050.png`.
- Recruited splash; 4-star green-ring badge + Lv.1 ribbon
  zoom-verified (`z61_3050_zbadge`); Offense + Electricity;
  +1000 coins bubble; Show off now!; See Details / Okay.
- Title matches catalog 052; re-recruit pair with idx 3028
  (no advancement between frames).

## Near-hits (hit=no per bar rules)

### Level + stars shown, no HP/ATK/DEF
- idx 3024: Elite Messenger / Experienced Hunter Hermes,
  Lv.1, 3-star gold (zoom-verified `z61_3024_zbadge`),
  Strength 2597; Class sword / Elemental hand icons
  (catalog 023; tier-title discrepancy).
- idx 3040: Animal Lover / Master Hunter Pansy, Lv.1,
  5-star blue (zoom-verified `z61_3040_zbadge`), Strength
  12216; Class heart / Elemental blue icons (catalog 057).

### Attributes with no hero identity
- idx 3007: Character Attributes strip HP 3142 / ATK 1935 /
  DEF 1210 / Attacking Speed 8 (cropped strip).

### 11-pull result (star counts only)
- idx 3037: 4x 1-star (brown) / 2x 2-star (silver) / 5x
  3-star (gold); One more time! 300 manda / Okay
  (4+2+5=11 verified).

### Recruit grid / event (no per-hero level/stars)
- idx 3021: Recruit 3-star Hunter grid (Defense filter):
  Nene / Athena / Kain / Bear / Edward / Papillon / Dumble
  / Calibur / Juno with titles (see sic list).
- idx 3023: card-flip event grid, 8x 1-star brown hero
  cards + 3x gear BONUS cards; Reveal All.

## Cross-batch pairing notes

- Hermes chain: idx 3008 (Experienced Hunter Lv.1 3-star,
  637/507/358) -> idx 3024 (same tier Lv.1 3-star, Strength
  2597) -> idx 3031 (Master Hunter Lv.30 5-star, 3187/1977/
  1227, Strength 30742) + idx 3033 jewel screen (same hero:
  3104+83 / 1657+320 / 1198+29, 6x red Lv.15 jewels) +
  idx 3030 crop (Lv.MAX 30742). Tier titles run Elite
  Messenger (header) / Experienced Hunter / Master Hunter
  vs catalog 023 Elite Messenger.
- Shared jewel-set bonus vector (+344 / +449 or +454 /
  +132 / +0 / +2.47 / +20.76 / +0 / +5.21 / +0.91 / +1.44 /
  +12.33 / +0, 3x Mount 2 Increase ATK 5%): idx 3014
  (23121+6961) = idx 3016 gear diagram = idx 3032
  (23668+7074, different hero base) = idx 3033.
- Hunter-list scroll pair (same account): idx 3038 (By
  Power 43/54 tail) -> idx 3039 (head, top team 26327
  Leader / 25066 Offense Team / 24815 Defending).
- Legends guild chain: idx 3010 (rank 40, 5744750, My
  Guild) -> idx 3011 (guild info: Contribution
  5744750/15620000, Region Rank 48, Public, Required 1000,
  Rewards 5744750/10000000); elb profile idx 3044 sits in
  the same guild (level-4 badge).
- elb account: idx 3043 (drawer, level 64) -> idx 3044 (My
  Information: FC power 122840, League 1215/616th, Heart
  of the Golden Abyss Area 360, Midgard, Norway flag).
  FC wallet delta vs idx 3042 (86888) = different accounts.
- Battle side-panel pair: idx 3046 (ally column) + idx
  3047 (enemy column); rooster (Beckhen) appears both
  sides.
- Windblade re-recruit: idx 3028 -> idx 3050 (both Windy
  Soul Lv.1 4-star, no advancement).
- Promo: idx 3035 (triangle-1600% x80000 + Veteran Point
  Gift Certificate x3) matches the batch-58 ladder
  (1600% x80000 vs 200% x10000, 8x both legs).
- Duplicate: idx 3003 pixel-duplicates idx 3002 (Light
  Green Manda Bundle).
- Transcendence tiers: +12% strips (idx 3009, 3026) vs
  +14% strip (idx 3034).

## Most valuable economy/mechanic readings

- Rupee promo (idx 3035): triangle-1600% x 80000 (huge
  amount) + Veteran Point Gift Certificate x3; implied
  base 5000 (80000/16).
- VIP privilege ladder (idx 3036): Guru 3 (+14/+14) ->
  Guru 3 block (Hidden Hunter, Abyss +1, Fuel +16, Rupee
  +16, Invites +16) -> Legendary 1 (Abyss +2, +18s) ->
  Legendary 2 (Abyss +2, Special Support Fuel +20, +20s)
  -> Legendary 3 (Abyss +3, +22s).
- Manda bundles (idx 3002/3004): Light Green (blue scroll
  X1, green scroll X3, blue stones X200, orange ticket X1
  / black ticket X4, red-cap X1, arcade X450, orange
  machine X40, orange ticket X1); Dark Green (black ticket
  X8, red scroll X1, blue stones X500, green ticket X1 /
  blue scroll X1, green ticket X1, arcade X1000, red-cap
  X4, orange machine X100, red-cap X3, blue orb X10).
- Fight Chips shop (idx 3020): wallet 2110; Beckhen's /
  Natalia's / Juno's Trace x5 @375 each; list refresh
  03:19:16. Boutique Ticket x1 @6000 (idx 3041).
- Major Goal (idx 3022): "But it's hard to save...",
  Rupees Spent 17863465/20000000, green gem x30.
- Geranium rebalance notice (idx 3045): 2nd-skill max-HP
  cut removed -> bleeding-until-disabled; 4th-skill enemy
  buff-strip added (Force Switch subject); 5th-skill armor
  pen 10 -> 15.
- Trace tier (idx 3025): Offense 15/16, Critical Damage
  Bonus 15.0% -> 16.0%.
- Blog pull math (idx 3017/3018): Diana 300-manda rate
  ~11.621848778% per pull (weekend-only 4-star);
  Teresa 1.4%/11 tries (4.12% at 300%), full binomial
  formula in notes.
- FC Team Attacking Powers: 86888 (idx 3042) vs 122840
  (idx 3044, 5x Lv.MAX); preview ties at 18606 x4
  (idx 3049).

## Non-ASCII names (transliterated, for searchability)

- idx 3049: Neko Suki Gyu-don-san (Japanese script
  transcribed verbatim in TSV), DeusEx87, WolfCage,
  TayOtaku. idx 3044: elb. idx 3017/3018: RaynerSin,
  Ninja4Hire, Diana, Teresa. idx 3020-3021: Beckhen,
  Natalia, Juno, Nene, Athena, Kain, Bear, Edward,
  Papillon, Dumble, Calibur.

## Contaminants

- idx 3013: YouTube battle clip (player UI + suggested
  videos), damage 8649 / HP 1668.
- idx 3017/3018: blog/forum screenshots (pull-odds
  discussion); game-adjacent, classified other.
- idx 3019: Video_Player battle clip, damage 11455,
  F DOWN label; small crop.
- idx 3048: Google Play Store listing (Blustone 2 -
  Adventure Anime RPG, VisualShower Corp.).
- OS chrome: Android nav bars on recruit splashes
  (idx 3027/3028/3050); status-bar scraps on VIP/shop
  screens; transcribed and flagged non-game.

## Sic list

- "The Prestigious Tailor" Erise (idx 3027, client
  article vs catalog 063 "Prestigious Tailor").
- "Flame of the Battlefield" Athena (idx 3021, extra
  "the" vs catalog 027 "Flame of Battlefield").
- "The Revenant" Calibur / "The Aircraft Mechanic" Juno
  (idx 3021, client articles vs catalog 053 "Revenant" /
  062 "Aircraft Mechanic").
- "Juno´s" (idx 3020, acute accent for apostrophe).
- "Electricity" element wording (idx 3027/3028/3040/3050,
  vs catalog "Lightning").
- "I play cause its fun." (idx 3044, grammar kept).
- OCR misread "41600%" for visual triangle-1600%
  (idx 3035, zoom wins, recorded as method note).
