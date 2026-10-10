# SYNTHESIS index — base-stat recovery session, 2026-10-05

**Written:** 2026-10-05, as a navigation layer over this folder. It is a
**read-only synthesis**: nothing here re-derives a value, and nothing here is
evidence. Every claim below names the file that holds it. Where a file
contradicts itself across its own sections, that is recorded as such rather
than silently harmonised.

**Two files define the goal and were not modified:** [`coverage.md`](coverage.md)
(target definitions, denominators, current counts) and
[`README.md`](README.md) (source table, search log, per-source visual verdicts).
This file does not restate their contents; it points at them.

## Headline state (as recorded in `coverage.md`)

| Dataset | Count | Target | Source of the count |
|---|---|---|---|
| Hero base stats | **1 / 113** (`051` Beckhen) | 80 | `coverage.md` "Starting point" |
| Jewel set-bonus families | **12 / 12 observed** (11 locale-consistent, 1 disputed) | 9 — met | `coverage.md`; transcription in `jewel-help-locales-2026-10-05.md` §1.4 |
| Mounted jewel panels | **6 / 6 samples** | 5/6 — met | `coverage.md`; re-verified in `jewel-instance-2026-10-05.md` §1 |
| Accessories | **1 / 100** (Jack, Max HP 260 @ Lv.50) | 70 | `coverage.md` |
| Monsters | **0 / 22** | 16 | `coverage.md` |

**The single most important structural finding of the session** is stated in
`fixture-conflict-audit-2026-10-05.md` §2.1: the replica's *protocol shapes* are
overwhelmingly corroborated (29 CORROBORATED rows, of which the vast majority are
native-parsed) while its *numbers* are overwhelmingly unrecovered (~78
UNSUPPORTED). The shape of that tally **is** the finding. A future agent should
not read the economy fixtures as "probably right" or as "known wrong" — most of
them are simply unconstrained.

## 0. Evidence classes used across this folder

Defined in `fixture-conflict-audit-2026-10-05.md` (verdict scale + evidence-class
column) and honoured by every lane file:

- **[NATIVE]** native parser / decompile / runtime read — strongest.
- **[ORIGDATA]** data or prose shipped inside the original client (`UI_CSV`
  `HELP_DATA`, `R_EPISODE.jet`, `CHAR_STR_RO`, recovered CSV).
- **[COMM]** community prose (one source, or two that agree).
- **[SELF]** the replica's own captured receipt — proves internal coherence only.

Two further labels are per-lane and must not be mixed with the above: **PURE**
(verbatim reading, no interpretation) and **UNPUR[E]** (every numeral preserved
as an era-tagged token, zero coverage credit). Most dated lane files are split
this way on purpose.

**Era rule, absolute.** `stat-version-context.md` fixes the rebalance threshold
at **2019-09-05** (announcement 2019-09-04, effective after 2019-09-05). Full
announcement text is transcribed in `wayback-announce-2026-10-05.md` §1.1 and
`apk-diff-2026-10-05.md` corroborates. PRE/POST tagging is required for every
datum; `namu-tables-2026-10-05.md` and the whole Namu corpus are
**ERA-UNRESOLVED** and must never be normalised across the threshold
(`transcendence-skill-cost-2026-10-05.md` source table; `help-2_8-sweep-2026-10-05.md` §0.1).

---

## 1. What was actually RECOVERED vs what stayed a negative, by system

"Recovered" below means *the artifact exists in hand at the stated class*. It
does not mean "original balance recovered" — very few originals were.

### 1.1 Gacha / recruitment

**Recovered (native + live UI + image frame):**
- Exact prices and the complete count vocabulary: 30 single / 300 bundle, and
  only counts 1 and 11 exist. Native constant vector `[100, 300, 11, 30]` at
  `CSRDataMgr::Init` `8b1d60`, renderer at `e40824`, no divisor in
  `PurchaseConfirm::SetData`. Verdict row **F1/F2 CORROBORATED**
  (`fixture-conflict-audit-2026-10-05.md` §1.F).
- Count-dependent award shape: cnt1 → single object, cnt>1 → array, cnt0 → null
  (`F7`, native `f753f8`; root-cause write-up in AGENTS §26).
- The three-star-or-above bundle guarantee, **seen on device**
  (`F3`; AGENTS §59; confirm screenshot in `analysis/testing/revival-009/`).
- Recruitment mileage per-phase split, **original pixels**: `0→x3`, `x10`,
  `x25`, `x40`, summing to 78 (`result-screens-2026-10-05.md` R5, RECOVERED-image-frame).
- Coupon path exists natively: `Lottery.OnClickRequestGachaByCoupon` `Ge40020` →
  `LotteryShot` → `/shop/GachaPremium` with `item_inst_id`
  (`fixture-conflict-audit-2026-10-05.md` D2; AGENTS §118).

**Negative / still missing:** pool contents, per-pool probabilities, pity and the
16-pull banner guarantee are **[COMM] only** (`F4`); the guaranteed-ticket
detail is 2.8.0.1-only first-party prose (NEW-4 in
`help-2_8-sweep-2026-10-05.md` §2.8). Official **gacha boost multipliers are now
three datapoints and reconcile by scope**: September limited ★3 = 400%, all ★3 =
200%; October limited = 400%, all = 200%; Halloween-limited = 500%, all = 200%
(`event-board-bodies2-2026-10-05.md` §2.7) — this **retires** pass 2's
"self-contradiction" flag.

### 1.2 Training / RankUp / level curve

**Recovered (three-way agreement is the strongest result in this system):**
- Max 5 partners per Raise: guide + native five-source limit `G101de2e..3c` +
  server refusal all agree (`training-rankup-rules-2026-10-05.md` rule 1, MATCH).
- Fodder eligibility mechanism: native `SearchStuff` ctor `101f9bc` builds a
  rank-1 whitelist (006/007/011/014/016/017/018/019/020) and a rank-2 whitelist
  (005/013/015/021/024/025/030/032) and filters on minimum **STAT** rank, not
  recruit grade (rule 2, DIRECTION MATCH; `B13` CORROBORATED).
- Rank-up material count = current star count, for ranks 1–4 (`B6`
  CORROBORATED; two community sources plus native capacity/getter shape).
- Ordinary level cap 30 regardless of grade (`B4` CORROBORATED; community +
  native `GetCardMaxLevel` shape).
- Zero→1 skill initialisation is legal natively (`A6` CORROBORATED, no
  positive-owned-level gate at `Select` `d55bfc`).
- Five mandatory skill slots and their semantics map one-to-one onto first-party
  `CONTENTS4_4` (`A7` CORROBORATED).
- Ordinary level/EXP/gold cost for Raise, source XP and cumulative XP: **not
  recovered at all** (`B1`–`B3` UNSUPPORTED).
- RankUp cost `1000/source` and `stat_bonus: 5` coefficient: **not recovered**
  (`B8`, `B9` UNSUPPORTED); only native *formula* shape exists.

**Native parser recoveries (structure, not values):**
- `/gym/RankUpBundle` **is** the native batch path; requester
  `RequestGroupRankUp(uint×5)`, callback `ReqGroupRankUpCB`, sink
  `CSRInventory::SetCardRank` — and it carries **no PARAM struct**, unlike
  single `ReqRankUpCB` which sinks `void(RANK_UP_PARAM)` by value
  (`batch-rankup-chucoin-2026-10-05.md` §1.1). Wire shape NOT recovered.
- `/shop/SellCard` takes an **instance-ID vector**; request field recovered as
  `inst_id_list`, numbers not strings
  (`batch-rankup-chucoin-2026-10-05.md` §1.2;
  `grouprankup-sellcard-bodies-2026-10-05.md` §1.3).
- Batch rank-up response uses `card.removed_inst_id_list` + `card.target_list[]`,
  **not** the single-path `target_inst` family
  (`grouprankup-sellcard-bodies-2026-10-05.md` §1.6).

**Negative:** the Chu-coin / Secret Market economy is a **native negative** — no
coin/secret/market key in any of the four audited bodies (same §1.6), so
training-rankup-rules rule 9 stays UNIMPLEMENTED on archive evidence only.

### 1.3 Transcendence and skill costs

**Recovered (two-source reconciliation, `[EN-2017]` × `[NAMU]`):**
- The two sources are **the same table**: 9 identical Transcendence cells and
  **30/30 identical skill material cells**, 39 exact coincidences across two
  languages and two sites. Both most plausibly transcribe a common original;
  **neither is native-recovered** (`transcendence-skill-cost-2026-10-05.md`
  headline finding 1).
- Fragment ladder is a **decadal step function**: `[EN-2017]`'s `1,1,2,2,3,3,4,4,5,5`
  collapses to `1..5`, which uniquely resolves `[NAMU]`'s five-values-for-ten-bands
  pairing into **consecutive band-pairs** (finding 3; conflict C9 RESOLVED).
- fragment:crystal = **10:1 holds 9/9 in `[EN-2017]` and 11/11 in `[NAMU]` — but
  table-scoped only.** The skill table has no crystal column, so 10:1 is **not** a
  global invariant (finding 4).
- The `3★`-floor fodder rule is **not** a conflict between the two sources: first-party
  `CONTENTS4_3` says both clauses in one paragraph (C3 RESOLVED, §2.10).
- First-party prose publishes the **gate** text identically in 1.4.4.1 and
  2.8.0.1 for Advancing / Transcendence / Skill Training / Group Advancement,
  including byte-identical group-advance material counts (FOUR ★1 / FIVE ★2)
  (`help-2_8-sweep-2026-10-05.md` §2.4).

**Recovered from original pixels (era-tagged, one account, one build):**
- Transcendence button **9000** rupees + materials 9 / 90 (`result-screens-2026-10-05.md` R9).
- Skill training button **800** rupees at skill 35 with 4 / 4 / 2 materials (R8) —
  and a contemporary source statement: "Collect items by clearing the Expedition Area".
