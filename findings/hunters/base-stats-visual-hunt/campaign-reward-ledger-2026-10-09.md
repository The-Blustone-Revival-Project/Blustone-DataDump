# CAMPAIGN REWARD LEDGER — what is actually documented, system by system (2026-10-09)

**Lane goal:** every campaign reward, in every area, at every threshold; every
non-campaign reward; the currency flow graph; and an explicit, ranked gap list.

**Headline, before anything else:** the campaign's **three regional thresholds
(10 / 20 / 30 stars) are now confirmed from an original English-language source,
in three independent dated captures.** What that source also says — that the
**30-star** reward is **the region's hunter** — directly contradicts the Korean
first-party statement recorded earlier ("만다나 의뢰서"). Both are recorded
below; neither is silently preferred. **The 10-star and 20-star rewards remain
[UNKNOWN].** Nothing in this note authorises a number where the sources are silent.

**Read-only lane.** `server-ts/` was read, never written. No build, no tests, no
dev server. §7 reports exactly what the replica publishes today.

**Coverage counters unmoved: heroes 1/113 (0.9 %), accessories 1/100 (1.0 %),
monsters 0/22 (0 %).** Nothing here is a base stat. This file is economy /
progression evidence only, per `coverage.md`'s scope rule.

---

## 0. Method, controls, and two instrument faults caught

### 0.1 Corpus actually read this lane

| corpus | what | how |
|---|---|---|
| `recovered-assets/forum-en-2026-10-05/` — `get-body/body` (166), `pass2/body` (3 036), `pass2/body-latest` (575), `pass2/topup` (146), `pass2/get-list/list` (205), `pass2/list` (41) | 4 169 HTML files, **3 219 741 characters of post body + replies** | offline re-read, no network |
| `vsfan.net/wiki/*` via Wayback — 26 pages in batch 1, 82 targets in batch 2 | 65 pages stored to `recovered-assets/vsfan-reward-2026-10-09/` | `http://` only, 3 workers, one shared `Session` |
| 9 vsfan titles re-enumerated by **exact-URL CDX** with every capture fetched | 26 captures across 9 titles | `matchType=exact`, `collapse=digest` |
| prior notes | `star-conditions-era-2026-10-09.md`, `rewards-economy-2026-10-05.md`, `cost-ledger-2026-10-09.md`, `fc-economy-2026-10-05.md`, `namu-first-party-mechanics-2026-10-08.md`, `namu-item-economy-tables-2026-10-08.md`, `namu-tables-2026-10-05.md`, `share-en-panels-2026-10-05.md`, `vsfan-wiki-2026-10-05.md` | read, used by reference |

### 0.2 Positive controls — run before every zero

| control | expected | result |
|---|---|---|
| `149251` contains `Metron Crystals` (documented in `forum-en-mining-pass2` §3.1) | present | **PASS**, both arms |
| `149251` ladder text (`5,000`) present | present | **PASS** |
| archive image `…/75605/303/534/001/725a8e175454a533e96dac68fc5fdb49.jpg` | HTTP 200 / 57 414 B / `ffd8ffe1` | **PASS ×4 batches** |
| `Expedition_Area` contains `Regional rewards` | present | **PASS ×3 captures** |

**One control FAILED and correctly aborted the run.** A second batch returned
`POSITIVE CONTROL: code=0 size=0 -> FAIL` and the script exited before issuing a
single page request. That was a transport fault, not a content negative; the
batch was re-run after a pause and passed. Recorded because a reader must be able
to tell "the archive refused me" from "the page does not say this".

### 0.3 Instrument fault #1 — the board's sidebar ate every keyword screen

The first pass searched whole-page text. The XE board template repeats **every
thread title on the page** in a sidebar, so the screen for "star reward" hit
**2 668 files** and the screen for "guild" hit **2 833** — out of 4 169. Those
numbers were meaningless. Re-run after extracting only
`<div class="document_* xe_content">` plus every `<div class="comment_* xe_content">`:

| screen | whole-page files | **body-only files** |
|---|---:|---:|
| star threshold | 2 668 | **393** → 40 distinct ids |
| login / attendance | 3 268 | **412** |
| arena | 1 565 | **421** |
| guild / gvg | 2 833 | **419** |
| supply | 125 | **63** |
| mirage | 1 193 | **303** |
| fishing | 571 | **107** |
| currency | 2 678 | **1 021** |

Every number in this note comes from the **body-only** pass. Quoting the first
column as a hit count would have been the "false zero" pattern in reverse — a
false *abundance*.

### 0.4 Instrument fault #2 — a fetch guard that rejected every real page

The vsfan fetcher originally required `b'<!DOCTYPE' not in body[:400]`. Every
MediaWiki page *starts* with `<!DOCTYPE html>`, so **26/26 pages were silently
not written to disk** while the log cheerfully reported
`code=200 bytes=38733`. The directory was empty. Replaced with a
content-based rejection (`Temporarily Offline` / `not archived` / `Got an HTTP
302` in the first 4 kB) plus a SHA-256 per body, per guard rule. Re-fetched, and
the byte counts then matched the archived `vsfan-wiki-2026-10-05` ledger exactly
(`Expedition_Area` 38 733 B, `List_of_Blustone_Items` 104 950 B, `Abyss_Area`
50 028 B …).

**This is the second time in this project that a "successful" log line
concealed an empty result.** It is recorded because the failure mode is silent:
the tool reports success, the directory is empty, and a later agent concludes
"already checked".

---

# 1. THE HEADLINE FINDING — campaign regional rewards

## 1.1 The text, verbatim, from the ORIGINAL source

`vsfan.net/wiki/Expedition_Area` — a community wiki of the **English** client,
MediaWiki, `oldid=3233`. Fetched at **three** independently-chosen Wayback
timestamps; the paragraph is **byte-identical in the rendered text of all
three**:

> Regional rewards are available by clearing areas and gaining stars. There are
> **three regional rewards, one at 10 total stars gained in the region, another at
> 20 stars, and the last at 30 stars. You obtain the hunter specific to the region
> for gaining 30 stars.** You obtain stars by satisfying the following conditions
> when clearing an area.
> — Area successfully cleared.
> — Complete the area in the allotted time. (Time bar is shown on the bottom left
>   of the battle.)
> — All hunters on your team have survived.

| capture (UTC) | HTTP | bytes | sha256 (16) | the paragraph present |
|---|---|---:|---|---|
| `web/20190826070239` | 200 | 38 733 | `9faa58b1573e179c` | **yes** |
| `web/20191020212117` | 200 | 38 733 | `bc5587b54ed7ce1c` | **yes** |
| `web/20191214142617` | 200 | 38 778 | `ecda5055da781539` | **yes** |

Three captures, 46 days and 116 days apart, three different digests (the page
was edited in between) — and the reward paragraph is **unchanged**. This is a
**maintained statement, not one lucky revision**, which is the same test
`star-conditions-era-2026-10-09.md` §3.2 applied to the star-condition wording
and which correctly refused to blame the 2019-09-05 rebalance.

Era: Aug–Dec 2019, i.e. **after** the 2019-09-05 rebalance.

## 1.2 What this settles, and what it does not

