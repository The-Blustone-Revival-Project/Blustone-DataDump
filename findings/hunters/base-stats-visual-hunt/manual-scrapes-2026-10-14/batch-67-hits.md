# Batch 67 hits (idx 3301-3350)

Lane: `findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/`
Crops: `hits/batch-67-3302.png`, `hits/batch-67-3306.png`,
`hits/batch-67-3307.png`, `hits/batch-67-3317.png`,
`hits/batch-67-3320.png`, `hits/batch-67-3321.png`,
`hits/batch-67-3325.png`, `hits/batch-67-3330.png`,
`hits/batch-67-3342.png`, `hits/batch-67-3346.png`,
`hits/batch-67-3347.png` (11 HITs, all full-frame copies).
Zooms (lane folder, provenance only): `z67_3302_badge.png`
(5-star blue badge + Lv.18 ribbon, verified 1 big + 4 small
stars) / `z67_3302_stats.png` (stat-block OCR probe) /
`z67_3306_badge.png` (4-star green badge + Lv.1 ribbon
exemplar) / `z67_3320_badge.png` (3-star gold badge + Lv.1
ribbon exemplar) / `z67_3326_head.png` (transcend header).
OCR: tesseract `--tessdata-dir` `%TEMP%/opencode/tessdata`,
`-l eng` on `z67_3302_stats.png` and `z67_3306_badge.png`
both returned empty on stylized game text — visual wins.
Write script: `_tmp67_write.py` (+ `_tmp67_work.py`, kept in
lane folder per rules).

## HITs: 11/50

### idx 3302: Knight of Swimming Pool Lawrence, Lv.18/30, 5-star (catalog 095)
- File: `Screenshot_20200916-163619_Blustone-3f2e32238ba52e7d.jpg`
  (1080x2280). Crop: `hits/batch-67-3302.png`.
- Train Teammate screen; Strength 29298; HP 2994; ATK 1341;
  DEF 1716; all 5 skills 50/50; blue badge zoom-verified
  5 stars + Lv.18 ribbon; Elemental cyan-fist icon.
- Catalog 095 title-exact (blank-name swim variant, owner
  079); only training HIT of the batch.

### idx 3306: Little Reaper Mary, Lv.1, 4-star (catalog 066)
- File: `Screenshot_2020-09-23-18-03-42-50-71a06d4badd833aa.png`
  (720x1280). Crop: `hits/batch-67-3306.png`.
- Recruited splash; Offense + Fire; coins +1000;
  OK / See Details. Screen matches catalog exactly.

### idx 3307: Master of Counterattack Monica, Lv.1, 4-star (catalog 081)
- File: `Screenshot_20200924-102842-a918d5f992dd2708.jpg`
  (1080x2340). Crop: `hits/batch-67-3307.png`.
- Recruited splash; Defense + Electricity; coins +1000;
  "Show off now!" / See Details / Okay.

### idx 3317: Prestigious Tailor Erise, Lv.1, 4-star (catalog 063)
- File: `Screenshot_20200927-094327-eadf01577dbd9e5f.jpg`
  (1080x2340). Crop: `hits/batch-67-3317.png`.
- Recruited splash; Defense + Electricity; coins +1000;
  "Show off now!". Pairs with chooser idx 3311 (same account).

### idx 3320: Nature's Gift Bear, Lv.1, 3-star (catalog 036)
- File: `Screenshot_20200929-111954_Blustone-9014791973f1aa94.jpg`
  (1080x2280). Crop: `hits/batch-67-3320.png`.
- Recruited splash; Defense + Electricity; coins +1000.

### idx 3321: Guardian of Fight Club Beckhen, Lv.1, 3-star (catalog 051)
- File: `Screenshot_2020-10-03-12-16-40-63-94cf4b70dde56334.png`
  (720x1280). Crop: `hits/batch-67-3321.png`.
- Recruited splash; Offense + Ice; coins +1000.
  Title/name match catalog 051 exactly.

### idx 3325: Defense Knight Lawrence, Lv.1, 4-star (catalog 079)
- File: `Screenshot_20201008-113726_Blustone-e98a6a3ad0e9b3d0.jpg`
  (1080x2280). Crop: `hits/batch-67-3325.png`.
- Recruited splash; Defense + Fire; coins +1000.
  Matches base catalog 079 on all four axes.

### idx 3330: White Darkness Selene, Lv.1, 4-star (catalog 068)
- File: `Screenshot_2020-10-15-12-07-10-105_com.vsh-520729d7f1978a65.jpg`
  (1080x2340). Crop: `hits/batch-67-3330.png`.
- Recruited splash; Bomber + Ice; coins +1000;
  "Show off now!".

### idx 3342: Master of Recruitment Lottery Mouse, Lv.1, 4-star (catalog 084)
- File: `Screenshot_20201225-013606_Blustone-ec1aa693e5147900.jpg`
  (1440x3040). Crop: `hits/batch-67-3342.png`.
