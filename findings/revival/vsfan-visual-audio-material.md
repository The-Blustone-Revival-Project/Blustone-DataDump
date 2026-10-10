# VSFan curated visual, audio and intro assets

**Source scope:** `analysis/VSFan/Images`, `analysis/VSFan/Audio/Blustone`, and `analysis/VSFan/Intro.mp4`. The source directory was left unchanged. All 220 curated PNGs were reviewed as labeled contact sheets; exact relative paths, byte sizes, dimensions and SHA-256 values are in [`vsfan-image-manifest.tsv`](vsfan-image-manifest.tsv).

The manifest found two exact duplicate-file pairs: `Items/Materials/metron_fragment.png` and `Items/Metron/metron_fragment.png`, and `NPCs/Faces/lana_face.png` and `NPCs/Original/lana_full.png`. Preserve both source paths in lookups; do not interpret duplicate paths as distinct content.

## Blustone images

The 183 files under `Images/Blustone` form a curated visual-reference set, not a numeric reference database.

| Group | Count | Contents and research use |
|---|---:|---|
| `Emoji/` | 22 | Character reaction heads for Captain, Karl Steiner, Lana, Lantern, Mowgli, Nene, Rebecca, Sunny, Teddy Bomber and Tyltyl; also a lottery-mouse icon. Filenames distinguish several expressions. Useful for identity/UI matching. |
| `Hunters/Half Size/` | 22 | Half-size portraits for Acerola (`030`), Athena (`027`), Balian (`019`), Bruce Bang (`016`), Captain (`009`), Denali (`013`), Diana (`031`), Hermes (`023`), Karl Steiner (`012`), Lantern (`001`), Lapis (`017`), Levi (`015`), Locke (`014`), Metis (`007`), Mowgli (`002`), Rebecca (`021`), Riko (`024`), Robin (`018`), Sienna (`020`), Sunny (`022`), Sylvester (`006`) and Tyltyl (`004`). |
| `Hunters/Original/` | 24 | Larger portraits for the same set plus Gerard (`005`) and Hecate (`011`). Names are cross-checked against [`card-catalogue.tsv`](../../catalog/legacy-catalogue-data/card-catalogue.tsv). This is artwork coverage only; there are no stat labels or progression states. |
| `Items/` | 35 | Coupon types, Rupee/Manda/letter icons, event boxes and event item-list strips, 13 training/upgrade materials, Metron crystal/fragment, recruitment requests, and Octavia trace art. Individual icon assets do not expose item-stat values. |
| `Locations/` | 39 | 14 half-size and 25 original location illustrations covering Expedition Areas, Excavation Association and Midgard town scenes/buildings. Useful for area identity, map/theme and UI scene matching. |
| `NPCs/` | 35 | Face, half-size and full-body art for Beckhen, Clala, Dawdly, Estelle, Jack, Lana, Lottery Mouse, Pandahawk, Red, Schumann and Westfield, plus the Mysterious Woman. These are NPC/identity assets; file family alone does not prove playable-card status. |
| `Screenshots/Original/` | 6 | Six full-screen captures described below. These provide UI, economy/progression snapshots and identity evidence, but no hero base-stat tuple or monster stat table. |

### Six full-screen captures

- **`battle_screen_full.png`:** “Ready to Battle” for Blood Red Canyon, Area 40; a three-star row is shown, with an energy display `166/60`, four ally portraits versus three opponent portraits, an “Available Items” strip, and a Begin Battle cost of 6. These are screen-state values and icons, not monster HP/ATK/DEF. Hero IDs and exact game build are not established by the image.
- **`dialogue_system_full.png`:** Ornithopter Platform and Lana dialogue/options. The snapshot shows fuel `243/60` and options to cruise, view missions, talk, or leave. It documents interface wording and flow, not a maximum-energy rule.
- **`migard_lower_full.png`:** Midgard town lower view; visible balance icons read Rupees `28,202` and Manda `16`, and a tutorial/achievement bubble says “Clear Expedition Areas 15 times!”. These are a player snapshot; no account name is copied into this report.
- **`migard_upper_full.png`:** Midgard upper view; energy `198/60`, mail `6/6`, and expedition progress `282/360` stars are visible. The screenshot documents town layout and a progress UI snapshot, not current caps or catalog totals.
- **`recruitment_screen_full.png`:** Recruit result for Lantern (“First Ever Hunter”), three-star badge, Bomber / Fire labels, and a visible `1,000` currency amount. The amount’s cost/reward semantics are not established by this screenshot; no HP/ATK/DEF is shown.
- **`visualshower_shirt_full.png`:** White Island Season 2 dialogue UI. Character Jae recognizes a VisualShower T-shirt. This is a cross-title reference between the publisher’s games, not a Blustone stat source.

## Other VisualShower titles and brand assets

- `Images/Beyond the Bounds` contains 19 PNGs: Leonardo and a tower image, a small press-kit logo/icon/main image, seven press-kit backgrounds, four character assets (`lentern.png`, `mogri.png`, `nene.png`, `odri.png`), and three screenshots. The filenames and image content identify the *Beyond the Bounds* property and share some names/visual motifs with Blustone; do not assume matching card IDs or stat values from artwork alone.
- `Images/White Island` contains 14 PNGs: four hospital backgrounds, four characters, an app icon, main promo image, two screenshots, and black/white wordmarks. The VS T-shirt dialogue in the Blustone image above provides an explicit cross-title reference; these assets otherwise belong to a separate game.
- `Images/VisualShower` contains four corporate/logo variants (`CI Black`, `CI White`, `vslogo_smaller`, `vslogo`). They are branding/reference assets.

## Audio inventory

The ten supplied MP3 filenames and measured durations are:

| File | Duration |
|---|---:|
| `01 Fight Club.mp3` | 158.109 s |
| `02 Hunter Gym (Original).mp3` | 40.378 s |
| `03 Fight Club (Muffled).mp3` | 158.093 s |
| `04 Main Theme.mp3` | 69.184 s |
| `05 Suspicious Shop.mp3` | 45.143 s |
| `06 Hunter Gym (Current).mp3` | 55.909 s |
| `07 Rupee Purchase.mp3` | 0.605 s |
| `08 Defeated.mp3` | 5.557 s |
| `09 Unidentified Sound.mp3` | 1.031 s |
| `10 Dubious.mp3` | 42.648 s |

All are 320 kb/s MP3 except the short Rupee Purchase and Unidentified Sound files, which have different encoded bitrates. Metadata confirms durations only. Track names suggest UI/music cue roles; the audio itself was not independently transcribed or identified, so keep those labels as supplied filenames.

## `Intro.mp4`

The 30.186-second 1088×1920 H.264/AAC recording opens on an Android home screen, then shows the BLUSTONE “A Beyond the Bounds Story” cloud/airship loading screen. Contact-sheet samples continue to show the loading indicator at 0%; no readable stat panel or later gameplay appears in this clip. The file does not establish when it was captured or which app build was running.

## Stat-recovery disposition

These curated images and the intro clip add useful identity, content, UI, locale and scene references, but no new hero HP/ATK/DEF tuple, accessory/jewel item-instance value, or monster base-stat row. The six screenshot values are not to be copied into base-stat tables as general rules. The older APK’s parsed in-game help and its disputed jewel-set table are documented separately in [`vsfan-extracted-assets.md`](../resources/vsfan-extracted-assets.md); the 2017 captures’ encrypted game responses are analyzed in [`vsfan-packet-capture-findings.md`](vsfan-packet-capture-findings.md).
