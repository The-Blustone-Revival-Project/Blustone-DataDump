# Blustone DataDump 2026-10-14

Stats and evidence snapshot as of 2026-10-14 (Asia/Jerusalem).

## Included

- **BLUSTONE-Stats.md:** historical hunter values, curated screenshot/equipment tables, original IDs and explicit unknowns.
- **BLUSTONE-Evidence.md:** source classes, coverage, conflicts, source hashes and reproduction instructions.
- **BLUSTONE-Stats.json:** all eight normalized datasets, derived estimate tables (113 hero at-draw rows, 100 accessory rows, 22 monster rows, 565 skill rows), curated source tables and machine-readable changes from the previous release.
- **RELEASE-MANIFEST.json** and **SHA256SUMS.txt:** reproducibility and integrity.

## Changes

Compared with 2026-10-11.2.

| Dataset | Added | Changed | Removed |
|---|---|---|---|
| hunter_identities | 0 | 0 | 0 |
| hunter_stat_observations | 0 | 0 | 0 |
| hunter_skill_reference | 0 | 0 | 0 |
| monster_identities | 0 | 0 | 0 |
| campaign_identifiers | 0 | 0 | 0 |
| episode_story_graph | 0 | 0 | 0 |
| episode_rewards | 0 | 0 | 0 |
| hunter_gear_identities | 0 | 0 | 0 |
| hero_at_draw_estimates | 0 | 0 | 0 |
| accessory_stat_estimates | 0 | 0 | 0 |
| monster_stat_estimates | 0 | 0 | 0 |
| skill_magnitude_estimates | 0 | 0 | 0 |
| curated_source_tables | 0 | 0 | 0 |


## Coverage and limits

121 catalogue rows /113 playable identities;22 monster identities;806 numeric historical claims;50 campaign IDs;147 Episode nodes;1070 symbolic skill records. Derived estimates added in this snapshot carry per-row class and confidence; fixture rows are excluded from the payload. New since 2026-10-11.2: a 3,626-screenshot manual transcription lane (73 batches, 119 stat-panel hits, 22 full triples) with back-calculated tier evidence, explicit conflicts, and gear/star-state calibration — no tiers changed, decisions pending; top remaining gap is Katrina-090 with zero hits. Conflicting jewel values and incomplete monster/base-stat evidence remain visible.