| question | answer | class |
|---|---|---|
| How many regional (star-total) rewards per region? | **three** | **[COMMUNITY, ×3 captures]** — corroborated structurally by the client's own `GetRewards()` iteration and by `FIXTURE_CHEST_COUNT = 3` |
| What are the three thresholds? | **10 / 20 / 30 total stars** | **[COMMUNITY]** ×3 captures · **independent structural corroboration** below |
| What does the **10-star** reward pay? | **unknown** | **[UNKNOWN]** |
| What does the **20-star** reward pay? | **unknown** | **[UNKNOWN]** |
| What does the **30-star** reward pay? | **the region's own hunter** | **[COMMUNITY]** ×3 captures — **and contradicted by first-party Korean**, §1.3 |

### The structural corroboration is the strongest part

This is **not** only a wiki claim. The replica's client-side arithmetic is
independently recovered from native code and **forces** the same three numbers:

- `CSRGameStage::ShowReward` draws the chest labels **`S`, `(S*6)/3 == 2S`,
  `S*3`** where `S = GetStageCnt(area)` (`ghidra-chest-03-getters.txt` /
  `analysis/research/chest-rewards.md`, cited in `bootstrap.ts:609-616`).
- Both the claimable test (`ShowReward :3218`) and the request gate
  (`SendRewardRequest :1572-1574`) compare progress against **`S * (i + 1)`**.
- With `S = 10` (ten `stage[]` links per area, which is what the recovered
  `campaign-stages.csv` gives for all five areas) that is **10, 20, 30**.

So the **count** (three) and the **thresholds** (10/20/30) are agreed by
**two independent classes**: an English community wiki from 2019 and the
client's own compiled arithmetic. The **payout contents** are not: `S*(i+1)`
says nothing about what is inside.

**This is also the first external confirmation of the replica's own
`achieve_cnt = stageCount * (index + 1)` derivation.** It was previously derived
from native code alone and carried a `[FIXTURE]`-shaped uncertainty about whether
the arithmetic matched the shipped reference table. It now has an outside
witness.

## 1.3 ⚠ CONFLICT — what the 30-star reward is

| source | locale | capture / revision | date | claim |
|---|---|---|---|---|
| `vsfan Expedition_Area` ×3 captures | **EN** | `oldid=3233` | 2019-08-26 / 10-20 / 12-14 | 30 stars → **the region's hunter** |
| namu main page, quoted in `namu-first-party-mechanics-2026-10-08.md` §2 F3 | **KO** | browser-rendered, last modified 2026-10-01 | content spans 2017–2021 | "상위 지역 하나 당 **10개의 하위 지역**을 각각 **별 3개**, 상위 지역을 **별 30개**의 성적으로 클리어하면 **만다나 의뢰서**를 보상" |
| `vsfan Guide_to_Blustone` (2019-09-23, `oldid=7465`) | EN | `e01c67efa522394d` | 2019-09-23 | "unlock the next region by **beating the boss** of the current region. When you do beat the boss, **you will obtain the hunter** for whom you were doing the storyline quest for" |

**These are not reconcilable as written, and I am not reconciling them.**

- namu says the 30-star total pays a **만다나 의뢰서** (a Mandaring *commission*).
- vsfan says the 30-star total pays **the region's hunter**.
- vsfan's own Guide says the **hunter comes from beating the region boss**, which
  is a *different* trigger from a 30-star total (30 stars is 10 stages × 3
  stars and does not require a boss kill in particular… unless the boss IS
  stage 10 and 3-starring it is what makes 30).

**Three readings survive, and the sources do not choose between them:**

1. **Both are true of different things.** The hunter is the *boss-clear* reward
   (Guide), and the 30-star *chest* pays a Mandaring commission (namu). vsfan's
   Expedition_Area would then be conflating the two.
2. **Both are true of the same thing.** The 30-star chest *is* the boss clear
   (stage 10 at 3 stars), and it pays both the hunter and a commission. The
   namu sentence may be listing the commission because the hunter is obvious.
3. **One era changed it.** namu spans 2017–2021 and was last edited 2026-10-01;
   vsfan is 2019. A change between is possible.

**What is NOT in doubt:** the 30-star threshold **exists**, it is the **last of
three**, and **something is paid at it**. The *identity* of that something is
**[UNKNOWN — two sources, two answers]**.

**Consequence for the replica: none yet.** The replica pays **gold** at all
three (`FIXTURE_CHEST_ITEMS` 300/200/100) and grants no card
(`card_list: []`, deliberately — `bootstrap.ts:582-587`). Under all three
readings above the replica is **wrong at 30 stars** (it pays gold where a hunter
and/or a commission belongs) and **unevidenced at 10 and 20**.

## 1.4 The threshold count also matches the Korean source exactly

namu, first-party: 10 sub-areas per upper area × 3 stars each = **30 stars** max
per region. vsfan, community English: "**three** regional rewards… 10 / 20 / 30".
Native: `GetRewards()` iterated three times, gated on `S*(i+1)` with `S=10`.
Three independent sources, three thresholds. **This is the best-corroborated
number in the whole campaign reward system.**

## 1.5 Per-area and per-threshold status — the honest table

The replica's five areas are `n_01`…`n_05` (recovered `campaign-stages.csv`,
10 stages each). **Nothing in any source names a specific area's reward.** The
per-area question is therefore not "which number" but "does a per-area table
exist at all", and the answer is: **no source found one.**

| area | 10-star | 20-star | 30-star | class of the gap |
|---|---|---|---|---|
| `n_01` (Snowfield) | **[UNKNOWN]** | **[UNKNOWN]** | **[UNKNOWN]** — threshold confirmed, payout disputed (§1.3) | needs the original `achieve_reward[]` reference table |
| `n_02` | **[UNKNOWN]** | **[UNKNOWN]** | **[UNKNOWN]** — same | same |
| `n_03` | **[UNKNOWN]** | **[UNKNOWN]** | **[UNKNOWN]** — same | same |
| `n_04` | **[UNKNOWN]** | **[UNKNOWN]** | **[UNKNOWN]** — same | same |
| `n_05` | **[UNKNOWN]** | **[UNKNOWN]** | **[UNKNOWN]** — same | same |
| `n_00` (origin/Village) | n/a — 1 stage link, `S=1`, so thresholds are 1/2/3 | — | — | origin node, not a reward region |

**Fifteen cells, fifteen `[UNKNOWN]`.** The *thresholds* are known for all of
them; not one *payout* is.

### Live-observed replica behaviour (not original data)

From `AGENTS.md`: the replica paid gold at the **20-star** threshold for `n_02`
and `n_03` (§116) and a 10-star threshold exists for `n_01` (§69). Those are
**observations of the replica's own fixture paying out**, not evidence about the
original. They are listed here only so nobody mistakes them for a source.

---

# 2. What each regional reward is NOT

Stating this because each of these is a plausible-sounding thing to invent:

- **Not gold.** No source says the chests pay gold. The replica's 300/200/100
  gold has **no source at all**.
- **Not a Transcendence Ticket.** The replica publishes `★2/★3/★4
  Transcendence Ticket` (`912/913/914`) as the chest items, and those **ids are
  genuinely recovered** (rows of `CHAR_STR_RO`, `bootstrap.ts:512-517`). But
  **nothing links them to the star chests** — that link is a local choice.
