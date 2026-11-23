# BLUSTONE Evidence and Coverage — 2026-11-23.2

As of **2026-11-23 (Asia/Jerusalem)**; source observation dates remain separate.

## Evidence classes

- RECOVERED: original extracted record with exact file/key/chunk locator.
- COMMUNITY-SOURCED: source-backed page/archive/screenshot claim.
- INFERRED: explicit derivation or hypothesis.
- INFERRED-FIXTURE: replica policy; not original-game evidence.
- UNKNOWN: missing or unresolved.

## Dataset coverage

| Dataset | Records | Pinned source |
|---|---|---|
| balance_followup | 22 | datasets/gameplay/balance-observations.json |
| snowfields_gameplay | 3 | datasets/campaign/snowfields-gameplay.json |
| hunter_level_one_panels | 3 | datasets/hunters/level-one-panels.json |
| historical_market_quotes | 58 | datasets/economy/market-quotes.json |
| hunter_identities | 121 | datasets/hunters/identities.json |
| hunter_stat_observations | 819 | datasets/hunters/stat-observations.json |
| hunter_skill_reference | 1070 | datasets/hunters/skill-reference.json |
| monster_identities | 22 | datasets/monsters/identities.json |
| campaign_identifiers | 50 | datasets/campaign/stage-identifiers.json |
| episode_story_graph | 147 | datasets/episodes/story-graph.json |
| episode_rewards | 18 | datasets/economy/episode-rewards.json |
| hunter_gear_identities | 121 | datasets/equipment/hunter-gear-identities.json |
| hero_at_draw_estimates | 113 | findings/hunters/base-stats-visual-hunt/hero-at-draw-estimates-2026-11-23.tsv |
| accessory_stat_estimates | 100 | findings/hunters/base-stats-visual-hunt/accessory-stat-estimates-2026-10-11/accessory-stat-estimates-2026-10-11.tsv |
| monster_stat_estimates | 22 | findings/hunters/base-stats-visual-hunt/monster-stat-estimates-2026-10-11/monster-stat-estimates-2026-10-11.tsv |
| skill_magnitude_estimates | 565 | findings/hunters/base-stats-visual-hunt/skill-magnitude-estimates-2026-10-11/skill-magnitude-estimates-2026-10-11.tsv |

## Reading the stats document

Archive claims retain original URL, capture timestamp, raw text, units, identity match and unknown state fields in BLUSTONE-Stats.json. Screenshot tables carry a pinned document hash and source-line locator. Do not merge measurements at different levels, ranks or equipment states. White/green display separation is evidence for one observed build, not proof of final-version balance.

## November observations and open research


