# Weekday schedule UI text inventory (2026-10-05)

**Scope:** expand §2.1–2.3 of `sunday-settlement-2026-10-05.md` into a complete
verbatim inventory of every weekday-named schedule row in the recovered
LevelDB UI tables, plus the adjacent rows needed to read them correctly.

**Inputs (read-only):** `analysis/recovered-data/leveldb-tables/all-tables.json`
only. No native decompilation, no Ghidra, no server, no APK, no emulator, no
phone. No source file was modified.

**No coverage-count change.** Heroes 1/113, jewelry/accessories 1/100,
monsters 0/22 — all unchanged. Nothing below counts toward any 70% threshold.

**Conventions.**

- Line numbers are `all-tables.json` line numbers. Row order in that file is
  **plyvel iteration order**, not sorted (`tools/mine-export-reference-tables.py`
  iterates the DB directly), so line numbers are extraction-order artifacts, not
  a semantic or alphabetical order. Keys are the stable identifier.
- "verbatim" means the parsed `json` value's `TEXT`, reproduced exactly,
  including the literal two-character `\n` token (see §1.0).
- Every row is a **UI string table** row. Nothing here is a wire field.

**Row totals: 17 schedule-bearing rows across 15 keys, in 2 tables.**

| table | keys | rows | schedule |
|---|---|---|---|
| `UI_JSON_RO` | 3 | 15 | Sunday→Monday ranking payout (2 keys × 5 locales), Saturday 24:00 Dismount Pass recharge (1 key × 5 locales) |
| `UI_TEXT_RO` | 2 | 2 | Wednesday Fight Club ranking announcement (`TIP_4`), Wednesday Guild Blitz registration (`TIP_8`) — 5 locale values each inside 2 rows |

Locale coverage per row: `EN`, `JA`, `KO`, `SC`, `TC` for all 17 rows.

---

# §1 PURE — verbatim shipped rows (values and keys only, no interpretation)

## 1.0 Line-break token, read before the rows

Three distinct in-string separators appear across these rows. They are **not**
equivalent and must not be normalised:

| token | appears in | meaning |
|---|---|---|
| literal `\n` (backslash + `n`, two chars) | `TX_TITLE` EN, `TX_TITLE` KO, `TX_TITLE` SC, `TX_TITLE` TC | TalkerMaker-style in-game line break |
| literal `\|` (pipe) | `TEXT` SC, `TEXT` TC | alternate in-game line break, used only by the Chinese rows |
| no token | `TX_TITLE` JA, all `TEXT` EN/JA/KO, all `TX_LEAVE`, all `UI_TEXT_RO` | single line, or break handled by layout |

The `TX_TITLE` rows are the only rows in this inventory whose `json.TEXT`
contains a literal backslash. The `raw` field of the same rows carries
`\\\\n` (four backslashes) because the original stored DB bytes contained two
backslashes inside their own JSON string; `json.dumps` re-escaped them. Do not
read the `raw` backslash count as an extra break.

## 1.1 Sunday 12 A.M. snapshot → Monday 6 A.M. ranking-reward payout (10 rows)

`UI_JSON_RO`. Two distinct Korean source sentences, each in five locales.
Both are the **same notice** at two layout slots: `TX_TITLE` (SIZE 20, centred,
alpha 175) and `TEXT` (SIZE 26, top-aligned, alpha 175). Screen context is the
ranking-reward cluster: sibling keys `랭킹 1위`, `랭킹 2위`, `랭킹 3위`,
`랭킹 4-10위`, `랭킹 11-50위` (`|TEXT|<locale>`, lines 131804–132202) and
`랭킹 확인|TX_O|<locale>` (lines 132364–132447).

### 1.1a key `랭킹 보상은 매주 일요일 밤 12시에 지급됩니다.|TX_TITLE|<locale>`

Layout, identical in all five rows:
`FONT=DEFAULT_FONT`, `SIZE=20`, `ALIGN=center|center`, `COLOR=255|255|255|175`,
`LSPACE=1.2`, `TSPACE=1`, `B_RECT=0|3`, `B_SIZE=600|80`, `B_ALIGN=center|top`.

