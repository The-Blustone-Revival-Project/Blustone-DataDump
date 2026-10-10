# Star-clear conditions: what they were, and when they changed (2026-10-09)

**Lane:** the CN-beta `全体生存` finding in
[`cn-beta-video-2026-10-09.md`](cn-beta-video-2026-10-09.md) §6.2 asked whether the
project's three default conditions (Complete / Under 60 s / ≤1 Straggler) are era-wrong.

**Verdict up front, in four parts.**

1. **The third condition did change.** It was **"all survive"** and became
   **"1 Straggler or Less"**. This is no longer a hypothesis: both eras are present in
   the game's **own shipped localisation data**, under the **same on-screen ID** and the
   **same Korean key**, with **only the text differing**.
2. **It is not the CN build's content.** The CN beta shows the *older* string set
   verbatim. It is a pre-change client, not a regional rule difference.
3. **Bracket: after 2019-12-14, before 2.8.0.1.** The 2019-09-05 rebalance **did not**
   do it — the old rule was still being published three months later.
4. **The server's current default is correct** for the client it ships, and the two
   other conditions are **unchanged across the whole era span**. Only one of three moved.

---

## 1. The instrument: where the labels actually live

The star labels are **client-side text, selected by a fixed index** — the server never
supplies the wording. This is the structural fact the rest of the note rests on.

`achieve[].order` (0/1/2) selects one of **three hard-coded on-screen strings** carried
in the client's own text table, with stable IDs:

| slot | on-screen ID | meaning |
|---|---|---|
| 1 | `TX_RS_M` | mission/clear |
| 2 | `TX_RS_C` | time |
| 3 | `TX_RS_T` | survival |

A fourth ID, `TX_TG`, carries the same three concepts for the mission-list / tooltip
context (`OO:OO 이내 클리어`, `클리어`, and the survival condition).

**Evidence.** Two independent stores, both read here:

* **1.4.4.1** — flat five-locale CSV inside the APK: `assets/UI_CSV.jet` chunk 3
  (localisation, 818 rows) and chunk 4/5 (text-layout table, 11,561 rows).
* **2.8.0.1** — the downloaded LevelDB stores `UI_JSON_RO.db` (12,490 records, key
  `ORI|ID|LANG`) and `UI_TEXT_RO.db` (1,589 records, `{KO,EN,JA,SC,TC}`).

All 7 workspace copies of `UI_TEXT_RO.db` are **byte-identical** (one SST sha256
`329d09cf75c451c4…`), so they give no era spread. The era spread comes from the
**1.4.4.1 APK**, which is a different build entirely.

### 1.1 Instrument faults caught before any zero was recorded

* My first LevelDB reader returned **0 entries** — the compression byte was being read
  at `raw[-1]` instead of `raw[size]`. Fixed, then positively controlled: 1,589 /
  12,490 / 584 entries across the three stores.
* `tools/extract-jet-chunk.py --index 4` on the **2.8** `UI_CSV.jet` returns an ISO
  **country-code** table whose `KR`/`EN`/`JP` columns are country names. Reading it as
  a localisation table would have produced a false "the strings were deleted" result.
  In 2.8 the localisation table moved out of `UI_CSV.jet` into the LevelDB.
* Two `False` results from hand-typed Korean literals in a shell one-liner (guard
  rule 13). Re-run by slicing the keys out of the data: the thresholds **are** present.
  The `False` values were the instrument, not the data.

---

## 2. Every documented version of the star conditions

### Version A — client **1.4.4.1** (VSFan archive APK)

`com-vshower-prd-sr-1441-39567016-ef64fd3f499bd158a709f4c380d3c06d.apk`,
94,877,834 B, versionCode 1441, minSdk 16 / targetSdk 26.
Extracted **directly from the APK bytes** in this lane and verified byte-identical to
the pre-existing VSFan copy (both 81,975 B; identical star row).

| slot | ID | layout ORI | KR | EN | JA | ZH | ZH-HANT |
|---|---|---|---|---|---|---|---|
| 1 | `TX_RS_M` | `임무 완료` | `임무 완료` | `Mission\nComplete` | `Mission\nComplete` | `任务完成` | `Mission\nComplete` |
| 2 | `TX_RS_C` | `60초 이내 클리어` | `60초 이내\n클리어` | **`Under 60s`** | `60秒以内\nクリア` | `60秒以內\n完成` | `60秒以內\n完成` |
| 3 | `TX_RS_T` | `팀 전원 생존` | `팀 전원\n생존` | **`All\nSurvived`** | `全メンバー\n  生存` | **`全体生存`** | `全隊生還` |

Tooltip twin `TX_TG`, ORI `팀원 전원 생존`: EN `All Teammates Survived`,
JA `全メンバー生存`, ZH `全体队员存活`, ZH-HANT `全體隊員生還`.

