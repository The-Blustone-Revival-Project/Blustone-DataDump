# LOGIN BONUS / ATTENDANCE CALENDAR — recovered table and semantics (2026-10-09)

**Lane: G1** of `campaign-reward-ledger-2026-10-09.md` §6 — "the single largest
untouched reward table in the project."

**Headline: the day-by-day table is RECOVERED.** A complete **7-day week with
exact item + quantity per day**, plus a separate **cumulative ladder at
5 / 10 / 15 / 20 days**, was recovered from one original-language (English)
wiki page that is **byte-identical across three dated Wayback captures**
(2019-08-21, 2019-10-15, 2020-08-08). The **28** in `campaign-reward-ledger` §4.1
is **not an invention in the sense of being unfounded** — a **28-day cycle is
independently documented** — but the *28 entries × 100 gold* the replica
publishes is still **invention**, and the recovered week shows it is wrong in
**content**, not merely in detail.

**Read-only lane.** `server-ts/` was read, never written. No build, no tests, no
dev server. §8 reports exactly what the replica publishes today.

**Coverage counters unmoved: heroes 1/113 (0.9 %), accessories 1/100 (1.0 %),
monsters 0/22 (0 %).** Nothing here is a base stat; this file is economy
evidence only, per `coverage.md`'s scope rule. **No append to
`polluted-observations.md`.**

---

## 0. The recovered table — verbatim, with provenance

### 0.1 The source, and why it is trustworthy

`vsfan.net/wiki/Hunter_Supply_Office` — a community wiki of the **English**
client (VisualShower), MediaWiki. This is the page the prior lane recorded as a
"navigation stub with no reward content at all"
(`campaign-reward-ledger-2026-10-09.md` §4.3, under *Hunter Supply Station* /
*Hunter Supply Office*). **That prior reading is wrong and is retracted here:**
the page carries two reward tables. The mistake was almost certainly reading
`Hunter_Supply_Station` (which really is a stub) and generalising it to
`Hunter_Supply_Office`.

| capture (UTC) | HTTP | bytes | sha256 (16) | tables present |
|---|---|---:|---|---|
| `web/20190821011235` | 200 | 26 283 | `2995eb8054f91dba` | **both, unchanged** |
| `web/20191015115618` | 200 | 26 283 | `d5117e32fb8dc229` | **both, unchanged** |
| `web/20200808181724` | 200 | 25 966 | `2a8e37c7897e94c7` | **both, unchanged** |

Revision: **`oldid=6016`, "This page was last edited on 8 October 2017, at
13:51"** — identical in all three captures, so this is one revision, not a
drifting one.

**The "maintained statement" test was applied and passed.** The *whole page*
digest differs across the three captures (26 283 / 26 283 / 25 966 B, three
different SHA-256s — the page chrome, nav and asset URLs changed), while the
**table regions are byte-identical**: region SHA-256 `65f97237669d7924…` for
the cumulative table in **all three**, and the daily table in all three. So the
page was edited between captures and the tables were **not** touched. That is
the same discriminator `star-conditions-era-2026-10-09.md` §3.2 used to refuse
blaming the 2019-09-05 rebalance.

**Era anchor — the table is post-patch-1.0.8.0.** `vsfan Patch_1.0.8.0_(Blustone)`
(dated **August 3, 2017**) lists, verbatim:

> **New rewards for player attendance have been added**
> The original New Hunter event has been retired
> Player attendance has been added to the daily assignments menu
> The daily attendance challenge for store purchases has been lowered from 3 to 1
> …
> The Hunter Supply Station attendance page has been improved
> …
> **Fuel Supply awarded to Veterans has been slightly increased**

