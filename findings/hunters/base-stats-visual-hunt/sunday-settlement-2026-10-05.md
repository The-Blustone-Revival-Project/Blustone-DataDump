# Sunday / settlement / weekly-reset native-literal hunt (2026-10-05)

**Scope:** close the §1.7 gap in `fc-native-2026-10-05.md` (clock units agree,
weekly schedule gap: no Sunday/settlement/reset literal recovered). Read-only:
`analysis/research/arena-season-time-units.md`,
`analysis/ghidra-arena-corrected-strings.txt`,
`analysis/ghidra-arena-enter-rival-strings.txt`,
`analysis/ghidra-arena-league-reference-strings.txt`,
`analysis/native-all-strings.tsv`,
`analysis/recovered-data/leveldb-tables/all-tables.json`.
No server/APK change. No coverage-count change (heroes 1/113, accessories
1/100, monsters 0/22).

**Address convention:** G addresses are Ghidra addresses (= ELF code VA +
0x10000). String-table VAs (0x1d7xxxx) are native `.rodata` addresses from
`native-all-strings.tsv` — ⚠️ **which are themselves Ghidra image addresses
(= ELF VA + `0x10000`), not ELF VAs** (corrected 2026-10-05). Verified: 17/17
string-VA pairs in this file match byte-exactly at `VA − 0x10000`, 0/17 at the VA
as printed — e.g. `season_no` printed `0x1d7331e` is at ELF VA `0x1d6331e`.
Both columns therefore share **one** convention; to read bytes, subtract `0x10000`
(all these literals are in the first `PT_LOAD`, where `p_vaddr == p_offset`).
Definitive table: `address-convention-2026-10-05.md`.

---

## 1. PURE — native literals and consumers found (values only, no provenance)

"Literal" = a string-table entry with a proved `ldr [pc]` + `add pc`
consumer in the corrected resolver dumps. A bare string-table entry with no
recovered consumer is reported as unbound, not as proof of a schedule.

### 1.1 Weekly cadence literals — RECOVERED with consumers

**`ParseSeason` (G 0x942e24)** — 8/8 resolved (`ghidra-arena-corrected-strings.txt`
§`00942e24`):

| literal | string VA | ldr | add |
|---|---|---|---|
| `season_no` | 0x1d7331e | @00942e34, slot 0x9430d8 | @00942e42 |
| `weekly_no` | 0x1d73362 | @00942e98, slot 0x9430dc | @00942e9e |
| `start_datetime` | 0x1d7336c | @00942ee6, slot 0x9430e0 | @00942eec |
| `end_datetime` | 0x1d72926 | @00942f34, slot 0x9430e4 | @00942f3c |
| `next_datetime` | 0x1d7337b | @00942f86, slot 0x9430e8 | @00942f8e |
| `weekly_start_datetime` | 0x1d73389 | @00942fd8, slot 0x9430ec | @00942fe0 |
| `weekly_end_datetime` | 0x1d7339f | @0094302a, slot 0x9430f0 | @00943032 |
| `weekly_next_datetime` | 0x1d733b3 | @0094307c, slot 0x9430f4 | @00943084 |

**`ParseUser` (G 0x9430f8)** re-consumes `season_no` (ldr@009431ec → 0x1d7331e)
and `weekly_no` (ldr@0094323a → 0x1d73362), plus `league_level`,
`rating_point`, `league_win`, `win`, `lose`, `refresh_datetime`,
`start_message`, `win_message`, `lose_message` (13/13 resolved).

**`ReqEnterCB` (G 0xf5d3b4) → `ParseEnter` (G 0x942c3c)** consumes
`is_weekly_reward`: ldr@00942d78, slot 0x942e1c → string VA 0x1d732f4
(`ghidra-arena-enter-rival-strings.txt:8`). `arena.status == 1` gates all
season/user parsing (`arena-lobby-contract.md:36`).

**`ParseBattleWeeklyRwd` (G 0x948b48)** consumes the weekly-reference
container `weekly_reward`: ldr@00f83a7e, slot 0xf83aa4 → string VA 0x1d90238
(`ghidra-arena-league-reference-strings.txt:32`), then `min_ranking`
(ldr@00948d02 → 0x1d73585), `max_ranking` (ldr@00948d6e → 0x1d73591),
`user_exp`, `gold`, `honor`, `free_iap`, `item_list`/`id`/`qty`.