The flat localisation CSV keys the same records by their **original Korean text**.
For slot 3 that key is **`동료 전원 생존`**, whose Korean value is `팀 전원 생존`.
Both the record key `동료 전원 생존` and the layout ORI `팀 전원 생존` are the
*pre-change* wording — see §2's diff and §2.1.

Dating of version A: **not internally stamped** (all ZIP entry dates zeroed to
1980-01-01). Its sibling captures in the same archive are dated —
CDN reslists `20170904165634` (1.1.2.0) and `20170908141924` (1.1.3.0), and
bug-report screenshots `20170812`…`20170820`. Softonic lists this exact APK
(same filename hash) at version 1.4.4.1. So version A is **2017-or-later**, and the
first *dated* proof of the string is in §3.

### Version B — client **2.8.0.1** (the replica's own client)

| slot | ID | layout ORI | KR | EN | JA | ZH (SC) | ZH-HANT (TC) |
|---|---|---|---|---|---|---|---|
| 1 | `TX_RS_M` | `임무 완료` | `임무 완료` | `Mission\nComplete` | `ミッション\n完了` | `任务完成` | `Mission\nComplete` |
| 2 | `TX_RS_C` | `60초 이내 클리어` | `60초 이내\n클리어` | **`Under 60s`** | `60秒以内\nクリア` | `60秒以內\n完成` | `60秒以內\n完成` |
| 3 | `TX_RS_T` | `팀 전원 생존` | `낙오자\n1명 이하` | **`1 Straggler\nor Less`** | `脱落\n1名以下` | **`落伍\n1名以下`** | `一名以下\n掉落` |

Tooltip twin `TX_TG`, ORI `팀원 전원 생존`: EN `1 Straggler or Less`,
JA `脱落1名以下`, ZH `落伍1名以下`, ZH-HANT `一名以下的掉落`.

In `UI_TEXT_RO.db` the slot-3 record is still keyed **`동료 전원 생존`**
(`KO` `낙오자 1명 이하`, `EN` `1 Straggler or Less`, `SC` `落伍1名以下`) — the same key
it carried in 1.4.4.1, where its value was `팀 전원 생존` / `All Teammates Survived` /
`全体生存`.

### 2.1 The stale-key signature

Two identifiers for slot 3 survive **verbatim** into 2.8.0.1 while every rendered value
around them changes:

| identifier | where | says |
|---|---|---|
| `동료 전원 생존` | flat record key (both eras, both stores) | "fellow members all survive" |
| `팀 전원 생존` | `TX_RS_T` layout ORI (both eras) | "whole team survives" |

Yet 2.8.0.1 renders `1 Straggler or Less` / `낙오자 1명 이하` / `落伍1名以下` for that
slot. **Both handles still name the old rule while the rule is the new one.**

This is the signature of a balance change applied without touching the localisation
keys — the lookup handles were left pointing at text that no longer existed, and the
value behind the stable key `동료 전원 생존` was simply overwritten. It is the single
strongest piece of evidence that the **condition** changed rather than merely being
re-translated: a translation fix would have moved the *value* only, which is what
happened, but a *new condition* would have needed a new key, and none was added.

### Version C — the CN beta, **2018-12-12/13** (regional build)

`任务完成` / `60秒以内完成` / `全体生存`, read by eye at 5× from
`cnbeta-frames-2026-10-09/claim-C06-victory-stars.png` (t = 705 s).

**This is version A verbatim**, slot for slot, including the `60` threshold:

| slot | CN beta | version A ZH | match |
|---|---|---|---|
| 1 | `任务完成` | `任务完成` | identical |
| 2 | `60秒以内完成` | `60秒以內\n完成` | same reading; differs only by the simplified/traditional form of 内/內 and a line break |
| 3 | `全体生存` | `全体生存` | identical |

(The era-A `ZH` column carries the traditional `內` even in the column labelled
Simplified — a quirk of the shipped table, not a transcription slip here.)

**Conclusion: the CN beta is not a different content set and not a regional rule
variant.** It is a client still shipping the pre-change string table. The CN beta
deserves no separate treatment, and no "CN servers had stricter stars" story should be
written.

### The diff between A and B — exactly one line moved

| slot | 1.4.4.1 | 2.8.0.1 | changed |
|---|---|---|---|
| 1 `TX_RS_M` | `Mission\nComplete` | `Mission\nComplete` | **no** — all 5 locales |
| 2 `TX_RS_C` | `Under 60s` | `Under 60s` | **no** — all 5 locales, same ID, same size 13, same `B_SIZE 100\|80` |
| 3 `TX_RS_T` | `All\nSurvived` | `1 Straggler\nor Less` | **YES** — all 5 locales |

