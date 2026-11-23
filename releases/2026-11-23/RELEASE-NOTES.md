# Blustone DataDump 2026-11-23

Stats and evidence snapshot as of 2026-11-23 (Asia/Jerusalem).

## Included

- **BLUSTONE-Stats.md:** historical hunter values, curated screenshot/equipment tables, original IDs and explicit unknowns.
- **BLUSTONE-Evidence.md:** source classes, coverage, conflicts, source hashes and reproduction instructions.
- **BLUSTONE-Stats.json:** all 11 normalized datasets, derived estimate tables (113 hero at-draw rows, 100 accessory rows, 22 monster rows, 565 skill rows), curated source tables and machine-readable changes from the previous release.
- **RELEASE-MANIFEST.json** and **SHA256SUMS.txt:** reproducibility and integrity.

## Changes

- Three original Snowfields clears establish early effective HP and settled Rupee amounts. Three level-one Hunter panels carry upload-era context.
- The market ledger records 55 priced offers across ten dated screens, including eight ordinary Market rotations and two separate purchase screens.
- Reclassified 62 Japanese archive tuples as uncalibrated at-draw estimates. Their recorded numeric values are preserved.

Compared with 2026-10-17.

| Dataset | Added | Changed | Removed |
|---|---|---|---|
| snowfields_gameplay | 3 | 0 | 0 |
| hunter_level_one_panels | 3 | 0 | 0 |
| historical_market_quotes | 55 | 0 | 0 |
| hunter_identities | 0 | 0 | 0 |
| hunter_stat_observations | 0 | 0 | 0 |
| hunter_skill_reference | 0 | 0 | 0 |
| monster_identities | 0 | 0 | 0 |
| campaign_identifiers | 0 | 0 | 0 |
| episode_story_graph | 0 | 0 | 0 |
| episode_rewards | 0 | 0 | 0 |
| hunter_gear_identities | 0 | 0 | 0 |
| hero_at_draw_estimates | 0 | 62 | 0 |
| accessory_stat_estimates | 0 | 0 | 0 |
| monster_stat_estimates | 0 | 0 | 0 |
| skill_magnitude_estimates | 0 | 0 | 0 |
| curated_source_tables | 0 | 2 | 0 |


## Coverage and limits

121 catalogue rows /113 playable identities;22 monster identities;806 numeric historical claims;50 campaign IDs;147 Episode nodes;1070 symbolic skill records. Derived estimates carry per-row class and historical confidence; fixture rows are excluded from the payload. Conflicting jewel values and incomplete monster/base-stat evidence remain visible.