The strongest evidence for starting HP is the same fresh party entering three Midgard Snowfields battles in September 2019 footage. Before contact, the protagonist shows 173, 175 and 177 HP, while Tyltyl shows 156, 157 and 158. These are full effective battle HP readings and can include party effects. Each clear gains one Hunter level. Each entry costs six Fuel. The settled Rupee totals are 56, 54 and 54 after the victory counter finishes. Team-level bonuses appear separately. Each area has one observed clear. [First formation](https://www.youtube.com/watch?v=4VMg-VMJudU&t=680s) · [First settlement](https://www.youtube.com/watch?v=4VMg-VMJudU&t=764s) · [Second and third battles](https://www.youtube.com/watch?v=gMKUEl3xf-k&t=13s)

A Japanese video uploaded December 12, 2018 shows a newly recruited three-star, level-one Akasha with 543 HP, 362 ATK, 372 DEF, attack speed 7 and 1,834 Strength. The upload falls after the Japanese sequel announcement. Its recording date, client build and equipped bonuses remain unknown. Level-one Tyltyl and Riko recordings from January and June 2018 belong to the preceding era. [Akasha card](https://www.youtube.com/watch?v=GxThPFqGBQk&t=63s) · [Strength](https://www.youtube.com/watch?v=GxThPFqGBQk&t=66s) · [Tyltyl](https://www.youtube.com/watch?v=U4WLbs4GoHk&t=441s) · [Riko](https://www.youtube.com/watch?v=vXuGNGCMg3Q&t=1053s)

The 2019 Japanese archive lists Tyltyl at 1,467 HP. Its level and equipment fields are unknown. The earlier at-draw estimates inferred a common starting state across 62 profiles. The videos give a direct reason to reopen that inference. We retain the archive values for comparison. The November estimates mark their at-draw interpretation as uncalibrated. Higher-tier extrapolations that depend on those rows inherit this uncertainty, including the historical confidence bands. The Hermes comparison uses a five-star, level-30 panel and a modeled growth rate. [Archive](https://github.com/The-Blustone-Revival-Project/Blustone-DataDump/blob/2026-11-23.2/findings/hunters/base-stats-visual-hunt/archived-hunter-database-2019.tsv) · [October interpretation](https://github.com/The-Blustone-Revival-Project/Blustone-DataDump/blob/2026-11-23.2/findings/hunters/base-stats-visual-hunt/panel-adjudication-2026-10-17.md)

The Market ledger records one row per legible priced offer. Dates come from the filenames. Each row identifies the shop, currency, total lot price, quantity when visible, image hash and public transcription line. The linked Korean and Japanese announcements date the transition to late 2018. Exact builds, regions and account servers for the market images are unknown. A countdown measures time remaining in the captured rotation. Purchased cards with hidden prices supply no quote. The June 2019 yen package and My Trace confirmation are separate purchase screens. The Trainer price is legible, while its lot count is unspecified. [Korean launch announcement](https://m.inven.co.kr/webzine/wznews.php?idx=210886&site=mobilegame) · [Japanese launch announcement](https://www.4gamer.net/games/442/G044285/20181203042/) · [Market ledger](https://github.com/The-Blustone-Revival-Project/Blustone-DataDump/blob/2026-11-23.2/findings/economy/market-quotes-2026-11-23.tsv)

## Follow-up measurements

The same recording follows the starting Captain from one star at level 27 (Strength 556) through training to level 30 (586) and advancement to two stars at level 1 (799). A different Hunter, Hermes, has a dated three-star level-one panel with 637 HP, 507 ATK and 358 DEF. At five stars and level 30 his displayed totals are 3,187, 1,977 and 1,227. The later jewel panel explains part of the difference. The equipment screen has a one-point ATK subtotal discrepancy. These observations constrain a progression curve while leaving individual core-stat growth open. [Captain training](https://www.youtube.com/watch?v=gMKUEl3xf-k&t=718s) · [Captain advancement](https://www.youtube.com/watch?v=gMKUEl3xf-k&t=790s) · [Hermes panels](https://github.com/The-Blustone-Revival-Project/Blustone-DataDump/blob/2026-11-23.2/findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/batch-61.tsv#L32)

Full pre-contact HP is also visible farther along in the same run. The Captain and Tyltyl show 179/159 at level 4, 222/180 at level 25, and 224/181 at level 26. Scar shows 298 at level 1 and 331 at level 17. Extending the opening Captain slope of +2 from 173 HP at level 1 predicts 221 and 223. The observed party HP is one point higher at both later levels. Tyltyl matches the +1 projection at each sampled level. The footage leaves rounding and party bonuses unresolved. [Area 4](https://www.youtube.com/watch?v=gMKUEl3xf-k&t=265s) · [Area 5](https://www.youtube.com/watch?v=gMKUEl3xf-k&t=460s) · [Area 6](https://www.youtube.com/watch?v=gMKUEl3xf-k&t=535s)

In Midgard Snowfields Area 4 the first manual clear paid 54 Rupees. The same player then collected 1,098 Rupees across 20 tutorial dispatches to that cleared stage. The per-run mean is 54.9. Each individual payout and the ordinary manual replay distribution remain unknown. The tutorial waived both dispatch and skip costs. At Wolf’s Mouth Area 57, a 2021 dispatch quote shows 120 Fuel and 48 minutes for 20 runs. This gives a later cost benchmark; the screenshot ends before settlement. [Area 4 first clear](https://www.youtube.com/watch?v=gMKUEl3xf-k&t=309s) · [Repeat setup](https://www.youtube.com/watch?v=gMKUEl3xf-k&t=408s) · [Batch result](https://www.youtube.com/watch?v=gMKUEl3xf-k&t=434s) · [Area 57 quote](https://github.com/The-Blustone-Revival-Project/Blustone-DataDump/blob/2026-11-23.2/findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/batch-68.tsv#L22)

Across the first seven Snowfields victories, the settled amounts are **56, 54, 54, 54, 56, 52 and 52 Rupees**, totaling **378** in this playthrough. Area 5 pays on the successful retry after the guided loss to Lapis. After Area 7, reaching team level 4 separately awards 60 Fuel and increases the Fuel cap by one. [Area 5 victory](https://www.youtube.com/watch?v=gMKUEl3xf-k&t=519s) · [Area 6 victory](https://www.youtube.com/watch?v=gMKUEl3xf-k&t=599s) · [Team-level popup](https://www.youtube.com/watch?v=gMKUEl3xf-k&t=675s)

On May 3, 2019, the Fight Chips Shop displayed Beckhen, Natalia and Juno at five traces for 375 chips each. The timer showed 03:19:16. The 1.4.4.1 and 2.8.0.1 client help entries agree that Rupee and Fight Chips stock rotates and Manda can refresh it. An undated Beckhen screenshot shows his purchased card. The interval, reset fee, sequel-era Mowgli and Riko lots and ordinary Manda-tab item prices remain open. [May shop](https://github.com/The-Blustone-Revival-Project/Blustone-DataDump/blob/2026-11-23.2/findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/batch-61.tsv#L21) · [Purchased card](https://github.com/The-Blustone-Revival-Project/Blustone-DataDump/blob/2026-11-23.2/findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/batch-14.tsv#L48) · [Original help excerpts](https://github.com/The-Blustone-Revival-Project/Blustone-DataDump/blob/2026-11-23.2/findings/gameplay/original-help-excerpts-2026-11-23.json)

Two 2021 Episode recordings show why combat timing needs two clocks. In Episode 13 Story 02 the Captain falls to Vincent after about 33 seconds of footage and 12.4 seconds of the combat timer. In Episode 15 Story 05 the five-opponent fight spans about 72 seconds of footage and 27 combat seconds. Both timers hold during skill animations. These are scripted encounters with recorded damage and recovery visible on screen. The observations do not establish ordinary Expedition enemy coefficients or separate skill healing from passive recovery. [Episode 13 duel](https://www.bilibili.com/video/BV1Dq4y1D7tZ/?t=62) · [Episode 15 fight](https://www.bilibili.com/video/BV1SL411E77Q/?t=52)

## Remaining measurements

The next sources to seek are matched Blustone 2 starter ATK and DEF panels across a level gain, a manual first-clear and replay pair with settled XP and Rupees, a continuous ordinary Market purchase through refresh, and a late Expedition run with known builds and visible damage and healing. The full observations include timestamps, screenshot fingerprints and uncertain fields. [Observation ledger](https://github.com/The-Blustone-Revival-Project/Blustone-DataDump/blob/2026-11-23.2/findings/gameplay/balance-observations-2026-11-23.json)

The revival trial uses archive ratios, capped promotion growth and fixed first-clear rewards as design choices. Those formulas belong to the Server. [Server trial and verification](https://github.com/The-Blustone-Revival-Project/Blustone-Server/blob/bf555fe/docs/revival-balance-2026-11-23.md)

## Conflicts and known limits

- The 62 archive tuples are historical display readings. Their at-draw level and equipment remain unverified. The November classification supersedes the October interpretation.
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
| datasets/gameplay/balance-observations.json | 3245f7d7ecf5a9aa6eb341a7a1620a029e2591446e936138611162007b75309b |
| datasets/campaign/snowfields-gameplay.json | 2d524c42e5bf82a430169f97c10a6c0a8f8cb6bfb4553a26f0504eca84063636 |
| datasets/hunters/level-one-panels.json | 56e51285ba5de98627c2e0b976b1f25cb924302308ebfff6d8dd03eb9f6f5d4c |
| datasets/economy/market-quotes.json | ac6477e9c68721195b3027aee53213fa3a67cdb9eb428c9734cf6b56ecfa4cd2 |
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
| findings/balance-research-2026-11-23.md | 1f6b408ef52d5bc9bcfe1d3f30d4d74e5da599c40aaa7259db89c34f85311d00 |
| findings/campaign/snowfields-gameplay-2026-11-23.tsv | 6699757b1af3140ddb769ec6b83e3af924ae129caa986d0d2cd6a47603370e42 |
| findings/economy/market-quotes-2026-11-23.tsv | 4174ea1be209cefba455e2b1caea3d53ab79e433253e0cdbd670ceb39bf47dd3 |
| findings/gameplay/balance-observations-2026-11-23.json | dab00e73cd72fdf54cc36ecfaf4677baf27f35ece7536d90f1317a3c4961e4e5 |
| findings/gameplay/original-help-excerpts-2026-11-23.json | 2f41f8f16d3c84f526f69195a9a94767f07cebcae63e3b3699fdaef6964fb1a5 |
| findings/hunters/base-stats-visual-hunt/jewel-help-locales-2026-10-05.md | 74ca4f5a245a67fd298b0dfca7e46b4dd5583b8908b20830b5d92fe2782def3f |
| findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/batch-08.tsv | 60911bd28119290ad5070b45421a98a56ab36d3733559b5fe98d1cbe7db4b0cc |
| findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/batch-10.tsv | b0f6c3c11a60df18901b3751bfa3d01127cae7c1d484e4e4469c115b7d5c30e1 |
| findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/batch-13.tsv | 6200aec8418e90c23645014fba5c67b6d349516ab4d11eb824fed02de8ca2e8a |
| findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/batch-14.tsv | 601b9e3cc08e36ab61cf39d9428232034d4c5b01f478866802e8690ad7bd7559 |
| findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/batch-43.tsv | ba4c70022cc7c5d6dc77f4b37069b4d1c7d632f13a8a279b214ab67d7a13be50 |
| findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/batch-46.tsv | ef0adb864a6b2f896db3c6fed30c55ea3fb9d9d52a9ce3fa58b0fa253272633e |
| findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/batch-50.tsv | c1eabd52424c4d8e5bdca006b5ba80246e1e7d6774e06fcc1074d1d1d9fbc55a |
| findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/batch-54.tsv | 8feb8dcdf48d62877b3bd7dd02add0c401364bdb56ddb71b4b758859dd5ae840 |
| findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/batch-57.tsv | 9dd8d6ebd709fb0cb9d3281ab20a00511f5116b5fd247805f0b769cc82238fa4 |
| findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/batch-58.tsv | 88a72051906dd3dafecbc349aca152bdeac4b50ee1f225de1b11e69bfadb1ec3 |
| findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/batch-60.tsv | 07c1caf96edf56f83b1c39d941abbb05699ba126a282b96059aa884e29694181 |
| findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/batch-61.tsv | 7043efb7d63f094e0ed089bf7e30165fd335956a699c8a677cb7513ce1cc8914 |
| findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/batch-63.tsv | 7b57a14e9b0a72ebfb96323dcf17c01954ee9ea2be3ace71371cbf4d57b72d32 |
| findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/batch-64.tsv | c9e08971df4536fe87f974b6db72aaa0e9a25ac0f270a84c9b37edb2e4d90ea5 |
| findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/batch-68.tsv | b2e7006ce6b8fb706b6b2997c8a5932926c91dfe460a04ae46c67bc9c55aca69 |
| findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/scrape-consolidation-2026-10-14.md | fa025031c2631bcf11d6c1105c8b1a298494dceade5c43466dca598bc2e3d936 |
| findings/hunters/base-stats-visual-hunt/panel-adjudication-2026-10-17.md | 9c7cfd7271c93171a8fe43e3981eb16902048f099f405310526e61572fd3fc3d |
| findings/hunters/level-one-panels-2026-11-23.tsv | 8c1e0d7fa4186534238e264c36487e48038f77ac0bf543b451e16fb736047218 |
| findings/resources/vsfan-extracted-assets.md | 9b88dd41ef5633b29931cf5f1ae726a9270989a7b5485b124a06d9040d6550b8 |
| findings/hunters/base-stats-visual-hunt/hero-at-draw-estimates-2026-11-23.tsv | 77bcf2c5b3709090275003230149dc5685b58161e724a59c20913f136b8a64cc |
| findings/hunters/base-stats-visual-hunt/accessory-stat-estimates-2026-10-11/accessory-stat-estimates-2026-10-11.tsv | 3fe09a576aaec43ce9285a262f81b02a2eacb4445a2de99a15d979dde010b223 |
| findings/hunters/base-stats-visual-hunt/monster-stat-estimates-2026-10-11/monster-stat-estimates-2026-10-11.tsv | 325b1d62ae33d98f728b31b5524843d7552280e007f87f0e5b6d47db9add8f7f |
| findings/hunters/base-stats-visual-hunt/skill-magnitude-estimates-2026-10-11/skill-magnitude-estimates-2026-10-11.tsv | 431239bb588e0590380b8fe558f3e8bbba5a046fae0d7b00b97fe88c400b2b28 |

## Reproduce this release

Check out tag `2026-11-23.2`, run `python tools/normalize/validate-datasets.py`, then `python tools/releases/build-snapshot.py --date 2026-11-23 --revision 2 --out local/reproduced/2026-11-23.2`. Use the previous release's BLUSTONE-Stats.json with `--previous-json` when applicable.

## Integrity

SHA256SUMS.txt pins the two documents, the JSON snapshot and the release manifest. The release manifest pins every dataset source used to construct this snapshot. Private captures, cookies, saves, signing keys and raw account telemetry are excluded.