Two supporting details that confirm this is a text swap inside one widget rather than a
redesign:

* `TX_RS_T` keeps **size 13** and **`B_SIZE 120|80`** in both eras; only `B_RECT`
  shifts negative (`-5|0` EN) to fit the longer string.

The stale-key argument is in §2.1.

---

## 3. When it changed

### 3.1 The dated bracket

| date | source | third condition |
|---|---|---|
| ≤ 2017-08/09 | 1.4.4.1 APK (sibling reslists 2017-09-04 / 2017-09-08) | all survive |
| **2018-12-12/13** | CN beta result screen, by eye | `全体生存` |
| **2019-08-26** | vsfan wiki `Expedition_Area`, Wayback capture | "All hunters on your team have survived." |
| **2019-10-20** | same page, second capture | *unchanged* |
| **2019-12-14** | same page, third capture | *unchanged* |
| before 2.8.0.1 | 2.8.0.1 `UI_JSON_RO.db` | `1 Straggler or Less` |

> **Bracket: the change happened after 2019-12-14 and before 2.8.0.1.**

The vsfan wording, quoted from the 2019-08-26 capture:

> You obtain stars by satisfying the following conditions when clearing an area.
> Area successfully cleared. Complete the area in the allotted time. (Time bar is shown
> on the bottom left of the battle.) **All hunters on your team have survived.**

### 3.2 The 2019-09-05 rebalance did **not** cause it

This is the check the previous lane applied to the level-cap story, applied here.

The project's hard era boundary is the 2019-09-05 rebalance
([`stat-version-context.md`](stat-version-context.md)). That announcement covers
equipment stats +50 %, crystal main stats +30 %/+50 %, all crystal substats +50 %, and
larger upgrade gains after equipment Lv.20. **It says nothing about stars.**

Independently, the vsfan page was captured **2019-10-20 and 2019-12-14** — 45 and
**70 days after** the rebalance — and still says "All hunters on your team have
survived." The page was demonstrably being maintained across those captures (11,142 →
11,152 → 11,189 B), so this is not a stale page: it was edited and the star sentence
was left alone.

**So: not the rebalance.** No patch note in any corpus recovered by this project
announces the change. It was a silent balance adjustment.

### 3.3 Instrument results that are *not* negatives

Recorded so a later agent does not repeat them:

* **namu.wiki is unreachable in this session, three ways.** Direct fetch → **403**;
  Wayback CDX → **HTTP 503** (transport fault, guard rule 18); no desktop browser
  attached. The 503 control is decisive: the *same code path* returned three clean rows
  for the vsfan URL one call earlier. **This is an instrument fault and establishes
  nothing about namu's content.** The Korean wiki was not searched.
* **vsfan.net is dead** (transport error), but its 516-page wiki is in Wayback.
  Enumerated by crawling the `url=` **prefix** form (per guard rule 17 — `matchType=domain`
  truncates), 500 + 16 rows, two requests, one session. Only **3 of 516** page titles
  concern stars/clear/conditions; `Expedition_Area` was the productive one.
* **The Google Play changelog** (`blustone.apps112.com`, controlled: the page renders
  and is dated) reaches back only to 2021-11-02 and mentions nothing about stars. A
  dated negative for **2021-11 → 2022-07** only; it says nothing about 2019-12 → 2021-11.
* **The 1.4.4.1 in-game help** (`3d98d128.json`, 157 records, 84 categories parsed) does
  **not** document the star conditions. The game never explained them in Help, in either
  era that we hold.

---

## 4. Is the condition party-size dependent?

**Yes for the old rule, no for the new one. This is the substantive balance change.**

* **Old — party-size dependent.** `팀 전원 생존` ("whole team survives"),
  `All Teammates Survived`, `全体生存`, `全隊生還`. The 2019-08-26 English guide spells
  the scope out: "**All hunters on your team** have survived." The predicate is
  *zero deaths among N party members*, so its difficulty rises with party size.
* **New — an absolute threshold.** `1 Straggler or Less`, `낙오자 1명 이하`,
  `脱落1名以下`, `落伍1名以下`, `一名以下的掉落`. Every one of the five locales is a
  **fixed number**, with no reference to team size. The predicate is *at most one
  death*, whatever N is.

So the change did two things at once: it **relaxed** the condition by one death, and it
**de-coupled it from party size**. At 1 actor the two rules coincide; at 5 actors the old
rule demanded 5/5 and the new one demands 4/5. With the 5-hunter parties the replica
uses, that is the difference between "nobody may fall" and "one may fall".

No source recovered by this lane states a scaling formula (nothing of the form
`dead ≤ f(N)`), and none should be invented.

---

## 5. The native metric, and whether the server's mapping holds

### 5.1 What the strings imply

