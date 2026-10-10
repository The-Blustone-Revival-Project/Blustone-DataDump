# Multiplier / percentage-addition lane — 2026-10-05

**Lane:** jewel set bonuses, crystal main/sub stats, equipment upgrade gains,
skill percents, recruitment-bonus overlays, Strength-list context.
**Status:** research consolidation only. No server/APK changes. No new strict
coverage credit; all strict percentages are unchanged.

**Rules applied:** raw numerals and units preserved exactly (Image 11 `30` /
`12` carry no printed unit — no `%` added); pre/post 2019-09-05 eras separated;
generic `LEVELING.jet` parameters never used as per-hero or per-item rows.

## 1. Sources consulted

| # | Source | What it contributes | Era tag |
|---|---|---|---|
| S1 | Community FAQ images 10/11 (`analysis/catalogue/stats/found/faq-image10-jewel-seteffects-a.png`, `faq-image11-jewel-seteffects-b.png`), transcribed in `analysis/catalogue/stats/GEAR.md` §3 | 12-family set-bonus list incl. Offensive Mount 2 / AP 5%; literal `30` / `12` tokens | **ERA-UNKNOWN** — FAQ doc recovered 2026-09-30; exact screenshot capture build/date not established; do not assume a side of the 2019-09-05 change |
| S2 | VSFan APK 1.4.4.1 `UI_CSV/3d98d128.json` record `CONTENTS11_8` ("Set Effect"), extracted in `analysis/research/vsfan-extracted-assets.md` §"Jewel set-bonus table" | All 12 set bonuses with 2/4-piece thresholds, five locales (KO/EN/JP/ZH/ZT) | **PRE-THRESHOLD build** (1.4.4.1 predates the 2019-09-05 announcement; exact help revision date unknown) |
| S3 | Six Lv.15 mounted-jewel panels (`GEAR.md` §2, FAQ images 22–27) | Sample main/sub stats at Lv.15/15, 5-star "Highest Class" | **ERA-UNKNOWN** (same FAQ capture caveat as S1) |
| S4 | Official TapTap announcement ([post 73656](https://www.taptap.io/post/73656), posted 2019-09-04, effective after 2019-09-05), summarized in `stat-version-context.md` | Crystal/equipment percentage changes, upgrade-gain change | **THRESHOLD DEFINITION** itself — divides pre/post eras; supplies no per-item rows |
| S5 | FAQ image 7 (`faq-image07-card-010-vincent-equip-EN.png`, `GEAR.md` §1/§4, `catalogue/stats/010.md`) | Adjacent-level armor comparison, upgrade cost | **ERA-UNKNOWN** (FAQ capture caveat) |
| S6 | Caragublu guide ([2018-12 post](https://www.caragublu.com/2018/12/blustone-game-guide.html), image 4/7) | Crocus skill percent pair | **PRE-THRESHOLD** (2018-12 publication predates 2019-09-05) |
| S7 | Reddit clan-Discord gallery ([Old Bluestone Screenshots](https://www.reddit.com/r/Blustone/comments/1vyddln/old_bluestone_screenshots/), items 9/10/12/13) | Lawrence / Leon Summer bonus overlays; Offense/Defense Strength lists | **POST-THRESHOLD captures** (photo-viewer overlays 2020-07/08 for items 9–10; list frames undated within the same gallery; client build unknown in all cases) |
| S8 | `LEVELING.jet` (21 resources / 20 textual payloads) + `EQUIP.jet` (24 `I2` textures) decoded audits | Negative result: shared tuning only; no per-item rows | N/A — constraint source |

## 2. Jewel set-bonus rows (12 families)

Threshold semantics from S2 EN help: 2-piece tier for the first five families,
4-piece tier for the remaining seven; set counting is slot-independent;
duplicate set effects can stack. S1 corroborates structure (its Speed
`1.72` matches an in-game set banner exactly per `GEAR.md` §3).

| Family | Mount | Bonus (raw, as stated) | Source | Era |
|---|---|---|---|---|
| HP Jewel | 2 | Increase HP **5%** | S1 + S2-EN | S2 pre-threshold; S1 era-unknown |
| Offensive Jewel | 2 | Increase AP **5%** (`AP` literal; abbreviation not expanded) | S1 + S2-EN | S2 pre-threshold; S1 era-unknown |
| Defensive Jewel | 2 | Increase DP **5%** (`DP` literal) | S1 + S2-EN | S2 pre-threshold; S1 era-unknown |
| Critical Jewel | 2 | Increase Critical Attack Chance **4.5%** | S1 + S2-EN | S2 pre-threshold; S1 era-unknown |
| Block Jewel | 2 | Increase Block Chance **4.5%** | S1 + S2-EN | S2 pre-threshold; S1 era-unknown |
| Fatal Jewel | 4 | Increase Critical Attack Damage **50%** | S1 + S2-EN | S2 pre-threshold; S1 era-unknown |
| Super Block Jewel | 4 | Damage Reduction Rate **5%** (EN/JP/ZH/ZT) vs **9%** (KO `막기 피해량 9% 증가`) — **unresolved locale conflict, preserve both** | S2 all five locales; S1 reads 5% | S2 pre-threshold; S1 era-unknown |
| Element Jewel | 4 | Increase Elemental Enhancement **23** (flat; S2-EN explicit) | S2-EN (+ S1 wrapped `2…3` digit, decimal unresolved there) | S2 pre-threshold; S1 era-unknown |
| Resistance Jewel | 4 | Increase Elemental Resistance **23** (flat; S2-EN explicit) | S2-EN (+ S1 `23`, decimal unresolved there) | S2 pre-threshold; S1 era-unknown |
| Speed Jewel | 4 | Increase Attack Speed **1.72** | S1 + S2-EN | S2 pre-threshold; S1 era-unknown |
| Regeneration Jewel | 4 | Increase HP Regeneration **30** — digits only, **no unit printed, none added** | S1 + S2-EN (`…Regeneration 30`) | S2 pre-threshold; S1 era-unknown |
| Penetration Jewel | 4 | Increase Armor Penetration **12** — digits only, **no unit printed, none added** | S1 + S2-EN (`…Penetration 12`) | S2 pre-threshold; S1 era-unknown |

Notes:
- The S2 flat `+23` readings resolve the **set-effect** Element/Resistance
  values only. They do not settle any individual jewel-instance main/substat
  decimal placement — keep those questions separate.
- S4 says set-bonus stats were also raised post-2019-09-05 but gives **no
  exact amounts**. Do not reverse-apply any delta to the rows above.
- Jewel count toward the goal is unchanged: 12/12 families historically
  observed (11 locale-consistent, 1 disputed); six Lv.15 panels remain a
  sample, not a catalog.

## 3. Crystal main/sub stats (post-threshold percentages, no per-item rows)

From S4 (official announcement text; no per-item anchors supplied):

| Scope | Change | Era |
|---|---|---|
| 1–3★ crystal main stats | **+30%** | post-2019-09-05 balance |
| 4–5★ crystal main stats | **+50%** | post-2019-09-05 balance |
| All crystal substats | **+50%** | post-2019-09-05 balance |
| Substat upgrade amounts | fixed at the **maximum** (was random in range) | post-2019-09-05 balance |
| Set-bonus stats | raised, **exact delta not given** | post-2019-09-05 balance |
| Main-stat selection frequency | adjusted (no numbers) | post-2019-09-05 balance |

Related S4 equipment rows kept here for stratification (not crystal data):
equipment stat values **+50%**; fractional stat increments removed; upgrades
after equipment-modification stage 2 (equipment level 20+) gain **larger
increases** (no exact curve). Attack, DEF, HP, elemental enhancement/
resistance, penetration strengthened; crit chance/damage, block chance,
block-damage reduction got smaller boosts (no numbers).

## 4. Equipment upgrade-gain observations (adjacent-level, era-unknown)

From S5 (`GEAR.md` §§1/4; FAQ capture build unknown):

- Vincent (`010`) Purple Combat Coat armor **Lv.49 → Lv.50**: DEF
  **101 → 102** (+1); displayed Strength **33,038 → 33,057** (+19).
  Single adjacent-level pair — indicative only, not a per-level curve.
- Beckhen (`051`) panels at **Lv.50/50** (weapon ATK 134, armor DEF 102,
  accessory Jack Max HP 260) are already maxed; their `30359 → 30359`
  Strength preview changed nothing.
- Upgrade screen cost: **50,000** currency + materials at **389/320** and
  **11/27** (red = short); held balance **8,695**.
- Modification gates at upgrade levels **10/20/30/40**; +1 jewel slot at
  level 20 (prose corroboration noted in `GEAR.md` §4).
- All of the above are **ERA-UNKNOWN**; do not place them pre/post threshold.

## 5. Skill and recruitment percent modifiers (rebalance context, no coverage)

| Subject | Raw reading | Source | Era |
|---|---|---|---|
| Crocus `Necromancer's Might`, skill Lv.35/50, All Enemies / Everlasting Effect | Enemy Max HP effect **8.75% → 9.00%** | S6 (skill-training panel) | PRE-THRESHOLD (2018-12) |
| Lawrence (`079`), `Knight of Swimming Pool`, `New Hunter Bonus` | DEF **20.0%** + adjacent **+1.0%** (meaning of `+1.0%` unknown); panel also shows `+1000`, `Show off now!` | S7 item 9 | POST-THRESHOLD capture (2020-08-24 overlay; build unknown) |
| Leon Summer (`094`), `Lifeguard`/`Leon`, `New Hunter Bonus` | HP **13.0%** + adjacent **+1.0%** (meaning unknown); panel also shows `+1000`, `Show off now!` | S7 item 10 | POST-THRESHOLD capture (2020-07-29 overlay; build unknown) |

All three are polluted/partial modifier evidence (full details in
`polluted-observations.md`); none is a hero base stat and none earns coverage.

## 6. Offense/Defense Strength lists (group-level context only)

S7 items 12–13: `Hunter List` sorted by `Strength`, roster count `98/105`.
Offense tokens (row-major): `43,358 / 43,047 / 42,329 / 40,214`;
`38,606 / 37,522 / 36,081 / 36,063`; `32,698 / 29,447 / 29,193 / 29,146`;
`28,821 / 23,160 / 17,243 / 16,548`. Defense tokens (row-major):
`53,395 / 45,183 / 44,712 / 39,189`; `37,562 / 36,822 / 36,734 / 35,138`;
`33,376 / 32,417 / 31,510 / 27,385`; `27,201 / 26,835 / 24,868 / 24,452`.
Most badges read `Lv.MAX` (one `Lv.19`, two `Lv.1`). These are current
displayed values under unknown gear/jewel/buff state — useful only for later
rebalance estimates. No per-hero mapping beyond the two medium-confidence
portrait matches already recorded in `polluted-observations.md`.

## 7. LEVELING.jet / EQUIP.jet constraint (do not use as growth)

- `LEVELING.jet` chunk 9 `rank_1..rank_5` = **monster-rank** multiplier, not a
  hero level curve (per `catalogue/INDEX.md` §5.2).
- `LEVELING.jet` chunk 19 = `power,rank,hyper,level` threshold table; chunk 1
  = upgrade-cost table. Neither supplies per-hero HP/ATK/DEF growth.
- `EQUIP.jet` = 24 `I2` textures; no stat table of any kind.
- Do not normalize the 2019 archive hunter profiles or any screenshot with
  these shared parameters.

## 8. Coverage impact

None. Strict ledgers are unchanged: heroes 1/113, jewel families 12/12
observed (1 disputed), mounted panels 6/6 samples, accessories 1/100,
monsters 0/22. Every row above is historical-version or polluted-track
material for future rebalance work.
