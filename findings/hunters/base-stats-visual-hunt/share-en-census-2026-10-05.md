# `share_en` board census — 105 posts enumerated, 105 bodies read, zero stat panels, and the attachment namespaces are NOT archived (2026-10-05)

**Lane:** the "HIGHEST-VALUE UNTRIED LEAD" of
[`review-posts-2026-10-05.md`](review-posts-2026-10-05.md) §3, which recorded
that `share_en` "as a board was **never enumerated** by any prior pass" and
outranked everything left on `event_en`. The prior pass had recovered 833 CDX
rows / 105 distinct ids, listed **one** body (`197745`) and read **zero**
images.

**This pass closes the enumeration.** Result headline, four findings:

1. **The board is fully enumerated and fully readable.** **105 of 105 distinct
   post ids have a retrievable 200 body**, and all 105 were fetched, parsed and
   transcribed. Every id now has a verbatim title, author and date. §1.
2. **The board is a player GUIDE board, not a screenshot board.** 105 posts,
   166,838 characters of body text, 54 posts with ≥500 characters, running
   2017-04-05 → 2018-04-08. Titles are overwhelmingly "Guide", "tips",
   "FAQ", "advancing", "cost of". §1.2.
3. **Zero HP / ATK / DEF numerals anywhere.** Not in any body, and — decisively
   — not obtainable from the images either: **the `565` and `567` attachment
   namespaces have no archived bytes at all.** A whole-namespace CDX sweep of
   `/files/attach/images/` returns 178 rows and **not one** is under `565` or
   `567`; direct `im_` fetches of five specific `565` files return **404**,
   with a `75605` control returning 200. This upgrades the prior pass's
   "retrieval reliability untested" risk into a **settled hard negative**. §1.4.
4. **The real payload is economy/progression numerics, not base stats.** Eight
   posts carry dense numeric tables (EXP-to-max by star, advancement costs,
   transcendence costs, shop prices, dispatch run counts). These are **not** base
   stat tuples, but they are directly relevant rebalance/economy evidence and
   are recorded as §2 UNPURE. §2.2.

---

## 1. PURE — verbatim census facts and body readings

Nothing in §1 is a base-stat reading. **There are no HP/ATK/DEF values in this
pass**, because no image was retrieved — see §1.4 for why none can be.

### 1.1 Fetch ledger — every attempt, HTTP status recorded

| # | Purpose | URL / query | HTTP | Result |
|---|---|---|---|---|
| 1 | `share_en` census | `cdx?url=bs.visualshower.com&matchType=domain&collapse=urlkey&filter=original:.*share_en.*&limit=20000` | 200 | 833 rows, **not truncated**; 105 distinct post ids |
| 2–4 | Board list pages 1–4 (`&l=en&page=N`) | `web/<ts>id_/…index.php?mid=share_en&l=en&page=N` | 200 ×4 | 46,632 / 44,421 / 34,340 / 45,549 bytes |
| 5–8 | Board list pages 5–8 | `&l=en&page=5` then plain `?page=6,7,8` | 200 ×4 | First attempt on 5–8 returned curl exit-code **000** (transport, no HTTP status); re-issued once with a delay and the recorded capture timestamps. All 200. |
| 9 | Board list page 9 | `?mid=share_en&page=9` | 200 | 34,420 bytes |
| 10–114 | **105 post bodies** | `web/<ts>id_/…/share_en/<id>` or `…index.php?mid=share_en&document_srl=<id>` | **200 ×105** | 105/105 retrieved. Intermediate curl **000** transport failures were retried with the alternate URL form and the id's other archived timestamp; all 105 eventually returned 200 with a valid post body. |
| 115 | `565` namespace sweep | `cdx?…url=bs.visualshower.com/files/attach/images/&matchType=prefix&collapse=digest&limit=20000` | 200 | **178 rows**, 177 with status 200, prefixes `75605`(148) `175`(7) `193`(6) `75601`(6) `75603`(4) `183`(2) `185`(2) `203`(2) `136`(1). **No `565`, no `567`.** |
| 116 | `565` prefix sweep | `cdx?…url=…/files/attach/images/565&matchType=prefix&collapse=urlkey&limit=500` | 200 | **0 bytes — zero rows.** |
| 117 | `565/745/197` prefix sweep | same, deeper prefix | 200 | **0 rows.** |
| 118 | `567` prefix sweep | `…/files/attach/images/567&matchType=prefix` | 200 | **0 rows.** |
| 119 | exact-URL CDX, 4 individual `565` files | `…&matchType=exact&limit=50` | 200 | **0 rows for every one.** |
| 120–124 | direct `im_` image fetch, 5 `565`/`567` files | `web/<ts>im_/…/files/attach/images/565/…` | **404 ×3** (4,727 bytes error page each) + `000` ×2 | **No bytes.** |
| 125 | wildcard-timestamp fetch `2018im_` / `2im_` on one `565` file | – | **404**, `000` | **No bytes.** |
| 126 | **control**: exact-URL CDX on a known-archived `75605` file | `…/75605/303/534/001/725a8e17….jpg&matchType=exact` | 200 | **1 row, status 200, 58,647 bytes** — proves the query method itself works. |
| 127 | **control**: `75605` prefix sweep | `…/files/attach/images/75605&matchType=prefix&collapse=urlkey&limit=500` | 200 | **148 rows.** |

**No 302 was returned to any image fetch.** The only non-200 image-side statuses
observed are **404 ×3** on `565` files and curl **000** transport failures on
the rest. `000` is recorded as such throughout and is **not** a server status.

**Important scope note on the retry discipline.** `000` is a client-side
connection failure, not an archive verdict. Three batches of body fetches and
four list-page fetches returned `000` on first contact and were re-issued after
a delay and/or against the id's other archived URL form and timestamp. This is
**not** a bypass — no URL was altered beyond the two legitimate forms, no
`savepagenow`, no cookie/`--header` trick. The final count is **105/105 HTTP
200**, and the enumeration is therefore complete.

### 1.2 The complete board — all 105 post ids

Columns: id · date · author · body-text chars · own-namespace attachment
images (`565`/`567`) · title. **Every row has a retrievable 200 body.**