- Advancement buttons **8000** (2 fodder) and **12000** (3 fodder) on the same
  target, so cost varies with fodder count; **no formula inferred** (R7).
- Equipment upgrade **50000** + 320 toolbox + 27 advanced toolbox at armor Lv.49→50 (R6).

**Negative (settled, do not re-run):** **no cost table exists in either help
corpus.** Re-run over all 95 `CONTENTS` records of 2.8.0.1 with 15–20 patterns,
zero hits for every cost pattern — tested twice (73 records of 1.4.4.1, then the
full 2.8.0.1 body). C1/C2/C4 **cannot be closed by help sweeping**
(`help-2_8-sweep-2026-10-05.md` §2.1 and §2.9).

### 1.4 Jewel / crystal / mining

**Recovered:**
- All 12 set-bonus families with 2/4-piece thresholds, five locales, in the
  1.4.4.1 in-game help `CONTENTS11_8` (`jewel-help-locales-2026-10-05.md` §1.3–1.4;
  consolidation with the FAQ panels in `multipliers-2026-10-05.md` §2).
- Element/Resistance set bonuses are **flat `+23`** — this resolves the earlier
  decimal-placement ambiguity for the *set effect* only
  (`multipliers-2026-10-05.md` §2 notes).
- The set-bonus table was **rewritten between versions**: 1.4.4.1 EN
  `5%/4.5%/50%/23/1.72/30/12` vs 2.8.0.1 EN `6%/5%/60%/35/1.72/30/16`
  (`apk-diff-2026-10-05.md` §4; `help-2_8-sweep-2026-10-05.md` NEW-7).
- **Super Block locale conflict is now sharper, not resolved:** 1.4.4.1 reads 9%
  in KO and 5% in EN/JP/ZH/ZT, while 2.8.0.1's `SC` copy says **9%** and the
  other 2.8.0.1 locales say 5% — i.e. **the shipped 2.8.0.1 client disagrees
  with itself**. Preserve both readings; do not assert one universal value
  (`jewel-help-locales-2026-10-05.md` §1.3.4 and §2.8; `coverage.md`).
- FAQ image 10 lists **12** families, not 11 — Offensive Jewel, Mount 2,
  Increase AP 5% (`coverage.md` observation row; this corrects an earlier
  transcription).
- FAQ image 11's `30` and `12` are legible **digits with no printed unit**; no
  `%` was added (same row).
- Polish-price reference schema, six fields, with literal addresses:
  `ret_data, level, price_type, price, possibility, failed_compensation,
  add_sub_ability` (`gem-polish-parsers-2026-10-05.md` §1.1–1.2). Three
  reference routes recovered: `/reference/GetGemLevelUpPrice`,
  `GetGemSellPrice`, `GetGemDisassemblePrice`. Sibling row shapes differ and must
  not be conflated (§1.7).
- `/gem/LevelUp` **request form keys recovered**: seven — `app_code`, `app_ver`,
  `market`, `pvid`, `otp`, `inst_id`, `max_tries` — where `inst_id` is the
  popup's `uint` and `max_tries` is an independent constant `7`
  (`gem-popup-bindings-2026-10-05.md` §1.6).
- A client-side precondition gate, a busy flag, and a wallet-check toast were
  located on that path (same §1.6).

**Negative (settled):**
- `/gem/LevelUp` **response** fields NOT recovered; `ParseGemLevelUp`
  `0x0a4e43c` is the only remaining source (`gem-popup-bindings-2026-10-05.md`
  §4 item 1; `gem-levelup-action-2026-10-05.md` §1.3).
- Manda mining / advanced-mining price: **no native route isolated**.
  `Check10GatchOverGemMineLimit` is a *limit* check, not a price; the
  `/gem/PaidGacha|MileageGacha|DailyFreeGacha` routes are gacha
  (`gem-polish-parsers-2026-10-05.md` §1.8).
- Per-star crystal catalog values NOT recovered; the Namu crystal section is an
  **empty header with no body** (`jewel-instance-2026-10-05.md` §2).
- No per-level equipment stat curve exists in any source; the Vincent
  Lv.49→50 `DEF 101→102` pair remains the only adjacent-level observation
  (same §3).
- Polish rupee table per stage still missing; `mining-costs-2026-10-05.md` §4
  names the only two promising leads (original `GetGemLevelUpPrice` reference
  rows, or an archived polish-panel capture) and states that further EN/KO web
  search **is exhausted by name collision**.
- Removal footer `40000` / `40` is a *removal* fee, not a polish or mining price
  (`gem-polish-parsers-2026-10-05.md` §2).

### 1.5 Campaign economy / missions

**Recovered:**
- The three-star structure (`GetStageAchieveCnt` sums exactly three bytes) and
  `achieve[].order` 0..2 (`C5` CORROBORATED).
- Defeat does not consume fuel: final original `UI_CSV.jet`
  `HELP_DATA/CONTENTS2_3` states ordinary defeat/forfeit does not consume fuel
  in KO/JA/SC/TC while EN says "returned" (`C9` CORROBORATED mechanism;
  implementation in AGENTS §115).
- Chest item **identities** are original: ids 912/913/914 are `CHAR_STR_RO`
  rows titled ★2/★3/★4 Transcendence Ticket (`C11` CORROBORATED for ids), and
  both community tables stop at a 4★ ceiling with no 5★ row.
- Chest *mechanism*: `achieve_cnt == GetStageCnt(area) × (i+1)` → 10/20/30, and
  the receipt applies gold only when `gold.prev != 0`. Amounts NOT recovered (`C10`).

**Recovered from original pixels (single-account, unknown build):**
- Original Search (ruins/abyss) payouts: team level 40 → **+1400** rupees with
  scroll 5 / leaf 4 / trace 40 / orb 1; team level 62 → **+2000** with crystals 8
  / stones 5 / trace 40 / scroll 1. **These are the first original-game Search
  payout pixels ever transcribed** (`result-screens-2026-10-05.md` R1–R3).
- Co-op Exploration Reward: 3 stars, `510/510`, rank 210, **21000** rupees (R4).

**Negative:** first-clear gold, first-clear user EXP, per-win hunter EXP, the
three star-condition definitions, replay payout split, per-stage fuel cost, and
chest amounts are all UNSUPPORTED (`C1`–`C4`, `C6`–`C8`, `C10`, `C14`;
`rewards-economy-2026-10-05.md` §D lists all 14 unknowns).

### 1.6 Arena / Fight Club

**Recovered (native parser surface):**
- Season/weekly cadence literals **with consumers**: `season_no`, `weekly_no`,
  `start_datetime`, `end_datetime`, `next_datetime`, `weekly_start_datetime`,
  `weekly_end_datetime`, `weekly_next_datetime` in `ParseSeason` (8/8 resolved),
  plus 13/13 in `ParseUser` including `league_level`, `rating_point`,
  `league_win`, `win`, `lose`, `refresh_datetime`
  (`sunday-settlement-2026-10-05.md` §1.1).
- Community economy tables, transcribed and cross-checked: tier rewards
  Silver/Gold 100+2, Emerald/Metron 150+2, Mandarin 200+2; scoring
  +15/−8/−5~6/−8; a 31-band rank table to 30000+; tier-up = 6 wins regardless of
  losses; settlement + reset every Sunday (`fc-economy-2026-10-05.md` §1;
  tables transcribed from `namu-tables-2026-10-05.md` §4–§5).
- Cross-source verdicts: tier table consistent **single-sourced**; scoring
  deltas consistent **two-source**; rank table consistent single-sourced with
  one anomaly; settlement cadence agrees (`fc-economy-2026-10-05.md` §1.4).

**Negative and important:** `fc-native-2026-10-05.md` §1.10 cross-check gives **zero
value-level agreements and nine documented gaps**. Native parsers prove *where*
Fight Club economy values would land; the tables supply candidate values under
different names with no recovered key mapping (`fc-native-2026-10-05.md` §1.10).
Specifically: `refresh_price{price_type,price}` has no table vocabulary at all
(§1.2); the `6` in `max_win 6` vs 6-win tier-up is a **numeric coincidence, not
corroboration** and was explicitly refused (§1.6); `GetMyRank`'s scalar `rank`
is a different thing from a rank-band reward (§1.8). All replica arena values
(BP 1, rating ±10, honor +10, six wins/league, rank 1, refresh 100/type 2,
all-zero reward rows) remain local fixtures (`H1`–`H8`, all UNSUPPORTED).
- The rank table contains a **preserved anomaly**: band 551-720 pays
  `?? ?? 255` where the sequence implies 225/250. Keep `255`; never smooth it
  (`fc-economy-2026-10-05.md` §2.2).
- Bronze tier entry value: never recorded in the source, and is **not** zero.

### 1.7 Episode

**Recovered (original shipped data, `[ORIGDATA]`):**
- 18 chapters / 128 stories / 147 unique IDs for season S01 from `R_EPISODE.jet`
  (`fixture-conflict-audit-2026-10-05.md` D1 row context; AGENTS §91).
- Original chapter reward declarations for all of them. Supported settlements:
  **E01 GC2 × 3** (D1 CORROBORATED), **E02 FMD1 × 30** (D3), **E05 AIRSHIP_TICKET
  × 20** (D5), **E18 RP1 × 100000** (D7). Unimplemented-but-known: E03/E04/E06–E17
  with GC3/GC4, GC8, OV1, CERUM01/02/03, SK13/23/33/43, EM02, LCOIN, GC9/10/11
  (D9, X11).
