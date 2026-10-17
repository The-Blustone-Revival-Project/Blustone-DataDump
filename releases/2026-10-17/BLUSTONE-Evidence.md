# BLUSTONE Evidence and Coverage — 2026-10-17

As of **2026-10-17 (Asia/Jerusalem)**; source observation dates remain separate.

## Evidence classes

- RECOVERED: original extracted record with exact file/key/chunk locator.
- COMMUNITY-SOURCED: source-backed page/archive/screenshot claim.
- INFERRED: explicit derivation or hypothesis.
- INFERRED-FIXTURE: replica policy; not original-game evidence.
- UNKNOWN: missing or unresolved.

## Dataset coverage

| Dataset | Records | Pinned source |
|---|---|---|
| hunter_identities | 121 | datasets/hunters/identities.json |
| hunter_stat_observations | 819 | datasets/hunters/stat-observations.json |
| hunter_skill_reference | 1070 | datasets/hunters/skill-reference.json |
| monster_identities | 22 | datasets/monsters/identities.json |
| campaign_identifiers | 50 | datasets/campaign/stage-identifiers.json |
| episode_story_graph | 147 | datasets/episodes/story-graph.json |
| episode_rewards | 18 | datasets/economy/episode-rewards.json |
| hunter_gear_identities | 121 | datasets/equipment/hunter-gear-identities.json |
| hero_at_draw_estimates | 113 | findings/hunters/base-stats-visual-hunt/hero-at-draw-estimates-2026-10-17.tsv |
| accessory_stat_estimates | 100 | findings/hunters/base-stats-visual-hunt/accessory-stat-estimates-2026-10-11/accessory-stat-estimates-2026-10-11.tsv |
| monster_stat_estimates | 22 | findings/hunters/base-stats-visual-hunt/monster-stat-estimates-2026-10-11/monster-stat-estimates-2026-10-11.tsv |
| skill_magnitude_estimates | 565 | findings/hunters/base-stats-visual-hunt/skill-magnitude-estimates-2026-10-11/skill-magnitude-estimates-2026-10-11.tsv |

## Reading the stats document

Archive claims retain original URL, capture timestamp, raw text, units, identity match and unknown state fields in BLUSTONE-Stats.json. Screenshot tables carry a pinned document hash and source-line locator. Do not merge measurements at different levels, ranks or equipment states. White/green display separation is evidence for one observed build, not proof of final-version balance.

## Conflicts and known limits

- The 62 archive rows are reclassified as at-draw basic rows under the 2026-10-11 derivation policy (page labels basic-at-draw, gear proven nude); the level numeral itself is derived, not printed.
- Beckhen 051 Lv.30 equipment ATK has a 78-point unreconciled subtotal.
- Vincent 010_1 equipment state is unknown.
- The 1.4.4.1 Super Block locale conflict and the distinct 2.8.0.1 Reduction wording/reordered help table are preserved; do not collapse eras or locales.
- Monster episode rows are per-encounter tuples; monster display names stay unknown.
- Tier-B/C hero point estimates are band centres; exact-tuple confidence is 2–25%.
- Original reward IDs are separate from server settlement mappings.
- No native battle, phone operation or new stat measurement is implied by publishing this snapshot.

## Derivation sources and methods

Per-row class (`[RECOVERED]` / `[DERIVED-ESTIMATE]`), confidence and method live in BLUSTONE-Stats.json under `derivations`. `[INFERRED-FIXTURE]` rows are excluded from the snapshot payload. Methods: hero archive-level derivation (`findings/hunters/base-stats-visual-hunt/archive-level-derivation-2026-10-11.md`), hero archetype model (`findings/hunters/base-stats-visual-hunt/hero-archetype-guesstimate-2026-10-11.md`), accessory model (`findings/hunters/base-stats-visual-hunt/accessory-stat-estimates-2026-10-11/REPORT.md`), monster model (`findings/hunters/base-stats-visual-hunt/monster-stat-estimates-2026-10-11/REPORT.md`), skill model (`findings/hunters/base-stats-visual-hunt/skill-magnitude-estimates-2026-10-11/REPORT.md`). The four estimate TSVs are fingerprinted in the sources table above.

## Source fingerprints

