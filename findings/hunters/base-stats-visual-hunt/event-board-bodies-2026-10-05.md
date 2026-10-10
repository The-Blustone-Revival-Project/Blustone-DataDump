# Official `event_en` board bodies, pass 2 — three new reward tables (2026-10-05)

**Lane:** continuation of [`official-posts-2026-10-05.md`](official-posts-2026-10-05.md)
§1.3. That pass recovered the 23-page board **index** (titles/dates/views) but only
**two** `document_srl` **bodies** (walnuts `1003633`, Jack's Treat `1008954`).
This pass mined **three** further bodies and the exact `document_srl` for every
visible board row.

**Era rule** (`stat-version-context.md`): all three bodies are Sept–Oct **2018**,
i.e. **PRE-rebalance** (the rebalance took hold after 2019-09-05). Nothing here is
POST-era. Values are **economy / drop / gacha context only** — see §4.

**Budget honoured:** **4 body fetches total** (1 = known-good board page reused
purely to harvest `document_srl` links, 3 = new bodies). **11 exact-URL CDX
queries.** No retry loops, no throttling bypass, no query re-run after a failure
except one naturally-spaced second attempt at the *next* URL form. One **503**
recorded and left alone. No server/APK/seed/emulator/phone/Ghidra/native-library
operation.

---

## 1. PURE — verbatim reward tables (archive URL + capture + post/event dates + era)

Everything in §1 is a **direct transcription** of the captured post body. HTML
entities were decoded (`&rsquo;`→`'`, `&ndash;`→`-`, `&nbsp;`→space, `&amp;`→`&`,
`&#39;`→`'`); no other change. Line breaks follow the original `<p>` boundaries.
`★` (U+2605) is the original glyph, rendered as `?` in the raw console dump.

### 1.1 [Event] Midgard Fall Festival Event! — the largest event table recovered

- **`document_srl` 989396**, board row **No. 427**
- **Archive:**
  [2018-10-25 17:57:40 capture](http://web.archive.org/web/20181025175740/http://bs.visualshower.com/event_en/989396)
  of `http://bs.visualshower.com/event_en/989396`.
  A second capture exists in the `index.php` form:
  `20180925213940` — `http://bs.visualshower.com/index.php?mid=event_en&document_srl=989396&l=en`
- **Post metadata:** author **Natara**, posted **2018.09.20 14:34**, Views
  **10349**, Votes **66**, **[12]** comments, 5 JPEG attachments (banners only —
  every reward table in this post is **text**, not an image).
- **Event period (verbatim):** `Sep 20th 15:00 ~ Sep 28th 15:00 (UTC+9)`
- **Era:** PRE-rebalance.

**1. Daily Attendance Gift (verbatim):**

> We would like to give out Manda daily to share this joy! During the event, 30
> Manda will be supplied daily to the Special Supply on your attendance (for 9
> days). A total of 270 Manda can be obtained if you don't miss any day!
>
> \*\* Attendance will be taken when you open the app, so make sure to close and
> re-open the app on daily basis!

**-Extra presents on the purchase (verbatim):**

> If you make any purchase during the event, a Legendary Request (★3 Recruit
> Guarantee) will be supplied to you at Schumann's Special Supply! This is
> limited to once only!

**2. Lana's Rice Cakes! (verbatim):**

> You can obtain rice cakes as you clear the general stages! The collected rice
> cakes are exchangeable for equipment modification materials and ★3 hunter
> traces.
>
> You can exchange 15 rice cakes for 1 box, and usually 3 ~ 5 traces will be found
> in a box, but if you get lucky, you will find 40 traces just in one box!

| Box (verbatim name) | Contents (verbatim) |
|---|---|
| Scorching Rice Cake Box | 1 Flammable Material + 3~40 Fire type ★3 hunter traces |
| Frozen Rice Cake Box | 1 Coolant + 3~40 Ice type ★3 hunter traces |
| Glittering Rice Cake Box | 1 Lightning Box + 3~40 Lightning type ★3 hunter traces |

> There are also prizes for accumulated rice cakes, so collect them as much as you
> can!

**`<Accumulation Rank Prizes>` — complete 17-row ladder, verbatim:**

| Rank band (verbatim) | Prize (verbatim) |
|---|---|
| 1st | 12 Metron Crystals, 600 Manda |
| 2nd | 11 Metron Crystals, 550 Manda |
| 3rd | 10 Metron Crystals, 500 Manda |
| 4th ~ 10th | 9 Metron Crystals, 450 Manda |
| 11th ~ 30th | 9 Metron Crystals, 400 Manda |
| 31st ~ 50th | 8 Metron Crystals, 350 Manda |
| 51st ~ 100th | 8 Metron Crystals, 300 Manda |
| 101st ~ 200th | 7 Metron Crystals, 250 Manda |
| 201st ~ 400th | 7 Metron Crystals, 200 Manda |
| 401st ~ 800th | 6 Metron Crystals, 150 Manda |
| 801st ~ 1600th | 6 Metron Crystals, 100 Manda |
| 1601st ~ 3200th | 5 Metron Crystals, 50 Manda |
| 3201st ~ 6400th | 5 Metron Crystals, 20000 Rupees |
| 6401st ~ 12800th | 4 Metron Crystals, 15000 Rupees |
| 12801st ~ 25600th | 4 Metron Crystals, 10000 Rupees |
| 25601st ~ | 3 Metron Crystals, 5000 Rupees |

**3. Exclusive Offer for Manda Package! (verbatim):**

> We want to follow the footsteps of our generous friend Lottery Mouse. There
> will be an EXCLUSIVE offer for Manda Package during the event!
>
> - 300 Manda Exclusive Package (Limited to 1-time purchase only during the event)
> Get 300 Manda at the price of 100 Manda (That's 300%)!
>
> This will be added to the existing package products page.

**4. Recruit Hot Time! / `<Event Effects>` (verbatim):**

> Recruit Hot Time is back! During the event, the probability of recruiting ★3,
> ★4 hunters will increase! Also 1 Metron Crystal will be supplied on every 10+1
> recruit.
>
> This will be added at the top of Lottery Mouse's recruit page.
>
> `<Event Effects>`
>
> - Probability of ★4 Lily & Lyla and Windblade 400% UP!
> - Probability of all the ★3 hunters 200% UP!
> - 1 Metron Crystal on every 10+1 Recruit!

**Two internal inconsistencies preserved, not smoothed over:**

1. **"Lightning Box"** in the Glittering row, where the two sibling rows say
   `Flammable Material` / `Coolant` (i.e. *…Material*). Quoted exactly as written;
   do not silently normalise it to "Lightning Material".
2. The narrative says boxes hold "usually 3 ~ 5 traces" while each row says
   "3~40". Both original; both retained.

### 1.2 [Event] October Limited Recruiting Hot Time! — limited-hunter gacha boost

- **`document_srl` 995273**, board row **No. 431**
- **Archive:**
  [2018-10-21 13:44:17 capture](http://web.archive.org/web/20181021134417/http://bs.visualshower.com/index.php?mid=event_en&document_srl=995273&l=en)
  of `http://bs.visualshower.com/index.php?mid=event_en&document_srl=995273&l=en`.
  Also captured in the permalink form at `20181019051052` and again at
  `20190913200101` — `http://bs.visualshower.com/event_en/995273`.
- **Post metadata:** author **Natara**, posted **2018.09.28 14:30**, Views
  **2895**, Votes **28**, **[7]** comments, 1 JPEG banner attachment.
- **Event period (verbatim):** `September 28th 15:00 ~ October 2nd 15:00 (UTC+9) (5 days)`
- **Era:** PRE-rebalance.

**`<Limited Hunters Available>` (verbatim):**

> ★3 Santa Clauster
> ★3 Santa Girl Rebecca
> ★2 Halloween Riko

**`<Event Details>` (verbatim):**

> Limited ★3 Hunter Recruit Chances 400% UP! (This will NOT be applied to ★2
> Halloween Riko)
>
> ★3 Hunter Recruit Probability 200% UP!
>
> 10 Traces of Santa Girl + 10 Traces of Santa Clauster on 10+1 Recruit!

Narrative verbatim: *"…hunters who are usually not recruitable will become
available with a high probability. Furthermore, this event isn't just about the
limited hunters: the probability of recruiting ★3 hunters will be increased as
well."*

### 1.3 [Event] Find Shiny Gemstones! — jewel-class exchange rates (JEWELRY ECONOMY)

- **`document_srl` 999764**, board row **No. 435**
- **Archive:**
  [2018-10-25 17:58:00 capture](http://web.archive.org/web/20181025175800/http://bs.visualshower.com/event_en/999764)
  of `http://bs.visualshower.com/event_en/999764`.
- **Post metadata:** author **Natara**, posted **2018.10.05 14:33**, Views
  **514**, Votes **3**, **[7]** comments, 1 JPEG banner attachment.
- **Event period (verbatim):** `Oct 5th 15:00 ~ Oct 8th 15:00 (UTC+9)`
- **Era:** PRE-rebalance.

**`<How To Participate>` (verbatim):**

> 1. At a fixed chance, clear general stages or abysses during the event period
>    and get gemstones!
> 2. Exchange the collected gemstones for Jewels according to their class through
>    the event page!
> 3. Collect your Jewel from Schumann's special supply!

**`<Gemstone Details>` (verbatim):**

> 1. Gemstones are classified into 3 different categories:
>
> Blunt Gemstone - Can be exchanged for any blunt ★2 Jewel per 10 blunt gemstones
> Ordinary Gemstone - Can be exchanged for any ordinary ★3 Jewel per 5 ordinary gemstones
> Shiny Gemstone - Can be exchanged for any shiny ★4 Jewel per 3 shiny gemstones
> At a rare chance, it can be exchanged for a radiant ★5 Jewel!
>
> 2. The higher stages and harder levels will have higher drop rates for
>    gemstones.

**Pure side-value (naming, not economy):** this post is the first recovered source
that binds the **jewel class names to a star tier** —
`blunt = ★2`, `ordinary = ★3`, `shiny = ★4`, `radiant = ★5` — and it names the
drop channel as **general stages *and* abysses**. Still **not** a jewel stat row
(§4).

---

## 2. UNPUR[E] — everything that is NOT a verbatim reward table

### 2.1 Exact `document_srl` map for the whole visible board (existence/leads only)

Harvested from the `event_en` list table embedded in the 2018-10-25 walnuts
capture. **`No.` is a display index, NOT an id** — the prior lane's `#440`-style
notation must not be used as an identifier. Views are as of that capture; the
current-post row renders `»` and its own row shows the live counter.

| No. | `document_srl` | Title | Board date | Views |
|---|---|---|---|---|
| Sticky | **1008972** | [Event] Halloween in Midgard! | 2018.10.19 | 3251 |
| Sticky | **1008954** | [Event] Jack's Treat! | 2018.10.19 | 347 (read in prior lane) |
| Sticky | **1003633** | [Event] Lottery Mouse Likes Walnuts! | 2018.10.12 | 483 (read in prior lane) |
| Sticky | **995291** | [Event] October Package | 2018.09.28 | 6176 |
| Sticky | **75679** | [Notice] How to Use the Events Section | 2017.07.05 | 1799 |
| 440 | **1009190** | [Event] Which Witch? Riko? | 2018.10.19 | 84 |
| 439 | **1005805** | [Event] Lottery Mouse's Amazing Gifts | 2018.10.15 | 3007 |
| 438 | **1003638** | [Event] Westfield's Boxing Gloves | 2018.10.12 | 226 |
| 437 | **1003645** | [Event] Clara's Surprise Weekend Gift | 2018.10.12 | 1444 |
| 436 | **1001701** | [Event] Lottery Mouse's Amazing Gifts | 2018.10.08 | 2777 |
| 435 | **999764** | [Event] Find Shiny Gemstones! | 2018.10.05 | 513 (read here) |
| 434 | **999762** | [Event] Schumann's Marvelous Lootbox | 2018.10.05 | 428 |
| 433 | **999761** | [Event] Clara's Surprise Weekend Gift | 2018.10.05 | 1429 |
| 432 | **997466** | [Event] Lottery Mouse's Amazing Gifts | 2018.10.01 | 3892 |
| 431 | **995273** | [Event] October Limited Recruiting Hot Time! | 2018.09.28 | 2900 (read here) |
| 430 | **995267** | [Event] Clara's Surprise Weekend Gift | 2018.09.28 | 2393 |
| 429 | **995260** | [Event] The More the Better by Lottery Mouse! | 2018.09.28 | 304 |
| 428 | **990227** | [Event] Estelle's Special Offer | 2018.09.21 | 631 |
| 427 | **989396** | [Event] Midgard Fall Festival Event! | 2018.09.20 | 10349 (read here) |
| 426 | **987322** | [Event] Lottery Mouse's Amazing Gifts | 2018.09.17 | 3027 |
| 425 | **987312** | [Event] Tyltyl's What's in the Box? | 2018.09.17 | 770 |

Board pagination still **23 pages**; pages 2–23 remain unmined. Captured-permalink
availability confirmed by exact-URL CDX for `1008972` only (`20181025015638`, in
the `http://bs.visualshower.com:80/?mid=event_en&document_srl=…&l=en` form);
`995291` returned no rows for that form. Availability of the other 13 srl values
is **untested** (no budget left), not negative.

### 2.2 Impure economy readings (every numeral here is context, not coverage)

- **Attendance currency: Manda, not Fuel.** 30/day × 9 days = 270. This
  **contradicts** any assumption that the game's daily-attendance reward is AP or
  Fuel. Cross-check only for the local fuel/supply fixtures — do **not** use it to
  set `local_fuel_0`.
- **Event drop currency is per-event, not global.** Rice cakes cost **15** per
  trace box; the walnuts event (prior lane) cost **95/125** per trace box for
  **2~4** traces vs rice cakes' **3~5** traces. Two different original scales ⇒
  the local `collect_qty` **10/20** fixtures (AGENTS §67/§68) are **not** an
  original scale and must not be "corrected" to 15 either.
- **10+1 bundle always carried a bonus; the bonus identity is event-specific.**
  September: **1 Metron Crystal**. October: **10 Traces of Santa Girl + 10 Traces
  of Santa Clauster**. This is independent official corroboration of the
  client-verified bundle mechanic (AGENTS §59) and of "bonus" ≠ Manda. It does
  **not** recover which bonus a given month shipped in the live 2.8.0.1 build.
- **Gacha boost multipliers are officially published, base rates are not.**
  Officially stated: named ★4 pair **400% UP**, all ★3 **200% UP** (September);
  limited ★3 **400% UP**, all ★3 **200% UP** (October). The original text
  therefore **conflicts with itself** on the ★3 multiplier (200% vs 400%)
  between two adjacent events — flagging rather than reconciling.
- **Boost scope is rarity-tier-scoped.** The October post explicitly excludes
  ★2 Halloween Riko from the 400% limited boost while still running a global ★3
  boost. This is direct original evidence that gacha boosts can be *per-hunter*
  and *per-tier*, which the native constant work (AGENTS §59/§82) has not
  modelled.
- **★4 identity leads (naming only, no stats).** "Lily & Lyla" and "Windblade"
  are named ★4 boost targets. Note AGENTS references a char-intro post
  `426682` for **"Lily&Lala"** — the spelling differs (**Lyla** vs **Lala**).
  Do **not** merge them into one identity without a further source.
- **Ticket taxonomy widened.** Original request/consumable ticket names now
  attested: **Legendary Request** (explicitly "★3 Recruit Guarantee"), plus
  Challenge / Elite / Special Requests and **Metron Crystal** / **Metron
  Fragments** from the prior lane. Legendary Request ↔ the client's ★3-guarantee
  behaviour is a **naming crosswalk lead**, not proof of the guarantee's
  implementation.
- **Equipment modification materials named:** `Flammable Material`, `Coolant`,
  and (per the original's own wording) `Lightning Box`. Element-keyed
  (Fire / Ice / Lightning) matches the recovered attr enum (AGENTS §19), but these
  are **materials**, not jewels and not equipment stat rows.
- **Real-money-adjacent in-game offer:** "300 Manda at the price of 100 Manda
  (That's 300%)", 1 purchase per event. Nothing in the local replica models a
  Manda-for-Manda package; recorded only.
- **Jewel class ↔ tier binding** (`blunt ★2 / ordinary ★3 / shiny ★4 /
  radiant ★5`) is a *naming* fact and a *drop-cost* fact. It is **not** a jewel
  stat value and **not** evidence about `GetGemEffectName` selector ordering
  (AGENTS §99). Accessory coverage stays **1/100**.
- **Player-reported numbers are anecdotal and are NOT promoted to tables.**
  From the Fall Festival thread: *"I did a 300 pull and got 1 silver and the rest
  were bronze"*; *"The 4* hunter drop rate is too low. Wasted 1.2k manda"*;
  *"4star drop rate is less than 1 percent. 400 times less than 1 percent is
  probably still less than 1 percent"*; *"I guess you only get 1 blue scroll. I
  made 3 purchases and only got 1....."*; *"I barely got any rice cakes"*; *"I
  made a purchase and didn't receive the legendary scroll."* From the Hot Time
  thread: *"I got a rock.... Four 10+1 pulls and no Clauser"*; *"Make it 1600
  might make a diffrence."* These are **uncontrolled self-reports** — they
  establish only that players *believed* ★4 rates were under 1% and that the
  Legendary Request was not always delivered. **No base gacha rate is recovered.**
  The Gemstones thread is pure sentiment (*"This event is the worst..."*).
- **Identity leads with no numeric value:** Santa Clauster (★3), Santa Girl
  Rebecca (★3), Halloween Riko (★2). Useful for the roster/crosswalk work only.
- **Still unrecovered after this pass:** base gacha probability table, attendance
  *calendar* (this post gives a 9-day window, not a cadence), attendance reward
  type outside Manda, jewel **stat** rows, equipment modification **material**
  quantities, and pages 2–23 of the board.

### 2.3 Method notes / throttling log for the next lane

- **A `?mid=…` CDX miss is a query-form false negative.** Exact-URL CDX with
  `matchType=exact` against
  `http://bs.visualshower.com:80/?mid=event_en&document_srl=<id>&l=en` returned
  **NO ROWS** for `995273`, `989396`, `999764` and `995291`, yet all of those ids
  *are* captured under `http://bs.visualshower.com/index.php?mid=event_en&document_srl=<id>&l=en`
  and/or the permalink `http://bs.visualshower.com/event_en/<id>`. **Always try
  all three URL forms** (`/?mid=`, `/index.php?mid=`, `/event_en/<srl>`) before
  declaring a board post uncaptured. This corrects the impression in
  `official-posts-2026-10-05.md` that the `event_en` board is thinly captured.
- **`rd_ft` markup quirk:** the closing tag in these captures is
  `<div class="rd_ft" >` (stray space). A body extractor keyed on
  `<div class="rd_ft">` silently yields **zero characters** and looks like an
  empty post. Anchor the body on `<div class="rd_body clear">` … `<div class="rd_ft"`.
- **Post body is plain text, not image tables.** All three posts carry only
  decorative banner JPEGs; every numeric table is real HTML text. No OCR needed,
  and no numerals are hidden in images.
- **Board row date cells carry a `title` attribute** (`<td class="time"
  title="12:15">`), so a `<td class="time">` extractor returns empty dates for
  most rows. Use `<td class="time"[^>]*>`.
- **Throttle log this pass:** CDX 503 ×1 (first attempt at the `index.php` form
  for `999764`; the immediately-following permalink query succeeded), CDX
  timeouts ×0, capture-body failures ×0. **11 CDX queries, 4 body fetches.** No
  query was retried after a failure; no bypass attempted.

---

## 3. Negative results preserved

| Target | Check | Result |
|---|---|---|
| `1008954` / `1003633` bodies | Already read in the prior lane | Not re-read as a source of new values; the 2018-10-25 walnuts capture was fetched **once** here only to harvest `document_srl` links, which is what unlocked this pass. |
| Remaining 13 board bodies (incl. `995291` October Package, `1008972` Halloween, `999762` Lootbox, `990227` Estelle, `987312` Tyltyl box, `1003638` Westfield gloves, 4× Lottery Mouse gifts, 3× Clara weekends, `1009190` Which Witch, `75679` notice) | Budget exhausted at 4 body fetches | **Not fetched.** Availability untested for 13 of them; `75679` (2017.07.05, "How to Use the Events Section") is the most likely to carry rules text rather than numerals. |
| Board pages 2–23 | Out of budget | Not visited. |
| Any HP / ATK / DEF numeral in any of the three bodies | Full body text read | **Zero.** No hero, monster or equipment stat value exists in any of the three posts. |
| Base gacha probability | Read all three bodies | **Not present.** Only event multipliers (`% UP`) and player opinion. |

---

## 4. Coverage disposition / files updated

- **New base-stat tuples: 0.** Hero coverage stays **1/113**; accessories
  **1/100**; monsters **0/22**. Nothing in §1 is an HP/ATK/DEF reading: every
  numeral is a currency amount, a material/trace count, a rank band, a gacha
  multiplier, or a jewel exchange cost.
- **Accessory coverage deliberately NOT incremented** despite §1.3 being a
  jewel post: a gemstone→jewel *exchange cost* is a drop/economy value, not a
  jewel stat row, and the class↔tier binding is naming only.
- **All economy numerals belong in the impure ledger.** `polluted-observations.md`
  gains a pointer subsection only (no numeric duplication there).
- **Era:** everything here is **PRE-rebalance** (Sept–Oct 2018). It must not be
  mixed with the 2019-09-05+ equipment/crystal multipliers in
  `stat-version-context.md`.
- **Files written:** this file (new);
  `polluted-observations.md` (pointer subsection appended).
  `coverage.md`, the TSVs, `README.md`, the server, the APK and all seeds are
  untouched. **No server/APK/state change, no emulator or phone contact, no Ghidra
  run, no native library read.**