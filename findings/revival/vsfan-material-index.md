# VSFan archive: learning-material index

**Review completed:** 2026-10-05. Source: local `analysis/VSFan/` folder, which remains untouched. The reviewed source inventory is approximately 1.07 GB across 8,551 files: 663 research documents/assets, 7,652 extracted resource files, 220 curated PNGs, 10 MP3s, five PCAPs, and `Intro.mp4`.

## Research reports

- [vsfan-research-material.md](vsfan-research-material.md) — five subcollections under `VSFan/Research`; full useful facts from 73 archived in-game help articles, 51 dated Blustone screenshots, both workbook sheets, package manifests, and other game/company materials. The 189-row hero-stat extract and 30-row Details sheet are kept separately as [vsfan-hunter-stats-raw.tsv](../hunters/vsfan-hunter-stats-raw.tsv) and [vsfan-hunter-details-raw.tsv](../hunters/vsfan-hunter-details-raw.tsv).
- [vsfan-extracted-assets.md](../resources/vsfan-extracted-assets.md) — three extracted asset variants plus APK provenance, in-game field definitions, historical jewel set effects, upgrade/jewel mechanics, story-actor identity leads, art packages, and extraction limits.
- [vsfan-packet-capture-findings.md](vsfan-packet-capture-findings.md) — all five captures, protocol/version/reslist deltas, useful endpoint families, encrypted-payload limits and sanitized handling notes.
- [vsfan-visual-audio-material.md](vsfan-visual-audio-material.md) — all 220 curated images, six representative Blustone UI captures, cross-game art, ten audio filenames/durations and the 30-second startup/loading recording. Exact PNG path/size/dimension/hash inventory: [vsfan-image-manifest.tsv](vsfan-image-manifest.tsv).

## Highest-value findings

### Hero and monster data

- The warning-named `Hunter Stats [BROKEN IGNORE].xlsx` is a **candidate source only**. Its 19 `Stats` names match 19 unique base catalog IDs and also appear in the 2019 Japanese archive. The `Stats` sheet has 189 labeled rank rows: 67 fully numeric, 22 all-`N/A`, 100 blank. Of the 19 `Base Bronze` rows, 10 are numeric and nine are `N/A`. It has no cited origin, capture date/build, defined level/rank mapping, or equipment state. Preserve every value as unverified rebalance material; it adds **zero** strict hero coverage.
- The 1.4.4.1 help and extracted DIALTU dialogue provide definitions and identity/story cues, not hero base tuples. Explicit actor leads include Nene (`003`), Vincent/“Unknown Man” (`010`), Lily & Lyla (`047`), Windblade (`052`), Genovia (`056`), with ID `009` still unnamed in these records. `Lantern` (`001`, `Char`) and `Lana` (`001`, `NPC`) are distinct actor types.
- Visual/resource families include Blustone hunter portraits, NPCs, locations and limited monster art for M001/M002/M005/M006/M008/M009/M100. None yields a source-backed monster HP/ATK/DEF row. The screenshot/video audit found identity and UI context, not new base-stat tuples.

### Jewel/equipment data

- `UI_CSV/3d98d128.json`, `CONTENTS11_8`, documents all 12 historical jewel set bonuses and their 2/4-piece thresholds. The 12-family observation target is met from this local in-game help. **Eleven are locale-consistent; Super Block is 9% in Korean and 5% in English, Japanese and both Chinese locales.** Keep the conflict and 1.4.4.1 version context; it is not proof of current 2.8.0.1 balance.
- The same help defines jewel/equipment roles and mounting/upgrading mechanics but supplies no per-accessory table, jewel quality/level rows, polish multipliers or instance stats. The 6/6 mounted-jewel screenshots remain examples; accessory stats remain 1/100.

### Protocol, resource and story context

- The 2017 Blustone captures expose the reference endpoint sequence for hero, level, item, monster, stage, mission, gacha, shop and reward data; the game API requests and responses are encrypted. They are useful protocol maps, not a source for numeric rows. In 1.1.3.0, `GetCardOvercome` appears as a new route.
- The two Blustone resource lists move from 140 to 149 package names, with 11 added, two removed and eight changed shared names. The extracted 2017 package trees and APK contain character/monster/UI art, but no readable card, equipment-instance or monster-stat table.
- BTBA installation traffic belongs to a distinct `_BTBA_PRD` product; BTBA and White Island session captures are TLS-only here. Press-kit/company files are useful for VisualShower product lineage and story links, not Blustone balance data.

## Strict coverage after this review

The active goal ledger remains [coverage.md](../hunters/base-stats-visual-hunt/coverage.md): heroes **1/113**, jewel set-bonus families **12/12 observed** (one localized conflict), mounted jewels **6/6 samples**, accessories **1/100**, monsters **0/22**. Polluted hero material, including the VSFan workbook, remains separate in [polluted-observations.md](../hunters/base-stats-visual-hunt/polluted-observations.md). No VSFan value was promoted to a strict hero or monster base-stat row.

The captures include account/session-associated fields; their research report omits tokens, cookies, identifiers and personal values. All five original PCAPs and every other source under `analysis/VSFan/` were read-only during this review.
