# VSFan research folder audit

Audited 2026-10-05 from `analysis/VSFan/Research/`. The source tree was left unchanged. This report condenses the useful learning, points to the original artifacts, and separates direct observations from notes, inference, and unverified data. Account/device identifiers, contact details, local usernames/paths, and named individuals in credit/contact lists are intentionally omitted.

## Inventory and best entry points

The folder has **663 files**: 584 `.txt`, 52 `.png`, 8 `.jpg`, 7 `.docx`, 7 `.pdf`, 3 `.mp4`, 1 `.md`, and 1 `.xlsx`. The largest substantive cluster is two September 2017 Blustone resource-list and parsed-package snapshots. The contents break down as:

- **Blustone — 639 files:** [API endpoint notes](<../../sources/community/raw/VSFan/Research/Blustone/API Endpoints.md>), the warned spreadsheet [Hunter Stats (BROKEN IGNORE)](<../../sources/community/raw/VSFan/Research/Blustone/Hunter Stats [BROKEN IGNORE].xlsx>), UI screenshots in `Bugs/` and `Errors/`, a `debug_strings.png`, two videos, and two extracted update snapshots.
- **Beyond the Bounds — 11 files:** four short reference documents, five story/game screenshots, and one video. These are useful for the shared setting and provenance of the “A Beyond the Bounds Story” framing, but do not contain Blustone stat tables.
- **VisualShower — 10 files:** company-history source notes, six event/company PDFs, and three office photos. They mostly establish product lineage and public appearances.
- **White Island — 2 DOCX files:** an informal overview and credits. The overview contains useful cross-project claims but also explicit guesses and dated price/rating notes.
- **LingoWinner — 1 PDF:** a 38-page company introduction, mostly localization/marketing services material; no Blustone game data was found.

The most useful files for the revival work are the Stats workbook and its paired hero-details sheet; both are preserved cell-for-cell in [vsfan-hunter-stats-raw.tsv](../hunters/vsfan-hunter-stats-raw.tsv) and [vsfan-hunter-details-raw.tsv](../hunters/vsfan-hunter-details-raw.tsv). For the protocol snapshot, start with [API Endpoints.md](<../../sources/community/raw/VSFan/Research/Blustone/API Endpoints.md>) and the two resource lists: [2017-09-04 / app 1.1.2.0](<../../sources/community/raw/VSFan/Research/Blustone/Extracted Updates/1.1.2.0/reslist_20170904165634.txt>) and [2017-09-08 / app 1.1.3.0](<../../sources/community/raw/VSFan/Research/Blustone/Extracted Updates/1.1.3.0/reslist_20170908141924.txt>).

## Hero data: promising, quarantined, zero strict credit

### What the workbook contains

Despite the filename warning, the workbook opens and has two nonempty sheets:

- `Stats`: 209 rows × 14 columns. It defines 13 fields, in order: **Strength, Life, Attack, Defense, Att Spd, CD Chance, Crit Dmg, Arm. Pen, Block Chance, Block Res, Str Elem Attr, Elem Att Res, Life Regen**. Nineteen named hunters each have a `- Base Bronze` row, but only **10 contain 13 numeric cells**; the other **9 contain literal `N/A` in all 13 cells**. Of 189 labeled rank rows, 67 are fully numeric, 22 contain 13 literal `N/A` cells, and 100 have all 13 stat cells blank. One nominal `- Max Blue` label is absent.
- `Details`: 30 named hunters with title, role, type/element, and up to five skill-name columns. The list is captured without interpreting blank skill cells in the paired raw TSV.

Rank-row population is uneven. Each cell below counts whole rows; `N/A` means every one of its 13 stat cells is the literal text `N/A`, and `blank` means all 13 stat cells are empty:

| Rank row | Labeled | Numeric | All-N/A | Blank |
|---|---:|---:|---:|---:|
| Base Bronze | 19 | 10 | 9 | 0 |
| Max Bronze | 19 | 9 | 9 | 1 |
| Base Silver | 19 | 16 | 2 | 1 |
| Max Silver | 19 | 10 | 2 | 7 |
| Base Gold | 19 | 11 | 0 | 8 |
| Max Gold | 19 | 7 | 0 | 12 |
| Base Green | 19 | 3 | 0 | 16 |
| Max Green | 19 | 1 | 0 | 18 |
| Base Blue | 19 | 0 | 0 | 19 |
| Max Blue | 18 | 0 | 0 | 18 |

Thus **67 rows (871 cells) are numeric**, **22 rows (286 cells) are all-`N/A`**, and 100 labeled rows are fully blank. There are no mixed/partially populated rank rows. The workbook stores literal values, not formulas (zero formula cells), so there is no formula-cache ambiguity. The raw TSV retains `N/A` as literal text and true empty cells as empty fields.

The 19 names map by exact unique display-name match to the base rows in the current [card catalogue](../../catalog/legacy-catalogue-data/card-catalogue.tsv). This is a high-confidence *identity crosswalk only*; it does not validate the spreadsheet's numeric data or rank semantics:

| Catalog ID | Name | Catalog ID | Name | Catalog ID | Name |
|---|---|---|---|---|---|
| `001` | Lantern | `005` | Gerard | `006` | Sylvester |
| `007` | Metis | `009` | Captain | `011` | Hecate |
| `012` | Karl Steiner | `013` | Denali | `014` | Locke |
| `015` | Levi | `016` | Bruce Bang | `017` | Lapis |
| `018` | Robin | `019` | Balian | `020` | Sienna |
| `021` | Rebecca | `022` | Sunny | `024` | Riko |
| `030` | Acerola | | | | |

### Why no values enter strict coverage

Keep the workbook and all values **polluted/unverified**. The file itself is named `Hunter Stats [BROKEN IGNORE].xlsx`; it has no cited source, capture date, game/client build, level definition, equipment state, enhancement state, or explanation of `Strength` and the `Base/Max Bronze/Silver/Gold/Green/Blue` labels. It cannot establish that “Base” means unequipped level 1, and “Bronze” cannot be translated into the current catalog’s rarity/awakening model from this file alone. Its Excel core metadata says it was created/modified by `openpyxl` on 2026-10-05; that is an export/metadata date, **not** evidence of when the underlying values were observed. The names crosswalk cleanly, but version and state do not.

The TSV is a literal extraction from every labeled Stats row. It records the original Excel row, hero cell, rank-label cell, each stat column, literal `N/A` strings, and empty stat cells as empty TSV fields. Only the 10 numeric `Base Bronze` tuples are candidate values; do not use them to claim a hero or catalog coverage milestone until an independent dated screenshot, video, source table, or reproducible game capture verifies value, rank, level, and equipment state.

The `Details` sheet is useful as a candidate name/title/role/skill index, but it has no provenance either. Preserve its exact text in the companion TSV and cross-check names/titles against the catalogue before reusing any skill wording.

## Blustone interface observations from dated screenshots

The 51 PNGs consist of one debug screen, 29 `Bugs/` captures, and 21 `Errors/` captures. Filenames timestamp most screenshots in August 2017. They document client UI/mechanics, not controlled stat measurements.

### Stat-adjacent and progression evidence