- Read/clear wire encoding: `r_<id>` for Read, bare `<id>` for Clear, same route,
  and `GetLog.read_log` must retain **both** (`D10` CORROBORATED; native
  `b19638` / `b19710`).
- EV05's declared schedule is expired 2020/2021 and is not reopened (D11).

**Recovered (native mechanism, not amounts):** `RP1` is the gold **display
identity** and `FMD1` the free-Manda **display identity**, both synthesised by
`ParseLoginBonusRef`; generic `Inventory.AddItem` does **not** credit gold
(D8 row; AGENTS §122–123). The mapping of each declaration onto
`user.gold.{prev,cur}` / `user.free_iap.{prev,cur}` is **explicit replica policy**,
recorded as UNSUPPORTED-for-original, not as recovery.

**Negative:** 15 of 18 chapters refuse redemption; the E01 coupon redemption path
exists natively but pool/tier/odds are unknown (D2, X12). E05's all-leaf gate is
**locally stricter** than native parent-aggregation (D6, UNCONTRADICTED).

### 1.8 Fishing

**Recovered (this system's lane in this folder is thin — most fishing work is in
AGENTS §119–§121, outside this folder):**
- Shipped `LEVELING` `FISHING` configuration exists with `common1` placement and
  CHIR timing fields; `FS001`..`FS011` are **sprite families, not proved API fish
  ids** (AGENTS §119).
- Failed/cancelled catch consumes bait after a bite; bait withdrawable beforehand
  (final `HELP_DATA10_8`, AGENTS §119).

**Negative:** fish identities, pools, prices, catch settlement are all
unrecovered; `ParseBegin`'s cached `COMMON_INFO`/`FISH_INFO` copy resolves the
object-kind question but requires `common1` to actually be loaded at runtime
(AGENTS §120–121). Nothing in this folder adds a fishing numeral.

### 1.9 Hunter Search / Abyss / traces

**Recovered:**
- `collect_qty` is a **per-hunter** threshold **graded by the hunter's star**, and
  natively it is a per-item field copied into `CardInfo+0x4c` with the consumer
  computing `max hunters = floor(owned / collect_qty)`
  (`trace-threshold-2026-10-05.md` §1.1–1.2; `E9` CORROBORATED).
- The item row schema carries **both** a `rank` and a `collect_qty` — exactly the
  layout a per-grade ladder needs (same §1.2; schema fact, not proof).
- Shipped 2.8.0.1 help **describes the system per-hunter and grade-graded with
  no numeral** (same §1.3).
- The official EN guide states the tiers are explicitly ★2/★3 (§1.4), and four
  official 2018 ★3 trace anchors exist: sold 15/box and 95/125 per box with
  jackpot 40; **granted 10 per 10+1** in two independent events; **granted 40** as
  a weekly first-purchase bonus (§1.5).
- Search result pixels R1–R3 above; capsule identity `AIRSHIP_TICKET` (`E1`
  CORROBORATED, native + tutorial 66).

**Negative:** `collect_qty` appears **0 times** across
`analysis/recovered-data/**` and `analysis/extracted/**`; the help gives no count;
the native reference key index scan found no separately named item/trace
reference database (`trace-threshold-2026-10-05.md` §1.8). The original numeral
is unrecovered.

**Also recovered (shipped 2.8.0.1 prose, NEW-5):** `CONTENTS12_1..12_6` documents
Hunter Search, Helium Capsules, events, dispatch and limits — first-party prose
with **zero** quantities (`help-2_8-sweep-2026-10-05.md` §2.8 NEW-5).

### 1.10 Monsters

**Recovered:**
- The Episode-only actor STAT table exists and is fully inventoried: 152 entries,
  151 identifiable rows, 34 monster `res_id` rows over 22 distinct tokens, plus 3
  monster-placed `C010` rows = 37 monster-like rows
  (`episode-stat-adjudication-2026-10-05.md` §2; `m034-variance-2026-10-05.md`
  header re-derivation).
  **[CORRECTED 2026-10-06: "fully inventoried" was wrong — 37 is an INCOMPLETE
  monster partition. Five further `C*`-namespace rows are also `type: "monster"`:
  `CB1102_006/_008/_011/_018/_019` (`C006`, `C008`, `C011`, `C018`, `C019`, all
  right side of `CB1102`, thumb L1/r5/hyper2). Exhaustive: `34 M* + 8 monster-typed
  C* = 42 monster-like rows`, and `109` hunter-typed `C*` hero rows (vs the 117
  `C*`-namespace rows). The 22 distinct `res` tokens, the 6 multi-tuple identities
  and the 160x `M034` spread are unaffected — they draw only on `M*` rows.]**
- **These rows are per-appearance scripted tuning, not base stats.** Six `res`
  identities carry two or more disagreeing tuples; `M034` spans HP 100→16000
  (**160×**) across four rows; identical thumb level does not predict STAT
  (M062 L1 hits harder than L20); and identical thumb context yields different
  STAT (same §1.1).
- Cleanest proof of the thumb being display context: `CB1401` reuses actor ids
  defined for `CB1201` (M041/M042) and re-thumbnails them from L10 to L15, while
  the STAT table holds one row per actor id (`m001-m100-insider-2026-10-05.md` §1.3).
- Cross-record actor reuse: three instances plus one mixed wave
  (`m034-variance-2026-10-05.md` §1.5).
- `CB0002_M01` is the **only zero-placement row in the whole table** — proved two
  ways, including a byte-level grep finding the id in exactly one file
  (`episode-res-crosswalk-2026-10-05.md` §1.8; `m034-variance-2026-10-05.md` §1.2).

**Negative (identity, and this is the decisive one):**
- The `M*` Episode `res` token is an **opaque per-appearance script token.** The
  `<res>.jet` filename convention holds **64/64** for the `C*` hunter-card
  namespace and only **2/22** for `M*` — and the two survivors (`M001`, `M100`)
  are precisely the two whose own catalogue rows are documented identity UNKNOWNs
  (`episode-res-crosswalk-2026-10-05.md` §1.3 and §1.6).
- `ref_id` is a **hunter-card namespace** (120/120 to cards, 0 to monsters) and
  cannot bind an `M*` token (§1.4).
- Only **2 of 22** catalog monsters have any Episode row, and 20 of the 22 catalog
  IDs (`M002`..`M021` except none) appear nowhere at all
  (`episode-stat-adjudication-2026-10-05.md` §1.4).
- No video ties any fixed value to an observed full HP bar. The P J contact sheets
  yield three *candidate* depletion runs, and 15-second sampling cannot prove no
  wave change between frames (`monster-fullhp-2026-10-05.md` §2). Stage-data
  `M`-ID mapping is a **negative** (same §3).
- MON BLAST! Monster Info cards (Snowfox 17,370/790; Pandahawk 17,460/1,110;
  Moonwoof 18,080/850, all Gold Card Lv.10 MAX) are a **different app**
  (`com.vshower.prd_pf`) with **no entity or scale crosswalk** — held at 0 credit in
  `cross-title-mon-blast.md` and quarantined in every lane that touched it.

### 1.11 Heroes / identity resolution

**Recovered (identity, not stats):**
- The 2019 `blustone.jp` archive yields **62 numeric 13-field profiles
  crosswalked to 62 unique catalog IDs** (`archived-hunter-database-2019.md`
  + `.tsv`), with the remaining 51 enumerated in `uncovered-archive-roster-2019.tsv`.
- **The archive is now a proven closed set.** Re-fetching the Oct index, the Dec
  index, and alternate 2019 windows produced **0 new rows**; the ★5/awakened index
  section renders with an **empty table** — no ★5 or awakened profile page was
  ever linked (`archive-jp-fill-2026-10-05.md` "Result up front" and §1).
- A second per-hero numeric source exists and was missed by the adjudication file:
  `analysis/recovered-reference/EPISODE_STAT_ACTORS.json` holds **117 hunter rows
  across 55 distinct heroes** (`ref_id` + `stat.hp/atk/def`)
  (`hero-stat-divergence-2026-10-05.md` "Correction to one premise").
  **[FILTER PRECISION 2026-10-06: 117/55 is the `res_id`-namespace count, not the
  `hunter` count; 8 of those 117 rows are `type: "monster"` placements, so the strict
  figure is `109 rows / 54 distinct heroes`. Both counts are "hero" rows in the
  identity sense — no coverage difference.]**
- Combined identity reach rises from 62 to **73 of 113**, with 11 heroes existing
  **only** in the Episode source; **40 heroes are in neither** (same §3a).
- The crosswalk is validated by shipped native enums, not name matching:
  **role 99/100 agreement** (sole mismatch `005`/`CB0102_005_1`) and **element
  94/100** (all six mismatches on variant packs or sentinel rows) (same §3a).
- Roster existence bounds: the Dec-2017 roster was catalog IDs `001`-`031`, proved
  by two stamped Sept-2017 CDN manifests plus the exact complement bundled in the
  held 1.4.4.1 APK (`roster-2017-2026-10-05.md`); and `roster-gaps-2026-10-05.md`
  supplies in-window dated records for `036` Bear (official "newly-added",
  2017-11-08), `038` Rebecca/"Santa Girl" (official debut, 2017-11-30) and `034`
  "Halloween Witch" (community, secondary), plus a **named existence date for
  `051` Beckhen**.

**Recovered (divergence priors, explicitly priors and not values):**
- P1 (strongest): role archetype sets the ATK/DEF **split** (disjoint ratio bands,
  Bomber 1.38–1.75, Defender 0.66–0.92) while HP is banded by rarity on a 20-step
  ladder. P2: rarity is the primary magnitude axis (pooled medians HP 1502/1624/
  1750/1955 for ★1–★4). P4: element is **not** a divergence axis for the core three.
  P7: monster divergence is **per-encounter**, not per-monster
  (`hero-stat-divergence-2026-10-05.md` §2 P1–P10).
