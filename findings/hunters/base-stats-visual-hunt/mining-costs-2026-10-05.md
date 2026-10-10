# Jewel mining/polish COST hunt — 2026-10-05

**Lane:** BLUSTONE mining/polish COST numbers (rupee cost table, Manda mining
price, per-stage success rates, polish-failure terms).
**Status:** research consolidation only. No server/APK changes. No new strict
coverage credit; strict ledgers unchanged (jewel samples 6/6, accessories
1/100, heroes 1/113, monsters 0/22).

**Rules applied:** raw numerals and units preserved exactly; pre/post
2019-09-05 eras separated; generic `LEVELING.jet` parameters never used as
per-item rows; community text and help prose are marked TEXT-SOURCE and never
presented as visual panel evidence. The `LEVELING.jet` res-1 CSV is
probability TUNING, not a cost table — it is never presented as costs.

Parent lanes: [`jewel-economy-2026-10-05.md`](jewel-economy-2026-10-05.md) §5
(mechanics + open gap), [`jewel-instance-2026-10-05.md`](jewel-instance-2026-10-05.md)
(removal footer), [`multipliers-2026-10-05.md`](multipliers-2026-10-05.md).
Coverage definitions: [`coverage.md`](coverage.md).
Impure ledger appendix: [`polluted-observations.md`](polluted-observations.md)
("Mining/polish impure cost tokens").

---

## 1. PURE — mechanics reconfirmed (no cost numerals asserted)

All of the following are qualitative rules re-verified against local sources
in this pass. None carries a rupee amount, a Manda price, or a success-rate
value.

- **Jewels are Metron Crystals graded by class; higher class = higher
  ability.** Collected through mining; also found via lucky Hunter Search and
  sold at the Market. Polishing further enhances effectiveness; wearing
  multiple jewels of the same kind creates a synergy (set) effect.
  Source: VSFan 1.4.4.1 EN help `CONTENTS11_4` (PRE-THRESHOLD build),
  full text in `analysis/research/vsfan-extracted-assets.md` ll.733–747.
- **Daily free mining:** the Hunter Union supports free mining every day; the
  player selects the kind of jewel and mines a random jewel of that kind.
  Source: `CONTENTS11_5` (`vsfan-extracted-assets.md` ll.749–753).
- **Manda mining:** rarer jewels are acquired by using Manda to mine — no
  amount stated. **Advanced mining** acquires higher-class jewels quicker —
  no price or rate stated. Source: `CONTENTS11_5` (ll.754–757).
- **Polish terms:** no particular materials are needed, but large sums of
  rupees are required (amounts unstated); the higher the polish stage, the
  more difficult (lower probability) it becomes; **failing loses only the
  spent rupees, with no further penalty.** Source: `CONTENTS11_6` (ll.759–770).
- **Mounting:** jewels mount into equipment rabbets whose shape must match;
  slotted equipment types are weapons, armor and accessories.
  Source: `CONTENTS11_7` (ll.772–782).
- **Native polish-price schema (field identities only, values unknown):**
  `/reference/GetGemLevelUpPrice` rows carry `level, price_type, price,
  possibility, failed_compensation, add_sub_ability`
  (`analysis/research/gem-reference-contract.md` §"Price-row fields").
  This proves the polish-cost table EXISTS as a server reference with a
  success-rate column (`possibility`) and a failure-compensation column —
  consistent with the probabilistic fail=lose-rupees rule — but **no original
  row values have been recovered**; the replica serves empty arrays.
  Sibling schemas `GetGemSellPrice (rank,level,price_type,price)` and
  `GetGemDisassemblePrice (level,price_type,price)` are likewise
  field-identities without values. No mining-price route (Manda mining cost)
  has been isolated in native evidence.
- **`LEVELING.jet` res-1 is NOT a cost source.** It is a polish-probability
  CSV covering ranks 2–15 with base/attempt values — shared tuning only, no
  costs, no stat rows
  (`old-apk-2026-10-05.md` §3 table row 1; `jewel-economy-2026-10-05.md`
  §5). Do not present it as a cost table.

## 2. UNPURE — every cost/probability numeral found (rebalance leads only)

None of the following counts toward any 70% threshold. Each entry preserves
its source, era, and the exact reason it is impure.

