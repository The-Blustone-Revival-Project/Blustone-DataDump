# Jewel-instance / crystal-catalog / equipment-gate lane — 2026-10-05

**Lane:** jewel INSTANCE main/substat decimals (separate from set-effect `+23`),
Lv.15 mounted-panel expansion beyond the 6 sampled, crystal catalog per-star
values, equipment modification 10/20/30/40 gates.
**Status:** research consolidation only. No server/APK changes. No new strict
coverage credit; all strict percentages are unchanged.

**Rules applied:** raw numerals and units preserved exactly; pre/post 2019-09-05
eras separated; generic `LEVELING.jet` parameters never used as per-hero or
per-item rows; text guides are marked TEXT-SOURCE and never presented as visual
panel evidence.

Parent consolidation: [`multipliers-2026-10-05.md`](multipliers-2026-10-05.md).
Coverage definitions: [`coverage.md`](coverage.md).

## 1. Six Lv.15 panels re-verified pixel-for-pixel (no expansion)

All six FAQ jewel panels under
`analysis/catalogue/stats/found/faq-image22..27-jewel-*.png` were opened
visually on 2026-10-05. Every main/substat transcription in
[`GEAR.md`](../../../datasets/equipment/GEAR.md) §2 matches exactly, including
decimal placement. No seventh panel surfaced anywhere in this lane's searches
(§4), so the sample stays at six.

Direct-viewing additions (layout facts visible on the panels themselves):

| Panel | Title (raw) | Mount (raw) | Main (raw) | Substats (raw, in order) |
|---|---|---|---|---|
| image22 | Radiant Speed Jewel | [Mounted on Weapon] | ATK `+29` | Critical Attack Damage `+3.13` · Block Chance `+0.72` · Elemental Resistance `+1.44` · Damage Reduction Block `+0.50` |
| image23 | Radiant Offensive Jewel | [Mounted on Weapon] | ATK `+29` | DEF `+11` · Damage Reduction Block `+0.38` · Elemental Enhancement `+1.65` · ATK `+11` |
| image24 | Radiant Offensive Jewel | [Mounted on Accessories] | Max HP `+58` | ATK `+12` · Max HP `+21` · Elemental Resistance `+1.69` · Block Chance `+0.56` |
| image25 | Radiant Speed Jewel | [Mounted on Accessories] | Max HP `+58` | Max HP `+18` · Critical Attack Damage `+3.87` · Block Chance `+0.56` · ATK `+13` |
| image26 | Radiant Speed Jewel | [Mounted on Armor] | Block Chance `+2.30` | Block Chance `+0.56` · Max HP `+21` · Damage Reduction Block `+0.50` · DEF `+11` |
| image27 | Radiant Speed Jewel | [Mounted on Armor] | DEF `+29` | Critical Attack Chance `+0.67` · Damage Reduction Block `+0.38` · ATK `+11` · Critical Attack Damage `+3.86` |

