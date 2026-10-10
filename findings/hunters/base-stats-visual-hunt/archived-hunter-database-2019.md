# Archived Japanese Hunter Database — numeric profile tables

This is a structured per-hunter database preserved by the Wayback Machine, not
guide prose. Its pages label stat sections **基本能力値** (“basic ability
values”), give the hunter's rarity **when drawn**, and list combat power,
HP/ATK/DEF, attack speed, and additional combat stats. Individual hero pages
also name the hero's associated weapon, armor, and accessory.

Across the 62 numeric profiles reviewed, the database does **not** print a
level, and
does not state whether the listed equipment is currently equipped or merely the
hero's associated gear. The values are therefore transcribed as page readings;
their status as exact level-1/nude base rows is a strong hypothesis, not a
verified fact. They remain outside strict coverage until level and gear context
are resolved. The source's `basic ability` label plus the Beckhen cross-check
below supports using them as baseline estimates.

## Profile readings

| Catalog ID | Hero | Captured | Role / element | Rarity when drawn | Combat power | HP | ATK | DEF | Speed | Crit | Crit dmg | Pen | Block | Block dmg red. | Elem. enhance | Elem. resist | HP regen. | Level / gear context | Strict count? |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| `051` | Beckhen | 2019-12-16 | Offense / Ice | 3★ | 8,709 | 1,678 | 864 | 660 | 8 | 33 | 200 | 0 | 14 | 42 | 5 | 5 | 42 | Level not printed; equipment section names Chicken Feet / Chicken Wings / Jack, but does not report equipped state or item levels. | No new credit; corroborates existing FAQ row |
| `023` | Hermes | 2019-12-10 | Offense / Fire | 3★ | 9,177 | 1,750 | 937 | 653 | 8 | 33 | 200 | 0 | 14 | 40 | 2 | 2 | 44 | Level not printed; equipment section names Fire Dual Swords / Messenger Jacket / Messenger Bag, but does not report equipped state or item levels. | No |
| `017` | Lapis | 2019-12-09 | Offense / Ice | 1★ | 7,495 | 1,537 | 854 | 540 | 8 | 33 | 205 | 0 | 14 | 40 | 0 | 0 | 38 | Level not printed; equipment section names Frost Sword / Military Tank Top / Memory Cord, but does not report equipped state or item levels. | No |
| `044` | Heidi | 2019-12-11 | Offense / Fire | 3★ | 9,764 | 1,750 | 952 | 689 | 8 | 33 | 200 | 0 | 20 | 40 | 5 | 5 | 44 | Level not printed; equipment section names Big Rabbit Pillow / Microfibrous Pyjamas / Pompom Headband, but does not report equipped state or item levels. | No |

## Provenance and interpretation