| id | date | author | chars | 565/567 imgs | title |
|---|---|---|---|---|---|
| 619 | 2017.04.05 | VSpang | 416 | – | [Guide] How to use the Tips section |
| 714 | 2017.04.06 | LucasYeeTr | 23 | – | How to advance units? |
| 787 | 2017.04.07 | JohnsonNg | 31 | – | Increase unit star |
| 954 | 2017.04.09 | Eisei | 544 | – | Clarification on skills |
| 974 | 2017.04.10 | JackCullen | 117 | – | Where do you farm? |
| 1260 | 2017.04.17 | HoZhihui | 1,960 | – | Guide and tips for the game ( updated) |
| 3816 | 2017.05.15 | GrassJelly | 48 | – | Is there a tier list out there? |
| 4921 | 2017.05.15 | Jai | 148 | – | Any tips on what to do and not do to? |
| 12043 | 2017.05.17 | MongoBjj | 29 | – | Unit? |
| 12240 | 2017.05.17 | Ragnaros | 211 | – | Team Comps? |
| 12305 | 2017.05.17 | Obinar | 38 | – | New training partners? |
| 12420 | 2017.05.17 | Kuhn | 44 | – | Advancement |
| 12654 | 2017.05.17 | Maxstroid | 82 | – | Veteran Level |
| 16494 | 2017.05.18 | Jiayun | 143 | – | What is Beginner 3? |
| 17502 | 2017.05.19 | Cloud_Strife | 314 | – | Few General Tips |
| 18069 | 2017.05.19 | ChillerX5 | 51 | – | How to advance my 2 star hunter |
| 18237 | 2017.05.19 | Elolust | 147 | – | Characters lvl |
| 19196 | 2017.05.19 | Weissheit | 142 | – | Character attributes - [4 chars UNRECOVERABLE: post 19196 title truncated by an encoding fault; NOT reconstructed] |
| 20858 | 2017.05.20 | Walphur | 150 | – | Easy tip to reduce amount of taps but maintain damage |
| 21506 | 2017.05.21 | Gareth | 284 | – | Bonuses for collecting characters |
| 21817 | 2017.05.21 | waldo_667 | 900 | – | advancing characters |
| 22732 | 2017.05.22 | Bond | 476 | – | Big tip for arena |
| 23201 | 2017.05.22 | HoZhihui | 501 | – | Tip for skill training |
| 23265 | 2017.05.22 | YukiJudai | 460 | – | Small FAQ |
| 24731 | 2017.05.23 | Kirinxd | 329 | – | General item shops |
| 24901 | 2017.05.23 | HoZhihui | 6,138 | – | Game guide and tips |
| 30997 | 2017.05.27 | KagamiX | 222 | – | Money/Rup |
| 30999 | 2017.05.27 | KagamiX | 216 | – | Money/Rup |
| 42865 | 2017.05.31 | McAroni | 289 | – | Character's stats info |
| 46406 | 2017.06.01 | Kaasha | 185 | – | Blustone guide! |
| **55607** | 2017.06.05 | VSpang | 685 | 3 | Lana's Guidebook Ch. 1: Put Your Back into It! Using Your Skills |
| **55613** | 2017.06.05 | VSpang | 523 | 3 | Lana's Guidebook Ch. 2: Don't Crash and Burn! Watching the Fuel Meter |
| **55618** | 2017.06.05 | VSpang | 1,366 | 5 | Lana's Guidebook Ch. 3: There's No I in Team. About Hunter Roles |
| **55626** | 2017.06.05 | VSpang | 1,001 | 8 | Lana's Guidebook Ch. 4: Rock, Paper, Scissors! Understanding Elemental Attributes |
| **55641** | 2017.06.05 | VSpang | 864 | 5 | Lana's Guidebook Ch. 5: Harder, Better, Faster, Stronger! Advancing your Hunter |
| **55672** | 2017.06.05 | VSpang | 651 | 6 | Lana's Guidebook Ch. 6: Where in the World is...? Using Hunter Traces |
| **55691** | 2017.06.05 | VSpang | 1,319 | 4 | Lana's Guidebook Ch. 7: I Wanna Be the Very Best! Climbing Up your Veteran Status |
| 62649 | 2017.06.12 | Gareth | 98 | – | Entrust |
| 69900 | 2017.06.22 | Nexor | 168 | – | List of traces per dungeon |
| 83188 | 2017.07.22 | Majo | 1,591 | – | Some Arena advice |
| 83282 | 2017.07.22 | Minueko | 3,866 | – | Bear Bring Beginner Barena Bips |
| 93837 | 2017.08.06 | Silverberg | 822 | – | The cost of making a five star hunter from a pile of novices |
| 94620 | 2017.08.07 | ninjakitteh | 317 | – | Switching hunters in expedition |
| **95628** | 2017.08.09 | BlackGeneral | 127 | 4 | Little tips about dormitory. |
| **96417** | 2017.08.10 | reese_y | 741 | 2 | Tips for advancing in the PVP/Arena |
| 97147 | 2017.08.11 | Spondyl | 2,331 | – | Some tidbits for keen-eyed lore fans |
| 98323 | 2017.08.14 | reese_y | 457 | – | Bronze, silver, or gold? |
| **100785** | 2017.08.19 | BlackGeneral | 643 | 4 | How to retake the money Westfield as stole you. |
| 105976 | 2017.08.27 | Spondyl | 214 | – | A Hunter's First Steps |
| **127526** | 2017.10.01 | Spondyl | 5,085 | 5 | A fix for "Network communication is not stable" |
| 138442 | 2017.10.11 | HoZhihui | 4,451 | – | Guide |
| 172181 | 2017.11.05 | GiulianoMo | 489 | – | Guide for newcomers |
| 173620 | 2017.11.05 | Kytsu | 3,166 | – | [Guide] Your first week in Blustone |
| **174414** | 2017.11.05 | LeGeneralNoire | 927 | 9 | BlackGuidebook Vol 1: How to Write A Guide and Stop the Apocalipse. |
| 175648 | 2017.11.05 | Smn42 | 2,205 | – | [Guide] What a new player should know. |
| 176367 | 2017.11.06 | Lgtmagician | 6,450 | – | [Guide] Hello Captains |
| 178267 | 2017.11.06 | farameir13 | 510 | – | Things I wish I knew (guide) |
| **178832** | 2017.11.06 | DaShade | 6,419 | 3 | Game Review - Blustone - A Beyond The Bound Story - Cute RPG Battler - Android / iOS / PC |
| 181257 | 2017.11.07 | Ratagast | 308 | – | New Players Guide |
| 183145 | 2017.11.07 | Wachi | 196 | – | Guide for beginner |
| 184960 | 2017.11.07 | OneShot | 2,524 | – | Reading a simple beginner's guide in one shot |
| 185186 | 2017.11.08 | siong | 250 | – | Pvp tips for new player |
| 185911 | 2017.11.08 | Dyos | 1,927 | – | New Players Guide from a One Week Old Player |
| 188040 | 2017.11.08 | Kirei | 3,008 | – | Guide for Beginning Players |
| 188557 | 2017.11.08 | HarrisonLane | 3,092 | – | Tips from a 1 month player |
| **189046** | 2017.11.08 | shvrkboy | 8,962 | 14 | Just the tips [Beginner Guide] - shvrkboy |
| 189672 | 2017.11.09 | Nievel | 478 | – | A simple guide/reminder for players |
| 190286 | 2017.11.09 | PanicPac | 701 | – | Some tips for the newbies |
| 190985 | 2017.11.09 | lolislayer | 1,028 | – | Beginners Guide |
| **192223** | 2017.11.09 | SyanL | 5,116 | 12 | A Beginner's Guide - by SyanL <3 |
| 192930 | 2017.11.10 | cyhcyh | 991 | – | A simple guide for beginners |
| 193383 | 2017.11.10 | UrielSR | 4,432 | – | [Guide] Some tips for the Beginners |
| 194024 | 2017.11.10 | RobyF | 375 | – | A few quick tips |
| 194179 | 2017.11.10 | Taurus_Silver | 563 | – | Guide: New Players Tip |
| 195719 | 2017.11.11 | lolr | 5 | – | Helpful tips |
| 196537 | 2017.11.11 | HowlsCastle | 928 | – | Newbie Guide :) |
| 196827 | 2017.11.11 | Rin_Okumura | 303 | – | Things i wish i knew-beginner tips |
| **197134** | 2017.11.11 | Renjixfen | 2,909 | 3 | Casual?s Guide to Character Ranking |
| 197642 | 2017.11.11 | d3v1l404 | 1,439 | – | Just some tips for new players |
| **197745** | 2017.11.12 | Alaiko | 19,072 | 11 | Guide to Blustone |
| 197885 | 2017.11.11 | HououinKyouma | 219 | – | How to keep winning |
| 198374 | 2017.11.12 | ArkenDragon | 2,361 | – | Essential Battle Non-essentials |
| 199332 | 2017.11.12 | BonkersRabbid | 7,612 | – | A guide that paints the road to being a Pro on BluStone! |
| **199711** | 2017.11.12 | WinJ | 8,456 | 11 (+56 external) | A Glorious Guide on [How not to be a n00b] [OUTDATED for Patch 1.2.0] |
| 201598 | 2017.11.13 | Enheim | 6,876 | – | Enheim?s guide for beginners |
| 201800 | 2017.11.13 | Axzariea | 1,374 | – | A small guide for starting Blustone! |
| 203849 | 2017.11.14 | Ziel- | 794 | – | Few Things i Wish i Knew When i Begin To Play - [4 chars UNRECOVERABLE: post 203849 title truncated by an encoding fault; NOT reconstructed] |
| **215324** | 2017.11.21 | VSpang | 2,452 | 6 | Lana's Guidebook Ch. 8: Transcendence Gives You Wings~! How to Transcend Your Hunter |
| 316245 | 2018.01.27 | Itida | 31 | – | How do you recruit using manda |
| 319492 | 2018.01.28 | Swifts | 144 | – | Ruins Community |
| 327919 | 2018.01.30 | Shiarial | 1,344 | – | Tips for begginers, how to build a good team. |
| **330982** | 2018.01.31 | BlackGeneral | 2,693 | 6 | List of Blustone FanArts |
| 395828 | 2018.02.16 | Nishino | 6,081 | – | Secrets a Top PvP player won't let you know. |
| 401574 | 2018.02.18 | FletchGod | 2,010 | – | How to git good for players who are cheap (f2p) |
| 440600 | 2018.02.26 | Nishino | 224 | – | FAQ for learners/semi experienced |
| **507556** | 2018.03.09 | FatherVinh | 1,063 | 1 | Hunter Tier List as of 02.08.2018 |
| 570606 | 2018.03.20 | Kevio | 156 | – | Denali or Tyltyl? |
| 588855 | 2018.03.25 | makoto69 | 108 | – | how do I use veteran tickets? |
| 601569 | 2018.03.29 | Katte | 907 | – | My Guide To You: Just The Beginning |
| 611579 | 2018.03.31 | Aromau | 245 | – | I need some help!! |
| 613470 | 2018.03.31 | Swedcarp | 407 | – | Fate? Webs and boosts |
| 630834 | 2018.04.04 | Dasai | 61 | – | Offense team help |
| **637237** | 2018.04.05 | Elysian97 | 131 | 2 | Help reform my team |
| 642013 | 2018.04.06 | Noxid | 267 | – | Best character from walnut event for newbie? |
| **650463** | 2018.04.08 | Sh17 | 91 | 1 | Which of these should be my first 5*? |