- **Not Manda.** No source says a star chest pays Manda, even though Manda is
  what a player *associates* with progress here (`forum 1368000`: "Free manda on
  Fight Club and Stages… everyone wants to get high rank in Fight Club for that
  manda").

---

# 3. THE CAMPAIGN'S OWN DROP TABLE — what a stage actually gives

`vsfan List_of_Blustone_Items` (2019-08-21, `oldid=5115`, 104 950 B) is the
single richest original campaign-economy source in the project. Verbatim, from
`Expedition_Area`:

> Every area drops different skill items, but all drop **Evaluation Requests,
> Elite Requests, Rupee Tickets, Metron Fragments, or hunter traces specific to
> that region by chance** and **always drops rupees**.

### 3.1 The stage-digit material rule — [COMMUNITY], three independent sources

| ending digit | material family | roles |
|---|---|---|
| **1 or 6** | Metal pieces | Offense |
| **2 or 7** | Shells | Defense |
| **3 or 8** | Flamestones | Bomber |
| **4 or 9** | Herbs | Support |
| **5 or 0** | none — "an increase in drops for **traces scrolls, traces of the particular hunter for that level** … and **metron fragments**" | — |

Sources agreeing: vsfan `Expedition_Area` (2019) · `share-en-panels` §1.6.4
Alaiko 2017-11-12 (`1/6 → Offensives, 2/7 → Defenders, 3/8 → Bombers, 4/9 →
Healers, 5/0 → none`) · the same note's independent 2018/2019 Google-Doc
community guide ("Those stages with a digit 6 are for Attacker materials …
Rupee tickets gather at any stage"). **Three sources, two languages, eight
years apart.**

### 3.2 Material grades, areas, and shop values — [COMMUNITY], 2019-08-21

| material | grade | areas available | value |
|---|---|---|---:|
| Rusty Metal Piece | 1 | Expedition 1–86, Electric Abyss, Hunter Shop | **10** |
| Sharp Metal Piece | 2 | Expedition 31–116, FC Shop, Hunter Shop, **and reaching your 2nd consecutive login day** | **50** |
| Unusual Metal Piece | 3 | Expedition 91–116, Electric Abyss, FC Shop | **250** |
| Broken Shell | 1 | Expedition 2–87, Cryogenic Abyss, Hunter Shop | **10** |
| Unscathed Shell | 2 | Expedition 32–117, FC Shop, Hunter Shop, **4th consecutive login day** | **50** |
| Invincible Shell | 3 | Expedition 92–117, Cryogenic Abyss, FC Shop | **250** |
| Cold Flamestone | 1 | Expedition 3–88, Hunter Shop, Volcanic Abyss | **10** |
| Burning Flamestone | 2 | Expedition 33–118, FC Shop, Hunter Shop, **6th consecutive login day** | **50** |
| Scorching Flamestone | 3 | Expedition 93–118, FC Shop, **6th consecutive login day**, Volcanic Abyss | **250** |
| Withered Herb | 1 | Expedition 4–89, Hunter Shop, Golden Abyss | **10** |
| Fresh Herb | 2 | Expedition 34–169, FC Shop, Hunter Shop, Golden Abyss | **50** |
| Fruit-Bearing Herb | 3 | Expedition 94–169, FC Shop, Golden Abyss | **250** |

**Two rows carry a genuine new fact: the 2nd / 4th / 6th *consecutive login day*
drop a mid-grade skill material.** That is the closest thing to a documented
Login Bonus calendar content in this corpus (§4.1).

### 3.3 The 190-stage ladder — a scope fact, not a reward

The same page's Locations nav lists expedition areas as **19 regions × 10 areas =
190 areas**, numbered 1–190 (Midgard Snowfields 1-10 … Gray Valley 181-190).

> ⚠ **This does not match the replica's 50.** namu says **50 dungeons as of
> 2019** (first-party). The recovered `campaign-stages.csv` gives
> **5 areas × 10 = 50** (`n_01_01`..`n_05_10`). vsfan says **190**.
> **Three numbers, three sources, unreconciled.** Recorded, not resolved. It
> bears on rewards only because a 190-stage ladder implies ~57 regional rewards
> at the same 10/20/30 cadence, against the replica's 15.

### 3.4 Region unlock gates — [COMMUNITY], and they gate the chests

| location | prerequisite (vsfan infobox) |
|---|---|
| Fight Club | **Clear Area 30** |
| Hunter Shop | **Clear Area 15** |
| Expedition Area | "Clear opening tutorial" |
| Abyss Area | "Proficient Hunters" (4★) |
| Rotation Area | "Novice Hunters" |

Plus `namu-first-party-mechanics` §2 F5: the **Jewel Mine and the Forge both
gate on owning a 4★ hunter** ("4성 헌터의 무기나 복장을 업그레이드").

---

# 4. EVERY NON-CAMPAIGN REWARD, by system

Ordered by how much is actually known. Class key:
**[R]** recovered from native · **[FP]** the game's own shipped text/pixels ·
**[1P-KR]** first-party Korean wiki · **[COMM]** community ·
**[FIX]** replica invention · **[UNK]** nobody has it.

## 4.1 Login Bonus / attendance — mostly **[UNK]**, with three structure facts

| fact | value | class · source |
|---|---|---|
| Calendar length | **28 days** in the replica | **[FIX]** `login-bonus.ts` |
| Calendar contents | — | **[UNK]** — the vsfan row "Cumulative Attendence Dates" names Rupee Lottery Tickets, 2~3★ Requests, 3★ Requests, Elite Requests, Veteran Tickets as what attendance *yields*, but **no amounts and no day-by-day table survives in any corpus** |
| **Consecutive-day structure exists** | vsfan item rows say "reaching your **2nd**/**4th**/**6th** consecutive login day" for Sharp Metal / Unscathed Shell / Burning+Scorching Flamestone | **[COMM]** ×1 page, 3 rows |
| **Rupee on day 1** | "reaching your **1st** consecutive login day" is a listed source of Rupee | **[COMM]** ×1 |
| **Rupee on day 3 as a new Hunter** | "reaching your **3rd** day as a new Hunter" is a listed Rupee source | **[COMM]** ×1 |
| Weekly scrolls from sign-in | "You get scrolls **weekly**, from daily sign in with **increasing star** as you progress in the month with a **10+1 in the third week**" (`forum 1422054`) | **[COMM]** ×1 |
| Day-7 4★ Selection ticket | `forum 1561517`: "Will I still be able to get the **4\* Selection ticket** on my **7th day**?" (a question — but the day-7 slot is corroborated by `forum 675557`, which discusses "day 7 reward" as real) | **[COMM]** ×2 |
| Monthly, not weekly | `forum 1167975`: "Rewards **stay the same** as they always have. The only difference is that now there is **not a weekly pattern anymore but a monthly** instead." | **[COMM]** ×1 — a **structure change**, dated only "recently" |
| Reset hour | `forum 1187734`: **16:00** for one player, **10 am** for another; a VS support reply says they are "under investigation about the reset time issue" | **[COMM]** + **[FP-support]** |
| 28-day "rainbow scroll" | `forum 675557` describes a **rainbow scroll** gating cumulative day rewards, and "It still says I am on day 28" | **[COMM]** ×1 |
| Veteran points from attendance | **40 points/day maximum** F2P; Guru 3 = **40 960** points ⇒ **1 024 days** | **[COMM]** `vsfan Veteran_Status` |
| Attendance reward claim UI | "press the '!' or '?' Button and then 'see all' in top right. Then you can **claim all outstanding achievement rewards**" (`forum 1160105`, 2019-05-31) — *"It's stopped being automatic."* | **[COMM]** + **[FP-support]**-adjacent |

**Two independent veteran-point figures that do not reconcile — recorded, not
resolved:**

| source | Guru 3 | daily/week rate | implied days |
|---|---:|---|---:|
| vsfan `Veteran_Status` (2019-09-23) | 40 960 | 40/day | **1 024** |
| `forum 1479784` (2021-01-10, author reports 1 069 days) | 67 520 | 320/week | 1 477 sign-ins |

Both are `[COMM]` ×1, from different years and authors. **Do not average them.**

**Notable: the Login Bonus calendar is the single largest untouched reward table
in the project** — §5 gap G1.

## 4.2 Arena / Fight Club — the best-documented non-campaign system

### 4.2.1 Rank rewards, 31 bands — **[COMM]** (namu main page, single transcription)

| rank | 파이트칩 | bonus | rank | 파이트칩 | bonus |
|---|---:|---|---:|---:|---|
| 1 | 2500 | 녹색 만다 800 | 551–720 | 1000 | 녹색 만다 **255** ⚠ |
| 2 | 2400 | 녹색 만다 650 | 721–950 | 900 | 녹색 만다 200 |
| 3 | 2300 | 녹색 만다 600 | 951–1250 | 800 | 녹색 만다 175 |
| 4–10 | 2200 | 녹색 만다 550 | 1251–1620 | 700 | 녹색 만다 150 |
| 11–20 | 2100 | 녹색 만다 500 | 1621–2120 | 650 | 녹색 만다 125 |
| 21–30 | 2000 | 녹색 만다 475 | 2121–2750 | 600 | 녹색 만다 100 |
| 31–50 | 1900 | 녹색 만다 450 | 2751–3600 | 550 | 녹색 만다 75 |
| 51–70 | 1800 | 녹색 만다 425 | 3601–4700 | 500 | 녹색 만다 50 |
| 71–100 | 1700 | 녹색 만다 400 | 4701–6100 | 450 | **고급 의뢰서 3** |
| 101–130 | 1600 | 녹색 만다 375 | 6101–8000 | 400 | 고급 의뢰서 2 |
| 131–180 | 1500 | 녹색 만다 350 | 8001–10300 | 350 | 고급 의뢰서 1 |
| 181–240 | 1400 | 녹색 만다 320 | 10301–13500 | 300 | **오르니톱터 연료 쿠폰 5** |
| 241–320 | 1300 | 녹색 만다 300 | 13501–17500 | 250 | 연료 쿠폰 4 |
| 321–420 | 1200 | 녹색 만다 275 | 17501–23000 | 200 | 연료 쿠폰 3 |
| 421–550 | 1100 | 녹색 만다 250 | 23001–30000 | 150 | 연료 쿠폰 2 |
| | | | below 30000 | 100 | 연료 쿠폰 1 |

Three currency regimes, cleanly bounded: **green Manda down to rank 4700 →
고급 의뢰서 (advanced requests) 4701–10300 → fuel coupons below 10301.**

⚠ **The 255 at 551–720 breaks the monotonic 250→200 descent.** `fc-economy
§2.2` quarantines it as a probable wiki typo with **no second source**.
**Preserve 255; never smooth it.**

### 4.2.2 Tier rewards — **[COMM]** ×2

| tier | 파이트칩 | 녹색 만다 |
|---|---:|---:|
| 브론즈 Bronze | *(absent)* | *(absent)* |
| 실버 Silver | 100 | 2 |
| 골드 Gold | 100 | 2 |
| 에메랄드 Emerald | 150 | 2 |
| 메트론 Metron | 150 | 2 |
| 만다(린) Mandaring | 200 | 2 |

**The blanks are editorial gaps, not zeros.** `namu-item-economy-tables` §1 is
explicit: *"The blanks are editorial gaps, not zero rewards. Do not publish 0."*

**Independent English corroboration** (`forum 1179899`, 2019-07-09): *"Each 6
victories at Mandarin Tier gives you **200 Fight Chips**"* — the namu Mandaring
row exactly. And the same thread's own arithmetic names the tier ladder:
*"enough to hit each grade win and metron grade wins two more times =
100 + 100 + 150 + 150 + 200 + 200 + 200 = 1100 a week"*. **Two languages, one
tier value, one ladder.**

### 4.2.3 Scoring and cadence — **[COMM]** ×2

win **+15** · loss **−8** · defence loss **−5~6** · revenge-loss or forfeit **−8**
· tier-up **6 wins regardless of losses** · **Sunday** settlement + reset ·
re-clearing 6 wins inside Mandaring **re-awards** the Mandaring reward.

### 4.2.4 Fight Club Shop — [COMM] ×2 sources, one with a second language

`vsfan Fight_Club_Shop` (2019-08-21, `oldid=5984`) — **7 rows, "replenished
every 12h"**:

| item | number | cost (fight chips) |
|---|---:|---:|
| Lantern's Trace / Akasha's Trace | 2 | **150** |
| Metron_Crystal | 1 | **1000** |
| 2-3 Star Request | 1 | **1500** |
| Elite Request | 1 | **500** |
| 2 star hunter's trace | 2 | **75** |
| Advanced skills advancement items | 3 | **25** |
| Expert skills advancement items | 3 | **75** |

Corroboration: `share-en-panels` §1.6.7, `199711` (WinJ, 2017-11-12) —
*"Fight Club Shop — Golden Hunter Traces (1st Priority) **150 for 2**; Metron
Crystal (2nd Priority) **1000 for 1**; Golden Hunter Materials **75 for 3**"*.
**Trace price 150/2 = 75 each, in both sources, six years apart.**

Also: 4 purchases/day, one every 6 h, 5 traces each (`forum 1179899`) — the
**per-purchase trace count is 5**, vs the wiki's 2. **Different eras or different
stock rows; unresolved.**

### 4.2.5 What is NOT arena

- **Entry cost**: 1 BP — **[FIX]** only (`ARENA_BP_COST`). No original.
- **"Honor"**: does not appear in any source. The namu table's currency is
  **파이트칩 (fight chips)**. The replica's `honor 10` has **no source**, and
  `fc-native-2026-10-05.md` §1.4 **forbids** deriving it from these tables.
- **Rating ±10**: contradicted by namu (+15/−8). **[FIX] and wrong.**

## 4.3 Login-Bonus-era supply and Special Supply

| fact | value | class |
|---|---|---|
| Special Supply is claimed at the Supply Station | `forum 127470`: *"please **collect your rewards on Special Supply section of Supply Station**!"* | **[COMM]** ×1 |
| Recommendation rewards flow into Special Supply | same | **[COMM]** ×1 |
| Special Supply contents | — | **[UNK]** |
| Special Supply triggers | — | **[UNK]** — the replica's "10 gold per first clear" is a **[FIX]** |
| Supply Depot / Hunter Supply Station — its own reward rows | — | **[UNK]**; `vsfan Hunter_Supply_Station` and `Hunter_Supply_Office` are **navigation stubs with no reward content at all** |

## 4.4 Episode chapter rewards — **[R]**, the one complete original reward table

From the original `R_EPISODE.jet` (SHA `7f4362cd…`, 18 episodes / 128 stories /
147 unique ids), quoted from `rewards-economy-2026-10-05.md` §B.5:

| ch | reward | ch | reward |
|---|---|---|---|
| E01 | **GC2 ×3** | E10 | SK13 ×30 + SK23 ×30 |
| E02 | **FMD1 ×30** | E11 | SK33 ×30 + SK43 ×30 |
| E03 | GC3 ×3 + GC4 ×3 | E12 | EM02 ×2000 |
| E04 | **GC8 ×1** | E13 | LCOIN ×20 |
| E05 | **AIRSHIP_TICKET ×20** | E14 | OV1 ×30 |
| E06 | OV1 ×10 | E15 | GC9 ×1 |
| E07 | CERUM01 ×20 | E16 | GC10 ×1 |
| E08 | CERUM02 ×20 | E17 | GC11 ×1 |
| E09 | CERUM03 ×20 | E18 | **RP1 ×100000** |

Identities proved: **GC2** = an owned Lottery coupon · **FMD1** = the free-Manda
display identity · **RP1** = the gold display identity. **Item metadata,
`use_type`, `effect` and redemption for every one of these remains [UNK]** —
which is why the replica correctly refuses the coupons (§4.8).

## 4.5 Guild / Guild Blitz / GVG

| fact | value | class · source |
|---|---|---|
| Contribution **rewards are separate from guild levelling** | "The guild contribution amount for **Leveling up is 3,120k** … whereas the amount for the **guild contribution reward is 5,000k**. They're really not the same thing." | **[COMM]** `forum 1083786` |
| Reward gauge **resets** at the 4th (final) star | *"[Vendor/support] … 'Contribution Rewards' gauge bar **\*resets\*** once the guild contribution reaches the **fourth(final) star** at the end. This does not affect the guild level, but **each guild member will receive a reward whenever it reaches a star**."* | **[FP-support]** — a first-party support answer, verbatim in `forum 1083786` |
| Contribution track numbers | 63 713 539 / 75 620 000 progress; **3 713 539 / 5 000 000** reward thresholds; members 21/40 | **[FP]** pixels (per `cost-ledger` §1.11) — **progress only, no payout named** |
| Fuel support | request total **60 fuel**, max **5 guildmates**, 12 fuel/member | **[FP]** shipped 2.8.0.1 help + **[COMM]** `forum 1161193` |
| Rupee donation | exists, "extremely expensive, NOT recommended" | **[COMM]** FAQ — **no figure** |
| **Guild Blitz** exists and pays **special coins** | `forum 1569774`: *"trade at shop **298 special coin** for a 4\* recruitment scroll. u get special coin by … **rewards from doing guild-blitz**"* | **[COMM]** ×1 |
| Blitz special coin **price** | 298 per 4★ recruitment scroll | **[COMM]** ×1 |
| Blitz **reward amount** | — | **[UNK]** |
| Blitz roster snapshot on signup | confirmed by a player and by support: *"once you sign up, it takes a snapshot of your roster for the week"* | **[COMM]** + **[FP-support]** `forum 1317799` |
| `GetGuildPrices` reference route | — | **[UNK]**, route absent from the replica |

**There is no "Guild reward" table anywhere.** Guild has structure and cadence
and **no numbers**, except the two contribution thresholds above.

## 4.6 Mirage Ruins

| fact | value | class |
|---|---|---|
| Currency | **신기루 조각 (mirage shard)** | **[1P-KR]** `namu-first-party` §3.5 |
| Mirage shop stocks | 특급 의뢰서, **메트론 결정체**, 강화 재료, 도구 상자, 고급 도구 상자, 결정, **3성 헌터 흔적**, 할리의 흔적 | **[1P-KR]** |
| Ruin type → material | Cryo→수속/등껍질 · Heat→**화속**/화염석 · High-voltage→전속/금속조각 · **Gold→루피 (varies by difficulty)** · Metron→메트론 조각 | **[1P-KR]** |
| Floors | 3 stages high, 6 deeper; not strictly sequential | **[1P-KR]** |
| Only your **strongest** hunter may be used on a floor | stated outright | **[1P-KR]** |
| Difficulty auto-computed from total combat power | "but even when your combat power exceeds the dungeons', team composition can still make you fail" | **[1P-KR]** |
| Uncleared floor → you stay until **midnight**, then reset/retreat | | **[1P-KR]** |
| A **Major Goal** "highest floor" paid **65 Manda + 60 traces of a 4★ Defender** | `forum 897813`: *"my major goal finnally got a red dot … it say highest floor … just got **65 manda and 60 traces** of the 4\* Defender from it"* | **[COMM]** ×1 — **the only quantified Mirage-adjacent reward found** |
| Mirage shop price of traces | "250–300 fragments for 10 of each material" (a *suggestion*, not a price) | **[COMM]** ×1, explicitly a proposal |

## 4.7 Fishing

| fact | value | class |
|---|---|---|
| Purpose | earn **루피**; non-fish drops include **메트론 결정체**, "확률이 극악하다" (extremely rare) | **[1P-KR]** `namu-item-economy` §6 |
| **Fish are auto-sold on capture** now | "예전에는 물고기를 얻고 보관했다가 … **물고기를 낚자마자 바로 판매가 된다**" | **[1P-KR]** — a real content change, and the replica's catch-inventory model contradicts it |
| Six species, price-ordered | 뼈살이 빙어 < 흰수염 메기 < 메트론 은어 < 칼날 뱀장어 < 짝발 민물게 < 은쟁반 가지미 | **[1P-KR]** |
| Rupee/crown variants by size | 은관 / 금관 | **[1P-KR]** |
| Catches can be **영웅 강화 재료** (등껍질, 금속조각) instead of fish | | **[1P-KR]** |
| `fish_id` / prices / grades | — | **[UNK]** — namu's two fish tables are **empty**, a real zero (namu site search works, unlike Miraheze) |
| Bait economy | "**6500 ruppe for 10 bait**"; "**6 manda** for 6.5k rupee"; regular bait 10–20 s wait, high-bait 5 s; average return "only 3k" | **[COMM]** ×1 thread, 4 numbers |

## 4.8 Systems that are correctly refused by the replica

For completeness, so nobody "fixes" them into fabricated successes:
`/fishing/*` (all but `GetInven`/`GetRecord` empty arrays), `/gem/*` (all),
`/reference/GetGuildPrices`, `/reference/GetCardOvercome` + `/gym/Overcome`,
`/reference/GetSkinRef` + `/skin/*`, gem-gacha references, gacha mileage,
`/shop/SellCard`, `RankUpBundle`, four unlisted gacha banners.

**Of these, `/shop/SellCard`, the three gem-gacha references and the four gacha
banners answer `result_code: 1`** — a *fabricated success*, not an absence
(`cost-ledger` §5.2). That is the most dangerous state in the whole reward
surface and it is **not** fixed by this note.

---

# 5. CURRENCY — the complete list, with every source and sink found

## 5.1 The list

| # | Currency | Korean | Identity | Sources found | Sinks found |
|---|---|---|---|---|---|
| 1 | **Rupee** | 루피 | the main soft currency; vsfan *"a small, shiny coin and the main currency of all the tribes"* | expedition areas (**always**), daily assignments, Golden Abyss, FC ranking, 1st consecutive login day, 3rd day as new Hunter, Rupee Lottery Tickets, selling items, ads | **5000 Rupees** → fuel · 20 000 → Rupee corner · **30 000** → Search reset · 5000–8000 → fuel recharges · 5000–4000 → shop popups · 5000 → challenge reset · 60 000 → awakening · 9 000–80 000 → transcendence · 1 000–60 000 → star advancement |
| 2 | **Manda** | 만다 | premium; **split free / paid** | FC rank + tier rewards (free Manda), stages, events, IAP, sharing BTB/WI episode completions | **10 Manda → Rupee** · **5 Manda → fuel** · gacha **30** single / **300** bundle · Abyss reset **30** · high bait · dorm expansion · fuel 5 → 7 escalation after 5 refills |
| 3 | **Free / green Manda** | 녹색 만다 | the earnable half | FC rank ladder (800→50) and tier ladder (flat **2**) | 4★ Transcendence Tickets are **only** buyable with free Manda (`forum 1140439`) |
| 4 | **Fight Chip** | 파이트칩 | FC currency: *"given as consideration for intense battle"* | FC ranking (**31 bands**), 6 wins per tier, FC battles, daily goals | FC Shop (7 rows, §4.2.4) |
| 5 | **Metron Fragment** | 메트론 조각 / 결정 | | expedition areas (all), ruins, FC shop 1500/15 | skill training (all bands), transcendence (**exactly 10× the crystal count**) |
| 6 | **Metron Crystal** | 메트론 결정체 | *"a very rare, pure Metron found in the deepest parts of the abyss"* | Cryogenic / Electric / Volcanic Abyss (Mirage shop too) | transcendence, awakening; value **1000** |
| 7 | **Mirage shard** | 신기루 조각 | | Mirage Ruins | Mirage shop |
| 8 | **Helium capsule** | 헬륨 캡슐 | **explicitly not fuel** — a different aircraft | general stages, Episode E05 (**×20**), missing-hunter ruins | Search: **10 / 32 / 30** by grade |
| 9 | **Trace** | 흔적 | per-hunter, grade-gated (namu §5.1–5.4 by ★) | evaluation/elite requests, FC shop, Mirage shop, Exchange | `/shop/PieceExchange` — **20 / 40 / 80 / 160** by grade (`(2^n)×10`) |
| 10 | **Challenge Invitation** | — | FC entry ticket | Events, Hunter Shop, Daily Rewards, Attendance Supply | **1 ticket → 2 invitations** |
| 11 | **Fuel Ticket** | — | | Expedition areas, Events, Hunter Shop, Daily Rewards, Daily Goals | **1 ticket → 60 fuel** |
| 12 | **Rupee Lottery Ticket** | — | *"the winner of the lottery receives a large amount of rupees"* | Attendance dates, Events, Expedition Areas, Daily Goals | **1 → 5 000 Rupees** |
| 13 | **Veteran Ticket** | — | a recommendation | small chance from other tickets | **+50 Veteran Points to another Captain** |
| 14 | **Veteran Point** | — | | daily goals, daily rewards, veteran tickets, packages | Veteran level; **40/day max** |
| 15 | **Elite / 2~3★ / 3★ Request** | 의뢰서 | Lottery Mouse recruitment slips | Events, Expedition Areas, FC Shop, Hunter Shop, Daily Rewards, Attendance, **Arena Rank Compensation** | Lottery Mouse |
| 16 | **Evaluation Request** | — | a "background check" on hunters | Expedition Areas, Hunter Shop, Daily Rewards, Arena Rank Compensation | Lottery Mouse |
| 17 | **Stimpack** | — | *"makes you attack as full rage"* | — | combat buff |
| 18 | **Special coin** (Guild Blitz) | — | | guild-blitz rewards | **298 → 4★ recruitment scroll** |
| 19 | **Fuel** | 오르니톱터 연료 | expedition/AP | daily assignments, **5 Manda**, **5000 Rupees**, events, tickets, Supply Station, ads, waiting | expedition + abyss entry |
| 20 | **Coupons** | — | namu: 비밀 코너 prices **5 gold** / **20 chips** | shop | shop |

## 5.2 골드 vs 루피 — resolved, with a caveat

The brief asks namu's distinction to be settled. It is, and the answer is
**not** that they are two currencies:

- **루피 (Rupee)** is the in-game soft currency: *"a small, shiny coin and the
  main currency of all the tribes"* (vsfan `List_of_Blustone_Items`, Currency
  table). The namu wiki and the English wiki **use the same word** for it.
- **"골드" appears in namu and in the English board in two different senses:**
  1. as a loose synonym for 루피 in player speech (`forum 888621` "160k→90k",
     `forum 1187250` "6500 ruppe", `forum 369923` "gold medals" for an event);
  2. as a **named Market corner** — namu `비밀 코너` (Secret corner) at **5 골드**,
     and `루피 코너` (Rupee corner) at **20 000**.
- The namu arena table's third column is **녹색 만다** — green Manda — **not**
  골드. So the arena ladder's "bonus" currency is Manda, and no source uses 골드
  as a separate wallet.

**Verdict: there is no separate "Gold" currency. 루피 is the gold; "골드" is a
synonym in speech and a shop-corner label.** The replica's `user.gold` field is
correctly the Rupee wallet, and the `IT_CO` coin icon is correctly the Rupee
icon (`AGENTS.md` §128, the RP1 = gold display identity).

**Caveat:** this rests on two corpora (vsfan 2019, namu 2017–2021). No native
string table was read for this lane, and `native-all-strings.tsv` is
printable-ASCII with **zero Hangul** (guard rule 12), so a locale-string check
was not possible. If a distinct 골드 wallet exists, it is not visible in any
language corpus the project holds.

## 5.3 Currency flow graph (text)

```
IAP ──────────────────────────────► PAID Manda ──┐
                                              ├──► gacha 30 / 300
sharing BTB / WI episode completion ─► FREE ─────┤
                                              ├──► fuel         (5 Manda, or 5000 Rupee)
                                              ├──► Rupee        (10 Manda)
                                              ├──► Abyss/Search reset 30
                                              ├──► high bait
                                              └──► dorm expansion
FC RANK LADDER (31 bands, Sunday) ──► FREE Manda │
        + Fight Chips 100…2500        800→50    │
FC TIER LADDER (6 wins/tier) ───────► 2 FREE Manda│
FC battles ────────────────────────► Fight Chips │
DAILY GOALS ───────────────────────► Fight Chips │
                                        + Veteran Points (40/day)
                                           + fuel
                                           + Rupee

EXPEDITION AREA  ── always ──────► Rupee
                ── by chance ────► Elite / Evaluation Requests
                                    Rupee Tickets, Metron Fragments,
                                    region hunter's traces,
                                    one of 12 skill materials (digit rule §3.1)
STAR CHESTS 10/20/30  ──────────► ???  (see §1.5 — 15 of 15 cells UNKNOWN)

FIGHT CLUB SHOP  ◄── Fight Chips (7 rows, 12h refresh)
MARKET CORNERS   ◄── Rupee (20 000 / 1000 / 1000 / 5)
                ◄── Fight Chips (1500 / 3000 / 20)
SEARCH  ◄──────────  Helium capsules  10 / 32 / 30 by grade
         ──────────► traces (1 or 10 per victory)
ABYSS   ◄──────────  20 fuel per entry
MIRAGE  ◄──────────  Metron materials, Rupee (Gold type)
         ──────────► mirage shards ─► Mirage shop
FISHING ◄──────────  bait (rupees or Manda)
         ──────────► fish ─► auto-SOLD for Rupee  (§4.7)

GUILD  ────────────► contribution ─► 4 stars, gauge RESETS
         ───────────────────────────► every member paid at each star (contents UNK)
GUILD BLITZ ───────► special coins ─► 298 per 4★ recruitment scroll
ATTENDANCE ────────► scrolls (weekly, rising grade, 10+1 in week 3)
         ──────────► 2nd/4th/6th consecutive day ⇒ mid-grade skill material
         ──────────► 1st day & 3rd-new-hunter day ⇒ Rupee
         ──────────► 7th day ⇒ 4★ Selection Ticket
EPISODE CHAPTER ───► GC2×3 / FMD1×30 / GC3+GC4×3 / GC8×1
                     AIRSHIP_TICKET×20 / OV1×10 / CERUM01-03×20
                     SK13+SK23×30 / SK33+SK43×30 / EM02×2000 / LCOIN×20
                     OV1×30 / GC9 / GC10 / GC11 / RP1×100000
```

**The flow graph's one glaring hole is the star-chest node: it is drawn as `???`
because fifteen of fifteen cells are unknown.** It is the only reward node in
the whole graph with no content at all, and it is the node the replica invented.

---

# 6. EXPLICIT GAP LIST, ranked

Ranked by *what would most change the replica*, not by how easy it is.

### G1 — 🔴 The Login Bonus calendar. **Largest untouched reward table in the project.**
**Status [UNK].** Nothing anywhere carries the day-by-day contents.
**What would settle it:** any screenshot of the Daily Sign-In / 출석 board showing
a day cell and its item; or the original `/supply/V2_GetSupplyInst` /
`LoginBonusRef` payload from a revival project's capture; or the namu
`블루스톤/아이템` attendance sub-page (never followed — `namu-browser-partial`
§5). The replica publishes **28 × 100 gold**, entirely invented, and the original
is documented to contain **scrolls, requests, veteran tickets and skill
materials** (`vsfan List_of_Blustone_Items` "Cumulative Attendence Dates" rows).

### G2 — 🔴 The 15 campaign star-chest payouts.
**Status [UNK]** for all 15 cells; thresholds **[COMMUNITY×3 + native]** for
all 15; the **30-star identity disputed** (§1.3).
**What would settle it:** the original `achieve_reward[]` rows. Realistically:
one screenshot of the regional reward panel per threshold, or a capture of
`/reference/GetArea` from any surviving server. Secondary: a dated Korean patch
note, since namu spans 2017–2021 and vsfan is 2019 — **the two disagree, and the
disagreement may itself be the answer** (a change between eras).

### G3 — 🔴 Whether the 30-star reward is a hunter or a 만다나 의뢰서.
**Status [UNK], two sources in direct conflict.**
**What would settle it:** one screenshot of a 30-star claim popup, or the
`card_list` field of any original `achieve_reward` row (the native struct
**already has a `card_list`** — `CSRGameStage::ACHIEVE_REWARD+0x28`,
`bootstrap.ts:582`). **A populated `card_list` at index 2 would prove the hunter
reading outright**; that is the single highest-value byte in the whole reward
surface.

### G4 — 🟠 The campaign's true extent: 50 vs 190 stages.
**Status [UNK] / contested.** namu (first-party KR) says **50 dungeons as of
2019**; vsfan lists **190 areas in 19 regions**; the replica publishes **50**.
**Consequence for rewards:** a 190-stage ladder implies ~57 regional rewards, not
15.
**What would settle it:** `analysis/recovered-reference/campaign-stages.csv` is
from the **base APK's `LEVELING.jet`**, which is a *config* file — the server's
`GetStage` may well have published far more. A single original
`/reference/GetStage` response from any revival project closes this.

### G5 — 🟠 Guild: every payout.
**Status [UNK].** Structure, cadence and the 4-star resetting gauge are known
(**[FP-support]**), and two contribution thresholds (3 120k level-up vs 5 000k
reward) are known, but **nothing says what a contribution star pays**, and
**Guild Blitz's reward amount is unknown** despite the special-coin sink being
priced at 298.
**What would settle it:** the absent `/reference/GetGuildPrices` payload; or a
screenshot of the Contribution Rewards panel.

### G6 — 🟠 Mirage: floor rewards and shop prices.
**Status [UNK].** The currency, the shop's stock list, the floor rules and the
element→material mapping are all **[1P-KR]**, but **no price and no per-floor
reward exists in any corpus**. The only quantified adjacent fact is one player's
"65 Manda + 60 traces" from a Major Goal.
**What would settle it:** the namu `미러지 상점` sub-page (never followed), or a
Mirage shop screenshot.

### G7 — 🟠 Fishing: ids, prices, grades.
**Status [UNK]** and structurally blocked — namu's two fish tables are **empty**,
the site search returns 0, and the original `fish_id` set is not in any recovered
cache. **Also a live contradiction:** namu says fish are **auto-sold on capture**,
while the replica implements a catch-inventory model.
**What would settle it:** `ParsePrice`'s `fish_id/b_price/s_price/g_price` from
any original `/reference/GetPrice` capture, or a Market sell screenshot with the
per-species price legible.

### G8 — 🟡 Special Supply contents and triggers.
**Status [UNK].** The claim location is known (**[COMM]**), the contents are not.
The replica's "10 gold per first clear" is a pure **[FIX]**.

### G9 — 🟡 Veteran ladder points (two irreconcilable figures) and the arena entry cost.
Guru 3 = 40 960 @ 40/day (vsfan) vs 67 520 @ 320/week (`forum 1479784`).
Arena entry cost 1 BP is **[FIX]** with no original counterpart.
**What would settle it:** a Veteran-status panel screenshot; one arena-entry
frame showing the ticket type consumed.

### G10 — 🟡 The three "fabricated success" shop/gacha routes.
`/shop/SellCard`, `/reference/GetPaidGemGacha`, `...Mileage`, `...DailyFree`,
`/lobby/GetGemGachaInfo`, `/shop/GachaGeneral`, `GachaEvent`, `GachaSpecificList`,
`GetGachaEventRef2` all answer `result_code: 1`. **Not a gap in knowledge — a gap
in the replica that knowledge would not close.** Listed because it is the only
item here that silently corrupts state.

### G11 — 🟢 Market corner contents.
Prices are known (4 corners × 2 currencies); **what is in each corner is
[UNK]**. Low impact — a shop listing, not a progression gate.

### G12 — 🟢 Gacha odds in the server.
The community ladder (0.07 % → 0.3 % → 0.33 %) is well sourced
(`forum-en-mining-pass2` §3.4, vendor-reported). The replica **publishes no
odds at all**, which is honest. Closing this needs the original pool table.

---

# 7. WHAT THE REPLICA PUBLISHES TODAY (read-only report)

Read from `server-ts/src` on 2026-10-09. **Nothing here was edited; the build and
tests were not run.**

## 7.1 The campaign reward block — `bootstrap.ts`

`FIXTURE_CHEST_ITEMS` (`bootstrap.ts:530-534`):

```ts
export const FIXTURE_CHEST_ITEMS = [
  { id: "914", title: "★4 Transcendence Ticket", qty: 1, gold: 300 },
  { id: "913", title: "★3 Transcendence Ticket", qty: 1, gold: 200 },
  { id: "912", title: "★2 Transcendence Ticket", qty: 1, gold: 100 },
] as const;
```

`areaAchieveRewards()` (`bootstrap.ts:630-648`) derives all three rows per area:

```ts
achieve_cnt: stageCount * (index + 1),   // 10 / 20 / 30 for every area
gold: item.gold,                          // 300 / 200 / 100
free_iap: 0, iap: 0,
item_list: [{ id: item.id, qty: item.qty }],
card_list: [],                            // deliberately empty
```

**Assessment against this lane's evidence:**

| element | status |
|---|---|
| three rows per area | ✅ **now externally confirmed** (`vsfan Expedition_Area` ×3 captures + native `S*(i+1)`) |
| `achieve_cnt` = 10 / 20 / 30 | ✅ **now externally confirmed** (same sources) |
| `gold` 300 / 200 / 100 | ❌ **no source whatsoever** — pure invention |
| `item_list` = Transcendence Tickets 912/913/914 | ⚠ **ids are [RECOVERED]** (`CHAR_STR_RO` rows); **the link to star chests has no source** |
| `card_list: []` | ⚠ correct given the replica's roster, but **wrong against vsfan's 30-star = hunter** — a populated `card_list` is exactly what §1.3 predicts |
| per-area differences | ❌ **all five areas get the identical triple**; no source shows they should differ, and no source shows they shouldn't |

**Net: 2 of 5 elements confirmed this lane, 1 has recovered ids but no
justification for its placement, 2 are invention.** The invented gold is the
number most likely to be mistaken for real.

## 7.2 Other campaign-reward constants (for the owner's cross-check)

| constant | value | file | this lane's verdict |
|---|---|---|---|
| `FIXTURE_STAGE_CLEAR_GOLD` | **10** | `state.ts` | **[FIX]**, no source |
| `LOCAL_CAMPAIGN_FIRST_CLEAR_TEAM_EXP` | **30** | `campaign-reward-policy.ts` | **[FIX]**, no source (now consistent between `/reference/GetStage` preview and settlement — AGENTS §202) |
| stage hunter EXP | **10** flat | `bootstrap.ts` | **[COMM]** says **7…32, region-graded** (`cost-ledger` N6) |
| AP per stage entry | **1** flat | `bootstrap.ts` | **[COMM]** says **6** (areas 1–40) → **12** (171–190) (N5) |
| search capsule cost | **1** | `hunter-search.ts` | **[1P-KR]** says **10 / 32 / 30** by grade |
| trace thresholds | **10 / 20** | `hunter-traces.ts` | **[COMM]** ×2 says **20 / 40** (exactly 2.0×) |
| arena rating | **±10** | `arena-service.ts` | **contradicted**: namu says **+15 / −8** |
| arena weekly anchor | **Thursday** | `arena.ts:76` | **contradicted**: namu says **Sunday** |
| arena league reward | **`honor: 0`** | `arena.ts:96` | **[FIX]**; `honor` is not a currency in any source — the ladder pays **Fight Chips + free Manda** |
| arena rival refresh | `{price_type:2, price:100}` | `arena-service.ts:9` | **[FIX]**; namu's 2→4 manda is a *different* purchase (shop listing refresh) |
| login calendar | **28 × 100 gold** | `login-bonus.ts` | **[FIX]**; §4.1 — contents are **[UNK]** and documented to be scrolls/requests/materials |
| VIP EXP per claim | **20** | `login-bonus.ts` | **[R]** — the one recovered login value |

---

# 8. Provenance ledger

Every claim above carries a source and a class. Machine-readable companions:

| artefact | what |
|---|---|
| `recovered-assets/vsfan-reward-2026-10-09/*.html` + `*.txt` | 65 archived vsfan pages, raw bytes + extracted text |
| `…/*__<timestamp>.html` | the 26 exact-URL CDX captures for the 9 re-enumerated titles |
| `analysis/research/base-stats-visual-hunt/campaign-reward-mining/screen-hits.json` | the body-only keyword screen, with the positive-control result and the per-file context |
| `…/dump-star-threshold.txt`, `dump-login-arena.txt`, `dump-goals.txt`, `dump-supply-guild.txt`, `dump-mirage-fish.txt`, `dump-star2.txt` | the verbatim context dumps each table above was read from |
| `tools/campaign-reward-mining-2026-10-09.py`, `tools/campaign-reward-dump-2026-10-09.py`, `tools/vsfan-reward-fetch-2026-10-09.py`, `tools/vsfan-reward-cdx-2026-10-09.py`, `tools/vsfan-reward-extract-text.py` | the four readers. GET-only, read-only against the archive |

**Per-reading provenance for the headline claim** (vsfan `Expedition_Area`,
`oldid=3233`): three Wayback captures
`web/20190826070239id_/…` (38 733 B, `9faa58b1573e179c`),
`web/20191020212117id_/…` (38 733 B, `bc5587b54ed7ce1c`),
`web/20191214142617id_/…` (38 778 B, `ecda5055da781539`), all HTTP 200,
all from `http://web.archive.org` (https is refused on this host).

---

# 9. Honest bottom line

**One real campaign-reward fact was recovered this lane:** the regional star
rewards are **three**, at **10 / 20 / 30 total stars**, confirmed by an original
English source across **three dated captures** *and* independently forced by the
client's own compiled arithmetic. That is now the best-evidenced number in the
campaign reward system, and it validates the replica's `achieve_cnt` derivation.

**One real conflict was found and is not resolved:** the 30-star reward is
**the region's hunter** (vsfan ×3, EN) or **a 만다나 의뢰서** (namu ×1, KO). The
native `ACHIEVE_REWARD` struct has a `card_list` field at `+0x28` that would
settle it instantly; nothing in this project's evidence fills it.

**Fifteen of fifteen campaign payout cells remain `[UNKNOWN]`.** The replica
publishes `300 / 200 / 100` gold for them. **No source in any language, any
year, any corpus this project holds, states that a star chest pays gold.**

**The single largest untouched reward system is the Login Bonus calendar** —
the replica invents a 28 × 100-gold table, while three independent sources say
attendance yields scrolls, recruitment requests, veteran tickets and skill
materials.

**Coverage counters unmoved: heroes 1/113, accessories 1/100, monsters 0/22.**
Nothing in this note was allowed to move them. §1's regional-reward table is a
reward-structure fact, not a base stat. **No append to
`polluted-observations.md`; `coverage.md`, every TSV, `server-ts`, fixtures, the
APK, seeds, the emulator, the phone and Ghidra were not touched.**

**Read-only confirmation for `server-ts`:** `git status --porcelain -- server-ts`
was read before and after and every access was a `read`/`grep`. No file under
`server-ts/` was written by this lane, and `npm run build` / `npm test` /
`npm run dev` were not run.