- [Beckhen profile capture](https://web.archive.org/web/20191216060610/https://blustone.jp/hunter/%E3%83%AC%E3%82%A2%E3%83%AA%E3%83%86%E3%82%A3%E5%88%A5/%E3%83%95%E3%82%A1%E3%82%A4%E3%83%88%E3%82%AF%E3%83%A9%E3%83%96%E3%81%AE%E5%AE%88%E8%AD%B7%E8%80%85%E3%80%8C%E3%83%99%E3%83%83%E3%82%B1%E3%83%B3%E3%80%8D)
- [Hermes profile capture](https://web.archive.org/web/20191210182657/https://blustone.jp/hunter/%E3%83%AC%E3%82%A2%E3%83%AA%E3%83%86%E3%82%A3%E5%88%A5/%E7%89%B9%E7%B4%9A%E4%BC%9D%E4%BB%A4%E4%BD%BF%E3%80%8C%E3%83%98%E3%83%AB%E3%83%A1%E3%82%B9%E3%80%8D)
- [Lapis profile capture](https://web.archive.org/web/20191209002932/https://blustone.jp/hunter/%E3%83%AC%E3%82%A2%E3%83%AA%E3%83%86%E3%82%A3%E5%88%A5/%E5%BF%AB%E9%80%9F%E3%81%AE%E5%89%A3%E8%A1%93%E5%A3%AB%E3%80%8C%E3%83%A9%E3%83%94%E3%82%B9%E3%80%8D)
- [Heidi profile capture](https://web.archive.org/web/20191211112706/https://blustone.jp/hunter/%E3%83%AC%E3%82%A2%E3%83%AA%E3%83%86%E3%82%A3%E5%88%A5/2%E3%81%A4%E3%81%AE%E9%A1%94%E3%82%92%E6%8C%81%E3%81%A4%E5%B0%91%E5%A5%B3%E3%80%8C%E3%83%8F%E3%82%A4%E3%83%87%E3%82%A3%E3%80%8D)

Identity was mapped from the Japanese profile titles/hero names to the local
catalog and `CHAR_STR` names. In particular, the Beckhen profile's white/basic
HP/ATK/DEF values are below the independently verified Lv.30 nude FAQ values
(2,879 / 1,471 / 1,149); their ratios are approximately 1.715 / 1.703 / 1.741.
That near-common factor is consistent with a lower-level base line, likely the
initial recruit level, but the profile does not print `Lv.1`. Preserve the
level as unknown until another source or native formula confirms it.

The archived rarity list identified the hunters' displayed role, element, and
rarity-on-draw; the profile pages expose the numeric tables. More profiles can
be appended to the table with the exact same field schema. The source is
version-sensitive (2019 captures) and predates later balance changes.

## Batch harvest from the 2019-10-15 archive index

The archived [rarity-index page](https://web.archive.org/web/20191015065805/https://blustone.jp/hunter/%E3%83%AC%E3%82%A2%E3%83%AA%E3%83%86%E3%82%A3%E5%88%A5) yielded 63 distinct named profile links. The exact October index-linked captures provided 30 complete numeric pages, one `???` placeholder, and 32 links with no page at that timestamp. A later 2019 wildcard lookup resolved all 32 remaining links to alternate November/December captures. Together, **62 profiles returned numeric values for all 13 fields** (combat power plus twelve ability fields), and the results are preserved in [`archived-hunter-database-2019.tsv`](archived-hunter-database-2019.tsv). Each row retains the exact capture URL and timestamp.

The 62 numeric pages crosswalk to 62 distinct catalog IDs by matching Japanese profile epithets against `CHAR_STR.json` titles, then checking draw rarity, role, and element. The 2★ Halloween Rico row resolves to base ID `034`; Kain (`029`) matches by Japanese name plus rarity/role/element; Santa Clauster (`042`) and both Tyltyl entries (`004`, `026`) have documented name/title matches. Four IDs (`017`, `023`, `044`, `051`) were already represented in earlier candidate or strict evidence, leaving **58 additional identified candidate tuples**. Every row still lacks a printed level and confirmed equipped/unequipped state. They are useful raw rebalance anchors and receive no new strict base-stat credit.

The TSV includes Japanese source title, catalog ID when crosswalked, draw rarity, role, element, combat power, all ability tokens, level/gear-context labels, fetch status, capture timestamp, and the exact archived profile URL. `ok` means the 13 numeric tokens were extracted; it does not certify a base-level or gear-free interpretation. The index harvest did not save page images or alter the archive.

## Local calibration limits

The recovered local leveling artifacts do not resolve the profile pages' missing level or equipment state:

- [`leveling-chunk09.json`](../../../sources/observations/in-game-stats/leveling-chunk09.json) contains role modifiers and `rank_1..rank_5`; the project balance analysis classifies that rank table as the **monster-rank** multiplier, not a hero level curve ([`catalogue/INDEX.md` §5.2](../../../catalog/INDEX.md)).
- [`leveling-chunk019.csv`](../../../sources/observations/in-game-stats/leveling-chunk019.csv) maps `power,rank,hyper,level` thresholds; it does not supply per-hero HP/ATK/DEF growth. [`leveling-chunk001.csv`](../../../sources/observations/in-game-stats/leveling-chunk001.csv) is an upgrade-cost table.
- Beckhen (`051`) has an independently verified Lv.30, 5★, no-equipment row in [`catalogue/stats/051.md`](../../../datasets/hunters/observed-stats/051.md). The archived profile says 3★ at draw, so comparing the rows mixes rank and level changes. The near-common HP/ATK/DEF ratios do not isolate either factor or establish baseline context for the other archived rows.

Do not normalize the archived profiles to Lv.1 or subtract gear using these shared tables. They remain useful static basic-ability estimates, with rank-at-draw visible and level/equipped state unresolved.