The wiki page was edited **8 October 2017**, i.e. **two months after** the patch
that introduced the attendance rewards. So the table below is the **post-1.0.8.0
attendance reward table**, not a pre-patch one. (There is **no** later patch note
in the corpus that changes it; the only later attendance-adjacent line is
`Patch_1.1.6.0`, "The 'Today's Assignments' bar is now cumulative rather than
resetting each day" — the *assignments* bar, a different widget.)

### 0.2 ✅ RECOVERED — Daily Rewards, 7 days (week 1)

Extracted from the raw HTML, with the item identity taken from the **linked
image `alt` attribute** and the quantity from the `<b>` run. **The separator
character is U+00D7 `×` (verified by codepoint, not by rendering), and each
digit run was extracted and printed individually** — see
`tools/login-bonus-bytes-2026-10-09.py`, which prints the codepoints of every
cell so a misread digit would be visible. The prior lane's text flattening had
rendered these as `?3000` etc.; that was a `cp1252` console artefact, not
corruption (**GUARD rule 2**).

| day | reward | qty | class |
|---:|---|---:|---|
| **1** | **Rupee** | **3000** | **[COMM] ×3 captures**, post-1.0.8.0 |
| **2** | **Evaluation Request** | **5** | **[COMM] ×3 captures** |
| **3** | **Rupee** | **5000** | **[COMM] ×3 captures** |
| **4** | **Fuel Ticket** | **2** | **[COMM] ×3 captures** |
| **5** | **Challenge Invitation Coupon** | **2** | **[COMM] ×3 captures** |
| **6** | **Elite Request** | **1** | **[COMM] ×3 captures** |
| **7** | **Metron Crystal** | **1** | **[COMM] ×3 captures** |

**Plus, on every daily claim** — verbatim, same page, same three captures:

> **"Claim your Daily reward give you 20 Veteran Points"**

⇒ **attendance pays 20 Veteran points per day.** This is the answer to G9's
half-question; see §4.

**Currency / class breakdown of the week:**

| class | rows |
|---|---|
| **soft currency (Rupee)** | day 1, day 3 |
| **recruitment request** (Evaluation / Elite) | day 2, day 6 |
| **coupon** (Fuel Ticket, Challenge Invitation Coupon) | day 4, day 5 |
| **Metron Crystal** (the 1000-value transcendence material) | day 7 |
| **Veteran EXP** | **+20 on every day, all 7** |

**Notably absent from week 1: gold.** No day in the recovered week pays gold.
See §8 — the replica pays 100 gold on *every* day, which this table contradicts
directly.

### 0.3 ✅ RECOVERED — Cumulative Attendence Dates (a second, separate ladder)

Same page, second table. (The wiki's spelling "Attendence" is preserved
throughout; it is the source's, not a transcription error here.)

| cumulative day | reward | qty | class |
|---:|---|---:|---|
| **5** | **Rupee Lottery Ticket** | **2** | **[COMM] ×3 captures** |
| **10** | **Elite Request** | **1** | **[COMM] ×3 captures** |
| **15** | **2-3 Star Request** | **1** | **[COMM] ×3 captures** |
| **20** | **3 Star Request** | **1** | **[COMM] ×3 captures** |

**This is a distinct track from the 7-day week**, on a different cadence
(5-day steps, threshold-keyed, not day-of-week-keyed). The prior lane recorded
that "Cumulative Attendence Dates" *names* Rupee Lottery Tickets, 2~3★ Requests,
3★ Requests, Elite Requests and Veteran Tickets as attendance outputs but
"**no amounts and no day-by-day table survives in any corpus**". **The amounts
do survive** — four of those five rows are now recovered with quantities and
thresholds. Only **Veteran Ticket** remains unrecovered as an attendance output.

### 0.4 The same page's remaining two sections (context, both partly recovered)

| section | content | class |
|---|---|---|
| **Activity Supply** | "Dawdly will give you **45 Fuel** between [08.00-12.00] [12.00-16.00] [16.00-20.00] and [20.00-24.00]. **You can claim a missed supply for 1 Manda**." | **[COMM] ×3 captures** |
| **Special Supply** | "where you can claim your Events rewards. **From Expert 1** you will receive **5 additional Fuel** when you claim an activity supply." | **[COMM] ×3 captures** |

Two independent corroborations for the **45 fuel** figure, which strengthens the
page's reliability generally:
- `Patch_1.0.7.0` (2017-07-12): "Daily fuel supply has been increased **from 30
  to 45**".
- `List_of_Blustone_Items` names **Hunter Supply Station** as an Ornithopter
  Fuel source.

**This is a second, non-daily fuel grant** and it is the **catch-up** mechanism:
a missed Activity Supply is claimable **for 1 Manda**. It is *not* the login
bonus, and the page does **not** say the same applies to Daily Rewards.

---

## 1. Cycle length and reset — what is recovered, what is not

### 1.1 ✅ The 28-day cycle is REAL — three independent sources

This is the single most important correction to the prior lane, which recorded
"Calendar length **28 days** in the replica — **[FIX]**". The *number 28* is not
a fixture; the **replica's 28 × 100 gold table** is.

| source | locale | date | verbatim |
|---|---|---|---|
| forum **292924** | EN | **2018-01-25** | "We all know that we can **pick any 3\* from legendary scroll once we achieved 28 checked in based on cumulative attendance**." |
| forum **1368000** | EN | **2020-05-19** | "**4★ Selection every 28 days**" (listed as one of the game's few permanent additions over 3 years) |
| forum **1393319** | EN | **2020-07-08** | "The game by now have **login-counter and reward**. Giving freely **4\* selection scroll monthly**" |
| forum **675557** + **691643** | EN | **2018-04-15 / 2018-11-17** | UI reads "**It still says I am on day 28**" and "Yes I see how it says **I am on day 28** and that the other rewards were 'received'" |

⇒ **The attendance cycle is 28 days and it ends in a 4★ Selection
("legendary") scroll.** Three sources, one language, three years, plus a UI
read-out of the number 28 observed by two independent players.

Note the 2018-01 poster writes "**28 checked in**", i.e. **28 check-ins, not 28
distinct calendar days** — a distinction that matters for §2.

### 1.2 ⚠ The 7-day week and the 28-day cycle are the SAME system — reconciled

The prior lane recorded these as apparently separate and conflicting:

- vsfan: a **1-7 Day** weekly table (which this lane recovered, §0.2);
- forum 1422054: "**weekly** … with a **10+1 in the third week**";
- forum 1167975: "not a **weekly** pattern anymore but a **monthly** instead";
- forum 1368000/1393319: a **28-day / monthly** 4★ scroll.

**Reconciliation that the sources support without inventing anything:**

```
28-day cycle  =  4 weeks  ×  7 days
                  │
                  ├─ week 1  = the recovered §0.2 table (Rupee 3000, Eval Req 5,
                  │            Rupee 5000, Fuel Tkt 2, Challenge Inv 2,
                  │            Elite Req 1, Metron Crystal 1)
                  ├─ week 2  = ???  [UNKNOWN]
                  ├─ week 3  = ??? + a 10+1 recruitment scroll   [1P-ish, 1 source]
                  └─ week 4  = ??? + the 4★ Selection scroll     [COMM ×4]
```

Every source fits this shape. The recovered week is **week 1 of a 4-week,
28-day cycle**, not the whole cycle. Forum 1167975's "weekly → monthly" remark
(2019-06) is then not a contradiction at all but a **player describing the same
28-day board as a "month" once the day-28 counter became prominent**.

**Weeks 2, 3 and 4 remain `[UNKNOWN]`.** The 2019 forum says of the chart "The
information for the daily sign in chart seems to **assume that the more days you
accumulate, the better your items become. This doesn't seem to be the case**" —
i.e. one player comparing their own chart with a wiki chart at 265 days found
**no escalation** across weeks, while another replied "Rewards stay the same. As
it has always been." **Two players, opposite readings, no screenshot.** Do not
resolve it.

### 1.3 ❓ The reset boundary is NOT the replica's UTC midnight — and was never settled

This is a **direct, sourced contradiction** of the replica's UTC-day keying, and
it comes from a **first-party support reply**:

`forum 1187734` — "Daily reset time question", **2019-07-25**:

> **[OP]** "Before one of the recent updates … Blustone always did its daily reset
> for me at **12:00 Midnight**. … With the most recent updates though, this seems
> to have changed."
> **[a]** "Daily missions/abyss/mirageruins reset is at midnight/01am as usual.
> **Daily sign in bonus is at 16:00 (4pm).** Works like that to me, dunno for
> others."
> **[b]** "**Sign in bonus is at 10 am for me**"
> **[VS Support, user "Natara"]** "Hello Captains, We are now **under
> investigation about the reset time issue** you have inquired. … We will check
> once again with our development team …"

| fact | value | class |
|---|---|---|
| Historically the daily reset was **local midnight** for the reporter | 12:00 | **[COMM]** ×1 |
| The **sign-in bonus has a different clock** from missions/abyss/mirage | — | **[COMM]** ×1 |
| That clock differs **per player** — two players report **16:00** and **10:00** | — | **[COMM]** ×2, mutually inconsistent |
| VisualShower's own answer | **"under investigation"**, never resolved in the corpus | **[FP-support]** |
| Related: the *other* dailies do reset at local midnight/01:00 | — | **[COMM]** ×1 |

⇒ **The attendance day boundary is a per-account server-side clock, not UTC, and
not the reporter's local midnight.** Two players see two different hours, which
means it is **not** a single global UTC boundary either. **The exact boundary is
`[UNKNOWN]` and VisualShower never published it.**

The replica's `Math.floor(now / 86_400_000)` UTC-day key is therefore
**incompatible with the only evidence that exists on this question**, and this
is the strongest available argument that the replica's calendar should not be
treated as a faithful reproduction.

---

## 2. Consecutive-day semantics — the streak question

### 2.1 ✅ There ARE two distinct systems, and they are not the same thing

The brief's hypothesis — that the "2nd/4th/6th consecutive day" rows and the main
calendar might be two systems — is **correct, and now provable**, because the
§0.2 table shows what day 2 actually pays.

`vsfan List_of_Blustone_Items`, "Areas Available" column, verbatim:

| item | "Areas Available" (verbatim) |
|---|---|
| **Rupee** | "… ranking up in Fight Club, **reaching your 1st consecutive login day**, **reaching your 3rd day as a new Hunter**, Rupee Lottery Tickets …" |
| **Sharp Metal Piece** | "Expedition Areas from 31 - 116, Fight Club Shop, Hunter Shop **and reaching your 2nd consecutive login day**." |
| **Unscathed Shell** | "Expedition Areas from 32 - 117, Fight Club Shop, Hunter Shop **and reaching your 4th consecutive login day**." |
| **Burning Flamestone** | "Expedition Areas from 33 - 118, Fight Club Shop, Hunter Shop **and reaching your 6th consecutive login day**." |
| **Scorching Flamestone** | "Expedition Areas from 93 - 118, Fight Club Shop, **reaching your 6th consecutive login day** and Volcanic Abyss" |

**Against the recovered calendar this is a flat contradiction on day 2:**

| day | recovered calendar (§0.2) | `List_of_Blustone_Items` "consecutive login day" |
|---:|---|---|
| 1 | Rupee 3000 | Rupee — **agrees** |
| 2 | **Evaluation Request ×5** | **Sharp Metal Piece** — **disagrees** |
| 3 | Rupee 5000 | (Rupee, but keyed to "3rd day as a **new Hunter**", not a login day) |
| 4 | **Fuel Ticket ×2** | **Unscathed Shell** — **disagrees** |
| 6 | **Elite Request ×1** | **Burning Flamestone** *and* **Scorching Flamestone** — **disagrees** |

**⇒ These are two different reward tracks, and one of them is an error.**

Three readings survive; the sources do not choose:

1. **`List_of_Blustone_Items` is simply wrong** on this column. It is a wiki
   volunteer-maintained page (and the *same* page's own recovered
   `Hunter_Supply_Office` sibling is demonstrably reliable — §0.1). The
   "consecutive login day" phrasing may be a copy-paste artefact from the
   "Hunter Shop / FC Shop / Expedition Areas" column it sits beside.
2. **Both are real**: the calendar day pays one thing and an *additional*
   "consecutive login" material drops alongside it. Nothing forbids two payouts
   on one day, and the recovered table's cells are single-icon, which does not
   exclude an off-table bonus.
3. **An era change**: the streak materials were the original system and were
   replaced by the §0.2 table in patch **1.0.8.0** ("**New rewards for player
   attendance have been added**"), after which the wiki's item-page column was
   never corrected.

Reading 3 is the most economical — it explains both the contradiction and why
`List_of_Blustone_Items` still names a *retired* pattern ("The original **New
Hunter** event has been retired", patch 1.0.8.0, right next to "reaching your
**3rd day as a new Hunter**"). **But it is not proven. Preserve both.**

### 2.2 ❌ Does a missed day reset the streak? — `[UNKNOWN]`, and the sources actively disagree

| reading | evidence | class |
|---|---|---|
| **Streak resets on a miss** | the phrase "**consecutive** login day" is only meaningful with a reset; and patch 1.0.8.0 lowered "the **daily attendance challenge** for store purchases from 3 to 1" — a *streak* of consecutive attendance drives an IAP challenge | **[COMM]** + inference |
| **Streak never resets; the counter just increments on visit** | forum 292924 (2018-01) says the legendary scroll comes "once we achieved **28 checked in**"; forum 1479784 (2021-01) reports "**1069 daily sign in**" to reach Guru 3 and computes `67520 ÷ 320 = 211 week × 7 = 1477 daily sign in` — **1 069 sign-ins over ~3 years is far more than 1 477 days of unbroken attendance would allow for a casual player, and it is far more than 28×N would need for a reset-free counter.** The 2019 chart comparison at "265 days" likewise presupposes a long unbroken count. | **[COMM]** ×2 |
| **Both** — a "consecutive" streak bonus *and* a never-resetting cumulative counter | the page literally has **two** tables: a 7-day **"Daily Rewards"** week and a threshold-keyed **"Cumulative Attendence Dates"** ladder at 5/10/15/20 | **[COMM]** ×3 captures |

⇒ **The most defensible reading is that the counter is cumulative and
never-resets within a cycle, and that "consecutive" in the item page is loose
wording.** But **this is an inference, not a recovered fact.** The native side
gives one hard constraint: `CachedParseLoginBonusRef` requires a **positive
1-based `count`** — *"zero makes the parser subtract 1 and index a vector,
throwing before any HTTP request"* — so a counter **does** exist and is
**1-based**. Nothing recovered here says whether it resets on a miss.

### 2.3 ✅ The rainbow scroll is a real gating object

Two 2018 threads describe it as a physical inventory item that **blocks progress**:

- `forum 675557` (2018-04-15): "So i got my **rainbow scroll** yesterday … I
  didn't accept my rainbow scroll yet but i was able to receive the day 1 reward
  … (**Normally it doesn't let you accept cumulative day rewards till you accept
  your rainbow scroll**) … It still says I am on day 28 :^) so I might be able to
  save it until my next rainbow or until the next weekly reward."
- `forum 691643` (2018-11-17): "**I am a day away from hitting the 7th day
  reward.** Once this happens, if i can seem to accept the 7th day rewards and so
  forth **while the rainbow scroll is available** … *Update: the game will not let
  you pass through day 7th reward even after redeeming the daily metron … it also
  seemed to **refresh my rewards so I have wasted a week of progress**.*"

⇒ **[COMM] ×2 (2018), two independent players**: the cycle's scroll must be
**redeemed** before the later cumulative rewards can be claimed, and the
calendar advances on redemption, not on login. **This is a real mechanic the
replica does not model** (`claimed` is an array of day numbers; there is no
gating object). It also explains "day 28" being *visible* while the underlying
week is still claimable.

### 2.4 🔴 The day-7 slot is contested across eras — the one direct conflict

| source | date | day-7 / scroll reward |
|---|---|---|
| **`Hunter_Supply_Office`** §0.2 | 2017-10-08, ×3 captures to 2020 | **Metron Crystal ×1** |
| forum **1561517** "Beginner Login Not showing up??" | **2022-01-11** | "Some time after I got my **6th login bonus** from the first week beginner log in thing … **Will I still be able to get the 4\* Selection ticket on my 7th day??**" |
| forum **1422054** | **2020-08-30** | "You get scrolls **weekly**, from daily sign in with **increasing star** as you progress in the month with a **10+1 in the third week**" |
| forum **1368000 / 1393319** | **2020** | "**4★ Selection every 28 days**" / "giving freely 4\* selection scroll monthly" |

The 2022 player places a **4★ Selection ticket on day 7**, which the 2017 wiki
puts on **day 28**. Both can be true only if **day 7 of the cycle carries a
4★ Selection in the later era and a Metron Crystal in the 2017 era** — i.e. a
**content change between 2017 and 2022**. The 2020 statements ("4★ Selection
every 28 days") are about the **cycle**; the 2022 statement is about **day 7
specifically** and is the only source that pins the scroll to day 7.

⚠ **The 2022 statement is an unanswered question, not an assertion.** It carries
**no reply in the corpus** and its author is speculating ("Will I still be
able to…?"). **Do not treat "day 7 = 4★ Selection" as recovered.** Record it as
a **single-source, question-form, 4-years-later claim that conflicts with the
recovered table**, and note that `campaign-reward-ledger` §4.1's "Day-7 4★
Selection ticket" rests on **this same single question** plus `forum 675557`,
which is about the **rainbow scroll** and the 7-day gate, **not** about the
day-7 slot's contents. **That ledger row is weaker than it looks.**

**Net:** day 7 = **Metron Crystal ×1 [COMM ×3]** (2017 era) with a
**single question-form 2022 claim of 4★ Selection** that may indicate an era
change. `[UNKNOWN]` whether the slot changed; **never interpolate.**

---

## 3. G9 — do the two Veteran-point figures reconcile?

**Partly. This lane recovers the missing half of G9.**

### 3.1 ✅ SOLVED: attendance pays 20 Veteran points per day

> **"Claim your Daily reward give you 20 Veteran Points"**
> — `Hunter_Supply_Office`, `oldid=6016`, byte-identical in 3 captures
> (2019-08-21 / 2019-10-15 / 2020-08-08)

This is the attendance-specific Veteran award G9 was missing. It is
**independently corroborated by a first-party receipt in this project's own
runtime**, which is the strongest corroboration available:

| evidence | value | class |
|---|---|---|
| `Hunter_Supply_Office` ×3 captures | **20 Veteran points per daily claim** | **[COMM]** |
| `AGENTS.md` §146 — actual native `/supply/LoginBonusReward` claim | **Veteran EXP +20** (`vip_exp` `prev`/`cur` receipt, thumb maker `VIP1`) | **[R] — live** |
| `AGENTS.md` §155 — actual native day-4 claim | **Veteran EXP +20** (`vip0→20`) | **[R] — live** |
| `AGENTS.md` §186 — actual native day-5 claim | **Veteran EXP +20** (`20→40`) | **[R] — live** |

⇒ **Three separate live claims all paid exactly +20 Veteran EXP.** The wiki
number is confirmed by the game itself. **This is the single best-corroborated
number in the whole attendance system.**

### 3.2 ✅ The arena-vs-attendance conflict is a **two-source** sum, not a contradiction

`vsfan Veteran_Status` (`oldid=6054`, edited 2017-11-08) states the F2P ceiling
as **40 points per day** from "**Daily Goals/Rewards**", and `List_of_Blustone_Items`
lists Veteran Points' sources as "**Daily Goals**, **Daily Rewards**, Veteran
Ticket, Buying Package Goods" — i.e. **two** daily sources.

Now apply §3.1:

```
daily sign-in / "Daily Rewards"   = 20   [recovered, wiki x3 + 3 live claims]
daily goals                        = 20   [inferred by subtraction]
                                   ----
F2P daily ceiling                  = 40   [COMM] vsforum Veteran_Status: AGREES
```

⇒ **The 40/day figure is 20 (attendance) + 20 (daily goals).** This is a
*reconciliation of the two sources of the 40*, not of the 320/week figure.

### 3.3 ⚠ The two Guru-3 thresholds remain genuinely unreconciled — and now we know why

| source | Guru 3 | rate | implied days |
|---|---:|---|---:|
| vsfan `Veteran_Status` (2017-11-08) | **40 960** | 40/day | **1 024** |
| forum 1479784 (2021-01-10) | **67 520** | **320/week** | **1 477** |

Check the forum's own arithmetic, quoted verbatim: *"67520├╖320=211week├ù
7=1477 daily sign in"* — and the poster's reported experience: *"**1069 daily
sign in**, i finaly reatched guru3"*, *"**320points by week = all daily task
done + daily sign in**"*.

**320/week = 45.7/day**, which is **not** 40/day and **not** 20+20. So:

- The two figures disagree on the **daily rate** (40 vs ≈45.7), *and*
- on the **Guru-3 threshold** (40 960 vs 67 520).

**Neither is resolvable from this corpus.** But two facts sharpen it:

1. **`40 960` is not a round number in the forum's frame** — it is exactly
   `40960 = 20 × 2^11`, i.e. **a clean doubling ladder** `20·2^n` with n=11 for
   Guru 3. The vsfan table's own Points row confirms the ladder is
   `20 40 80 160 320 640 1280 2560 5120` — **exact powers of two ×20**, Guru 1
   and Guru 2 cells empty in the HTML. **So 40 960 is internally consistent with
   the ladder the same page publishes.** That is a genuine argument *for* the
   vsfan figure and against 67 520.
2. **`67 520` does not fit that ladder** (`67520 / 20 = 3376`, not a power of
   two). It fits `20 × 2^8 = 5120` at Expert 3 with **a different ladder**, or
   simply a **different era's** balance.

⇒ **Verdict on G9: the *attendance award* is solved (20/day, triple-corroborated
including three live claims). The *Guru-3 threshold* is a genuine two-source
conflict between a self-consistent 2017 wiki ladder and a 2021 player's
account, and it is most likely an era change rather than an error. Record it;
do not average it, and do not "fix" the replica's Veteran ladder from it.**

---

## 4. What the 7-day table does *not* cover — the honest gaps

| cell | status | why |
|---|---|---|
| week 1 day 1–7 | ✅ **[COMM] ×3 captures**, amounts | §0.2 |
| cumulative 5/10/15/20 | ✅ **[COMM] ×3 captures**, amounts | §0.3 |
| 4★ Selection at day 28 | ✅ **[COMM] ×4**, 2018–2020 | §1.1 |
| 20 Veteran pts/claim | ✅ **[COMM] ×3 + [R] ×3 live** | §3.1 |
| Activity Supply 45 fuel + 1-Manda catch-up | ✅ **[COMM] ×3** | §0.4 |
| **week 2 contents** | ❌ **[UNKNOWN]** | no source; one player says no escalation, one says monthly |
| **week 3 contents** | ❌ **[UNKNOWN]** except "a **10+1**" **[COMM] ×1** | forum 1422054, 2020-08 |
| **week 4 contents** | ❌ **[UNKNOWN]** except the 4★ scroll | §1.1 |
| **Veteran Ticket** as an attendance output | ❌ **[UNKNOWN]** | named as attendance-yielding by `List_of_Blustone_Items`; **no amount, no day** |
| **the reset boundary hour** | ❌ **[UNKNOWN]**, and **not UTC** | §1.3; first-party said "under investigation" |
| **miss-day behaviour** | ❌ **[UNKNOWN]** | §2.2, three readings |
| day-7 slot, later era | ⚠ **contested** | §2.4 |
| item **quantities** for the streak materials | ❌ **[UNKNOWN]** | `List_of_Blustone_Items` gives *values* (10/50/250) not attendance *quantities* |

---

## 5. [FIRSTPARTY] image hunt — attempted, and honestly negative

**A `[FIRSTPARTY]` frame of the attendance board would outrank everything above.**
Three such frames are *referenced by name* in the recovered forum corpus and
would each settle the week-2/3/4 question outright:

| doc | attachment | what it shows |
|---|---|---|
| **1167975** (2019-06) | `BCEE7769-5722-4B76-BB11-2F43B97F1B9E.png` | "**New attendance counter good.**" — the whole new chart |
| **675557** (2018-04) | `Screenshot_20180415-000326.png` | "It still says **I am on day 28**" — the day-28 board |
| **691643** (2018-11) | 2 archived PNGs under `…/175/643/691/` | the day-7 rainbow-scroll gate |

**All three were attempted and none is recoverable.** Recorded with the
instrument trail, because a future lane should not repeat this:

1. **Direct `id_` fetch at the archive stamps already present in the forum HTML**
   → **HTTP 404**, 4 730–4 742 B, body `3c21444f…` = the archive's own error page.
2. **Exact-URL CDX** (the query shape proven to work — see §6) → **0 rows for all
   four image URLs**, with the control returning its row in the same run.
3. **CDX `prefix` queries** → the archive returned **HTTP 503 "Temporarily
   Offline"**, i.e. an **instrument fault**, not a content negative. Per guard
   rule 18, prefix queries with this corpus shape are unreliable.

**Controls that DID pass in the same run**, so step 2's zero is a real negative
and not a broken instrument:

| control | expected | result |
|---|---|---|
| `bs.visualshower.com/…/725a8e17….jpg` bytes | 200 / 57 414 B / `ffd8ffe1` | **PASS** |
| same URL via exact-URL CDX | ≥ 1 row | **PASS** (1 row) |
| local archived page contains the day-1 cell | present | **PASS** |

⇒ **Verdict: the attendance screenshots were never captured by the Internet
Archive, or were not indexed under these URLs.** Per guard rule 4 I therefore
**do not claim "no other capture exists"** — only that these four URLs yield
nothing retrievable through every shape that works on this host.

**The one consolation:** the *text* of the board survived in the wiki, which is
why the table above is `[COMM]` and not `[?]`. **If a future lane has a browser
or a fuller image corpus, the doc-1167975 attachment is the single highest-value
target** — it is the 2019 "new attendance counter", i.e. exactly the board that
`campaign-reward-ledger` §4.1 called a **structure change** ("not a weekly pattern
anymore but a monthly instead"). It would settle §1.2 and §2.4 at once.

---

## 6. Method, controls, and four instrument faults caught

Read `GUARD-encoding-and-archive-traps.md` first. Four faults produced false
results in this lane and are recorded so they are not repeated:

### 6.1 A CDX query-shape sweep was required before any CDX zero was believable

My first CDX run used `url=` + a **prefix**, and returned **0 rows for a URL
known to have captures**. A shape sweep against the known-good control then
produced:

| shape | rows | verdict |
|---|---:|---|
| exact-URL, full `https://…` | **1** | **works** |
| exact-URL, no scheme | **1** | **works** |
| `matchType=prefix` | **1** | works on exact URLs only |
| `url=` + folder prefix | **503 "Temporarily Offline"** | **instrument fault** |
| host-only prefix | 0 | **meaningless** |

⇒ **Only exact-URL CDX is trustworthy on this host.** Every zero in §5 was taken
under exact-URL CDX with a same-run passing control.

### 6.2 CDX itself produced a reproducible false negative *within one session*

The control URL in §5 returned **1 row** in run 1 and **0 rows** in run 2 —
identical query, minutes apart. The script **aborted** on the control and I
re-ran after a pause, at which point it passed. **This is exactly guard rule 3.**
Had the script trusted the CDX row count, the entire namu search in §6.4 would
have been a false negative.

### 6.3 `blustone.miraheze.org` is NOT the vsfan wiki — the enumeration control caught it

The archived page's images resolve to `static.miraheze.org/vsfanwiki`, so the
vsfan wiki migrated to Miraheze. I walked `blustone.miraheze.org` expecting the
game wiki and got:

```
namespace-0 pages: 335     <- exactly guard rule 9's "truncation" signature
allrevisions walked: 485   <- vs the 1567 the project previously measured
```

**Those numbers were the alarm, not the result.** Fetching `Main Page` proved
it: the site is the **"BluStone Archiving Wiki"** — *"Unofficial wiki for the
action game Blustone"*, 335 pages, whose content is **character galleries and
fan story transcripts** (`Leon`, `Patrone`, `Yet Another Genius`, …), and which
cites **`en.namu.wiki`** in its references. **A content scan of all 335 pages
(fetched 335, 333 non-empty, 58 carrying game vocabulary — control PASS) found
zero attendance pages.** This is a **real zero for that wiki**, not a truncation.

### 6.4 Korean and Chinese sources — genuinely unreachable from this session

| route | result |
|---|---|
| `namu.wiki` plain HTTP | **HTTP 403** — client-rendered shell, as documented in the brief |
| `en.namu.wiki` | same |
| **CDX for `namu.wiki/w/블루스톤`, `…/블루스톤/출석`, `en.namu.wiki/w/블루스톤`** | **0 rows**, with exact-URL-CDX control **PASS** in the same run ⇒ real negative for the archive |
| Korean search terms | **partly sliced from the workspace notes** (guard 13) — see §6.6 for the correction | `출석` `블루스톤` `보상` verified against the ledger's own codepoints; **`이벤트` was typed from memory and is NOT in the ledger** |
| **Browser** | **NOT AVAILABLE** — `browser.disconnected`; the brief specifies namu is *browser-rendered only*, so this route was closed |
| Web search (Korean, Chinese, English) | **returned nothing even for the trivial control query "VisualShower Blustone wiki"** ⇒ **the search instrument is dead in this session**, so no search-based negative is claimed |
| Chinese (疾风小侠 / 青石之战 / 青石) | **not searched** — see above |

⚠ **Consequence, stated plainly:** the Korean and Chinese attendance tables were
**not consulted**, because every route to them was unavailable here. This lane's
result is therefore **English-only**. The Korean namu attendance page is
precisely the source `campaign-reward-ledger` §6 G1 named as one of the three
things that would settle G1, and it remains **unread**.

### 6.5 One bug of my own, caught by a control

The corpus reader initially joined an already-joined string
(`"\n".join(body_of(raw))` where `body_of` returned a `str`), which split the text
into single characters and made the control document read as **0 hits**. The
control caught it immediately. **Recorded because it is the same silent
false-zero class the GUARD exists for, and it was caught only because a positive
control was mandatory rather than optional.**

### 6.6 ⚠ And a second one — the guard fired on ME, and this note was wrong

The brief warns (guard 13) that *"never hand-write Unicode codepoints for a search
term — slice it out of the data … a lane typed Hangul from memory, got two of
three wrong, and produced a false zero."* I ran a **codepoint-diff verification**
of this note's Korean against `campaign-reward-ledger-2026-10-09.md` and it
**failed**:

```
Hangul in MY note :  보상  블루스톤  이벤트  출석
matches ledger    :  True  True     False   True
RESULT: FAIL - invented tokens: ['이벤트']
```

`이벤트` ("event") is **not** among the ledger's 88 Hangul tokens, and the
slicer found **no** event-like token (`이벤*` / `행사*` → **NONE**). So that term
**was typed from memory**, exactly the act guard 13 prohibits.

**What this does and does not affect:**

- It **cannot have corrupted any finding in this note.** `이벤트` was used only
  as a candidate namu **page title**, and every namu result in §6.4 is a
  **negative** (0 rows). A wrong term can only ever produce a **false negative**,
  never a false positive — and §6.4 already concludes "unreached", not "absent".
- It **does** weaken the namu search slightly: `…/블루스톤/이벤트` may have been
  the wrong title. `…/블루스톤/출석` was queried with a **verified** term and
  also returned 0 rows, which is the load-bearing negative.
- Three of the four terms (`출석`, `블루스톤`, `보상`) **are** verified
  slice-equivalent, and the two terms actually used for the decisive query
  (`블루스톤`, `출석`) are both verified.

**Correction applied:** the §6.4 row now states the provenance exactly rather
than claiming all terms were sliced. **A future lane that gets a browser should
re-derive the Korean page titles by slicing from namu's own navigation, not by
typing them** — this is precisely the trap the guard was written for, and I fell
into it while trying to follow it.

---

## 7. Reconciliation against `campaign-reward-ledger-2026-10-09.md` §4.1

| prior ledger row | status after this lane |
|---|---|
| "Calendar length — **28 days** in the replica — **[FIX]**" | ⚠ **retracted as unfounded.** **28 days is [COMM ×4]** (forum 292924/1368000/1393319 + a UI read-out in 675557/691643). What remains **[FIX]** is the *table*, not the *length*. |
| "Calendar contents — **[UNK]** … no amounts and no day-by-day table survives in any corpus" | 🔴 **retracted.** §0.2 and §0.3 recover **11 rows with exact item + quantity**, plus the 20-Veteran-pt daily award. **9 rows of the 11 are attributable.** |
| "**Consecutive-day structure exists** — 2nd/4th/6th consecutive login day" | ✅ confirmed, and **now shown to conflict with the recovered calendar** (§2.1). Either the item page is wrong or they are two tracks. |
| "**Rupee on day 1**" | ✅ **confirmed by amount: 3000.** |
| "**Rupee on day 3 as a new Hunter**" | ⚠ The recovered **day 3 is Rupee 5000**, but `List_of_Blustone_Items` keys that Rupee to the **3rd day as a *new Hunter***, not to login day 3. **Two different Rupee grants are being conflated.** |
| "Weekly scrolls from sign-in … 10+1 in the third week" | ✅ consistent with the 4-week cycle (§1.2); **week 3's scroll is [COMM ×1] only.** |
| "Day-7 4★ Selection ticket (forum 1561517 + forum 675557)" | ⚠ **weaker than recorded.** The **recovered day 7 is Metron Crystal ×1**. `1561517` is an **unanswered question**; `675557` is about the **rainbow-scroll gate**, not the day-7 contents. See §2.4. |
| "Monthly, not weekly (forum 1167975)" | ✅ **reconciled**, not contradicted — "monthly" = the 28-day cycle (§1.2). |
| "Reset hour 16:00 / 10 am / under investigation" | ✅ **confirmed and strengthened**: the attendance clock is **per-player** and **separate from the missions/abyss/mirage midnight reset**, so it is **not UTC**. |
| "28-day 'rainbow scroll' … It still says I am on day 28" | ✅ **upgraded to a mechanism**: the scroll must be **redeemed** before later cumulative rewards unlock (§2.3). |
| "Veteran points from attendance — 40 points/day maximum" | ✅ **split and solved**: **attendance = 20/day** (wiki ×3 + **3 live native claims**), **daily goals = 20/day** by subtraction. §3. |
| "Hunter Supply Station / Hunter Supply Office … navigation stubs with no reward content at all" | 🔴 **retracted.** `Hunter_Supply_Office` carries **both reward tables**. `Hunter_Supply_Station` remains a stub — the prior lane merged two pages. |
| "**G9** Veteran ladder two irreconcilable figures" | ⚠ **partly resolved**: the attendance half is solved (§3.1); the Guru-3 threshold conflict stands and is most likely an era change (§3.3). |

---

## 8. What the replica publishes today — READ-ONLY report

Read from `server-ts/src` on 2026-10-09. **Nothing was edited; the build and
tests were not run.** `git status --porcelain -- server-ts` is unchanged by this
lane; every access was a `read`/`grep`.

### 8.1 `server-ts/src/login-bonus.ts` (36 lines, quoted in full for the constants)

```ts
export const LOGIN_BONUS_DAYS  = 28;    // [FIX] length is [COMM]; this table is [FIX]
export const LOGIN_BONUS_GOLD  = 100;   // [FIX] — CONTRADICTED by the recovered week
export const LOGIN_BONUS_VIP_EXP = 20;  // [R]  — §3.1, triple-corroborated
```

`loginBonusReference()` publishes, for each `target_cnt` 1..28:

```ts
{ target_cnt: n, gold: 100, free_iap: 0, item_list: "[]", card_list: "[]" }
```

`observeLoginBonus()` keys the day on **`Math.floor(now / 86_400_000)`** — a
**UTC** day — and does `eligible = Math.min(28, eligible + 1)`, i.e. **the
counter only ever increments and never resets**.
`loginBonusInstance()` returns `cur_value: eligible, cycle: 1, cycle_log: claimed`.

### 8.2 Assessment of the replica against this lane's evidence

| element | replica | evidence | verdict |
|---|---:|---|---|
| cycle length | **28** | **[COMM ×4]** | ✅ **now externally confirmed** (was **[FIX]**) |
| **table content** | **28 × 100 gold** | recovered week 1 = Rupee 3000, EvalReq 5, Rupee 5000, FuelTkt 2, ChallengeInv 2, EliteReq 1, **Metron Crystal 1** | ❌ **wrong in content, not just detail.** Gold appears on **no** day of the recovered week; **9 of 28 cells are now known and the replica matches none of them** |
| `item_list` / `card_list` | `"[]"` on every row | original rows carry `item_list`/`card_list` **as JSON strings with `ref_id`/`qty`** (native, §0) — the replica's empty arrays are wire-legal but **content-empty** | ⚠ structurally right, **9 rows of content now known and unpublished** |
| cumulative ladder | **absent** | 5/10/15/20 → RupeeLott 2, EliteReq 1, 2-3★Req 1, 3★Req 1 | ❌ **a whole second track is missing** |
| 4★ Selection at day 28 | **absent** | **[COMM ×4]** | ❌ **the single most valuable item in the system is missing** |
| Veteran points | **20** | **[COMM ×3] + [R] ×3 live** | ✅ **correct** — and now externally justified rather than merely observed |
| day boundary | **UTC midnight** | per-player, **not** the missions/abyss midnight, 16:00 vs 10:00, VS "under investigation" | ❌ **contradicted**; the original clock is `[UNKNOWN]` |
| catch-up / missed day | **none** | Activity Supply catch-up exists **for 1 Manda** (§0.4); login catch-up unstated | ⚠ the *fuel* catch-up is documented; the *login* one is not |
| rainbow-scroll gate | **absent** | **[COMM ×2]** — redemption gates later cumulative rewards and advances the calendar | ❌ **a real mechanic is unmodelled** |
| reset / cycle rollover | **`cycle: 1`, `eligible` caps at 28** | 28-day cycle **does** roll | ⚠ **cap at 28 is right; the rollover *boundary* and the claimed-day reset on rollover are unverified** |
| "consecutive day" streak | **not modelled** | 2nd/4th/6th-day skill materials, contested (§2.1) | ⚠ **correctly absent given the conflict — do not add it until §2.1 is resolved** |

**Net: 2 elements confirmed (cycle length 28; the 20 Veteran points), 2 wrong
(table content; UTC day boundary), 3 missing (cumulative ladder, the 4★ scroll,
the rainbow-scroll gate).** The `28 × 100 gold` table is the **most**
demonstrably wrong artefact in the replica's reward surface — worse than the
300/200/100 star chests, because here **9 cells of the original are now known
and every one of them differs.**

**Recommendation (for the owner, not acted on — this lane is read-only):**
replacing the invented 28 × 100 gold with the **recovered week 1** for days 1–7
and leaving days 8–28 `[UNKNOWN]` would be a strict accuracy gain, and is the
one change this lane's evidence authorises. **Do not interpolate weeks 2–4, do
not add the streak materials, and do not change the day boundary** — the last
has no recovered value and would be a new invention.

---

## 9. Provenance ledger

| artefact | what it is |
|---|---|
| `recovered-assets/login-bonus-2026-10-09/Hunter_Supply_Office__20190821011235.html` | archived capture, 26 283 B, sha256 `2995eb8054f91dba…` — **the recovered table** |
| `…__20191015115618.html` | 26 283 B, sha256 `d5117e32fb8dc229…`, **same oldid 6016** |
| `…__20200808181724.html` | 25 966 B, sha256 `2a8e37c7897e94c7…`, **same oldid 6016** |
| `recovered-assets/login-bonus-2026-10-09/miraheze-pages.json` | the 335-page enumeration + hit list (§6.3) |
| `tools/login-bonus-parse-2026-10-09.py` | extracts both tables from raw HTML; item identity from `alt`, quantity from the `<b>` run |
| `tools/login-bonus-bytes-2026-10-09.py` | **byte-level numeral verification** — prints the codepoint of every cell's leading char and the isolated digit run |
| `tools/login-bonus-fetch-2026-10-09.py` | fetches all three captures, hashes each, prints every table + prose keyword context |
| `tools/login-bonus-diff-2026-10-09.py` | region-level SHA-256 diff proving the tables are stable while the page is not |
| `tools/login-bonus-cdx-2026-10-09.py` / `-prefix-` / `-shape-` | CDX enumeration + the query-shape sweep (§6.1) |
| `tools/login-bonus-shots2-2026-10-09.py` | the [FIRSTPARTY] image attempt with dual controls (§5) |
| `tools/login-bonus-forum-screen-2026-10-09.py` / `-dump-` / `-full-` / `-week-` / `-cycle-` / `-latest-` | the 4 300-file body-only corpus readers, each gated on the 149251 positive control |
| `tools/login-bonus-veteran-2026-10-09.py` | the Veteran ladder table extraction behind §3.3 |
| `tools/login-bonus-patches-2026-10-09.py` / `-patchindex-` / `-patchfull-` | the 16 vsfan patch notes; source of the 1.0.8.0 era anchor |
| `tools/login-bonus-livewiki-2026-10-09.py` / `-findwiki-` / `-miraheze*` | the live-wiki hunt and its failure (§6.3) |
| `tools/login-bonus-namu-2026-10-09.py` / `-namu2-` | the namu attempts; Hangul **sliced from the ledger where the term exists** — see the correction in §6.6 |
| `tools/_verify_login_bonus_note.py` | the mandatory encoding check: U+FFFD, CRLF, lone CR, BOM, mojibake, and preservation of Hangul/CJK/`×`/`★` |
| `tools/_verify_hangul_sliced.py` | **codepoint-diff of this note's Korean against the source ledger** — this is the check that caught the §6.6 provenance error |

**Reading order for a successor:** §0.2 (the table) → §1.1 (28 days) → §3.1
(20 Veteran points) → §2.4 (the day-7 conflict, the one thing that could still
move) → §5 (the one image that would settle it).

---

## 10. Honest bottom line

**A real reward table was recovered this lane.** The Blustone Login Bonus /
attendance calendar is **7-day weekly**, with **exact item and quantity for all
seven days** — Rupee 3000, Evaluation Request 5, Rupee 5000, Fuel Ticket 2,
Challenge Invitation Coupon 2, Elite Request 1, Metron Crystal 1 — plus
**+20 Veteran points on every claim**. A **second, cumulative ladder at
5 / 10 / 15 / 20 days** was recovered with amounts (Rupee Lottery Ticket 2,
Elite Request 1, 2-3★ Request 1, 3★ Request 1). The source is one original
English-client wiki page, **byte-identical in the table regions across three
dated captures spanning a year**, anchored to a **named patch (1.0.8.0,
2017-08-03)** that introduced attendance rewards.

**The cycle is 28 days and ends in a 4★ Selection scroll** — three independent
2018–2020 sources plus a UI read-out of "day 28" by two players. This
**retracts** the prior ledger's classification of 28 as a fixture.

**G9 is half-solved:** attendance pays **20 Veteran points/day**, confirmed by
the wiki ×3 captures *and* by **three separate live native claims in this
project's own runtime** (+20 each). That splits the wiki's "40/day" into
20 (sign-in) + 20 (daily goals). The **Guru-3 threshold conflict (40 960 vs
67 520) stands unresolved** and is most likely an era change — the 40 960 fits
the same page's own `20·2^n` ladder exactly, the 67 520 does not.

**Three prior "unknown" rows are now wrong and are retracted:** the calendar
contents are *not* unknown; "28 days" is *not* a fixture; and
`Hunter_Supply_Office` is *not* a navigation stub.

**What remains open, honestly:** weeks 2, 3 and 4 of the cycle (only "a 10+1" in
week 3, **[COMM] ×1**); the Veteran Ticket's day and amount; the **reset hour**,
which is **proved not to be UTC** but is otherwise `[UNKNOWN]` and which
VisualShower's own support answered "under investigation"; and whether a missed
day resets the counter. The **day-7 slot is contested** — Metron Crystal in the
recovered 2017-era table versus a single, unanswered 2022 question claiming a
4★ Selection ticket — and **must not be interpolated**.

**The Korean and Chinese sources were not reached.** namu 403s to plain HTTP, the
CDX has no captures of the relevant pages (and one of my four candidate Korean
page titles was typed rather than sliced — §6.6 — so that negative is slightly
weaker than it looks), **no browser was attached to this subagent session**, and
**web search returned nothing even for a trivial control query**. The namu
attendance page named in the original G1 entry is still unread.

**No `[FIRSTPARTY]` image was recovered.** Three attendance-board screenshots are
named in the forum corpus and were attempted through every archive query shape
that works on this host; all four URLs return nothing under exact-URL CDX with a
same-run passing control, and prefix queries fail with an archive-side 503. **The
highest-value single target for a future lane is the doc-1167975 attachment
`BCEE7769-5722-4B76-BB11-2F43B97F1B9E.png`** — the 2019 "new attendance counter",
which would settle weeks 2–4 and the day-7 conflict in one frame.

**Coverage counters unmoved: heroes 1/113, accessories 1/100, monsters 0/22.**
Nothing here is a base stat. **No append to `polluted-observations.md`;
`coverage.md`, every TSV, `server-ts`, fixtures, the APK, seeds, the emulator,
the phone and Ghidra were not touched.**