- A checkable corroboration already exists: the replica's `recruitBirthRanks`
  agrees with the archive's `rarity_on_draw` for all five of `002`–`006`, while
  `001` is published at rank 1 locally against ★3 in the archive (same P2).

**Recovered from the audit of the fixture itself (all verified by re-reading
`server-ts/src/bootstrap.ts` this session):**
- Every non-`001` reference copies card `001`'s stat row **verbatim**, so **all six
  published heroes share one base stat line** (`bootstrap.ts:201`; `I5`).
- `ordinaryRankStats` applies **no** per-rank scaling — it stamps `[1..5].map(...)`
  (`I5` context in `hero-stat-divergence-2026-10-05.md` "Structural-fixture
  premise").
- Every published monster is one row `hp 100 / atk 10 / def 5`, level 1, rank 1,
  `hp_page 100` (`I2`, `I3`), so monster difficulty is a constant and per-area
  escalation does not exist locally.
- Every stage publishes `enemy_atk_per 100 / enemy_hp_per 100`, so **per-stage
  enemy scaling does not exist locally** (same premise table; `I1` confirms 100
  means 100 %, proven by the HP/damage paths).
- Team EXP is a **two-row** threshold table `0 / 100`, hard-capping Team level at 2
  (same premise table; called out in `fixture-conflict-audit-2026-10-05.md` §2.5
  as "the least visible and most structurally limiting fixture in the economy").

**Negative:** `attr_resist: 99` on 10 Episode rows is an apparent **sentinel**, not
a resistance value, and those rows' element cannot be trusted yet
(`hero-stat-divergence-2026-10-05.md` §3a "Still open"). `INDEX.md` §5.2
classifies `bonus.rank_1..rank_5` as **monster**-rank with no native proof either
way (same §3c).

### 1.12 Weekday scheduling

**Recovered (shipped UI strings, verbatim, from `all-tables.json`):**
- Sunday-12-AM snapshot → Monday-6-AM ranking-reward payout, 10 rows across 5
  locales (`weekday-ui-2026-10-05.md` §1.1).
- Wednesday Fight Club **ranking announcement** (`TIP_4`) and Wednesday Guild Blitz
  **registration** (`TIP_8`) — both Wednesday, two different systems
  (`weekday-ui-2026-10-05.md` §1.2–1.3).
- Saturday 24:00 Dismount Pass recharge, 5 rows (`weekday-ui-2026-10-05.md` §1.4).
- A weekday census across all 13 recovered tables (same §1.5).

**Negative:** no native literal, no `GetWeekday`/`tm_wday`/modulo-7 consumer, and
no binding between any of these texts and `weekly_end_datetime` /
`is_weekly_reward` was recovered (`sunday-settlement-2026-10-05.md` §1.3 verdict
table; `weekday-ui-2026-10-05.md` §2.2). Weekday words live only in a string
table / libc / curl block and are **unbound**. Saturday falsifies any single
"everything resets Sunday" model; three distinct systems need three rules
(same §2.2). `TIP_3` says "every week" with **no day** and cannot arbitrate.

### 1.13 Native parsers recovered (structure only — no values)

Consolidated here because this is the most reusable output of the session.

| System | What is recovered | File |
|---|---|---|
| `/gem/LevelUp` | 7 request form keys incl. `inst_id` and constant `max_tries=7`; precondition gate, busy flag, wallet toast | `gem-popup-bindings-2026-10-05.md` §1.6 |
| Gem price references | 3 routes → callbacks → parsers; 6-field polish row; sibling row shapes; honest empty reply is `{result_code:1,ret_data:[]}` | `gem-polish-parsers-2026-10-05.md` §1.1–1.7 |
| Gem popup display | full `CSRPopUpGemLevelUp` vtable; complete call-site census incl. negatives (two uncalled functions, one `.got` bind target) | `gem-popup-bindings-2026-10-05.md` §1.1–1.2 |
| `/gym/RankUpBundle` | requester/callback/sink; 5 uint request, `void(int)` sink, **no PARAM struct** | `batch-rankup-chucoin-2026-10-05.md` §1.1 |
| `ReqGroupRankUpCB` / `ParseSellCard` | response shape; `inst_id_list`; batch key family `card.removed_inst_id_list` + `card.target_list[]` | `grouprankup-sellcard-bodies-2026-10-05.md` §1.1–1.4 |
| Arena season | 8/8 `ParseSeason` + 13/13 `ParseUser` literals with consumers | `sunday-settlement-2026-10-05.md` §1.1 |
| Arena economy landing zones | 9 gaps, 0 value-level agreements | `fc-native-2026-10-05.md` §1.10 |
| Trace exchange | `collect_qty` per-hunter, star-graded; `floor(owned/collect_qty)` max | `trace-threshold-2026-10-05.md` §1.1 |

Method caveat that belongs with every row above: `gem-popup-bindings-2026-10-05.md`
§3 item 5 records that **the literal resolver returned 0 literals across every
function on its first two runs, which was false.** Both the false zero and the
later all-pass are preserved there deliberately.

---

## 2. Live contradictions still open

Each entry gives both sides and the file that holds it. None of these is resolved.

**C-1 · Skill level-25 material cost.** `[EN-2017]`: 4 bronze + 1 silver.
`[NAMU]`: 5 bronze + 2 silver. Both agree fragments at level 25 (3). Held as
**OPEN-1 / X5**, "mild lean `[NAMU]`".
→ `transcendence-skill-cost-2026-10-05.md` §2.9 C1; `help-2_8-sweep-2026-10-05.md`
§2.8 C1 ("still OPEN-1; swept and empty"); `fixture-conflict-audit-2026-10-05.md`
§2.6 X5.

**C-2 · Band-10 top level.** `[EN-2017]` covers `45-49`, leaving level 50 uncovered;
`[NAMU]` covers `45-50`. The replica publishes 50 rows.
→ `transcendence-skill-cost-2026-10-05.md` §2.9 C2, §2.4 "Correction: there is no
geometric rule to lean on"; `fixture-conflict-audit-2026-10-05.md` X6.

**C-3 · Base-hunter step gate (T2/T3).** `[EN-2017]` alone publishes T1 ≥★3,
T2 ≥★4, T3 ≥★5. Both help versions publish only a ★3 floor, so the help
**never grew** a 4★/5★ step gate — a two-version negative.
→ `transcendence-skill-cost-2026-10-05.md` §2.9 C4; `help-2_8-sweep-2026-10-05.md`
§2.8 C4.

**C-4 · Skill-slot unlock granularity.** Three sources each state a different
granularity (one slot per grade / "additional skills from ★4 and above" /
complementary). Not reconcilable into one rule; all three permit ≥2 skills at ★5.
→ `transcendence-skill-cost-2026-10-05.md` §2.9 C6.

**C-5 · Grade-row key meaning.** 9 cells agree numerically; the *label*
("Natural 1/2/3-star" vs `1★/2★/3★/4★`) is single-sourced.
→ `transcendence-skill-cost-2026-10-05.md` §2.9 C7.

**C-6 · Role material at 5★.** Not published by `[EN-2017]`, and `[NAMU]` has
**no 5★ row** — a gap in both.
→ `transcendence-skill-cost-2026-10-05.md` §2.9 C8.

**C-7 · Trace threshold value (E8/X3).** Local 10 / 20 vs `[NAMU]` 20 / 40. The
**dichotomy this was filed under is false**: `collect_qty` is per-hunter and
star-graded, so both are the same quantity on the same axis and can differ only
in value. The lane's verdict: the factor-2 claim is **NOT UPHELD as a demonstrated
error**; it is an exponent-convention offset against one self-contradicting
ERA-UNRESOLVED source, and the only external anchors fit the **local** ladder.
Recommended: soften the audit row to "shape corroborated, absolute value
unrecovered".
→ `trace-threshold-2026-10-05.md` §2.6 and the "Answer in one line" header;
`fixture-conflict-audit-2026-10-05.md` §2.3 and X3. **Note the register is
inconsistent**: the audit still carries E8 as CONTRADICTED and X3 as
`OPEN (contradiction)`.

**C-8 · Super Block jewel bonus.** 1.4.4.1 KO = 9%, EN/JP/ZH/ZT = 5%; 2.8.0.1
SC = 9% while its other locales stay 5% — the shipped client disagrees with
itself. `1.72` and `30` never changed.
→ `jewel-help-locales-2026-10-05.md` §1.4, §2.2, §2.5, §2.8; `coverage.md`
"Historical in-game help set-bonus table" row.

**C-9 · `CONTENTS12_3` grade vs level.** EN says the higher **Hunter Level** being
searched uses more capsules; KO says higher **grade**; JA says higher **rank**.
This is a **genuine semantic divergence**, not phrasing — and the corpus is
hand-maintained per locale, so **do not resolve by preferring English**.
→ `help-2_8-sweep-2026-10-05.md` §2.7.

**C-10 · Transcendence 2★ T3 cell.** `[EN-2017]` fills it with 60/600;
single-sourced, and no arithmetic rule predicts it. Namu's own header declares
three steps, favouring transcription omission.
→ `transcendence-skill-cost-2026-10-05.md` finding 2 and §2.2.

**C-11 · Episode E05 gate strictness.** Native checks the **parent story's**
clear; the replica requires **all 8 descendant stories**. Recorded as
UNCONTRADICTED and explicitly "locally stricter".
→ `fixture-conflict-audit-2026-10-05.md` D6.

**C-12 · Gacha affordability debit order.** Native affordability is the
**summed** wallet; consumption order is UNKNOWN. The replica uses free-first.
→ `fixture-conflict-audit-2026-10-05.md` F8 (UNCONTRADICTED); AGENTS §26 records
free-first as an explicit *local* policy with original priority missing.

**C-13 · Episode `EVCB*` scale hypothesis.** An EVCB ≈ 1.36 × archive shape was
measured (CV 13.7% on 23 heroes). The file's own instruction is explicit:
**test it, do not install it.**
→ `hero-stat-divergence-2026-10-05.md` §3b item 2 and P6.

**C-14 · Rank-up EXP-reset policy.** The preview path `SetPromotion(L)` resets
level→1 + rank→1 **in a cloned analyzer**; the persisted EXP-reset transition is
`[INFERRED]`, and no captured partial or full server response exists.
→ `training-rankup-rules-2026-10-05.md` rule 5 ("MECHANISM PARTIAL");
`fixture-conflict-audit-2026-10-05.md` B10.

**C-15 · Skill-level rank gate on newly promoted hunters.** Promotion preserves
trained skills with no auto-unlock; a new skill is supposed to be learned on
rank-up per guide, but native `SetRank` does **not** call `SetSkillLV` and
`ReqRankUpCB` parses no skill levels.
→ `training-rankup-rules-2026-10-05.md` rule 6 ("PARTIAL");
`fixture-conflict-audit-2026-10-05.md` B11 (UNCONTRADICTED).

---

## 3. Every retraction and correction issued during the session

Recorded so a future agent does not re-derive a falsified claim. Each entry names
what was retracted and the file that holds the retraction.

**R-1 · "`res` → art mapping is by filename convention" is FALSE.**
Originally asserted in `episode-stat-adjudication-2026-10-05.md` §3 (line 270)
and `m001-m100-insider-2026-10-05.md` §2.5 item 4. Retracted first for `M034` in
`m034-variance-2026-10-05.md` §3.3 item 1, then **completed** across all 22 tokens
in `episode-res-crosswalk-2026-10-05.md` §3.1. Measured reality: **64/64** for the
`C*` namespace, **2/22** for `M*`. The two survivors are exactly the two whose own
catalogue rows are documented identity UNKNOWNs, which is what made the rule look
general. Replacement statement is quoted verbatim in §3.1.

**R-2 · Four self-corrections inside `episode-res-crosswalk-2026-10-05.md`** (§3.1b):
local art inventory is **570** `C*` packs, not 520; **7** tokens have >1 row, not
8; **5 of 7** multi-row tokens disagree on rank, not "several"; max distinct thumb
contexts for one token is **3**, and the busiest context is shared by only **2**
tokens with `(20,5,2,1)` held by `M035` alone. Recorded as an explicit
self-retraction so a reader who already read the draft does not re-import them.

**R-3 · Eight corrections inside `m034-variance-2026-10-05.md`** (§3.3): no
`M034.jet` exists; `CB1501` **does** have a populated hunter actor (right wave,
slot 5) contrary to the earlier draft; `CB1501`'s right wave has **5** slots, not
4; `cool_time 99000` is shared by **4** rows, not only the M001 tutorial row;
nonzero `attr_enhance`/`attr_resist` on **2** of 18 rows, not 1; `EVCB0102_M2` has
**2** placements, not 3; **61** combat records (47 `CB` + 14 `EVCB`), 62 only if the
manifest is counted; `EVCB0301`'s title is `EV03_E01_TITLE`, not `EV01`.

**R-4 · P J video HUD token.** The earlier transcription `2,031` was a misread;
rechecking the saved frame supports **`2,551`** at ~01:15, with `1,253` also
visible at ~01:30.
→ `monster-hud-2026-10-05.md` §1 (RE-TRANSCRIBED);
`monster-hud-observations.md`; `README.md` P J row.

**R-5 · `price_type` as a `/gem/LevelUp` request field — RETRACTED, positively
falsified.** `price_type` does not appear as a form field (exhaustive literal
list) and `FindGemLevelUpPrice(int, PRICE_TYPE)` is **not called** on this path.
Do not build a `price_type`-keyed schema.
→ `gem-popup-bindings-2026-10-05.md` §3 item 1 and §1.6;
`gem-levelup-action-2026-10-05.md` §1.2 (the "one scalar is price_type" framing
is **withdrawn**).

**R-6 · `UpgradeEvent` "is a display binding helper" — RETRACTED.** It is
**uncalled dead code** whose body is the compiler-emitted twin of the loop inlined
in `UpgradeCB`; it contains no UI call and no string.
→ `gem-popup-bindings-2026-10-05.md` §3 item 3; the call-site table in §1.2 shows
`UpgradeEvent` with **NONE**, not in vtable, no pointer reference.

**R-7 · "Popup request `uint64` is the target gem `inst_id`" — REFINED, not
confirmed.** The value is indeed `inst_id`, but the same value also flows into the
popup's own `[this+0x6bc]`, and the `uint64` in
`RequestGemLevelUp(uint64, uint, cb)` is r2 as a 32-bit value; its 64-bit width is
not independently exercised.
→ `gem-popup-bindings-2026-10-05.md` §3 item 2.

**R-8 · "Untraced call sites for `StatusUpdate` / `SetUpgradeComment` /
`SetBaseInfo`" — CLOSED** with exact sites; and `SetState` is *also* uncalled,
which had not been stated.
→ `gem-popup-bindings-2026-10-05.md` §3 item 4.

**R-9 · Methodological false negative, recorded deliberately.** The first two
literal-resolver runs reported **0 literals across every function**, which was
false. Both the false zero and the later all-pass are preserved.
→ `gem-popup-bindings-2026-10-05.md` §3 item 5.

**R-10 · `/gem/LevelUp` request keys: "NOT recovered / no literal block exists" —
superseded to RECOVERED.** Seven keys recovered; the **response** remains
unrecovered.
→ `gem-levelup-action-2026-10-05.md` §1.3 first bullet;
`gem-popup-bindings-2026-10-05.md` §1.6.

**R-11 · `ReqGroupRankUpCB` callback sink type was WRONG.** It is `void(int)`, not
`void(int,int,int)` — the demangled `IFviE` reads as `void(int)` whereas the
wrong form would be `IFviiE`; exactly one int is materialised at the invoke site
and it is the result code. The structural conclusion (no PARAM struct) survives.
**The same correction applies to `analysis/systems/gym.md:97`.**
→ `batch-rankup-chucoin-2026-10-05.md` §1.1 note.

**R-12 · `src_rank` for `/gym/RankUpBundle`: "candidate" superseded to
[RECOVERED]** as an adjacency-free field.
→ `batch-rankup-chucoin-2026-10-05.md` §1.1 note 3.

**R-13 · Chu-coin / Secret Market is a NATIVE NEGATIVE.** Both bodies audited:
no `coin` / `chu` / `secret` / `market` key anywhere; no `prev` key; no
`removed_card` / `target_inst` / `skill_%u_level` / `card_list` / `item_list` /
`detection` key on either path.
→ `batch-rankup-chucoin-2026-10-05.md` §1.2;
`grouprankup-sellcard-bodies-2026-10-05.md` §1.6.

**R-14 · The `[HELP-1.4.4.1] CONTENTS6_1` "Metron Crystals **and skill
materials**" citation is true of 1.4.4.1 and FALSE of shipped 2.8.0.1.** In 2.8.0.1
`CONTENTS6_1` names only "Metron Crystal"; the skill half moved to `CONTENTS6_4`
as "skill training items"; the phrase "skill material" now occurs in **zero**
2.8.0.1 records. The *system* identity survives across two records; the
single-sentence proof does not.
→ `help-2_8-sweep-2026-10-05.md` §2.5(a), register NEW-1;
`transcendence-skill-cost-2026-10-05.md` §2.12 is the citation that must be
requoted or retracted; `fixture-conflict-audit-2026-10-05.md` A4 carries the
correction inline.

**R-15 · Abyss "up to 3 resets depending on Veteran rank" is 1.4.4.1-ONLY.**
2.8.0.1 publishes **no reset count and no Veteran cap anywhere** in the Abyss
block; it replaces the mechanism with daily-entry regulation plus Manda-bought
extra entries. Therefore the replica's empty Abyss reset price is **no longer a
first-party-proven gap for the shipped client**, and no reset quantity is
recoverable in **either** era. Register X8 was re-scoped from OPEN to
HISTORICAL.
→ `help-2_8-sweep-2026-10-05.md` §2.5(a) and NEW-2;
`fixture-conflict-audit-2026-10-05.md` E7, X8, §2.7.

**R-16 · Mirage Ruins `CONTENTS9_8`: "string deleted" is retracted.** The rule
text **survives** in KO/JA/SC/TC; only the **English copy** is absent from the
`desc1` map.
→ `help-2_8-sweep-2026-10-05.md` §2.5(b), NEW-3.

**R-17 · JSON-decoding correction.** `jewel-help-locales-2026-10-05.md` §0.4 said
the 2.8.0.1 help body needed `raw_decode` per-string. That is true of the
**1.4.4.1** corpus (surplus `}` before the final `]`); the **2.8.0.1** body parses
cleanly with a single `json.loads` into 205 records.
→ `help-2_8-sweep-2026-10-05.md` §0.1.

**R-18 · Gacha boost multipliers are a scope difference, not a contradiction.**
400% scoped to *limited* ★3, 200% to *all* ★3, and they appear **in the same
October body**; Halloween adds a 500% limited scope.
→ `event-board-bodies2-2026-10-05.md` §2.7.

**R-19 · Oct-2017 gacha boost contradiction retired.** As above; the September vs
October 200%/400% disagreement flagged in `event-board-bodies-2026-10-05.md` §2.2
is superseded by the third datapoint.

**R-20 · `148274` was mis-attributed.** It was cited as a `[Review]` post; it is
actually titled "My guess" and **is** archived. The 15 real `[Review]` ids are all
in `142946`–`147073` and none is archived. The prior range's upper endpoint was
just the last row on the list page.
→ `review-posts-2026-10-05.md` §2.1 and headline finding 2.

**R-21 · The "16 images" reading of the guide post is wrong — there are exactly
11.** The five `Screenshot_2017-11-11-*.png` names and `Arena.png` / `Fight
Club.png` / `Ruins.png` / `Training Gym.png` / `Cruise_beginning.png` /
`Cruising.png` are the **`alt` attributes of the 11 attachments** — the
originals' own upload filenames — not extra "in-image filenames".
→ `share-en-guide-2026-10-05.md` headline finding 2; corrects
`review-posts-2026-10-05.md` §1.6.

**R-22 · Board attachments are board-shared namespaces.** The premise that
`event_en` attachment URLs were the only namespace did not hold; the comment-image
namespace is the other half and is also empty of stat panels.
→ `board-attachments-2026-10-05.md` §2.1–2.3.

**R-23 · The `event_en` board is a FORUM board, not the game's event list.** The
official notice says the section "was made for forum events apart from in-game
events" and exists so players can share screenshots. The five "sticky" rows are
sticky because they are current **forum** events. Posts are marketing-grade text:
reliable for *what was advertised*, never for a complete event schema or a
probability table.
→ `event-board-bodies2-2026-10-05.md` §2.6.

**R-24 · Permalink form is not a reliable Wayback fallback** for this board — it
is **302-only**; the `index.php?mid=…&document_srl=…&l=en` form is the one that
carries bodies.
→ `event-board-bodies2-2026-10-05.md` §2.4.

**R-25 · Dec-2017 roster was `001`-`031`, not "27 asset-proved IDs".** Line B
closes the gap for `001` / `003` / `009` / `010` as the exact complement of the
Sept-2017 CDN set, proved APK-bundled instead. The file explicitly
"supersedes nothing else" and states the `031` upper bound is an **inference**
from three independent lines, not a primary record.
→ `roster-2017-2026-10-05.md` header.

**R-26 · `001`-`031` is the Sept-2017 art-proved FLOOR, not the Dec-2017 roster.**
CDN manifests are silent about the Oct–Dec window and cannot support an upper
bound across a period they do not cover.
→ `roster-gaps-2026-10-05.md` "The correction this forces".

**R-27 · The task brief's premise was incomplete.** It stated the 37 scripted
monster rows are the only local source pairing an enemy identity with
HP+ATK+DEF. True for monsters, but the **same file** also pairs a **hero**
identity with HP/ATK/DEF — 117 rows across 55 heroes. Raised identity reach from
62 to 73 of 113.
→ `hero-stat-divergence-2026-10-05.md` "Correction to one premise in the task
brief".

**R-28 · `apk-diff-2026-10-05.md` §4 required two corrections** on the jewel-help
history, both verified from disk: the version-span reading and the SC 9% /
other-locales 5% split. Corrected expansions are in `jewel-help-locales-2026-10-05.md`
§1.6; mirrored in `polluted-observations.md`.
→ `jewel-help-locales-2026-10-05.md` §1.6;
`polluted-observations.md` "Two corrections to `apk-diff-2026-10-05.md` §4".

**R-29 · Namu metron-fragment row "band pairing is unresolved" is superseded.**
→ `transcendence-skill-cost-2026-10-05.md` §2.13 (proposed, not yet applied to
the source files).

**R-30 · Attribute/level misreads retired.** `시계초` is a **passionflower common
noun** and the ~00:52 panel reading is near-certain a low-resolution misread;
**retire `시계초` as a search token.**
→ `video-loose-ends-2026-10-05.md` §4; `bahamut-thumb-2026-10-05.md` tail.

**R-31 · Two encoding incidents, both detected and fully repaired.** A PowerShell
5.1 round-trip double-encoded 112 em-dashes; a `Set-Content` pass flipped CRLF.
Separately, console rendering was twice mistaken for CJK corruption when the file
was fine.
→ `GUARD-encoding-and-archive-traps.md` Rules 1–3. **Any future agent editing a
non-ASCII file in this folder must use Python or the edit/write tools, never
PowerShell 5.1 `Set-Content`.**

**R-32 · Rank-up preview badges.** Both advancement-preview destination badges are
**FOUR** stars; the left is faded, not 3-star. No RankUp mutation was implemented
from the earlier misread.
→ AGENTS §29; carried in `training-rankup-rules-2026-10-05.md` §2c and
`fixture-conflict-audit-2026-10-05.md` B8 context.

---

## 4. Confirmed fixture contradictions, and what was deliberately not acted on

### 4.1 Actively CONTRADICTED fixture rows (from `fixture-conflict-audit-2026-10-05.md` §2.1)

The audit's own tally is **4 CONTRADICTED** rows, and they cluster in exactly one
system plus one trace constant.

| Row | Fixture | Contradicting evidence | Severity |
|---|---|---|---|
| **A1** | Skill gold `100 × (index+1)`, L1=100 … L50=5000 | `[EN-2017]` banded: L1–4=100 … L45–49=1000. Agree at **L1 only**; top band ~5× cheaper | **Soft.** Contradicts the local *formula*, not the local *row density* — a dense vector with band-constant gold satisfies native indexing **and** the community table. Residual risk: `[EN-2017]` band 10 leaves level 50 uncovered |
| **A3** | Skill materials `source_1..4_qty: 0` in every row | `[EN-2017]` and `[NAMU]` agree **cell for cell** (30/30) that role material is required **from level 5**: `0/0/0, 1/0/0, 2/0/0, 3/0/0, 4/1/0, 5/2/0, 0/3/1, 0/4/2, 0/5/3, 0/6/4` | **Highest.** The cleanest conflict in the audit. Three separable reasons: two independent sources on one ladder; the conflict is with the local **quantity**, not a schema dodge (native popup provably skips the lookup at qty 0, so 0 is legal); and rows 1–4 are unconstrained by both sources, confining it to levels 5–50 × 4 roles = 184 rows |
| **A4** | No fragment/Metron quantity in any skill row | Both sources: decadal `1–9→1, 10–19→2, 20–29→3, 30–39→4, 40–49→5` | **Unchanged verdict, evidence class downgraded.** First-party corroboration is **1.4.4.1-ONLY and lapses** (see R-14). Rests on the two community sources |
| **E8** | Trace thresholds Sylvester 006 = 10, Gerard 005 = 20 | `[NAMU]` fixed-recruit ladder 20 / 40 (formula 2ⁿ×10) | **Soft, and its premise was retracted.** See C-7: the "per-star vs per-hunter" dichotomy is false; factor-2 claim NOT UPHELD. Blast radius: `collect_qty` is reused as the guided-Search reward quantity, so one constant feeds two systems; a doubling stays self-consistent for a *new* guided run but would not retro-fit saved state, and legacy guided receipts are retained with no backfill |

### 4.2 Conflicts deliberately NOT acted on, and why

The audit's own statement governs this section: **"no fixture was changed and none
is recommended here. Every row is a statement about evidence, not a retune
instruction."** The repository owner decides any retune. Specifically:

- **X1/X2/X5/X6 (skill training)** — flagged, not fixed. The cheapest decisive step
  is a *data* step, not a formula step: recover the network `GetLevel.skill`
  price/material rows the native getter indexes. Help sweeping is now **closed as
  a route** (§5 below).
- **X4 (RankUp 1000 gold/source)** — flagged as implausible **scale** (8–12× against
  Caragublu's unnormalisable 8000/12000 previews) but with **no per-source anchor**,
  and the preview's source count is unknown so no conversion is possible. The
  *mechanism* is already native-recovered (sum over new real sources, placeholders
  skipped).
- **X7 (`sell_price: 0` for all ranks)** — an **inert gap**: no sell or release route
  exists, so the zero cannot be observed in play.
- **X9 (batch rank-up below max level)** — GAP; the guide claims an onboarding
  shortcut the replica does not implement, and native batch-rank parsing was only
  partially done this session (R-11, R-12, R-13).
- **X10 (★3 release → Chu-coins → trainer loop)** — UNIMPLEMENTED, and now
  **native-negative** on the currency (R-13). Closing it needs a release/sell
  route plus its currency, which native evidence does not supply.
- **X11/X12 (Episode E03–E17, E01 coupon)** — unimplemented against *known* original
  declarations. Needs item reference rows for `GC*`/`FMD1`/`SK*`/`EM02`/`LCOIN`/
  `OV1`/`CERUM*` tiers. Note the deliberate refusal is the correct state: the
  project already refuses rather than fabricating a claim receipt (AGENTS §118).
- **X13 (capsule display name "Helium Capsule")** — naming risk only; the
  Helium ↔ `AIRSHIP_TICKET` crosswalk is recorded **UNPROVED**.
- **I2/I4/I5 (monster and card stat rows)** — UNSUPPORTED, not contradicted.
  Card 001's numbers are **invented by the fixture's own comment**, and
  `bootstrap.ts:201` copies that one row into 002–006, so **all six published
  heroes are a single stat line**. Continued base-stat hunting is the route, not a
  retune.
- **Team EXP two-row table** — called "the least visible and most structurally
  limiting fixture in the economy" (`fixture-conflict-audit-2026-10-05.md` §2.5);
  still a statement about evidence, not a change request.
- **DailySignIn (28 × 100 gold)** — **not contradicted, just unsupported, and
  not the same thing as original attendance.** The official event attendance is
  event-parameterised Manda (30/day × 9 days = 270 in September 2018; 20/day × 15
  days = 300 at Halloween 2018), differing from the fixture in **currency**
  (gold vs Manda), **window** (28-day vs 9/15-day) and **trigger**. The file's
  conclusion is exact: the local fixture "is not recovered data and is not
  contradicted by an original source — it simply has no official counterpart in
  this corpus" (`event-board-bodies2-2026-10-05.md` §2.2).

---

## 5. The proven-negative list — closed, do not re-attempt

Each item is a *closed* question with the file that closes it.

**On where stat tables could hide:**
1. **No embedded per-entity stat table in any APK.** Every locally available
   version was audited read-only; stat data was **server-side** (`/reference/*`).
   APKs carry art, audio, dialogue, help text, UI strings and shared battle tuning
   only. → `old-apk-2026-10-05.md` "Result: negative"; `apk-diff-2026-10-05.md`
   header (version-added content is art/audio/dialogue/help/UI/tuning).
2. **`EQUIP.jet` is texture-only.** 24 `I2` textures, zero `textResources`, no
   stat table. → `local-reaudit-2026-10-05.md` §5.
3. **`LEVELING.jet` is shared tuning only.** 21 resources / 20 textual payloads;
   contains a `power,rank,hyper,level` curve and shared role/rank/area modifiers,
   but **no per-hero, per-monster or per-item rows**. Its res-1 CSV is
   polish-**probability** tuning, never a cost table. → `local-reaudit-2026-10-05.md`
   §6; `old-apk-2026-10-05.md` §3; `gem-polish-parsers-2026-10-05.md` §1.9.
4. **The 774-package JET scan found one shared tuning CSV, no per-card or per-item
   rows.** → `local-reaudit-2026-10-05.md` §9.
5. **The phone snapshot's recovered-reference manifest holds eight locale/skill/UI
   tables and no card, item or monster table.** → `local-reaudit-2026-10-05.md` §7.
6. **Catalogue JSONs are identity/descriptive metadata and art inventory, not
   stats.** → `local-reaudit-2026-10-05.md` §8.
7. **VSFan's 220 curated images and three resource sets contain no stat panels;
   the `Hunter Stats [BROKEN IGNORE].xlsx` recount confirms rather than extends the
   ledger** (19 named rows, 67 numeric, no source/level/gear context). → `local-reaudit-2026-10-05.md` §§1–3.
8. **The five VSFan PCAPs give a protocol map only; game bodies are encrypted.**
   → `local-reaudit-2026-10-05.md` §4; `../vsfan-packet-capture-findings.md`.
9. **The 2.8.0.1 `UI_CSV.jet` ships `monsterref: []` and `stageref: []` — both
   EMPTY arrays**, i.e. native reference hooks with no shipped rows.
   → `apk-diff-2026-10-05.md` §4.
10. **`recovered-assets/` contains zero `.pcap`/`.pcapng`/`.har`/`.ndjson`/`.jsonl`
    files** (filename-only audit). → `README.md` "Local recovered-capture audit";
    `coverage.md` row.

**On help text:**
11. **No cost table exists in either help corpus.** Tested over 73 records of
    1.4.4.1 and all 95 of 2.8.0.1, 15–20 patterns, zero hits. **C1/C2/C4 cannot
    be closed by help sweeping.** → `help-2_8-sweep-2026-10-05.md` §2.1, §2.9.
12. **The four gate-bearing help records are character-identical between versions**,
    including byte-identical group-advance material counts. → same §2.4.
13. **1.4.4.1 has no pinned date**; its PRE-2019-09-05 tag is a version-numbering
    **inference**. → same §0.1 and §2.9.
14. **A help table can lag the live balance table** — proven in-client by locale
    copies disagreeing. → same §2.7, §2.9.

**On archives and sources:**
15. **The 2019 Japanese hunter archive is a closed set.** Re-fetched index and
    alternate 2019 windows: 0 new rows; the ★5/awakened section was always an
    **empty table**. → `archive-jp-fill-2026-10-05.md` "Result up front";
    corroborated by `wayback-hunter-2026-10-05.md` (exactly two 200 index captures,
    163 urlkeys, no `064`–`098` and no awakened pages) and `wayback-blog-2026-10-05.md`.
16. **The `share_en/197745` guide images are a settled archival negative** — 0 CDX
    rows under four URL forms and all status codes, origin dead (503), proven with a
    **positive control**. Do not re-attempt. → `share-en-guide-2026-10-05.md`
    headline finding 1.
17. **Every `[Review]` post and both Arena posts are definitively absent** from the
    archive under all three URL forms and every status code — upgraded from a soft
    negative. → `review-posts-2026-10-05.md` headline finding 1.
18. **The `/capa2` subpage is confirmed empty** (single capture, POST-era, no
    numeral). The highest-value open Wayback lead is closed. → `capa2-diff-2026-10-05.md`
    §1.2.
19. **The three `blustone.jp` retry bodies (crystal guide, party-formation guide,
    FC 2018 World Championship reward detail) contributed zero numerals.**
    → `guide-bodies-2026-10-05.md` §1.2 and tail.
20. **The four official `bs.visualshower.com` character-intro posts have no archived
    copy** (CDX `[]` for all queried prefixes; availability API returns empty
    `archived_snapshots`). They remain unresolved *leads*, not evidence.
    → `striker-videos-2026-10-05.md` tail.
21. **The `event_en` board yields no player screenshots.** Five attachments opened
    byte-level: two official event card art, three promotional art, zero player
    screenshots; the only numerals are playing-card indices on a forum minigame.
    Player-screenshot hunting on this board is a dead end under archive coverage.
    → `board-attachments-2026-10-05.md` headline and §2.8.
22. **The Namu image host is 503 for all assets regardless of user agent**; the
    Seore mirror file route 404s; Wayback CDX 429s. The Lapis screenshot
    `Capture+_2019-01-25-23-49-07.png` is **STILL UNRESOLVED** and no values are
    inferred. → `namu-kr-blogs-2026-10-05.md` §7; `namu-hunter-gym-gallery.md`.
23. **The Blustone Archiving Wiki (Miraheze) is a mechanics/art record, not a stat
    source** — sampled pages render skill magnitudes as `[value]` placeholders and
    have **no HP/ATK/DEF field at all**. → `post2019-roster-2026-10-05.md` source 1;
    `miraheze-gallery-2026-10-05.md` "Result up front".
24. **Official skill-video cinematics show no Train/detail background.** 61
    pixel-inspected frames across 20 videos: **not one** showed a stat panel; every
    visible numeral is a battle-HUD or cinematic token. → `deko-thumbs-2026-10-05.md`
    "Result up front"; `official-skill-frames-2026-10-05.md`.
25. **Namu wiki direct fetch is 403**; only the `d.namu.moe` / `dark.namu.moe`
    mirrors work. → `namu-kr-blogs-2026-10-05.md` §8.
26. **Bahamut desktop is 403; the mobile mirror works.** → `bahamut-remaining-2026-10-05.md`.
27. **Search-based monster base stats are exhausted.** HUD numbers are current-bar
    only; 15-second sampling cannot prove no wave change between frames; no frame
    shows a monster name or `M`-ID; stage-data `M`-ID mapping is negative; Fandom
    page 403. `README.md` "Next visual searches" already says **do not spend
    another pass on monster base stats from battle HUD frames.**
    → `monster-fullhp-2026-10-05.md` §§2–3, §5.
28. **Accessory / mounted-jewel image search is exhausted by name collision** —
    English, Korean and Japanese queries all return other games' equipment
    screens. → `jewelry-visual-search-2026-10-05.md`;
    `jewelry-visual-followup-2026-10-05.md` (GameAppCH images 17–20 timed out and
    remain **unseen** — do not claim all 20 were inspected);
    `mining-costs-2026-10-05.md` §4.
29. **No dedicated native mining-price route exists.** → `gem-polish-parsers-2026-10-05.md` §1.8.
30. **The audio/transcript surface carries no stat-bearing speech**, the dialogue
    transcripts contain **no numerals at all**, and 7 extracted MP3 clips produced
    **no accepted transcript** (two ASR model sizes return *different* text for
    identical audio — a rejection, not a reading). → `audio-transcripts-2026-10-05.md`
    §2.4 and §2.7.
31. **`attr_resist: 99` is a sentinel on 10 Episode rows**, not a resistance value;
    those rows' element is untrusted. → `hero-stat-divergence-2026-10-05.md` §3a.

---

## 5.5 Process failures that produced wrong conclusions — read before trusting any "fixed"

These are **not** stat findings. They are the ways this session's own bookkeeping
went wrong, and each one has already cost real work. Evidence:
`c4-row-census-2026-10-05.md` §5, `address-convention-2026-10-05.md` §6.1.

1. **A correction note asserting a fix is NOT evidence the fix landed.** Two
   notes in this folder claimed a defect was already fixed; in both cases the
   defect was still present in the file that named it
   (`grouprankup-sellcard-bodies-2026-10-05.md` §1.0 still printed the old
   tool's biased address; `gem-popup-bindings-2026-10-05.md` still cited the
   wrong TSV row line). **A retraction written in file A does not repair file
   B.** Before believing a "fixed" claim, grep the *target* file for the old
   value.

2. **An error copied into a second file becomes apparent corroboration.** A false
   claim ("zero `R_ARM_RELATIVE` entries in this binary") was repeated in
   `point-info-type-2026-10-05.md` §1.9 and then cited as *supporting evidence*
   in `address-convention-2026-10-05.md`. The count was right; the relocation
   **type name** was wrong. Two documents agreeing is not two sources when one
   copied the other. Both are now retracted, and the operative conclusion
   survives only because it was re-derived on independent evidence.

3. **Assert a number you actually summed.** An agent reported "1012/1012" without
   having added the counts; the true figure was 888. This is AGENTS.md §16.7
   lesson 5 restated — *a stable metric can be a fact about the measurement
   rather than the system*. It self-corrected in place with a dated note rather
   than quietly fixing the number.

4. **A guard that cannot fail is worse than no guard.** One patch script's
   `'\ufffd'` literal was silently emptied by the tool chain, so its encoding
   check fired on every string. Two encoding guards in this folder are now
   **executable** (`enc-guard.py`, `verify-address-conventions.py`) so this
   class of defect is testable rather than trusted.

5. **Corpus counts are only valid against a stated corpus state.** Lanes run
   concurrently; this folder grew 308 → 312 files mid-sweep and
   `polluted-observations.md` was being appended to by another agent at the same
   moment. **State a count with a timestamp and a verified corpus hash**, or
   state the denominator explicitly. Never edit `polluted-observations.md` from a
   lane — the parent mirrors, so lanes never write the same file twice.

6. **Read `.text`'s real bounds before scanning it.** `.text` begins at ELF
   `0x00612cc0`, not 0. A lane that treated "everything below `.rodata`" as code
   manufactured hits out of `.dynstr`/`.hash`. Every negative below in §5 that
   came from a constant sweep should be read as *scoped to real code sections*.

7. **Substring searches need a word boundary — "Mon" matches "Money".** A probe
   for monster-named UI classes reported **32** hits in `CSRPopUp*`; every one was
   `SetMoney` / `CSRPopUpNoMoney`. Same trap class as `res`/`reference`
   (§5.17). Always anchor the token, and print the matching names before
   believing a count.

8. **Assert a count you actually summed, and reconcile disagreements openly.**
   A lane reported "179 `CardBook` hits"; the true figure is **143**
   (143 occurrences across 143 lines, 115 of them mangled symbols). Neither
   number changed a conclusion, but an unreconciled count is indistinguishable
   from a fabricated one. Related to item 3.

9. **A zero from a format-mismatched probe is void, not negative.** Checking for
   `CSRTable.*Mon` in `native-all-strings.tsv` returns 0 — but that table stores
   **mangled** names (`_ZN20CSRSceneStageConfirm…`), never dotted ones, so the
   probe could not have matched anything. The correct probe enumerates mangled
   names: of **1,083** `Dlg`, **25** `Dialog`, **2,227** `Scene`, **1,850**
   `Table`, **5,277** `PopUp` symbols, exactly **one** mentions a monster
   (`CSRSceneStageConfirm::RequestMonsterRef`, a request path — not a stat
   screen). Same void-probe failure as the Hangul one in
   `base-stat-heading-client-attested-2026-10-06.md` §4.

10. **Never hand-write Unicode codepoints for a search term — slice it out of the
    data.** Searching for `능력치` as `U+B2A5 U+BC25 U+CE60` returned **0 hits
    everywhere**, which was impossible: the parent had read that exact string out
    of `UI_TEXT_RO[329]` hours earlier. The real codepoints are
    **`U+B2A5 U+B825 U+CE58`** — two of three were wrong from memory. Taking the
    term as `UI_TEXT_RO[329]["json"]["KO"]` and slicing `[3:]` fixed it
   immediately and then confirmed the claim (4 buff sources). **A zero on a
   non-ASCII term is suspect until you have re-derived the term from the data
    itself.**

11. **The strongest claim of the session survived its own evidence and died on
    contact with a hostile read — commission that read for every big result.**
    `base-stat-heading-client-attested-2026-10-06.md` claimed the archive rows
    were client-attested *base* stats. Two links held (`L1` the heading ships;
    `L2` the archive uses both headings); the load-bearing third (`L3` therefore
    gear-free) had **zero positive support** and was killed by three independent
    negatives — the same block is used on `SR_ENHANCE`/`SR_EQUIP` gear screens,
    `기본 능력치` is a *live buffable combat pool* (`+10 %` in Fight Club and
    Guild Blitz), and EN "Base" is just a generic adjective. A dedicated
   adversarial lane found all three; the parent then re-verified each against the
    tables. **The error was not sloppiness — it was a valid-looking syllogism
    whose middle term was doing more work than the evidence allowed.** Strike and
    date such claims rather than defending them.

12. **An approximate fit reported as exact is a retraction waiting to happen.**
    The level anchor implies per-level factors of `1.018790 / 1.018519 /
    1.019301` for HP/ATK/DEF — a spread of 0.0008, with the DEF value *outside*
    the project's own expected 1.0185–1.0193 band. "≈1.0189 per level, with
    per-stat variation" is the honest form; "g = 1.0189" is not, and a single
    `g` fitted to the mean misses the panel by 6.6 cp at n=29.

13. **A pattern in a derived table is a HYPOTHESIS ABOUT PROVENANCE, never
    evidence about the cells. Fetch the page.** The parent twice built a
    data-defect story on a pattern and was wrong **both times**:
    - *Shared triple* → "`005`/`009` must be a copy-paste error." They are two
      distinct cards (different names, epithets, elements, all five skills, all
      three items) that the site simply publishes with **one shared base row**,
      at ★1 and ★2 respectively.
    - *Outlier ratio* → "so `009`'s ATK must be wrong." The cell is correct; the
      `628 → 576` substitution was numerology fitted to a good number.
    Both were refuted by one exact-URL re-fetch. **Do not explain an anomaly by
    postulating a defect you have not checked at the source** — that is the most
    attractive move available, because it converts an unexplained number into a
    tidy closed case. Both attempts also *suppressed* a real finding: the
    Captain T3 non-uniformity (ATK `1.1688` vs HP/DEF `1.2740` / `1.2788`) is
    **genuinely open**, with every cell now verified correct. Prefer leaving a
    number unexplained.

14. **Two archive-read caveats that will recur.** Wayback's CDX/API returns a
    **reproducible false negative** for at least one exact URL (empty body across
    3 encodings while the direct `id_` fetch returns 200 / 34,670 B), and an
    `id_` request at a non-captured timestamp returned 404 once and a correct 200
    later. So a capture set **cannot be enumerated reliably** — do not claim "no
    second capture exists". Always validate the read path on a known hero
    (`051` reproduced all 13 TSV values with zero mismatches) *before* trusting
    a new page.

---

## 6. If you have one hour, read these 8 files

In this order. Each earns its place by closing the most expensive open question.

1. **[`coverage.md`](coverage.md)** — 15 min. Target definitions, denominators,
   and what "counted" means. Read this *first*; without it every other file's
   verdict is unreadable, and §6's five qualification conditions are the reason
   hero coverage sits at 1/113.
2. **[`fixture-conflict-audit-2026-10-05.md`](fixture-conflict-audit-2026-10-05.md)**
   — 15 min. The single most valuable document in the folder. §1 is 90+ fixture
   rows each placed beside every piece of recovered evidence with a verdict;
   §2.1's tally is the headline finding; §2.6 is the conflict register; §2.5 names
   the fixtures whose scale is visibly wrong. Start here even if you only read
   §1 and §2.1.
3. **[`hero-stat-divergence-2026-10-05.md`](hero-stat-divergence-2026-10-05.md)**
   — 8 min. Answers "what *can* the local data distinguish?" with four hero-side
   and two monster-side sources plus an explicit negative list, then supplies the
   P1–P10 divergence priors and the 62→73 identity-reach result. §3c is the
   definitive "still unrecoverable from anything local" list.
4. **[`transcendence-skill-cost-2026-10-05.md`](transcendence-skill-cost-2026-10-05.md)**
   — 8 min. The model for how two sources should be reconciled cell by cell: the
   39-coincidence common-original argument, the decadal-band resolution that killed
   the pairing ambiguity, the table-scoped 10:1, the single level-25 conflict, and
   §2.12's explicit "flagged, NOT acted on".
5. **[`trace-threshold-2026-10-05.md`](trace-threshold-2026-10-05.md)**
   — 7 min. The best example in the folder of a *false dichotomy* being removed.
   Shows how the official 2018 ★3 trace anchors cut against the very contradiction
   they were filed under, and states the honesty boundary: nothing here licenses
   changing 10 or 20, nor asserting them as original.
6. **[`episode-res-crosswalk-2026-10-05.md`](episode-res-crosswalk-2026-10-05.md)**
   — 7 min. The 64/64-vs-2/22 measurement that retired a convention rule still
   live in two other files, the two `alt`-survivor explanation, the only-placement
   orphan proof, the false-friend table, and §3.1b's self-retraction.
7. **[`help-2_8-sweep-2026-10-05.md`](help-2_8-sweep-2026-10-05.md)**
   — 7 min. The decisive corpus sweep: all 95 shipped help records, zero cost
   patterns, the byte-identical gate records, the full Abyss rewrite, the
   EN-copy deletion, the locale divergences, and the NEW-1..NEW-7 register that
   forced R-14 through R-16.
8. **[`GUARD-encoding-and-archive-traps.md`](GUARD-encoding-and-archive-traps.md)**
   — 2 min, but read it *before* you edit anything. Two agents damaged
   `polluted-observations.md` in this session. Use Python or the edit/write tools
   for any non-ASCII file; never PowerShell 5.1 `Set-Content`; verify bytes, not
   console output.

**Two files to know about but not read first:** `README.md` (per-source visual
verdicts — go to it when a specific gallery or video is in question) and
`polluted-observations.md` (the supplementary ledger, 174 KB; it never contributes
to any threshold and is not part of the reconciliation chain).

## 7. Scope and compliance statement for this synthesis

- Read-only with respect to every existing file. `coverage.md`, `README.md` and
  `polluted-observations.md` were **not modified**; `polluted-observations.md` was
  **not appended**.
- No server, APK, seed, emulator, phone, Ghidra or native-library action was taken.
- No numeric value is asserted here that is not quoted from a cited file; no
  coverage count is recomputed or restated except as read from `coverage.md`.
- Where two files disagree (E8/X3 in §2 above; the trace-threshold verdict versus
  the audit register), that disagreement is **recorded, not resolved**.