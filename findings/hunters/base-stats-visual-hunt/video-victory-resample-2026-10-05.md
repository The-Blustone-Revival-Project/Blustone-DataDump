# Victory / rating video resample — 2026-10-05

**Lane:** close the two OPEN negatives in `result-screens-2026-10-05.md` —
"Errorflame `9fUxOnlmwxg` … victory *ratings* seen but no legible gold/XP
numerals" and "Ryu33s `8fEo7cb7fTk` … post-match team-rating cards at
02:00/04:40/06:30/08:20, no individual payout numerals".
**Both negatives are falsified.** 12 expedition victory receipts and 4 Fight
Club rating cards were recovered at native resolution, plus 6 campaign/economy
frames and 5 Fight Club HUD/dialog frames.
**Read-only:** no server, APK, state, emulator or account action. All video
work happened in a disposable temp dir
(`%TEMP%\opencode\vresample`); nothing but this report and the
`polluted-observations.md` append was written into the repo.

Tag convention is inherited: **Section 1 = PURE** (frames transcribed
verbatim with URL + absolute timestamp), **Section 2 = UNPURE** (polluted /
state-ambiguous, `polluted-observations.md` ledger). **No coverage change** —
nothing below is a base hero/monster/accessory/jewel tuple.

---

## 0. Why the earlier pass read "no legible numerals" — three independent causes

The previous result was not a property of the videos. Three separate sampling
defects each produced it, and the third is the dangerous one.

| # | Defect | Evidence |
|---|---|---|
| 1 | **Resolution.** Only the 240p progressive rendition (itag 134, **202×360**) had ever been downloaded. YouTube's format list for `9fUxOnlmwxg` tops out at itag **312 = 608×1080 @52fps**. At 202 px wide the result-screen numerals are ~4 px tall and genuinely unreadable. | `yt-dlp -F` on 2026-10-05: `311 406x720`, `312 608x1080`; the local copy used before was `202x360` 26 fps 30.69 MB. |
| 2 | **Sampling interval.** Result screens are on screen **4–6 s**. The earlier pass sampled every **10 s** (Ryu33s) / **20 s** (Errorflame). At 20 s intervals the chance of landing inside any given 5 s window is ~25%. | 12 distinct result screens exist in a 30.5 min video; 20 s sampling yields ~91 samples. |
| 3 | **Animated counters.** `Collected Rupees`, per-hunter `Power`, and `Received ×N` all **count up** over ~1.5 s before settling. A frame taken inside the animation reads the *initial* `0`, not the payout. | V01 reads `+ 0` at 00:02:20, `+ 26` at 00:02:20.5, `+ 49` at 00:02:21. The training receipt reads `377 → 377, →385, →399, →413, →428, →443, →458, →473, →503`. The map popup reads `×1996` at 00:19:25 and `×3000` at 00:19:26. |

**Defect 3 is the one to remember.** A coarse sampler reliably lands on a
mid-animation frame and reports a payout of **0** — a *positive-looking* result
that is simply wrong. Any future numeric frame read must state whether the
counter had settled.

### 0.1 New method actually used

1. Downloaded/located a **full-length low-res copy** as a time-accurate
   reference (`blustone-episode1-9fux.mp4`, 202×360, 1831.97 s;
   `ryu-ref360.mp4`, 640×360, 605 s).
2. Built **1 fps contact sheets over the whole runtime** to *locate* every
   result screen (13 sheets for Errorflame, 2 s interval for Errorflame to
   halve the count, 1 s for the dense re-check of one window).
3. Downloaded a **22 s native-resolution window** (`itag 312`, 608×1080 for
   Errorflame; `itag 299`, 1920×1080 for Ryu33s) around each located screen.
4. Extracted the **settled** frame at native resolution, cropped to the
   readable band, upscaled 2×, and transcribed.

### 0.2 `--download-sections` offset hazard (tooling finding, keep this)

YouTube serves DVR-style HLS manifests (`playlist_type=DVR`, `dove`, `short_key`).
On those, `yt-dlp --download-sections` hands ffmpeg `-ss <t>`, and **ffmpeg's
seek lands late by an amount that varies per invocation.**

Two invocations of the *identical* window `*00:02:08-00:02:30`:

| invocation | actual content start | offset |
|---|---|---|
| A | 00:02:08 (mid-battle, `2424` damage frame) | **0.00 s** |
| B | 00:02:40 (the Area 3 result screen) | **+12.40 s** |