Bold rows are the **23 posts that carry their own attachment images**. The
remaining 82 posts are **text-only** — zero in-content `<img>` tags at all.

### 1.3 Board structure — what `share_en` actually is

- **Header/counters:** 833 CDX rows resolve to 726× `200` + 107× `302`;
  710 rows are the `index.php?mid=share_en&document_srl=…` permalink-body form,
  90 the `/share_en/<id>` form, 33 board/sort/login/root rows. 105 distinct ids.
- **Pagination:** archived list pages `page=1`…`page=9`, in both the `&l=en` and
  plain `?mid=share_en&page=N` forms. Page 1's own nav shows only `1..5`
  because that capture is from a partial crawl; the *board* itself has more
  pages than 9 (page 1 lists post numbers up to 94, and post `650463` is dated
  2018-04-08, after the last list capture of 2018-06/07). **Page-level
  completeness therefore remains unknown** — the 105 ids are "every post with an
  archived body", not necessarily every post ever posted. This is the same
  limitation the prior pass recorded (§2.4) and it is **not** resolved here.
- **The list pages carry no content thumbnails** — only site chrome — so the
  board list can never itself yield a stat panel. Same structural limit
  `review-posts-2026-10-05.md` §1.4 found on `event_en`.
- **Character:** a community **guide/tips board**, not a "share your
  screenshots" board. The official `event_en` notice `75679` invited screenshot
  sharing on **`event_en`**; `share_en` is where players posted **written
  advice**. This matters, because it changes what the board can possibly
  contain: prose guides quote *costs and rules*, not *per-hero stat panels*.