The condition semantics map onto the client's own battle metrics, which the project
already captures in `play_info` (§16.5):

| slot | condition | implied metric |
|---|---|---|
| 1 | `TX_RS_M` mission cleared | `clear == 1` |
| 2 | `TX_RS_C` within 60 s | `clear_time < 60` |
| 3 (era A) | all survive | `dead_cnt == 0` |
| 3 (era B) | ≤1 straggler | `dead_cnt <= 1` |

**Honesty limit:** this lane established the *strings*, not the *native predicate*. It
did **not** decompile the comparison that sets order 2, and it did not prove that
`dead_cnt` is the field the star check reads. `dead_cnt` is a real native counter with
observed values 0 on wins and 1 on defeats (§21), which makes it the natural candidate,
but "natural candidate" is not "recovered". The server's mapping therefore **remains
local policy** and should keep saying so.

### 5.2 The time condition is *not* a server fixture in the way feared

Worth recording, because `Under 60s` has been treated as a chosen number:

* `TX_RS_C` **hard-codes** `60초 이내 클리어` / `Under 60s` in the **client string
  table**, identically in both eras. The star slot carries no per-stage time value from
  the server — the server only sets a byte.
* The client separately ships a **family of five thresholds plus a floor**:
  `30초 이내` / `60초 이내` / `90초 이내` / `120초 이내` / `180초 이내` and
  `180초 이상` ("More than 180 sec."), and a generic template
  `이내 클리어` → `%s 이내 클리어` / `Cleared within %s`. All five survive into 2.8.0.1.
  They are used by *other* contexts — the project's own records show an Episode list
  reading `Less than 30 sec.` — not by the campaign star slot.

So publishing 60 s **matches the label the client itself displays**. That is a
consistency win, not a coincidence, and it should be recorded as such.

### 5.3 `hp_page` — not reintroduced

No part of this analysis touches HP scaling. The star conditions are a **dead-count**
predicate over a counter, with no HP arithmetic anywhere in it. The standing warning
stands unchanged: `hp_page 100` is separate byte metadata and the proven HP/damage
functions do **not** multiply by it. Nothing here should be read as license to
reintroduce it.

---

## 6. What the server should do

1. **Change nothing.** The replica ships a 2.8.0.1 client, whose `TX_RS_T` string reads
   `1 Straggler or Less`. Evaluating order 2 as `dead_cnt <= 1`
   (`server-ts/src/progression.ts`) makes the awarded stars agree with the label the
   client is simultaneously drawing. Switching to `dead_cnt == 0` would award a star the
   client then labels wrongly. **The current default is correct and is now
   evidence-backed for the era it targets, not merely plausible.**
2. **Keep it labelled local policy** in `progression.ts` and the OpenAPI text. This lane
   recovered the *labels* and the *era bracket*; it did not recover the native predicate.
3. **Correct the "era-wrong" worry in the handoff.** `HANDOFF-to-server-agent.md` calls
   the fixtures potentially "transcribed from the first *evidence* that the star
   conditions moved". They were transcribed from the era the replica actually ships.
   The CN beta is not counter-evidence about the replica — it is a **2018-era client**.
4. **If an era-A mode is ever wanted**, it is one predicate: order 2 becomes
   `dead_cnt === 0`, and the on-screen label will still say "1 Straggler or Less" because
   the string lives in the client. That mismatch is unavoidable without an older client,
   and is a reason to leave the default alone.
5. **Do not chase a patch-note story.** Nothing in the recovered Google Play changelog,
   the VSFan wiki, or the 1.4.4.1 help announces this change. It was silent. Record it as
   a silent balance change in the `(2019-12-14, 2.8.0.1)` window and move on.
6. **The Korean wiki remains genuinely unsearched** (403 / 503 / no browser). A future
   agent with a working browser could still find a dated Korean patch note and close the
   bracket. That avenue is **open, not closed**.

---

## 7. Coverage and honesty summary

* **Coverage counters unmoved: heroes 1/113, accessories 1/100, monsters 0/22.**
  Nothing here is a hero, accessory or monster statistic. `Battle Clear` /
  `Straggler` / `全体生存` are UI strings.
* **Nothing appended to `polluted-observations.md`.** `coverage.md`, every TSV,
  `server-ts`, fixtures, the APK, seeds, the emulator, the phone and Ghidra were **not
  touched**. This note is read-only research plus one new file.
* **Sources are original bytes, not hearsay.** The 1.4.4.1 strings were re-extracted from
  the APK in this lane and checked byte-identical against the pre-existing copy; the
  2.8.0.1 strings come from the project's own recovered LevelDB; the CN frame was read
  by eye at 5×; the vsfan wording comes from three dated Wayback captures.
* **The one thing not established** is the exact native predicate and the exact patch.
  Both are stated as open rather than filled in.