- Recruited splash; Bomber + Ice; coins +1000;
  "Show off now!". Screen stacks title-above-name
  (title-first word order vs catalog name/title split).

### idx 3346: Runaway Bride Teresa, Lv.1, 4-star (catalog 065)
- File: `Screenshot_20201226-163420_Blustone-7cb59eb511bb163c.jpg`
  (1440x3040). Crop: `hits/batch-67-3346.png`.
- Recruited splash; Support + Fire; coins +1000;
  "Show off now!".

### idx 3347: Midgard's Finest Sword Estelle, Lv.1, 4-star (catalog 096)
- File: `Screenshot_20201227-180214-898b8c01c0646dd8.png`
  (720x1280). Crop: `hits/batch-67-3347.png`.
- Recruited splash; Offense + Fire; coins +1000;
  "Show off now!". Apostrophe-spacing artifact on screen
  ("Midgard ' s") vs catalog "Midgard's".

## Near-hits (hit=no per bar rules)

- idx 3301: fight-club Defending slot crop, Lv.MAX plate +
  Strength 27389, but hero unnamed (tight chibi crop).
- idx 3303: defensive-team strip with 5 levels + strengths +
  Team Strength 109790, but no names/titles/stars.
- idx 3326: Hunter Transcendence, Knight of Swimming Pool
  Lawrence, Lv.MAX, Strength 33732 -> 37265, fodder 0/2
  (Lv.1 Lawrence 6727 x2), items 59/40 + 209/400, cost
  40000, wallet 15362 — star rank not legible on chibi.
- idx 3311: Recruit 4-star chooser (Erise/Anemone/Junia/
  Lawrence/Monica/Kamala) — no levels or stars shown.

## Screen-type totals (recounted to 50)

- recruit 32 + hunter-list 9 + fight-club 2 + shop 2 +
  equipment 2 + training 1 + rankup-transcend 1 + story 1
  = 32+9+2+2+2+1+1+1 = 50.

## Same-account trails

- Sept-16 trio: 3301 (Defending 27389 crop) / 3302 (Lv.18
  29298 Lawrence training) / 3303 (defensive strip carries
  both 27389 and Lv.18 29298; Team Strength 109790).
- Sept-20 pair: 3304/3305 (same 31/51 Strength-sorted roster).
- Sept-24/25 recruit session: 3307-3314 + 3311 chooser
  (Monica/Erise/Lawrence recur as pulls).
- Dec-24 trio: 3338/3339 (BONUS reveal boards) / 3340
  (result grid + truncated "Bababo..." chat).

## Most valuable economy/mechanic readings

- Recruit price anchor: "One more time! 300" on every
  10/11-pull result grid (3308/3310/3312/3314/3316/3318/
  3322/3327/3331-3333/3335/3336/3340/3343); equip/gem
  boards cost 250 ("One more time! 250", 3344/3345).
- Transcendence pricing (3326): 40000 fee, fodder 0/2 same-
  hero, item gates 59/40 + 209/400, +3533 Strength
  (33732 -> 37265).
- Shop conversion event (3328/3329): "Very Successful
  Purchase" rate-up arrow 1600%; Rupee x80000 or Fuel x960
  + Veteran Point Gift Certificate x3.
- Fight-club strip (3303): 5-slot defensive team with per-
  slot Strength + Team Strength 109790 total.
- Story gate (3349): "Message from the Past" Ally 102177
  vs Opponent 120000, all-opponent-Lv.1 preview.
- Whale roster ceiling (3337): 205/231 hunters, top
  Lv.MAX 52721.

## Element / title wording tallies

- Screen element word is "Electricity" (3307/3317/3320)
  vs catalog "Lightning" for 081/063/036 — standing
  wording discrepancy, all other axes match.
- Roles seen: Offense / Defense / Bomber / Support.
- Sic list: "Midgard ' s Finest Sword" (apostrophe
  spacing artifact, 3347); truncated chats "BIG NEWS at
  the Sus..." (3331), "BIG NEWS at the Su..." (3340),
  "I need a circlmaster rn" (Discord overlay, 3323) —
  none completed by guessing.

## Non-ASCII names

- None in-game (idx 3348 is a full CHINESE client hunter
  list: 猎人名单/全职业/战斗力秩序/防御中/代表/出队/团体升级,
  Digi Wi-Fi VoWiFi status bar — first non-English client
  in this lane slice).

## Contaminants

- idx 3323: Discord overlay strip ("Blustone
  #blustone_ge...") over hunter list (brief note only).
- idx 3345: external messenger share frame ("You,
  24 December, 3:32 pm") around a genuine gem board.
- No promo art, no zero-digit runs: every recruit grid
  shows full star/level plates; no art-only crops.