Proved by 3-way frame comparison (clip frame 0 vs reference at 128 s vs
reference at 140 s) — clip B frame 0 is pixel-for-pixel the reference at
**140 s**. Measured offsets over the 12 Errorflame clips:
**+0.04 s ×9, +1.80, +3.16, +4.96, +8.36**; over the 4 Ryu33s clips:
**+0.00 ×4**.

**Every absolute timestamp below is offset-corrected** by grayscale-signature
alignment against the full-length reference (coarse 5 fps MAD search, then
25 fps refine), never by trusting `-ss`. Alignment margins are strong
(Errorflame fine-MAD 8.1–9.5 vs 9.2–11.3 runner-up; Ryu33s 1.42–1.61 vs
1.64–1.90). Residual timing uncertainty is ±0.04 s on the grid plus the
frame-sampling interval, i.e. **±1 s** for any row below.

---

# Section 1 — PURE (verbatim frames, URL + timestamp)

## 1.1 Sources

| Key | URL | Title / channel | Upload | Runtime | Rendition used |
|---|---|---|---|---|---|
| **ERR** | <https://www.youtube.com/watch?v=9fUxOnlmwxg> | *Blustone episode 1 ( I have no clue what to call this )* — Errorflame gamer | 2017-12-15 | 1831.97 s | itag 312, **608×1080**, 52 fps |
| **RYU** | <https://www.youtube.com/watch?v=8fEo7cb7fTk> | *Blustone - Playing with Twins&Windlade* — Ryu33s | 2020-09-09 | 605 s | itag 299, 1920×1080 (game drawn into a **504 px-wide** portrait strip, letterboxed left/right) |

## 1.2 Expedition victory receipts — 12 screens, ERR

Every screen is the standard campaign result: header area name, three star
slots, `Victory!`, `Team Level N` + progress bar, up to four party slots with
per-hunter `Lv. n` + `Power`, `Collected Rupees`, `Collected Items`, and
`Retry` / `Next Area`.

All 12 print the **settled** `Collected Rupees` value and a **3-of-3 or 2-of-3**
star outcome.

| # | Timestamp (ERR) | Header | Team Lv | Party slots as printed | `Collected Rupees` | `Collected Items` | Stars | Buttons |
|---|---|---|---|---|---|---|---|---|
| **V01** | **00:02:21 – 00:02:22** | `Unknown Snowfields` / `Area 3` | 1 | 1 hunter, `Lv.5`, power **321**, 3 empty slots | **+ 49** | *(row present, empty)* | 3/3 | `Next Area` |
| **V02** | **00:07:08 – 00:07:11** | `Midgard Snowfields` / `Area 1` | 1 | 2 hunters, both tagged `Lv. Up!`, powers **328** and **179**, 2 empty | **+ 53** | 1 green item **×3** | **2/3** (slot 3 label `All Teammates Survived`, unlit) | `Retry` `Next Area` |
| **V03** | **00:08:20 – 00:08:21** | `Midgard Snowfields` / `Area 2` | 1 | 2 hunters, powers **335** and **183**, both `Lv. Up!`, 2 empty | **+ 58** | 3 items, **×1 ×1 ×1** | 3/3 | `Retry` `Next Area` |
| **V04** | **00:09:44 – 00:09:46** | `Midgard Snowfields` / `Area 3` | 1 | 2 hunters `Lv.8` **342**, `Lv.4` **187**, 2 empty | **+ 58** | 1 blue-crystal item **×2** | 3/3 | `Retry` `Next Area` |
| **V05** | **00:12:58 – 00:12:59** | `Midgard Snowfields` / `Area 4` | 1 | 3 hunters, powers **349**, **191**, **761**, 1 empty | **+ 57** | 2 items, **×1 ×1** | 3/3 | `Retry` `Next Area` |
| **V06** | **00:14:13 – 00:14:14** | `Midgard Snowfields` / `Area 5` | 2 | 3 hunters, first tagged `Lv. Up!`, powers **363**, **199**, **770** | **+ 55** | 2 items, **×1** and **×2** | 3/3 | `Retry` `Next Area` |
| **V07** | **00:19:20** | `Midgard Snowfields` / `Area 6` | 2 | 3 hunters `Lv.12` **370**, `Lv.8` **203**, `Lv.4` **779**, 1 empty | **+ 55** | 1 blue-crystal item **×1** | 3/3 | `Retry` `Next Area` |
| **V08** | **00:21:01 – 00:21:02** | `Midgard Snowfields` / `Area 7` | 2 | 3 hunters, powers **377**, **207**, **798** | **+ 57** | 1 item **×1** | 3/3 | `Retry` `Next Area` |
| **V09** | **00:23:47 – 00:23:49** | `Midgard Snowfields` / `Area 8` | 2 | 3 hunters, all tagged `Lv. Up!`, powers **752**, **214**, **807** | **+ 61** | 1 item **×2** | 3/3 | `Retry` `Next Area` |
| **V10** | **00:24:44 – 00:24:47** | `Midgard Snowfields` / `Area 1` *(see §2.5 — header literally reads `Area 1` at Team Level 3)* | 3 | 3 hunters `Lv.3` **761**, `Lv.12` **218**, `Lv.8` **816**, 1 empty | **+ 52** | 1 orange/brown item **×3** | 3/3 | `Retry` `Next Area` |
| **V11** | **00:26:23 – 00:26:24** | `Midgard Snowfields` / `Area 9` | 3 | 3 hunters, first tagged `Lv. Up!`, powers **779**, **222**, **835** | **+ 56** | 2 items, **×2** and **×2** | 3/3 | `Retry` `Next Area` |
| **V12** | **00:28:10 – 00:28:14** | `Midgard Snowfields` / `Area 10` | 3 | 3 hunters, powers **789**, **230**, **844** | **+ 61** | 2 items, **×2** and **×1** | 3/3 | `Retry` `Next Area` |