Common chrome on all six: 5-star grade, `Highest Class Jewel Carries <Family>
Power` subtitle, `Lv. 15/15` level line. **ERA-UNKNOWN** (same FAQ capture
caveat as the parent lane's S1/S3).

### 1.1 Instance decimal-placement pattern (separate from set-effect +23)

Percent-type instance stats carry two decimals; flat stats are integers —
**except** Elemental Enhancement/Resistance instance substats, which carry two
decimals (`+1.44`, `+1.65`, `+1.69`):

- 2-decimal instance values: Crit Damage `+3.13/+3.87/+3.86`, Block Chance
  `+0.72/+0.56` (×3), Elem Resist `+1.44/+1.69`, Elem Enh `+1.65`, Dmg Red Blk
  `+0.50/+0.38` (×2 each), Crit Chance `+0.67`, Block Chance main `+2.30`.
- Integer instance values: ATK `+29/+11/+12/+13`, DEF `+11/+29`, Max HP
  `+58/+21/+18`.

This is an **instance-level** decimal observation. It does not change the
set-effect readings (Element/Resistance set bonus flat `+23`, Super Block
`5%` vs KO `9%`, unitless `30`/`12`) consolidated in the parent lane — keep
the two layers separate.

### 1.2 Jewel name does not determine the main stat (mechanics observation)

- Weapon slot yields main ATK `+29` under **both** names (Speed image22,
  Offensive image23).
- Accessory slot yields main Max HP `+58` under **both** names (Offensive
  image24, Speed image25).
- Armor slot yields **two different mains** under the **same** name
  (`Radiant Speed Jewel` → Block Chance `+2.30` in image26, DEF `+29` in
  image27).

So the panel title family is not a reliable predictor of the main stat in this
sample; slot correlates for weapon/accessory but armor varies. With n=6 this
is a mechanics lead only — do not generalize to a rule, and it earns no
coverage. Logged in the polluted ledger for rebalance context.

### 1.3 Panel chrome: set-effect footer and removal cost

- Each panel's `Set Complete Effect` footer restates its family bonus:
  Speed panels read `Mount 4, Increase Attack Speed 1.72`; Offensive panels
  read `Mount 2, Increase ATK 5%`. Note the panel wording is **ATK**, while
  the FAQ list (parent lane S1) and VSFan EN help (S2) word it **AP** /
  **DP**. Preserve both wordings; do not expand the abbreviation.
- image22 shows a `Required Cost for Remove` footer reading `40000` (gold
  icon) `/ 40` (second currency icon, identity unknown). The footer was only
  confirmed on image22 in this pass; do not assert it for the other five.
  Both tokens are polluted-track only.

## 2. Crystal catalog per-star values: NOT recovered

No per-star, per-item crystal/jewel main-stat table surfaced. The only
crystal numerics remain the S4 post-threshold percentages in the parent lane
(1–3★ main `+30%`, 4–5★ main `+50%`, all substats `+50%`, substat upgrades
fixed at maximum). The Namu item page's `4.4.3 결정` (Crystal) section is an
**empty header with no body text** (verified 2026-10-05 via page fetch) —
a negative result, not a source.

## 3. Equipment modification gates: text-source cross-check (no new values)

Three independent text sources agree on modification at upgrade levels
**10/20/30/40**, consistent with the FAQ prose already cited in `GEAR.md` §4:

1. FAQ prose (via `GEAR.md` §4) — modification gates 10/20/30/40, +1 jewel
   slot at level 20. ERA-UNKNOWN.
2. VSFan 1.4.4.1 help `CONTENTS11_3` (PRE-THRESHOLD build) — modify at
   levels 10/20/30/40; modification raises ability and the upgrade cap;
   element materials Fire=Flammable Material, Ice=Coolant,
   Electricity=Lightning Box; materials are rare Mirage Ruins finds.
3. Namu item page §4.3 (TEXT-SOURCE, ERA-UNKNOWN — mirror edited
   2026-06-19, content describes the pre-shutdown game): each equipment
   grade holds 10 levels and grade-up (`장비 개조`) occurs per grade;
   element materials 번개 막대/냉각수/인화성 물질; toolbox/rupee cost
   tables are only partly legible (grade-1 toolbox row fragments, costs
   `500/1000/5000` in garbled table order) — **do not transcribe these as
   exact values**; the table rendering is ambiguous. No per-level stat
   curve is given anywhere.

No source in this lane supplies a per-level equipment stat curve or a
per-grade stat table. The Vincent Lv.49→50 `DEF 101→102` pair (parent lane
S5) remains the only adjacent-level observation.

## 4. Searches run (negative results preserved)

| Query / source | Result |
|---|---|
| Korean `블루스톤 보석 세트효과 수정 수치 쥬얼 장착 스크린샷` | Black Desert crystal guides; no Blustone panel |
| Japanese `ブルーストーン ジュエル 装着 効果 数値 修正 クリスタル` | Real-world gemstone jewelry; no game panel |
| English `Blustone VisualShower Metron Crystal jewel mount polish mining screenshot` | One [official event post](https://www.facebook.com/visualshowerEN/posts/blustone-event-the-more-the-better-by-lottery-mouseyou-will-get-a-metron-crystal/1124385431051052/) (Metron Crystal per 10+1 pull — economy note, not stats); wiki/index pages |
| Korean `블루스톤 메트론 수정 연마 장착 쥬얼 효과` | Namu lore/review pages; no stat panel |
| English `blustone jewel guide upgrade level 15 radiant polished stats` | Unrelated music/game results; no panel |
| [Namu item page](https://dark.namu.moe/w/%EB%B8%94%EB%A3%A8%EC%8A%A4%ED%86%A4/%EC%95%84%EC%9D%B4%ED%85%9C) (TEXT-SOURCE) | §4.3 grade/gate structure + garbled cost tables; §4.4.3 결정 empty; no per-star crystal values |
| Miraheze wiki `Jewel` full-text search | 4 hits, all story-dialogue pages (`Blue Jewel`, `A Metron Crystal!`) — no item-stat page |
| Fandom `blustone.fandom.com` wiki | HTTP 403 on fetch; no content inspected |
| r/Blustone `iq4irt` jewel thread | Fetch blocked; only a search-snippet community claim (jewels usable from 4★ hunters in the equipment panel) — unattributed text, not visual evidence |
| Prior gallery audits (Reddit 13-image, memorial 57-image, GameAppCH 20, AppStorio, HungryApp, Aptoide, PDALIFE, Uptodown) | Already screened per `coverage.md` / README; none contains a jewel/crystal detail panel |

## 5. Coverage impact

None. Strict ledgers are unchanged: mounted panels 6/6 samples (no seventh
found), accessories 1/100, heroes 1/113, monsters 0/22. The §1.2–§1.3
mechanics observations and the §3 text cross-check are polluted/supplementary
track only.