- `Bugs/Screenshot_20170812-002615_01.png`: a three-star **Emerald Canyon** stage tile. It proves the stage name and star presentation; it provides no hero attributes.
- `Bugs/Screenshot_20170813-114345.png` and `Screenshot_20170815-134824.png`: hunter-list views show collection counts `32/60` and `42/60`, combat-power-like numbers beneath portraits, lock/max badges, and class/element-like icons. The portraits are not named in these screens and the displayed numbers are not identified as base HP/Attack/Defense. Do not attach these aggregate or account-state values to individual catalog rows.
- `Bugs/Screenshot_20170813-164411.png`: Veteran Status shows **Expert 1**, **1290/2560 Veteran Points**, and benefits including Special Support Fuel +5, Fuel Recharge +7, Rupee Exchange +7, and Challenge Invitations Recharge +7. This is progression/economy context, not hero stats. A personal identifier visible in the screenshot is deliberately excluded.
- `Bugs/Screenshot_20170815-173559_01.png`: a hunter-training panel at **Lv. 11/30**, “A Sword in Each Hand,” says polishing twin swords increases attack speed. Its display reads **Attack Speed 1126.72% → 31.00%**. Treat `1126.72%` as a polluted/bugged observation, not a real base stat or valid bonus. The hunter identity is not established by the screenshot.
- The `Bugs/Screenshot_20170818-105428.png` through `...110108.png` sequence shows the **Story → Fate** screen. Its header displays account-level HP/Attack/Defense bonuses between **1% and 4%** in these captures; individual visible Fate rows show a **Health +2%** reward and a “Less than 30 sec.” condition. Visible pair/story titles include “No Spitting Anywhere,” “Ladies’ Dinner,” “Last Soldier,” “Won’t Back Down,” “Challenge,” “Promises,” “To Each Her Own Skill,” “Awkward Encounter,” “Your Scarf,” “Infamous Client,” “Take Care of the Teddies,” “Dummy Counselor,” “First Fight,” “Solid and Soft,” “His and Her Bat,” “Skin Care Enemy,” “Little Brothers,” “Midnight Prayer,” “Our Fate in the Stars,” “A Chunk of Metal,” “Opening Act: The Battle of Survi…,” “A Legendary Man,” “Groundbreaking Upgrade,” “Experienced Senior,” “Created Freedom,” “Trouble Maker’s Scale,” “Chaos! Destruction! Oblivion!,” “Sweet Bombs,” “Polar Bear Greetings,” “Idiot VS Loan Shark,” and “Stalker VS Loan Shark.” The icon portraits are not named in the relevant panels; these titles cannot safely be mapped to hero IDs from this evidence alone. Treat the header totals as one observed account state, not canonical balances.

These Fate screenshots are useful evidence that recruiting/story relationships grant passive team-stat percentages, and that the game surfaces aggregate HP/Attack/Defense bonuses separately from per-hunter attributes. Their contribution is not strict base-stat coverage.

### Combat, event, story, and UI context

- `Bugs/Screenshot_20170820-223928.png` shows a battle tutorial with a 389-HP enemy bar, a turn/timer dial, floating damage numbers, and the line “Now’s the time to use my emergency cooking skills!” The screen is dimmed by the tutorial overlay; damage values are not tied to named hunters or controlled conditions.
- `Bugs/Screenshot_20170820-224858_01.png` shows an event panel titled **Collect Hunter Traces**. It says “The Lottery Mouse collects hunters’ traces” and offers one- and three-trace collection options. This is event UI context only; the button labels do not establish an item’s exchange price.
- `Bugs/Screenshot_20170820-225950_01.png` shows **Teddy Bomber’s Trace**, quantity 30, with descriptive text about a bomb hidden in a teddy bear. It describes a collectible/event item, not the corresponding hunter’s combat stats.
- The `Bugs/Screenshot_20170820-231349_01.png` / `...231410_01.png` captures show new story entries for Gerard (“Exposing a Secret Training S-essi…”) and Robin (“prophecy? warning?”). `...231425.png` shows a story list with “Midgard’s Story” and several Sienna entries, including “Towards the ultimate weapon,” “Sienna Cannon Custom 2,” “A cautious approach,” “A difficult world to find friend,” and “Find good friends.” `...231444.png` shows Sienna discussing the Sienna Custom Cannon 2 costume in Black Rock Mountain. This helps map story and costume UI, but the captures are not stat panels.
- `Bugs/Screenshot_20170814-080541.png` is an unlabeled full-screen hunter illustration. It may support later visual identity matching, but this audit did not assign the portrait a name.

### Failed reference requests

