# Official `event_en` board bodies, pass 3 — four more bodies, zero stat rows (2026-10-05)

**Lane:** third pass of the mining series begun in
[`official-posts-2026-10-05.md`](official-posts-2026-10-05.md) §1.3 and continued in
[`event-board-bodies-2026-10-05.md`](event-board-bodies-2026-10-05.md) (pass 2).
Pass 2 recovered five bodies (`1003633`, `1008954`, `989396`, `995273`, `999764`)
and left **13** board bodies unfetched. This pass reads **four** of them:
`1008972` Halloween in Midgard!, `999762` Schumann's Marvelous Lootbox,
`995291` October Package, and `75679` the "[Notice] How to Use the Events
Section" rules post.

**Era rule** (`stat-version-context.md`): the three 2018 posts are Sept–Oct 2018,
**PRE-rebalance** (the rebalance took hold after 2019-09-05). `75679` is a
**2017.07.05** post read in its **2018-10 revision** (see §1.4) — still
PRE-rebalance, and in any case pre-dates the 2018 *Blustone 2* rebrand. Nothing
here is POST-era. Every numeral in §1 is **economy / drop / gacha / shop context
only** — see §4.

**Budget honoured:** **4 body fetches total**, all four successful, zero
retries. **12 exact-URL CDX queries** (4 ids × 3 URL forms, per the pass-2
method note in §2.3 of that document). CDX failures **0**; timeouts **0**; 503s
**0**. No query was re-run, no throttling bypass attempted. No server, APK,
seed, emulator, phone, Ghidra, native-library or state operation.

---

## 1. PURE — verbatim body text and reward tables