| line | locale | `TEXT` verbatim |
|---|---|---|
| 132204 | EN | `Ranks as of Sunday 12 A.M. will be distributed\ntheir ranking rewards by Monday 6 A.M` |
| 132220 | JA | `ランキング報酬は毎週日曜 夜12時のランキングをもとに、月曜日の朝6時に支給されます` |
| 132236 | KO | `랭킹 보상은 매주 일요일 밤 12시의\n순위를 기준으로 월요일 아침 6시에 지급됩니다.` |
| 132252 | SC | `排名奖励以每周星期日晚上12点的排名为准\n将在星期一早上6点赠送。` |
| 132268 | TC | `排名獎勵將以每周日晚間１２點的名次為準\n周一早上6點進行發放` |

Pure observations about this group, no inference:

- The EN row has **no terminal period**; the KO, SC, TC rows do; the JA row has
  none. The JA row has **no** `\n` token although its box is two lines tall.
- The EN wording is ungrammatical in the original ("will be distributed their
  ranking rewards"), reproduced here unchanged. Do not silently repair it.
- TC uses full-width `１２` (U+FF11 U+FF12) for "12" in this group, while the
  `TEXT` TC row below uses half-width `12`. Both are as shipped.
- SC here uses "星期日/星期一" (the explicit weekday form); the `TEXT` SC row
  below uses "周日/周一". Both are as shipped.

### 1.1b key `랭킹 보상은 매주 일요일 밤 12시의 순위를 기준으로 월요일 아침 6시에 지급됩니다.|TEXT|<locale>`

Layout, identical in all five rows:
`FONT=DEFAULT_FONT`, `SIZE=26`, `ALIGN=center|top`, `COLOR=255|255|255|175`,
`LSPACE=1`, `TSPACE=1`, `B_RECT=0|25`, `B_SIZE=600|100`, `B_ALIGN=center|top`.

| line | locale | `TEXT` verbatim |
|---|---|---|
| 132284 | EN | `Ranks as of Sunday 12 A.M. will be distributed their ranking rewards by Monday 6 A.M.` |
| 132300 | JA | `ランキング報酬は毎週日曜 夜12時のランキングをもとに、月曜日の朝6時に支給されます` |
| 132316 | KO | `랭킹 보상은 매주 일요일 밤 12시의 순위를 기준으로 월요일 아침 6시에 지급됩니다.` |
| 132332 | SC | `排名奖励会以每周日晚上12点的排位为准|将在星期一早上6点发放。` |
| 132348 | TC | `排名獎勵會以每周日晚間12點的排名為準|將於週一早上六點進行發放。` |

Pure observations:

- The `TEXT` JA row is **byte-identical** to the `TX_TITLE` JA row.
- EN/JA/KO rows contain **no** line-break token at all in this group; SC and TC
  use the literal pipe.
- Same EN sentence as §1.1a, but here **with** the terminal period. The two
  slots disagree on punctuation; that is as shipped.

### 1.1c Weekday/time tokens present in §1.1

`일요일` (Sunday) appears in the KO key and KO `TEXT` only.
`월요일` (Monday) appears in the KO key and KO `TEXT` only — **the English,
Japanese, SC and TC rows carry no Korean weekday token**; the non-Korean
weekday words are inside their own locale text.

## 1.2 Wednesday Fight Club ranking announcement — `TIP_4` (1 row, 5 locales)

`UI_TEXT_RO`, line 45022 (key), values 45024–45030. Row shape is locale-keyed
(`KO`/`EN`/`JA`/`SC`/`TC` at the top level), **no** `|locale` suffix in the key,
no layout fields.

| locale | value verbatim |
|---|---|
| KO | `파이트클럽의 순위는 매주 수요일에 발표됩니다.` |
| EN | `Fight Club rankings are announced every Wednesday.` |
| JA | `VSクラブのランキングは毎週水曜日に発表されます。` |
| SC | `搏击俱乐部的排名会在每周三公布。` |
| TC | `鬥陣俱樂部的排名會在每週三公佈。` |

## 1.3 Wednesday Guild Blitz registration — `TIP_8` (1 row, 5 locales)

`UI_TEXT_RO`, line 45066 (key), values 45068–45074. Same row shape as §1.2.

| locale | value verbatim |
|---|---|
| KO | `협회 쟁탈전은 매주 수요일부터 참가 접수를 받습니다.` |
| EN | `Guild Blitz participation requests can be made every Wednesday.` |
| JA | `ギルド争奪戦は毎週水曜から参加申請を受付けています。` |
| SC | `公会争夺战从每周三起开放报名。` |
| TC | `公會爭奪戰從每週三起開放報名。` |

Pure observation: `TIP_4` and `TIP_8` are the **only** two rows in the whole
recovered table set that name Wednesday, and both describe a Fight Club / Guild
Blitz event, **not** the ranking payout of §1.1.

## 1.4 Saturday 24:00 Dismount Pass recharge — `해제권은|TX_LEAVE|<locale>` (5 rows)

`UI_JSON_RO`, keys at lines 244044/244060/244076/244092/244108. Layout
identical in all five rows: `FONT=DEFAULT_FONT`, `SIZE=18`,
`ALIGN=center|top`, `COLOR=255|255|255|230`, `LSPACE=1`, `TSPACE=1`,
`B_RECT=0|90`, `B_SIZE=500|70`, `B_ALIGN=center|top`.

| line | locale | `TEXT` verbatim |
|---|---|---|
| 244044 | EN | `해제권은 매주 토요일 24시에 충전됩니다.` |
| 244060 | JA | `해제권은 매주 토요일 24시에 충전됩니다.` |
| 244076 | KO | `해제권은 매주 토요일 24시에 충전됩니다.` |
| 244092 | SC | `해제권은 매주 토요일 24시에 충전됩니다.` |
| 244108 | TC | `해제권은 매주 토요일 24시에 충전됩니다.` |

Pure observations — the strongest single result in this inventory:

- **All five locale rows are byte-identical Korean.** The `EN`, `JA`, `SC` and
  `TC` rows are untranslated. This is a shipping defect in the original data,
  not a decode failure and not an extraction artefact.
- `토요일` (Saturday) and `24시` (24:00, i.e. end of Saturday) are the **only**
  Saturday/time-of-day tokens in the recovered tables.
- Sibling keys identify the resource as Dismount Passes:
  `보석 해제에 필요한 해제권이 모자랍니다. |TX_MD_BG|EN` (line 161724) reads
  `You do not have enough\nDismount Passes to remove the Jewel(s).` — the same
  literal `\n` break token as §1.1 — and `해제권 사용|TX_BT4_TX|<locale>`
  (lines 243964–244041) reads `해제권으로 해제` under the `開採結晶`
  (gem-mining) heading at line 161721. `결정 해제권이 부족합니다.`
  (line 46485, `UI_TEXT_RO`) is a further shortage string with no locale
  variants.

## 1.5 Weekday census across all 13 recovered tables

Exhaustive token sweep of `all-tables.json` for every Korean and English
weekday word:

| weekday | Korean token | lines | rows |
|---|---|---|---|
| Sunday | `일요일` | 14 | 10 (§1.1) |
| Monday | `월요일` | 9 | 5 (§1.1, in KO text only) |
| Tuesday | `화요일` | 0 | 0 |
| Wednesday | `수요일` | 4 | 2 (§1.2, §1.3) |
| Thursday | `목요일` | 0 | 0 |
| Friday | `금요일` | 0 | 0 |
| Saturday | `토요일` | 10 | 5 (§1.4) |
| "every week" | `매주` | 30 | 17 (§1.1, §1.2, §1.3, §1.4) **+ `TIP_3`** |

English names: `Sunday` 4 lines, `Monday` 4, `Wednesday` 4, and **zero**
`Tuesday` / `Thursday` / `Friday` / `Saturday` — because the only Saturday text
is the untranslated Korean block of §1.4. Three distinct weekdays appear in
shipped UI: Sunday, Monday, Wednesday, Saturday.

**Zero weekday tokens were found in** `SKILL_REF_RO`, `SKILL_TAG_RO`,
`SKILL_EFFECT_RO`, `SKILL_DESC_RO`, `TAG_REF_RO`, `CHAR_STR_RO`,
`INGAME_TALK_RO`, `ADMIN_ID_RO`, `UI_EPISODE_RO`, `UI_XML_RO`, `BADWORD_RO`.

## 1.6 Adjacent rows inventoried and deliberately excluded

Recorded so a later reader does not mistake them for weekday schedule rows:

| line(s) | key | why excluded |
|---|---|---|
| 45011–45019 | `TIP_3` | `매주` / "Every week" but names **no weekday**: `Every week, you can get Fight Chips and Manda based on your Fight Club ranking. Collect Challenge Invitations and fight!` A weekly-cadence row with no day, so it cannot arbitrate between Sunday and Wednesday. |
| 47475–47483 | `길드_탈퇴_확인팝업_설명[%s]` | `24시간` = **24 hours**, a rejoin cooldown: `If you leave the Guild, your accumulated Contributions\nwill disappear, and you won't be able to rejoin for 24 hours.` A duration, not a weekday, despite sharing the `24` numeral with §1.4. |
| 131804–132202 | `랭킹 1위`, `2위`, `3위`, `4-10위`, `11-50위` \|TEXT\|<locale> | Five ranking-band labels × 5 locales = 25 rows. Band boundaries only (`1위`, `2위`, `3위`, `4-10위`, `11-50위`); no day, no amount. |
| 132364–132447 | `랭킹 확인\|TX_O\|<locale>` | Button caption `Leaderboards` × 5 locales. No schedule content. |
| 161724–161800, 46485, 243964–244041 | `해제권` shortage / use rows | Identify the Saturday-recharged resource (§1.4) but carry no weekday. |

---

# §2 UNPURE — every schedule token as impure operations context

Everything in §2 is **impure** and counts toward nothing. All of it is
**ERA-UNRESOLVED** — no dated capture distinguishes pre- or post-2019-09-05
balance eras (`stat-version-context.md`). None of it is a parser binding; the
native weekday/schedule literals (`Sunday`/`Monday`/`Wednesday` at
0x1dab860/0x1dab82e/0x1dab83d) are an unbound libc/curl block per
`sunday-settlement-2026-10-05.md` §1.2, and that negative result **still
stands** — this inventory adds shipped UI text, not native consumers.

## 2.1 Token ledger

| # | impure token | rows | shipped claim | native binding |
|---|---|---|---|---|
| T1 | Sunday 12 A.M. snapshot | §1.1 (10) | ranks as of Sunday midnight | **none** |
| T2 | Monday 6 A.M. payout | §1.1 (10) | ranking rewards paid by Monday 06:00 | **none** |
| T3 | Wednesday Fight Club ranking announcement | §1.2 (1) | weekly Wednesday announcement | **none** |
| T4 | Wednesday Guild Blitz registration open | §1.3 (1) | registration from Wednesday | **none** |
| T5 | Saturday 24:00 Dismount Pass recharge | §1.4 (5) | weekly Saturday-24:00 refill | **none** |
| T6 | "every week" without a day | `TIP_3` | weekly FC ranking payout | **none** |

## 2.2 The scheduling model these texts imply, and why it is not recovered

- **Sunday → Monday ranking payout (T1/T2).** A ~6-hour settlement window:
  snapshot at Sunday 24:00, payout by Monday 06:00. This is the *intended*
  cadence only. No native literal, no `GetWeekday`/`tm_wday`/modulo-7
  consumer, and no binding of this text to `weekly_end_datetime`,
  `weekly_next_datetime` or `is_weekly_reward` was recovered. The replica's
  week-aligned Unix-second season is a **unit-correct fixture**, not this rule.
- **Wednesday is a different event, not a variant (T3/T4).** `TIP_4` announces
  Fight Club *rankings*; `TIP_8` opens Guild Blitz *registration*. Both are
  Wednesday. **Do not collapse them into the Sunday payout** and do not read
  "Wednesday" as a rival answer to "Sunday" — they are three distinct systems
  (ranking payout, FC announcement, Blitz registration) with three distinct
  texts. A schedule model needs three separate rules, not one weekday.
- **Saturday shows the week is not Sunday-anchored (T5).** A second, unrelated
  weekly refill at Saturday 24:00 falsifies any single "everything resets
  Sunday" simplification. Two weekly deadlines six days apart both ship in the
  same data set.
- **`TIP_3` cannot arbitrate (T6).** It says "every week" and gives the reward
  *type* (Fight Chips and Manda by Fight Club ranking) but **no day**. It is
  consistent with either Sunday or Wednesday and therefore supplies no
  discriminating evidence; keep it as context, not as a tiebreaker.
- **Untranslated Saturday text is a caution against trusting EN for schedule.**
  §1.4's `EN` row is Korean. Any future English-only scrape of these tables
  would have found **zero** Saturday evidence. Locale-keyed rows (`UI_TEXT_RO`)
  and `|locale`-suffixed keys (`UI_JSON_RO`) fail in opposite directions, so a
  schedule inventory must sweep all five locales — as §1.5 does.

## 2.3 What a future schedule model must not assume

1. Not that `weekly_end_datetime` is Sunday 24:00 UTC. The replica's current
   fixture aligns to a Unix week; the shipped text says *Sunday local*, and no
   timezone was recovered (§2.5).
2. Not that "24시" is a client timezone marker. §1.4's `24시` is Korean 24-hour
   notation for midnight ending Saturday; §1.6's `24시간` is a 24-hour
   cooldown. Same numeral, unrelated semantics.
3. Not that the 6-hour Sunday→Monday window is a server-enforced deadline. It
   appears only as display copy in two layout slots.
4. Not that ranking bands `1 / 2 / 3 / 4-10 / 11-50` (§1.6) are the reward
   tiers. They are labels present in the same cluster; no amount is shipped
   here and none was recovered.
5. Not that Dismount Pass Saturday refill implies a purchasable Saturday ticket
   or any price. No amount, price or purchase path exists in these rows.

## 2.4 Cross-reference status

Unchanged from `sunday-settlement-2026-10-05.md` §2.4–2.5: the Namu
`(티어)보상` / `(순위)보상` wiki cells still describe a Sunday settlement and a
rank payout after settlement, and still have **zero** native corroboration. The
shipped UI text of §1.1 is *newly consistent* with that wiki prose — two
independent sources now agree on Sunday-snapshot → Monday-morning payout — but
**agreement is not corroboration**: both are text, not protocol. Keep
`sunday-settlement-2026-10-05.md` §1.2's negative result intact; do not
upgrade this to a recovered schedule. The 2018 World Championship reward-body
empty archive, the absence of any season length / season number / timezone /
payout-amount literal, and the unrecovered bronze tier value, gacha rates and
login-supply calendar all remain open exactly as recorded there.

## 2.5 Open questions this inventory raises, none answered

- Which of Sunday 24:00 or Monday 06:00 is the snapshot and which is the
  deadline? The EN copy is ambiguous on its face ("Ranks as of Sunday 12 A.M.
  will be distributed their ranking rewards by Monday 6 A.M"), and the KO is
  only clearer because it says "based on".
- Is the Saturday 24:00 refill a **grant** of a fixed count or a reset to a
  cap? The text says only "충전됩니다" ("is recharged/filled"). Count, cap and
  timezone are all absent.
- Are Wednesday's two texts driven by the same weekly cycle as Sunday's, or by
  a separate one? Three texts, no shared literal, no answer.
- Do the JA rows' missing `\n` and the SC/TC pipe separators mean those locales
  render on one line inside a two-line box? Rendering was not verified on device.
- Is there any weekday-named text in the 774 `.jet` packages or in
  `UI_CSV.jet` that this LevelDB-only sweep could not see? Not checked here;
  this inventory is bounded to `all-tables.json`.

---

# §3 File log

- **This file (new):** `analysis/research/base-stats-visual-hunt/weekday-ui-2026-10-05.md`.
- `polluted-observations.md`: appended a pointer section to this file, marked
  impure, with no coverage-count effect and no duplicated numeric rows beyond
  the schedule pointers in §2.1.
- Sources read: `analysis/recovered-data/leveldb-tables/all-tables.json`
  (lines 1–56 header, 45005–45093, 47470–47493, 131804–132447, 161718–161800,
  243958–244125) and `tools/mine-export-reference-tables.py` lines 30–90 for
  the plyvel-ordering caveat.
- **No** server source, APK, seed DB, emulator, phone, Ghidra project, or
  native library was touched. Read-only inventory.
- No coverage-count change; no goal completion implied.