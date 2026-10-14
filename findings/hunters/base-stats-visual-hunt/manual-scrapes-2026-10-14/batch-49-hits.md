# Batch 49 hits (idx 2401-2450)

Lane: `findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/`
Crops: `hits/batch-49-2416.png` (720x640 Train panel),
`hits/batch-49-2417.png` (1080x442 recruit plate),
`hits/batch-49-2437.png` (720x295 recruit plate).
Zooms (lane folder, provenance only): `z49_2416_badge` (Octavia
5-star Lv.1 badge), `z49_2407_ts` / `z49_2407_ts2` / `z49_2407_tsband` (Team Strength 31952), `z49_2407_lp`
(League Points 1185/12134).
OCR (lane folder): `_batch49_ocr.json` (50 frames, tesseract
`--tessdata-dir` `%TEMP%/opencode/tessdata`, `-l eng`; sparse on
art-heavy frames, verbatim where legible).

## HITs: 3/50

- idx 2416: Octavia, Second Most Popular, Lv.1, 5-star (blue badge,
  zoom-verified), Master Hunter, Strength 10713 (Train screen).
  Catalog 028 (TITLE NOTE: screen/library show Second Most Popular;
  recruit splash shows The Frost Witch; catalog Frost Witch).
- idx 2417: Recruited Silent Canine Patrone, Lv.1, 3-star
  (gold badge), Bomber + Ice, coin +1000. Catalog 033, all
  title/class/element match exactly.
- idx 2437: Recruited Maiden of Gods Akasha, Lv.1, 3-star,
  Support + Electricity. Catalog 008 (ELEMENT NOTE: screen shows
  Electricity vs catalog Lightning; title matches exactly).

## Near-hits (full numbers, hit=no per bar rules)

### Train screen without stats (level+stars but no HP/ATK/DEF/Strength)
None (2416 has Strength, hence HIT).

### Recruit menus (no level/stars/stats per hero, hit=no)
- idx 2425 (Support): Maiden of Gods Akasha / Walking Infirmary Joy.
- idx 2426 (Bomber): First Ever Hunter Lantern / Thunder Arrow Diana /
  Silent Canine Patrone / Airport Officer Gullveig.
- idx 2427 (Defense): Walking Disaster Nene / Flame of the
  Battlefield Athena / Steely Bodyguard Kain / Nature's Gift Bear /
  Robot Engineer Edward.
- idx 2428 (Offense): Immortal One Karl Steiner / Second Most
  Popular Octavia / Noble Spear Natalia (+2 cut).

### Card-detail without level/stats (hit=no)
- idx 2422: Strange Twins Lily & Lyla; sword icon labeled Class +
  red peace-sign icon labeled Elemental; 5 skill icons, names cut.

### Skill-training without hero level/stars (hit=no)
- idx 2410: Yuri's Immunity, Lv.10/40, Duration 1.80Sec -> 1.82Sec,
  items 209/2 + 1/2, Begin Training 300 silver, coins 12807.

### Same-account trails (all hit=no, names unshown)
- 2414 -> 2429 (Build Team): leader 13777 Lv.22 -> 13883 Lv.23
  (+106); anchors 7670/4435/6857 unchanged.
- 2444 -> 2448 (Hunter List 34/45): leader 15063 Lv.29 ->
  15675 Lv.MAX; 11489 Lv.13 -> 12414 Lv.17; 9655 Lv.11 ->
  10590 Lv.15; duplicate 2563 Lv.1 Locked pair persists.
- 2446 -> 2449 (Hunter List 30/48): leader 12646 Lv.15 ->
  12742 Lv.16; 7859 -> 7934; 6746 -> 6821; 6663 -> 6743;
  6387 Lv.28 Exploring -> 6485 Lv.MAX Locked; row4 trio replaced.
  UI typo on 2449: 5865 plate reads "Lorked" (sic).
- 2432 <-> 2435: altespU profile (Level 7) + Snowy Mountain village
  hub (fuel 1926/60, tickets 43/10).

### Fight-Club defensive pair (hit=no)
- 2438 + 2439: same defensive team
  22915/18847/18035/18825/20985, Team Strength 99607; 03.07
  ladder traffic vs CJK-nickname (Rank 19/3899, msgs ":(" then
  ":)") and Elysia00 (Rank 45/3551, "I told you. You definiterly
  lose." [sic], -6, Revenge queued). Ordinary traffic, no
  collusion evidence.

## OCR-vs-zoom disagreements (zoom wins)
- idx 2407: OCR League Points "7185"/12134 vs zoom crop
  `z49_2407_lp` 1185/12134 -> recorded 1185.
- idx 2407: OCR Team Strength illegible (stylized cyan) vs visual
  31952 (full frame + `z49_2407_tsband`) -> recorded 31952.
