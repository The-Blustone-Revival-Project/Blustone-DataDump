# BLUSTONE Evidence and Coverage — 2026-10-11

As of **2026-10-11 (Asia/Jerusalem)**; source observation dates remain separate.

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

## Reading the stats document

Archive claims retain original URL, capture timestamp, raw text, units, identity match and unknown state fields in BLUSTONE-Stats.json. Screenshot tables carry a pinned document hash and source-line locator. Do not merge measurements at different levels, ranks or equipment states. White/green display separation is evidence for one observed build, not proof of final-version balance.

## Conflicts and known limits

- 2019 archive levels/equipment are unestablished; zero archive claims count as complete base-stat evidence.
- Beckhen 051 Lv.30 equipment ATK has a 78-point unreconciled subtotal.
- Vincent 010_1 equipment state is unknown.
- The 1.4.4.1 Super Block locale conflict and the distinct 2.8.0.1 Reduction wording/reordered help table are preserved; do not collapse eras or locales.
- Monster video/HUD readings without an identified full/max HP cannot establish a base tuple.
- Original reward IDs are separate from server settlement mappings.
- No native battle, phone operation or new stat measurement is implied by publishing this snapshot.

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
| findings/resources/vsfan-extracted-assets.md | 9b88dd41ef5633b29931cf5f1ae726a9270989a7b5485b124a06d9040d6550b8 |

## Reproduce this release

Check out tag `2026-10-11`, run `python tools/normalize/validate-datasets.py`, then `python tools/releases/build-snapshot.py --date 2026-10-11 --revision 1 --out local/reproduced/2026-10-11`. Use the previous release's BLUSTONE-Stats.json with `--previous-json` when applicable.

## Integrity

SHA256SUMS.txt pins the two documents, the JSON snapshot and the release manifest. The release manifest pins every dataset source used to construct this snapshot. Private captures, cookies, saves, signing keys and raw account telemetry are excluded.

## Derivation evidence added 2026-10-11 (findings, not normalized records)

Under the ledger's 2026-10-11 derivation-counts policy, a derived row counts when it rests on a source-backed anchor for the same quantity, carries an explicit class (`[DERIVED]` exact / `[DERIVED-ESTIMATE]` fitted, both distinct from `[INFERRED-FIXTURE]`), records numeric per-row confidence, and is free of unsubtracted contamination. Per-tier confidences (band vs exact-tuple) are stated in BLUSTONE-Stats.md; the honesty correction (tier-B medians are band centres, not likely-exact values) applies everywhere. Stat-panel HITs 1–3 claim 0% coverage (gear state unproven). The VSFan attach-census lane running at cutoff is not part of this snapshot.

Supplementary fingerprints (finding files as of this snapshot; the stat-panel `hits/` frames are binary image evidence preserved in-lane and not hashed here):

| Finding file | SHA-256 |
|---|---|
| findings/hunters/base-stats-visual-hunt/hero-at-draw-estimates-2026-10-11.tsv | 55c7ca84f7166d25c361a1282f0eafa95a74c3c9b94a34bf8006d9c8ccb57a6c |
| findings/hunters/base-stats-visual-hunt/hero-archetype-guesstimate-2026-10-11.md | baea34627160f891da5defd13b1093db3788c198f19a68f5b25d5996f986a165 |
| findings/hunters/base-stats-visual-hunt/hero-archetype-guesstimate-2026-10-11.tsv | 75bc657994a6f750ac086445ebc8cf37114d1f8c9deebdb087492424cdb4b4f6 |
| findings/hunters/base-stats-visual-hunt/archive-level-derivation-2026-10-11.md | fab1117af236ab56c3071aaf2c176365090f5373baebabdbf798fe1165e9274f |
| findings/hunters/base-stats-visual-hunt/accessory-stat-estimates-2026-10-11/REPORT.md | 2e2a5c58bdee3821e884eb008d84b673d6058e83a3c1aa8fa67b6dbb55e69a4e |
| findings/hunters/base-stats-visual-hunt/accessory-stat-estimates-2026-10-11/accessory-stat-estimates-2026-10-11.tsv | 3fe09a576aaec43ce9285a262f81b02a2eacb4445a2de99a15d979dde010b223 |
| findings/hunters/base-stats-visual-hunt/accessory-stat-estimates-2026-10-11/per-level-curve.tsv | cdde96dc90f1f1b12790aef00e6e7cebaa488bed7dcc267b8cce4f20542de8d1 |
| findings/hunters/base-stats-visual-hunt/skill-magnitude-estimates-2026-10-11/REPORT.md | c7a2e8cf7fce1ddda1af62750376605dc996592a2fe663576954469394f25242 |
| findings/hunters/base-stats-visual-hunt/skill-magnitude-estimates-2026-10-11/skill-magnitude-estimates-2026-10-11.tsv | 431239bb588e0590380b8fe558f3e8bbba5a046fae0d7b00b97fe88c400b2b28 |
| findings/hunters/base-stats-visual-hunt/monster-stat-estimates-2026-10-11/REPORT.md | 668c8cf0f270a8054ad74a4cb6967177f341c92cf6ce9808fdbea257e4465ff4 |
| findings/hunters/base-stats-visual-hunt/monster-stat-estimates-2026-10-11/monster-stat-estimates-2026-10-11.tsv | 325b1d62ae33d98f728b31b5524843d7552280e007f87f0e5b6d47db9add8f7f |
| findings/hunters/base-stats-visual-hunt/stat-panel-hunt-2026-10-11/REPORT.md | 8bb334c1c06b7de41ff2bd2208f2458145c9eb34ecda701db79f3ef5f2bc6b17 |
| findings/hunters/base-stats-visual-hunt/coverage.md | c9bb4aabe139af30de53f47dfcd2151d7a14c7160df7255b3abd811e8e4f05d2 |