- **Jewel removal footer: `40000` (gold icon) / `40` (second currency icon,
  identity unknown).** Visual panel evidence (FAQ image22 footer,
  `analysis/catalogue/stats/found/faq-image22-jewel-*.png`), but confirmed on
  image22 ONLY — do not assert it for the other five panels. The second
  currency is unidentified (not proven to be Manda). Capture era unknown
  (ERA-UNKNOWN). This is a REMOVAL fee, not a mining or polish price; do not
  file it as either. Source: `jewel-instance-2026-10-05.md` §1.3.
- **Community refine budget: "at least 600k rupees"; fail risk rises "after
  level 9+".** Unattributed FAQ prose
  (`recovered-assets/community-notes-2026-09-30/Blustone Guide FAQ.md` L426):
  *"it also makes the stat reward higher … However, the higher the level a
  gem is, the higher the chance to fail refining it will be. (It can be very
  frustrating and money/time consuming after level 9+, so be sure to count
  with lots of resources before attempting to do so, at least 600k
  rupees)."* TEXT-SOURCE, author/date/build unknown, ERA-UNKNOWN. The
  level-9+ risk escalation corroborates the native "higher stage = harder"
  rule qualitatively; the 600k figure is a player budget recommendation, NOT
  a per-attempt price. No per-stage price or success-rate table accompanies it.
- **Honor-medal trace rates: ★4 trace = 700 medals per 8 traces; ★3 trace =
  350 per 8.** TEXT-SOURCE from the Namu item page (§4.3-adjacent economy,
  transcribed in `jewel-economy-2026-10-05.md` §3; mirror edited 2026-06-19,
  content describes the pre-shutdown game, ERA-UNKNOWN). Adjacent economy
  context only — these are trace-exchange rates, not mining/polish costs.
- **Post-threshold polish growth (official text, POST era): ★1–★3 mains
  +30%, ★4–★5 mains +50%, all substats +50%, substat upgrades fixed at
  maximum.** Source: Traditional-Chinese TapTap announcement posted
  2019-09-04, effective after 2019-09-05
  (`stat-version-context.md`; `wayback-announce-2026-10-05.md` §1.1). These
  are growth multipliers, not prices or success rates; stratify pre/post
  screenshots as separate eras.
- **Namu equipment upgrade rupee/toolbox tables: NOT transcribed.** Grade-1
  rows show toolbox/rupee tokens (`500/1000/5000`-ish) in garbled table order
  and grades 3–5 render only as guild-discount placeholders
  (`jewel-economy-2026-10-05.md` §3; `namu-tables-2026-10-05.md`). Column
  alignment is ambiguous, so no exact per-level value is claimed here — and
  these are equipment-upgrade costs, not jewel mining/polish costs in any case.
- **Namu item page §4.4.3 결정 (Crystal): still an empty header** (negative
  result reconfirmed via full-text fetch in `jewel-economy-2026-10-05.md`
  §3). No per-star crystal/jewel stat or price table exists there.
- **Fresh-search negative results (this pass):**
  - English game-jewel queries (`Blustone jewel mine polish upgrade cost
    screenshot game`; `"blustone" game jewel refine rupee cost level 9`)
    return only the Indian jewelry retailer, unrelated titles, or unrelated
    places/materials — the game name collides with a jeweler and a building
    stone. No game cost screenshot.
  - Korean queries (`블루스톤 보석 연마 비용 루피 광산`) return Clash of
    Clans gem-mine guides, Aion 2 gem-polish guides, Lost Ark crystal-cost
    threads, and the Namu wiki item page — no Blustone jewel cost panel.
  - The Namu wiki item-page snippet visible in search confirms adjacent
    fuel/shop figures only (Manda 5 → 60 fuel; market rupee corner 6,000 →
    60 per 4h), already captured in `jewel-economy-2026-10-05.md` §3.

## 3. Coverage impact

None. Strict ledgers are unchanged: mounted panels 6/6 samples (no seventh
found), accessories 1/100, heroes 1/113, monsters 0/22. §1 is qualitative
mechanics context; §2 numerals are polluted/supplementary track only.

## 4. Remaining open gap (unchanged)

Still missing: the **rupee polish-cost table per stage** (native schema
`GetGemLevelUpPrice` proves where it would live), the **Manda mining price /
advanced-mining price**, and any **per-stage success-rate screenshot or value
table**. The most promising unmined leads are archival captures of the
in-game polish panel and the original `GetGemLevelUpPrice` reference rows —
not further English/Korean web search, which is exhausted by name collision.