**Also printed on these screens (ERR, 00:02:21–00:02:22 at ~50 % scale, and
corroborated by V02's slot-3 label at native scale):** the three star-condition
captions read **`Mission Complete`**, **`Less than 60 sec Clear!`**,
**`All Teammates Survived`**. Wording is **medium confidence** — first read from
a 300-px-wide re-render, not a native-scale crop; the slot-3 string was
re-confirmed natively on V02.

**`Collected Rupees` value set across 12 campaign clears (ERR):**
`49, 53, 58, 58, 57, 55, 55, 57, 61, 52, 56, 61`.
Arithmetic mean 56.4, min 49, max 61, spread 12 across nodes 1–10 and across
both an untrained and a trained party. See §2.1 for what may **not** be
concluded from that.

## 1.3 Team-level and reward receipts — ERR

| Key | Timestamp | Verbatim |
|---|---|---|
| **B1** | **00:14:15 – 00:14:16** | `TEAM LEVEL UP` / `Lv. 2` / `- Level Up Bonus -` **[red fuel icon] `×30`** / `You are one step closer to becoming the top hunter.` / `Okay` |
| **B2** | **00:24:43 – 00:24:44** | `TEAM LEVEL UP` / `Lv. 3` / `- Level Up Bonus -` **[red fuel icon] `×30`** / `- New Area Unlocked -` **`Midgard Ice Zone`** |
| **B3** | **00:19:25** | `Received` shield, gold rupee **`× 1996`** *(mid count-up — do not cite)* |
| **B3b** | **00:19:26 – 00:19:27** | same shield, gold rupee **`× 3000`**, `Congratulations`, `Okay` |
| **B4** | **00:23:54** | same shield, blue item **`× 20`**, `Congratulations`, `Okay` |
| **B5** | **00:14:25 – 00:14:26** | `Episode` screen, `Clear the Expedition Area and receive a new episode!` — row 1 greyed with red overlay **`Midgard Snowfields Area 7 Clear!`**; row 2 **`2. What's a Metron Worth?`** / `Less than 30 sec.` / red `N` ribbon; row 3 **`1. What Should Metron Hunter Do?`** / `Less than 30 sec.` / red `N` ribbon; bottom bar list icon **`2`**, two chest icons **`10`** and **`20`** |
| **B6** | **00:16:00 – 00:16:03** | item popup `Rupee` / **`Current Amount 482`** / `A single, shiny coin and the main currency of all the tribes.` / `Areas Available` → `Purchase Manda` (`Move >`) |
| **B6b** | **00:16:02 – 00:16:03** | item popup `Rupee Lottery Ticket` / **`Current Amount 0`** / `A lottery ticket issued by the Hunter Union. If the winner of the lottery receives a large amount of rupees.` / `Areas Available` → `All Midgard Areas` (`Move >`) |
| **B7** | **00:16:00 – 00:16:06** | `Hunter Supply Office` / tab `Attendance Supply` / `Daily Points` / `Receive 20 Veteran Points per attendance day.` / `Day` row: rupee **`×3000`** with `Accept`, then `Available in 1 day`, `Available in 2 days`, `Available in 3 days`; second row `Available in 6 days`, `Available in 7 days`, `Available in 8 days` / `Cumulative Attendance Dates:` / **`Day 0/20`** / `Day 5` `Day 10` `Day 15` `Day 20` with `2` and `Accept` / `Veteran Level` **`Unknown`** + `Veteran Points` **`0/20`** |
| **B8** | **00:17:52 – 00:17:56** | `Assignments` / `Daily Goals`: `Bonus Goal Reward` **`0/7`** with rewards **`×1` `×1` `×1` `×20`** and `Receive`; `Check In` **`Complete`** → **`×1000`**; `Clear Areas` **`6/15`** ("Clear Expedition Areas 10 times!") → **`×30`**; `Receive Supplies` **`1/2`** → **`×30`**; footer `Veteran Level` **`Beginner 1`**, `+ Veteran Points` **`20/40`**. `Assignments` / `Major Goals`: `Bonus Goal Reward` **`1/7`**; `Receive Supplies` `1/2` → **`×10`**; `Recruit Hunters` **`1/2`** → **`×1`**; `Buy Item` `0/1` → **`×1000`**; `Train Skills` `0/3` → **`×10`**; `Challenge` `0/3` → **`×20`**; `Receive Fuel Supplies` **`BONUS!`** ("Receive 100 more fuel everyday with the Fuel Package!") → **`×30`** |
| **B8b** | **00:17:55** | `Received` shield, gold rupee **`× 1000`**, `Congratulations`, `Okay` — the `Check In` payout |
| **B9** | **00:22:13 – 00:22:16** | `Amateur Hunter` / **`Power Upgraded  377  →  503`** (count-up sampled at `377, 385, 399, 413, 428, 443, 458, 473`, settling on **503**) |
| **B10** | **00:22:55 – 00:22:56** | `Advancement Successful` / **`Amateur Hunter  503  →  Novice Hunter  743`** / `New Skill Unlocked` / `Increased Chance of Defense` / `You have advanced to a greater level!` / `Okay` |
| **B11** | **00:22:59 – 00:23:01** | `Train Teammate` / `Captain` **`errorfrost`** / **`Strength 743`** / title `Novice Hunter` / **`Lv. 7`** / buttons `Train`, `Transcendence`, `Skill Training`, `Upgrade Equipment`, `Story` / NPC line `Whoa... Captain! I think you've gotten much stronger!` |
| **B12** | **00:08:30** | `Ready to Battle` / `Midgard Snowfields - Area 3` / fuel **`102/60`** with `+` / **three empty stars** / `Available Items` with 4 item icons / ally side: hunter `Lv. 7` with a red **`1st`** badge and a **Bomber** role icon, hunter `Lv. 3` with a **Support** role icon, 2 empty `+` slots / `Ally Teammates` **`VS`** `Opponent Teammates` / opponent side: a penguin (blue element dot), a brown beast (Bomber role icon), a grey owl (blue element dot) |
| **B13** | **00:19:26** (slightly later frame of B3b) | `Midgard Snowfields` map: nodes **`10`** and **`9`** locked (grey), **`8`**/`7`/`6`/`5`/`4`/`3` each showing **three gold stars**, fuel **`153/60`** with `+` |

## 1.4 Fight Club team-rating cards — RYU

**Four** distinct opponents fought the same player inside one 10 min video.
Each card prints the opponent (red, top) and the player (blue, bottom) with
**`Strength`**, **`Point ×N`** and **`Rank`**.

| Key | Timestamp (RYU) | Opponent (red) | Player (blue) |
|---|---|---|---|
| **R1** | **00:01:52 – 00:01:54** | name **`Ramenman`**, subtitle **`Tonkotsu`**, **`Strength 186529`**, **`Point × 1593`**, **`Rank 89`** | name **`Ryuichiツ`**, **`Strength 129507`**, **`Point × 1459`**, **`Rank 115`**, portrait badge **`99`** |
| **R2** | **00:04:34 – 00:04:36** | name **`Graf`**, motto **`I'm here for TC (Tournament of Chaos all year!)`**, **`Strength 163578`**, **`Point × 1531`**, **`Rank 100`** | name **`Ryuichiツ`**, **`Strength 139610`**, **`Point × 1489`**, **`Rank 110`** |
| **R3** | **00:06:23 – 00:06:25** | name **`TayOtaku`**, subtitle **`Norn`**, **`Strength 170371`**, **`Point × 1694`**, **`Rank 73`** | name **`Ryuichiツ`**, **`Strength 135191`**, **`Point × 1504`**, **`Rank 107`**, portrait badge **`99`** |
| **R4** | **00:08:13 – 00:08:15** | name **`HeroKing`**, motto **`I'm gonna be the king, so don't stand in my way!`**, **`Strength 139135`**, **`Point × 1722`**, **`Rank 70`** | name **`Ryuichiツ`**, **`Strength 141249`**, **`Point × 1520`**, **`Rank 102`**, portrait badge **`99`** |

**This is the strongest single result of the resample.** The same player's four
cards, in video order, give:

| | R1 00:01:52 | R2 00:04:34 | R3 00:06:23 | R4 00:08:15 |
|---|---|---|---|---|
| `Strength` | 129507 | **139610** | **135191** | 141249 |
| `Point` | 1459 | 1489 | 1504 | 1520 |
| `Rank` | 115 | 110 | 107 | 102 |

`Point` is **strictly increasing** (+30, +15, +16) and `Rank` is **strictly
improving** (115 → 110 → 107 → 102, a falling number) across all four cards,
while `Strength` is **not monotone** (it dips at R3). Therefore:

- **`Point` + `Rank` are the account ladder pair** — the pair the local replica
  would have to model as one currency and one ordinal.
- **`Strength` is a separate party/roster rating**, not the ladder value, and
  must never be substituted for either.

This corrects a tempting misreading: the three-card subset quoted earlier in
this file looked monotone in all three fields, which would have wrongly implied
`Strength` is the ladder. The fourth card falsifies that. Opponent `Strength`
is likewise uncorrelated with opponent `Rank` (186529/89, 163578/100,
170371/73, 139135/70).

## 1.5 Fight Club battle HUD and dialogs — RYU

| Key | Timestamp (RYU) | Verbatim |
|---|---|---|
| **H1** | **00:06:34 – 00:06:43** | Opponent camp HP readout counting down across samples: **7480 → 7383 → 7260 → 7163 → 7066 → 6968 → 6869 → 6793 → 6772** (single 4-digit figure, presented with a space between the leading pair and trailing pair) |
| **H2** | **00:06:34 – 00:06:43** | Per-actor HP figures: **8250**, **7963**, **8238**, **8420**, **8336**, **8596**, **6496**, **6332**; actor levels **46**, **46**, **85**; damage pops **161**, **161**, **133**, **148**; `FEVER!` gauge; `TAP` and `×1` |
| **H3** | **00:06:44 – 00:06:49** and **00:08:26 – 00:08:30** | bet prompt **`Which side are you choosing to bet?`** with a coin icon and a dial of selectable counters **1 2 3 4 5 6** |
| **H4** | **00:06:43** | comparison popup `Attack▼` / `Defense▼` with **`DEF DOWN!`** |
| **H5** | **00:06:23** onward | opponent taunt line **`Alia can do it!`** (H5 text visible at 00:08:26 as a speech bubble) |
| **H6** | **00:08:31 – 00:08:33** | pause dialog **`Paused`** / **`Resume`** / **`Forfeit Game`** |
| **H7** | **00:08:26 – 00:08:31** | opponent camp HP readout: **7392 → 7291 → 7192 → 7094 → 6974 / 6973**; damage pops **97**, **83**, **129**; turn counter **1 2 3 3** |
| **H8** | **00:04:46 – 00:04:53** | opponent camp HP readout: **7410 → 7391 → 7283 → 7184 → 7083 → 6984 → 6889 → 6783**; damage pops **21**, **16**, **107**, **102**, **102**, **152**, **56**; `FEVER!` then `SUPER!!`; turn counter **2 3 3 4 4 4**; taunt bubble **`Why bootstrapping allows certain… Huh? I like that!`** |

---

# Section 2 — UNPURE (polluted; appended to `polluted-observations.md`)

Everything in Section 2 is a **polluted / state-ambiguous** observation. None
of it is a base stat, and none of it changes the 70% thresholds in
`coverage.md`.

## 2.1 `Collected Rupees` = 49–61 on 12 campaign clears — era-sensitive, one account

Raw set (ERR, 2017-12-15 build): `49, 53, 58, 58, 57, 55, 55, 57, 61, 52, 56, 61`.

What is **observed**: the payout sits in a narrow band across ten different
stages and across a party whose power more than doubled between V02 and V10.

What is **NOT** concluded:
- **Not a per-stage table.** Nodes 1–10 all land in the same band, and the two
  lowest values (49, 52) are the *tutorial* stage and a *repeat* clear — not
  the low stages generally.
- **Not a power-independent constant.** One account, one party, one session.
- **Not comparable to the FAQ Search payouts** (`+1400`, `+2000`) in
  `result-screens-2026-10-05.md` — different mode, and per §77 the 2019-09-05
  rebalance moved equipment/crystal stats, so rupee balance may also have moved
  between 2017-12 and the FAQ capture. **Stratify by era; do not merge.**
- **No fixture retune is authorized.** The local replica's 10-gold / 30-XP
  first-clear values are unaffected by this; nothing here validates them.

## 2.2 `Lv. Up!` and party `Power` on the result screen — progression, not base stats

`Power` per party slot is a **post-combat rating**, not a base stat: it visibly
animates upward within the same screen (V02 `321 → 327 → 328`;
V04 `335 → 347 → 342`; V05 `342 → 349`) and is tagged `Lv. Up!` when a level-up
occurred. Slot occupancy grows from 1 (V01) to 2 (V02–V04) to 3 (V05+), and the
values run 176–844 while Team Level runs 1 → 3.

**Level floors are not pinned.** V07 prints `Lv.12 / Lv.8 / Lv.4` beside powers
`370 / 203 / 779` and V10 prints `Lv.3 / Lv.12 / Lv.8` beside `761 / 218 / 816`
— i.e. a `Lv.12` hunter sits at power 218 while a `Lv.4` hunter sits at 779 in
the *same* party. Level and rating are **independent**; the pair is a
`rating / level` ordering by descending rating, not by level.

## 2.3 Team Level 1→3, `Level Up Bonus ×30`, `Midgard Ice Zone` unlock

B1/B2 print `TEAM LEVEL UP / Lv. 2` and `Lv. 3` with an identical
`- Level Up Bonus - ×30` on a **red fuel-can icon**, and B2 adds
`- New Area Unlocked - Midgard Ice Zone`. The icon is the same red can used
for the fuel meter (`102/60`, `153/60`) and for `Top up the Hunting Ship!` in
the village, so **`×30` reads as 30 fuel**, but the icon-to-currency crosswalk
is an inference from shape, not a labelled value. This is a **Team-level**
bonus, distinct from the per-hunter and per-Account `Lv. n` scales; do not fold
the three together.

## 2.4 B9/B10/B11 — one hunter's Raise then Advancement chain

`377 → 503` (`Power Upgraded`, ordinary training) then `503 → 743`
(`Advancement Successful`, `Amateur Hunter → Novice Hunter`, `New Skill
Unlocked: Increased Chance of Defense`), ending on a `Train Teammate` panel at
**`Lv. 7` / `Strength 743`**.

Fodder, equipment, jewels and comparison semantics are all unstated in these
frames, and the `377` baseline is a *trained* hunter, not a base one. **No
count as a base stat**; keep as a progression anchor. Note the resulting
`Lv. 7` after advancement is *lower* than the pre-advancement `Lv. 12` seen in
V07/V10, which is consistent with the community-documented 3★ Lv.30 → higher-
grade Lv.1 reset but does **not** prove it from this frame.

## 2.5 V10 header reads `Midgard Snowfields - Area 1` — sequence anomaly, unresolved

V10 (00:24:46) prints `Midgard Snowfields - Area 1` at **Team Level 3** with a
party of `Lv.3/Lv.12/Lv.8`, immediately after V09 cleared `Area 8`, and its
`Team Level Up / Midgard Ice Zone` popup fires 3 s later. The natural reading is
a **repeat clear of node 1 with a now-trained team**, but that is an inference.
The header text is transcribed verbatim and the anomaly is **left unresolved**;
do not renumber the area, and do not use V10 as evidence of an Area-1 payout
distinct from the first clear.

## 2.6 Fight Club `Strength` / `Point` / `Rank` — a rating triple, and `Strength` is *not* the ladder

`Strength` here is a **party rating**, not a hero stat: it is ~129 000–187 000,
five to six orders of magnitude above hero HP. Across the same player's four
cards `Point` and `Rank` move monotonically while `Strength` does not (§1.4), so
`Strength` must not be read as the ladder value and must not be substituted for
`Point`/`Rank`.

`Strength` is the **same field family** as the `Strength`/`Team Strength`
labels already grounded in `UI_CSV/7adedb12.txt` (`TX_LI_TG2`, `TX_CH_TL`,
`TX_POWER`) — which is what lets the Reddit `13`/`12` Offense/Defense Strength
lists, the Naver `55/114` roster and the AppStorio `19/102` list be treated as
*rating* columns rather than HP/ATK/DEF. **That inference is strengthened; no
individual screenshot's field assignment is resolved.**

The four-point `Point` series `1459, 1489, 1504, 1520` is a **single account's
Point total**, not a per-match award — the card prints the *pre-match* standing
and the deltas (+30, +15, +16) are not attributable to any one match without the
settlement screen, which is **not** in any of the four windows. **No Point
award per win/loss may be inferred.**

The portrait badge **`99`** repeats on three cards at an unknown semantic level
(captain marker, pet, or level). The opponent subtitles `Tonkotsu` / `Norn` and
mottos are unlabelled text under the name; `Norn` also appears as a mid-map name
on ERR (B7/B13), so it may be a companion/captain name rather than a guild.
`Graf`'s motto expands `TC` as `Tournament of Chaos`, i.e. a ladder-season name.
**Unresolved.**

## 2.7 Fight Club opponent HP `7480 → 6772` — opponent-camp bar, not a monster

H1/H7/H8 show a 4-digit value in the **thousands** decreasing over ~9 s against
`161`/`97`/`83`/`152` damage pops, with per-actor values `8250`, `7963`, `8238`,
`8420`, `8336`, `8596`, `6496`, `6332`, `7897`, `7668`, `7467`, `7240`, `7099`,
`6911`, `6779`, `6761`, `5503`, `5360`, `5156`, `5091` and actor **levels 46 /
46 / 85**. Levels in the 40s–80s are far outside the 1–30 community band, which
is a **second, independent reason** not to treat these as `048`-style campaign
monsters. This is the **opponent's party**, i.e. PvP combatants whose stat
source is unknown.

**Do not** cross-assign these to any recovered monster or hero row, and do not
count toward monster coverage (still **0/22**). Recorded in
`monster-hud-observations.md`'s sibling ledger, not in base coverage.

## 2.8 Betting, forfeit, taunts — new Fight Club UI surface

`Which side are you choosing to bet?` with a 1–6 counter dial, `Paused /
Resume / Forfeit Game`, `Attack▼ / Defense▼` with `DEF DOWN!`, and the taunt
`Alia can do it!` are **newly visible original Fight Club UI**. They matter for
`analysis/research/fc-native.md` and `fc-economy-2026-10-05.md`, which
documented parser shapes but no bet/forfeit surface. **No wager amount is
printed in these frames** — the counter is a slot selector, not a sum; do not
read a price from it.

## 2.9 Episode list conditions — `Less than 30 sec.` and an area gate

B5 prints two `NEW` episode rows with the condition `Less than 30 sec.` and one
locked row gated on `Midgard Snowfields Area 7 Clear!`, plus a bottom bar with
`2` / `10` / `20`. This corroborates `UI_CSV/e44ab8ed.txt` key
`30초 이내'` (`Less than 30 sec.`) recovered in the polluted ledger, and adds
an **Episode-mode star-condition wording plus a stage-clear prerequisite** that
is directly relevant to the project's Episode work. It does **not** establish
the `>=180 sec.` half of that table, nor any Episode reward amount.

## 2.10 Attendance / daily-goal amounts — economy, era-sensitive

`Day 0/20`, `Receive 20 Veteran Points per attendance day`, day-1 reward
**`×3000`**, `Day 5/10/15/20` **`×2`**, `Veteran Level Unknown → 0/20`;
daily goals `Check In ×1000` (paid out at 00:17:55), `Clear Areas 6/15 ×30`,
`Receive Supplies 1/2 ×30`, `Recruit Hunters 1/2 ×1`, `Buy Item 0/1 ×1000`,
`Train Skills 0/3 ×10`, `Challenge 0/3 ×20`, `Receive Fuel Supplies BONUS! ×30`
(whose description reads `Receive 100 more fuel everyday with the Fuel Package!`);
`Rupee Current Amount 482`, `Rupee Lottery Ticket Current Amount 0`.

Two caveats: the `×N` glyphs carry **currency icons whose exact currency is not
always labelled** (only the `Check In ×1000` receipt proves a rupee payout), and
all of it is a **single account at one moment**. These do **not** validate the
replica's `local_fuel_0 / AP10` or `100-gold calendar` fixtures, which remain
fixtures.

## 2.11 B12 — role icons corroborate the recovered enum, at low resolution

B12 shows role glyphs beside party slots: a **fire** glyph on `Lv. 7` and a
**rabbit** glyph on `Lv. 3`, plus a **brown beast** opponent carrying the same
fire glyph. Read at native resolution but small, this is **medium confidence**.
If correct it corroborates `analysis/research/card-enums.md`
(1 Offense, 2 Defense, 3 Bomber, 4 Support) by shape. **Not upgraded to
RECOVERED** — no native string crosswalk was done for these glyphs in this pass.

---

## What this changes / does not change

**New (Section 1, RECOVERED-video-frame at native resolution):**
- **12 expedition victory receipts** with settled `Collected Rupees`
  (`49, 53, 58, 58, 57, 55, 55, 57, 61, 52, 56, 61`), star outcomes
  (11× 3/3, 1× 2/3), Team Level progression **1 → 2 → 3**, per-hunter
  `Lv. n` + rating, and item counts.
- **2 `TEAM LEVEL UP` receipts** (`Lv. 2`, `Lv. 3`) with `Level Up Bonus ×30`
  and the **`Midgard Ice Zone`** unlock.
- **2 `Received` payouts** (`×3000` rupee, `×1000` rupee from Check In) and one
  `×20` item.
- **One Raise + one Advancement chain** (`377 → 503`, `503 → 743`).
- **3 Fight Club team-rating cards** (6 `Strength`, 6 `Point`, 6 `Rank` values)
  and **1 `Ready to Battle`** star/fuel row (`102/60`, three empty stars).
  *(Superseded during this pass by four cards — see §1.4 — 8 `Strength`,
  8 `Point`, 8 `Rank`, and the `Point`/`Rank` = ladder, `Strength` ≠ ladder
  split.)*
- **New Fight Club surface**: bet prompt + 1–6 dial, `Paused/Resume/Forfeit
  Game`, `Attack▼/Defense▼` + `DEF DOWN!`, taunt text.
- **Episode-mode condition wording** (`Less than 30 sec.`) and a stage-clear
  prerequisite (`Midgard Snowfields Area 7 Clear!`).

**Not changed:**
- **Strict hero / monster / accessory / jewel coverage is untouched.** No base
  tuple was recovered. Hero remains **1/113**, monster **0/22**, accessory
  **1/100**, jewel instance **1/100**. The Fight Club `7480 → 6772` figure is
  explicitly *not* monster coverage (§2.7).
- **No local fixture is validated or retuned.** The 10-gold / 30-XP / 10-char-EXP
  clears, the 100/800/900/5000/12000/50000 gold costs, the 100-gold calendar
  and the Search 1/10-trace rules are all untouched; these frames are a single
  2017 account and in several cases **contradict** the fixtures.
- **Era is not resolved.** ERR is a **2017-12-15** upload and RYU a
  **2020-09-09** upload; per `stat-version-context.md` the 2019-09-05 rebalance
  sits between them, and per `result-screens-2026-10-05.md` the FAQ's
  post-2019-04-01 ruins change is a third boundary. **Never merge ERR, RYU and
  FAQ economy rows into one table.**

**Method, worth carrying forward:**
1. Never sample a numeric HUD at coarse intervals — the counter animates, and
   you will record `0`.
2. Always check the rendition list before declaring a video illegible; a
   202-px-wide copy cannot resolve HUD text that a 608-px copy reads at a glance.
3. **`yt-dlp --download-sections` on YouTube DVR-HLS manifests lands late by a
   per-invocation amount (0–12.4 s measured).** Align every clip against a
   full-length reference before quoting an absolute timestamp.

**Residual gaps:**
- **No Fight Club settlement/award screen was captured.** All four windows
  contain the pre-match card and live combat but no post-match result panel, so
  the `Point` deltas (+30, +15, +16) remain unattributed and no per-win award
  is established. This is the one piece of the original "post-match" wording in
  the prior note that is **still** unresolved.
- No **star-condition wording** was captured at native scale for all three
  conditions (§1.2 caveat).
- No **monster max HP/ATK/DEF** and no **hero HP/ATK/DEF** was recovered; the
  Fight Club figures are opponent ratings, not stats.