# Polluted and state-ambiguous hero observations

**Purpose:** Preserve raw hero values visible in public videos/screenshots when
identity, rank, level, equipment, awakening, jewel, or buff state is missing or
mixed. These records can inform later rebalancing estimates. They are a
**secondary evidence track and never count toward the 70% completion targets**
unless a separate source later establishes every required base-state condition.

Do not normalize across levels/ranks, estimate missing fields, or subtract an
adjacent green number unless its meaning is proven. Keep the source locator and
record exactly what is legible plus what remains unknown.

## Named archive tuples with missing baseline context

The archived Japanese hunter database exposes named numeric profiles but does
not print the level or establish whether listed equipment is applied. Preserve
these as provisional rebalance anchors: 62 numeric profile rows crosswalk to
62 unique catalog IDs, including 58 additional IDs beyond the previously logged
Lapis (`017`), Hermes (`023`), Heidi (`044`), and Beckhen (`051`) evidence.
Their 13-field readings, archive-index coverage, and per-row source locators
are in [`archived-hunter-database-2019.md`](archived-hunter-database-2019.md)
and [`archived-hunter-database-2019.tsv`](archived-hunter-database-2019.tsv).
Beckhen (`051`) appears in the archive as a cross-source check against an
independently captured Lv.30 row. Santa Clauster (`042`) and Tyltyl (`004`,
`026`) use documented Japanese name/title matches. One profile has only
placeholder readings. None of the newly harvested pages resolves level or gear
state, so they add no strict base-stat credit.

## VSFan workbook stat candidates — source context unresolved

- **Source:** `analysis/VSFan/Research/Blustone/Hunter Stats [BROKEN IGNORE].xlsx`, `Stats` sheet. The source filename itself says `BROKEN IGNORE`; no original author/source citation, app version, level, equipment state, or verification trail was found in the supplied file.
- **Raw layout:** 19 hero sections with up to ten rows (`Base/Max Bronze/Silver/Gold/Green/Blue`) and 13 stat columns (`Strength`, `Life`, `Attack`, `Defense`, speed and combat modifiers). Of 189 labeled rank rows, 67 are fully numeric, 22 are all-`N/A`, and 100 are fully blank. Only 10 of the 19 `Base Bronze` rows are numeric; nine are all-`N/A`. The extracted copy is [`vsfan-hunter-stats-raw.tsv`](../vsfan-hunter-stats-raw.tsv), preserving source cells, row labels, blank cells and literal `N/A` entries. The `Details` sheet separately lists 30 role/type/skill summaries; its values are also source-uncorroborated.
- **Identity crosswalk:** All 19 `Stats` names match a unique current base-card catalog name: Acerola (`030`), Balian (`019`), Bruce Bang (`016`), Captain (`009`), Denali (`013`), Gerard (`005`), Hecate (`011`), Karl Steiner (`012`), Lantern (`001`), Lapis (`017`), Levi (`015`), Locke (`014`), Metis (`007`), Rebecca (`021`), Riko (`024`), Robin (`018`), Sienna (`020`), Sunny (`022`) and Sylvester (`006`). All 19 also appear in the 2019 Japanese archive table, but those profile rows omit level/equipped state and do not validate this workbook's labels or numeric values.
- **Cross-source check:** A provisional field-name comparison (`Life`↔HP, `Attack`↔ATK, `Defense`↔DEF) found no exact three-field numeric match between any workbook rank row and the same hero's 2019 archive profile. This does not show which source is wrong or authorize a conversion; the versions and progression/equipment states are unknown.
- **Raw readings:** The populated rows include `Life` / `Attack` / `Defense` alongside Strength and modifiers, but `Base`/`Max` and color-grade meanings are not defined by the workbook. Values span multiple apparent progression rows; do not select a row as the default baseline or normalize/merge it with the Japanese archive.
- **Status:** Preserve as quarantined rebalance hypotheses only. The warning filename and missing provenance are material; these rows do **not** count as strict hero base stats, jewelry, or monster coverage.

## VSFan stat-adjacent UI observations without hero base tuples

- **Broken training-panel stat read:** `analysis/VSFan/Research/Blustone/Bugs/Screenshot_20170815-173559_01.png` is a Training panel at `Lv.11/30` for an unnamed hunter, “A Sword in Each Hand.” The visible text says polishing twin swords increases attack speed; the display reads `Attack Speed 1126.72% → 31.00%`. The first token is implausibly large and likely corrupted/UI-bugged. Identity, rank, gear, item level and actual field semantics are unknown. Preserve both raw numbers as polluted; do not use either as a base value.
- **Unmapped roster scores:** `Bugs/Screenshot_20170813-114345.png` and `Bugs/Screenshot_20170815-134824.png` show hunter-list counts `32/60` and `42/60` with numeric values below portraits, but no named identity or explicit stat label. Portraits and numbers are not assigned to catalog rows or to Strength/HP/ATK/DEF. See the full screenshot inventory in [`vsfan-research-material.md`](../../revival/vsfan-research-material.md).
- **Account Fate bonuses, not individual base stats:** The VSFan Fate Story screenshot sequence shows account/header HP/Attack/Defense bonus percentages from 1% to 4%, and one visible `Health +2%` Fate reward with a `Less than 30 sec.` condition. Most pair portraits are not named in these panels. Keep these as account/story modifier context only; do not allocate the bonus to a hero or subtract it from a stat tuple.

## Identity-uncertain hero image leads (no numeric readings)

The user asked that unclear heroes be documented even when no stat can be
recovered. These image-only records preserve source and visual context for
future portrait matching. They are not assertions that every pictured figure
is a catalog hero, and they carry no stat or completion credit.

### Reddit memorial gallery profile identities (no numeric readings)