The 21 `Errors/Screenshot_20170817-012605.png` through `...012743.png` screenshots form a rapid sequence of “Request failed!” popups while the client is on its splash/loading screen. The named operations visible are `ReferenceSync` Stage, Card, Item, Supply, Monster, StageMonster, Dialog, Scenario, Level, CardRankUp, CardEnhancePrice, CardChain, Quest, Shop, Extra, and Area; callbacks also name Supply, Quest, NPC, Gacha, CardBook, and BattleLeague. A separate popup identifies DailyQuest. This shows which initialization/reference calls were failing in that captured session; it does not establish why. The sequence overlaps the packet-capture index in [API Endpoints.md](<../../sources/community/raw/VSFan/Research/Blustone/API Endpoints.md>), so it should be treated as corroborating UI evidence, not a second independent schema source.

### Debug screen

`Blustone/debug_strings.png` exposes a development/debug overlay with project `_SR (1073)`, engine tag `Peppermin_170711_1430`, Android 7.1.1, English locale, and 1080×1920 physical / 640×1136 logical display. It also shows package/storage/memory figures that may be debug-account/device-specific. The screenshot includes a device identifier/network data; those values are not repeated here. The engine tag suggests a July 2017 build, but the image file itself has no capture timestamp, so treat that date as an inference from the tag.

## Protocol and versioned resource evidence

### Packet-capture summary

The local [API Endpoints.md](<../../sources/community/raw/VSFan/Research/Blustone/API Endpoints.md>) says its endpoint order was transcribed from two packet captures dated **2017-09-05 (app 1.1.2.0 / 1120)** and **2017-09-08 (app 1.1.3.0 / 1130)**. The raw PCAP files are not in this research folder, so this is a second-hand summary rather than direct verification here.

The note distinguishes platform calls to `pv-prd.vshower.com` from game calls to `sr-prd.gshower.net`, and asset downloads from a CloudFront host. All calls were HTTP POST; platform launcher/tracker requests are described as plain form, account/game bodies as encrypted, and assets as package GETs. It records:

- `/pv_launcher/check_acceptable`, `/shared_secret/Exchange`, encrypted `/account/Login` (512-byte request), and tracker reports.
- Reference loads for Extra, Area, Stage, Card, Item, Supply, Monster, StageMonster, Dialog, Scenario, Level, CardRankUp, CardEnhancePrice, CardChain, Quest, Shop, NPC, Gacha, CardBook, Battle, Abyss, and (in 1.1.3.0) CardOvercome; plus lobby inventory/instance calls, scenarios, daily quests, supply refresh, and mission/tutorial calls. The source file retains the complete ordered path list.
- `/tuto/Clear`, `/mission/Start`, and `/mission/Complete` appear only in the 1.1.2.0 capture. `/reference/GetCardOvercome` appears only in 1.1.3.0. The three 1.1.2.0-only requests are reported as 96, 160, and 256 bytes, respectively. It says the other game bodies were generally 80 bytes.
- Asset packages use names such as `C002_20170811151651.pkg`. The versioned resource manifests give an item count, aggregate bytes, per-package timestamp/size/hash fields. Hashes are intentionally not recopied here; use the source manifests for integrity work.

This source’s endpoint vocabulary overlaps the repo’s native-string, parser, and route work. Cross-check each path/shape against the native callbacks before implementing behavior; a packet list alone does not define response JSON.

### September resource deltas and package families

The 1.1.2.0 manifest is stamped `20170904165634` and lists **140 packages / 379,438,483 bytes**. The 1.1.3.0 manifest is stamped `20170908141924` and lists **149 packages / 385,496,169 bytes**. By package name, 1.1.3.0 adds `UI_BATTLE`, `UI_CHALLENGE`, `UI_CHA_GET2`, `UI_ENHANCE2`, `UI_ENHANCE_NEW`, `UI_ICON`, `UI_ITEM`, `UI_ITEM_CHA`, `UI_PACKAGE`, `UI_SELECT`, and `UI_SHOP`; removes `UI_NEW` and `UI_NOUSE2`; and updates eight shared package names: `DIALOGUE-EN`, `DIALOGUE-JP`, `DIALOGUE-KO`, `LAYOUT-EN`, `LAYOUT-JP`, `LAYOUT-KO`, `LEVELING`, and `UI_CHA_GET`. Among the 138 names shared by both manifests, 130 extracted `.pkg.txt` payloads have identical SHA-256; eight differ. This is useful version-delta evidence, not proof that identical packages contain no relevant data.