**`ReqMyRankCB` (G 0xf600d8)** consumes scalar `ret_data.rank` → PlayData+0x128
(`arena-my-rank-contract.md`). Rank scalar only; no schedule content.

**Clock units (agreed, unchanged):** `end_datetime` is numeric server-epoch
**seconds** — `RemainTimeTextRenewal` (G 0xc0c5cc) subtracts
`CGMTime::GetCurServerTime` (G 0x797628, tick-ms ÷ 1000) with no millisecond
scaling, divides by 86400 (`arena-season-time-units.md`). All six season/weekly
datetime fields store as numeric64 without scaling. This proves units and clock
coordinate, not any weekday or reset schedule.

### 1.2 NEGATIVE — no Sunday/settlement/reset/schedule literal with an arena consumer

- **`Sunday` (0x1dab860), `Monday` (0x1dab82e), `Wednesday` (0x1dab83d):**
  present in `native-all-strings.tsv:453907–453913`, but contiguous with
  `Thu/Fri/Sat/Sun` short forms (0x1dab7c7–0x1dab7d3), scanf/time formats
  (`%31[...]`, `%02d:%02d:%02d`) and the TFTP state-machine strings
  (`bind() failed`, timeout/retry/ACK messages, 0x1dab867+). This is a
  libc/curl day-name + time-format + TFTP block, **not** an arena schedule
  table. No `ldr`/`add` pair in any corrected arena dump resolves to
  0x1dab82e/0x1dab83d/0x1dab860. **Unbound; not a settlement literal.**
- **`arena_season_no` (0x1d913e1):** present in the string table
  (`native-all-strings.tsv:448759`); no recovered `ldr` consumer in any
  arena dump. **Unbound.**
- **`settlement` / `settle` / `reset_day` / `weekly_reset` / `payout` /
  `schedule`:** zero string-table hits. `Reset*` hits are exclusively C++
  method names (`CMUpdatable::Reset`, `CSRScene::Reset`,
  `CSRSyncExplore::RequestAbyssReset`, etc.), none an arena weekly-schedule
  key. **Not recovered.**
- **Weekday-index arithmetic:** no `GetWeekday`/`tm_wday`/modulo-7 consumer
  was found on any arena path inspected. The weekly window is carried purely
  as the six opaque `*_datetime` numeric64 fields above.
- **Result:** the native code proves a *weekly window vocabulary*
  (`weekly_no`, three weekly datetimes, `is_weekly_reward`, `weekly_reward`
  rows) with second-unit timestamps — and **no weekday name, no settlement
  verb, no reset rule, no payout-timing literal bound to any of them**.
  fc-native §1.7's "clock units agree; weekly schedule gap" stands unchanged.

### 1.3 Pure verdict table

| candidate | native status |
|---|---|
| `season_no` / `weekly_no` | bound (§1.1) — identifiers only, no weekday |
| `start/end/next_datetime` + weekly trio | bound (§1.1) — opaque numeric64, seconds proved for display path |
| `is_weekly_reward` | bound (Enter gate flag) — boolean, no day |
| `weekly_reward[]` + `min/max_ranking` | bound (reference rows) — band shape, rewards 0/empty in replica |
| `arena_season_no` | string-table only, no consumer — unbound |
| `Sunday` / `Monday` / `Wednesday` | string-table only, libc/curl block — unbound, not arena |
| settlement / reset-day / payout-timing | absent — negative result |

---

## 2. UNPURE — every Sunday/settlement/weekday token as impure operations context

Nothing below counts toward any 70% threshold (heroes, jewelry/accessories,
monsters). Do not normalize against the 2019-09-05 rebalance; every token is
**ERA-UNRESOLVED** unless a dated capture is noted. Do not treat a weekday
word in UI text as corroboration of any native parser field (§1.2 precedent).

### 2.1 Shipped UI text: Sunday/Monday ranking-reward notice (strongest impure lead)

- **Source:** `analysis/recovered-data/leveldb-tables/all-tables.json`
  (~lines 132204–132348), key `랭킹 보상은 매주 일요일 밤 12시에 지급됩니다.|TX_TITLE|EN`
  (and `...|TEXT|EN`, plus JA/KO/SC/TC rows).