### 1.4 Attachment namespaces found per post — and the hard negative

Own-namespace attachments per post (path scheme
`/files/attach/images/<board-prefix>/<a>/<b>/<hash>.<ext>`, where `a`=`post id ÷
100` and `b`=`post id mod 100`, matching the prior pass's `565/745/197` finding
for post `197745`):

| post | namespaces | own images | uploader-chosen alt filenames (the only subject hints) |
|---|---|---|---|
| 55607 | `565/607/055` | 3 | `main.jpg`, two hash-named `.jpg` |
| 55613 | `565/613/055` | 3 | `main.jpg`, two hash-named `.jpg` |
| 55618 | `565/618/055` | 5 | `main.jpg`, 4 files whose `alt` is mojibake Korean (`????_??.png`) |
| 55626 | `565/626/055` + `567/943/018` + `567/029/019` | 8 | all `alt` empty — a scraped role/element diagram set |
| 55641 | `565/641/055` + `567/046/019` | 5 | `main.jpg`, `527ccb73….png`, `1.jpg`, `2.jpg` |
| 55672 | `565/672/055` | 6 | `main.jpg`, `527ccb73….png`, `1.jpg`–`4.jpg` (same base diagram as 55641) |
| 55691 | `565/691/055` | 4 | `main.jpg`, `1.1.jpg`, `2.jpg`, `1.2.jpg` |
| 95628 | `565/628/095` | 4 | three `Screenshot_20170809-*` + `20170809_141956.png` |
| 96417 | `565/417/096` | 2 | `Blustone_2017-08-10-04-56-00.png`, `20170810_045812.png` |
| 100785 | `565/785/100` | 4 | four `20170818_*` captures |
| 127526 | `565/526/127` | 5 | five `Screenshot_20171001-*` (Android DNS settings) |
| 174414 | `565/414/174` | 9 | `I'm too good with you.png`, two Spanish `Captura de …`, `20170818_154602.png`, 4 forum GIFs |
| 178832 | `565/832/178` | 3 | three `Screenshot_2017110*` (loading screen, village, dorm) |
| 189046 | `565/046/189` | 14 | **`exp rate.png`, `4starguide.png`, `transend.png`, `priority hunters.png`, `Abyss4.jpg`, `Abyss5.jpg`, `money wise.png`, `fuel resets.png`, `pure fuel.png`, `skills.png`**, `autocruise.png`, 3 `IMG-855*` |
| 192223 | `565/223/192` | 12 | `Image.jpg` + 11 UUID-named `.jpg` |
| 197134 | `565/134/197` | 3 | three iPhone UUID `.jpeg` |
| 197745 | `565/745/197` | 11 | `Cruise_beginning.png`, `Cruising.png`, `Ruins.png`, **`Training Gym.png`**, `Fight Club.png`, `Arena.png`, 5 `Screenshot_2017-11-11-*` |
| 199711 | `565/711/199` | 11 (+56 external) | 11 `Screenshot_2017*` |
| 215324 | `565/324/215` | 6 | `lana.jpg`, `transc.jpg`, **`di1.PNG`, `di2.PNG`, `di3.PNG`**, `trans2.PNG` |
| 330982 | `565/982/330` | 6 | one GIF repeated 6× (`I did this **** in 1.24 min.gif`) |
| 507556 | `565/556/507` | 1 | `20180306_111705.png` |
| 637237 | `565/237/637` | 2 | `Screenshot_20180405-172305.jpg`, `-172315.jpg` |
| 650463 | `565/463/650` | 1 | `Screenshot_20180408-012318.png` |

Totals: **26 distinct own namespaces**, **128 own-namespace image
references**, **23 posts with attachments**, **82 text-only posts**.
`565` is the board prefix for all `share_en` posts; `567` appears in exactly
two posts (`55626`, `55641`) for what look like **scraped web diagrams**
re-uploaded by the same author (VSpang, the official guide author) — the
`527ccb73….png` base image is reused across `55641` and `55672`.

**56 further `<img>` tags in `199711` are external hotlinks**, not board
attachments: 54 to `vsfan.net/wiki/images/…` (item and hunter **icons** —
`Metron_Crystal.png`, `Akasha_Trace.png`, `2star-symbol.png`, `Captain-icon.png`
…) and 2 to `media-curse.cursecdn.com`. These are **structurally incapable of
holding a stat panel** (45–86 px wiki thumbnails) and belong to a different
domain anyway.

**The decisive negative.** Despite 128 references to 128 own-namespace files
across 23 posts:

- A whole-namespace CDX sweep of `/files/attach/images/` returns **178 rows**
  (177 with 200), and the prefixes are `75605`(148), `175`(7), `193`(6),
  `75601`(6), `75603`(4), `183`(2), `185`(2), `203`(2), `136`(1).
  **Neither `565` nor `567` appears.**
- Dedicated `565`, `565/745/197` and `567` prefix sweeps each return
  **zero rows**.
- Exact-URL CDX on four individual `565` files returns **zero rows** each.
- Direct `im_` fetches on five `565`/`567` files return **404** (4,727-byte
  error page) or curl `000`. A wildcard-timestamp fetch (`2018im_`, `2im_`)
  returns **404** / `000`.
- **Control:** the same exact-URL query on a known-archived `75605` file returns
  a 200 row (58,647 bytes), and the `75605` prefix sweep returns 148 rows.