Package-name families include `C###` hunter art/content with `_EFT`/`_SND` companions, `M###` monster assets, `N###` map/area assets, `ST###` stage assets, UI/animation packages, language-specific `DIALOGUE-*` and `LAYOUT-*`, plus `GACHA`, `LEVELING`, `WEATHER`, `MAP_ZONE_1`, and `SND_CDN`. The naming is a package classification, not a verified database schema. The `_info.txt` sidecars are MediaInfo-style file metadata. Most `.pkg.txt` files are strings/raw-container extractions containing media signatures and non-readable binary fragments; package name alone must not be mistaken for a source table.

The two extracted `LEVELING.pkg.txt` payloads contain a readable `#ID,Name,PreFix,` header, repeated `STI001`…`STI006`/`STI099`/`STI900`…`STI903` strings, and numeric-looking IDs/tuples amid binary fragments. The 1.1.3.0 carving has additional references (including 503, 512, 523, 527–531) relative to the earlier snapshot. Because the surrounding table boundaries/field semantics are not intact, do not treat these fragments as hero stats or infer a growth formula from them. For already established local `LEVELING.jet` analysis, see the calibration notes in [archived-hunter-database-2019.md](../hunters/base-stats-visual-hunt/archived-hunter-database-2019.md) and the current `AGENTS.md` constraints.

## Related titles and company history

These materials help establish lineage and possible narrative/visual leads. They do not provide Blustone stat coverage.

- The local `VisualShower/Sources.docx` notes a company timeline: VisualShower startup in 2004; company incorporation in 2007; early mobile-engine/middleware development; `Beyond the Bounds` launch in 2010; `Beyond the Bounds: Escape` in 2013; `Beyond the Bounds: The Secret of Blue Stone` in January 2014; and a global PV gaming platform in November 2015. The same document lists appearances at events including Dubai World Game Expo 2010, GDC 2012/2014, E3 2013/2014 Korea Pavilion, G-Star 2011/2014, and TGS 2010. Treat this as a compiled company-history note, not an independent primary source.
- `VisualShower/Unknown E3 Korean Pavilion Brochure.pdf` and `...Company Descriptions.pdf` present **Beyond the Bounds: The Secret of Blue Stone** as a VisualShower-developed mobile/console/online/arcade/handheld RPG/adventure and describe it as a collection-and-battle game combining RPG and adventure elements, with story, animation, and interactive gimmicks. The brochure says it was available through Korean app markets at the time. These are exhibitor-pamphlet claims, useful for product positioning, not balance data.
- `VisualShower/2014 E3 Gameshow Korea Pavilion.pdf` presents a **Beyond the Bounds: Green Light** brand entry and says the series was being expanded from adventure toward collection/battle and MMORPG genres in a steampunk-fantasy setting. This is dated promotional context; do not assume “Green Light” is a released Blustone mode.
- The local `White Island/Overview.docx` is informal and explicitly speculative in places. It describes White Island as exploration plus story, says Beyond the Bounds preceded Blustone and used the White Script Engine, and characterizes Blustone as a more open-ended event/social clicker/RPG with character backstories. It says Blustone’s assets/story derive from `BTB: The Legend of Blue Stone`. These are leads to compare against local assets and dialogue, not confirmed engine or monetization facts. Historical prices/ratings in that note are stale and omitted.
- `Beyond the Bounds/BTB Characters.docx`, `BTB Locations.docx`, and `BTB Walkthrough.docx` document a small puzzle-game section at **Nameless Snowfield**. The walkthrough involves Lantern and Nene, a Dodo, an aerodynamics book, parachute repair using a fruit skin and cooled strands, and meeting Albert/using a strange machine. `BTB Characters.docx` says Lantern is spontaneous and can talk to animals, Nene mocks people who do not read, the Dodo has lost its glasses, and Albert is looking for Edison for Lady 4994. These are short-game-specific story notes; reuse as Blustone lore only where confirmed by its own dialogue/resources.
- The related BTB `.jpg` images show newspaper/page-like game art and promotional material. The 70.5-second Unicode-named MP4’s sampled frames show snowy establishing shots and animated story scenes; file metadata gives a 2011-06-08 creation timestamp. No readable combat stats are present.
- `VisualShower/2010 Dubai World Game Expo Report.pdf` and the 2014 ChinaJoy post-show report are broad event reports; the latter lists VisualShower among Korean exhibitors. The remaining 2013/2014 pavilion brochures and LingoWinner deck are corporate/exhibitor material. They may help provenance searches, but this audit found no additional Blustone combat tables in them. VisualShower office photos are generic interiors.
- BTB/White Island credit documents contain production credits. Names were not re-copied because they are not needed for the revival or stat task. The same privacy rule applies to contact details in event PDFs and source notes.