Everything in §1 is a **direct transcription** of the captured post body. HTML
entities were decoded (`&rsquo;`/`&lsquo;`→`'`, `&ldquo;`/`&rdquo;`→`"`/`,
`&nbsp;`→space, `&amp;`→`&`, `<br />`→line break); no other change. `<p>`
boundaries became line breaks. `★` is the original glyph.

> **Shared markup fact, recorded without interpretation.** Every body is wrapped
> in an XE component marker of the form
> `<div class="document_<srl>_<rev> xe_content">` / `<!--BeforeDocument(<srl>,<rev>)-->`.
> Observed: `document_1008972_67474`, `document_999762_67474`,
> `document_995291_67474`, `document_75679_208`. The identical `67474` across
> three different 2018 documents suggests a board/component revision counter
> rather than a per-document value. **Unverified; not a game field.**

### 1.1 [Event] Halloween in Midgard! — attendance + limited-recruit + weekly purchase bonus

- **`document_srl` 1008972**, board row **Sticky** (board date **2018.10.19**,
  views **3251** as of the pass-2 index capture)
- **Archive used:**
  [2018-10-25 01:57:03 capture](http://web.archive.org/web/20181025015703/http://bs.visualshower.com/index.php?mid=event_en&document_srl=1008972&l=en)
  of `http://bs.visualshower.com/index.php?mid=event_en&document_srl=1008972&l=en`.
  Four `index.php`-form captures exist, incl. `20181021134401`, `20181023222707`
  and `20181225003552`; the permalink form exists but is **302-only** (§2.4).
- **Post metadata (author / posted time / votes / comment count):** **not
  captured this pass** — the extraction was body-only and the 4-fetch budget was
  spent. Board date above is quoted from the pass-2 index map, not from this
  capture.
- **Event period (verbatim):** `October 19th 18:00 ~ November 2nd 15:00 (UTC+9) (15 days total)`
- **Era:** PRE-rebalance.
- **Attachments:** 3 JPEGs, all names only (no image bytes fetched, no OCR).
  Banner `미드가드할로윈축제_600x343_en.jpg`; two **hash-named** hunter-art files
  `72717abfd0243270a18c3a6af00cee58.jpg` and
  `7a441e0b2db3517c6cb41e5a3610db94.jpg`. The hash filenames carry no identity,
  so every hunter name below comes from the body text alone.

**Full body, verbatim:**

> Hello! Midgard's Captains!
>
> We are approaching the end of October, the season of Halloween! Here are the
> details of our 2-week-long event to celebrate Halloween in Midgard!
>
> `<Event Period>`
> October 19th 18:00 ~ November 2nd 15:00 (UTC+9) (15 days total)
>
> 1. New 2018 Halloween-Limited Hunters!
>
> Say hello to our new hunters with cool Halloween costumes! Check out
> "Jack-O'-Lantern" designed by Nene by putting a huge pumpkin on Lantern's head
> and "Broom Witch Denali" who has finally found a broomstick and turned herself
> into a witch!
>
> The new Halloween-limited hunters will be available at the Lottery Mouse's
> Recruit Hunters section. Available hunter traces will change during the event
> so don't forget to check the date!
>
> - Halloween-limited hunters
>   Jack-O'-Lantern(★3), Broom Witch Denali(★3), Halloween Witch Riko(★2)
>
> - Recruiting Chances UP!
>   ★3 Halloween-limited hunters recruiting chances 500% UP!
>   All ★3 hunters recruiting chances 200% UP!
>
> - On the first recruit, Transcendence +1!
>   Jack-O'-Lantern(★3), Broom Witch Denali(★3)
>
> - On 10+1 recruit, the following hunter traces will be given(UTC+9):
>   [Oct 19th 18:00 ~ Oct 26th 15:00] 10 traces of Jack-O'-Lantern
>   [Oct 26th 15:00 ~ Nov 2nd 15:00] 10 traces of Broom Witch Denali
>
> 2. Halloween Attendance Gift!
>
> In celebration of Halloween, daily attendance gift will be given to all
> Midgard Captains!
>
> During the event period of 15 days, 20 Manda will be available at the Special
> Supply each day. If you play every single day during the event, you will
> receive a total of 300 Manda!
>
> \*\* Please restart the app each day to receive the daily attendance gift!
>
> - Halloween Bonus Gift
>
> During the event, there will be a bonus gift with the first purchase of each
> week(UTC+9)!
>
>   - 1 Special Request, 40 Jack-O'-Lantern's Trace (Oct 19th 18:00 ~ Oct 26th 15:00)
>   - 1 Special Request, 40 Broom Witch Denali's Trace (Oct 26th 15:00 ~ Nov 2nd 15:00)
>
> Happy Halloween with the Halloween-limited hunters!
>
> Thank you.

**`<Halloween Bonus Gift>` as a two-row table, verbatim:**

| Week window (verbatim) | First-purchase bonus (verbatim) |
|---|---|
| Oct 19th 18:00 ~ Oct 26th 15:00 | 1 Special Request, 40 Jack-O'-Lantern's Trace |
| Oct 26th 15:00 ~ Nov 2nd 15:00 | 1 Special Request, 40 Broom Witch Denali's Trace |

### 1.2 [Event] Schumann's Marvelous Lootbox — a **probability-free** prize list

- **`document_srl` 999762**, board row **No. 434** (display index, **not** an id),
  board date **2018.10.05**, views **428**
- **Archive used:**
  [2018-10-25 17:54:24 capture](http://web.archive.org/web/20181025175424/http://bs.visualshower.com/event_en/999762)
  of `http://bs.visualshower.com/event_en/999762` — one of the few ids whose
  **permalink form itself returns 200** rather than a 302.
- **Post metadata:** **not captured this pass** (see §1.1).
- **Event period (verbatim):** `Oct 5th 15:00 ~ Oct 12th 15:00 (UTC+9)`
- **Era:** PRE-rebalance.
- **Attachment:** 1 JPEG banner, `NEW_슈만의_보급상자_600X343_en.jpg`.

**Full body, verbatim:**

> Hello, everyone!
>
> Schumann has prepared something for a more successful expedition. During the
> event period, use fuel and Manda to earn a Lootbox and in it awaits various
> prizes!
>
> `<How to Participate>`
> 1. Get the 'Mystery Lootbox' every time you spend 30 Manda or 200 fuel!
> 2. Accept your rewards through your Special Supplies.
>
> `<Prize List>`
> - 1 Legendary Request (3★)
> - 1 Special Request (2★)
> - 1 Metron Crystal
> - 3 Elite Requests
> - 300 Fuel
> - 10000 Rupees
> - 30 Metron Fragments
> - 1 Elite Request
> - 3 Evaluation Requests
> - 3000 Rupees
> - 15 Metron Fragments
>
> `<Event Period>`
> Oct 5th 15:00 ~ Oct 12th 15:00 (UTC+9)
>
> `<Warning>`
> You cannot open any more boxes when the event period is over, so please
> remember to open your boxes before the event finishes!
>
> Thank you for your interest.

**`<Prize List>` as a table — all 11 rows, in the original order, verbatim:**

| # | Prize row (verbatim, including its original wording and star order) |
|---|---|
| 1 | 1 Legendary Request (3★) |
| 2 | 1 Special Request (2★) |
| 3 | 1 Metron Crystal |
| 4 | 3 Elite Requests |
| 5 | 300 Fuel |
| 6 | 10000 Rupees |
| 7 | 30 Metron Fragments |
| 8 | 1 Elite Request |
| 9 | 3 Evaluation Requests |
| 10 | 3000 Rupees |
| 11 | 15 Metron Fragments |

**No probability, weight, odds column or box-count cap appears anywhere in the
post.** Three internal oddities are preserved, not smoothed over:

1. Row 2 carries a trailing non-breaking space in the source markup
   (`1 Special Request (2★)&nbsp;`) — cosmetic only, no value change.
2. Rows 4 and 8 are the same item at two quantities with **different plural
   agreement**: "3 Elite Requests" vs "1 Elite Request". Quoted as written.
3. This post writes star labels as **`(3★)` / `(2★)`** — numeral then star —
   whereas every gacha post in this series writes **`★3` / `★2`**. Both orders
   occur in the official English corpus; do not normalise either.

### 1.3 [Event] October Package — one-time store package contents

- **`document_srl` 995291**, board row **Sticky** (board date **2018.09.28**,
  views **6176** — the highest-viewed unread row)
- **Archive used:**
  [2018-10-23 19:51:39 capture](http://web.archive.org/web/20181023195139/http://bs.visualshower.com/index.php?mid=event_en&document_srl=995291&l=en)
  of `http://bs.visualshower.com/index.php?mid=event_en&document_srl=995291&l=en`.
  A second `index.php`-form capture exists at `20181021134422`; the `?mid=`
  short form has **no** capture and the permalink form is **302-only** (§2.4).
- **Post metadata:** **not captured this pass** (see §1.1).
- **Purchase period (verbatim):** `September 30th 24:00 ~ October 31st 24:00 (UTC+9)`
- **Era:** PRE-rebalance.
- **Attachment:** 1 JPEG banner, `10월패키지_600x343_en.jpg`.

**Full body, verbatim:**

> Hello, Midgard Captains!
>
> Here is the October Package and this can only be purchased once per user.
>
> `<Package Content>`
> - 200 Manda
> - 1,000 Metron Fragments
> - 1,000 Fight Chips
> - 1,000 Mirage Fragments
> - 50,000 Rupees
> - 1980 VP
>
> `<Purchase Period>`
> - September 30th 24:00 ~ October 31st 24:00 (UTC+9)
>
> Thank you.

**`<Package Content>` as a table, verbatim:**

| # | Package line (verbatim) |
|---|---|
| 1 | 200 Manda |
| 2 | 1,000 Metron Fragments |
| 3 | 1,000 Fight Chips |
| 4 | 1,000 Mirage Fragments |
| 5 | 50,000 Rupees |
| 6 | 1980 VP |

Note `24:00`, not `00:00`, in the purchase period — quoted as written.

### 1.4 [Notice] How to Use the Events Section — rules text, **no** reward table

- **`document_srl` 75679**, board row **Sticky**, board date **2017.07.05**,
  views **1799**
- **Archive used:**
  [2018-10-25 17:54:19 capture](http://web.archive.org/web/20181025175419/http://bs.visualshower.com/event_en/75679)
  of `http://bs.visualshower.com/event_en/75679`.
  This id is the **most heavily captured** of the four: eight `index.php`-form
  captures spanning **2018-02-18 → 2018-12-25**, plus three 200 permalink
  captures. The text below is therefore a **2018 revision of a 2017.07.05 post**,
  not necessarily its original wording — see the era caveat at the end.
- **Post metadata:** **not captured this pass** (see §1.1).
- **Event period:** none (a rules notice, not an event).
- **Era:** PRE-rebalance; 2017 post observed in a 2018 revision.

**Full body, verbatim:**

> Hello, welcome to the Events section of the forums!
>
> This section was made for forum events apart from in-game events. Our upload
> image feature has also been added, so share away your screenshots! But please
> be aware there are some exceptions from using the upload feature as outlined
> below:
>
> 1. Anyone can upload images in the PC version of the forums.
>
> 2. Certain terms must be met to upload images on your device.
>    - iOS: All available.
>    - AOS: OS over 5.0 (Lollipop)
>
> 3. If your Android device has an operating system version less than 5.0, the
> upload button will not show.
>
> We will be posting new forums events everyone can easily participate in and
> earn rewards.
>
> Thank you for your attention!

**This body contains no reward table and no gameplay numeral at all.** The only
numerals are the client platform versions `5.0` / `Lollipop`. It is included
because it changes how the whole board must be read — see §2.6.

---

## 2. UNPUR[E] — everything that is NOT a verbatim reward table

### 2.1 Exact-URL CDX availability, all three URL forms, 4 ids

Query form: `http://web.archive.org/cdx/search/cdx?url=<exact>&matchType=exact&output=json&limit=20&collapse=timestamp:8`.
**12 queries, 0 errors, 0 retries.** `200` = capture exists in that form;
`302` = capture exists but is a redirect stub with no body.

| `document_srl` | `http://bs.visualshower.com:80/?mid=event_en&document_srl=…&l=en` | `http://bs.visualshower.com/index.php?mid=event_en&document_srl=…&l=en` | `http://bs.visualshower.com/event_en/<srl>` |
|---|---|---|---|
| `1008972` | 20181025015638 (200) | 20181021134401, 20181023222707, **20181025015703**, 20181225003552 (all 200) | 20181023222707 (302), 20190913231244 (302) — **no 200** |
| `995291` | **no rows** | 20181021134422, **20181023195139** (both 200) | 20181023195139 (302), 20190923150031 (302) — **no 200** |
| `999762` | **no rows** | 20181021134437 (200) | **20181025175424** (200), only 200 permalink capture |
| `75679` | **no rows** | 20180218085251, 20180420074545, 20180521220550, 20180623163038, 20180823214258, 20181024100436, 20181223232220, 20181225164037 (all 200) | 20180218201303 (200), 20180422122259 (200), **20181025175419** (200); 20180420074545, 20180623163038, 20180823214258, 20181225164037 are 302 |

Nine of the twelve remaining board bodies were **not tested for availability in
this pass** — untested, **not** negative (§3).

### 2.2 Attendance is event-parameterised, not a fixed daily value (and not the local DailySignIn)

- September 2018 (pass 2): **30 Manda/day × 9 days = 270 Manda**.
- October 2018 Halloween (§1.1): **20 Manda/day × 15 days = 300 Manda**.
- Both are **Manda**, both are handed out through the **Special Supply**, and
  both require an app restart/reopen per day.
- Therefore **no original fixed daily attendance number exists**; the amount is
  an event parameter. Neither figure may be used to set `local_fuel_0`, and
  neither corroborates the replica's 28-day **100-gold** DailySignIn calendar
  (AGENTS §83): that fixture differs in currency (gold vs Manda), in window
  (28-day vs 9/15-day) and in trigger. **The local fixture is not recovered
  data and is not contradicted by an original source — it simply has no
  official counterpart in this corpus.**

### 2.3 Fuel is a spendable event currency, and the Lootbox pays fuel back

- `1 box per 30 Manda` **or** `1 box per 200 fuel` (§1.2). Ratio
  **200 fuel : 30 Manda ≈ 6.67 fuel per Manda** — a **ladder/ratio reading only**.
  No exchange route, rounding rule or direction of conversion is recovered.
- `300 Fuel` is itself one of the 11 Lootbox prizes, i.e. the box is
  **partially self-funding** in fuel terms. The local fuel model (10 AP per
  `local_ap` item, AGENTS §34) is a **fixture** and must not be used to convert
  200 fuel into an AP figure.
- The only official statement of a fuel↔AP relationship anywhere in this corpus
  remains absent; the September/October Manda attendance (§2.2) and the Lootbox
  Manda ladder are the two separate spend channels.

### 2.4 Method correction: the permalink form is not a reliable fallback

Pass 2 §2.3 advised trying all three forms because a `?mid=` CDX miss is a false
negative. This pass sharpens that: for `1008972` and `995291` the
`/event_en/<srl>` form has captures but they are **302 redirect stubs with no
document body**. A lane that tries the permalink first and treats "a CDX row
exists" as "a body exists" will fetch a redirect and record an empty post — the
same silent-empty failure mode as the `rd_ft` quirk. **The
`/index.php?mid=event_en&document_srl=<id>&l=en` form was the only form that
returned a 200 body for 3 of the 4 ids** (the exception, `999762`, has its only
200 in the permalink form). Recommended order for a future lane:
`index.php?mid=` → permalink → `?mid=`, and **require `statuscode == 200`**.

### 2.5 Ticket and currency taxonomy widened (naming + magnitudes, all impure)

- **Star-labelled requests:** `Legendary Request (3★)`, `Special Request (2★)`.
  This is the first official pairing of those two ticket names with explicit
  star labels, and it is consistent with pass 2's "Legendary Request (★3 Recruit
  Guarantee)" narrative. A **naming crosswalk lead only** — it does not recover
  the guarantee's implementation.
- **Unlabelled requests, now attested with quantities:** `Elite Request`
  (3 and 1 in one list) and `Evaluation Request` (3). Neither has a star label
  in any recovered official text.
- **Metron currency is two-tier:** `Metron Crystal` (whole) vs `Metron Fragments`
  (30 / 15 in the Lootbox; 1,000 in the October Package; 3–12 per rank band in
  the September ladder). That fragments accumulate into crystals is *plausible*
  and consistent with the naming, but **no conversion threshold is recovered**.
- **Two new official currency names:** `Fight Chips` and `Mirage Fragments`
  (1,000 each in the October Package). These are **naming crosswalk leads
  against the Fight Club/Arena local model** (BP / honor / league currencies,
  AGENTS §45/§56). **Explicitly unproven: do not assert "Fight Chips = BP" or
  any other mapping.** No native or client field is bound here.
- **`1980 VP`** in the October Package. Almost certainly a real-money/store
  figure, which makes that post a **store package**, distinct from the
  September "300 Manda at the price of 100 Manda (300%)" **in-game**
  Manda-for-Manda offer. Two different mechanisms; do not merge them, and note
  that nothing in the replica models VP.
- **One-time-per-user purchase is official twice:** "can only be purchased once
  per user" (§1.3) and "Limited to 1-time purchase only during the event"
  (pass 2 §1.1). A per-user purchase cap on named offers is original behaviour.

### 2.6 The board is a FORUM board, not the game's event list — the most consequential finding

§1.4 states in the official voice that this section "was made for **forum events
apart from in-game events**" and exists so players can "share away your
screenshots". Consequences, all of which change how this corpus should be used:

1. **The five "sticky" rows are sticky because they are the current *forum*
   events**, not because they are a canonical in-game event list. The `No.`
   ordering in pass 2 §2.1 is a board sort, not an event chronology contract.
2. **These posts are marketing-grade text.** They may simplify or omit in-game
   detail. They are a reliable source for *what was advertised*, never for a
   complete event schema, and never for a probability table.
3. **New mining direction, higher value than more post text:** because the
   board's declared purpose is player image upload, its **attachments and
   comment images are a purpose-built corpus of player-captured in-game
   screenshots** — stat panels among them. This pass recorded attachment
   *filenames* only and opened none of them. A future lane that enumerates
   attachment and comment image URLs for these posts serves the base-stat goal
   directly, and is a better use of budget than a 5th body fetch. Note the two
   Halloween hunter-art filenames are **hash-named**, so identity mapping must
   come from body text or from viewing the image, never from the filename.

### 2.7 Gacha boost multipliers: the pass-2 "self-contradiction" is probably a scope difference

Pass 2 §2.2 flagged that two adjacent official events disagree on the ★3
multiplier (200% in the September post, 400% in the October Hot Time post).
With this pass's third data point the reading changes:

| Official post | Scoped effect | Multiplier |
|---|---|---|
| September Fall Festival (pass 2) | named ★4 pair "Lily & Lyla", "Windblade" | 400% UP |
| September Fall Festival (pass 2) | all ★3 hunters | 200% UP |
| October Hot Time (pass 2) | **limited** ★3 hunters (incl. ★3 Santa Clauster, Santa Girl Rebecca) | 400% UP |
| October Hot Time (pass 2) | all ★3 hunters | 200% UP |
| Halloween 2018 (§1.1) | **Halloween-limited ★3** hunters | **500% UP** |
| Halloween 2018 (§1.1) | all ★3 hunters | 200% UP |

The 400% and 200% appear **in the same October body**, one scoped to *limited*
★3 and one to *all* ★3. So the two numbers are most likely **per-scope
multipliers rather than a contradiction**. This is an **inference that resolves a
flagged conflict**, not a recovered rule: no official text states how scoped and
global boosts compose, and no base rate is published anywhere in the corpus.

### 2.8 Other economy and roster readings (all impure)

- **Weekly purchase bonus is original:** "bonus gift with the first purchase of
  each week(UTC+9)" = 1 Special Request + **40** traces, with the trace identity
  switching mid-event. Two readings: (a) original purchase counters have a
  **weekly** reset boundary, and (b) trace grants of **40** are original-scale.
  Both are far above the local `collect_qty` 10/20 fixtures (AGENTS §67/§68).
  **Do not "correct" the local fixtures from this** — it is a different mechanic
  (purchase bonus vs trace exchange threshold).
- **10+1 bundle bonus identity varies by event, third data point:** 1 Metron
  Crystal (September) → 10+10 traces (October Hot Time) → **10 traces of one
  of two hunters, switching mid-event** (Halloween). Confirms pass 2's
  event-specificity finding.
- **"Transcendence +1 on the first recruit"** for two named ★3 hunters is the
  first official statement of a free **Transcendence/Awakening** grant in the
  official corpus, and a naming crosswalk lead to the local
  `AwakeLevelUp`/Transcendence model (AGENTS §29). Magnitude is **+1** only; the
  consumed resource, the eligibility rule and the "first recruit" reset scope
  are **all unrecovered**. It was scoped to two named hunters, explicitly not a
  global ★3 effect.
- **Identity leads, recorded with their conflict and not merged:** "★2 Halloween
  Riko" (October Hot Time) vs "Halloween Witch Riko(★2)" (Halloween) — likely one
  hunter, not proven. **"Broom Witch Denali" is a new name not present in any
  prior lead or in the recovered catalog roster** used in AGENTS §24/§67
  (001 Lantern, 002 Mowgli, 003 Nene, 004 Tyltyl, 005 Gerard, 006 Sylvester).
  Crosswalk **unproven**. Jack-O'-Lantern is described as a *Lantern* skin
  ("putting a huge pumpkin on Lantern's head") — a **narrative/skin** lead,
  which is the kind of thing that must not be turned into a new card id.
- **Drop-channel statements differ and must not be generalised:** gemstones
  dropped by "general stages **or** abysses" (September), rice cakes by
  "general stages" only (September), and the Halloween post states **no** drop
  channel at all.
- **Original UI string, behaviour not modelled:** "You cannot open any more
  boxes when the event period is over" implies an unopened-lootbox expiry in the
  original. The local Special Supply model (AGENTS §89/§90) currently allows
  claiming pending rows with no expiry. Recorded as a **string fact only**; no
  change was made and none is implied.
- **Still unrecovered after this pass:** base gacha probabilities, Lootbox
  probabilities, an attendance *calendar* or cadence outside event windows,
  jewel **stat** rows, equipment modification material quantities, the
  VP↔real-money mapping, any Fight-Chips↔Arena-currency mapping, board pages
  2–23, and nine unread board bodies.

---

## 3. Negative results preserved

| Target | Check | Result |
|---|---|---|
| Any HP / ATK / DEF numeral in **any** of the four bodies | Full body text read | **Zero.** Every numeral in §1 is a currency amount, a material/trace/request count, a star tier, a gacha multiplier, a purchase/attendance quantity or a client OS version. |
| Lootbox odds / weights / box cap | Full body read | **Absent.** 11 prize rows, no probability column, no cap. |
| Base gacha probability | Full bodies read | **Still not present** in the four new bodies; only scoped `% UP` multipliers (§2.7). |
| Author / posted timestamp / votes / comment counts for the 4 bodies | Body-only extraction, budget spent | **Not captured.** Re-fetching would exceed the 4-body budget; board dates are quoted from the pass-2 index map instead. |
| Attachment and comment images (5 attachments across the 4 posts) | Filenames recorded, no bytes fetched | **Not opened; no OCR.** §2.6 item 3 records them as the recommended next mining direction. |
| `75679` as a *rules-with-numbers* post | Full body read | **No.** It is an image-upload policy notice; its only numerals are OS `5.0`/`Lollipop`. Its value is §2.6, not its numerals. |
| `995291` `?mid=` short form availability | Exact-URL CDX | **No rows** — confirms pass 2's query-form false-negative rule a second time; the same id *is* captured under `/index.php?mid=`. |
| `1008972` / `995291` permalink bodies | Exact-URL CDX | **302 stubs only** — new negative for the permalink-first strategy (§2.4). |
| Remaining 9 board bodies (`990227` Estelle, `987312` Tyltyl box, `1003638` Westfield gloves, `1009190` Which Witch, 4× Lottery Mouse gifts, 3× Clara weekends) | Budget exhausted at 4 body fetches | **Not fetched; availability untested, not negative.** The 4× and 3× families are *recurring titles* across adjacent dates, so a single fetch of the earliest of each family may cover its own month only — do not assume template identity. |
| Board pages 2–23 | Out of budget | Not visited. |

---

## 4. Coverage disposition / files updated

- **New base-stat tuples: 0.** Hero coverage stays **1/113**; accessories
  **1/100**; monsters **0/22**. Nothing in §1 is an HP/ATK/DEF reading.
- **Accessory coverage deliberately NOT incremented.** §1.2 is fuel/currency
  economy, not a jewel row; §1.2's tickets are not accessories. Pass 2's jewel
  class↔tier binding is unaffected.
- **All economy numerals belong in the impure ledger.**
  `polluted-observations.md` gains a **pointer subsection only** — no numeric
  duplication there.
- **Era:** the three 2018 bodies are **PRE-rebalance** (Sept–Oct 2018). `75679`
  is a 2017.07.05 post observed in a **2018 revision**, so its wording is not
  safely datable to 2017. None of this may be mixed with the 2019-09-05+
  equipment/crystal multipliers in `stat-version-context.md`.
- **Files written:** this file (new);
  `polluted-observations.md` (pointer subsection appended).
  `coverage.md`, the TSVs, `README.md`, the server, the APK and all seeds are
  untouched. **No server/APK/state change, no emulator or phone contact, no
  Ghidra run, no native library read, no archive write or re-upload.**