**Conclusion: the Wayback Machine never captured a single `share_en` player
screenshot.** This is not "200 row ≠ retrievable bytes" flakiness as in
[`board-attachments-2026-10-05.md` §2.7 — there are **no rows at all** for this
namespace, verified against a working control. The prior pass's "untested
retrieval risk" is now a **settled negative**, and the entire image half of this
lane is closed.

### 1.5 Bodies with no stat content — the dominant case

The 82 text-only posts are short community questions and answers. Verbatim
examples, transcribed exactly:

- `195719` "Helpful tips", author `lolr`, **5 characters of body text**. Nothing
  else exists.
- `316245` "How do you recruit using manda", `Itida`, 2018-01.27, 31 chars.
- `630834` "Offense team help", `Dasai`, 2018.04.04, 61 chars.
- `714` "How to advance units?", `LucasYeeTr`, 2017.04.06, 23 chars.
- `637237` "Help reform my team", `Elysian97`, 2018.04.05, 131 chars:
  > Can anyone help me to make my offense defense and main team. Im kind of
  > confused because i have quiet many 3 stars and above hunter
- `650463` "Which of these should be my first 5*?", `Sh17`, 2018.04.08, 91
  chars:
  > I was thinking of Nene, but it's taking too long to get 4 4* , and that made
  > me rethink it.

None of these can carry a stat panel even in principle; three of them *do*
carry screenshots (`637237` ×2, `650463` ×1) which are **unretrievable** per
§1.4.

### 1.6 `507556` "Hunter Tier List" — read in full, and it is meta, not stats

Title `Hunter Tier List as of 02.08.2018`, author `FatherVinh`, 2018-03-09,
1,063 characters, **1 own image** (`565/556/507/20180306_111705.png`, which is
the tier-list graphic itself and is unretrievable).

Body text, verbatim as rendered:

```
Here is my take on hunter priorities based on the current meta in the top 100
ranked players.
Focus on 5 starring hunters over transcending them. A 5* hermes with no
transcendence is stronger than a 4* hermes with full transcendence.
Focus on a good mix of hunters from the highest tier shown that you have
access to. There is no "dream team." You will always be changing your team
according to the enemy's defense and element.
For PVE, have a team consisting of a good attacker, defender, bomber, and
healer. Don't expect to advance far wothout variety.
The meta for offense is a strong attacker such as Hermes and multiple
bombers. Possibly a healer or tank if you need it.
The meta for defense is 1-3 tanks and 1-3 healers OR use the meta for offense
(Hermes + 4 bombers etc)
These are NOT 100% the best team builds, these are the most popular in the
Top 100 ranking players in Fight Club.
Please spread this post to as many people with questions as you can so you can
de-saturate the forums with people asking who to 5 star next or what is the
best team.
Amen.
```

**Zero stat values.** The post is a *meta opinion*, and the actual tier
assignments live in the single unretrievable image. Named hunters (`Hermes`)
carry no numerals and no level/gear state.

### 1.7 `192223` "A Beginner's Guide - by SyanL" — the guide the prior passes' citations pointed at

`training-public-evidence.md` and `training-rankup-rules.md` both cite
`share_en/192223` as a community source that "timed out" on the live site. Its
**archived body is now read**. 5,116 characters, 12 own images
(`565/223/192`, all UUID-named except `Image.jpg`). Verbatim opening:

```
A Beginner's Guide
Currency
Manda
obtainable only by in-app purchases
Rupee
obtainable through auto cruising or rupee ticket drops
Tickets
With Lottery
Rupee Tickets : 5000 rupees
Fuel Tickets : 60 fuels
Challenge Invitation Tickets : 2 challenge invitation
May win up to x2 or x 16 when claimed
If you win the x16 lottery, you will obtain 3 veteran tickets which you can
gift to other players
(update : x16 is applicable to both rupee, fuel and challenge invitation
tickets )
Can only be gifted
Veteran Tickets
To gift a veteran ticket
When receiving a veteran ticket
Importance of Veteran Status
More features (such as number of dispatch allowed) unlocked
At Guru 3, receive a hidden hunter called Vincent
You will receive 20 vet points on each daily login and another 20 upon
completing 7 daily goals, under bonus goal reward.
```

The body then lists shop priorities and one hard number:
`Metron Crystal ( 1000 chips )` in the Fight Club Shop. The rest of the guide's
substantive content is in the 12 images, **all unretrievable**.

---

## 2. UNPUR[E] — everything that is not a verbatim base-stat reading

### 2.1 Confirming the negative: no stat panel in any body

Two independent scans over the full 166,838 characters of extracted body text:

1. `(HP|ATK|DEF|attack|defence|defense|health|power|strength)` — 24 posts match
   on **prose only**. Every hit is a sentence of the form "they do not have a
   lot of health and defense" (`55618`), "Hermes is running low on hp, switch out
   to Nene" (`176367`), "a high atk" (`193383`). **No numeral is attached to
   any of them.**
2. `\b(HP|ATK|DEF|power|health|damage|strength|rating|force)\b\s*[:=]?\s*\d{2,}`
   and `\d[\d,]{2,}\s*(HP|ATK|DEF|power)` — **0 posts match.**

**Zero HP/ATK/DEF numerals in 105 posts.** Hero coverage stays **1/113 (0.9%)**,
accessories **1/100**, monsters **0/22**.

### 2.2 The actual numeric payload — economy and progression, not base stats

Eight posts carry dense, quotable numeric tables. **None is a hero base stat**,
but all are legitimate original-era economy evidence for the rebalance work in
`§19`/`§25` of `coverage.md` and for the project's provisional economy
fixtures. Recorded verbatim where it matters; full transcriptions are in the
section 2.2 sub-tables.

#### 2.2.1 EXP-to-max by star — **three independent posts agree exactly**

`199711` (WinJ, 2017-11-12), `189046` (shvrkboy, 2017-11-08), `138442`
(HoZhihui, 2017-10-11) and `201598` (Enheim, 2017-11-13) all publish the same
ladder:

| star | EXP to max level | advances from |
|---|---|---|
| 1★ | 200 | 1★ (1→2) |
| 2★ | 400 | 2★ (2→3) |
| 3★ | 1,200 | 3★ (3→4) |
| 4★ | 4,800 | 4★ (4→5) |
| 5★ | 24,000 | – |

`138442` and `201598` state the max ordinary level explicitly: **level 30**
("The hero you want to advance have to be max at 30 level" / "once your
character is maxed level"). `24901` describes it as "4 dots and 5 diamonds".

This is a **4-way independent corroboration** of the original EXP ladder and
level cap, and it is materially stronger evidence than anything the project
currently holds for those curves. It still says **nothing about HP/ATK/DEF
growth per level**, which remains unrecovered.

#### 2.2.2 Advancement (star-up) costs — **two posts agree exactly**

`138442` and `24901` publish the identical table:

| advance | fodder | rupees |
|---|---|---|
| 1★ → 2★ | 1 × 1★ | 1,000 |
| 2★ → 3★ | 2 × 2★ | 3,000 |
| 3★ → 4★ | 3 × 3★ | 12,000 |
| 4★ → 5★ | 4 × 4★ | 60,000 |

`93837` (Silverberg, 2017-08-06) reaches the same numbers by a different route
and adds the 5★ promotion figure:
> And finally, the 5star. 5x 4stars. 24*5= 120 hunters on the chopping block […]
> (Word's out that the promotion cost is 60k. In this case, 5*36 = 180k rupees,
> plus this 60k makes a total cost of 240k rupees.)

`189046` independently states the fodder counts: 2★ needs 1× 1★, 3★ needs 2×
2★, 4★ needs 3× 3★, 5★ needs 4× 4★, and totals **120 1★ / 24 2★ / 5 4★ =
149 + 1**, itself estimating "205 hunters in total".

#### 2.2.3 Transcendence costs — **three posts agree, one differs in a way that matters**

Official guide `215324` (VSpang, 2017-11-21) publishes the full 3×3 table, and
`197745` (Alaiko) and `138442` reproduce it:

| base | step | Metron Crystals | Metron Fragments | Rupees | duplicate 3★ hunters |
|---|---|---|---|---|---|
| 1★ | 1st | 5 | 50 | 5,000 | 1 |
| 1★ | 2nd | 15 | 150 | 15,000 | 2 |
| 1★ | 3rd | 45 | 450 | 45,000 | 3 |
| 2★ | 1st | 7 | 70 | 7,000 | 1 |
| 2★ | 2nd | 25 | 250 | 25,000 | 2 |
| 2★ | 3rd | 60 | 600 | 60,000 | 3 |
| 3★ | 1st | 9 | 90 | 9,000 | 1 |
| 3★ | 2nd | 30 | 300 | 30,000 | 2 |
| 3★ | 3rd | 80 | 800 | 80,000 | 3 |

`197745` states **the 2★ 2nd step as 25 crystals / 250 fragments / 25,000
rupees**, matching `215324`. `189046` gives 2★ 2nd as `?` (unknown) and 3★ as
9/30/80, matching. `138442` **omits the 2★ row entirely**.

`215324` also asserts the key rule the project's fixtures only approximate:
> Transcendence gives you the same amount of stat bonuses no matter what your
> Hunter Grade is.

And the gate: 1st transcendence requires a **3★ base + one 3★ duplicate**; 2nd
requires 4★ base + two 3★ duplicates; 3rd requires 5★ base + three 3★
duplicates (`215324`, `197745`, `189046`, `201598` all agree).

#### 2.2.4 Dispatch / EXP-per-fuel — **`199711`'s table, and a second reading in `197745`**

`199711` publishes a per-star dispatch cost table:

| star | EXP to max | level-40 cruises | fuel |
|---|---|---|---|
| 1★ | 200 | 18.18 → 19 | 114 |
| 2★ | 400 | 36.36 → 37 | 222 |
| 3★ | 1,200 | 109.09 → 110 | 660 |
| 4★ | 4,800 | 436.36 → 437 | 2,622 |
| 5★ | 24,000 | 2,181.81 → 2,182 | 13,080 |

derived from **11 EXP per 6 fuel (1.83 EXP/fuel)** at level 40. `199711`
adds that EXP is **not shared** between characters, is independent of
star/type/element, and that level 40 beat level 39 by ~20% over 100 tested
dispatches. `201598` and `197134` independently give the same 11-exp/6-fuel
figure and the same "19 runs for 1★, 37 runs for 2★" reading; `197134` adds
**110 runs** for rank-3 and **96 rank-1** for a single rank-4→5. `197745`
confirms the 6-fuel boundary: levels ending in 5 or 0 cost more, and "the next
region costs 7 fuel".

#### 2.2.5 Shop / currency prices

- Fuel direct purchase: **5,000 rupees for the first two per day, then 9,000**
  (`24901`). `23265` states "5000 for 1-2 and 3-6 cost 9000". `189046`: "You
  can only buy up to three fuel recharges for 5000 coins. After that the
  recharge will increase to 8000 during the day." (`176367` says "costs 5000
  for the first 3x […] costs more after". The three counts **disagree** —
  see §2.3.)
- Shop refresh: **every 4 hours** (`24901`, `189046`); shop fuel tickets fixed
  at **5,000** (`24901`); daily challenge reset **4,000** for first three
  (`189046`).
- Lottery Mouse ticket payouts (`192223`): Rupee Ticket **5,000 rupees**, Fuel
  Ticket **60 fuels**, Challenge Invitation **2**; may win **×2 or ×16**; a ×16
  also yields **3 veteran tickets**.
- Estelle's Hunter Shop (`199711`): Fuel Ticket **5,000 for 1**; Challenge
  Invitation **5,000 for 1**; Metron Fragment **1,500 for 15**.
- Fight Club Shop (`199711`): Golden Hunter Traces **150 for 2**; Metron
  Crystal **1,000 for 1**; Golden Hunter Materials **75 for 3**.
- Abyss reset: **30,000 rupees or 30 Manda**, cost rising per reset
  (`197745`); `189046` says "Abyss resets are 30 manda each".
- Challenge/daily gift: **100 rupees** per player who uses your hunters
  (`199332`); daily challenge all-complete gives **1 fuel + rupee ticket**
  redeemable for **60 fuels / 5,000 rupees**, plus **20 veteran points**
  (`199332`, `192223`).
- Share button: **1,000 gold** (`178832`).
- `176367`: mats cost **1,000 rupees** in the daily shop.

#### 2.2.6 Progression facts with numbers, no stats

- Elite-scroll drop rate: "about **60** elite scrolls before pull a nat 3* unit"
  (`176367`).
- Veteran gating: **Guru 3** grants the hidden hunter **Vincent**; Guru 3 is
  "about **60k+** veteran points" (`201598`, `192223`).
- Dorm building unlocks: two at level **15**, two at level **30** (`178832`).
- Hunter recruitment by clearing **30 stars** per area; first free recruit is
  **Lapis**, day-2 recruit is **Sienna** (`178832`).
- Free tier gates: 1★/2★/3★ from normal scroll + traces; 3★ natural
  (`karl`, `nene`, `akasha`) elite-scroll only (`24901`).

### 2.3 The one substantive internal contradiction found

The **fuel purchase daily limit is reported three different ways**, all from
the same era:

| Source | Date | Claim |
|---|---|---|
| `24901` | 2017-05-23 | first **two** purchases 5,000, then 9,000 and rising |
| `23265` | 2017-05-22 | "5000 for 1-2 and **3-6** cost 9000" |
| `189046` | 2017-11-08 | "only up to **three** fuel recharges for 5000 coins. After that […] **8000** during the day" |
| `176367` | 2017-11-06 | "costs 5000 for the first **3x** I believe, never buy more than 3x, costs more after" |

Three independent counts (2 / 3 / 3) and **two different post-soft-cap prices
(9,000 vs 8,000)**. This is a genuine unresolved discrepancy in the original
economy, not a transcription error, and it is directly relevant to the
replica's fuel-reset fixture. It must not be silently resolved to one value.

### 2.4 Rank / tier naming — a terminology trap, recorded so it is not misread

These posts use **"star"** (1–5, the *grade*/rarity) and **"transcend tier"**
(T1–T3) and **"veteran status"** (Guru/Expert levels) as three different
things, and `24901` maps them to **border colours**:

```
1 star ( brown)   2 star ( sliver)   3 star ( gold)   4 star ( green)   5 star ( blue)
```

`197745` and `189046` both note that a natural 3★ is stronger than a 1★/2★ at
the same level (`138442`), and `24901` says "natural 3 stars are stronger than
2 stars and 1 star". **None of these is a stat value**; they are grade
relations. Do not let a 3★/5★ token from these posts enter a stat ledger.

### 2.5 Identity tokens from these posts — recorded, unusable as stats

| Token | Where | Why it is not coverage |
|---|---|---|
| `Hermes`, `Captain`, `Levi`, `Denali`, `Athena`, `Akasha`, `Diana`, `Lantern`, `Patrone`, `Karl`, `Lapis`, `Nene`, `Rebecca`, `Gerald`, `Metis`, `Tyltyl`, `Sylvester`, `Bruce`, `Hecate`, `Locke`, `Robin`, `Riko`, `Sienna`, `Acerola`, `Balian`, `TeddyBomber`, `Mowgli`, `Vincent` | many | **named in advice prose only**; no level, rank, gear, jewel or equipment state. "Hermes" alone cannot identify a catalog row. |
| `Fenrir`-class role/element pairs ("Captain (Electric Balanced Tank)", "Levi (Ice Glass Cannon)", "Hermes (Fire Glass Cannon)", "Lantern (Fire Buff Attack Support)", "Patrone (Ice Buff Attack Support)", "Diana (Electric Buff Attack Support)", "Athena (Defense)") | `189046`, `199711` | player shorthand, **not** catalog metadata; role/element enum values are already recovered from native (`analysis/research/card-enums.md`). Do not merge. |
| `Diana` as the worked transcendence example | `215324` | the guide says "all her statistics have increased" — **the before/after numbers are in the 6 images**, which are unretrievable. This is the single most tantalising miss in the pass (§4.1). |
| `1star-symbol.png`, `2star-symbol.png`, `1*`/`2*`/`3*` glyphs | `24901`, `199711` images | grade markers, not values |
| `30k power`, `60k+ veteran points`, `below 30k power` | `83282`, `201598` | **team/personal power thresholds in advice prose**, no team composition or level given |
| `gauge of 5.5`, `1/8 stamina` | `198374` | fever gauge and a **stamina** resource this project has not otherwise documented; no identity, no gear |
| 54 `vsfan.net/wiki/images/…` icons | `199711` | item/role/hunter **icons** at 30–86 px; structurally incapable of a stat panel, and a different domain |

### 2.6 Method limits of this pass

- **`collapse=urlkey` returns one row per URL**, so per-id multiple-capture
  counts are unavailable. The census is an existence map, not a capture
  history.
- **Board-level completeness is still unknown.** Only list pages 1–9 exist in
  the archive; the board demonstrably ran past post number 94 and past
  2018-04-08, so posts without archived bodies are certainly not enumerated.
  This pass closes the *105-id corpus*, not the *board*.
- **No OCR and no image was opened** — because no image can be opened (§1.4).
  Every subject attribution in §1.4 is `alt`-attribute based and labelled as
  such.
- **`curl 000` is not an HTTP status.** It appears on ~26 of the ~140 fetch
  attempts and is recorded as transport failure. All of them were re-issued
  against a legitimate alternate archived form; the final state is 105/105 at
  HTTP 200.
- **Text extraction is tag-stripped, not OCR'd.** A stat panel rendered as
  *text inside a post body* would have been captured; a stat panel *inside an
  image* would not. §1.4 proves no image is available, so both readings are
  exhausted for this corpus.
- **Era:** every post is **2017-04-05 → 2018-04-08**, i.e. entirely
  **pre-2019-09-05**. Per
  [`stat-version-context.md`](stat-version-context.md) all of §2.2 is
  pre-rebalance economy and must not be mixed with post-2019 values.

---

## 3. Ranked candidates for the next lane

Ranked by expected yield per fetch, weighted toward `stat` / `review` /
`guide` / `progress` subject matter as instructed. **Rank 0 is the finding that
reorders everything below it.**

### Rank 0 — the whole `share_en` image lane is CLOSED. Do not re-attempt.

`565` and `567` have **zero** archived rows, verified against a working
`75605` control, with five direct `im_` fetches returning **404**. Any future
plan that spends fetches on `share_en` player screenshots is spent on nothing.
This supersedes `review-posts-2026-10-05.md` §3 items 1–3 and §4's
"unresolved" row for `565/745/197/`.

### Rank 1 — mine the §2.2 numeric tables (no fetch cost at all)

The highest-value output of this pass is **already in hand** and costs nothing
further: the 4-way-corroborated EXP ladder (200/400/1200/4800/24000), the
level-30 cap, the 4-way-corroborated advancement costs
(1k/3k/12k/60k), the 3-way-corroborated 3×3 transcendence matrix, the 11-exp/6-fuel
dispatch economy, and the shop price list. **Action:** reconcile §2.2 against
the project's provisional fixtures in `server-ts` and record which are now
community-evidenced rather than invented. Only §2.3's fuel-limit contradiction
needs new sources.

### Rank 2 — `42865` "Character's stats info" (McAroni, 2017-05-31)

The **only post whose title promises stat-panel content**, and it is
**text-only** — 289 characters, zero images. Read in full during the scan; it
is a short forum answer about which numbers the UI shows. **Its content is
already extracted and contains no values.** Effectively a dead end, but it is
the cheapest possible check and it is now closed.

### Rank 3 — `197134` "Casual?s Guide to Character Ranking" (Renjixfen, 2017-11-11)

Best *unopened* candidate by subject: a **hand-computed ranking-efficiency
guide** ("I did all this by hand"), 2,909 characters, **3 iPhone screenshots**
(`81554CCE-….jpeg`, `30A10D6C-….jpeg`, `C644ED48-….jpeg`) — unretrievable. Its
body already yields the **119 rank-1 / 96 rank-1 / 19 / 37 / 110-run** figures.
**But the 3 images are unreachable**, so its marginal value is zero for stats.

### Rank 4 — `189046` "Just the tips [Beginner Guide]" (shvrkboy, 2017-11-08)

The single richest body in the board (8,962 chars) with **14 images**, six of
them named for exactly the subjects this goal needs: `exp rate.png`,
`4starguide.png`, `transend.png`, `priority hunters.png`, `Abyss4.jpg`,
`Abyss5.jpg`, `skills.png`, `money wise.png`. If any `565` bytes were
recoverable this would be the top target. **They are not** (§1.4). Ranked here
only to record that it was the best candidate and is closed, not because it is
actionable.

### Rank 5 — `215324` "Lana's Guidebook Ch. 8: Transcendence" (VSpang, 2017-11-21)

The **most likely single image to contain a stat panel**: the body says
*"Ta-da! Diana is transcended! And as you can see, **all her statistics have
increased**"* — i.e. `transc.jpg` / `trans2.PNG` / `di1–di3.PNG` are almost
certainly a **before/after stat panel**. Unretrievable. This is the pass's most
concrete documented loss and the strongest argument that the `565` gap
matters.

### Rank 6 — `507556` "Hunter Tier List as of 02.08.2018" (FatherVinh, 2018-03-09)

One image = the entire tier-list graphic (tiers, hunter names, possibly star
grades). **Late-era** (2018-02, still pre-rebalance). Unretrievable.

### Rank 7 — `192223` "A Beginner's Guide" (SyanL, 2017-11-09)

12 UUID-named images plus the two community-source citations in
`training-public-evidence.md` / `training-rankup-rules.md` that previously
"timed out". Body now read (§1.7); images unreachable. Useful only because its
body resolves two of those citations.

### Rank 8 — `197745` "Guide to Blustone" (Alaiko, 2017-11-12)

The prior pass's recommended target. Now **fully characterised**: 11 images,
subjects known from `alt` (`Training Gym.png`, `Arena.png`, `Fight Club.png`,
`Ruins.png`, `Cruising.png`), all unretrievable. Its **19,072-character body is
already fully extracted** and is the best single prose source for the
transcendence matrix and the fuel/dispatch rules. **The next lane should treat
`197745` as a text source that is already mined, not an image target.**

### Rank 9 — non-`share_en` follow-on: `vsfan.net` wiki HTML

`199711` hotlinks 54 `vsfan.net/wiki/images/…` assets. That is the **community
wiki**, a different domain with its own archive coverage, and its *item/hunter
pages* — not its icons — are the natural next corpus. `archived-hunter-database-2019.md`
already harvested the Japanese `blustone.jp/hunter` database; the English
`vsfan.net` wiki is a parallel, unmined source. **This is the best surviving
lead from this lane** and it is out of scope for `bs.visualshower.com`.

### Rank 10 — the board's text-only tail

The 82 text-only posts are individually exhausted (§1.5 and the body scan in
§2.1). Two are worth a *non-visual* follow-up if economy is in scope:
`395828` "Secrets a Top PvP player won't let you know" (Nishino, 6,081 chars,
the longest text-only post and only partially quoted here) and
`173620` "[Guide] Your first week in Blustone" (3,166 chars). Both are already
retrieved locally and cost no further fetch.

---

## 4. Negative results preserved

| Target | Check | Result |
|---|---|---|
| Any HP / ATK / DEF numeral in any of the 105 post bodies | two regex scans over 166,838 chars | **Zero.** 24 posts match on stat *words* in prose, none with a value. |
| Any stat panel / hero detail screen / gear row / jewel row | 105 bodies | **Zero.** The board is prose advice; 82 posts have no image at all. |
| `565` attachment bytes (any of 123 files) | 2 whole-namespace CDX sweeps + 1 dedicated prefix sweep + 4 exact-URL CDX + 5 direct `im_` fetches + 2 wildcard-timestamp fetches | **404 ×3, `000` ×2, and zero CDX rows.** Control `75605` returns 200/58,647 bytes. **Hard negative.** |
| `567` attachment bytes (5 files, posts `55626`/`55641`) | prefix sweep | **Zero rows.** |
| `565/745/197` — the prior pass's specific untested lead | prefix sweep + direct fetch | **Zero rows, 404.** Resolves `review-posts-2026-10-05.md` §4's "Untested" row as a negative. |
| `share_en` board enumeration | CDX + 9 list pages + 105 body fetches | **Complete for the archived corpus: 105/105 ids, 105/105 titles, 105/105 dates, 105/105 authors, 105/105 bodies at HTTP 200.** |
| Board-level completeness | list pages 1–9 only | **Still unknown.** Board ran past post #94 and past 2018-04-08. |
| `42865` "Character's stats info" — the only stats-titled post | body read | **289 chars, text-only, no values.** Dead end, closed cheaply. |
| `507556` tier list image | direct fetch | Unretrievable (§1.4). |
| `215324` before/after transcendence stat panel | inferred from body prose, not pixels | Unretrievable. Documented as the pass's most concrete loss. |
| `vsfan.net` wiki **icons** hotlinked by `199711` | structural | 30–86 px thumbnails — structurally incapable of a stat panel, and a different domain. Not pursued. |

---

## 5. Coverage disposition / files updated

- **New base-stat tuples: 0.** Hero **1/113 (0.9%)**, accessories **1/100**,
  monsters **0/22** — all unchanged.
- **No coverage inflation.** §2.2's economy tables are quarantined from the
  stat ledgers. §1.4's image subjects are `alt`-based and explicitly labelled;
  none is in §1 as a pixel reading.
- **`polluted-observations.md` gains a pointer subsection only** — the identity
  and threshold tokens in §2.5 are named but not numeric stat rows, so there is
  nothing to duplicate numerically.
- **Era:** 100% of the corpus is **pre-2019-09-05** (§2.6) and must be read
  under that era's balance per `stat-version-context.md`.
- **Files written:** this file (new); `polluted-observations.md` (pointer
  subsection appended). `coverage.md`, `README.md`, `coverage.tsv`, the archive
  TSVs, `server-ts`, the APK and all seeds are **untouched**. **No server/APK/
  state change, no emulator or phone contact, no Ghidra run, no native library
  read, no archive write, no re-upload, no login, no form submission.** All
  fetches were GET-only reads of `web.archive.org`.