## Videos and limits of this pass

Three local MP4s were inventoried and sampled by frames across their durations:

- `Blustone/Blustone Launch Ceremony.mp4` is about **612 seconds**. Sampled frames show a dim event/party setting and monitors, but no readable game demonstration or stat panel. No usable mechanics/stat evidence was recovered from the sampled video; its event name alone does not independently date the footage.
- `Blustone/Parallax Break.mp4` is about **47 seconds**. Frames show Blustone running in a narrow phone capture with background/parallax transitions and UI overlays, but no readable base-stat data. The “Break” filename does not itself establish a reproducible defect.
- The BTB video described above is about **71 seconds**, animation/story footage only.

These videos were visually sampled, not speech-transcribed. Any spoken historical claims remain unresolved unless someone can provide a reliable transcript/audio review. This is not a claim that the entire event recording has been exhaustively interpreted.

## Duplication, low-value material, and next work

- **Keep both resource versions.** They are mostly duplicates, but the manifest delta is meaningful: 11 new package names, two removed names, and eight modified shared packages. The 130 identical common payloads are redundant for repeated reading once their hashes are established, but remain useful as version-specific provenance.
- The 1.1.2.0 parsed folder contains a `.DS_Store` artifact and a duplicate `LAYOUT-EN.xml.txt` view of `LAYOUT-EN.pkg.txt`; neither adds a second independent source. The `_info.txt` files are metadata sidecars, not game data.
- The 21 failure screenshots repeat the splash background but each advances a different failed operation; keep the sequence or the transcribed operation list. The story/Fate captures overlap visually but show different bonuses and pair titles; retain the sequence as one account-state snapshot.
- The broken-warning workbook is the only substantial numeric hunter candidate surfaced in this directory. The images give story/fate bonuses, CP-like list numbers, and one clearly corrupted attack-speed display, but none is a valid named, level/rank/equipment-controlled base-stat reading.
- Next high-value follow-up is to trace the workbook’s origin or find independent in-game screenshots for its 19 Base Bronze rows, then establish what Bronze and Base mean and whether the values are unequipped. Separately, recover a structured `LEVELING` source rather than interpreting strings-carving fragments; review the full Blustone launch video/audio if reliable transcription becomes available; and cross-map story-pair portraits only with independent identity evidence.

**Outcome for the active stats goal:** this folder contributes **zero strict hero, jewelry, or monster base-stat credit** at present. It adds 10 numeric but polluted/unverified Base Bronze tuples and nine `N/A` rows across a 19-hero candidate roster, a 30-hero metadata/skill list, protocol/version history, progression/Fate bonuses, and several visual/mechanics leads. Keep it separate from the independently sourced numeric rows in the active coverage tracker.