| Source path | SHA-256 |
|---|---|
| datasets/hunters/identities.json | b3fd3db855913d41b45c2e2309c9562eb064564238f541909d1f296309a2bbe2 |
| datasets/hunters/stat-observations.json | 0caf6f79877b186861c970fbf446779eaa33199cb1c379279ed1d594b8a02f9e |
| datasets/hunters/skill-reference.json | 996c324949fbc57862481527b84a67493b6dd2f0d61aac9b0f1736c3b6960d1e |
| datasets/monsters/identities.json | 535cd90c44b523ca556320d3c5b0f3fc076e81be3b877741e76a3beec80cf688 |
| datasets/campaign/stage-identifiers.json | db576e6022305c4d2e4cbb927a0758e5f4eb919f1bf572a90b193ba52a53a4ee |
| datasets/episodes/story-graph.json | 0c35669d00514ee1d2ff0b8182859d5fc577b7335be7ad6c8d5833cb7957069d |
| datasets/economy/episode-rewards.json | 1b4359aa7f4ed31c8d707493540efb702aade0cc4c628ccee3c8aa98ceef345a |
| datasets/equipment/hunter-gear-identities.json | 198f049ae6a6bd7cc6325d334447c447624b3f1b1172b63a2e2ec9c5a96c8ca7 |
| datasets/equipment/GEAR.md | 8467819aa46a185ec5c10ff79af2b216902545270d1aabff579cc77294e293e9 |
| datasets/hunters/observed-stats/010.md | e928d2866778a3c17ec5a33b9f2418556ae155d7af2b49bfb3315f9843f713c3 |
| datasets/hunters/observed-stats/010_1.md | 6962b2c7b53b7bcadcc1b837343dd89e871fc4d41f93a3f1d3cfd2a746bca44e |
| datasets/hunters/observed-stats/051.md | 08891ac93cd14720519c4fbe8494db53008c1bdab18c3fd65ff4c6c6c81c4858 |
| findings/hunters/base-stats-visual-hunt/jewel-help-locales-2026-10-05.md | 74ca4f5a245a67fd298b0dfca7e46b4dd5583b8908b20830b5d92fe2782def3f |
| findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/scrape-consolidation-2026-10-14.md | 3b0b5fec4927ca69b348bbf469567c5428cf2080ad31b21bb2023985f5aeecd3 |
| findings/hunters/base-stats-visual-hunt/panel-adjudication-2026-10-17.md | 9c7cfd7271c93171a8fe43e3981eb16902048f099f405310526e61572fd3fc3d |
| findings/resources/vsfan-extracted-assets.md | 9b88dd41ef5633b29931cf5f1ae726a9270989a7b5485b124a06d9040d6550b8 |
| findings/hunters/base-stats-visual-hunt/hero-at-draw-estimates-2026-10-17.tsv | f5d9541e7ab6c1eae9ed8ad3281770333a3d9f31f9199ac323cc080449a3352b |
| findings/hunters/base-stats-visual-hunt/accessory-stat-estimates-2026-10-11/accessory-stat-estimates-2026-10-11.tsv | 3fe09a576aaec43ce9285a262f81b02a2eacb4445a2de99a15d979dde010b223 |
| findings/hunters/base-stats-visual-hunt/monster-stat-estimates-2026-10-11/monster-stat-estimates-2026-10-11.tsv | 325b1d62ae33d98f728b31b5524843d7552280e007f87f0e5b6d47db9add8f7f |
| findings/hunters/base-stats-visual-hunt/skill-magnitude-estimates-2026-10-11/skill-magnitude-estimates-2026-10-11.tsv | 431239bb588e0590380b8fe558f3e8bbba5a046fae0d7b00b97fe88c400b2b28 |

## Reproduce this release

Check out tag `2026-10-17`, run `python tools/normalize/validate-datasets.py`, then `python tools/releases/build-snapshot.py --date 2026-10-17 --revision 1 --out local/reproduced/2026-10-17`. Use the previous release's BLUSTONE-Stats.json with `--previous-json` when applicable.

## Integrity

SHA256SUMS.txt pins the two documents, the JSON snapshot and the release manifest. The release manifest pins every dataset source used to construct this snapshot. Private captures, cookies, saves, signing keys and raw account telemetry are excluded.