- **Raw EN tokens:** TITLE `Ranks as of Sunday 12 A.M. will be distributed\ntheir ranking rewards by Monday 6 A.M`;
  TEXT `Ranks as of Sunday 12 A.M. will be distributed their ranking rewards by Monday 6 A.M.`
  KO: `랭킹 보상은 매주 일요일 밤 12시의\n순위를 기준으로 월요일 아침 6시에 지급됩니다.`
- **Why impure:** shipped display text proves the *intended* cadence
  (Sunday-midnight snapshot → Monday-6AM payout), but no native parser or
  clock consumer binding this text to `weekly_end_datetime`/`is_weekly_reward`
  was recovered. The KO key asks for a TX_TITLE/TEXT lookup, not a JSON wire key.
- **Status:** operations-context lead for future schedule modeling; never a
  parser binding.

### 2.2 Shipped UI text: Wednesday Fight Club / Guild Blitz notices (weekday contrast)

- **Source:** same `all-tables.json` (~lines 45024–45074):
  KO `파이트클럽의 순위는 매주 수요일에 발표됩니다.` / EN
  `Fight Club rankings are announced every Wednesday.`;
  KO `협회 쟁탈전은 매주 수요일부터 참가 접수를 받습니다.` / EN
  `Guild Blitz participation requests can be made every Wednesday.`
  (JA/SC/TC rows present).
- **Why preserved:** a second weekday (Wednesday) governs Fight Club *ranking
  announcements* in shipped text, conflicting with a naive "everything settles
  Sunday" model. Do not collapse Wednesday announcements into the Sunday payout
  rule; the two texts describe different events.
- **Status:** impure contrast tokens; no native consumer recovered.

### 2.3 Shipped UI text: Saturday ticket recharge (further weekday contrast)

- **Source:** same `all-tables.json` (~lines 244046–244121): five identical
  TEXT rows `해제권은 매주 토요일 24시에 충전됩니다.` (release tickets recharge
  every Saturday at 24:00).
- **Status:** impure; kept so a future schedule model does not invent a
  Sunday-only reset week.

### 2.4 Wiki Sunday settlement (operations context, ERA-UNRESOLVED)

- **Tokens:** settlement + reset every Sunday; rank payout after settlement only.
- **Sources:** Namu main-page footnotes `(티어)보상` / `(순위)보상` via mirror
  `https://d.namu.moe/w/블루스톤` (mirror HTTP 200, fetched 2026-10-05; page
  last-modified 2026-08-13, content spans 2017–2021); canonical
  `https://namu.wiki/w/블루스톤` (direct fetch 403). Prose agreement in
  `namu-kr-blogs-2026-10-05.md` §2; exact cells in `namu-tables-2026-10-05.md`
  §§4–5. Full cross-check: `fc-economy-2026-10-05.md` §1.4 (A/B agree, C empty).
- **Native status:** zero corroboration (§1.2). The replica's week-aligned
  Unix-second season is a unit-correct fixture, not a recovered Sunday rule.
- **Status:** impure rebalance/operations context; consistent but single-wiki-sourced.

### 2.5 Negative results preserved

- 2018 World Championship reward detail body empty in archive
  ([2019-11-22 capture](https://web.archive.org/web/20191122162749/https://blustone.jp/%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88-%E3%83%95%E3%82%A1%E3%82%A4%E3%83%88%E3%82%AF%E3%83%A9%E3%83%962018%E3%83%AF%E3%83%BC%E3%83%AB%E3%83%89%E3%83%81%E3%83%A3%E3%83%B3%E3%83%94%E3%82%AA%E3%83%B3-2));
  `blustone.jp` is a Japanese fan walkthrough site, not VisualShower's server
  (see `wayback-announce-2026-10-05.md`).
- No season length, season number, timezone, or payout-amount literal recovered
  on any arena path inspected.
- Bronze tier value, gacha rates, login-supply calendars, CDN/reslist strings,
  per-entity stat anchors: not recovered in these sources.

### 2.6 File log

- This file (new): `sunday-settlement-2026-10-05.md`.
- `polluted-observations.md`: appended §"Sunday/settlement native-literal hunt
  (2026-10-05)" pointing here; numeric/schedule tokens not duplicated beyond
  pointers and the Sunday–Monday payout wording.
- No coverage-count change; no server/APK change.