- **Source:** Three `fluger69` posts in [r/Blustone](https://www.reddit.com/r/Blustone/comments/15yxj4j/i_have_a_ton_of_images_of_the_characters_ill_be/), [part 2](https://www.reddit.com/r/Blustone/comments/15yxjp9/i_have_a_ton_of_images_of_the_characters_ill_be/), and [part 3](https://www.reddit.com/r/Blustone/comments/15yxkae/i_have_a_ton_of_images_of_the_characters_ill_be/), galleries of 20/20/17 images visually navigated on 2026-10-05.
- **Readable named profile screens:** Part 1: Alia (`070`), Lottery Mouse (`084`), Judith as Red Shadow (`067`) and Florist Lady (`087`), Harley as Man of Justice (`046`) and Florist (`088`), and Juno (`062`). Part 2: Kamala (`083`), Katrina (`090`), Bella (`075`), Lily & Lyla (`047`), Monica (`081`), Lawrence (`079`), Papillon (`043`), Blondie (`077`), Selene (`068`), Dino (`054`), Patrone (`033`), Metis (`007`), Sienna (`020`), Clara (`089`), Leon (`074`), Leon (Summer) (`094`), Westfield (`080`), Teresa (`065`), and Teresa (Halloween) (`078`). Part 3: Joy (`035`), Therapy (`050`), Akasha (`008`), Gullveig (`039`), and Teddy Bomber (`025`). Visible labels/titles and mapping notes are in [`reddit-memorial-galleries.md`](reddit-memorial-galleries.md).
- **What is visible:** Hero art, profile labels, class/element icons, skill icons, and some recruit/skin-success art. No numeric hero stats, item/jewel stats, or monster-stat panel appears in the readable frames. Some part-3 frames briefly remained blurred/loading; their contents stay unknown.
- **Unknown:** Progression, level/rank, awakening, gear/jewel state, and numeric stats for all these displayed profiles; catalog identities for other art-only figures.
- **Status:** Identity-only supplement for future visual matching. It supplies no numeric polluted row and no coverage credit.

### AppStorio iPhone screenshots 1–2, identities unresolved

- **Source:** [AppStorio archived Blustone listing](https://blustone.appstor.io/), iPhone screenshots 1–2 as rendered in the listing page on 2026-10-05. The listing reports version 2.8.0.1; the individual screenshot capture build is not established.
- **What the inspected pixels show:** Screenshot 1 is a battle/promo montage with multiple chibi hunters; screenshot 2 is the snowy village/hub with several characters. The image labels do not name the characters.
- **Raw stat readings:** None attributable to an individual hero. A small `3100` token appears in screenshot 1's upper HUD area, but its field and subject are unclear and are not recorded as a stat.
- **Unknown:** Character IDs for the visible portraits, exact screenshot build, and the meaning of the unlabeled HUD token.
- **Status:** Identity-only visual leads. Do not assign hero IDs from appearance alone or count these frames toward any threshold.

### Blustone 2 launch-art portraits, identities unresolved

- **Sources:** [GameApps.hk launch announcement](https://www.gameapps.hk/news/30971/RPG-Blustone-2), all six embedded images (2018-11-22); [4Gamer Blustone 2 screenshot gallery](https://www.4gamer.net/games/442/G044286/screenshot.html), images 001–008 (2018-12-03); [mob.org Blustone 2 listing](https://mob.org/en/android/games/g-blustone_2_anime_battle_and_arpg_clicker_game), all four images reopened on 2026-10-05; [TapTap Blustone listing](https://www.taptap.io/jp/app/49376), six-frame carousel checked on 2026-10-05 (capture build unknown); [BrowserCam listing](https://www.browsercam.com/apk/com.vshower.prd_sr/), all three promotional screenshots (version 2.0.5.1 listing, 2018-08-22 update).
- **What the inspected pixels show:** Character collages with multiple distinct portraits and chibi sprites; a voice-actor promo panel labeled `拉娜` (rendered as Lana) and Rie Takahashi; story/guild scenes; and battle-screen montages. mob.org repeats the logo collage, hero art, and battle imagery. TapTap adds a broad hunter lineup and a village screenshot, but the visible characters have no name/stat labels; its two missing frames remain unknown. BrowserCam adds a three-image older-version listing: hero promo art, battle montage, and fishing scene. None provides individual stats or an identity crosswalk. These promotional images do not prove that every portrait maps to the later 2.8.0.1 catalog.
- **Raw numeric stat readings:** None confidently attributable to an individual hero. The guild screenshot has guild-level figures, and the battle montage only shows transient combat UI; neither is a hero stat observation.
- **Unknown:** Names/IDs for most portraits, whether duplicate art across the two galleries is the same unit/skin, and version/catalog mapping.
- **Status:** Identity-only matching lead. Do not assign catalog IDs from appearance alone or count it toward any 70% threshold.

### Uptodown story-character portraits, identities unresolved

- **Source:** [Uptodown Blustone 2 listing](https://blustone-2.en.uptodown.com/android), gallery screenshots 1 and 4; full-size gallery overlay visually inspected on 2026-10-05. The listing advertises version 2.8.0.1, but the capture build is not shown in the screenshots.
- **What the inspected pixels show:** Screenshot 1 has a light-brown-haired male character in a red/black coat speaking in the snowy `Unknown Snowfields`; screenshot 4 has a dark-haired, cat-eared woman riding or standing with a large pale beast in the same story setting. Dialogue speaker labels appear as `???`.
- **Raw stat readings:** None.
- **Unknown:** Both character identities/catalog IDs, whether screenshot 4's beast is a separate monster or mount, and the screenshots' exact game build.
- **Status:** Identity-only visual leads for portrait matching. Do not assign IDs from appearance alone or count toward any completion threshold.

### Bilibili snowy story preview, identity unresolved

- **Source:** [Blustone2](https://www.bilibili.com/video/BV173JM6iEzc/) by `Takane_Manaka`, posted 2026-06-14; the accessible preview was sampled through about 01:01 on 2026-10-05. The video is 4:17, but a sign-in dialog blocks the remaining frames.
- **What the visible frames show:** Around 00:24, a server-selection screen says “This is the server I developed.” Around 00:50, a light-brown-haired male in a red/black coat speaks in a Snowfields scene; a small penguin-like creature appears nearby. Speaker identity and creature ID are not shown. The developer-server label means these frames are not treated as original-server stat evidence.
- **Raw stat readings:** None.
- **Unknown:** Character/catalog identity, monster ID, scene/build provenance beyond the visible server-selection statement, and any later video content.
- **Status:** Visual-only identity lead. Do not assign catalog IDs or count toward base-stat coverage.

## Observations

### Dumble (`048`), Lv.1 training card; power only

- **Source:** Naver post [“블루스톤(근황)”](https://blog.naver.com/1gktnrn/221270079446), posted 2018-05-07; photo viewer image 1 of 2, visually inspected 2026-10-05.
- **Visible identity/context:** Korean display name `기이한 노인 덤블` (“Strange Old Man Dumble”), exact catalog match `048`; `Team Training` screen, `Lv.1`, `Intermediate Hunter` label.
- **Raw value:** `전투력` / battle power **2,183**.
- **Unknown:** HP/ATK/DEF, weapon/armor/accessory/jewel state, and exact build/version. The separate 2019 archive profile lists Dumble at 3★ draw with combat-power token 9,322, but its level/gear state is unknown and the score is not reconciled with this Lv.1 screenshot.
- **Status:** Named, level-known power observation only; not an HP/ATK/DEF tuple and no strict coverage credit.

### Naver hunter-list number tokens, catalog identities unresolved

- **Source:** Naver post [“블루스톤”](https://blog.naver.com/1gktnrn/221205850161), posted 2018-02-10; photo viewer image 1, visually inspected at 80–144% on 2026-10-05.
- **Visible context:** `Hunter List`, count `32/72`; 12 numeric tokens appear under four rows of three portraits. A fifth portrait row is visible, but its numbers are cut off.
- **Raw row-major tokens:** `18,597 / 17,077 / 9,754`; `4,288 / 15,501 / 14,755`; `14,036 / 12,155 / 6,119`; `6,055 / 5,959 / 5,330`.
- **Unknown:** The numeric field is not labelled in the captured crop; hero IDs/names, levels/ranks, awakening, gear/jewels, lower-row values, and version remain unknown. Treat the values as unlabeled roster scores, not Strength or HP/ATK/DEF.
- **Status:** Group-level polluted evidence for future portrait matching only; no catalog mapping or coverage credit.

### Bright (`049`), recruit-result art only

- **Source:** Naver post [“블루스톤[근황]신규헌터!!”](https://blog.naver.com/1gktnrn/221281674595), posted 2018-05-22; first photo-viewer image, visually inspected 2026-10-05.
- **Visible identity:** Recruit-success card names `성냥팔이 소년 브라이트` (“Little Match Boy Bright”), matching catalog `049`.
- **Stats/context:** No HP/ATK/DEF, Strength, level, or item panel is visible.
- **Status:** Identity-only visual reference; no numeric observation or coverage credit.

### Therapy (`050`), recruit-result art only

- **Source:** Naver post [“블루스톤(3성뽐음)”](https://blog.naver.com/1gktnrn/221308021615), posted 2018-06-27; photo-viewer image 1, visually inspected 2026-10-05.
- **Visible identity:** `마성의 물리치료사 테라피` (“Diabolic Physiotherapist Therapy”), a three-star Support / Ice hunter, matching catalog `050`.
- **Stats/context:** No HP/ATK/DEF, Strength, level, or equipment panel is visible.
- **Status:** Identity-only visual reference for future image matching; no numeric observation or coverage credit.

### Unmapped Korean name, `시계초` (catalog ID unknown)

- **Source:** [펩시 — 블루스톤 헌터 각성](https://www.youtube.com/watch?v=Y2nxj-YwI5I), approx. 00:52; browser inspected 00:20, 00:52, and 01:07 on 2026-10-05.
- **Visible frame:** Hunter training/detail panel. Name is best read as `시계초`, but it is not mapped to an English catalog ID.
- **Raw values:** Lv.1/30; Strength 27,155; HP 3,021; ATK 1,144; DEF 1,671.
- **Related frame:** At approx. 01:07, Awakening panel shows Strength 27,155 → 28,502 and a 50,000 currency cost.
- **Unknown:** Catalog identity; star/rank and awakening state at the detail frame; gear, jewels, skills, and other modifiers; whether Lv.1 totals are base.
- **Status:** Polluted/partial. Do not count as base coverage.

### Natalia (`037`), training comparison

- **Source:** [Caragublu — Blustone Game Guide Tips & Trik](https://www.caragublu.com/2018/12/blustone-game-guide.html), embedded image titled `Cara Meningkatkan Level Hunter Blustone`, image viewer 2 of 7; direct image filename `Blustone Train Hunter.jpg`.
- **Visible frame:** `Train Teammate`; named hunter **Natalia**, title “Noble Spear.” Left pane shows Strength **2,480**, `Lv. 1`, and `Experienced Hunter`; right pane shows Strength **3,323**, `Lv. 30`, and the `Advance` button. A star insignia is visible; exact rank interpretation is not relied on here.
- **Unknown:** Whether the two panes share identical rank, equipment, jewels, skills, or other modifiers; HP/ATK/DEF; whether either Strength is nude/base.
- **Status:** Polluted/partial Strength observations only. Do not infer growth or count base coverage.

### Identity unknown, equipment-upgrade screen

- **Source:** [Caragublu — Blustone Game Guide Tips & Trik](https://www.caragublu.com/2018/12/blustone-game-guide.html), embedded image titled `Cara Upgrade Equipment pada Blustone`, image viewer 6 of 7; direct image filename `Upgrade Equipment.jpg`.
- **Visible frame:** `Upgrade Equipment`, with nine visible equipped-slot nodes labeled Lv.6, Lv.6, Lv.25, Lv.6, Lv.20, Lv.20, Lv.8, Lv.8, and Lv.8. `Apply Set` shows two set icons. The bottom visible stat line reads Strength **18,244** with an adjacent green **+4,186**.
- **Unknown:** Hero identity, level/rank, the equipment-to-slot mapping, whether `+4,186` is a gear delta or another comparison, HP/ATK/DEF, and any other modifiers.
- **Status:** Polluted/partial; preserve both tokens literally. Do not subtract the green number or count base coverage.

### Unidentified hunter, advancement comparison

- **Source:** [Caragublu — Blustone Game Guide Tips & Trik](https://www.caragublu.com/2018/12/blustone-game-guide.html), embedded image titled `Cara Meningkatkan Bintang Hunter Blustone`, image viewer 3 of 7; direct image filename `Blustone Hunter Adcance.jpg`.
- **Visible frame:** `Advancement Match`; the same-looking hunter begins at `Power Upgraded` **2,628** in both example panes. The left pane shows **2,628 → 3,068**; the right pane shows **2,628 → 3,947**. Visible fodder portraits carry Power values **1,939**, **1,971**, and **2,220**.
- **Unknown:** Hunter identity, exact target rank/level, which material/fodder choice explains each result, equipment/jewels/skills, and how displayed `Power Upgraded` relates to Strength or HP/ATK/DEF.
- **Status:** Polluted aggregate comparisons only; do not convert to core stats or count base coverage.

### Bear (`036`), transcendence comparison

- **Source:** [Caragublu — Blustone Game Guide Tips & Trik](https://www.caragublu.com/2018/12/blustone-game-guide.html), embedded image titled `Blustone Cara Transcendence Hunter`, image viewer 5 of 7; direct image filename `Blustone Hunter Transcendence.jpg`.
- **Visible frame:** `Hunter Transcendence`, title “Nature's Gift,” named **Bear**. Strength reads **3,425 → 3,969**. The selected identical Bear fodder reads `Lv.1`, Strength **2,568**. The screen states identical hunters of 3★ or above can be used as fodder.
- **Unknown:** Target Bear's level/rank/gear/jewels/skills and whether the visible Strength is otherwise modified; no HP/ATK/DEF.
- **Status:** Identified but progression-contaminated Strength values only; not base coverage.
- **Additional polluted roster token:** The [Naver hunter-list screenshot](https://blog.naver.com/1gktnrn/221263609574) includes a Bear portrait with `Lv.MAX` and numeric token **12,213**. The portrait match to card `036` is likely but the number's field meaning and equipment state are not shown; do not call it Strength or a base stat.

### Immortal One Karl Steiner

- **Source:** [The Radiant — Blustone review / recruit 10 hunters](https://www.youtube.com/watch?v=xO38bbWThF8), approx. 07:24.
- **Raw values:** Lv.30; Strength **3,201**.
- **Unknown:** Rank, equipment, jewels, other modifiers; no HP/ATK/DEF tuple.
- **Status:** Auxiliary Strength only; not base coverage.

### Generic “Amateur Hunter” (catalog identity unknown)

- **Source:** [Errorflame gamer — Blustone episode 1](https://www.youtube.com/watch?v=9fUxOnlmwxg), approx. 22:00.
- **Raw values:** Lv.13; Strength **377**.
- **Unknown:** Catalog identity, rank, equipment, jewels, other modifiers; no HP/ATK/DEF tuple.
- **Status:** Polluted/partial; not base coverage.

### FAQ image 8 orphan card (catalog identity unknown)

- **Source:** [FAQ image 8](../../../datasets/hunters/observed-stats/found/faq-image08-unidentified-card-equip-KO.png), credited in the FAQ to Aeku; transcription in [`analysis/catalogue/stats/010.md`](../../../datasets/hunters/observed-stats/010.md).
- **Raw values:** White stat fields read Strength **23,847**, HP **2,866**, ATK **1,522**, DEF **1,103**, Attack Speed **8.00**. Green adjacent values read `+4047`, `+221`, `+126`, `+110`, `+1.72` respectively.
- **Base-state interpretation:** The white/green layout matches Beckhen's FAQ image 17, where white Strength **24,068** plus green gear delta **6,291** equals the separate card-page Strength **30,359**. By the same UI convention, this orphan's white HP/ATK/DEF values are a likely gear-removed stat anchor. Confidence is high for the printed numbers and medium for transferring the UI interpretation to this second card.
- **Identity-search result:** Exact-number web searches pairing `23847`, `2866`, `1522`, and `1103` with Blustone terms returned unrelated numeric tables; no duplicate image or character name was found.
- **Visible context:** Weapon Lv.40, armor Lv.20, accessory Lv.20, and six jewels at Lv.5–Lv.10. Hero level, rarity/rank, awakening, and catalog identity are not shown.
- **Status:** Anonymous base-state tuple for rebalance estimates only. It is not attributable to any catalog row and does not count toward hero coverage.

### Naver max-level hunter list (multiple identities unresolved)

- **Source:** [Naver “Recent status [Blustone]”](https://blog.naver.com/1gktnrn/221263609574), 2018-04-28; the complete embedded image was opened in Naver's photo viewer and checked at 144% zoom on 2026-10-05.
- **Visible values:** Header reads Hunter List `55/114`. Twelve numeric tokens are legible in four rows: `18,228 / 17,287 / 1,234`; `535 / 19,069 / 16,035`; `15,759 / 16,081 / 12,463`; and `12,213 / 6,153 / 6,086`. Visible portrait badges read `Lv.MAX`. Korean status labels include `방어 중` (defending), `리더` (leader), `탐사 중` (exploring), and `잠금` (locked).
- **Field inference:** The roster numbers likely represent a hunter rating/power (medium confidence): an AppStorio roster value `3,014` repeats as the pre-advancement value on its rank-up screen, and the comparable Caragublu rank-up screenshot explicitly labels its number field `Power Upgraded`; the Naver list itself does not name that field.
- **Identity cross-check:** The lower-row bear portrait at `12,213` is a medium-confidence match to card `036` Bear: its animal portrait matches the Bear artwork in recovered [`C036.jet`](../../../../Blustone-Instrumented/local/legacy-analysis/extracted/assets/C036.jet), and [`cards/036.md`](../../../datasets/hunters/catalogue/036.md) identifies that catalog row as Bear. This validates the likely portrait mapping, not the numeric field.
- **Unknown:** Other portrait-to-catalog mappings and star/rank, gear, jewels, and other modifiers. No HP/ATK/DEF fields are identified.
- **Status:** Preserve as group-level raw UI readings for balance estimates; do not assign the values to hero stats or count coverage.

### Generic “Amateur Hunter” → “Novice Hunter”, rank-up screen

- **Source:** [スマホゲームCH — ブルーストーン review](https://gameappch.com/app/?app=04374), screenshot 16 of 20; direct image: [04374_16.jpg](https://img.gameappch.com/image/app/04/04374/16.jpg). The review page is dated 2017-05-18; the screenshot was visually inspected on 2026-10-05.
- **Visible frame:** Rank-up success panel; generic labels `Amateur Hunter` → `Novice Hunter`; below the portraits the raw values read **1,417 → 2,389**. The panel also says `NEW skill OPEN` and `Block Chance Up`.
- **Confidence:** High for the visible text and numeric tokens; medium for the likely `Power Upgraded` field attribution.
- **Field inference:** Caragublu image 3 explicitly labels an analogous rank-up value pair `Power Upgraded`; this panel's `1,417 → 2,389` is likely that rating field, though the screenshot itself omits the label.
- **Portrait cross-check:** Reopened the full image and compared the small rank-up portrait against the recovered `C###_Q.jet` card-art set. No catalog portrait could be matched confidently; keep the identity generic/unmapped rather than assigning a likely blonde character.
- **Unknown:** Exact catalog identity; level, star/rank mechanics, equipment, jewels, and other modifiers; no HP/ATK/DEF tuple.
- **Status:** Polluted progression-only evidence for later balance estimates. Do not infer the numeric field or count base coverage.

### Generic “Middle Hunter” → “Advanced Hunter”, rank-up screen

- **Source:** [FreeGame Mugen — ブルーストーン~Blustone~](https://freegame-mugen.jp/spapp/game_6433.html), screenshot labelled `ランクアップ` (rank-up); direct image: [item-20170913151119.png](https://ytt26ko6.user.webaccel.jp/images/item-20170913151119.png). The listing is dated 2017-09-13; screenshot visually inspected 2026-10-05. Its linked YouTube video, `P8S-48rDFHk`, is unavailable.
- **Visible frame:** Rank-up success; generic `Middle Hunter` → `Advanced Hunter`; raw values **7,092 → 11,277** beneath the portraits. The left portrait appears `Lv.MAX` and the right `Lv.1`. A new skill opens, described as additional damage to enemies.
- **Confidence:** High for rank-up text and numeric tokens; moderate for the small level labels; low-to-medium for assigning a numeric field.
- **Field inference:** The number pair may be the same `Power Upgraded` rating shown on Caragublu's rank-up screenshot, but this screenshot does not print that field label.
- **Unknown:** Catalog identity; precise star/rank meaning; equipment, jewels, and other modifiers; no HP/ATK/DEF tuple.
- **Status:** Polluted progression evidence for later balance estimates only. Do not infer the numeric field or count base coverage.

### App Store Hunter List (`19/102`), multiple identities unresolved

- **Source:** [AppStorio archived Blustone listing](https://blustone.appstor.io/), screenshot 3 for iPhone and screenshot 3 for iPad; direct images: [iPhone screenshot](https://is4-ssl.mzstatic.com/image/thumb/Purple118/v4/83/5e/18/835e1803-0bc9-d168-7f8d-86482641d2cf/source/320x480bb.jpg) and [iPad screenshot](https://is4-ssl.mzstatic.com/image/thumb/Purple118/v4/ca/fb/3d/cafb3d01-0935-76f2-b4a3-8ed9148c5283/source/360x480bb.jpg). Both mirrored assets were visually inspected on 2026-10-05.
- **Visible frame:** Hunter List header `19/102`; roster portraits with status labels (including `Exploring` and `Defending`). Fourteen legible raw values appear below portraits: `17,878 / 14,749 / 13,455 / 10,369`; `6,839 / 5,892 / 5,774 / 5,628`; `3,014 / 2,986 / 2,723`; and `1,220 / 1,216 / 901`. A promotional overlay obscures some lower-right slots.
- **Confidence:** High for the listed digits and `19/102`; medium for row placement and a roster rating/power interpretation; low-to-medium for portrait-to-catalog attribution.
- **Field inference:** The values likely show a hunter rating/power rather than HP/ATK/DEF: row 3, portrait 1 shows `3,014`, matching the pre-advancement value on AppStorio screenshot 4; the similar rank-up UI is explicitly labeled `Power Upgraded` in Caragublu image 3. Neither Hunter List screenshot prints that field label.
- **Identity cross-check:** Row 1 portrait 2's bear icon is a medium-confidence match to Bear (`036`) by comparison with recovered [`C036.jet`](../../../../Blustone-Instrumented/local/legacy-analysis/extracted/assets/C036.jet) artwork and [`cards/036.md`](../../../datasets/hunters/catalogue/036.md). `14,749` remains an unassigned rating token.
- **Unknown:** Character level, star/rank, gear, jewels, and buffs are not established. No HP/ATK/DEF fields are identified.
- **Cross-screen clue:** The row 3 blonde portrait resembles the advancement portrait, but the catalog identity remains unconfirmed.
- **Status:** Group-level polluted roster evidence for future rebalance estimates only. Do not assign the values to stat fields or count base coverage.

### Unidentified hunter, advancement-success screenshot

- **Source:** [AppStorio archived Blustone listing](https://blustone.appstor.io/), screenshot 4 for iPhone and screenshot 4 for iPad; direct images: [iPhone screenshot](https://is4-ssl.mzstatic.com/image/thumb/Purple128/v4/d5/45/7f/d5457f73-388e-bf2f-eab7-171d8ac7c125/source/320x480bb.jpg) and [iPad screenshot](https://is4-ssl.mzstatic.com/image/thumb/Purple118/v4/7b/33/66/7b336609-f45a-d2b2-b445-c0e9a84b0b77/source/360x480bb.jpg). Both mirrored assets were visually inspected on 2026-10-05.
- **Visible frame:** `Advancement successful`; generic `Experienced Hunter` → `Proficient Hunter`; raw values **3,014 → 4,407**. The panel says `New Skill Unlocked` and `Additional Damage`.
- **Confidence:** High for labels and digits; medium for the likely rating field; low for catalog identity.
- **Field inference:** The pair is likely a `Power Upgraded`-style rating because Caragublu image 3 explicitly labels a similar rank-up comparison that way.
- **Unknown:** Hero ID, level/star context, equipment, jewels, and modifiers; no HP/ATK/DEF tuple.
- **Cross-screen clue:** `3,014` also appears under a similar-looking blonde portrait in screenshot 3's Hunter List. This is a possible same-hero/same-rating match, not a verified catalog mapping.
- **Status:** Polluted progression evidence only. Do not infer the numeric field or count base coverage.

## Vincent (`010_1`), awakened Lv.30 stat panel; gear state unknown

- **Source:** Locally preserved community FAQ image 5, visually transcribed in [`catalogue/stats/010_1.md`](../../../datasets/hunters/observed-stats/010_1.md); image file [`faq-image05-card-010_1-vincent-awakened.png`](../../../datasets/hunters/observed-stats/found/faq-image05-card-010_1-vincent-awakened.png).
- **Visible context:** Vincent, epithet “Despair of a Millennium”; `Lv.30/30`, `Lv.MAX`, five stars, all five skills `50/50`; an `Awaken. Transc.` button is present.
- **Raw values:** Strength **61,815**; HP **4,980**; ATK **2,634**; DEF **1,992**.
- **Confidence:** High for the identity, visible progression labels, and digits; low/unknown for base-state attribution.
- **Unknown:** Whether equipment is attached; weapon, armor, accessory, and jewel levels; whether these totals include gear or other modifiers; historical game build.
- **Status:** Identified but gear-ambiguous full tuple. Keep for rebalance estimates; do not count as a nude/base hero row.

## Vincent (`010`), armor-upgrade comparison; core stats incomplete

- **Source:** Locally preserved community FAQ image 7, visually transcribed in [`catalogue/stats/010.md`](../../../datasets/hunters/observed-stats/010.md); image file [`faq-image07-card-010-vincent-equip-EN.png`](../../../datasets/hunters/observed-stats/found/faq-image07-card-010-vincent-equip-EN.png).
- **Visible context:** Identity is cross-validated as Vincent (`010`) by the “Purple Combat Coat” name/description and recovered card text. The screen shows a fully equipped card with weapon Lv.50 and accessory Lv.40; the armor changes from Lv.49 to Lv.50.
- **Raw values:** displayed Strength **33,038 → 33,057** (**+19**); armor DEF **101 → 102** (**+1**).
- **Confidence:** High for the visible item name, levels, and digits; unknown for the complete equipment/jewel build and the attribution of the Strength delta beyond this upgrade comparison.
- **Unknown:** Hero HP/ATK/DEF; total gear contribution; skill/jewel/buff context; whether the starting build is nude in any slot.
- **Status:** Partial equipped observation only. Do not infer base stats or subtract the single armor delta from any other total; no hero coverage credit.

## Reddit clan-Discord screenshot archive

The source is [Old Bluestone Screenshots](https://www.reddit.com/r/Blustone/comments/1vyddln/old_bluestone_screenshots/), posted by `Plane-Ad264`. The author says the images were previously shared in their clan Discord. Reddit's in-app browser exposes a 13-image gallery; the entries below were visually inspected there. Photo-viewer date overlays are preserved as likely capture dates only; the game build is not shown.

### Katrina (`090`), Lv.30 training/detail panel; gear state unknown

- **Source locator:** Gallery item 7 of 13; `Train Teammate` panel. The iOS photo-viewer overlay reports 2020-08-12 (likely image capture date, not client version).
- **Visible identity/context:** `Katrina`, title `Owner of Saw Blade`; `Lv.30/30`. The exact name/title match catalog `090`. The on-screen `Equipment` action is visible, but no equipment panel is open.
- **Raw values:** Strength **38,842**; HP **3,846**; ATK **2,913**; DEF **1,757**.
- **Cross-screen clue:** An Offense-filter Hunter List in the same post shows a blonde, rabbit-eared chainsaw portrait at **42,329 Strength**, `Lv.MAX`. That portrait is a medium-confidence match to Katrina (`090`) when compared with the local [`C090.jet`](../../../../Blustone-Instrumented/local/legacy-analysis/extracted/assets/C090.jet) sprite atlas. Treat it as a separate displayed build/state, not a base value or exact growth comparison.
- **Unknown:** Weapon/armor/accessory levels, mounted jewels, buffs, exact star state in the panel, and whether any total is nude/base.
- **Status:** Identified partial tuple and a likely second Strength reading. No hero base-coverage credit.

### Lawrence (`079`), summer recruitment bonus overlay

- **Source locator:** Gallery item 9 of 13; recruitment screen. The iOS photo-viewer overlay reports 2020-08-24 (likely image capture date; app build unknown).
- **Visible context:** `Lawrence`, summer title `Knight of Swimming Pool`; recruitment overlay says `New Hunter Bonus`.
- **Raw modifier tokens:** DEF **20.0%** and adjacent **+1.0%**. `+1000` and `Show off now!` also appear on the recruitment panel.
- **Unknown:** Whether `+1.0%` is a comparison delta, bonus progression, or another overlay; no hero HP/ATK/DEF panel or level/equipment context.
- **Status:** Polluted bonus evidence for Lawrence (`079`); not a base-stat value and no coverage credit.

### Leon (Summer, `094`), recruitment bonus overlay

- **Source locator:** Gallery item 10 of 13; recruitment screen. The iOS photo-viewer overlay reports 2020-07-29 (likely image capture date; app build unknown).
- **Visible context:** `Lifeguard` / `Leon`, matching catalog `094` Leon (Summer); recruitment overlay says `New Hunter Bonus`.
- **Raw modifier tokens:** HP **13.0%** and adjacent **+1.0%**. The panel also shows `+1000` and `Show off now!`.
- **Unknown:** Meaning of the adjacent `+1.0%`, hero level/rank, gear/jewels, and whether this is a special recruitment modifier or a character stat.
- **Status:** Polluted bonus evidence for Leon (Summer, `094`); not a base-stat value and no coverage credit.

### Strength-sorted Hunter Lists, identity and build state mostly unresolved

- **Source:** The same Reddit gallery. One list is filtered to `Offense`; another visible gallery image is filtered to `Defense`. Both show `Hunter List`, selected sort `Strength`, and roster count `98/105`.
- **Offense-list raw readings:** Row-major visible tokens: `43,358 / 43,047 / 42,329 / 40,214`; `38,606 / 37,522 / 36,081 / 36,063`; `32,698 / 29,447 / 29,193 / 29,146`; `28,821 / 23,160 / 17,243 / 16,548`. Most visible badges read `Lv.MAX`; one reads `Lv.19`, and two read `Lv.1`. The `23,160` rooster portrait is a medium-confidence match to Beckhen (`051`) against local [`C051.jet`](../../../../Blustone-Instrumented/local/legacy-analysis/extracted/assets/C051.jet) art. No other portrait-to-catalog mapping is assigned here.
- **Defense-list raw readings:** Row-major visible tokens: `53,395 / 45,183 / 44,712 / 39,189`; `37,562 / 36,822 / 36,734 / 35,138`; `33,376 / 32,417 / 31,510 / 27,385`; `27,201 / 26,835 / 24,868 / 24,452`.
- **Field confidence:** High that these are current Hunter List values sorted by the selected `Strength` field; the UI does not establish that they are base stats.
- **Unknown:** Most hero IDs, full row membership below the crop, per-card level/rank, gear/jewels, skills, buffs, historical client balance build, and whether the values can be reconciled across screenshots.
- **Status:** Group-level Strength observations for later rebalance work only. Do not map unknown rows, normalize them, or count base coverage.

## Related skill modifiers (not hero stats)

### Beckhen / Baek Hen (`051`) — Fight Club Guardian skill effects

- **Source:** [Namu Blustone/Hunter/Striker page](https://en.namu.wiki/w/%EB%B8%94%EB%A3%A8%EC%8A%A4%ED%86%A4/%ED%97%8C%ED%84%B0/%EA%B3%B5%EA%B2%A9%EC%88%98), section 2.3.1, text-fetched 2026-10-05 (page last modified 2026-08-20). "Baek Hen" is a transliteration variant of the same Fight Club chicken as catalog `051` Beckhen; the page confirms Fight-Chip acquisition and periodic-invincibility lore shared with defender Papillon.
- **Raw effect magnitudes (text, not pixels):** special-skill damage **~9046**; attack-speed buff **~20.00%**; self damage-immunity **every 3 seconds**, duration **0.51–1.00 seconds** (1 second at max level; page notes a historical nerf); defense-reduction effect **~30.00%**; Fight-Club-only block-chance effect **~30.00%**.
- **Unknown:** game build/version for these numbers, exact skill levels they apply to, whether `~` marks rounding or approximation in the original, and any HP/ATK/DEF base values for the hero itself.
- **Status:** Skill/effect modifier context for later rebalance work, same class as the Crocus entry below. Not Beckhen's own stats; no coverage credit. The page's per-hero YouTube skill-video links remain uninspected visual leads.

### Crocus — `Necromancer's Might`

- **Source:** [Caragublu — Blustone Game Guide Tips & Trik](https://www.caragublu.com/2018/12/blustone-game-guide.html), embedded image titled `Blustone Cara Meningkatkan Skill Hunter`, image viewer 4 of 7; direct image filename `Blustone Skill Training.jpg`.
- **Visible effect:** Skill Lv.35/50; `All Enemies` / `Everlasting Effect`; `Max HP` changes **8.75% → 9.00%** in the `Special Training Effects` panel. Description says Crocus reduces all enemies' maximum HP.
- **Status:** Skill/effect modifier, not Crocus's own HP or a base-stat observation. Preserve for later rebalancing context; no coverage credit.

### Namu Striker page text modifiers (Mowgli, job mechanics, prose-only skills)

- **Source:** [Namu Blustone/Hunter/Striker page](https://en.namu.wiki/w/%EB%B8%94%EB%A3%A8%EC%8A%A4%ED%86%A4/%ED%97%8C%ED%84%B0/%EA%B3%B5%EA%B2%A9%EC%88%98), full text fetched 2026-10-05 (page last modified 2026-08-20). Full video inventory and official-post retry log: [`striker-videos-2026-10-05.md`](striker-videos-2026-10-05.md).
- **Raw text magnitudes:** Mowgli (`002`) 5th specialty — temporary damage immunity every 3 seconds, duration **0.51–1.00 seconds** (same range format as Baek Hen's). Striker job: skill costs **3 Rage** (Lily & Lala `047` cost **4 Rage**); skill front-only with auto-move-to-front; training goods rusty/sharp/mysterious metal pieces. Karl Steiner (`012`) no-skill attack speed **7** vs **8** for all other attackers.
- **Prose-only (no numerics):** Mary (defense/block/element-resist reduction, immunity block, bleed-until-dispelled, regen-to-0), Bella (attack-speed/bleed, 10% stackable ATK/AS, damage immunity on max skill), Zenobia (buff strip plus up-to-4.5 s buff prevention, ignore-block damage), Kalbaram/Blade Wind (ignore-defense up to half, damage-immunity piercing, bleed-until-retreat).
- **Unknown:** game build/version for every number, exact skill levels, whether `~` marks rounding, and any HP/ATK/DEF base values. The 21 linked Deko Boko GAMES skill-cinematic videos were metadata-checked only, never pixel-inspected; one Vincent video (`s4-OmmRZJDM`) refuses oEmbed (HTTP 403).
- **Official-post retry:** `bs.visualshower.com` posts 707457 (Heidi), 426682 (Lily&Lala), 1082853 (Chichi), 912433 (Kalbaram) remain inaccessible — HTTPS certificate error, HTTP 503 with GNAME parking script, and zero Wayback captures for all four document URLs. Namu's quoted intro prose is second-hand transcription, not an official fetch.
- **Status:** Skill/effect and job-mechanic context for later rebalance work. Not any hero's own stats; no coverage credit.

## Lapis (Awakened, likely `017_1`), Lv.30 training panel; gear state unknown
- **Source:** [Reddit comment by `awesome8679`](https://www.reddit.com/r/Blustone/comments/1mcmqfz/comment/n5v5188/) in the [`r/Blustone` screenshot post](https://www.reddit.com/r/Blustone/comments/1mcmqfz/screen_shots/); [attached image](https://preview.redd.it/screen-shots-v0-kefkx9agovff1.jpeg?width=1179&format=pjpg&auto=webp&s=d3fb2630fec780416857d66cbb911c89d24907a1), opened at full image view on 2026-10-05.
- **Visible context:** `Train` screen, character name `Lapis`, `Lv.30/30`; five skill slots display `50/50`. The image has `Skill Training`, `Awaken. Transc`, and `Equipment` actions. The commenter calls this Awakened Lapis and says it was their strongest, supporting a likely catalog match to `017_1`; the exact awakening/build state is not otherwise specified on the screen.
- **Raw values:** Strength **53,046**; HP **4,501**; ATK **2,382**; DEF **1,789**.
- **Confidence:** High for the four displayed values and level; high for the visible name `Lapis`; medium for mapping to awakened row `017_1` based on the comment context.
- **Unknown:** Weapon, armor, accessory, mounted jewels, other modifiers, exact awakening/transcendence state, and client balance version. The `Equipment` button is visible, but no loadout view is open.
- **Status:** Identified, level-known but gear-ambiguous partial hero tuple for later rebalance estimates. Do not call the values nude/base or count the hero toward base-stat coverage.

## 2026-10-05 JP/CN video-lane pass (no new numeric observations)

Full lane log: [`youtube-jp-cn-2026-10-05.md`](youtube-jp-cn-2026-10-05.md).
No new HP/ATK/DEF, Strength, or item value was recovered in this pass, so
nothing below changes any coverage count.

### Bilibili 128-part story collection (dialogue/art lead, no stats)

- **Source:** [(Blustone)主线剧情第一章：突如其来的考试.第1话](https://www.bilibili.com/video/BV1wo4y1X7K2/)
  by `乛ㅂ乛`, posted 2021-07-07; collection `Blustone主线故事第一季`
  (128 parts, chapters 1–18). Same uploader's NPC stories (`列奥纳多`,
  `艾斯特`, `拉娜`, `贝克汉&杰克`) and character story
  (`圣诞双胞胎-莉兰&拉兰`) indexed from the related-video list.
- **Raw values:** None — page metadata and episode list only; no video frame
  was played or inspected, so no character art, stat panel, or number is
  claimed.
- **Unknown:** All future frame contents; whether any episode contains a
  roster/battle frame worth sampling. Story episodes are a low prior for
  stat panels.
- **Status:** Identity/dialogue lead only. Any future frame is Blustone 2 /
  2021 balance (post-2019-09-05 rebalance); never assume earlier balance.

### Awakening-lead name still unmapped

- Metadata lookups (`noembed`, YouTube `oembed`) for the 1:12 awakening video
  ([Y2nxj-YwI5I](https://www.youtube.com/watch?v=Y2nxj-YwI5I)) returned 401,
  so no title/description text was recovered. Exact-token searches for
  `27155`, `28502`, `3021`, `1144` with `블루스톤` / `시계초` returned
  unrelated results. Display name `시계초` stays unmapped; the Lv.1/30 panel
  (Strength 27,155; HP 3,021; ATK 1,144; DEF 1,671) remains a partial lead
  with no base coverage.

### MON BLAST! clip titles re-confirmed (cross-title only)

- `noembed` confirms official `VisualShower Corp.` titles: Snowfox Area 1
  ([sAlXfcSOKTc](https://www.youtube.com/watch?v=sAlXfcSOKTc)), Pandahawk
  Area 7 ([rt85g45tBY8](https://www.youtube.com/watch?v=rt85g45tBY8)),
  Moonwoof Area 1 ([bytCvTR6L3c](https://www.youtube.com/watch?v=bytCvTR6L3c)).
  Values stay in `cross-title-mon-blast.md`; zero Blustone coverage credit.

## 2026-10-05 video-loose-ends follow-up (no new numeric observations)

Full lane log: [`video-loose-ends-2026-10-05.md`](video-loose-ends-2026-10-05.md).
No new HP/ATK/DEF, Strength, or item value was recovered, so nothing below
changes any coverage count.

### Short RG47CcM7c20 still uninspected; access characterized

- [펩시 — 블루스톤 헌터 자기극복](https://www.youtube.com/shorts/RG47CcM7c20)
  (19 s): direct fetch returns the generic shell; `noembed`/`oembed` 401
  (same egress limitation as the prior pass's 401s, not a removal signal);
  `yewtu.be` and `inv.nadeko.net` API routes 403; exact-ID search has no
  mirrors. Thumbnail URL
  (`https://i.ytimg.com/vi/RG47CcM7c20/hqdefault.jpg`) is the cheapest next
  pixel attempt. Namu prose confirms self-overcoming opens at 3★ (duplicate +
  metron/pieces), so this is likely a transcendence-comparison panel of the
  Caragublu-Bear class. No values inferred.

### Bilibili pages sampled at metadata level (dialogue/art leads only)

- Entry [Ch.1 Ep.1](https://www.bilibili.com/video/BV1wo4y1X7K2/) re-fetched
  (2021-07-07, 4:02, 385 plays; 128-part collection, 4,676 plays).
- [Ch.1 Ep.2](https://www.bilibili.com/video/BV1to4y1X77n/) (2:08, 105 plays)
  and NPC story [Leonardo](https://www.bilibili.com/video/BV1Rq4y1Q78Z/)
  (2021-08-14, 40 plays) page-sampled. No frame played on any page.
- Related rails expand the NPC/character-story inventory (Shuman, Audrey,
  Clara, Gullveig, Westfield, lottery mouse, Bibi, Celine, Selene-Valentine,
  first-hunter Lantern, Nene variants, Lawrence, Kain-class stories). Titles
  name dialogue subjects; no title→catalog ID mapping is performed here.
- All 2021 Blustone 2 international-version balance if frames ever surface.

### Bahamut board text access recovered; two threads read

- Desktop routes are 403 via fetch, but `m.gamer.com.tw/forum/C.php` returns
  full text. [Server-status thread](https://m.gamer.com.tw/forum/C.php?bsn=33171&snA=347&bpage=1&ltype=)
  (2021-03-31 crash reports, no stats) and [2017 beginner guide](https://m.gamer.com.tw/forum/C.php?bsn=33171&snA=17)
  (2017-11-03; recruit-source prose + ~12 uninspected `truth.bahamut`
  art attachments; evolution-cost prose 1k/3k/12k/60k kept as unverified
  economy context) were read. Remaining threads and image bytes are leads.

### `시계초` is a common noun, not a hunter name

- `"시계초" 블루스톤` searches return only passionflower (Passiflora)
  botanical results. The ~00:52 awakening-panel reading is most likely a
  low-resolution misread of the Korean hunter name; do not search it as a
  name. Productive retry is a fresh pixel read against the Korean client name
  list. Panel values stay a partial lead with no base coverage.

## Namu KR text-lane numeric tokens (2026-10-05)

Full lane log: [`namu-kr-blogs-2026-10-05.md`](namu-kr-blogs-2026-10-05.md).
Text-extracted (not screenshot) values from the Namu hunter/main mirrors plus
dated blog/review prose. **Era is unresolved per item** unless noted; never
normalize against the 2019-09-05 rebalance. No HP/ATK/DEF base tuple here.

### Lantern (`001`), 5-star crit skill magnitude

- **Source:** Namu hunter mirror `d.namu.moe` §2.1 attacker row (text, fetched 2026-10-05).
- **Raw text:** "크리티컬 4스킬이 터질 시 5성기준 상대에게 한번에 10000이 넘는 미친데미지"
  (when crit skill 4 fires, at 5★, 10,000+ damage in one hit) plus DEF-down debuff.
- **Unknown:** Gear/jewels/skills state, client build, era, enemy armor context.
- **Status:** Skill-magnitude context for rebalance estimates; not a hero stat.

### Attack-speed modifiers (Gullveig / Hermes / Karl Steiner)

- **Source:** Same Namu hunter mirror (§2.3 bomber rows, §2.1 Karl row).
- **Raw tokens:** Gullveig permanent ally AS +7.5%; Hermes AS passive +15%
  (wiki stacks to 22.5%; +Karl skill → 37.5%, wiki arithmetic, unverified);
  Karl Steiner no-skill attack speed **7**; other attackers all AS **8**
  ("공격수들은 얘를 제외하곤 공속이 모두 8이다").
- **Unknown:** Builds, era, whether wiki percentages are additive in-client.
- **Status:** Modifier/base-speed context; Karl's 7 vs the 8.00 constant in
  `010.md` is preserved as the documented exception, not a contradiction to resolve here.

### Beckhen Fight Club-only +10% modifier

- **Source:** Same mirror §2.1: "파이트클럽에서만 공격, 방어, 생명력이 10% 증가되는 헌터"
  (+10% ATK/DEF/HP in Fight Club only); traces via Fight Chip shop
  (375 chips / 5 traces, 6h restock).
- **Status:** Mode-conditional modifier, not a base row.

### Bond percentages (Haisen, Chirrchirr-Alice)

- **Source:** Same mirror §2.4: Haisen bond 4★ 8% / 5★ 16%; Alice-Chirrchirr bond 4★ 10%.
- **Status:** Modifier context only.

### Economy tokens (Namu text; local-fixture cross-check only)

- **Gacha:** 30 manda 1 pull / 300 manda 10+1 (unit implied by context).
- **Fixed recruit traces:** 20/40/80/160 for 1★–4★ ((2^n)×10).
- **Stim@s:** 3000 rupees or 3 manda (literal "3000천 루피" preserved; ~2019-04 change).
- **Rage costs:** attackers/defenders 3, bombers/helpers 4 (Lily&Lala, Bear cost 4).
- **Self-overcoming metron pairs** (crystal/fragment): 1★ 5/50, 15/150, 45/450;
  2★ 7/70, 25/250; 3★ 9/90, 30/300, 80/800; 4★ 12/120, 40/400, 110/1100.
- **Equipment costs:** rupee breakpoints 500 → 1000 → 5000 → 15000 → 30000 → 100000
  at +10/20/30/40/50; toolbox 130/10 per level at 40–49 (full grid re-fetchable
  from mirror lines ~280–420).
- **Mirage fuel:** 15 + 5(n−1); **helium:** 1★ 2×5 (10), 3★ 15×2 (30), ≤4 boxes/run;
  **star condition:** clear + under-01:00 + full survival; region 30 stars → manda
  or request ticket; **FC tiers** Bronze→Manda(rin), 6 wins per tier, win +15 /
  loss −8; full tier/rank reward tables in lane log §2.
- **Era note:** undated wiki text (mirror modified 2026-08-13, content 2017–2021);
  dated anchors: stim change ~2019-04 (pre), HungryApp mechanics 2019-09-05
  (rebalance day 0), rollback narrative 2021-09 (post). No normalization applied.

## Namu exact table transcription lane (2026-10-05) — ERA-UNRESOLVED

Full cell-by-cell source: [`namu-tables-2026-10-05.md`](namu-tables-2026-10-05.md)
(raw-HTML cell extraction from both mirrors, fetched 2026-10-05). Every token
below is ERA-UNRESOLVED (wiki undated; content range 2017–2021) — never
normalize against the 2019-09-05 rebalance. Rebalance-estimate context only;
no base-stat credit.

### Equipment enhancement grid 1–50 (text-table tokens)

- **Per-level toolbox (normal/advanced) + rupees:** lv1–2: 0/0, 500;
  lv3–4: 2/0, 500; lv5–6: 4/0, 500; lv7–8: 8/0, 500; lv9: 12/0, 1000;
  lv10–12: 10/0, 750; lv13–15: 12/1, 750; lv16–17: 14/3, 750; lv18: 22/4,
  750; lv19: 40/5, 1500; lv20–29: 30/6, 5000; lv30–39: 70/8, 15000;
  lv40–50: 130/10, 30000.
- **Remodel rows (element material + rupees, 0/0 boxes):** lv10: 1 + 5000;
  lv20: 6 + 10000; lv30: 25 + 40000; lv40: 50 + 100000; lv50: (element cell
  empty in source) + 30000.
- **Structural cautions preserved from source:** boundary levels 10/20/30/40
  appear twice with different numbers (remodel vs next-block base row) — do
  not collapse; lv50 element cell is empty, not zero; rows 2–9 / 11–19 /
  21–29 / 31–39 / 41–49 carry no element cell in the source (rowspan).

### Self-overcoming exact pairs (crystal/fragment)

- 1★: 5/50, 15/150, 45/450; 2★: 7/70, 25/250 (third step EMPTY in source);
  3★: 9/90, 30/300, 80/800; 4★: 12/120, 40/400, 110/1100. No 5★ row exists.

### Skill-training role-material grid (shared quantities, materials differ)

- Shared quantity grid per band (1~4 … 45~50): `0/0/0 | 1/0/0 | 2/0/0 |
  3/0/0 | 4/1/0 | 5/2/0 | 0/3/1 | 0/4/2 | 0/5/3 | 0/6/4` (rowspanned from the
  attacker row in the wiki source; defender/bomber/helper rows show labels
  only). Materials: attacker 금속 조각 (녹슨/예리한/신기한), defender 등껍질
  (부서진/멀정한/무적의), bomber 화염석 (차가운/뜨거운/이글거리는), helper
  약초 (시든/싱싱한/열매 맺은). 종합 metron fragments read `1|2|3|4|5` —
  five values for ten bands, pairing unresolved.

### Fight Club tier rewards (exact)

- 실버/골드: chips 100 + green manda 2; 에메랄드/메트론: 150 + 2; 만다린:
  200 + 2. 브론즈 has NO source entry (unrecorded, not zero).

### Fight Club rank rewards 1–30000+ (exact)

- 1: 2500+800 · 2: 2400+650 · 3: 2300+600 · 4–10: 2200+550 ·
  11–20: 2100+500 · 21–30: 2000+475 · 31–50: 1900+450 · 51–70: 1800+425 ·
  71–100: 1700+400 · 101–130: 1600+375 · 131–180: 1500+350 ·
  181–240: 1400+320 · 241–320: 1300+300 · 321–420: 1200+275 ·
  421–550: 1100+250 · 551–720: 1000+**255 sic** (breaks the 250→200 descent;
  preserved literally, likely wiki typo) · 721–950: 900+200 ·
  951–1250: 800+175 · 1251–1620: 700+150 · 1621–2120: 650+125 ·
  2121–2750: 600+100 · 2751–3600: 550+75 · 3601–4700: 500+50 (green manda
  ends here) · 4701–6100: 450+고급 의뢰서 3 · 6101–8000: 400+2 ·
  8001–10300: 350+1 · 10301–13500: 300+fuel coupon 5 · 13501–17500: 250+4 ·
  17501–23000: 200+3 · 23001–30000: 150+2 · below 30000: 100+1.
- **Corrections to the earlier text-lane section above:** helium is
  1★ 5×2=10 / **2★ 4×8=32** / 3★ 2×15=30 (the 2★ row was omitted there);
  FC win/loss is +15/−8 with defense-loss −5~6 and revenge/forfeit −8.

### Seore/Lapis Capture retry (still unresolved, no credit)

- `dark.namu.moe` file page = metadata only (no pixels); Wayback
  availability API = zero snapshots; exact-filename web search = zero
  alternate hosts. `Capture+_2019-01-25-23-49-07.png` remains an image lead
  only.

## Post-2019 roster lane (2026-10-05)

Full lane log: [`post2019-roster-2026-10-05.md`](post2019-roster-2026-10-05.md).
Zero strict rows; hero coverage stays 1/113. Entries below are
identity/context/leads only, with no base-stat credit.

### Miraheze archiving wiki is stat-free (identity context only)

- **Source:** [Characters index](https://blustone.miraheze.org/wiki/Characters)
  (103 pages, edited 2024-06-04); sampled [Estelle](https://blustone.miraheze.org/wiki/Estelle)
  (`096`), [Katrina](https://blustone.miraheze.org/wiki/Katrina) (`090`),
  [Lapis (Awakened)](https://blustone.miraheze.org/wiki/Lapis_(Awakened)) (`017_1`).
  All three share one template: skill magnitudes are `[value]`
  placeholders and **no HP/ATK/DEF field exists** — a mechanics/art
  record, not a stat source. No exhaustive 103-page crawl performed.
- **Identity context preserved:** Estelle `096` Offense/Fire, released
  10 Sep 2020, equipment Rapier / Clerk Uniform / Ribbon Brooch;
  Katrina `090` Offense/Lightning, B.F. Chainsword / Cast Iron Gauntlet
  / Saw Blade Sneakers; Awakened Lapis `017_1` ★5 Offense/Ice, Frost
  Sword / Military Tank Top / Destiny Knot, with full skill-mechanics
  text at `[value]` magnitudes.
- **Era stratification (index release dates):** Geranium `064` Mar 2019
  through Bella `075` Aug 2019 predate the 2019-09-05 rebalance; Themis
  `092` (12 Jun 2020) and Estelle `096` (10 Sep 2020) postdate it. Many
  076–098 variants show no date; absence of a date is not a claim.
- **Unknown:** Every numeric stat; level/gear for all panels.
- **Status:** Context for future era-tagging only; no coverage credit.

### Uninspected 2020+ video leads

- `20+ Hunters Recruiting! | Blustone 2` by GuitarRock First
  ([cnMBlXFd5W4](https://www.youtube.com/watch?v=cnMBlXFd5W4),
  existence confirmed via `oembed`, date/frames unrecovered) and
  `블루스톤 헌터 섭외`
  ([hnnxZmmPg0Q](https://www.youtube.com/watch?v=hnnxZmmPg0Q),
  confirmed-exists only). Recruitment footage = low prior for stat
  panels; needs a browser-capable frame pass.
- Official Estelle ultimate-skill video
  ([blustone_jp status 1392041790094598147](https://x.com/blustone_jp/status/1392041790094598147),
  May 2021, linked from the Miraheze Estelle gallery): skill demo, no
  stat panel expected; uninspected.
- **Status:** Leads only; no values, no credit.

### Miraheze gallery audit + skill-video queue (2026-10-05)

Full lane log: [`miraheze-gallery-2026-10-05.md`](miraheze-gallery-2026-10-05.md).
Zero strict rows; no coverage credit. Art and links only — no stat is
inferred from any sprite, portrait, or equipment name.

- **Gallery existence:** `Estelle/gallery`, `Katrina/gallery`,
  `Themis/gallery` do not exist (HTTP 404 redlinks — nothing to
  inspect). `Lapis/gallery` (oldid=923) holds base Lapis
  Idle/Sad/Angry/Joy/Shock/Etc + Awakened Idle; `Geranium/gallery`
  (oldid=1458) holds base five emotions plus a second five-emotion set
  headed **Geranium (Valentine)** — no catalog ID assigned, do not map
  it to any row; `Bella/gallery` (oldid=1544) holds five emotions. All
  sprite-only, no numbers/panels/levels.
- **Fandom closed:** page fetch 403 is gating, not content — the wiki's
  own API lists exactly 12 generic pages (Attackers, BLUSTONE, BLUSTONE
  Wiki, Bombardier, `Charaters:Captain`, Defender, Fire/Scissors,
  Helper, Ice/Rock, Main Page, Striker, Thunder/Paper) and reports
  Katrina missing. No per-hero content exists to mirror.
- **Video queue (all unplayed):** Themis
  ([blustone_jp 1356527779781705728](https://x.com/blustone_jp/status/1356527779781705728)),
  Estelle
  ([blustone_jp 1392041790094598147](https://x.com/blustone_jp/status/1392041790094598147)),
  Geranium Short
  ([mFTmAXPz-dk](https://youtube.com/shorts/mFTmAXPz-dk)); then the 21
  Deko Boko cinematics; recruitment videos last (GuitarRock
  `cnMBlXFd5W4` oEmbed-confirmed `20+ Hunters Recruiting! | Blustone 2`;
  `hnnxZmmPg0Q` oEmbed 401, restricted/egress-gated, not removal).
  Sample for Train/detail backgrounds behind cinematics; Katrina and
  Bella have no video link queued.
- **Identity context (text, `[value]` magnitudes throughout):**
  Geranium `064` Bomber/Lightning, 29 Mar 2019, Whip Sword / Black
  Uniform / Forbidden Suitcase, 4 Rage; Themis `092` Bomber/Fire,
  12 Jun 2020, Monster Sniper Rifle / Reinforced Exoskeleton Suit /
  Large-Caliber Special Bullet, 4 Rage; Bella `075` Offense/Ice,
  30 Aug 2019, Sword Dance Swords / Dancing Clothes / Blue Skirt,
  3 Rage. Full mechanics prose in the lane log. Katrina `090`
  re-confirmed with no date/gallery/video.

## Jewel-instance mechanics lane (2026-10-05)

Full lane log: [`jewel-instance-2026-10-05.md`](jewel-instance-2026-10-05.md).
Zero strict rows; mounted panels stay 6/6 samples, accessories 1/100.
Entries below are rebalance/mechanics context only, with no base-stat credit.

### Jewel name does not predict the main stat (6-panel sample)

- **Source:** Direct visual re-read 2026-10-05 of FAQ jewel panels
  `analysis/catalogue/stats/found/faq-image22..27-jewel-*.png`
  (all Lv.15/15, 5-star Radiant, Highest Class). Transcriptions match
  `GEAR.md` §2 exactly.
- **Raw pattern:** Weapon slot mains ATK `+29` under both `Radiant Speed
  Jewel` (image22) and `Radiant Offensive Jewel` (image23); Accessory slot
  mains Max HP `+58` under both names (images 24/25); Armor slot mains
  differ under the same `Radiant Speed Jewel` title (Block Chance `+2.30`
  image26 vs DEF `+29` image27).
- **Instance decimals (separate from set-effect +23):** percent-type
  instance stats carry two decimals (Crit Dmg `+3.13/+3.87/+3.86`, Block
  `+0.72/+0.56`, Dmg Red Blk `+0.50/+0.38`, Crit Chance `+0.67`, Block main
  `+2.30`); flat stats are integers (ATK `+29/+11/+12/+13`, DEF `+11/+29`,
  Max HP `+58/+21/+18`) — except Elemental Enhancement/Resistance
  instance substats, which carry two decimals (`+1.44/+1.65/+1.69`).
- **Chrome tokens:** Speed footers read `Mount 4, Increase Attack Speed
  1.72`; Offensive footers read `Mount 2, Increase ATK 5%` (panel says
  ATK, FAQ list/VSFan EN help say AP — preserve both). image22 removal
  footer reads `40000` (gold icon) `/ 40` (second currency icon unknown);
  confirmed on image22 only.
- **Unknown:** Whether name/slot/main mapping generalizes beyond n=6;
  removal-cost currency identity; capture era (ERA-UNKNOWN).
- **Status:** Mechanics lead only; no coverage credit.

### Equipment modification gates text cross-check (no new values)

- **Source:** [Namu item page](https://dark.namu.moe/w/%EB%B8%94%EB%A3%A8%EC%8A%A4%ED%86%A4/%EC%95%84%EC%9D%B4%ED%85%9C)
  §4.3 (TEXT-SOURCE, ERA-UNKNOWN): each equipment grade holds 10 levels
  with grade-up (`장비 개조`) per grade; element materials
  번개 막대/냉각수/인화성 물질. Toolbox/rupee cost tables only partly
  legible — not transcribed as exact values. §4.4.3 결정 (Crystal) is an
  empty header: no per-star crystal values (negative result).
- **Community text (unattributed snippet):** r/Blustone jewel thread
  search snippet claims jewels are usable from 4★ hunters in the equipment
  panel. Thread fetch was blocked; keep as unverified community text, not
  visual evidence.
- **Status:** Corroborates the 10/20/30/40 gates from FAQ prose and VSFan
  `CONTENTS11_3`; no per-level curve; no coverage credit.

### Jewel economy lane (Metron, 4★ gate, mining/polish — TEXT-SOURCE only)

Full lane log: [`jewel-economy-2026-10-05.md`](jewel-economy-2026-10-05.md).
Zero strict rows; mounted panels stay 6/6 samples, accessories 1/100.
Entries below are rebalance/mechanics context only, with no base-stat credit.

- **Metron Crystal per-10+1 economy note:** Prior lane's [official event
  post](https://www.facebook.com/visualshowerEN/posts/blustone-event-the-more-the-better-by-lottery-mouseyou-will-get-a-metron-crystal/1124385431051052/)
  (one Metron Crystal per 10+1 pull) could not be re-opened (Facebook login
  wall). Official-channel search snippets corroborate the pattern as text:
  *"You will get a Metron Crystal for every 10+1 pull! And extra rewards are
  available based on your total number of Lottery Mouse pulls!"*
  (`@VisualShowerEN`), plus parallel 10-traces-per-10+1 event posts
  (`BlustoneEN`: Mary, Katrina). Post dates/builds unestablished
  (ERA-UNKNOWN). Economy note only; no crystal stat values.
- **4★-usability snippet verified, thread still unread:** Page and `.json`
  fetches of the `iq4irt` thread both return 403; no body inspected. The
  search snippet is now fuller and matches the earlier fragment: *"The jewel
  you can use once you have 4☆ hunter in equipment panel. Only 4☆ hunter
  above can use jewel. Jewel boost your hunter stats."* Still unattributed
  community text, not visual evidence. Mechanical cross-check (inference,
  not proof): archived JP rank-up guide says equipment unlocks at ★4 and
  VSFan `CONTENTS11_7` mounts jewels onto equipment, so a 4★ jewel gate
  follows from the equipment gate without a separate jewel rule.
- **Namu item page re-check (TEXT-SOURCE, ERA-UNKNOWN):** §4.4.3 결정
  (Crystal) is still an empty header — no per-star crystal values (negative
  result reconfirmed). §4.1 메트론 is legible: fragments (basic, widely
  used) vs intact crystals (deep-ruins rare); S1 승리의 푸른빛 dialogue
  values one crystal far above 1,000 fragments **but states fragments cannot
  be exchanged for a crystal** (in-fiction line, not a rate); fragments are
  consumed in self-overcoming in grade/count-varying amounts (no table).
  §4.3 grade-1 toolbox/rupee tokens (`500/1000/5000`-ish) are garbled —
  not transcribed as exact values; grades 3–5 costs are unstated
  (guild-discount placeholders).
- **Adjacent Namu economy (same page, TEXT-SOURCE):** Metron crystal at
  극악 fishing probability; fight-chip corner sells Metron crystals;
  honor medals 700/8 traces (★4), 350/8 (★3); fuel 5,000 → 10,000 rupees
  from 3rd purchase, Manda 5 → 60; 10+1 form guarantees ≥1 ★3; stim-pack
  speed tiers ★1–2 FEVER / ★3–4 SUPER / ★5 ULTRA; helium 2/8/15 per grade
  with 5/4/2 searches, 4 waves, 2 traces/box (min 2, max 8). Role skill-mat
  band tables are garbled — band alignment unverified.
- **Mining/polish rules (local texts, no cost screenshot found):** VSFan
  1.4.4.1 `CONTENTS11_5/11_6` — daily free kind-selected mining, Manda and
  advanced mining, lucky Search finds, Market sales; polishing costs rupees
  only, is probabilistic, harder at higher stages, failure loses only the
  rupees. `LEVELING.jet` res-1 is a rank-2–15 polish-probability CSV
  (tuning, not costs). Post-threshold 研磨 growth: ★1–3 mains +30%,
  ★4–5 mains +50%, all substats +50%, substat upgrades fixed at max. **No
  rupee cost table or success-rate screenshot has surfaced.**
- **Bahamut negative:** board bsn=33171 exists (intro snA=353,
  group/心得 snA=340); no crystal-build thread found; direct fetch 403.
- **Unknown:** pull-post dates/builds; thread authorship/context; exact
  equipment/polish rupee tables; per-star crystal stat rows.
- **Status:** Economy/mechanics context only; no coverage credit.

## Wayback announcement/guide numeric context (2026-10-05)

Full lane log:
[`wayback-announce-2026-10-05.md`](wayback-announce-2026-10-05.md).
Rebalance/reward/progression-rule context only — **no base-stat credit**.
Era tags use the 2019-09-05 rebalance threshold.

### Official rebalance post, full Traditional-Chinese wording (POST era)

- **Source:** [TapTap post 73656](https://www.taptap.io/post/73656),
  posted 2019-09-04 by `SmileV`, effective after 2019-09-05.
- **Equipment (POST):** stats +50% on existing base; fractional/decimal-point
  increments removed; upgrades after modification stage 2 (equipment Lv.20+)
  gain much larger increases.
- **Crystals (POST):** large buff to ATK/DEF/HP/element-enhance/element-resist/
  penetration; small buff to crit chance/crit damage/block/block-dmg-reduction;
  main-stat option frequency fix; mains +30% (1–3★) / +50% (4–5★); ALL
  substats +50% with upgrades fixed at max (was random-in-range); set bonuses
  raised with no exact amounts; requires latest client version.
- **Status:** Version-stratification anchor. New vs `stat-version-context.md`:
  fractional-removal rule, Lv.20 stage-2 breakpoint, per-stat buff grouping,
  frequency fix, fixed-at-max substat rule.

### Training rules (POST era, 2019-12-11 guide capture)

- **Source:**
  [トレーニング](https://web.archive.org/web/20191211104454/https://blustone.jp/%E8%82%B2%E6%88%90%E8%AB%96/%E3%83%88%E3%83%AC%E3%83%BC%E3%83%8B%E3%83%B3%E3%82%B0).
- **Rules:** Gym training; max **5 partners per session**; **★1–★2 fodder
  recommended**; max-level hunters proceed to rank-up. No cost/XP numbers.
- **Status:** Rule context; consistent with the local 5-partner cap.

### Rank-up rules and trainer economy (POST era, 2019-11-13 guide capture)

- **Source:**
  [ランクアップ](https://web.archive.org/web/20191113131941/https://blustone.jp/%E8%82%B2%E6%88%90%E8%AB%96/%E3%83%A9%E3%83%B3%E3%82%AF%E3%82%A2%E3%83%83%E3%83%97).
- **Rules:** max **★5**; materials = **same count of same-★ partners**
  (★3→★4 needs three ★3s); level resets to 1, new skill learned, **★4+
  unlocks equipment**; **batch rank-up** for ★1–★2 without max level.
- **Economy:** releasing a ★3 yields **8 Chu-coins**, buying **two ★3
  trainers** at the Secret Market; feeding ranked-up ★3s beats consuming
  natural ★3s.
- **Status:** Rule/economy context; ★3→8-coins→2-trainers and ★4-equipment
  unlock are new numeric leads, original-server proof unestablished.

### Launch anchor (PRE era, 2017-05-15 press)

- **Source:** [Inven `news=177783`](https://www.inven.co.kr/webzine/news/?news=177783).
- **Facts:** Singapore soft launch April 2017; White Island Season 2
  season-pass buyers receive heroine Min Hae-sun as a playable hunter.
- **Status:** Earliest dated Korean press anchor; no numbers.

### Event-calendar negative result (PRE-era posts, bodies empty)

- **Source:**
  [Event index 2019-12-09](https://web.archive.org/web/20191209131405/https://blustone.jp/category/event):
  15 dated Feb–Mar 2019 events (Fight Club 2018 championship rewards, NEW ★4
  Elise capture, March package, boutique festival, Valentine war, Midgard
  sports festival, mirage hot-time, popularity ranking, etc.).
- The championship-reward detail body is empty in the archive; **no reward
  tables or rates recovered**. No 2020/2021 event captures exist, so EV05 web
  schedule remains unrecovered (R_EPISODE.jet export stands as the source).

## Official skill-video thumbnails (2026-10-05, POST-era / unresolved)

Full lane log: [`official-skill-frames-2026-10-05.md`](official-skill-frames-2026-10-05.md).
Poster thumbnails only (no full-video playback); zero strict rows. No
Train/detail background appears behind any cinematic — all are full-screen
skill cut-ins over dimmed battles. All numbers below are quarantined
battle/cinematic tokens (damage popups ≠ base stats).

### Themis (`092`), skill cut-in thumbnail; HUD tokens quarantined

- **Source:** [blustone_jp post 1356527779781705728](https://x.com/blustone_jp/status/1356527779781705728),
  posted 2021-02-02 (POST-rebalance); video 638×1280, 14.2 s; thumbnail
  `pbs.twimg.com/ext_tw_video_thumb/1356176636538880001/pu/img/ZEUpIQAxqVl--gXL.jpg`,
  visually inspected 2026-10-05.
- **Visible frame:** silver-haired sniper woman, large red rifle, red
  bullet in clawed gauntlet, red crystals + dark beast behind; banner
  **"Armor-Piercing Ammunition"**. Portrait-level gear match to Themis;
  corroboration only.
- **Raw HUD tokens:** green-icon `3`, coin `23`, dimmed enemy bar `2927`
  with `x2`, small portrait token approximately `1996` (low confidence).
  Enemy unidentified, build unknown.
- **Status:** Cinematic/HUD observations only; no coverage credit.

### Estelle (`096`), skill cut-in thumbnail; HUD tokens quarantined

- **Source:** [blustone_jp post 1392041790094598147](https://x.com/blustone_jp/status/1392041790094598147),
  posted 2021-05-11 (POST-rebalance); video 640×1280, 7.9 s; thumbnail
  `pbs.twimg.com/ext_tw_video_thumb/1386581815205396483/pu/img/32wGC39YNPTNxrKu.jpg`,
  visually inspected 2026-10-05.
- **Visible frame:** red-haired fox-eared swordswoman with rapier, blue
  owl + butterfly; banner **"Flash Stab"**. Portrait-level match to
  Estelle; corroboration only.
- **Raw HUD tokens:** green-icon `1`, coin `6`, right-edge `x1` marker.
  Field meaning unproved.
- **Status:** Cinematic/HUD observations only; no coverage credit.

### Geranium (`064`), Short cut-in + VICTORY frames; era unresolved

- **Source:** [YouTube Short mFTmAXPz-dk](https://youtube.com/shorts/mFTmAXPz-dk),
  oEmbed title "the NEW ★4 Hunter Geranium!", author VisualShower Corp.;
  oEmbed carries no date — era unresolved, never normalize against the
  2019-09-05 rebalance.
- **Visible frames (all `i.ytimg.com/vi/mFTmAXPz-dk/` variants inspected):**
  `hq2` shows the dark-haired man in red/black coat, banner **"Whip Sword
  Strike"**, top-bar token `64`; `hqdefault`/`0`/`hq1` show his closeup
  above an **"ULTRA!!!"** gauge over a stage interior (double doors,
  green/red signs), red-circle `1`; `hq3` shows a **"VICTORY"** ribbon with
  circular portrait, badge `38`, name token **"Pabian"** (identity
  unresolved — player nickname, hunter, or NPC unknown; no catalog mapping),
  greyed button, pink "Okay" button.
- **Status:** Identity/cinematic leads only; no coverage credit.

## Old-APK mirror metadata anchors (2026-10-05, context only, no stat rows)

Full lane log: [`qooapp-apk-2026-10-05.md`](qooapp-apk-2026-10-05.md).
Listing-page metadata only; no binary downloaded, no stat panel surfaced.

### QooApp shared card (single entry, no stats)

- **Source:** [QooApp Blustone2 cards](https://apps.qoo-app.com/en/app-card/6128),
  one card by `Wong Zi Xian`, 2020-07-04 (POST-rebalance).
- **Raw tokens:** Player Name `友`; intro `？？？？为什么一直這樣子啊`
  (user complaint, not game data); counters 1 share / 0 likes.
- **Status:** No hero identity, no HP/ATK/DEF; cards route exhausted.

### Store version-code anchors (late spine only)

- **Source:** [TapTap all-info](https://www.taptap.cn/app/49376/all-info).
- **Raw tokens:** 2.8.0.1 = `28010` (2022-07-14), 2.8.0.0 = `28000`
  (2022-06-20), 2.7.9.9 = `27990` (2022-06-16); Android launch `2017-05-15`;
  vendor VisualShower Corp. / supplier HONGKWANPARK. Changelogs generic
  stability text, no balance notes.
- **Status:** Version anchors only; no downloadable old build, no stats.

### Oldest-mirror-build anchor (PRE-rebalance physical target, not fetched)

- **Source:** [ApkHere history](https://cn.apkbe.com/app/com.vshower.prd_sr):
  67 dated builds, tail **1.2.1.1 (2017-12-21)** → head 2.5.9.0 (2020-09-18).
- **Caution:** per-build size/date cells inherit the head template
  (1.4.4.1 down page repeats 104.3 MB / 2020-09-18, contradicted by the
  measured 94,877,834 B local APK) — sizes below the head row are unverified.
- **Status:** 1.2.1.1 is the cheapest PRE-rebalance download candidate
  (~21 months before the 2019-09-05 rebalance); low prior for embedded stat
  tables per the server-side-data finding. No coverage credit.

### Store-gallery spine + ApkHere tail rows (2026-10-05, impure anchors only)

Full lane log:
[`apkhere-gallery-2026-10-05.md`](apkhere-gallery-2026-10-05.md).
Listing-page metadata only; no binary downloaded, no gate bypassed.

- **QooApp gallery (POST pin 2.1.7.3 / 108.53 MB / 2022-07-14):**
  24 screenshot thumbnails inventoried, all sharing one generic caption —
  0 classifiable from text, video `5PyrPVT_Ofs` not played. No stat panel
  advertised. Source: `https://apps.qoo-app.com/en/app/6128`.
- **ApkHere tail + 1.4.x rows:** tail `1.2.1.1` (`12/21/2017`); all sixteen
  1.4.x rows `1.4.0.0` (`06/22/2018`) … `1.4.8.2` (`10/19/2018`)
  transcribed with dates; head `2.5.9.0` / `104.3 MB` / `2020-09-18`.
  Family counts corrected to 1.2.x = 11, 1.3.x = 14, 1.4.x = 16 (total 67).
  Source: `https://cn.apkbe.com/app/com.vshower.prd_sr`.
- **Stahuj row:** `2.5.7.0` / `103 MB` / `17. 2. 2020` (POST); 4 page thumbs
  + 7-preview gallery (prior 7-image inspection stands).
- **ProDroid row:** `2.7.9.2` / `1.08 GB` page claim / `29 Nov 2024` (POST);
  7 generic thumbs + video `vsiZlUIOg_E`; description `90` huntresses is
  marketing text, not a catalog count.
- **BrowserCam:** live URL now `404`; archived `2.0.5.1` / `2018-08-22`
  (PRE) 3-image inspection stands.
- **Status:** version/date/size anchors and gallery inventories only.
  No hero, accessory, or monster values. No coverage credit.

## Episode scripted monster rows (2026-10-05, impure rebalance material only)

- **Source:** `analysis/recovered-reference/EPISODE_STAT_ACTORS.json`
  (original `R_EPISODE.jet`, SHA `7f4362cd…`), manifest-scoped as an
  **Episode-only actor STAT table**, joined to per-appearance
  level/rank/hyper context in `EPISODE_COMBAT_CB*.json`. Full per-row
  adjudication: [`episode-stat-adjudication-2026-10-05.md`](episode-stat-adjudication-2026-10-05.md).
- **Raw content:** 37 monster-like scripted rows (34 `M*` res + 3
  enemy-placed Vincent `C010`): e.g. M001 150/130/100 @r1 (single tutorial
  appearance); M100 16000/7000/300 vs 20000/8000/280 @r5; M034 across
  100/7000/13000/16000 HP in four appearances (one, `CB0002_M01`
  100/100/100, is defined but placed in zero combat records).
- **Why impure:** same-`res` values disagree by up to 160x (M034); thumb
  level does not predict STAT (M062 ATK doubles while thumb level falls
  20→1; `CB1301_M1` vs `CB1501_M2` differ at identical L20/r5/h2); 20 of 22
  distinct `res` IDs lie outside the 22-monster catalog (only M001/M100
  intersect); no row is tied to an observed full-HP bar or rendered native
  combat.
- **Status:** Rebalance/scaling hypotheses only. Monster strict coverage
  stays **0/22**. Never quote these as base stats.
- **M034 variance + orphan probe (2026-10-05, impure):** full per-appearance
  file [`m034-variance-2026-10-05.md`](m034-variance-2026-10-05.md),
  re-verified from disk this session (STAT values under nested `stat`;
  **61** combat records — 47 `CB` + 14 `EVCB` — placement-censused; byte grep
  over every `recovered-reference/*.json`).
  - **Orphan, twice-proved:** `CB0002_M01` 100/100/100 @r1 (all-zero
    secondaries, `cool_time` 99000 — shared with 3 other rows, not 1 — and the
    sole `ref_id`-carrying M034 row, `034`) is referenced by **zero** combat
    records. It is the **only zero-placement row among all 151 identifiable STAT
    rows**, and its id bytes appear only in `EPISODE_STAT_ACTORS.json`. The
    `CB0002` fight itself fields just enemy-Vincent `CB0002_BOSS` + hunter
    `CB0002_C009`. It sits in the 4-record `combat_base: "mission"` tutorial
    family (CB0001–CB0004, all power 1000 / `game_res_id` 2) and shares rank 1 +
    all-zero secondaries + DEF 100 with `CB0001_M01` / `CB0001_BOSS`. Identity
    **doubly unresolved**: its `ref_id` `034` names hunter card 034
    ("Halloween Witch", 5 slots) while its `res_id` M034 has no art/catalog row.
  - **Placed M034:** `CB1501_M1` 7000/6800/280 @r5 (CB1501 L20/r5/h2 slots
    1+3 of a 5-slot wave + EVCB0301 slot 4 L1/r5/h0 reuse; nonzero enhance 20 /
    resist 10 — shared with `CB1501_M2`), `CB1002_M3` 13000/5500/280 @r5
    (CB1002 slot 5, hyper 1), `CB1301_M3` 16000/7000/300 @r5 (CB1301 slot 5,
    hyper 2) — **160x** HP spread; ATK 6800→5500→7000 and block_chance
    40.00→40.00→**35.00** are non-monotone at constant thumb L20/r5.
  - **Ladder-breaker:** M035's fourth row `CB1501_M2` 7000/6800/280 @r5 is
    numerically identical to the M034 row it stands beside (and shares its
    `cool_time` 8000, vs 5000 on the other three M035 rows), breaking the
    M035/M036 paired ladder (EVCB0102 3000/3500/200 @r4; CB1002 5500/4500/280
    @r5; CB1301 7000/6000/300 @r5 — identical per encounter, attr 1 vs 3).
  - **Shared-tuning groups:** CB1201 trio (M041/M040/M042) shares
    6500/6000/300 @r5; CB0501 quartet (M046/M052/M048/M054) shares
    1000/1200/180 @r3/role 2 — identical across *every* secondary, not just
    HP/ATK/DEF.
  - **Identity negative (new, corrects both this file and the parent):** local
    monster art is exactly `M001`–`M021` + `M100` and the catalogue exactly
    matches; of the 22 distinct Episode `res` tokens only **M001** and **M100**
    resolve to art + a catalogue row. **No `M034.jet` exists** — M034, M035,
    M036, M040, M041, M042 etc. have neither, so `res` is an opaque script
    token, not a resolvable monster identity.
  - All 18 rows in scope carry `"skill": []` and every placement
    `[0,0,0,0,0]`; era-tag unknown. Count per encounter/group, never per row.
    Four cross-record actor-reuse instances recorded (CB1501_M1→EVCB0301,
    CB1201_M1/M3→CB1401, CB0501_M2/M4/BOSS→EVCB0101, EVCB0102_M2→EVCB0301).
  - **Superseded readings** (do not re-import): CB1501 is **not** actor-free —
    scripted hunter `CB1501_C041` (L30/r5/h2/attr3) stands at slot 5 of the
    right wave; the wave is 5 slots, not 4; `EVCB0102_M2` has **2** placements
    in EVCB0102 (not 3) plus 3 in EVCB0301; `EVCB0301`'s title is
    `EV03_E01_TITLE`.

## Training/rank-up impure economy tokens (2026-10-05)

Full lane log:
[`training-rankup-rules-2026-10-05.md`](training-rankup-rules-2026-10-05.md).
Rebalance/economy context only — **no base-stat credit**. Era tags use the
2019-09-05 rebalance threshold. Local fixtures carry no era.

### blustone.jp guides (POST era)

- **Training (POST, [2019-12-11 capture](https://web.archive.org/web/20191211104454/https://blustone.jp/%E8%82%B2%E6%88%90%E8%AB%96/%E3%83%88%E3%83%AC%E3%83%BC%E3%83%8B%E3%83%B3%E3%82%B0)):**
  max 5 partners/session; ★1–★2 fodder recommended; max-level → rank-up.
  No cost/XP numbers. Matches the native/local 5-cap.
- **Rank-up (POST, [2019-11-13 capture](https://web.archive.org/web/20191113131941/https://blustone.jp/%E8%82%B2%E6%88%90%E8%AB%96/%E3%83%A9%E3%83%B3%E3%82%AF%E3%82%A2%E3%83%83%E3%83%97)):**
  ★5 ceiling; N same-★ partners for ★N; level resets to 1; new skill; ★4+
  unlocks equipment; batch rank-up for ★1–★2 without max level; ★3 release →
  **8 Chu-coins** → **two ★3 trainers** (→ 4 coins/trainer) at the Secret
  Market. The coin/trainer rate and ★4-equipment rule are new numeric leads;
  original-server proof unestablished.

### Namu KR text lane (ERA-UNKNOWN unless dated)

- **Source:** [Namu hunter mirror](https://d.namu.moe/w/%EB%B8%94%EB%A3%A8%EC%8A%A4%ED%86%A4/%ED%97%8C%ED%84%B0)
  (full tables in `namu-kr-blogs-2026-10-05.md`).
- Grade titles 1★ Novice → 5★ Master; natural-born max 4★; advancement needs
  same-grade count = star count; char cap Lv30 regardless of grade (visual
  anchor: PRE 2018-12 Natalia 3★MAX screenshot).
- Fixed-recruit traces 1★ 20 / 2★ 40 / 3★ 80 / 4★ 160; self-overcoming metron
  pairs (1★ 5/50, 15/150, 45/450; 2★ 7/70, 25/250; 3★ 9/90, 30/300, 80/800;
  4★ 12/120, 40/400, 110/1100); skill-training role-mat bands + 10/grade caps;
  equipment-enhancement rupee/toolbox breakpoints (500→1000→5000→15000→
  30000→100000; toolbox 130/10 at 40–49; remodel/10; guild discount).
- Sell: 1–2★ rupees, 3★+ secret-corner coins, Lily&Lala 12 coins → 5 traces.
- Gacha 30 single / 300 bundle(11); stim-pack 3000 (2019-04 = PRE); Rage 3
  (attacker/defender) / 4 (bomber/helper; Lily&Lala + Bear 036 excepted).
- Skill magnitudes: Lantern 10,000+ (5★ crit skill 4); Gullveig +7.5% ally AS
  (Hermes +15% → 22.5%; +Karl → 37.5%); Karl base AS 7; Haisen bonds 8%/16%,
  Chirrchirr 10%; Beckhen Fight Club +10% ATK/DEF/HP (375 chips / 5 traces).

### Screenshot-anchored rank-up prices (PRE, not promotion proof)

- 8000/12000 preview prices ([Caragublu Dec-2018](https://www.caragublu.com/2018/12/blustone-game-guide.html),
  both badges four-star; faded preview ≠ partial proof); 7,092 → 11,277
  ([Mugen 2017](https://freegame-mugen.jp/spapp/game_6433.html)); 1,417 →
  2,389 ([GameAppCH](https://gameappch.com/app/?app=04374) image 16).
  Likely Power-rating fields; polluted progression only.

### Local fixtures (no era, explicitly not original)

- Raise 100 gold/source, source XP 100×level, cumulative 100×(level−1);
  skill-up 100×destinationLevel; rank-up 1000/source + 5%/material.
  Fixtures preserving old thresholds, not captures.

## Bahamut 2018 roster screenshots (2026-10-05, polluted rating tokens)

Full lane log: [`bahamut-thumb-2026-10-05.md`](bahamut-thumb-2026-10-05.md).
Five `truth.bahamut.com.tw` attachments from the queued direction/roster threads
(`snA=76` ×4, `snA=223` ×1) downloaded HTTP 200 and pixel-read. All show the
Traditional Chinese 獵人名單 roster grid: header `owned/total`, per portrait a
`Lv. N`/`Lv.MAX` badge, ONE unlabeled large integer (same presentation as the
Naver max-level list's unassigned numbers — record as a roster rating token,
likely power/Strength, never HP/ATK/DEF), an element icon, and a state label
(鎖定 locked / 探險中 exploring / 防禦中 defending / 代表 representative).
Portraits carry no names; **no catalog IDs assigned**.

- **snA76-09c0bdf** (OP image-only post, 30/33): 5839, 5338, 1190, 1082, 7171,
  7483, 6870, 6823, 6667, 6597, 6401, 6045, 6039, 3904, 2831 (15 tokens).
- **snA76-628a9c99** (19/27): 2959, 2820, 2572, 2528, 2433, 2326, 2306, 1845,
  1701, 883, 861, 855 (12 full tokens; partial 5th row cut).
- **snA76-fc0cffb5** (27/42 part 1): 12549, **6601 (brown-bear-head portrait,
  Lv.22, exploring — medium-confidence `036` Bear per `C036.jet` photo-bear art,
  polluted only)**, 6413, 4648, 6045, 13184, 8182, 7565, 3953, 3412, 3129, 3089
  (12 full tokens).
- **snA76-1f4bec7b** (27/42 part 2): 2906, 2847, 2755, 2580, 2488, 2227, 2163,
  2146, 2103, **1977 ×2 (twin red-hood portraits, Lv.1 locked — duplicate-owned
  observation)**, 1249 (12 full tokens).
- **snA223-83e098e1** (20/33, 團體晉級 button): 5284, 4500, 2599, 2116, 3294,
  3044, 2515, 1084, 973, 846, 415, 343 (12 full tokens).
- 63 roster-rating tokens total. Image files preserved beside the lane log
  (`snA76-*.jpg`, `snA223-*.jpg`). **No base-stat coverage credit**: single
  unlabeled field, identities unassigned, gear/jewel/awakening unknown.
- Crystal thread `snA=348` (2021) is build advice only (Captain 6 DEF, twins
  4 ASPD + 2 ATK, mouse 6 ATK, Celine 6 DEF; 恢復 = in-ship regen, not heal) —
  jewel-lane context, no values. Queued guides `snA=59/58/60` are mechanics
  prose with no stat numbers.

## Short RG47CcM7c20 thumbnail (2026-10-05, animation frame, no panel)

- `mqdefault`/`hqdefault`/`sddefault` all HTTP 200 (4,677 / 7,442 / 30,749 B);
  largest preserved as `short-RG47CcM7c20-thumb-sd.jpg`. All three show the
  SAME frame: low-angle screaming rabbit-like creature with radial burst
  background, vertical-Short crop, maple-leaf player UI strip.
- Reading: awakening/transcendence animation frame consistent with the
  self-overcoming title context — **no numbers, no panel, no comparison**.
  Species resemblance to the Lottery-Mouse class is noted and NOT claimed as an
  ID. The titled panel remains uninspected; full video access still needed.

## Korean four-role name roster (2026-10-05, crosswalk aid, no stats)

Namu role pages (공격수/수비수/폭격수/도우미) yielded the working Korean ↔
catalog title list in [`bahamut-thumb-2026-10-05.md`](bahamut-thumb-2026-10-05.md)
§5 (Namu's own English readings kept; bracketed catalog mappings approximate).
Role mechanics captured as context: attacker 3 Rage front-only, defender 3 Rage
(Bear 4), bomber/support 4 Rage in-ship-only, unified support 3rd specialty.
**`시계초` retirement:** no roster name on any page resembles it — combined with
the passionflower common-noun finding, the ~00:52 panel reading is near-certain
a low-resolution misread. Do not search it further; re-read that frame against
the roster list when pixel access allows.

## Mining/polish impure cost tokens (2026-10-05)

Full lane log:
[`mining-costs-2026-10-05.md`](mining-costs-2026-10-05.md).
Rebalance/economy context only — **no base-stat credit**. Era tags use the
2019-09-05 rebalance threshold. `LEVELING.jet` res-1 is probability tuning,
never a cost table.

- **Jewel removal footer (visual, single-panel):** FAQ image22 footer reads
  `40000` (gold icon) / `40` (second currency icon, identity unknown);
  confirmed on image22 only. ERA-UNKNOWN. Removal fee, not a mining/polish
  price.
- **Community refine budget (TEXT-SOURCE, ERA-UNKNOWN):** FAQ L426 advises
  "at least 600k rupees" with fail risk rising "after level 9+". Player
  budget recommendation, not a per-attempt price; level-9+ escalation
  corroborates the native harder-at-higher-stage rule qualitatively.
- **Honor trace rates (Namu TEXT-SOURCE, ERA-UNKNOWN):** ★4 = 700 medals
  per 8 traces; ★3 = 350 per 8. Trace-exchange context, not mining/polish.
- **POST-era polish growth (official TapTap 2019-09-04 text):** ★1–3 mains
  +30%, ★4–5 mains +50%, all substats +50%, substat upgrades fixed at max.
  Growth multipliers, not prices or success rates.
- **Native polish-price schema without values:** `GetGemLevelUpPrice` rows
  carry `level, price_type, price, possibility, failed_compensation,
  add_sub_ability` (field identities recovered, no original rows). The
  per-stage rupee table, Manda mining price, and success-rate values remain
  the open gap.
- **Polish-parser pass 2026-10-05 (IMPURE, no new numerals):**
  [`gem-polish-parsers-2026-10-05.md`](gem-polish-parsers-2026-10-05.md) §1
  pins row literal addresses, per-field types (`level/price_type/price`
  uint32; `possibility/failed_compensation` uint64; `add_sub_ability` bool),
  the 0x28-byte record layout, the `(level, price_type)` lookup key
  (`FindGemLevelUpPrice`), and the `/gem/LevelUp` action route — but recovers
  NO original price, possibility, or compensation amounts, and isolates NO
  Manda mining-price route. No new impure numeral surfaced in this pass; the
  tokens above remain the complete impure set.

## Official board event economy (2026-10-05, PRE-rebalance, no coverage credit)

Full lane log: [`official-posts-2026-10-05.md`](official-posts-2026-10-05.md).
Two complete October-2018 official `bs.visualshower.com` event bodies recovered
from the archived `event_en` board (prior "board documents uncaptured" note
corrected — only the four character-intro `document_srl` posts stay missing).
Economy/event context only; no hero HP/ATK/DEF.

- **Lottery Mouse Likes Walnuts!**
  ([2018-10-25 capture](http://web.archive.org/web/20181025015633/http://bs.visualshower.com:80/?mid=event_en&document_srl=1003633&l=en),
  period Oct 12–26 2018): earn — 5 general stages (dispatch counts) → 1 walnut;
  1 Hunter Search → 3; 1 Abyss → 5; 1 recruit scroll → 6 (excl. Evaluation
  Request); Manda recruit → 45. Exchange 95/125 walnuts per trace box (Crocus
  125; Apollon/Dino/Calibur/Therapy 95); boxes hold 2–4 traces, lucky 40.
  Must exchange before the period ends. Replies ask for Heidi/Nene traces.
- **Jack's Treat!**
  ([2018-10-25 capture](http://web.archive.org/web/20181025175725/http://bs.visualshower.com:80/?mid=event_en&document_srl=1008954&l=en),
  period Oct 19–Nov 2 2018): 5 points per Fight Club use; 30 points → 30 Fuel
  or 1 Challenge Invitation. Cumulative victories (one-time each): 5 → 4
  Challenge Invitations; 10 → 1 Elite Request; 15 → 30 Metron Fragments;
  20 → 120 Fuel; 30 → 10000 Rupees; 40 → 1 Metron Crystal; 50 → 50 Manda;
  65 → 20000 Rupees; 80 → 3 Metron Crystals; 100 → 1 Special Request.
- **Board calendar:** both bodies embed the `event_en` index (page 1 of 23):
  ~15 dated Sept–Oct 2018 events (Halloween, October Package, recurring
  Lottery Mouse gifts / Clara weekends, gemstone/Recruit Hot Time/Fall
  Festival 10348 views, etc.). Existence leads only.
- **Negative results held:** char-intro posts 707457/426682/1082853/912433
  still uncaptured; no 2020/2021 `blustone.jp` event pages (EV05 schedule
  stays `R_EPISODE.jet`-only); TapTap 73656 snapshot unverified (CDX timeout);
  Inven captures confirmed via exact-URL CDX (177783 ×4, 212307 ×1) after
  availability-API false negatives — bodies not re-fetched; Namu histories
  unmined (403). Gacha/attendance rules not recovered on the board.

## Fight Club economy cross-check (2026-10-05)

Full lane log:
[`fc-economy-2026-10-05.md`](fc-economy-2026-10-05.md).
Rebalance/economy context only — **no base-stat credit**. Era tags use the
2019-09-05 rebalance threshold; every FC value below is ERA-UNRESOLVED.

### Tier rewards (Namu main-page footnote, ERA-UNRESOLVED)

- **Source:** mirror `https://d.namu.moe/w/블루스톤` (mirror HTTP 200,
  fetched 2026-10-05; page last-modified 2026-08-13, content spans
  2017–2021). Canonical `https://namu.wiki/w/블루스톤` (direct 403).
  Exact transcription in `namu-tables-2026-10-05.md` §§4–5; prose pointer
  in `namu-kr-blogs-2026-10-05.md` §2 (no conflicting number).
- **Raw tokens:** Silver 100 chips + 2 green manda; Gold 100 + 2;
  Emerald 150 + 2; Metron 150 + 2; Mandarin 200 + 2. Bronze entry absent
  (unrecorded, not zero-claimed).
- Tier-up = 6 wins regardless of losses; re-clearing 6 wins inside Mandarin
  re-awards. Scoring: win ≈ +15, loss ≈ −8, defense loss −5~6,
  revenge-loss/forfeit −8 (both Namu-derived sources agree).

### Rank rewards (31 bands, 1–30000+, ERA-UNRESOLVED)

- Same mirror/era as above; sole transcription (no second-source conflict).
- Top: rank 1 → 2500 chips + green manda 800; rank 2 → 2400 + 650;
  rank 3 → 2300 + 600, descending to rank 30000 Under → 100 + fuel coupon 1.
- Bonus-currency breaks: green manda ends at 4700; 고급 의뢰서 4701–10300;
  ornithopter fuel coupons below 10301.
- **255 anomaly:** band 551–720 reads 1000 chips + green manda **255** (sic),
  breaking the ...275 → 250 → 200 descent. Preserved literally, likely wiki
  typo; never smooth. No second source confirms or corrects it.

### Sunday settlement (operations context, ERA-UNRESOLVED)

- Settlement + reset every Sunday; rank payout after settlement only (both
  Namu-derived sources agree).
- 2018 World Championship reward detail body is empty in the archive
  ([2019-11-22 capture](https://web.archive.org/web/20191122162749/https://blustone.jp/%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88-%E3%83%95%E3%82%A1%E3%82%A4%E3%83%88%E3%82%AF%E3%83%A9%E3%83%962018%E3%83%AF%E3%83%BC%E3%83%AB%E3%83%89%E3%83%81%E3%83%A3%E3%83%B3%E3%83%94%E3%82%AA%E3%83%B3-2)):
  **no reward table recovered** (negative result, see
  `wayback-announce-2026-10-05.md` §2). No 2020/2021 event captures exist.

## Fight Club native-parser cross-check (2026-10-05)

Full lane log:
[`fc-native-2026-10-05.md`](fc-native-2026-10-05.md).
Rebalance/economy context only — **no base-stat credit**. Every token below
is ERA-UNRESOLVED (2019-09-05 threshold); shared numerals (6, 100, 150, 200,
15, 8) are NOT corroboration of any native parser field.

- **Verdict:** zero value-level agreements between the recovered native FC
  parsers (Enter/FindRival/Start/Complete/MyRank/season-units) and the
  Namu-derived tables; nine documented gaps. Parsers prove *where* economy
  values would land (Complete `{prev,cur}` pairs, league[]/weekly_reward[]
  reference rows, refresh_price); tables supply values under different names
  with no recovered key mapping.
- **Tier tokens (impure):** Silver/Gold 100+2, Emerald/Metron 150+2, Mandarin
  200+2 (mirror `https://d.namu.moe/w/블루스톤`, canonical
  `https://namu.wiki/w/블루스톤` 403). No tier-reward key in any native
  parser; replica refresh fixture (price_type 2 / price 100) is unlinked.
- **Scoring tokens (impure):** +15 / −8 / −5~6 / −8 unattributed to native
  `rating_point`; replica local policy is ±10 rating / +10 honor. Never
  overwrite the fixture from the table.
- **Rank tokens (impure):** 31 bands 1–30000+ share only band-shape with
  native `min_ranking`/`max_ranking`; all native reward cells read 0/empty
  and bonus currencies have no native key. 255 anomaly (551–720 → 255, sic)
  preserved literally.
- **Settlement token (impure):** Sunday settlement/reset has no native
  Sunday literal; only end_datetime seconds-units are natively proved.

## Transcendence PRE/POST diff impure tokens (2026-10-05)

Full lane log:
[`capa2-diff-2026-10-05.md`](capa2-diff-2026-10-05.md)
(plus prior [`guide-bodies-2026-10-05.md`](guide-bodies-2026-10-05.md)).
Rule/economy context only — **no base-stat credit**. Era tags use the
2019-09-05 rebalance threshold.

- **Capacity-transcendence rules (PRE, [2019-03-31 main guide](https://web.archive.org/web/20190331201909/https://blustone.jp/%E8%82%B2%E6%88%90%E8%AB%96/%E3%82%AD%E3%83%A3%E3%83%91%E8%B6%85%E8%B6%8A)):**
  same-name ★3+ hunters transcend the stat capacity; up to **3 times per
  rank-up**, base stats rise each time; done at the Midgard Gym via Hunter
  List; materials are same-name ★3+ hunter(s) + intact Metron crystals +
  Metron fragments + rupees (amounts unstated). Adjacent to (never merged
  with) Bahamut `snA=56` prose (≈ +10%/breakthrough, seven total copies,
  rank retained) and Namu metron-pair tables.
- **POST `/capa2` negative result (POST, [2019-12-16 capture](https://web.archive.org/web/20191216051555/https://blustone.jp/%E8%82%B2%E6%88%90%E8%AB%96/%E3%82%AD%E3%83%A3%E3%83%91%E8%B6%85%E8%B6%8A/capa2)):**
  single-capture subpage, title + nav + footer chrome only — **no prose,
  no table, no numeric token**. The PRE-vs-POST comparison is prose-vs-empty,
  not a rule change; no contradiction or confirmation of the PRE rules.
- **Status:** impure rule/economy tokens only; strict coverage unchanged
  (heroes 1/113, accessories 1/100, monsters 0/22).

## Episode scripted monster rows — M001/M100 insider (2026-10-05, IMPURE)

Full lane log:
[`m001-m100-insider-2026-10-05.md`](m001-m100-insider-2026-10-05.md).
Source: `analysis/recovered-reference/EPISODE_STAT_ACTORS.json` (152 rows) joined
to `EPISODE_COMBAT_CB0001/CB1201/CB1401.json`, via the 37-row adjudication in
[`episode-stat-adjudication-2026-10-05.md`](episode-stat-adjudication-2026-10-05.md).
Scripted per-appearance Episode tuning, **not** nude/base stats — **no monster
coverage credit (0/22 unchanged)**. Era-tags unknown against the 2019-09-05
rebalance threshold. Never join these HP values to video bar tokens.

- **M001 `CB0001_M01` (single L1 tutorial row, 4x placements in `CB0001`):**
  HP 150 / ATK 130 / DEF 100 @ rank 1, thumb L1/r1/h0/attr2, slots
  `[0,0,0,0,0]`; secondaries all zero (spd 0.00, crt 25/175, pen 0,
  enhance 0, block 0/0, resist 0, regen 0); STAT skill `[]` (empty).
  Weakest scripted enemy in the table; constrains tutorial tuning only.
- **M100 `CB1201_BOSS` (L10 boss):** HP 16000 / ATK 7000 / DEF 300 @ rank 5,
  thumb L10/r5/h2/attr2, slots `[0,0,0,0,0]`; spd 0, crt 40.00/200, pen 0.00,
  enhance 0, block 30.00/30, resist 0, regen 100; STAT skill `[]` (empty).
- **M100 `CB1401_BOSS` (L15 boss):** HP 20000 / ATK 8000 / DEF 280 @ rank 5,
  thumb L15/r5/h2/attr2, slots `[0,0,0,0,0]`; spd 0, crt 40.00/250, pen 0.00,
  enhance 0, block 30.00/30, resist 0, regen 150; STAT skill `[]` (empty).
- **A→B delta (impure, not growth):** HP +25%, ATK +14%, DEF *falls* 300→280
  as thumb level rises 10→15 at constant rank 5/hyper 2; crt_dmg 200→250,
  regen 100→150. No monotone level-scaling law; two independent tunings.
- **Reuse proof (pure context):** `CB1401` reuses actor ids `CB1201_M1`
  (M041) / `CB1201_M3` (M042) thumbed L15 where `CB1201` thumbs them L10 —
  one fixed STAT row serving two displayed levels, decoupling thumb level
  from STAT.

## Bahamut remaining threads (2026-10-05, impure training/evo/roster prose)

Full lane log:
[`bahamut-remaining-2026-10-05.md`](bahamut-remaining-2026-10-05.md).
Four mobile-mirror threads (`snA=336/56/230/90`); 12 attachments URL-level
only (not pixel-read). Rebalance/economy context only — **no base-stat
credit**. Era tags use the 2019-09-05 rebalance threshold; all values below
are unattributed player prose unless noted.

- **Max-EXP prose (snA=56):** 1★ 200 / 2★ 400 / 3★ 1200 / 4★ 4800 / 5★ 24000.
  Unverified player text; do not normalize against any XP curve.
- **Transcendence prose (snA=56 + B3):** each breakthrough ≈ +10% of the
  three stats (ATK/DEF/HP, explicitly not B/W/H); seven total copies;
  breakthrough rank retained on rank-up, not reset. Approximate prose.
- **Farm-stage prose (snA=56/230/90):** 36–40 rubi卷/metron fragments,
  stage 40 fodder + old-man traces, 66–69 mid materials, 126–129 / 166–169
  high materials; 16x-class map grind; stuck at stage 120. Stage claims only.
- **Healer comparison (snA=230, snA=90 replies):** Joy heals more than the
  Tidityl-class hunter. Direction only, no magnitudes.
- **Raise/freeze/shop advice (prose):** twins to 5★ then freeze; keep
  natural-3★; rabbit-hunter to 5★ first; Harley first (mirage-only relation),
  Beckhen first (PVP).
- **Attachment ledger:** 6 × `s01/202008/*` (snA=336), 3 × `s01/201801/*`
  skill/transcendence tables (snA=56), 2 × `s01/201806/*` (snA=230),
  1 × `s01/201802/*` roster (snA=90). All uninspected leads; no roster
  token transcribed here (prior 63-token set unchanged).

## Guide-body retry lane: transcendence rules + three confirmed-empty pages (2026-10-05)

Full lane log: [`guide-bodies-2026-10-05.md`](guide-bodies-2026-10-05.md).
Rule/economy context only — **no base-stat credit**. Era tags use the
2019-09-05 rebalance threshold. Budget was 4 capture-body fetches, all HTTP
200, none retried; all three prior empties are single-capture pages with no
alternate body.

- **Capacity-transcendence guide (PRE, [2019-03-31 capture](https://web.archive.org/web/20190331201909/https://blustone.jp/%E8%82%B2%E6%88%90%E8%AB%96/%E3%82%AD%E3%83%A3%E3%83%91%E8%B6%85%E8%B6%8A)):**
  same-name ★3+ hunters transcend the stat capacity; up to **3 times per
  rank-up**, base stats rise each time; done at the Midgard Gym via Hunter
  List; materials are same-name ★3+ hunter(s) + intact Metron crystals +
  Metron fragments + rupees (amounts unstated). First prose recovery of the
  limit-break loop in this lane. Adjacent to (never merged with) Bahamut
  `snA=56` prose (≈ +10%/breakthrough, seven total copies, rank retained)
  and Namu metron-pair tables.
- **Confirmed-empty retries (negative results):** crystal guide
  ([2019-12-10](https://web.archive.org/web/20191210184203/https://blustone.jp/%E8%82%B2%E6%88%90%E8%AB%96/%E7%B5%90%E6%99%B6),
  630 chars chrome only), party-formation guide
  ([2019-12-16](https://web.archive.org/web/20191216043116/https://blustone.jp/%E8%82%B2%E6%88%90%E8%AB%96/%E3%82%AD%E3%83%A3%E3%83%A9%E7%B7%A8%E6%88%90%E4%BE%8B),
  646 chars), FC 2018 championship reward detail
  ([2019-11-22](https://web.archive.org/web/20191122162749/https://blustone.jp/%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88-%E3%83%95%E3%82%A1%E3%82%A4%E3%83%88%E3%82%AF%E3%83%A9%E3%83%962018%E3%83%AF%E3%83%BC%E3%83%AB%E3%83%89%E3%83%81%E3%83%A3%E3%83%B3%E3%83%94%E3%82%AA%E3%83%B3-2),
  date stamp only). No reward table, no crystal values, no formation data.
- **Status:** impure rule/economy tokens only; strict coverage unchanged
  (heroes 1/113, accessories 1/100, monsters 0/22).

## Batch rank-up / Chu-coin impure economy tokens (2026-10-05)

Full lane log:
[`batch-rankup-chucoin-2026-10-05.md`](batch-rankup-chucoin-2026-10-05.md).
Rebalance/economy context only — **no base-stat credit**. Native batch
(`/gym/RankUpBundle`) and release (`/shop/SellCard`) parsers are symbol-mapped
but field/key-unproved; no Chu-coin literal and no Secret Market route exist in
the native tables, so none of these tokens has a proved wire key.

- **Release yield (impure, POST):** ★3 release → 8 Chu-coins; two ★3
  trainers per 8 coins (→ 4 coins/trainer) at the Secret Market. Source:
  blustone.jp rank-up guide 2019-11-13 (see lane log for archived URL).
- **Batch scope (impure, POST):** ★1–★2 rank-up without max level. Same source.
- **Preview prices (impure, PRE 2018-12):** 8000 / 12000. Both destination
  badges are four-star; the faded two-source preview is NOT partial-promotion
  proof. Source: Caragublu Dec-2018 guide (see lane log for URL).
- **Rank-up pairs (impure, PRE 2017, polluted progression):** 7,092 → 11,277
  (FreeGame Mugen 2017-09-13); 1,417 → 2,389 + Block Chance Up (GameAppCH
  review image 16). See lane log for URLs.
- **Coin-loop corroboration (impure, ERA-UNKNOWN):** 1–2★ sell for rupees;
  3★+ give secret-corner coins; Lily&Lala traces 12 coins → 5. Source: Namu
  hunter mirror §1.3. Direction only — no native reward key.
- **Local fixtures (NO era, not original):** rank-up 1000 gold/source with +5%
  stat bonus per credited material; raise 100 gold/source. Mechanism recovered,
  amounts fixture — never original balance.

## Gem LevelUp action pass (2026-10-05, IMPURE — no new numerals)

Full lane log:
[`gem-levelup-action-2026-10-05.md`](gem-levelup-action-2026-10-05.md).
Schema context only — **no base-stat credit**.

- **Pure result (negative on the wire fields):** `/gem/LevelUp` action symbols
  are fully inventoried with Ghidra addresses (`RequestGemLevelUp` 00a5811c =
  `(uint64, uint32, cb-with-pair)`, `ParseGemLevelUp` 00a5e43c = `(json)`,
  popup requester 00bd0bf4 = `(uint32)`, `UpgradeCB` 00bd2368, price lookup
  `(int, PRICE_TYPE)` 00a54f00). But NO request form key and NO response
  consumed field is recovered — no decomp dump of any action body exists, and
  the offline literal resolver was deliberately not run (UNPROVEN tool with
  known false-key modes). The existing authenticated `/gem/*` refusal must
  stay; `uint64~inst_id` / `uint32~price_type` remain unproved hypotheses.
- **Impure tokens:** none new. Impure set unchanged from the polish-parser pass
  (removal 40000/40, 600k budget, trace 700/350 per 8, POST growth
  +30%/+50%). No price, possibility, or compensation amount recovered.

## Sunday/settlement native-literal hunt (2026-10-05)

Full lane log:
[`sunday-settlement-2026-10-05.md`](sunday-settlement-2026-10-05.md).
Schedule/operations context only — **no base-stat credit**. Strict coverage
unchanged (heroes 1/113, accessories 1/100, monsters 0/22).

- **Pure result (negative on the schedule):** weekly window vocabulary is natively
  bound (`season_no`/`weekly_no`, six `*_datetime` numeric64 fields in
  `ParseSeason` G 0x942e24; `is_weekly_reward` in `ParseEnter` via ldr@00942d78
  → 0x1d732f4; `weekly_reward[]` + `min/max_ranking` in `ParseBattleWeeklyRwd`
  G 0x948b48; `end_datetime` seconds proved via `RemainTimeTextRenewal`
  G 0xc0c5cc). No `Sunday`/`settlement`/`reset-day`/`payout-timing` literal has
  a recovered arena consumer: `Sunday` 0x1dab860 sits in a libc/curl day-name +
  TFTP block (unbound), `arena_season_no` 0x1d913e1 has no consumer, and
  settlement/reset/schedule strings are absent outside C++ `Reset*` method names.
- **Impure tokens:** shipped UI text `Ranks as of Sunday 12 A.M. will be
  distributed their ranking rewards by Monday 6 A.M`
  (`all-tables.json` ~132204–132348, KO/JA/SC/TC rows present); Wednesday
  Fight Club ranking + Guild Blitz notices (~45024–45074); Saturday ticket
  recharge text (~244046–244121); wiki Sunday settlement + reset with payout
  after settlement only (mirror `https://d.namu.moe/w/블루스톤`, canonical 403,
  ERA-UNRESOLVED). Weekday words in UI text do not bind any parser field.

## Weekday schedule UI text inventory (2026-10-05)

Full verbatim inventory:
[`weekday-ui-2026-10-05.md`](weekday-ui-2026-10-05.md).
**Impure, ERA-UNRESOLVED** — schedule/operations context only, **no base-stat
credit of any kind**. Strict coverage unchanged (heroes 1/113, accessories
1/100, monsters 0/22). Read-only: `analysis/recovered-data/leveldb-tables/`
only; no server, APK, seed DB, emulator, phone, Ghidra or native library
touched.

- **Pure part (verbatim shipped rows, no interpretation):** 17 schedule-bearing
  rows across 15 keys in 2 tables, all five locales (`EN`/`JA`/`KO`/`SC`/`TC`)
  present. `UI_JSON_RO`: Sunday-12 A.M.-snapshot → Monday-6 A.M. ranking-reward
  payout notice, 2 Korean source sentences × 5 locales as `TX_TITLE` (SIZE 20,
  `COLOR 255|255|255|175`) and `TEXT` (SIZE 26, same alpha), keys/values
  132204–132361; Saturday-24:00 Dismount Pass recharge `해제권은|TX_LEAVE`
  (SIZE 18, `COLOR 255|255|255|230`), 244044–244121. `UI_TEXT_RO`: `TIP_4`
  Fight Club Wednesday ranking announcement and `TIP_8` Guild Blitz Wednesday
  registration, 45022–45074. Also recorded purely: three distinct in-string
  break tokens (literal `\n` in `TX_TITLE` EN/KO/SC/TC, literal `|` in `TEXT`
  SC/TC, none in JA/EN/KO `TEXT` or `TX_LEAVE`); the EN `TX_TITLE` row lacks a
  terminal period while the EN `TEXT` row has one; TC uses full-width `１２` in
  `TX_TITLE` and half-width `12` in `TEXT`; SC uses `星期日/星期一` in `TX_TITLE`
  and `周日/周一` in `TEXT`; and all five `TX_LEAVE` locale rows are
  **byte-identical Korean** (untranslated shipping defect, not a decode
  failure). Exhaustive weekday census: only Sunday, Monday, Wednesday and
  Saturday appear anywhere in the 13 recovered tables; Tuesday, Thursday and
  Friday are zero-hit in every locale. Zero weekday tokens in
  `SKILL_REF_RO`/`SKILL_TAG_RO`/`SKILL_EFFECT_RO`/`SKILL_DESC_RO`/`TAG_REF_RO`/
  `CHAR_STR_RO`/`INGAME_TALK_RO`/`ADMIN_ID_RO`/`UI_EPISODE_RO`/`UI_XML_RO`/
  `BADWORD_RO`.
- **Impure tokens, all with no native consumer:** T1 Sunday 12 A.M. rank
  snapshot; T2 Monday 6 A.M. payout (an implied ~6h settlement window in
  display copy only, not a server-enforced deadline); T3 Wednesday Fight Club
  ranking announcement; T4 Wednesday Guild Blitz registration open; T5
  Saturday 24:00 Dismount Pass refill (grant count, cap and timezone all
  absent); T6 `TIP_3` "every week" with **no** weekday, which therefore cannot
  arbitrate between the Sunday and Wednesday texts. Three distinct weekdays
  across three distinct systems means a future schedule model needs three
  separate rules, not one weekday — and Saturday falsifies any single
  "everything resets Sunday" simplification. Sibling rows identify the Saturday
  resource as Dismount Passes (`보석 해제에 필요한 해제권이 모자랍니다.`
  `TX_MD_BG` → `You do not have enough\nDismount Passes to remove the
  Jewel(s).`; `해제권 사용|TX_BT4_TX` under the `開採結晶` gem-mining heading).
  Explicitly excluded from the schedule set: ranking-band labels
  `랭킹 1위/2위/3위/4-10위/11-50위` (25 rows, labels only, no amount),
  `랭킹 확인|TX_O`, and `길드_탈퇴_확인팝업_설명` whose `24시간` is a 24-hour
  guild-rejoin **cooldown** that shares the `24` numeral with `24시` but is not
  a weekday. A future English-only scrape of these tables would have found zero
  Saturday evidence, because the Saturday rows are all untranslated Korean.
- **Unchanged negatives:** the Sunday/settlement native-literal negative still
  stands — `Sunday` 0x1dab860 / `Monday` 0x1dab82e / `Wednesday` 0x1dab83d
  remain an unbound libc/curl day-name + TFTP block with no arena consumer, and
  no `GetWeekday`/`tm_wday`/modulo-7 consumer exists on any inspected arena
  path. The Namu wiki Sunday-settlement prose and these shipped rows now agree,
  but agreement between two text sources is **not** native corroboration; do
  not upgrade this to a recovered schedule. Season length, season number,
  timezone, payout amounts, bronze tier value, gacha rates and login-supply
  calendar all remain unrecovered. `.jet`/`UI_CSV.jet` weekday text was not
  examined by this LevelDB-bounded pass.

## Official `event_en` board bodies pass 2 (2026-10-05, PRE-rebalance, IMPURE)

Full lane log with verbatim tables, archive URLs, capture timestamps and post
metadata:
[`event-board-bodies-2026-10-05.md`](event-board-bodies-2026-10-05.md).
Extends the earlier two-body pointer above (§"Official board event economy").
**Impure, PRE-rebalance (Sept–Oct 2018), no base-stat credit of any kind.**
Strict coverage unchanged (heroes 1/113, accessories 1/100, monsters 0/22).
Read-only web/wayback work; no server, APK, seed DB, emulator, phone, Ghidra or
native library touched.

- **Three more complete bodies mined** from the archived official board (only 2
  had been read before): **`989396` [Event] Midgard Fall Festival Event!**
  (2018-10-25 capture, post 2018.09.20 14:34, 10349 views — the largest event
  table yet), **`995273` [Event] October Limited Recruiting Hot Time!**
  (2018-10-21 capture, post 2018.09.28 14:30) and **`999764` [Event] Find Shiny
  Gemstones!** (2018-10-25 capture, post 2018.10.05 14:33). All three bodies are
  **plain text** — every table is real HTML, no numerals hidden in banner images.
  **Zero HP/ATK/DEF numerals in any of them.**
- **Impure economy tokens (raw values live in the lane log, not duplicated
  here):** attendance pays **Manda** 30/day for 9 days (**270** total), not Fuel
  or AP; any purchase during the event granted one **Legendary Request**
  ("★3 Recruit Guarantee"); a **17-row accumulation-rank ladder** of
  **Metron Crystals** + Manda/Rupees from 1st (12 crystals, 600 Manda) down to
  25601st+ (3 crystals, 5000 Rupees); rice-cake boxes at **15** cakes each holding
  **3~40** ★3 traces plus an element-keyed material (Flammable Material /
  Coolant / "Lightning Box"); an in-game package of **300 Manda for 100 Manda
  (300%)**, once per event; officially published gacha boosts of named ★4 pair
  **400% UP** and all ★3 **200% UP** (the two adjacent events **disagree** on the
  ★3 multiplier, 200% vs 400%, and the October post explicitly excludes a ★2
  limited hunter from the boost — preserved, not reconciled); and a **10+1 bundle
  bonus** that was 1 Metron Crystal in September but **10+10 traces** in October,
  so the bonus identity is event-specific. Player-thread numbers ("300 pull got 1
  silver", "wasted 1.2k manda", "4star drop rate less than 1 percent") stay
  **anecdotal**: **no base gacha rate is recovered.**
- **Jewel economy (why accessory coverage still does NOT move):** gemstone →
  jewel exchange costs **10 blunt → any blunt ★2 Jewel**, **5 ordinary → any
  ordinary ★3**, **3 shiny → any shiny ★4**, rare **radiant ★5**; dropped by
  clearing general stages *and* abysses, claimed from Schumann's special supply;
  "higher stages and harder levels will have higher drop rates". This is the
  first source binding the **jewel class names to star tiers**
  (`blunt ★2 / ordinary ★3 / shiny ★4 / radiant ★5`) — a **naming** fact plus a
  **drop cost**, not a jewel stat row and not evidence about `GetGemEffectName`
  selector ordering. Accessories stay 1/100.
- **Crosswalk leads with no numeric value:** ★4 hunters **"Lily & Lyla"** and
  **"Windblade"** named as boost targets; ★3 **Santa Clauster**, ★3 **Santa Girl
  Rebecca**, ★2 **Halloween Riko** as limited recruits. Note the prior lane's
  uncaptured char-intro post `426682` is spelled **"Lily&Lala"** — the two
  spellings differ and must **not** be merged into one identity without another
  source. **Legendary Request** joins the Challenge/Elite/Special Request and
  Metron Crystal/Fragments ticket taxonomy as a naming crosswalk only.
- **Exact `document_srl` map recovered for all 17 visible board rows** (plus 5
  stickies), listed in the lane log §2.1. Correction for future lanes: the `No.`
  column is a **display index, not an id** (No. 427 = `document_srl` 989396), so
  the earlier `#NNN` notation must not be used as an identifier.
- **Method negatives kept:** a CDX `?mid=…` miss is a **query-form false
  negative** — `http://bs.visualshower.com:80/?mid=event_en&document_srl=<id>&l=en`
  returns NO ROWS for ids that *are* captured under `/index.php?mid=…` and/or the
  permalink `http://bs.visualshower.com/event_en/<id>`; try all three forms before
  calling a board post uncaptured. Also: the body-closing tag in these captures is
  `<div class="rd_ft" >` (stray space), so an extractor keyed on `<div class="rd_ft">`
  silently returns an **empty** post; and `<td class="time">` needs `[^>]*` because
  the date cells carry a `title` attribute. Budget honoured: **4 body fetches,
  11 exact-URL CDX queries, one 503 recorded and left alone, no retry loops**.
  13 board bodies and pages 2–23 remain unmined and are **untested, not negative**;
  `75679` (2017.07.05, "[Notice] How to Use the Events Section") is the most
  likely of the unread ones to carry rules text rather than numerals.

## Jewel set-bonus help deltas, `CONTENTS11_8` (2026-10-05, impure rebalance material only)

- **Source:** the in-game jewel **set-effect help table**, record
  `CONTENTS11_8` / `res G_LI11_8` / `type contents`, `desc2` field, in both
  shipped client generations. 1.4.4.1:
  `analysis/VSFan/Extracted Assets (2026)/1441 (APK)/UI_CSV/3d98d128.json`,
  187,121 B, SHA `ce32b2ff…786c4`, locale keys `ko/en/jp/zh/zt`. 2.8.0.1:
  `analysis/extracted/assets/UI_CSV.jet`, 93,380 B, SHA `73a9dc47…4dac8`,
  locale keys `KO/EN/JA/SC/TC`. Full per-locale transcription with byte
  offsets: [`jewel-help-locales-2026-10-05.md`](jewel-help-locales-2026-10-05.md).
- **Raw content — 12 set-bonus families, mount 2 or mount 4.** 1.4.4.1 → 2.8.0.1
  (EN reference; KO/EN/JA/TC agree, SC does not):
  HP 5%→6%, Offensive/AP 5%→6%, Defensive/DP 5%→6%, Critical chance
  4.5%→6%, Fatal/crit damage 50%→60%, Block chance 4.5%→**5%**, Super Block
  → **Reduction** damage reduction 5%→10%, Elemental enhancement 23→35,
  Elemental resistance 23→35, Penetration 12→16, **Attack speed 1.72→1.72
  (unchanged)**, **HP regeneration 30→30 (unchanged)**. Relative factors:
  ×1.20 (HP/AP/DP/crit damage), ×1.333 (crit chance, penetration), ×1.5217
  (elemental), ×1.111 (block chance), ×2.00 for the reduction jewel measured
  from the EN copy. Every changed value rose; none fell.
- **Locale divergence is the strongest datum here.** In **1.4.4.1** the
  row-7 value is **9% in `ko`** (`철벽의 결정 - 4개 장착 시, 막기 피해량 9% 증가`)
  and **5% in `en`/`jp`/`zh`/`zt`**. In **2.8.0.1** `KO`/`EN`/`JA`/`TC` carry the
  revised table (Reduction 10%) while **`SC` still shows 9%** with the old
  numerals — so the 9% is a value that genuinely circulated, not a
  mistranscription, and the revision shipped **incomplete inside one client**.
  `SC` also keeps the old row order, lacks the `<color='241,26,90,255'>`
  wrapper the other four new locales carry, drops the `阻挡`/`ブロック` "block"
  qualifier from row 7, and changes `恢复量`→`恢复力` on row 11.
- **Era:** 2.8.0.1 = **POST** the 2019-09-05 rebalance (safe — recorded phone
  build, updated 2024-05-07). 1.4.4.1 = **PRE**, *inferred* from version code
  `1441` < `2.0` plus Blustone 2 (`2.0.x`) being a 2018 release; **no build
  date is pinned in this workspace**. Do not present the PRE tag as dated fact.
- **Why impure:** these are **help/UI copy strings**, i.e. set-bonus
  *definitions*, not any recovered engine constant and not a jewel-instance
  stat row. No native consumer was located; the values are rounded display
  integers with inconsistent unit discipline (`%` vs bare `23`/`35`/`1.72`/`30`
  /`16`/`12`); a help table can lag or lead the live balance table; and the
  one-corpus locale split is direct proof that at least one copy was wrong at
  some point. They describe **set aggregation**, not a hero, monster or item
  baseline.
- **Correspondence, not identification.** The official 2019-09-04 TapTap post
  (`stat-version-context.md`) says attack/defense/HP/elemental/penetration were
  strengthened while crit chance, crit damage, block chance and block-damage
  reduction got "smaller boosts", with no amounts. The measured family ordering
  matches that shape. But 1.4.4.1→2.8.0.1 spans far more than that one change,
  and the post supplies no numbers — so it cannot be used to derive any figure
  here.
- **Status:** rebalance-direction and cross-locale anchors only. Accessory /
  jewel-instance coverage stays **1/100**; heroes **1/113**; monsters **0/22**.
  Never quote these as base stats or reverse-apply the ratios elsewhere.
  A whole-corpus numeral sweep also reports 73 changed vs 84 unchanged help
  record ids, but that figure is **not** a balance signal — the new corpus added
  `<size>`/`<color>` markup numerals to most help strings and contaminates any
  naive numeral diff. Bounded positive check: of the `G_LI11_*` siblings,
  **only `CONTENTS11_8` carries a set-bonus numeral at all**, so no other
  jewel-help bonus value was revised.
- **Two corrections to `apk-diff-2026-10-05.md` §4**, both verified from disk
  this pass: (1) the CJK in these files is **valid UTF-8**, not CP949 mojibake —
  the earlier mojibake was a CP1252 read artefact, and the KO 9% reading did not
  rely on numeral-position inference; (2) `SC` does **not** retain the 1.4.4.1
  table "verbatim" — its 9% is the **KO** variant, and two further lines differ
  in wording. Also: the old **English** string has two missing `\n` separators
  (row 7 wraps; rows 9–10 merge), which is why the earlier line-based table made
  `Penetration 12` look orphaned; the family never left the table, it moved to
  entry 8.

## Official `event_en` board bodies pass 3 (2026-10-05, PRE-rebalance, IMPURE)

Four more official board bodies read (`document_srl` **1008972** Halloween in
Midgard!, **999762** Schumann's Marvelous Lootbox, **995291** October Package,
**75679** the "[Notice] How to Use the Events Section"). Full verbatim
transcriptions, per-body archive URLs, capture timestamps and event/purchase
periods live in [`event-board-bodies2-2026-10-05.md`](event-board-bodies2-2026-10-05.md).
**Every numeral below is economy / drop / gacha / shop context and adds ZERO
base-stat coverage** - hero 1/113, accessories 1/100, monsters 0/22 unchanged.
No HP/ATK/DEF value appears in any of the four bodies.

- **Attendance is event-parameterised, not a fixed daily amount:** **20 Manda/day
  x 15 days = 300 Manda** (Halloween, 2018-10-19 ~ 2018-11-02) vs the prior
  lane's **30 Manda/day x 9 days = 270 Manda** (September). Both paid in Manda
  through the Special Supply, both requiring an app restart per day. So there is
  **no original fixed attendance number**, and the replica's 28-day **100-gold**
  DailySignIn calendar (AGENTS section 83) has **no official counterpart in this
  corpus** - different currency, window and trigger. It remains a fixture, and is
  neither corroborated nor contradicted here.
- **Fuel is a spendable event currency and the box pays fuel back:** `1 Mystery
  Lootbox per 30 Manda or 200 fuel`, an 11-row `<Prize List>` containing
  `300 Fuel`, `1 Metron Crystal`, `10000`/`3000 Rupees`, `30`/`15 Metron
  Fragments`, `1 Legendary Request (3 star)`, `1 Special Request (2 star)`,
  `3 Elite Requests`, `1 Elite Request`, `3 Evaluation Requests`. **No
  probability, weight or box cap appears anywhere** - no lootbox odds recovered.
  The `200 fuel : 30 Manda ~ 6.67` ratio is a ladder reading only; no conversion
  route or rounding is recovered, and the local 10-AP `local_ap` fixture
  (AGENTS section 34) must not be used to convert it.
- **Weekly first-purchase bonus is original:** **1 Special Request + 40 traces**
  per week (UTC+9), trace identity switching mid-event. Original purchase
  counters therefore have a **weekly** reset boundary, and trace grants of **40**
  are original-scale - both far above the local `collect_qty` 10/20 fixtures
  (AGENTS sections 67/68). Different mechanic (purchase bonus vs exchange
  threshold); **do not "correct" the local fixtures from this**.
- **"Transcendence +1 on the first recruit"** for two named star-3 hunters is the
  first official statement of a free Transcendence/Awakening grant, and a naming
  crosswalk lead to the local `AwakeLevelUp` model (AGENTS section 29). Magnitude
  **+1** only; consumed resource, eligibility rule and reset scope **unrecovered**.
  Scoped to two named hunters, explicitly not a global star-3 effect.
- **Scoped gacha boosts resolve the prior lane's flagged contradiction:** star-3
  appears as **400% UP scoped to *limited* star-3** *and* **200% UP for *all*
  star-3 in the same October body**, and Halloween adds **500% UP for
  Halloween-limited star-3** alongside the same 200% all-star-3. The two numbers
  are therefore most likely **per-scope multipliers, not a contradiction**.
  Inference only - how scoped and global boosts compose is unrecovered, and no
  base rate is published anywhere.
- **10+1 bundle bonus identity varies by event (third data point):** 1 Metron
  Crystal (September) -> 10+10 traces (October Hot Time) -> **10 traces of one of
  two hunters, switching mid-event** (Halloween).
- **Two new official currency names:** **Fight Chips** and **Mirage Fragments**,
  **1,000 each** in the October Package, alongside `200 Manda`, `1,000 Metron
  Fragments`, `50,000 Rupees`, `1980 VP`. Naming crosswalk leads against the
  Fight Club/Arena local model (BP / honor / league, AGENTS sections 45/56).
  **Explicitly unproven: do not assert "Fight Chips = BP" or any other mapping.**
  `1980 VP` reads as a real-money store figure, making that post a **store
  package**, distinct from September's in-game "300 Manda for 100 Manda (300%)"
  offer - do not merge the two mechanisms.
- **One-time-per-user purchase is official twice** ("can only be purchased once
  per user"; "Limited to 1-time purchase only during the event"), so a per-user
  cap on named offers is original behaviour.
- **Metron currency is two-tier** (Metron Crystal vs Metron Fragments). That
  fragments accumulate into crystals is plausible and naming-consistent, but
  **no conversion threshold is recovered**.
- **Identity leads with their conflict preserved, not merged:** "star-2 Halloween
  Riko" (October Hot Time) vs "Halloween Witch Riko(★2)" (Halloween) - likely one
  hunter, unproven. **"Broom Witch Denali" is a new name absent from every prior
  lead and from the recovered catalog roster** used in AGENTS sections 24/67
  (001 Lantern, 002 Mowgli, 003 Nene, 004 Tyltyl, 005 Gerard, 006 Sylvester);
  crosswalk unproven. Jack-O'-Lantern is narrated as a *Lantern* skin ("putting
  a huge pumpkin on Lantern's head") - a narrative/skin lead that must not be
  turned into a new card id.
- **BOARD-IDENTITY FINDING (affects future mining):** the `event_en` notice states
  in the official voice that this section "was made for **forum events apart from
  in-game events**" and exists so players can "share away your screenshots".
  So (a) the five "sticky" rows are the current *forum* events, not a canonical
  in-game event list, and the `No.` ordering is a board sort rather than an
  event chronology contract; (b) these posts are **marketing-grade text** - good
  for what was advertised, never for a complete event schema or any probability;
  (c) **best next mining direction is attachments and comment images**, since the
  board's declared purpose is player image upload - this pass recorded 5
  attachment *filenames* and opened none. Note the two Halloween hunter-art
  filenames are **hash-named**, so identity must come from body text or from
  viewing the image, never from the filename.
- **Method correction to pass 2's URL-form advice:** for `1008972` and `995291`
  the `/event_en/<srl>` permalink has CDX captures that are **302 redirect stubs
  with no body**. "A CDX row exists" does not mean "a body exists" - a permalink-
  first lane can fetch a redirect and record a silent empty post, the same failure
  mode as the `rd_ft` stray-space quirk. The `/index.php?mid=event_en&document_srl=<id>&l=en`
  form returned the only 200 body for 3 of these 4 ids. Recommended order:
  `index.php?mid=` -> permalink -> `?mid=`, requiring `statuscode == 200`.
  `995291` again returned **no rows** for the short `?mid=` form while being
  captured under `/index.php?mid=` - second confirmation of the query-form false
  negative.
- **Original UI string, behaviour not modelled:** "You cannot open any more boxes
  when the event period is over" implies an unopened-lootbox expiry in the
  original; the local Special Supply model (AGENTS sections 89/90) has no expiry.
  Recorded as a string fact only - no change made, none implied.
- **Era note:** the three 2018 bodies are PRE-rebalance (Sept-Oct 2018).
  `75679` is a 2017.07.05 post observed in a **2018 revision** (eight captures
  2018-02-18 -> 2018-12-25), so its wording is not safely datable to 2017. None of
  this may be mixed with the 2019-09-05+ equipment/crystal multipliers.
- **Budget:** **4 body fetches, all successful, 12 exact-URL CDX queries
  (4 ids x 3 forms), 0 failures, 0 retries, 0 bypass attempts.** Nine board
  bodies remain unread with availability **untested, not negative**; board pages
  2-23 unvisited. No server/APK/seed/emulator/phone/Ghidra/native operation.

## Official board attachments, pass 1: no observations to record (2026-10-05)

**Pointer only; no new readings and no numeric duplication.** The recommended
direction in `event-board-bodies2-2026-10-05.md` section 2.6 item 3 was the
`event_en` board's attachment and comment images, on the theory that the board
exists so players can upload in-game screenshots. Full write-up with fetch
ledger, per-image pixel descriptions, archive URLs and negatives:
[`board-attachments-2026-10-05.md`](board-attachments-2026-10-05.md).

Result: **5 images opened (6 fetches, 1 hard 404 despite a 200 CDX row),
0 HP/ATK/DEF numerals, 0 stat panels, 0 player screenshots.** The three
640x200 three-panel images are official event-card art (a sword/board/hibiscus
trio, a nib/coat/hat trio, a scythe/jar/horn trio) with no on-image text; one
is a full-body promotional key-visual whose only text is the `BLUSTONE` logo,
the tagline `A BEYOND THE BOUNDS STORY` and a 2022 copyright line; the fifth is
a forum **card-minigame** screen whose only numerals are playing-card indices,
and whose text is multilingual (`LUCKY POT` plus Chinese and Japanese strings).

Reason the premise failed: the attachment namespaces are **board-shared**. The
`75605` prefix holds 158 archived images against 4 under `75603` (which is the
prefix `event_en` posts actually reference), and the `75605` cluster is
2021-2022 decoration from the other-language boards. Player-uploaded in-game
screenshots are simply **not captured** for this board, in attachments or in
comments.

Implication for this ledger: nothing here adds a polluted observation, and
nothing counts toward any coverage threshold. Also note the images are 2019-2022
board decoration, so they are **not** safely datable to the PRE-2019-09-05
balance era; a numeral from this corpus would have carried an unresolvable
balance era even if one had been present.

## Episode `res` crosswalk, all 22 tokens - identity closed (2026-10-05)

Full crosswalk: [`episode-res-crosswalk-2026-10-05.md`](episode-res-crosswalk-2026-10-05.md).
**Rebalance context only - zero base-stat credit, zero monster coverage.** This
closes the identity question the `m034-variance` note could only scope to
`M034`. **Monster strict coverage remains 0/22**, unchanged.

- **Identity question answered: NO.** The Episode `M*` `res` token is an **opaque
  per-appearance script token**, not a monster identity. Of 22 distinct tokens:
  **2** (`M001`, `M100`) have a local art pack and a catalogue row; **20** have
  neither; **0** resolve to an identity.
- **The "filename convention" claim is FALSE in both parent docs, now
  retracted in full.** `episode-stat-adjudication-2026-10-05.md` line 270 and
  `m001-m100-insider-2026-10-05.md` line 189 both still assert it as live text.
  The replacement measurement is an **asymmetry**: the `C*` (hunter-card art)
  namespace obeys `<res>.jet` at **64/64** tokens, while the `M*` namespace
  manages **2/22**. The naming rule is real and simply does not carry over.
  Corroborating negatives: no local pack stem even *contains* a token as a
  substring; **0 of 22** tokens appear in `native-all-strings.tsv` (which holds
  only three `M\d{3}` literals in 12 568 812 bytes - `M263`, `M701`, `M705`); and
  `EPISODE_S01.json` mentions **no** `M\d{3}` token and **no** `.jet` filename.
  There is no local binding table of any kind. Local art inventory
  re-measured: **774** `.jet` packs, of which **570** are `C*`-prefixed (113
  bare `C###` plus 457 suffixed forms such as `C001_Q`/`C036B`/`C051A`) and
  **22** are bare `M###`; a workspace-wide sweep finds those same **22** names
  in **154** files across **7** duplicated extraction trees, so no further
  monster art exists in any copy.
- **`ref_id` is disqualified as the alternative key:** **120/120** rows carrying
  it resolve to `analysis/catalogue/cards/`, **0/120** to `catalogue/monsters/`,
  55 distinct values. Only **3 of 34** `M*` rows carry it - `CB0001_M01`
  (`001`), `CB0001_BOSS` (`040`), orphan `CB0002_M01` (`034`) - and all three
  point at **hunter cards**.
- **The two "resolving" tokens resolve to a negative-result document.**
  `catalogue/monsters/M001.md` and `M100.md` both read `Identity: [UNKNOWN]`,
  `Base stats: [UNKNOWN]`, `0 rows match M\d{3}`. Do not read `art: yes` as an
  identity. The `res_prefix` = monster-id line in those files is `[INFERRED]`
  about the **server** field (an environment id per AGENTS s16.2), not about the
  Episode `res_id`, and must not be imported here.
- **New identity-unbinding facts beyond `M034`:** `M040` spans a tutorial boss
  and a chapter-12 mob; `M062` is the only token whose two rows disagree on
  `role`; `M023` holds HP flat while ATK/DEF rise with displayed level. All 72
  `M*` placements are right-side, `type: monster`, skill flags `[0,0,0,0,0]`.
  Row-count census: **7 tokens have >1 row** (`M023`2 `M034`4 `M035`4 `M036`3
  `M040`2 `M062`2 `M100`2), 15 are single-row; rows agree on `attr` 7/7 and on
  `role` 6/7, and disagree on `rank` 5/7 (`M034` 1/5, `M035` 4/5, `M036` 4/5,
  `M040` 1/5, `M062` 3/4).
- **Thumb-decoupling is real but MILD — do not overstate it.** The `M*`
  namespace covers **30 distinct thumb contexts** across 72 placements
  (levels 1/5/10/15/20/30), but the maximum distinct thumb contexts for a single
  token is only **3** (`M034`, `M035`, `M036`), and the busiest single context is
  shared by only **2** tokens (`M048`/`M054` at `20,3,0,3`; `M035`/`M062` at
  `1,4,0,1`; `M040`/`M100` at `10,5,2,2`; `M046`/`M052` at `20,3,0,2`;
  `M001`/`M040` at `1,1,0,2`). An earlier draft of the crosswalk claimed "up to 6
  contexts per token" and "12 tokens share `(20,5,2,1)`"; both are **retracted**
  — `(20,5,2,1)` is held by `M035` alone. Crosswalk §3.1b records the correction.
- **Two further cross-record reuse instances** (5th and 6th): `EVCB0301_M044` and
  `EVCB0301_M057` are placed **only** in `EVCB0303`; their actor-id prefix names
  a record that contains neither. They are also the only rows whose actor id
  embeds the `res` token verbatim.
- **Tuple corrections to carry forward** (verified against disk, replacing
  inferred secondaries): `M022` crt`20.00/180` blk`10.00/10` regen`5`;
  `M023` crt`20.00/200` regen`8`/`10`; `M049`/`M050`/`M051` regen`15`;
  `M044`/`M057` crt`30.00/200` blk`30.00/30` regen`50`; `M058` blk`30.00/30`
  regen`50`; `M062` `1800/750/160` blk`30.00/30` regen`25` vs
  `2000/1500/210` blk`20.00/30` regen`30`; `M100` crt_dmg`200`->`250`,
  blk`30.00/30` (not 35.00/35), regen`100`->`150`.
- **New table-level inconsistency:** `CB0501_BOSS` is the **only** row of the 34
  whose `block_chance` (`20.00`) differs from its `block_dec_dmg` (`30`). Do not
  assume the pair is equal.
- **Offence-weighted rows:** five rows have ATK > HP - the whole `CB0501`
  quartet `1000/1200` plus `M058` `2400/2600`.
- **False friend, read before any join:** 20 of the 22 tokens have a **hunter
  card row of the same number** (`M034`->card `034`, etc.), and `M001` collides
  with card `001`. Namespace collision, **not** a binding. The table itself
  disproves it by carrying both namespaces on one row (`res_id M001` +
  `ref_id 001`).
- **Era:** every row era-tag **unknown** against the 2019-09-05 rebalance
  threshold. Count per encounter/group, never per row; `M034` spans 160x HP.
  Never join to video bar tokens. `CB0002_M01` is the sole zero-placement row of
  all 151 identifiable STAT rows and must not anchor a curve.
- No server/APK/seed/emulator/phone/Ghidra/native operation; coverage files
  untouched.

## Dec-2017 roster reconstruction + release-date anchors (2026-10-05, IMPURE)
Full write-up: `roster-2017-2026-10-05.md`. Coverage impact **none**
(heroes 1/113, monsters 0/22, accessories 1/100 unchanged).
- **Roster identity anchors, not stats.** The shipped-art set for the Dec-2017
  cutoff (ApkHere tail `1.2.1.1`, 2017-12-21) is catalog IDs **`001`-`031`** =
  **30 named hunters + 1 variant row** (`026`, title "In Wonderland",
  `owner_card_id` `004` = Tyltyl variant). Composition: Offense 9 / Bomber 7 /
  Defense 8 / Support 6; Lightning 11 / Fire 10 / Ice 9; 1-star 11 / 2-star 9 /
  3-star 9 / 4-star 1 (Vincent `010`). **All four roles were populated**, so
  store copy advertising a "4-role team" describes the launch roster. Proven by
  two stamped Sept-2017 CDN manifests (27 packages, byte-identical set across
  stamps `20170904165634` and `20170908141924`) plus the four remaining IDs
  (`001`/`003`/`009`/`010`) proved APK-bundled by the held `1.4.4.1` APK -- the
  CDN set's complement inside `001`-`031` is *exactly* the APK set. Shipped art
  proves **no** stat and **no** playability: per-entity stat tables are
  server-side in every audited build.
- **Release-date anchors (community-harvested, second-hand -- use for ordering
  only, never to date a stat value).** `028` Octavia 30 Jun 2017 · `029` Kain
  31 Jul 2017 · `031` Diana 31 Aug 2017 are the only rows dated on or before the
  cutoff. Post-cutoff: `045` Yuri 9 Feb 2018 · `048` Dumble 9 Mar 2018 ·
  `049` Bright 23 Mar 2018 · `050` Therapy 5 Apr 2018 · `044` Heidi 26 Apr 2018 ·
  `052` Windblade 20 Jul 2018 · `057` Pansy 14 Sep 2018 · `056` Genovia
  29 Nov 2018 · `063` Erise 28 Feb 2019. **`044` before `048`: release order is
  not card-id order -- match by name, never by position.**
- **New cross-validation.** The Bahamut §5 Korean four-role roster carries its
  own per-hero dates, and two match the Miraheze index **exactly**: Dino `054`
  2018-06-29 ice, Apollon `055` 2018-08-17 fire. Two unrelated community
  sources agreeing to the day raises confidence in the date axis (which the
  `>= 032` upper bound leans on) without making any single date primary.
- **Upper bound is an inference, not a record.** Three legs: no `C032`+ hero
  package in the Sept-2017 manifest; first post-`031` dated release is Feb 2018;
  `032` Scar (2-star Offense Ice) adds no combination the range lacks. **Residual
  gap: no manifest exists between 2017-09-08 and the 2017-12-21 cutoff -- a
  14-week window. A late-2017 `032`-class hero is OPEN, not closed.**
- **Roster-rating tokens (one unlabeled integer per portrait) -- the dominant
  reusable material here.** Bahamut `snA=76` x4 (Feb 2018) + `snA=223`
  (May 2018) = **63 tokens**, transcribed in `bahamut-thumb-2026-10-05.md` §3.
  Field is **almost certainly a rating/power, not HP/ATK/DEF**: one integer
  where a stat panel shows three, and it tracks investment (MAX rows high,
  Lv.1 rows low) rather than identity. Identities unassigned -- portraits carry
  no names. **Era PRE-rebalance and inside the Dec-2017 roster's lifetime.**
  Ownership observations to keep: duplicate twin red-hood pair `1,977` x2
  Lv.1 locked; denominators `30/33`, `19/27`, `27/42` (x2), `20/33`.
  Medium-confidence Bear `036` match at Lv.22 / 6,601 (`C036.jet` photo-bear
  art) stays polluted-only.
- **Rank / power-up progression tokens (era-unresolved or PRE).**
  `7,092 -> 11,277` `Middle -> Advanced Hunter` `Lv.MAX -> Lv.1` (FreeGame
  Mugen 2017-09-13, the **only 2017-dated visual** found, video unavailable);
  `Power Upgraded` `2,628 -> 3,068` / `2,628 -> 3,947`, fodder
  `1,939`/`1,971`/`2,220`; transcendence Bear `036` `3,425 -> 3,969` fodder
  `2,568` (Caragublu); `3,014 -> 4,407` `Experienced -> Proficient Hunter`
  (AppStorio -- its `3,014` repeats as the rank-up start value, matching the
  `Power Upgraded` reading); `1,417 -> 2,389` `Block Chance Up` (GameAppCH
  img 16). Field still unconfirmed for all except Caragublu's label.
- **Independent roster-growth check.** Reddit 2020 clan-Discord gallery
  Offense/Defense `Strength`-sorted lists carry denominator **`98/105`**. It sits
  between the Dec-2017 roster (31) and the 2019-archive ceiling (`001`-`063`,
  62 rows + 1 placeholder) -- consistent with a mid-era capture. Row tokens
  already recorded above; no new rows this pass.
- **Crosswalk hazards found, do not repeat.** (a) `026` and `034` have **empty
  `name`** in `card-catalogue.tsv`; a naive name-keyed crosswalk silently drops
  them. (b) Bahamut §5 romanises `056` as **"Zenobia"** where the catalogue says
  **Genovia** -- match on ID, not name. (c) `칼바람` / "Khalbaram" has **no
  catalogue match; no ID assigned**, do not invent one. (d) `C003_DIALOG` in
  `recovered-reference/EPISODE_S01.json` is a **dialogue resource family**
  (`EP_DIA_4` + `C003_DIALOG`), and the `010` hits in that file sit inside the
  literal `CB0101` -- it is **not** episode-actor evidence for `003`/`009`/`010`.
  (e) `analysis/extracted/assets/` `C001`-`C098` is the **final 2.8.0.1** build,
  not 2017 evidence.
- **Store/version anchors (listing metadata only, no roster content).** ApkHere
  67 rows, tail `1.2.1.1`/2017-12-21, head `2.5.9.0`/2020-09-18, families
  1.2.x=11 / 1.3.x=14 / 1.4.x=**16** (1.4.0.0 06/22/2018 -> 1.4.8.2
  10/19/2018), per-build sizes below head unverified template inheritance;
  BrowserCam `2.0.5.1`/2018-08-22 PRE, live URL now **404**; Stahuj
  `2.5.7.0`; ProDroid `2.7.9.2` (7 generic-alt thumbs, 0 classifiable);
  QooApp `2.1.7.3` 24 screenshots whose captions are all identical, **0
  classifiable from text**. ProDroid's marketing `90` huntresses is **copy, not
  a catalog count**. PRE = `1.2.1.1`/all `1.4.x`/`2.0.5.1`; POST = `2.5.7.0`/
  `2.5.9.0`/`2.1.7.3`/`2.7.9.2`. Every ID in the roster table is PRE.
- No server/APK/seed/emulator/phone/Ghidra/native operation; no mirror binary
  downloaded; no stat inferred from art.

---

## Pointer — `[Review]` / `share_en` board pass, 2026-10-05 (no numeric reading)

Full write-up: [`review-posts-2026-10-05.md`](review-posts-2026-10-05.md).

**No HP/ATK/DEF tuple, no monster stat and no accessory row was recovered, so
nothing numeric is duplicated into this ledger.** Recording the pointer and the
specific tokens a future reader must not mistake for observations:

- `event_en/148274` body (archived, 200, read 2026-10-05) carries
  **`Denner` `Lv. 1` `0/100`**. This is a *Guess-that-Hunter* forum entry, the
  post is titled **"My guess"** and not `[Review]` as an earlier pass recorded.
  `Denner` is not in the recovered 001-006 catalog, so **no identity may be
  assigned**. `Lv. 1` / `0/100` are a guess slot, not a hunter stat; gear state
  unknown and irrelevant. Forum counters `Views 30`, `Votes 0`.
- `share_en/197745` ("Guide to Blustone", 2017-11-12) signature carries
  **`Alaiko` `Lv. 8 25/100`** and names **`Cyana, Fin, KronX`** plus
  `Father` as "hyper boosters". Author profile and team composition only; no
  stats attached to any of them, no level/rank/gear/jewel context.
- **All 15 `[Review]` posts (`142946`...`147073`) and both
  `[Arena special rank reward] Rank 10/11` (`199340`, `199521`) are absent from
  the Wayback archive under every status code and all three URL forms.** Hard
  negative; do not re-attempt and do not assume a stat panel was in them.
- **Open lead, deliberately unopened:** `share_en/197745` references **11 real
  in-game screenshots** under attachment prefix `565/745/197/` (plus named
  `Gym.png`, `Arena.png`, `Club.png`, `Ruins.png`, `Cruising.png`,
  `Cruise_beginning.png`, five `Screenshot_2017-11-11-*.png`). The fetch budget
  was exhausted before any image bytes were requested. Subject suggestions are
  **filename inferences only, not pixel readings.** Post is dated 2017-11-12,
  i.e. **pre-2019-09-05**, so any stat panel found there belongs to the older
  balance era of `stat-version-context.md`.
- `share_en` as a board was **never enumerated by any prior pass**: 105 distinct
  archived post ids, 833 CDX rows. It is the recommended next lane.
- Neither `148274` nor `197745` changes any coverage percentage. Hero stays
  1/113, accessories 1/100, monsters 0/22.

---

## Deko Boko `[Blustone] special move` cinematics — thumbnail-only pass (2026-10-05)

Lane log: `deko-thumbs-2026-10-05.md`. **20 of 21 videos sampled, 61 frames
pixel-inspected.** Thumbnails via `curl.exe` + local pixel read
(`i.ytimg.com/vi/<id>/{hqdefault,sddefault,maxresdefault,hq1,hq2,hq3}.jpg`);
120 files HTTP 200 `image/jpeg`, all `maxresdefault` a true 1280x720. Era from
the watch page `uploadDate` field. **No decoder, no full playback** — every
observation is a single frame. All 20 are **2018 uploads => PRE-2019-09-05
rebalance era** (`stat-version-context.md`), which tags every row below.

**Answers the standing question: none of these videos shows a Train / hunter
detail / stat panel.** The series is a fixed two-panel branding template —
left = character illustration over a *blurred warm interior* (same plate in all
20) with the `BLUSTONE / A BEYOND THE BOUNDS STORY` logo, no stat chrome at
all; right = one of four frame types (chibi skill card / English-name title card
/ orange splash / real in-game battle). The earlier lane's
`official-skill-frames-2026-10-05.md` expectation of full-screen cut-ins does not
describe this uploader's format.

### Purple-icon integer beside the `ULTRA!!!` control — a *negative* result worth keeping

Every battle frame shows a purple square icon with an integer. Readings:
Lapis `130`, Sylvester `128`, Balian `125`, **Rebecca `133`**, Scar `125`,
Mowgli `129`, Hermes `125`, Octavia `125`, **Rebecca (Santa Girl) `125`**,
Yuri `131`, Heidi `190`, Bibi `125`, Natalia `125`, Lily & Lyla `128`,
Vincent `190`. Not observed in the sampled frames of videos 07/11/14/15/21.

**This is demonstrably NOT a per-character base stat.** Videos 04 and 10 are the
same character in two costumes (base Rebecca `021` = `133`, Santa-costume
Rebecca = `125`); `125` is the modal value (7 of 15); and Heidi and Vincent both
read `190`. An unproved transient scalar — plausibly a computed/buffed attack
value, a skill-power figure, or a gauge count. Not SP: AGENTS-measured SP runs
`0.01`/s with max `10`, and skills cost 3-4 Rage. **Field meaning deliberately
not guessed.** Zero coverage credit; era PRE-rebalance.

### Corner counters, damage numbers, combo counts

Green counter `0`/`1`/`2` and a coin integer `0,1,6,7,9,12,13,15,16,17,20,24,28,
35,39,42`. Within a video the coin value sometimes rises (04: `9`->`15`; 14:
`9`->`12`; 18: `13`->`16`) and sometimes falls (01: `20`->`16`), so wave-counter
and score/currency readings are both consistent — **unproved**. Damage values on
unidentified enemies: 01 `256`/`139`; 04 `22`/`9`/`26`/`83` and `82`/`299`/`237`;
05 `23`/**`1320`**; 06 `15`; 07 `45`; 10 `3`/`3`; 18 `164`/`61`/`84`/`85`; 21
`160`/`145` and `126`/`231`. Combo `x3` (06), `x4` (18). Red kanji attack-name
overlays and the `ULTRA!!!` label are VFX/strings. Enemies seen (orange
fox-like head, brown mound, blue penguin/shark, small blue shark, white blob,
brown reindeer, blue bird, white chicken) are **unidentified** — monster coverage
stays 0/22. Video 13 `hq3` has an **opaque white rectangle** over the coin
counter; cause unknown, **not** read as a value.

### Identity corroboration — textual (strongest class in this set)

Five videos carry an on-screen English **name title card**, matching the Namu
Striker page: `Wandering Fighter Scar` (05, exact), `Balian` (03, exact),
`Elite Messenger Hermes` (08, translation variant), `Immortal One Karl Steiner`
(15, epithet variant), `Renegade Vincent` (19, exact). Video 04 vs 10 share face,
hair and bat wings across costumes, confirming Namu's Rebecca / Santa Girl
Rebecca split — **the Santa variant stays unmapped**. All 20 subjects are in
Namu's 공격수 (Attacker) list, so the inventory is coherent.
**No catalog ID was asserted from any pixel**; the ID column is inherited from
`striker-videos-2026-10-05.md`, and Scar / Octavia / Santa Rebecca / Yuri /
Chichi / Bibi / Windblade **remain unmapped**.

### Two unresolved anomalies

- **Video 07 (`051`)** shows a **white chicken on a perch** on the left panel in
  all 5 frames, with a blonde braided sunglasses-wearing chibi (apparent beard,
  low confidence) plus a small chicken on the right; video 08 `hq2` likewise puts
  a **rooster** left while the right is the rabbit-helmeted man. Either a
  costume/mascot, a chibi mascot form, a mislabel, or another character. Because
  `051` is the **one** hero with a verified base-stat row, **video 07 must not be
  used to characterise Beckhen in either direction.**
- **The left panel is not reliably the right panel's subject** (video 08). It is
  never valid identity evidence.

### Availability

Video 20 `s4-OmmRZJDM` is **genuinely unavailable**: all six thumbnail variants
HTTP 404 (1,097-byte error JPEG), oEmbed 403, and the watch page returns title
`"Sign in"` with no `uploadDate`. **Wayback CDX is non-diagnostic and not cited**
— a control query for a *known-live* thumbnail also returned empty, so CDX is not
indexing `i.ytimg.com` here. No date invented; video 19 already covers Vincent
for portrait purposes.

**Zero new base-stat tuples.** Heroes stay **1/113**, monsters **0/22**,
accessories **1/100**. Because the series is a cinematic montage, it is unlikely
ever to yield base stats; the equipment/gym-panel class is the better target. The
2 recruitment videos (`cnMBlXFd5W4`, `hnnxZmmPg0Q`) remain queued. No
server/APK/seed/emulator/phone/Ghidra operation.

---

## Pointer — `share_en/197745` "Guide to Blustone", 2026-10-05 (attached, ZERO pixels recoverable)

Full write-up: [`share-en-guide-2026-10-05.md`](share-en-guide-2026-10-05.md).

**No image byte is retrievable, so there is nothing numeric to duplicate into
this ledger.** All 10 image fetches returned HTTP 404 (4,727-byte `<!DOCTYPE
html` Wayback error pages, no PNG signature), and 5 CDX queries — exact URL
without and with `:80`, prefix `565/745/197*`, prefix `565/745/`, and a
domain-wide regex over **all status codes** — returned **zero rows**. The
identical query shape against `75605/303/534/001` (a namespace a prior pass
*did* download) returned 4 rows, so the negatives are sound. Live origin: HTTP
503. **Hard negative; do not re-attempt.**

Recording the pointer plus the specific tokens a future reader must not
misread as observations. Every item is **PRE-2019-09-05** (post dated
2017-11-12) per `stat-version-context.md`:

- **11 original upload filenames recovered from the archived body** (they are
  the `alt` attributes of the 11 attachments, not extra images — this corrects
  `review-posts-2026-10-05.md` §1.6, which implied ~16, and mis-transcribed
  `Gym.png`/`Club.png`): `Cruise_beginning.png`, `Cruising.png`,
  `Screenshot_2017-11-11-07-17-55.png`, `Ruins.png`, **`Training Gym.png`**,
  `Screenshot_2017-11-11-14-46-11.png`,
  `Screenshot_2017-11-11-14-46-43.png`,
  `Screenshot_2017-11-11-14-45-20.png`,
  `Screenshot_2017-11-11-15-07-52.png`, **`Fight Club.png`**, `Arena.png`.
  Two of these (Gym, Arena/Fight Club) were the filenames a prior pass
  speculated might hold stat panels. **Unknowable — no pixels exist.**
- **Named hunters with NO numbers attached, which must never be joined to any
  other source's values.** A name-only mention is the easiest way to
  manufacture a fake base tuple, so it is refused explicitly:
  - 3-star trace sources per the guide: **Hermes, Karl, Nene, Athena.**
  - Arena "offense team" list: **Hermes, Octavia, Vincent, Captain, Diana,
    Lantern, Patrone, Levi, Karl.**
  - Arena "defense team" list: **Athena, Nene, Kain, Captain, Akasha, Denali.**
  - Signature "hyper boosters": **Cyana, Fin, KronX, Father.**
  Several of these (Nene `003`, Vincent `010`) do appear in the recovered
  catalog. **No level, rank, gear, jewel or skill state is stated for any of
  them, and no stat panel was ever seen.** Zero coverage credit.
- **Grade/level indices, never stat values:** `1-star`…`5-stars`,
  Transcendence `T1`/`T2`/`T3`, skill levels `1 - 4` … `45 - 49`, and the
  `Guru 3` band gating Vincent's armour penetration. These index the guide's
  *cost* tables only.
- **Author/profile tokens:** `Alaiko`, `Lv. 8 25/100`; post counters
  `Views 1571`, `Votes 0`, `Reply 5`; dates `2017.11.12`, `2017-11-11`
  (uploader-side filenames, not device-clock or archive evidence), body capture
  `20180227140354`.
- **The genuine recoverable artefact is the guide's body text**, quoted verbatim
  in §1.5 of the write-up: fuel costs (6 then 7 per cruise run; 20 per Ruins),
  Abyss day-mapping and stage rewards (1/1/2/2/3 metron crystals), Abyss reset
  `30,000 Rupees or 30 Manda`, Advance fodder counts 1/2/3/4, the **full
  Transcendence cost table for natural 1/2/3-star**, the **full skill-level cost
  table**, skill-slot unlock by grade, and Arena rules. These are
  **player-reported prose, not pixel readings** - the honest tier for dated
  community claims - and several overlap values the replica currently treats as
  fixtures. **Recorded for cross-lane use; no server, fixture or test was
  changed.**
- **Method trap, reusable:** Wayback rewrites `img src` into `im_` form inside
  captured HTML **whether or not the image was ever captured**. A rewritten
  image URL in an archived body is not evidence that any bytes exist. Always
  require a CDX row, and always run a positive control before reading a
  zero-row result as a real negative.
- The **other** `share_en` lead stays open and untouched: **105 distinct
  archived post ids / 833 CDX rows**, still never enumerated by any prior pass.
  Extract per-post `alt`+`src` from the captured body HTML, and locate each
  post's *actual* attachment prefix - the `565` namespace is entirely empty.

**Zero new base-stat tuples.** Heroes stay **1/113**, monsters **0/22**,
accessories **1/100**. No server/APK/seed/emulator/phone/Ghidra operation.

## Cross-check IMPURE: Transcendence + skill-level cost tables (2026-10-05)
Full reconciliation: [`transcendence-skill-cost-2026-10-05.md`](transcendence-skill-cost-2026-10-05.md).
Coverage impact **none** (heroes 1/113, monsters 0/22, accessories 1/100) —
these are economy numerals, not stat rows. **Do not join any of these numbers
to any hero/monster/accessory observation.**
- **Two community sources, reconciled cell by cell.** `share_en/197745` (EN
  guide, post dated 2017-11-12, **PRE-2019-09-05**) versus the Namu 헌터
  table (**ERA-UNRESOLVED**). Agreement: **9 identical Transcendence
  crystal/fragment cells and 30/30 identical skill-material cells** across two
  languages/sites/era tags. Numbers double-sourced; **labels, rupees and
  duplicate counts remain single-sourced to the EN guide.**
- **Era tags do not match.** Never merge these rows across the 2019-09-05
  rebalance line; the Namu table has no usable date anchor.
- **Fragment:crystal 10:1 holds in both sources, but is table-scoped and
  redundant** (fragment = 10 x crystal in every cell of both), and the skill
  table has no crystal column at all. Do not generalise it to Metron spending.
- **Two resolved reconciliations:** the EN per-band fragment sequence
  `1,1,2,2,3,3,4,4,5,5` collapses to `1,2|3,4|5,6|7,8|9,10`, which **resolves
  the "five values for ten bands" pairing** recorded as unresolved in the Namu
  section above; and the apparent fodder-grade conflict (EN "duplicates only
  need 3-stars" vs Namu "same-grade hunter") is a **false conflict** — the
  original in-game help `CONTENTS4_3` states both clauses in one paragraph.
- **OPEN-1 / OPEN-2 left open on purpose.** The two sources disagree on the
  material cost of **exactly one skill level, level 25** (4 bronze + 1 silver
  vs 5 bronze + 2 silver) and on the top band label (`45-49` vs `45-50`). The
  EN guide's 4-star/5-star step gate for the 2nd/3rd transcendence is
  **uncorroborated**. Do not pick a side from these sources.
- **The original in-game help contains NO cost numerals** (all 73 records
  swept, `UI_CSV` `HELP_DATA` from the 1.4.4.1 APK) — it confirms gates and
  system rules only, so it cannot settle either open item. Unchecked extension:
  the shipped 2.8.0.1 corpus has `CONTENTS12_*`-`CONTENTS15_*` sections that
  were not swept.
- **Replica-fixture discrepancies flagged, NOT acted on** (no server change):
  the local skill price is `100 x level` (per-level) where the EN guide is
  banded 100-1000, and the local skill rows charge **zero materials** where
  both sources require role materials from level 5. The native price getter
  `roleVector[destinationLevel-1]` favours the per-level shape, so native
  evidence and community prose disagree and neither wins here.
- No server/fixture/APK/seed/state/emulator/phone/Ghidra operation. Only a
  read-only parse of an already-extracted local JSON asset (which is
  malformed by one surplus brace; parsed by record split, source unmodified).---

## Roster-window closure: `032`+ dated in-window records (2026-10-05)

Companion to [`roster-gaps-2026-10-05.md`](roster-gaps-2026-10-05.md), which
closes the 14-week window `2017-09-08` → `2017-12-21` left open by
[`roster-2017-2026-10-05.md`](roster-2017-2026-10-05.md) §1.8. **This subsection
records only the CONTAMINATED material from that lane.** The existence and
release records themselves (`036` Bear newly added 2017-11-08; `038` Santa Girl
Rebecca debut 2017-11-30; `051` Beckhen named 2017-11-08) are primary and live in
that file's §1. Coverage is unchanged: **heroes 1/113, monsters 0/22,
accessories 1/100.**

### Release-date anchors (contaminated)

- **Roster-count token, `36`.** Bahamut `bsn=33171` `snA=17`, **2017-11-03**
  22:05:19, verbatim 「這遊戲目前總共有36隻角色」 — "this game currently has a total
  of **36 characters**".
  <https://m.gamer.com.tw/forum/C.php?bsn=33171&snA=17>
  **Unreconciled.** `001`-`036` is exactly 36 rows, but `036` Bear was announced
  as *new* five days later, so the ID-space reading is self-contradictory; a
  player-pool reading is equally consistent. Preserve as a dated magnitude
  anchor only. **Do not date any ID from it**, and do not argue `032`-`035`
  existed on its strength.
- **Regional-release finding (method).** Same post, verbatim 「這遊戲繁中化約一個月
  了推出的時候是在5月」 — the Traditional-Chinese service opened ~Oct 2017, i.e.
  **inside** the window, and the game launched **May 2017**. Hence **Miraheze
  release dates are region-scoped, not global.** This is why `036`/`038`/`051` can
  be live in Nov 2017 while `045` Yuri is dated 9 Feb 2018, `048` Dumble 9 Mar,
  `049` Bright 23 Mar, and `050` Therapy 5 Apr 2018. Do not treat the community
  date column as an existence bound. This also qualifies the parent file's §1.4
  argument that two community sources agreeing to the day (Dino `2018-06-29`,
  Apollon `2018-08-17`) raises confidence in the date axis: the axis is real for
  one region and silent about others.
- **`034` official-vs-community CONFLICT (unresolved).** Bahamut `snA=17`
  2017-11-03 says 「萬聖節魔女莉可」 was 「前陣子萬聖節活動推出的限時金券角」 — a
  *recent* Halloween-event release, implying **Halloween 2017**. Official
  `event_en/1008972` (2018-10-19) is headed "1. New 2018 Halloween-Limited
  Hunters!" and lists `Halloween Witch Riko(★2)` — implying **2018**. Both
  preserved; not decided. A third reading is that "new" applies to the whole
  limited line-up, with `059`/`060` the genuine 2018 additions.
- **In-window official rows that only re-confirm `001`-`031`** (consistency
  check, no new IDs): `event_zh/139571` spot-the-difference, event
  **2017-10-13 → 10-16**, names 「卡因」 Kain `029`, 「奧賽蘿拉」 Acerola `030`,
  「杰羅得」 Gerard `005`, 「文森特」 Vincent `010` (body captured 2017-12-18).
  `event_zh` Sticky 「[活動] 蒂蒂爾的噗通噗通箱子」 2017.12.05 names 「蒂蒂爾」
  Tyltyl `004`. The pre-window English board (2017-09-14 capture) shows
  `[Event] Diana's Growth Period` 2017.08.31, `[Event] Special Search for
  Octavia!` 2017.09.07, and `[Event] Sunny in Midgard? … White Island x Blustone
  collaboration` 2017.07.18 — Diana `031`, Octavia `028`, Sunny `022`. The
  dedicated **Diana `031` growth event dated 2017-08-31** independently supports
  the parent file's 31 Aug 2017 date for `031`.

### Unresolved identity leads (do NOT invent a mapping)

- **`黑主`** — Bahamut `snA=17` 2017-11-03: the strongest attacker, 「目前遊戲唯一
  擁有無敵時間的技能」 (the only skill in the game with invincible time), obtainable
  by paying to 老手等級:英雄三 (~NT$18,000), and explicitly distinguished from
  「鷹男」 (= Karl Steiner `012`, "eagle man"). **No catalogue or Namu match.
  Unassigned.**
- **`蘭索恩`** — same post, paired with 「阿克沙」 (Akasha `008`) as a T1 support.
  **No catalogue or Namu match. Unassigned.**
- **`艾斯特` "Estelle"** — official `event_zh` Sticky 「[活動] 艾斯特的特別提案」
  **2017.12.01** (SmileV, 631 views). **Conflicts** with Miraheze `096` Estelle
  10 Sep 2020 and with English `[Event] Estelle's Special Offer` `990227`
  2018.09.21. Most likely an **NPC/shopkeeper** of the same name. Unresolved;
  do **not** map to `096`.
- **`抽獎鼠` "Lottery Mouse"** — recurring board mascot in in-window official
  posts `event_zh/194203` (2017.11.10), `/225275` (2017.11.30), `/234003`
  (2017.12.05). Candidate `084` Lottery Mouse *"Master of Recruitment"*, but
  **NPC-vs-card is not established.** Lead only.
- **`韋斯特菲爾` "Westfield"** — official `event_zh/206098` 「[活動] 韋斯特菲爾的訓練
  手套」 **2017.11.15**; English twin `[Event] Westfield's Boxing Gloves` `1003638`
  2018.10.12. The community index leaves `080` **undated**. Same NPC-vs-card
  question. Lead only.

### In-window player prose (already logged elsewhere; cross-reference only)

All from Bahamut `snA=17` 2017-11-03, PRE-2019-09-05 era, **player prose, not
measured values**: evolution costs `2★ 1000 / 3★ 3000 / 4★ 12000 / 5★ 60000`
(already transcribed in this ledger and in `video-loose-ends-2026-10-05.md` — not
duplicated here); 「一天只能換一次燃料券」 (one fuel-ticket exchange per day) and
「靠每4小時的體力補給」 (natural fuel supply every 4 hours) — **cross-check only,
never set the local `local_fuel_0` fixture from these**; arena advice (park the
weakest hunter on defence so points bleed) — prose; 「快速出隊要耗費的曼達」 (fast
dispatch costs Manda) — prose, no amount given.

### Still open

`032` Scar, `033` Patrone, `035` Joy, `037`, `039`-`050`, `052`+ have **no** dated
in-window record — open, **not excluded**. The final ~2.5 weeks of the window
(**2017-12-06 → 2017-12-21**) have no board coverage at all. Highest-value next
fetch: the `event_en/1008972` body, to settle the `034` conflict. No `032`+ base-stat
row was recovered by any of this; nothing here may be promoted toward the 70%
thresholds.

### Gem popup bindings pass (2026-10-05) — IMPURE, no coverage credit

Source: [`gem-popup-bindings-2026-10-05.md`](gem-popup-bindings-2026-10-05.md)
(ELF `libnative_core.so`, read-only `llvm-objdump`/`llvm-nm`, no Ghidra lock).
**Strict coverage UNCHANGED: heroes 1/113, accessories 1/100, monsters 0/22.**
Nothing below is a hero stat, an accessory row, or a monster tuple.

Every numeral and numeral-shaped observation from that pass, listed so the
impure set is auditable in one place:

| Observation | Site (ELF) | Status |
|---|---|---|
| `pair.first == 1` is the polish **success test**; the same value is passed as `CSRDataMgr::GetErrorStr(int,...)` | `0x0bc2384`, `0x0bc2456` | Structural result code. Corroborates the standing `result_code: 1` finding. **Not economic.** |
| STAT_BOX node field written as `3`, or `2` when `repeat == 1 && [gem_inst+0x28] == 0` | `0x0bc23e2`/`0x0bc23e8` | Discriminator. Field identity **unnamed**; do **not** inherit "main"/"sub" from the inventory parser. |
| `max_tries` request field = literal `7` | `0x0a482d4` | Client-side retry cap, shipped constant. **Not a price, not a probability.** |
| Pre-request gate threshold `0xe` (14) on `[this+0x7b8]+0x1c` | `0x0bc0c18` | Client-side level/permission gate. Uninterpreted. |
| `CMHashID` name offset `+8`; Korean comment template length `0x17` (23 bytes) | `0x0bc0086`, `0x0bc1f0a` | String-construction constants. |
| `Anvilheated(int)` renders a `'%'`-suffixed text on a float compare (`vsub.f32`/`vcmpe.f32`) | `0x0bc07f0`, `0x0bc0804`, `0x0bc0822` | **Formatting binding only.** The compared float's provenance is UNKNOWN; **no success-rate/possibility value recovered.** |
| `OnRefresh` uses `SRCalculationFloatString(float,unsigned)` and `SRGetNumberKMB(unsigned)` | `0x0bc198c`, `0x0bc1afc` | Interpolated **display** counters. `KMB` implies a magnitude abbreviation, but **no threshold numeral was read**. Formatter, not a stat. |
| Korean UI templates `[강화성공]메시지`, `[강화실패]메시지` (23 bytes each) | `0x1d6ea1a`, `0x1d6ea3c` | UI strings, KO locale. Not numerals. |
| `루피가 부족합니다.` (insufficient-funds Toast) | `0x1d61416` | UI string, KO locale. **Not a price.** |
| `보석 제련` (gem refining) localised string | `0x1d6e903` | UI string, KO locale. |
| `RE_GEM_RIGHT` / `RE_GEM_RIGHT2` greyscale styling | `0x0bbef8c` region | Affordability **styling**; no amount. |

**This pass added NO new economic numeral.** Its contribution is a *mechanism*
constraint for future balance readings: the popup's success/failure comment and
animation are driven by the `2`-vs-`3` STAT_BOX value originating from
`/gem/LevelUp`'s `pair<int,int>` (`error_code`, `repeat_count`), **not** by an
independent client-side probability roll. A future attempt to read a polish
success rate must therefore look at the **response**, not at this popup.

Retracted in that pass (recorded here so they are not re-introduced): the
earlier suggestion that the popup's `uint32` request argument is `price_type`
is **falsified** — `price_type` is absent from the exhaustive `/gem/LevelUp`
form-key list, and `CSRGem::FindGemLevelUpPrice(int, PRICE_TYPE)` is not called
on that path. See that file §1.6 and §3.

### VSFan audio / transcript pass (2026-10-05) - IMPURE, no coverage credit

Source: [`audio-transcripts-2026-10-05.md`](audio-transcripts-2026-10-05.md).
Full corpus: `analysis/VSFan/` = 172 MP3 (1,126.033 s) + 257 videos, of which
**exactly 8 videos carry an audio stream and exactly one contains speech**.
Method: `ffprobe`/`ffmpeg` 8.1.2 plus `faster-whisper` 1.2.1 multilingual
`small` and `large-v3`; every zero-speech verdict cross-checked against an
independent `volumedetect` level reading so it could not be blamed on a quiet
source. **Strict coverage UNCHANGED: heroes 1/113, accessories 1/100,
monsters 0/22.** Nothing below is a hero stat, accessory row, jewel-instance
value, or monster tuple.

Locators are repository-relative paths plus media timestamps. These are local
archive files; **no public URL exists for any of them.** Spoken numbers are
polluted leads only.

| Observation | Locator / timestamp | Claimed field | Status / uncertainty |
|---|---|---|---|
| Spoken countdown `10` | `Research/Blustone/Blustone Launch Ceremony.mp4`, 535.48-536.18 s | **none** - ceremonial countdown ordinal | `large-v3` + `small` agree; `avg_logprob` approx -0.31; crowd mic over music. Not a game field. |
| `9` / `8` / `7` / `6` / `5` / `4` / `3` / `2` | same file, 536.18-546.04 s | none - countdown | same |
| `3, 2, 1` | same file, 545.00-547.26 s (tail pass) | none - countdown | resolves `1`, which the full-file pass does not emit |
| `런칭!` ("Launch!") | same file, 548.00-548.64 s | launch cue, not a number | `small` places the same shout at 548.53-549.41 s |
| `4!` | same file, 547.05-547.45 s | none | **UNRESOLVED / not confirmed.** `small` only; `large-v3` emits no token there. Falls after `2!`, inconsistent with `10 -> 0`. Do not cite as a read numeral. |
| `하나, 둘, 셋` ("one, two, three") | same file, 570.96-572.14 s | none | **REJECTED as unreproducible.** `large-v3` transcribed the same region differently and a `small` region re-run produced nothing. Model artifact. |
| Scan hits for Sino-Korean `이` / `일` / `구` / `사` / `만` | ceremony transcript, e.g. 395.16 / 531.96 / 441.44 / 455.10 / 393.56 s | none | **Homographs, not numerals** (이거 "this", 제일 "most", 누구 "who", 사용 "use", 나만 "just me"). Listed so they are not re-raised. |
| `Thanks for watching` / `ご視聴ありがとうございました` / `You're welcome` / `Thank you` / `BEEP` | 7 extracted MP3s under `C021_SND`, `C022_SND`, `C028_SND`, `SND1` | none | **Rejected as ASR hallucination.** The two model sizes return *different* text for identical audio (`small` KO vs `large-v3` JA on `d4f45e5e.mp3`, language p=0.176), the same generic family recurs across unrelated packages, and reported `speech_sec` (29.98) exceeds several file durations. **Explicit retraction: do not claim these clips contain YouTube/creator narration.** |
| `Sort by Strength` (`TX_LI_TG2`), `Strength` (`TX_CH_TL`, `STRENGTH`, `TXT_INVEN_SRT3`), `Team Strength` (`TX_POWER`) | original localization `Extracted Assets (2026)/1441 (APK)/UI_CSV/7adedb12.txt` | **Strength/rating column label** | Grounds the *inference* behind the Naver `55/114` roster, Reddit `98/105` Offense/Defense lists and AppStorio `19/102` list as a rating field rather than HP/ATK/DEF. **IDs, level/rank and gear remain unresolved; tokens stay unassigned; no coverage change.** |
| `Power\nUpgraded` (`UI_TR_AT_TX`, `UI_EV_AT_TX`) | same file | **rank-up/advancement rating label** | Confirms the label is original for Caragublu `2,628 -> 3,068` / `2,628 -> 3,947`, AppStorio `3,014 -> 4,407`, GameAppCH `1,417 -> 2,389`, FreeGame Mugen `7,092 -> 11,277`. Those screenshots still do not print the label and identity/gear are unresolved. **No coverage change.** |
| `HP` / `DEF` / `ATK` as the EN abbreviations, with `현재 체력` (current HP) and `최대 체력` (max HP) as *separate* keys | `UI_CSV/e44ab8ed.txt`, 9 rows | stat-field labels | Makes a bare `HP` reading **ambiguous between current and maximum** outside a `TX_ST_TL1 "Character Attributes"` row. No value changes. |
| 12-attribute panel order `HP, DEF, ATK, Attacking Speed, Critical Attack Chance, Critical Attack Damage, Armor Penetration, Block Chance, Damage Reduction Block, Elemental Enhancement, Elemental Resistance, Regeneration` (+ `Strength`) | `UI_CSV/7adedb12.txt`, keys `TX_ST_SB1`-`TX_ST_SB12` | stat-panel field set | Gives a *plausible positional* mapping for the 62 archived 13-field rows, but those pages print none of these labels, so the mapping is **unverified** and no row is promoted. |
| Placeholder literals `10000` (`TRC_POWERNUM1/2`, `TRC_STAT1_1/1_2`, `TRC_STAT2_1/2_2`, `TRC_STAT3_1/3_2`) and `0` (`TX_ST_NM1`-`NM12`, `TX_SK_LI_AF/BF`, `UI_LI_IF_NM`), `15000` (`TX_MD_BN_NM`) | `UI_CSV/7adedb12.txt` | **none - design-time dummies** | Recorded explicitly so these are never mistaken for recovered stat data. |
| `Less than 30 / 60 / 90 / 120 / 180 sec.` and `More than 180 sec.` | `UI_CSV/e44ab8ed.txt`, keys `30초 이내` .. `180초 이내`, `180초 이상` | mission clear-condition **time** thresholds | Historical wording (1.4.4.1) for conditions the replica currently implements as local policy. Rule evidence, not a stat. |
| `At least 1 out of 11 is guaranteed to be a 2★ or above.` | same file, key `11명의 헌터를 섭외하시겠습니까?` | gacha guarantee | Original 10+1 wording says **2★**; the replica's current local bundle policy is 3★. Record the version difference; do not reconcile by assumption. |
| `Area 10`, `3★`/`4★` gates, `level 7 or lower` / `level 8 or higher`, `Guru 1`, dispatch caps `10` then `50`, `10+1 Jewels` / `11 Jewels`, shop reset `1st and 15th`, attendance `28 days`, input limits `64` / `8~20`, nickname `1~9999`, `%04d` channel, `%m/%d/20%y` | same file | rules / formats | Also note a **shipped KR/EN mismatch**: key `레벨 20 이하 …` carries EN `level 7 or lower`. Preserve both. |
| `Ruins' Special Effect: … offensive hunters is increased by 30%.`; `Excavation entrances … reset every day at 00:00 (GMT+9).`; `1 Metron Crystal … 10+1 pull!`; `★3~5 class Jewel` | `UI_CSV/7adedb12.txt`, keys `TX_CH_RU_SP`, `TX_CH_LF_INFO`, `EV_INFO`, `EVENT_SUBNAME` | area/event modifier, daily reset, event drop, gacha band | The only 4 EN rows in that file combining a stat keyword with a number. Not hero stats. |
| Sound-event FX table: 34 rows with `지연시간` (delay) and `볼륨` (volume); `EQUIP_LEVELUP` volume `0.3` vs `1` elsewhere | `UI_CSV/300e08f5.txt` | **none - audio cue timings** | Maps the game's cue vocabulary (`FX_GYM_TRN` 훈련 / `FX_GYM_RU2` 승급 / `FX_GYM_TRC` 초월; `GACHA_GET1/2/3` = 1성/2성/3성이상; `FX_UI_FUEL` 연료). `RASE-RESULT` is a shipped typo. Timings are not statistics. |
| 668 `Dialogue Text` prose lines x 5 locales with **zero numerals** | `Extracted Assets (2026)/1441 (APK)/DIALTU-{KO,EN,JP,ZH,ZT}/`, 17 files each | n/a | **Strong negative result.** The only 8-11 digit-bearing prose lines per locale are RGBA markup such as `<color='240, 20, 50, 255'>`. All other digits in these files are structural (`CardID` `009`/`010`/`047`/`052`/`056`, `wait duration:0.3`, `scr-fade duration:0.6`, `scale:(1.11,1.11,1.11)`). |
| 0 speech in 10/10 curated MP3s; 0 speech in 155/162 extracted MP3s; 0 speech in the 4 loud `STORY_TUTO` clips (mean -12.0 .. -14.0 dB) | `Audio/Blustone/*.mp3`, `Extracted Assets/**/*.mp3` | n/a | **Strong negative result, not a level artifact** - all these sources are loud. Corrects the prior note that the 10 curated tracks "were not independently transcribed": they are now confirmed **non-speech** cues. The `STORY_TUTO` audio-bearing cutscenes are **not narrated**. |

Corrections to existing VSFan notes, recorded here so they are not lost:
`vsfan-material-index.md` summarises the audio material as "ten MP3s" plus a
"30-second startup capture", whereas the corpus is 172 MP3 and 8 audio-bearing
videos; `vsfan-extracted-assets.md` calls `7adedb12.txt` a style table when it is
additionally the full 5-locale UI string table and the origin of the stat
labels; `e44ab8ed.txt` (820 rows) and `3d9fb02e.json` were previously
unaudited; and `Blustone Launch Ceremony.mp4` (612 s) had only been reviewed
visually - its audio is Korean event-room chatter with a launch countdown and no
gameplay content, and its monitor content is illegible at the source 360x640
resolution.

---

## Pointer - `share_en` panel sweep, 2026-10-05 (105 bodies; 21 namespaces control-proven dead; 28 REAL pixels decoded, all already mined)

Full record: [`share-en-panels-2026-10-05.md`](share-en-panels-2026-10-05.md).
**Pointer only - this pass contributes ZERO new hero / accessory / monster tuple.**
Hero stays **1/113 (0.9%)**, accessories **1/100 (1.0%)**, monsters **0/22 (0%)**.

### Relationship to the concurrent census - read this before trusting either file

A concurrent pass wrote [`share-en-census-2026-10-05.md`](share-en-census-2026-10-05.md)
over the same 105 bodies on the same day. **The two overlap heavily and neither
supersedes the other.** Duplicated, do not re-derive: the 4-source EXP ladder, the
advancement costs, the 3x3 transcendence numbers, the identity tokens, and the
conclusion that the `565`/`567` namespaces are dead.

What this pass adds, which the census does **not** contain:

| Addition | Why it is new |
|---|---|
| **The `565/134/197/` namespace** (`197134`'s 3 images) | Census probed namespaces but not this one. Also **31 individual files across 19 namespaces** byte-fetched, vs the census's 5. Same conclusion, ~6x the evidence. |
| **The `440600` Google-Doc is LIVE.** `export?format=txt` = 36,493 B; `export?format=html` = 31,038,481 B containing **28 base64 images that all decode with valid signatures.** | The census never mentions Google at all. **This is the only place in the entire `share_en` lane where real pixels were obtained.** |
| **A vendor statement about a native UI gesture.** `VSpang` replies in `42865`: the training screen's full stat list is shown by **swiping up**, and was under-exposed because "there is a slight glitch when viewing the stats". | Census lists `42865` as an unread *candidate*; it never fetched the reply. |
| **The Transcendence table as a vendor-authored HTML `<table>`** in `215324`, agreeing cell-for-cell with the community table the census took from `197745`/`138442`. | Upgrades an existing community-sourced matrix to **vendor-sourced**, and adds the grade-independence rule and the one-wing-per-transcendence affordance. |
| **`69900`'s dungeon -> trace band table, transcribed in full**, and triangulated against three other posts onto `31-40 = Sylvester`. | Census lists `69900`'s title only. |
| **`forum_en` - a different board with 131 distinct post ids**, control-verified, never enumerated by any pass. | Census has zero `forum_en` hits. **Highest-value open lead.** |
| **All 21 board rows 17 / 38-75 titles read** from the archived `<title>`; two turned out to be genuinely unmined and are mined: `138442` "Guide - Blustone" and `613470` "Fate? Webs and boosts". | Census lists these ids but does not transcribe `138442`. |
| **The EXP multiplier rule `x(n+1)` written out** (`200 -> 400 -> 1200 -> 4800 -> 24000` = `x2, x3, x4, x5`) in `138442`. | Census has the ladder's *values* from 4 sources; it does not have the *rule*. Turns 4 data points into a closed geometric law. |
| **Max level 30**, fifth voice, in `138442`: "The hero you want to advance have to be **max at 30 level**." | Tips C2 toward 30 (3 sources vs 1). |
| **A second full copy of the skill-cost table** in `138442`, with **carat tiers resolved**: `1 carat` = bronze, `2` = silver, `3` = gold, and all 10 bands' rupee + fragment columns matching `197745` exactly. | Upgrades a 1-source table to 2-source. |
| **Eleven community icon names crosswalked to game material names**, incl. the garbled **"So?shell" = `Unscathed Shell`** (matches `Unscathed_Shell.png` in `199711`'s hotlinks). Usable by the project's skill-material item work. | Census has the `vsfan.net` filenames as *unidentified icons* only. |
| **The Fate gate: no 4-star fate stories exist; fates are 5-star only** (`613470`, Kain/Diana/Joy/Athena). | Census treats Fate as neutral prose. This is a structural gate claim. |

### Impure tokens this pass adds - none is a stat row

| Token(s) | Source | Why it is not coverage |
|---|---|---|
| `23847 +4047`, `2866 +221`, `1103 +110`, `1522 +126`, `8.00 +1.72`, and the equipment tree Weapon Lv.40 / Armor Lv.20 / Accessory Lv.20 / jewels Lv.5-Lv.10 | `440600` FAQ image `faq-image08` (KO) | **Card identity unknown.** Already in the ledger as an anonymous triple; Strength, Attacking Speed and the level tree are additions to that anonymous record only. |
| **Label-order flag:** `AGENTS.md` records this panel as "HP/ATK/DEF `2866 / 1522 / 1103`"; the panel's own KO field order is Strength/HP/ATK/DEF/AS, so it reads HP 2866, **DEF 1522**, **ATK 1103**. | same | **Flagged, not corrected.** `AGENTS.md` deliberately left unedited by this pass. Worth a human check against the image. |
| `Radiant Speed Jewel`, `Required Cost for Remove 40000 / 40` | `faq-image22` | A **jewel instance** removal cost, not an accessory-name row. Jewels are a separate item class from the goal's 100 accessory names. **No accessory credit.** |
| `19 / 37 / 110 / 437 / 2182` runs and `114 / 222 / 660 / 2622 / 13080` fuel | `199711`, `201598`, `197134` + commenter | Derived grind costs, not entity stats. |
| `Diana` "all her statistics have increased" with **no value**, screenshots dead | `215324` | Same loss the census records. **Do not synthesise values.** Its 4 named images (`transc.jpg`, `trans2.PNG`, `di1.PNG`, `di3.PNG`) were individually fetch-probed this pass and are **404**. |
| The four **tier/grade** vocabularies still confusable: grade 1-5, transcendence T1-T3, veteran status, and the **gem tier names** bronze/silver/**gold/green/emerald**/blue | `24731`, `24901`, `22732`, `215324` | Names only. Note `22732` uses *emerald* where `24901` uses *green* for the same 4th tier. |
| `Fire > ice` (inverted) | `194024` RobyF 2017-11-10 | **Factually wrong** against vendor `55626`. Recorded as evidence the community was unreliable on this in 2017, and as the reason C4 in the panels file exists. |
| Element-2 named **"water"** by four community posts vs **"Ice"** by the vendor and the current client string | `1260`, `24901`, `198374`, `194024` vs `55626` | Naming drift only. The **advantage direction** agrees everywhere except `194024`. |

### Source-conflict register (impure, do not silently resolve)

C1 4*->5* advancement cost **60,000** (4 posts) vs **15,000** (`24731`, the earliest,
and the only one *about item shops*). C2 max level before advance **20** (`23265`,
2017-05) vs **30** (`194179` 2017-11, `138442` 2017-07, plus the project's own 3* Lv.30
screenshot - now **3 vs 1 for 30**). C7 skill-cost band edges `20-25/26-29/45-49` vs
`20-24/25-29/45-50` (`197745` vs `138442`; rupee and fragment columns agree in all 10
bands). C8 Fate bonuses **lost on sacrifice** (`24901`/`138442`, one author) vs
**permanent once unlocked** (`Arzack` in `613470`). C9 **no 4-star fates exist**. C10 the
element cycle has **four** naming conventions (Fire/Ice/Lightning, fire/water/lightning,
fire/electric/thunder, scissor/paper/stone) that all agree on direction once mapped.
C1 and C2 may both be one patch change between May and November 2017. Full table with
sources in the panels file 2.1. **The replica fixture was not touched**, and C8 cannot
be wrong in code because collection bonuses are neutral.

### Era

`share_en` bodies: all **pre-2019-09-05**. The `440600` FAQ document: **MIXED** -
created 2018-02-26, footer reads "last edited 21 / 09 / 2026", and it self-references
patch 2.6.5.0, so it is neither pre-rebalance nor the 2.8.0.1 balance. Its glossary and
equipment/jewel **architecture** are era-neutral; its Awakening costs, gem-pull prices
and recruitment guarantees are late-era. Nothing from it may be mixed with
`stat-version-context.md` multipliers or treated as 2.8.0.1 balance.

---

## Video victory/rating resample 2026-10-05 — original HUD ratings, still no base stats

Full method, verbatim frame transcriptions and offset corrections are in
[`video-victory-resample-2026-10-05.md`](video-victory-resample-2026-10-05.md).
Two previously recorded negatives ("Errorflame victory ratings seen but no
legible numerals"; "Ryu33s post-match cards, no individual payout numerals")
are **falsified**. Source media:

| Key | URL | Channel / upload | Native rendition used |
|---|---|---|---|
| ERR | <https://www.youtube.com/watch?v=9fUxOnlmwxg> | Errorflame gamer, 2017-12-15, 1832 s | itag 312 **608x1080** @52 fps |
| RYU | <https://www.youtube.com/watch?v=8fEo7cb7fTk> | Ryu33s, 2020-09-09, 605 s | itag 299 1920x1080 (game in a 504 px portrait strip) |

**Nothing below changes hero 1/113, monster 0/22, accessory 1/100 or jewel
instance 1/100.** All readings are ratings / progression / economy on
state-ambiguous screens.

| Observation | Locator / timestamp | Claimed field | Status / uncertainty |
|---|---|---|---|
| `Collected Rupees` **49, 53, 58, 58, 57, 55, 55, 57, 61, 52, 56, 61** on 12 campaign clears | ERR 00:02:21, 00:07:08, 00:08:20, 00:09:44, 00:12:58, 00:14:13, 00:19:20, 00:21:01, 00:23:47, 00:24:44, 00:26:23, 00:28:10 | **expedition clear payout (rupees)** | Narrow band across nodes 1-10 and across a party whose power more than doubled. One account, one session, 2017 build. **Not a per-stage table**, not power-independent, and **not comparable** to the FAQ Search `+1400`/`+2000` rows (different mode, and the 2019-09-05 rebalance sits between). **No fixture retune authorized.** |
| Party slot **rating** beside `Lv. n`, tagged `Lv. Up!` when levelling: 176-844 over 12 clears; a `Lv.12` hunter at **218** sits above a `Lv.4` hunter at **779** in the same party | ERR V02-V12 (see file section 1.2) | hunter rating | **Level and rating are independent fields.** Values animate within the screen (`321 -> 327 -> 328`). Progression reading, **not** a base stat. |
| `TEAM LEVEL UP` / `Lv. 2` / `Lv. 3` with `- Level Up Bonus -` **x30** on a red fuel-can icon; `Lv. 3` also prints `- New Area Unlocked - Midgard Ice Zone` | ERR 00:14:15 and 00:24:43 | Team-level bonus + area unlock | Icon matches the fuel meter (`102/60`, `153/60`) so `x30` reads as 30 fuel, but the icon-to-currency mapping is **an inference from shape, not a labelled value**. Third distinct level scale (Team / hunter / account) - keep separate. |
| `Power Upgraded 377 -> 503` (Raise), then `Advancement Successful: Amateur Hunter 503 -> Novice Hunter 743`, `New Skill Unlocked: Increased Chance of Defense`, ending `Train Teammate` at `Lv. 7` / `Strength 743` | ERR 00:22:13, 00:22:55, 00:22:59 | rating upgrade chain | Fodder/gear/jewel state unstated; `377` is a *trained* baseline. Result `Lv. 7` is lower than the `Lv. 12` seen at V07/V10, consistent with the community-documented grade reset but **not proven** here. |
| V10 header reads `Midgard Snowfields - Area 1` at **Team Level 3** with `Lv.3/Lv.12/Lv.8`, 3 s after V09 cleared `Area 8`, immediately before the Ice Zone unlock popup | ERR 00:24:46 | area label | **UNRESOLVED.** Natural reading is a repeat clear of node 1 with a trained team, but that is inference. Transcribed verbatim; do not renumber or use as a distinct Area-1 payout. |
| Fight Club VS cards, **8 `Strength` / 8 `Point` / 8 `Rank`**. Opponents: `Ramenman` **186529 / 1593 / 89**, `Graf` **163578 / 1531 / 100**, `TayOtaku` **170371 / 1694 / 73**, `HeroKing` **139135 / 1722 / 70**. Player `Ryuichiツ` in order: **129507 / 1459 / 115**, **139610 / 1489 / 110**, **135191 / 1504 / 107**, **141249 / 1520 / 102** | RYU 00:01:52, 00:04:34, 00:06:23, 00:08:13 | **player rating, ladder points, ladder rank** | Strongest result of the pass: for the **same account**, `Point` is strictly increasing (+30, +15, +16) and `Rank` strictly improving (falling number) across all four cards while `Strength` is **not monotone** (dips at R3). Therefore **`Point`+`Rank` = ladder pair and `Strength` = separate party rating**; `Strength` must never be substituted for either. The three-card subset looked monotone in all three fields - the fourth card falsified that reading. Strengthens the `TX_LI_TG2`/`TX_CH_TL`/`TX_POWER` `Strength` label as a *rating* column (hence Reddit 13/12 lists, Naver 55/114, AppStorio 19/102 are rating columns, not HP/ATK/DEF) **without resolving any single screenshot's field**. Point series is a pre-match standing, so **no per-win Point award is inferable** - no settlement screen was captured. |
| Fight Club opponent-camp HP countdown **7480 -> 6772** (also 7392 -> 6973, 7410 -> 6783); per-actor **8250, 7963, 8238, 8420, 8336, 8596, 6496, 6332, 7897, 7668, 7467, 7240, 7099, 6911, 6779, 6761, 5503, 5360, 5156, 5091**; actor levels **46 / 46 / 85**; damage pops 161, 97, 83, 152, 129, 107, 102, 21, 16, 56 | RYU 00:06:34-00:06:43, 00:08:26-00:08:31, 00:04:46-00:04:53 | opponent party combat stat | **Not a monster.** Actor levels 46-85 are far outside the 1-30 community band - a second independent reason to reject a campaign-monster reading. Source of these stats unknown. **No monster coverage credit; do not cross-assign to any recovered row.** |
| Fight Club surfaces: `Which side are you choosing to bet?` with a 1-6 counter dial, `Paused / Resume / Forfeit Game`, `Attack▼ / Defense▼` + `DEF DOWN!`, taunts `Alia can do it!` and `Why bootstrapping allows certain... Huh? I like that!` | RYU 00:06:43-00:06:49, 00:08:26-00:08:33, 00:04:46 | UI surface only | New original Fight Club UI, relevant to `fc-native.md` / `fc-economy-2026-10-05.md`. **No wager amount is printed** - the 1-6 dial is a slot selector, **not a price**; do not read a stake from it. `Graf`'s motto expands `TC` as `Tournament of Chaos`, i.e. a ladder-season name. |
| `Ready to Battle / Midgard Snowfields - Area 3`, fuel **102/60**, **three empty stars**, `Available Items` x4, ally `Lv. 7` (red `1st` badge, fire glyph) + `Lv. 3` (rabbit glyph) vs penguin / brown beast (fire glyph) / grey owl | ERR 00:08:30 | fuel, star state, role glyphs | **Medium confidence** role-glyph read; if correct it corroborates `card-enums.md` (1 Offense, 2 Defense, 3 Bomber, 4 Support) by shape, but **no native string crosswalk was done here, so NOT upgraded to RECOVERED**. Fuel `102/60` is an over-cap display reading. |
| Episode list: `3. About Flight Boss` locked with red overlay **`Midgard Snowfields Area 7 Clear!`**; `2. What's a Metron Worth?` / `1. What Should Metron Hunter Do?` both **`Less than 30 sec.`** with `N` ribbons; bottom `2` / `10` / `20` | ERR 00:14:25 | Episode mode star condition + prerequisite | Corroborates the `Less than 30 sec.` key already in the `e44ab8ed.txt` ledger row. Adds an **Episode star-condition wording and a stage-clear prerequisite**. Does **not** establish the `>=180 sec.` half, nor any Episode reward amount. |
| Attendance / daily goals: `Receive 20 Veteran Points per attendance day`, day-1 **x3000**, `Day 0/20`, `Day 5/10/15/20` **x2**, `Veteran Level Unknown` `0/20`; daily `Check In` **x1000** (paid out as `Received x1000` at 00:17:55), `Clear Areas 6/15` **x30**, `Receive Supplies 1/2` **x30**; major `Recruit Hunters 1/2` **x1**, `Buy Item 0/1` **x1000**, `Train Skills 0/3` **x10**, `Challenge 0/3` **x20**, `Receive Fuel Supplies BONUS!` **x30** ("Receive 100 more fuel everyday with the Fuel Package!"); `Rupee Current Amount 482`; `Rupee Lottery Ticket Current Amount 0` | ERR 00:16:00-00:16:06, 00:17:52-00:17:56 | attendance / daily-goal economy | Single account, 2017 build. The `xN` glyphs carry **currency icons whose exact currency is not always labelled** - only the `Check In x1000` receipt proves a rupee payout. **Does not validate** the replica's `local_fuel_0 / AP10` or 100-gold calendar fixtures. |
| Star-condition captions `Mission Complete` / `Less than 60 sec Clear!` / `All Teammates Survived`; 11 of 12 clears scored 3/3, V02 scored **2/3** with slot 3 unlit | ERR 00:02:21 (all three, ~50% scale); V02 slot 3 native | mission star conditions | Slot-3 string re-confirmed at native scale on V02; the other two captions were first read from a 300-px re-render, so **medium confidence**. Compatible with the 60 s threshold already in the `e44ab8ed.txt` ledger row. **No local star-gate fixture is validated by this.** |

Method note carried forward, because it is the generalisable part:
`yt-dlp --download-sections` on YouTube **DVR-style HLS manifests lands late by a
per-invocation amount** - two invocations of the identical window
`*00:02:08-00:02:30` returned content from 00:02:08 and 00:02:40 (+12.40 s),
proved by frame comparison against a full-length reference. Align every clip
before quoting an absolute timestamp. Separately, numeric HUD counters **animate
upward**, so a coarse sampler lands mid-animation and records a payout of `0`;
never sample a numeric field without stating whether it had settled.