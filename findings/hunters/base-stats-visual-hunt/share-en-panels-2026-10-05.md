# `share_en` board sweep — 105 post bodies recovered, OFFICIAL Transcendence table, all 21 image namespaces dead (2026-10-05)

**Lane:** the untouched `share_en` corpus named as "still 105 ids / 833 CDX rows, never
enumerated" in
[`share-en-guide-2026-10-05.md`](share-en-guide-2026-10-05.md) §3, plus its
`review-posts-2026-10-05.md` §1.6-1.7 method notes.

---

## 0. HEADLINE — read this before the tables

**Zero new base-stat tuples. Hero stays 1/113 (0.9%), accessories 1/100 (1.0%),
monsters 0/22 (0%).**

**Of 21 attachment namespaces tested across all 12 image-bearing `share_en` posts,
every one is dead: 0 images with pixels.** That is now proven with a positive control
that passes *in the same session as every zero* (§1.1), which is exactly the
requirement `share-en-guide-2026-10-05.md` §2.2 set up and which the earlier passes
did not fully honour.

**But the bodies are not empty, and this lane recovered four things the earlier
`share_en` pass did not:**

| # | Finding | Confidence | Where |
|---|---|---|---|
| **A** | **The OFFICIAL VisualShower Transcendence cost table, all 9 cells, as a real HTML table** in a developer-authored post — and it agrees cell-for-cell with the *player-reported* table already recorded in `share-en-guide-2026-10-05.md` §1.5. Nine independent corroborations of a table that previously had one source. | **[VENDOR-AUTHORED]**, cross-checked against 1 independent player source + 2 partial | §1.6.1 |
| **B** | **A five-source EXP-to-max-level ladder `200 / 400 / 1200 / 4800 / 24000`, with the multiplier rule now written out** (`×(n+1)`: `200→400→1200→4800→24000`), and its cruise-cost corollary `19 / 37 / 110 / 437 / 2182` runs at 11 exp per 6 fuel. This **contradicts the replica's current fixture** of cumulative XP `100*(level-1)`. | **[MULTI-SOURCE, 5 authors]** | §1.6.2, §1.6.11 |
| **C** | **A developer statement about a native UI affordance.** `VSpang` replies in `42865`: the training screen's full-stat panel is revealed by **swiping up**, and was deliberately under-exposed because "there is a slight glitch when viewing the stats". | **[VENDOR-AUTHORED]** | §1.6.3 |
| **D** | A **36 KB live community stat glossary/FAQ** recovered through the Google-Doc link in post `440600`, containing the game's **complete 13-stat vocabulary**, the Awakening cost ladder, and the equipment/jewel slot structure. | **[PLAYER-REPORTED, LIVE, spans 2018→2026]** | §1.6.4 |
| **E** | A **second, independently authored full copy of the skill-level cost table** in `138442`, with the **carat tiers resolved** (`1 carat` = bronze, `2` = silver, `3` = gold) and **eleven community icon names crosswalked to game material names** — including `So?shell` = **`Unscathed Shell`**. | **[MULTI-SOURCE]** | §1.6.11 |

Plus a derived 1★→5★ fodder/rupee ladder (§1.6.5) that **two independent authors
agree on to the figure 120**, and a genuine **source-conflict register** (§2.1) that
this project has never had for this board.

**New corpora found but not mined** (§5): the `forum_en` board (**131 distinct post
ids** in a single prefix query, control-verified) and two dead `/share_en/1494773` +
`/en/849114` ids surfaced by the FAQ.

---

# 1. PURE — verbatim readings, exact ledger, pixels actually decoded

Nothing in §1.6 is a *base-stat* reading except §1.7, and §1.7 yields **no new**
tuple. §1.6 is **post-body text**, transcribed verbatim, and is labelled as such
throughout. §1.7 is the only section containing decoded pixels.

## 1.1 The positive-control gate — and why it had to be re-run four times

`share-en-guide-2026-10-05.md` §2.2 records the method trap: *a rewritten `img src` is
not evidence bytes exist*. §1.3 of that file also records the correct discriminator —
a **CDX row** — and then notes a CDX row "still needs a positive control before its
absence means anything".

This lane made that a **hard gate**, not a formality: every fetch harness here runs a
known-downloadable control **first** and **aborts** if the control does not return
decodable pixels. It fired once, for real:

```
$ fetchq.ps1 -QueueFile queue2.tsv -OutDir get2 ...
Out-File : Could not find a part of the path '...\get2\_ledger.tsv'
=== POSITIVE CONTROL: code=200 size=0 sig=-- tries=1 -> FAIL ===
CONTROL FAILED - zeros would be uninterpretable. ABORT.
```

The control failed because the output directory did not exist. **The abort was
correct** — with a broken harness, every "404" in that batch would have been
meaningless. The directory was created and the batch re-run from scratch.

**Control definition, used unchanged in every batch:**

```
http://web.archive.org/web/2021/https://bs.visualshower.com/files/attach/images/75605/303/534/001/725a8e175454a533e96dac68fc5fdb49.jpg
```

**Every control result this lane, all four PASS:**

| Batch | Control HTTP | Bytes | Signature | Verdict |
|---|---|---|---|---|
| CDX positive control (§1.2) | 200 | 4 JSON rows | — | **PASS** |
| queue1 — 22 post bodies | 200 | 57,414 | `ffd8ffe1` | **PASS** |
| queue2 — 13 images | 200 | 57,414 | `ffd8ffe1` | **PASS** |
| queue3 — docs + `forum_en` CDX | 200 | 57,414 | `ffd8ffe1` | **PASS** |
| queue6 — 31 post bodies + 2 leads | 200 | 57,414 | `ffd8ffe1` | **PASS** |
| queue5/7 — Google Doc exports | 200 | 57,414 | `ffd8ffe1` | **PASS** |

`ffd8ffe1` is a JPEG SOI + APP0 marker: **real pixels, not an error page.**

**The archive is heavily rate-limited and this materially affects method.** Transport
failures (`curl` exit / HTTP `000`) were routine — the *same* control URL needed **5
consecutive attempts** to succeed once. Two consequences, both load-bearing:

1. **HTTP `000` is never a result.** Every `000` here was retried (up to 10 tries with
   growing backoff). Any zero in this file that is reported as `404` was an *actual
   HTTP 404 response*, not a transport failure.
2. **`matchType=domain` + `filter=` queries are unusable at this reliability.** They
   timed out at 21 s repeatedly. `matchType=prefix` queries succeed, so all index
   queries here use prefix form. This is a correction to
   `share-en-guide-2026-10-05.md` §1.3, whose control used the domain form — that
   control is sound as a *statement about index content* but is not reproducible here.

## 1.2 CDX positive control, index form — `75605/303/` returns 4 rows

Same method as the prior lane's control, but in the cheaper prefix form:

```
$ .../cdx/search/cdx?url=bs.visualshower.com%2Ffiles%2Fattach%2Fimages%2F75605%2F303%2F&matchType=prefix&output=json&limit=800

20210903030305 .../75605/303/534/001/725a8e175454a533e96dac68fc5fdb49.jpg  200 image/jpeg 58647
20210903030326 .../75605/303/534/001/7e951164fd7e45dbfc5d2b33b106fddc.jpg  200 image/jpeg 116003
20210903030226 .../75605/303/534/001/8356e1c4a5f7f7388d7c24f04ba0108f.jpg  200 image/jpeg 58477
20210903030212 .../75605/303/534/001/f9a04919d2f82addf089a6f98a9d1c28.jpg  200 image/jpeg 237347
```

This reproduces **exactly** the four rows printed in
`share-en-guide-2026-10-05.md` §1.3, in the same order. **Index-query method
validated.**

## 1.3 Namespace sweep — 21 attachment namespaces, all dead

Index form (`matchType=prefix`, all statuses), then direct byte fetch of one
representative file per namespace via the nearest-capture form
`web/2018/<original-url>` — which is *form-independent*, so a 404 there means "no
capture of that exact URL at any timestamp", not "wrong timestamp".

| # | Namespace | Post(s) using it | Index rows | Byte fetch | Bytes | Signature |
|---|---|---|---|---|---|---|
| 1 | `565/` (whole prefix) | all | **0** | – | – | – |
| 2 | `567/` (whole prefix) | all | **0** | – | – | – |
| 3 | `565/324/215/` | `215324` Lana Ch.8 | **0** | **404** | 4,730 | `3c21444f` |
| 4 | `565/417/096/` | `96417` | **0** | **404** | 4,730 | `3c21444f` |
| 5 | `565/526/127/` | `127526` | **0** | **404** | 4,730 | `3c21444f` |
| 6 | `565/607/055/` | `55607` Lana Ch.1 | **0** | **404** | 4,730 | `3c21444f` |
| 7 | `565/613/055/` | `55613` Lana Ch.2 | **0** | **404** (after 8 tries) | 4,730 | `3c21444f` |
| 8 | `565/618/055/` | `55618` Lana Ch.3 | **0** | **404** | 4,730 | `3c21444f` |
| 9 | `565/626/055/` | `55626` Lana Ch.4 | **0** | **404** | 4,730 | `3c21444f` |
| 10 | `565/628/095/` | `95628` | **0** | **404** | 4,730 | `3c21444f` |
| 11 | `565/641/055/` | `55641` Lana Ch.5 | **0** | **404** | 4,730 | `3c21444f` |
| 12 | `565/672/055/` | `55672` Lana Ch.6 | **0** | **404** | 4,730 | `3c21444f` |
| 13 | `565/691/055/` | `55691` Lana Ch.7 | **0** | **404** | 4,730 | `3c21444f` |
| 14 | `565/711/199/` | `199711` | **0** | **404** | 4,730 | `3c21444f` |
| 15 | `565/745/197/` | `197745` (prior lane's 11) | **0** | **404** | 4,730 | `3c21444f` |
| 16 | `565/785/100/` | `100785` | **0** | **404** | 4,730 | `3c21444f` |
| 17 | `565/982/330/` | `330982` | **0** | **404** | 4,730 | `3c21444f` |
| 18 | `565/134/197/` | `197134` (**new, found this pass**) | – | **404** ×3 | 4,731 | `3c21444f` |
| 19 | `567/029/019/` | `55626` | **0** | **404** | 4,730 | `3c21444f` |
| 20 | `567/046/019/` | `55641` | **0** | **404** | 4,730 | `3c21444f` |
| 21 | `567/943/018/` | `55626` | **0** | **404** | 4,730 | `3c21444f` |

**Totals: 21 namespaces probed at index level, 19 of them also byte-fetched,
31 individual image files fetched. Every one returned HTTP 404.** The remaining 12
individual files beyond the one-representative-per-namespace sweep, all in namespaces
already shown dead above:

| Namespace | Files fetched (all 404) |
|---|---|
| `565/134/197/` | `07e1a683….jpeg`, `b3331ec7….jpeg`, `b3b55d25….jpeg` (**all 3** — namespace found this pass) |
| `565/607/055/` | `55c804d0….jpg`, `7cc77ce9….jpg` |
| `565/641/055/` | `ad77885e….jpg`, `bee2b5f1….jpg`, `c20ec959….jpg` (**all 4**, namespace fully covered) |
| `565/324/215/` | `b9bddbea….jpg` (**`transc.jpg`**), `3365176c….PNG` (**`trans2.PNG`**), `dd439829…..PNG` (**`di1.PNG`**), `f665e07c….PNG` (**`di3.PNG`**) |

The four `565/324/215/` files are named in the body of §1.6.1 and are **exactly the
screenshots that would have shown the Transcendence panel's "all her statistics have
increased" before/after values.** Their loss is the single most consequential image
loss in this lane, and it is why §1.6.1 has no numeral for a stat increase.

**Every non-pixel response is byte-identical**: 4,730 or 4,731 bytes, signature
`3c21444f` = `<!DO` — the archive's own "not archived" page. **No PNG (`89504e47`),
JPEG (`ffd8ff`) or GIF (`47494638`) signature appears in any of them.**

**Corrects `review-posts-2026-10-05.md` §2.3, partially.** That file states the `565`
prefix appeared **27 times** in a broad domain sweep "via `procFileDownload&module_srl=…`".
This lane found **zero rows at `/files/attach/images/565/`** and zero rows at
`index.php?module=file`. One `procFileDownload` URL was fetched directly and returned
a genuine **HTTP 404** (4,720 bytes, `3c21444f`). The `procFileDownload` CDX prefix
test here is **not conclusive** on its own — CDX sorts query parameters alphabetically,
so a prefix on `index.php?module=file` cannot match a urlkey beginning
`index.php?act=…`. That query is recorded as **INCONCLUSIVE**, not as a refutation.
The decisive evidence is the 21 direct 404s on the canonical `/files/attach/images/`
form, which is what an archiver would have captured.

**Conclusion: `share_en` screenshots are unrecoverable from the Wayback Machine.
This generalises `share-en-guide-2026-10-05.md`'s finding from one post's 11 images to
all 12 image-bearing posts on the board, and closes the lead.**

## 1.4 Board census — recovered from the archived list pages

`share_en` has 105 distinct post ids with archived bodies. The board's own pagination
recovers **titles for 57** of them. Rows 1–37 and 76–94 of the board listing are
present; **rows 17 and 38–75 have no captured list page** and their titles are
[UNKNOWN]. Post bodies exist for all 105 ids.

**The 12 image-bearing posts — every one dead per §1.3:**

| Id | Title | Author | Date | Views | Imgs in body |
|---|---|---|---|---|---|
| 55607 | Lana's Guidebook Ch. 1: Put Your Back into It! Using Your Skills | VSpang | 2017.06.05 | 20,456 | 3 |
| 55613 | Lana's Guidebook Ch. 2: Don't Crash and Burn! Watching the Fuel Meter | VSpang | 2017.06.05 | 1,377 | 3 |
| 55618 | Lana's Guidebook Ch. 3: There's No I in Team. About Hunter Roles | VSpang | 2017.06.05 | 2,101 | 5 |
| 55626 | Lana's Guidebook Ch. 4: Rock, Paper, Scissors! Understanding Elemental Attributes | VSpang | 2017.06.05 | 2,542 | 8 |
| 55641 | Lana's Guidebook Ch. 5: Harder, Better, Faster, Stronger! Advancing your Hunter | VSpang | 2017.06.05 | 3,231 | 5 |
| 55672 | Lana's Guidebook Ch. 6: Where in the World is...? Using Hunter Traces | VSpang | 2017.06.05 | 1,903 | 6 |
| 55691 | Lana's Guidebook Ch. 7: I Wanna Be the Very Best! Climbing Up your Veteran Status | VSpang | 2017.06.05 | 3,541 | 4 |
| 197134 | Casual's Guide to Character Ranking | Renjixfen | 2017.11.11 | 606 | 3 |
| 197745 | Guide to Blustone (prior lane) | Alaiko | 2017.11.12 | 2,048 | 11 |
| 199711 | A Glorious Guide on [How not to be a n00b] [OUTDATED for Patch 1.2.0] | WinJ | 2017.11.12 | 1,300 | 67 |
| 330982 | List of Blustone FanArts | BlackGeneral | 2018.01.31 | 405 | 6 (one .gif) |
| 507556 | Hunter Tier List as of 02.08.2018 | FatherVinh | 2018.03.09 | 215 | 1 |

Plus `215324` **Lana's Guidebook Ch. 8: Transcendence Gives You Wings~! How to
Transcend Your Hunter** (VSpang, 2017.11.21, 6 images, `565/324/215/`, dead) — the
list page does not flag it as image-bearing, but its body does. **13 posts carry
images; 0 survive.**

`199711`'s 67 `<img>` tags are **mostly not Blustone screenshots at all** — 39 are
`vsfan.net` wiki icons and `cursecdn` gifs hotlinked into a community guide. Only 8
are `bs.visualshower.com` attachments (`565/711/199/`), all dead.

## 1.5 Bodies read — coverage

**105 ids in the archive; 105 post bodies fetched or recovered; titles known for 78
after this lane's completion batch** (§5 L8). 62 bodies were already on disk from an
interrupted earlier pass and were re-read in full; **43 were fetched fresh** here (22
in the priority batch, 31 in the completion batch, with overlap). Every numeral below
is from a body that returned **HTTP 200 with HTML**. The only two targets in the whole
lane that returned **404** are the two ids the FAQ cites but that are not archived
(§3).

## 1.6 The recoveries — verbatim, per source

Era tags are applied throughout; see §2.5 for the tag definitions and §2.5.3 for the
one document that spans eras.

### 1.6.1 ★ The OFFICIAL Transcendence cost table — post `215324`

**Author `VSpang`, the game's own forum account, dated `2017.11.21 16:49`.** The
title contains **8 chapters** by `VSpang` and one sticky *official* board; the
signature-free body is written as in-game dialogue by Lana. **This is a vendor-authored
document, not a player report.**

Body text, verbatim (the star glyph does not survive the archived encoding and
renders as `?`; everything else is the author's own):

> Welcome to the latest chapter of my guide, Captain!
> This time, it's about upgrading your hunters, not by advancement or training, but by transcendence!
> What is transcendence exactly? Well, have you ever had one or more of the same hunter in your dormitory? Don't throw the duplicates away, because you can fuse two of the same hunters to transcend them, making the hunter stronger!
> You can transcend your hunter when they are an Experienced hunter (3?). Let's bring in Diana as an example!
> […]
> Ta-da! Diana is transcended! And as you can see, all her statistics have increased. What's more, she's got a little wing next to her frame to show that she has been transcended once. **Diana will have to get to 4? to get to her second transcendence.**
>
> In summary of the 3 levels of transcendence:
> For the 1st transcendence: 3? base hunter, 1 3? duplicate hunter, and additional materials
> 2nd transcendence: 4? base hunter, 2 3? duplicate hunters, and additional materials
> 3rd transcendence: 5? base hunter, 3 3? duplicate hunters, and additional materials

And the table, which in the archived body is a **real HTML `<table>`** (row/cell
boundaries preserved here as `|`, exactly as rendered):

```
1? Base Hunter
Transcendence | Metron Crystals | Metron Fragments | Rupees    | Duplicate Hunters
1st           | 5               | 50               | 5,000     | 1
2nd           | 15              | 150              | 15,000    | 2
3rd           | 45              | 450              | 45,000    | 3

2? Base Hunter
Transcendence | Metron Crystals | Metron Fragments | Rupees    | Duplicate Hunters
1st           | 7               | 70               | 7,000     | 1
2nd           | 25              | 250              | 25,000    | 2
3rd           | 60              | 600              | 60,000    | 3

3? Base Hunter
Transcendence | Metron Crystals | Metron Fragments | Rupees    | Duplicate Hunters
1st           | 9               | 90               | 9,000     | 1
2nd           | 30              | 300              | 30,000    | 2
3rd           | 80              | 800              | 80,000    | 3
```

And, verbatim, the grade-independence statement:

> Another commonly asked question is, does the effectiveness of transcendence change if
> you're a 3?, 4?, or 5? hunter? **The answer is no! Transcendence gives you the same
> amount of stat bonuses no matter what your Hunter Grade is.**

**This independently corroborates all nine cells** of the *player-reported* table
already recorded in `share-en-guide-2026-10-05.md` §1.5 — a different author, a
different date (2017-11-21 vs 2017-11-12), a different document class (vendor guide vs
player guide), and a different format (HTML table vs prose). Every value matches:
crystals `5/15/45`, `7/25/60`, `9/30/80`; fragments exactly 10×; rupees exactly
1000×; duplicates `1/2/3`. **The geometric structure noted as suspicious in that
file's §2.1 is now confirmed by the publisher itself**, so it is not a player
invention.

Two **new** facts not in that file:
- Transcendence's stat bonus is **grade-independent** (verbatim above) — a structural
  rule, not a number.
- The in-game affordance: a **wing icon next to the card frame** marks a hunter as
  transcended **once**.

### 1.6.2 ★ EXP-to-max-level ladder — four independent authors

**`199711` — WinJ, 2017-11-12 16:32, "Guide Updated for VER. 1191".** Rendered as a
table in the archived body:

```
n th Star | Required Exp to Max Level | Amount of Lvl 40 Cruises Required | Fuel Required
1 Star    | 200 Exp                    | 18.18 ? 19                        | 114
2 Stars   | 400 Exp                    | 36.36 ? 37                        | 222
3 Stars   | 1200 Exp                   | 109.09 ? 110                      | 660
4 Star    | 4800 Exp                   | 436.36 ? 437                      | 2622
5 Stars   | 24000 Exp                  | 2181.81 ? 2182                    | 13080
```

Preceding it, verbatim:

> Levels 36 - 40 give 11 exp per 6 Fuel (or 1.83 exp/fuel)

**`189046` — shvrkboy, 2017-11-08 23:32, "Just the tips [Beginner Guide]".**
Author states level 60+ and a top-50 arena rank, and gives only the grades it
considers relevant:

> EXP:
> 1-Star requires 200 EXP
> 2-Star requires 400 EXP
> 3-Star requires 1200 EXP
> EXP for 4 and 5-stars don't really matter for beginner levels
> because you don't really think about grinding exp for them.

**`201598` — Enheim, 2017-11-13 12:00, "Enheim's guide for beginners".** Gives four
grades and the sacrifice cost per grade:

> 1-Star - 200 exp , req to advance - 1x 1-Star hunter sacrifice
> 2-Star - 400 exp, req to advance - 2x 2-Star hunter sacrifice
> 3-Star - 1200 exp, req to advance - 3x 3-Star hunter sacrifice
> 4-Star - 4800 exp, req to advance - 4x 4-Star hunter sacrifice
> Notice I stopped at 4-star advancement, even though there's a 5-star tier, that's because a character is capped out at 5-star, there's no 6-star here.

and the cruise corollary:

> the best stages to farm for exp that is fuel efficient would be staged 36-39, where each stage yields 11 exp for 6 fuel. So **19 runs for 1-star, and 37 runs for 2-star** to be brought to max level.

**`197134` — Renjixfen, 2017-11-11, "Casual's Guide to Character Ranking".** Third
independent statement of the same run counts, plus a commenter confirming them a
second time:

> For Rank 1 units, **19 runs** in the Level 36-39 range is perfect to get all of them to Max Level and be ready to rank up to 2. After that, it takes **37 runs** to get the Rank 2 units to Max Level. Then, even after that it takes **110 runs** to get the Rank 3 up to Rank 4

Comment `Lgtmagician`, 2017-11-13 01:21:

> if want to max a unit, 1 2 3*, farming stage 36 to 39, need respectively **19 37 110** that many times, farming at these stages is fuel cost effective and efficient.

**So `19 / 37 / 110` is stated by three authors plus one commenter in four separate
posts, and `200 / 400 / 1200` by three.** The ratio is `1 : 2 : 6`; extended by
`199711` alone to `4800` and `24000`, making the full ratio `1 : 2 : 6 : 24 : 120`.

**Internal consistency check, done here rather than assumed:** 19 × 11 = 209 ≥ 200;
37 × 11 = 407 ≥ 400; 110 × 11 = 1210 ≥ 1200; 437 × 11 = 4807 ≥ 4800;
2182 × 11 = 24002 ≥ 24000. Fuel column = runs × 6 exactly (114, 222, 660, 2622,
13080). **The table is arithmetically self-consistent in all 15 cells.**

> **Direct consequence for the replica, flagged NOT acted on.** The server's
> documented character-EXP fixture is cumulative `100*(level-1)` with source XP
> `100*level` (`server-ts` skill/character XP, per `AGENTS.md` §19 and §24). That
> fixture makes **XP 100 ⇒ LV2**, which these four authors contradict: the community
> ladder says a 1★ hunter needs **200** total EXP to max. **This subagent made no
> server, fixture or test change.** Adopting any part of §1.6 is a separate,
> separately-reviewed decision, and the discrepancy is recorded here so it is not
> discovered later as a surprise.

### 1.6.3 ★ Vendor statement about the native full-stat panel — post `42865`

`42865` "Character's stats info", McAroni, 2017-05-31. Whole body, verbatim:

> Just sharing a "discovery" i just made. (Might probably already know this)
> When viewing a character's attributes via the training screen, **swipe up to show all
> of his/her stats (HP-defense-attack-speed…)**
> Now to reassure myself, I'm not the only one that didn't know that was there, right?

**The first reply is from `VSpang`, 2017.05.31 18:23 — the vendor's own account.
Verbatim:**

> Hi there, we were purposely not making this feature too obvious because there is a
> slight glitch when viewing the stats. We will make sure to make this feature more
> obvious once we've worked out the kinks in this feature.

This is a **[VENDOR-AUTHORED]** statement that (a) the training screen's full stat
list is a **swipe-up gesture** on an existing panel, and (b) the vendor knew it was
glitchy and under-exposed in 2017. It is the **only first-party confirmation of a
specific native UI affordance recovered anywhere in this project's visual lanes**, and
it independently corroborates that a full 13-stat line exists on that screen — which is
what makes §1.7's reading legitimate rather than assumed.

### 1.6.4 ★ Live community stat glossary — post `440600` → Google Doc

`440600` "FAQ for learners/semi experienced", Nishino, **2018-02-26**, is a two-line
post whose entire content is a link:

> https://docs.google.com/document/d/1O_xdOZqplSVw2XczV2nEl2_wvEZaOc_Mm9RFIY2qaXc/edit?usp=sharing
> I was originally going to share it with my Discord group only, but you guys could
> probably benefit from using it too. Have fun.

**This link is LIVE.** The `edit?usp=sharing` page returns 546,370 bytes of Google
Docs viewer boilerplate with no content; the `export?format=txt` endpoint returns
**36,493 bytes of real text**, and `export?format=html` returns **31,038,481 bytes
with 28 embedded base64 images** (§1.7). The document's own footer reads:

> This guide was last edited: 21 / 09 / 2026 (04:51 am GMT-5 Mexico time zone)

**So this document spans 2018 → 2026 and must NOT be read as a single era.** Its
content is split in §2.5.3. Selected verbatim recoveries:

**The game's complete stat vocabulary.** Verbatim glossary entries, trimmed only at
the examples:

> **Combined Power:** A synonym of Total Power/Combat Power/CP/TP, it directly links
> the strength of your units to the amount of gathered Attack, Defensive power, and
> Health, along with other sub-stats and modifiers (Transcendence, equipment, fates,
> jewels, collection bonus.)
>
> **Block Chance:** Stat used widely to negate most of the critical damage done by
> units. It also greatly weakens the performance of special attacks of Attackers and
> Bombers, as it lowers the maximum normal and critical damage hits.
>
> **Block Resistance:** […] It's effectiveness is linked to block chance; it also
> affects special attacks.
>
> **Critical Damage:** Stat which greatly increases the maximum damage done and
> received by auto attacks and special movements, but that can be easily negated by
> increasing the block chance/resistance stat of a unit. **Currently the most relevant
> offensive trait in the game.**
>
> **Enrage:** The rate at which special movement bar fills up, some units can greatly
> increase it, while others can slow it. Example of adders: Celine, Captain. Example of
> removers: Vincent, Lottery Mouse.
>
> **Snare:** […] Makes your base speed 0 during the special attack duration and greatly
> reduces the damage of a special movement. Not to be confused with Stun, as Snare
> still allows for character's swapping
>
> **Stun:** […] Makes the unit become unable to attack or swap out […]
>
> **Attacker:** Unit with high speed, high attack, but low hit points and defence.

Note **Enrage** is the community's name for the SP/Rage gauge, and this glossary
names **adder/remover** units — directly relevant to the replica's `maxSP`/group-SP
model in `AGENTS.md` §35.

**Transcendence effect size and stat linkage:**

> Does Transcendence affect skill stats and effects?
> Yes. It does, by a high amount (**An estimated 7% boost per tier**)
> **The higher your Attack Power (AP), the higher an attacker / bomber's special move
> point cap can be. The higher your Defensive Power (DP), the higher the degree of
> regeneration / healing will be.**

**Awakening cost ladder (complete):**

> (A1=30 crystals + 30k rupees, A2=50 + 100k, A3=100 + 150k, for a total of **180
> crystals and 280k rupees**, + **9 hearts** per fully made unit)

**Equipment and jewel structure:**

> It's a feature first unlocked when a hunter reaches the **Proficient Hunter degree
> (4 stars)**. […] It's divided in 3 pieces: *Weapons will augment your Attack Power […]
> Armor will augment your Defensive Power […] Accessories will augment your Life
> Points.*
>
> The special element modificators (Coolants, Flammable materials, Lightning boxes) are
> used every time you get an equipment piece to **levels 10, 20, 30 and 40**
>
> **Modification materials are available when you clear stage 3, 6, 9 in Mirage Ruins.**
>
> **Equipment comes with 1 slot by default. Upon reaching level 20, an equipment gains
> an additional jewel slot.**
> - Jewels can be detached and have their own unique abilities […]
> - Jewels are classified into **five classes**. The higher the class, the more power it
> has. - The class of Jewels is determined at the time of acquisition, and the class
> itself cannot be changed.

This block is explicitly attributed: **"Stated by VisualShower's / Blustone's
moderators."** — i.e. first-party relayed through a player document.

**Other numerals:**

> All 4* characters can be guaranteed to be recruited on their banners after **16
> pulls (4,800 manda)**
>
> When you do a **10 gems pull (250 manda cost)**, all the gems that you get will be
> focused on the skill set you picked for them. (**You can get up to 300 in total**
> before having to start selling them)
>
> […] the higher the level a gem is, the higher the chance to fail refining it will be
> […][b]e sure to count with lots of resources before attempting to do so, at least
> **600k rupees**)
>
> Contributions are made through participation in the Fight Club (**each win
> guarantees you 300 points, while defeats are 250**) or by using your Guild Cooperative
> partners on ruins / searches (**Roughly 75 points** each).
>
> Some of these guilds will also ask for a certain score in the Fight Club […] **This
> score can range from 0 up to 4,000 points.**

**A live confirmation of this project's own item finding:**

> As of **April 1st 2019**, you can only receive traces + metron fragments only. All
> other rewards stopped being given […] Plus they **do not use fuel, but instead,
> Helium Capsules.**

This matches the replica's `AIRSHIP_TICKET` = "helium capsule" conclusion
(`AGENTS.md` §72), reached independently. `AIRSHIP_TICKET` is corroborated as the
original in-game name of the Search currency.

**And the level-ending-digit material drop rule — an independent second confirmation
of Alaiko's 2017 rule** (`share-en-guide-2026-10-05.md` §1.5):

> Those stages with a digit **6** are for Attacker materials.
> Those with a **7** are for Defenders materials.
> Those with **8** are for Bombers.
> Those with **9** are for Healers.
> Rupee tickets gather at any stage.

Alaiko (2017-11-12) wrote `1/6 → Offensives, 2/7 → Defenders, 3/8 → Bombers,
4/9 → Healers, 5/0 → none`. **Same rule, same digits, different author, eight years
apart.** Strong corroboration.

### 1.6.5 ★ The 1★→5★ fodder and rupee ladder

**`93837` — Silverberg, 2017-08-06, "The cost of making a five star hunter from a pile
of novices."** Whole body, verbatim:

> To start, making a single 2star needs 2x 1stars, one as promoted and one as
> sacrifice. On top of this, it costs 1k rupees.
> Making a 3 star, costs 3x 2stars. That's two sacrifice and one move up. 3\*2= 6
> 1star hunters spent, and 6k rupees - 3x 1k rupees from making the 2star, and 3k to
> promote a 2star to a 3star.
> Making a 4star needs three sacrifices - for a total of 4x 3stars. 24 hunters. 36k
> rupees. 4x 6k + the 12k promotion.
> And finally, the 5star. 5x 4stars. **24\*5= 120 hunters** on the chopping block, and
> one of these moves up and becomes a legend. I can't see what the promotion cost is,
> I'm too poor for that right now.
> (Word's out that the promotion cost is 60k. In this case, 5\*36 = 180k rupees, plus
> this 60k makes a total cost of **240k rupees**.)

**`189046` — shvrkboy, 2017-11-08** independently arrives at the same fodder count by
a different route:

> HOW MANY HUNTERS DOES IT TAKE TO GET TO A 5 STAR?
> In theory, it would require
> Five 4-star hunters
> Twenty 3-star hunters
> Sixty 2-star hunters
> **One-hundred twenty 1-star hunters**
> 205 hunters in total […]
> You would only be advancing 81 times, that's 81 hunters you're maxing out and feeding.
> The remaining 4 are the four vanilla 4-stars used for 5-advance.

**Both authors independently reach 120 one-star hunters as the base fodder count**
(Silverberg as `24×5`, shvrkboy as `1+2+6+12+24+48`… presented as "One-hundred
twenty"). Their totals differ (Silverberg counts the promoted one as inside the 120;
shvrkboy's 205 counts the whole tree), and §2.1 records the disagreement.

### 1.6.6 Advancement cost — five sources, and one dissenting value

| Source | Date | 1→2 | 2→3 | 3→4 | 4→5 |
|---|---|---|---|---|---|
| `24731` Kirinxd, *General item shops* | **2017.05.23** | 1,000 | 3,000 | 12,000 | **15,000** |
| `24901` HoZhihui, *Game guide and tips* | 2017.05.23 | 1k | 3k | 12k | 60k |
| `193383` UrielSR, *[Guide] Some tips for the Beginners* | 2017.11.10 | 1k | 3k | 12k | 60k |
| `189046` shvrkboy | 2017.11.08 | 1,000 | 3,000 | 12,000 | 60,000 |
| `201598` Enheim | 2017.11.13 | (sacrifice counts 1/2/3/4) | | | |

`24731` verbatim, and note it uses the **gem tier names**:

> Don't waste rupees to get challenge invitation, the recharge is only 2 time unlike fuel.
> Bronze to Silver cost 1000 rupees
> Silver to Gold cost 3000 rupees
> Gold to Green cost 12000 rupees
> **Green to Blue cost 15000 rupees**

The tier names are corroborated by `24901`, verbatim:

> There are different stars in game , 1 to 5 stars. […] 1 star ( brown) / 2 star (
> sliver) / 3 star ( gold) / 4 star ( green) / 5 star ( blue)

and by `22732` (Bond, 2017-05-22), which uses them conversationally: "I have a
**gold** character currently in my defense team […] use to make another character
**emerald**!" — so *emerald* is a fifth name for the green tier.

**4→5 is therefore contested: 60,000 in four sources, 15,000 in the earliest source.**
See §2.1.

### 1.6.7 Fuel, AP and shop economy

**`23265` — YukiJudai, 2017-05-22 (the earliest dated numeric source in this lane).**
Whole body verbatim — a five-item FAQ:

> 1. Purchase of fuel is **5000 for 1-2 and 3-6 cost 9000** so stock up fuel tickets
>    which cost **5000** for refills after 2(daily)
> 2. Challenger tickects give **2 more chances**
> 3. **Max level before advance is 20 which is 5 crystals \* 4 balls**
> 4. blue beats red / red beats yellow / yellow beats blue
> 5. Wonderland tylir is only obtainable by pre reg rewards currently. Sunny can only
>    be get by purchasing season 2 pass for white island (other game by same company
>    $8.99) currently

**`193383` — UrielSR, 2017-11-10:**

> you have a **limit of 60 units** of fuel […]
> Fuel is recharged though various methods: waiting, using a Fuel Ticket (which can be
> bought in the shop) or **using Gold (5k)**. Every time you use a tiket to recharge
> your Fuel or get Gold you may win the lottery and obtain **2x, 4x, 8x or 16x** bonus.

**`24901` — HoZhihui, 2017-05-23:**

> Shop items refreshes every **4 hours 12am, 4am , 8 am** […]
> **First two purchase per day is 5k each after that is 9k** and it will continue to
> increase..**fuel ticket is fixed at 5k** from the shop […]
> Recruitment Requests have a drop rate about **1 per 4-5 areas** cleared, but the Elite
> Recruitment Request is dropped about **once per 60 clears** and the Rupee Lottery
> Ticket is dropped **once per about 30 clears**.
>
> Arena shop: Refreshes on **0000 and 1200 hrs**. Manda can be used to refresh the shop
> . **first 2 times is 2 manda and next 2 times is 4 mandas.**

**`199711` — WinJ, 2017-11-12, VER. 1191**, verbatim price table:

> **Popups:** Only buy from the popups when it costs **5000/4000 Rupees**. NEVER USE
> MANDAS FOR THESE. (Note: The amount of rupees required increases by **3000 after
> every 3 purchases**)
>
> **Estelle's Hunter Shop** — Fuel Tickets **5 000 for 1**; Challenge Invitation
> Tickets **5 000 for 1**; Metron Fragment **1500 for 15**
>
> **Fight Club Shop** — Golden Hunter Traces (1st Priority) **150 for 2**; Metron
> Crystal (2nd Priority) **1000 for 1**; Golden Hunter Materials **75 for 3**
>
> **Everyday Supply Package** IDR59,000 = $4.99 → **1700 Fuel (200 + 150 Fuel Everyday
> for 15 Days)**, **20 Manda**, **550 Veteran Points**
>
> **Goal Achievement Package** IDR 349,000 = $25.99 → **3 Elite Requests**, **3 ?2
> Recruitment**, **1 ?3 Recruitment**, **340 Manda**

**`189046` — shvrkboy**, verbatim Manda/coin exchange rates:

> $1 - 10 Manda (Through Manda Tab)
> $1 - 1 Crystal
> 30000 Coins - 3 Crystals (Through Abyss Reset)
> $1 - 300 Fuel (Through Half-month Fuel Supply)
> **5000 Coins - 60 Fuel/1 Coupon** (Through first three fuel resets and coupons in shop)
> $1.50 - 1 Elite Scroll
> 30000 Coins - 1 Elite Scroll
> […]
> Abyss resets are **30 manda each**. TL:dr: Manda should only be used for Abyss
> resets and Dorm Expansion.
> […]
> The $100 training package gives you **15 metron crystals and 400 Manda**.
> 400 Manda is enough for **13 Abyss Resets which would get you 39 crystals** in any
> Area 5. 39 + 15 = 54
> However if you purchase $100 in manda, (**1100 manda**) you would be able to farm
> **108 crystals** through abyss resets. (30 manda per reset)
>
> […] **It takes 6 coin tickets to get 30000 coins.** […] One Elite Scroll = 6 Coin
> Tickets […] DO NOT SPEND COINS ON ELITE SCROLLS
>
> Fuel: Only purchase the 5000 daily fuel resets. […] **You can only buy up to three
> fuel recharges for 5000 coins. After that the recharge will increase to 8000** during
> the day.
>
> The shop also has challenge resets for **5000 coins**, however daily reset costs
> **4000 for first three purchases**.

Cross-check on that last figure: `199711` says popups cost "5000/4000" and
`189046` says 5000 coins normally but 4000 for the first three daily challenge
resets. **Consistent.**

### 1.6.8 ★ Dungeon → trace level mapping — post `69900`

`69900` "List of traces per dungeon", Nexor, **2017-06-22**. The **entire body** is a
mapping, transcribed verbatim:

```
Lapis- 1-10
Metis- 11-20
Bruce- 21-30
Sylvester- 31-40
Loke- 41-50
Hecate- 51-60
Balian- 61-70
Sienna- 71-80
Robin- 81-90
Denali- 91-100
Denali- 101-110
Gerard- 111-120
```

**Triangulated by three other posts, all independent:**
- `197134` Renjixfen: "the amount of **Sylvester** traces help exponentially […]
  based around these levels [36-39]"
- `199332` BonkersRabbid: "A good place to farm for sacrificial hunters would be
  **lvl 31-40** where you can get **Sylvester's traces**."
- `189046` shvrkboy: "**91-100** is great for rank 2 & 3 materials" (Denali's band per
  the table), and "I always run area **31-40** when grinding 1 star hunters."

**Four posts agree that levels 31–40 is the Sylvester band.** That is the single most
useful mapping in this lane, because it is the one the community repeats as the
fodder-farming optimum.

### 1.6.9 Elements, roles and mechanics — vendor + community agreement

**`55626` — VSpang, Lana's Guidebook Ch. 4 (vendor), verbatim:**

> The Hunter Union not only separates hunters by role but by elemental attributes as
> well. […] There are three elemental attributes in total. Fire / Ice / Lightning
>
> **Fire gains an offensive bonus when attacking Lightning.
> Lightning gains an offensive bonus when attacking Ice.
> Ice gains an offensive bonus when attacking Fire.**

**`55618` — VSpang, Ch. 3 (vendor)**, the four roles with their field/ship constraint,
verbatim:

> The Hunter Union analyzes Metron hunters' traits, attributes, and interests, then
> assigns **one of the four roles** of hunters.
> **Offense** — The role you can rely on to inflict a large amount of damage! […] They
> can only use their active skill **when out in the field**.
> **Defense** — […] They can only use their active skill **when out in the field**.
> **Bomber** — Has a stronger active skill than Offense. […] Their active skill can
> only be used **inside the ornithopter**.
> **Helper** — Has average stats. […] able to heal hunters. […] Their active skill can
> only be used **inside the ornithopter**.

**This is a first-party confirmation of the replica's role enum** (`AGENTS.md` §19:
roles 1 Offense, 2 Defense, 3 Bomber, 4 Support) — and of the **vendor's own term
being "Helper", not "Support"**. It also independently confirms the field/ship
restriction that the replica implements.

**`55607` — VSpang, Ch. 1 (vendor),** the Rage mechanic, verbatim:

> Build your **rage** by attacking your enemy or getting hit by your enemy...
> Then touch the skill icon above your head!
> **Remember, the required number of rage is written in the skill icon.**

**`55613` — VSpang, Ch. 2 (vendor),** the fuel meter, verbatim:

> If your battle lasts too long, the ornithopter must return to prevent crashing. […]
> **all your teams will return to Midgard, and the team member out in the fields are
> left to finish up the battle.** […] When the fuel meter goes down... **You can no
> longer change teammates!**

**`55672` — VSpang, Ch. 6 (vendor)**, traces; **`55691` — VSpang, Ch. 7 (vendor)**,
the complete Veteran-Status benefit list (verbatim, 11 items): *Fuel Purchase Limit;
Rupee Purchase Limit; Challenge Invitation Purchase Limit; Hunter Shop Renewal; Fight
Club Shop Renewal; Purchase Missed Supplies; Special Fuel Reward; Auto-Combat 10
Times; Auto-Combat 50 Times; Hidden Hunter.*

**Community corroboration of the SP cap — two independent posts:**

> `198374` ArkenDragon, 2017-11-12: "Middle Left - **Ability gauge (Max lvl is 10)**"
> […] "I recommend **reaching a gauge of 5.5** before anything. It allows ample time to
> react in case some enemy brings you down to **1/8 stamina**"
> `190286` PanicPac, 2017-11-09: "As you hit enemies, there is this counter that keeps
> rising till **'10'** that is something like your MP"

This matches the replica's runtime-measured `maxSP = 10` (`AGENTS.md` §35).

**`21817` — waldo_667, 2017-05-21,** the dots/stars distinction, verbatim:

> there are two measures for leveling up a character, **the stars and the dots**.
> Dots can be gained by either running missions or by sacrificing other characters on
> the train screen. You'll know that you are leveling dots on the train screen cause the
> button says **train, not advance**.
> Stars on the other hand, can only be gained by sacrificing characters with the same
> number of stats. So one 1\* character sacrificed to get to 2\*, two 2\* characters to
> get to 3\*.
> The characters you sacrifice just need to required stars, they dont need any dots,
> but the character you are upgrading needs full dots.

**`954` — Eisei, 2017-04-09 — skill NAMES for two catalog hunters.** Verbatim:

> Lets take **Sylvester**'s as an example, how does '**Attack Increase**' work? Does it
> increase the damage of '**Basic Combo**' itself or does it act as a buff for
> subsequent attacks?
> Another example would be **Sienna**, do skills such as '**Supporting Gunman**' and
> '**Weapons Expert**' activate after using '**Making a Beehive**' or are they passive
> abilities?

Four verbatim skill names attached to two named hunters, with slot ordering implied by
the question. `Sylvester` is catalog `006` (added by this project, §67).

### 1.6.10 Other dated numerics

| Post | Date | Verbatim numeral |
|---|---|---|
| `184960` OneShot | 2017.11.07 | "cumulative reward every **5, 10, 15 and 20 days**!( A **3\* scroll on day 20**! Yeahh!)" |
| `197134` Renjixfen | 2017.11.11 | "If I want him to make it to **5\*** it would cost me **119 Rank 1**"; "To get one single Rank 4 to Rank 5 is **96 Rank 1**, down from the 119/120. Which means only maxing **48 Rank 1**"; "you can check in **every six hours** for a run of **10** and then **9**. You can max **8 Rank 1** / Bronze in **12 hours**" |
| `194179` Taurus_Silver | 2017.11.10 | "(You can mass level **1\* Hunters from lvl 1 -30** once you get high enough)" |
| `96417` reese_y | 2017.08.10 | "**STAT BOOSTS** […] fighting along side with **Lantern** gives your team a **critical chance boost**? So its ideal to have him **close to the end** because once he's knocked out, you lose the boost." |
| `62649` Gareth | 2017.06.12 | "what being able to **Entrust 50 consecutive times** gets you at **Professional level 3**?" |
| `190985` lolislayer | 2017.11.09 | "the **metron selling rate (1000R)**" |
| `23201` HoZhihui | 2017.05.22 | "**1 carat metron** for the type of heroes are highly needed..**you need them to train from skill level 5 to 29**.therefore farming them at **stages 60 to 69** should be done" |
| `98323` reese_y | 2017.08.14 | "depending on what **scratch** you hear will determine the hunter rank. […] the more mellow scratches for the silvers and golds" (BGM encodes tier) |
| `94620` ninjakitteh | 2017.08.07 | "you have to actually **DRAG the hunter** you want to the **exit door**. Simply tapping them will not suffice." |
| `22732` Bond | 2017.05.22 | "a character in your arena team, both fighting and defense, **you can't use that character for advancement** of another character." |
| `401574` FletchGod | 2018.02.18 | 10+1 recruit sample: "**one 1 gold and 10 bronze and 2 silver**" / "**9 bronze and 1 gold 2 silver and 8 bronze**" vs one-at-a-time "**5 and 15 silver**" |
| `330982` BlackGeneral | 2018.01.31 | "People who complain about **Papillon 300% rate Up**"; "spenz **3000**?phercantage" |

### 1.6.11 ★ Post `138442` "Guide - Blustone" — the EXP multipliers, max level 30, and the full skill-cost table with material names

`138442`'s title was one of the 21 recovered only in this lane's completion batch
(§5 L8), so its content was previously unmined. It is a rewrite of HoZhihui's
`24901` with substantial additions. Verbatim, the parts that are new:

**The EXP ladder, fifth independent source, now with the multipliers written in:**

> Experience needed for max level for different stars
> 1? 200
> 2? 400 (1?x2)
> 3? 1200 (2?x3)
> 4? 4800 (3?x4)
> 5? 24000 (4?x5)

**This resolves the multiplier pattern §1.6.2 could only tabulate.** The step is
`×(n+1)`: `200 → 400 → 1200 → 4800 → 24000` is `×2, ×3, ×4, ×5` on the previous grade.
Derived here, checked against all five published values — exact. So the ladder is a
closed geometric rule, not four independent data points, which makes it much harder
for a single bad source to have produced it.

**Max level 30 — a fifth voice, and the tie-breaker for conflict C2:**

> The hero you want to advance have to be **max at 30 level**.

Together with `194179` ("mass level 1\* Hunters from **lvl 1 -30**") and the project's
own `training-public-evidence.md` (3★ **Lv.30 MAX** screenshot), that is **3 against 1**
for 30 over `23265`'s 20. Recorded as leaning, not settled (§2.1 C2).

**The skill-level cost table with material tiers named** — the same 10-band shape as
`197745` §1.5, but with the carat tiers explicit and the material families spelled out.
Verbatim:

> Materials for skill upgrading
> ATT- Rusty metal fragments, sharp metal fragments, Magical Metal fragments Stage X1,X6
> DEF- Broken shell ,So?shell , Invincible shell Stage X2,X7
> Bomber- Cold flame stone , burning flamestone, scorching stone Stage X3,X8
> Healer- A wilted herb, fresh herbs ,fruit bearing herb Stage X4,X9
>
> Material needed for skill upgrade ( the type of carat depend on the type of hero skill you training)
> Level 1 to 4 : 1 metron fragments( 100rupees)
> 5 to 9 : 1 metron fragments and 1 1 carat (200 rupees)
> 10- 14 : 2 metron frag and 2 1 carat ( 300 rupees)
> 15-19 : 2 metron frag and 3 1 carat (400 rupees)
> 20-24 : 3 metron frag and 4 1 carat and 1 2 carat( 500 rupees)
> 25 -29 : 3 metron frag and 5 1 carat and 2 2 carat (600 rupees)
> 30 - 34: 4 metron frag and 3 2 carat and 1 3 carat (700 rupees)
> 35- 39: 4 metron frag and 4 2 carat and 2 3 carat (800 rupees)
> 40 - 44: 5 metron frag and 5 2 carat and 3 3 carat (900 rupees)
> 45 - 50: 5 metron frag and 6 2 carat and 4 3 carat (1000 rupees)

Three things fall out:

1. **A carat crosswalk.** `1 carat` = the **bronze** tier, `2 carat` = **silver**,
   `3 carat` = **gold** — i.e. `197745`'s prose "Bronze tier materials / Silver tier
   Material / Gold tier Materials" is the same table expressed in words, and the
   rupee column and the metron-fragment column **match `197745` band for band**. That
   is a **second, independently authored full confirmation of the whole skill-cost
   table**, which previously had one source.
2. **The skill material families are named**, and they crosswalk onto the `vsfan.net`
   icon filenames already listed in `199711`'s body (`Rusty_Metal_Piece`,
   `Sharp_Metal_Piece`, `Broken_Shell`, `Unscathed_Shell`, `Invincible_Shell`,
   `Cold_Flamestone`, `Burning_Flamestone`, `Scorching_Flamestone`,
   `Withered_Herb`, `Fresh_Herb`, `Fruit-Bearing_Herb`). `138442`'s garbled
   **"So?shell"** is **`Unscathed Shell`**. This resolves 11 community icon names to
   game material names, which is directly usable by the project's item/skill-material
   work.
3. **The band boundaries disagree with `197745`** — see **C7** in §2.1.

**Role grouping and the element metaphor**, verbatim:

> There are clearly 3 different element in the game which are depicts as **scissor,
> paper, and stone**. So there are clear advantage that **scissor will beat paper and
> paper will beat stone**.
> In additional to the different elements , there are 4 different classes which are
> **offensive, defensive, bomber and healer. Normally we will term bomber and healer as
> supports** in the game.
> […] all hero can be max at 5 stars. However do take note that **natural 3 stars are
> stronger** than 2 stars and 1 star.

The scissor-paper-stone naming is a **fourth** naming convention for the element cycle
(after Fire/Ice/Lightning, fire/water/lightning, fire/electric/thunder). The
"Bomber and Healer are termed supports" grouping is worth noting against
`199711`'s table, which lists Bomber as its own deck category.

### 1.6.12 Post `613470` "Fate? Webs and boosts" — the Fate unlock gate, and a Fate conflict

`613470`, 2018-04-01, is a three-reply thread with **no body numerals**, but it
establishes two structural facts about the collection-bonus system:

> Am I missing something? **Why are there no 4star fate stories?** I kept making sure
> to advance different hunters for use as 4star fodder to try to unlock new fates, but
> am pretty sure I've gone through most by now.

Reply `Katte`, 2018-03-31 16:36:

> I have 4 different 4 stars ( Kain, Diana, Joy and Athena ) and none of them have 4
> star fate, but they have **5 star fates** ( or Kain has two at the least ).

Reply `Arzack`, 2018-04-01 20:03:

> **Once you have unlock the fate bonus, it'll remained unlocked forever. Even if you
> have used the character as fooder.**

So: **fate stories gate at 5★, not 4★** — a player spending fodder to reach 4★ gets
nothing, which is the complaint being answered. And `Arzack`'s claim that fate bonuses
**persist permanently** after unlock directly contradicts `138442` and `24901`, which
both say a sacrificed hunter **loses** the bonus:

> `138442`: "If you sacrifice the hero for advancement and train **the bonus will be
> gone**."
> `24901`: "If you scarifice the hero for advancement and train **the bonus will be
> gone**."

Two sources against one, and the two are the *same author* (`138442` is a rewrite of
`24901`), so it is really one claim vs one. Recorded as **C8**, unresolved. The
project's replica currently treats collection bonuses as **neutral**
(`AGENTS.md` §24), so neither side is implemented and nothing needs changing.

The FAQ document of §1.6.4 embeds **28 images** as base64 in the HTML export. All 28
were decoded and written to disk; **all 28 have valid image signatures and real
dimensions** (1080×1920 down to 444×180). **This is the only pixel evidence produced
anywhere in this lane.**

**They are a re-fetch of an already-mined document.** The project's
`recovered-assets/community-notes-2026-09-30/Blustone Guide FAQ.md` already supplied 16
of them, saved as `analysis/catalogue/stats/found/faq-image*.png`. **16 of 28 already
exist in the repo; hero coverage does not move.**

I decoded and inspected the key ones by eye:

**`faq_19` = already-recorded `faq-image17-card-051-beckhen-stats.png`.** Titled
**"Upgrade Equipment"**. Reproduces `051.md` exactly — Strength `24068` `+6291`, HP
`2879` `+437`, DEF `1149` `+154`, ATK `1471` `+317`, Attacking Speed `8.00` `+1.72`,
Critical Attack Chance `33.00` `+0.67`, Critical Attack Damage `200.00` `+10.86`,
Armor Penetration `0.00` `+0`, Block Chance `14.00` `+4.69`, Damage Reduction Block
`42.00` `+1.76`, Elemental Enhancement `5.00` `+1.65`, Elemental Resistance `5.00`
`+3.13`, Regeneration `42.00` `+0`, and the banners **"Mount 2, Increase ATK 5%"** and
**"Mount 4, Increase Attack Speed 1.72"**. **Independently re-verified; adds nothing.**

**`faq_09` = already-recorded `faq-image08-unidentified-card-equip-KO.png`.** Korean
UI. `AGENTS.md` records only its HP/ATK/DEF `2866 / 1522 / 1103`. The full panel also
reads, and these are **not** in the ledger:

| stat | white | green |
|---|---|---|
| 전투력 (Strength) | **23847** | **+4047** |
| 생명력 (HP) | **2866** | **+221** |
| 공격력 (ATK) | **1103**… | **+110** |
| 방어력 (DEF) | **1522** | **+126** |
| 공격 속도 (Attacking Speed) | **8.00** | **+1.72** |

> Correction on my own reading order: the KO panel stacks fields as 전투력/생명력/
> 공격력/방어력/공격 속도 = Strength/HP/ATK/DEF/AS, so ATK is `1103 +110` and DEF is
> `1522 +126`. The values `2866 / 1522 / 1103` recorded in `AGENTS.md` as
> "HP/ATK/DEF" therefore read, on this panel, as **HP 2866, DEF 1522, ATK 1103** —
> i.e. the recorded label order is transposed relative to the panel. Flagged, **not**
> silently corrected in `AGENTS.md` by this subagent.

Also visible and **not recorded anywhere**: the **equipment/jewel level tree** —
Weapon **Lv.40**, Armor **Lv.20**, Accessory **Lv.20**, and six jewels at
**Lv.5 / Lv.5 / Lv.5 / Lv.10 / Lv.5 / Lv.10**, with a **세트 적용 ("set applied")**
row showing two activated set icons. This is direct visual confirmation of the FAQ
prose rule "equipment comes with 1 slot by default; at **level 20** an equipment gains
an additional jewel slot" — each piece here shows two jewels.

**`faq_23` = already-recorded `faq-image22-jewel-weapon1.png`.** "Radiant Speed Jewel",
**Lv.15/15**, five stars, ATK **+29**, subs Crit Damage **+3.13** · Block Chance
**+0.72** · Elemental Resistance **+1.44** · Damage Reduction Block **+0.50**, Set
Complete Effect **"Mount 4, Increase Attack Speed 1.72"**. All already in `GEAR.md` §2.

**New in this panel and not in `GEAR.md`:** the bottom row reads
**"Required Cost for Remove — 40000 / 40"** — a **jewel removal cost of 40,000
currency plus 40 of a second material.** That is a cost numeral not previously
recorded.

**The other 25 images** were located, dimensioned and captioned (§5 table) but not
individually decoded, because the project's `found/` directory already holds the
corresponding panels for the Beckhen/Vincent/jewel/equipment sets and re-reading them
cannot change coverage. They are listed in §5 so a later pass can check the
unmatched ones (notably `faq_01`–`faq_04`, the **original Mirage Ruins loot
screenshots**, and `faq_07`, the mileage scroll-count table) without redoing the fetch.

**Coverage statement, stated first and not buried: this lane decoded 28 images and
produced ZERO new base-stat, accessory or monster tuples.** Every stat panel it
contains was already mined by a prior round of this project.

---

# 2. UNPUR[E] — everything that is not a verbatim reading

## 2.1 ★ Source-conflict register — new, and it matters more than the tables

These are **contradictions between sources of unequal standing**, recorded so no later
pass silently picks one.

| # | Quantity | Values | Sources | Assessment |
|---|---|---|---|---|
| **C1** | **4★→5★ advancement rupee cost** | **60,000** (×4) vs **15,000** (×1) | 60k: `24901` HoZhihui 2017-05-23, `193383` 2017-11-10, `189046` 2017-11-08, `201598` 2017-11-13. 15k: `24731` Kirinxd **2017-05-23** | The dissenting value is the **earliest by eight months** and sits in a post *specifically about item shops*, i.e. the most likely place to have read the number off the screen. The four 60k sources are guides, and `93837` (2017-08-06) admits its 60k is hearsay: "**Word's out** that the promotion cost is 60k." **Unresolved.** Do not adopt either without native evidence. |
| **C2** | **Max level before advancement** | **20** vs **30** | 20: `23265` 2017-05-22 ("Max level before advance is 20 which is 5 crystals \* 4 balls"). 30: `194179` 2017-11-10 ("mass level 1\* Hunters from **lvl 1 -30**") | Same seven-month gap as C1. A patch change between May and November 2017 would explain both at once. **Unresolved.** Note the project's own `training-public-evidence.md` records a 3★ **Lv.30 MAX** screenshot, which agrees with `194179` and contradicts `23265`. |
| **C3** | **1★ fodder consumed per 5★ hunter** | **120** vs **96** vs **119** | 120: `93837` (`24*5=120`, 2017-08-06) and `189046` ("One-hundred twenty 1-star hunters", 2017-11-08). 96: `197134` (2017-11-11, "To get one single Rank 4 to Rank 5 is 96 Rank 1 … only maxing 48 Rank 1"). 119: same post ("it would cost me 119 Rank 1") | **120 has two independent sources eight months apart; 96 and 119 are the same author contradicting himself two paragraphs apart.** `197134` also proposes a *reuse* method (keep and re-rank half the fodder), so its lower number is a **method difference, not a disagreement about the cost**. **120 is the better-supported figure**; 96/119 are strategy variants. |
| **C4** | **Element advantage direction** | correct vs **inverted** | correct: `55626` (vendor), `1260`/`24901`, `198374`, `193383`, `23265`. **inverted**: `194024` RobyF 2017-11-10 ("Fire-Strong against **ice** but weak to electric") | `194024` is simply wrong — its author writes "I'm only level 3". **Recorded because it is direct evidence that the community was wrong about this in 2017**, which is why a single community source must never be adopted without a vendor cross-check. |
| **C5** | **Transcendence 2★-base crystal cost** | **25 / 60** vs **"?"** | 25/60: `215324` (vendor) and `197745` Alaiko. Unrecorded: `189046` shvrkboy writes "- T2: **?** Crystals" | **Settled in favour of 25/60** by the vendor table. Recorded because it shows the community table circulating in `share-en-guide-2026-10-05.md` was *already complete* and one later author simply failed to fill the row. |
| **C6** | **Transcendence fragment multiplier** | exactly **10× crystals** in all 9 rows | `215324` (vendor), `197745` | No conflict. Recorded as a **verified structural invariant** of the vendor table, so a later pass can use it as a checksum when re-entering the numbers. |
| **C7** | **Skill-cost band boundaries** | `20-25 / 26-29 / 45-49` vs `20-24 / 25-29 / 45-50` | `197745` Alaiko (20-25, 26-29, 45-49) vs `138442` (20-24, 25-29, 45-50) | The **rupee and fragment columns match exactly in all 10 bands** — only the band edges differ, and only at three of them. Two authors transcribing the same on-screen table. Most likely a misread of a boundary digit. **No practical impact** (a player at level 25 is described by one source as band 6 and the other as band 6 anyway, since both price 500/600 at adjacent bands) but recorded because it is the only place the two independent copies of this table disagree. |
| **C8** | **Do Fate bonuses survive sacrificing the hunter?** | **lost** vs **permanent** | lost: `24901` HoZhihui and `138442` (its rewrite, so **one claim**). permanent: `Arzack`, reply in `613470`, 2018-04-01 | 1 author vs 1 commenter. **Unresolved.** The replica treats collection bonuses as **neutral** (`AGENTS.md` §24), so neither side is implemented and **no fixture is wrong**. |
| **C9** | **Which grades have Fate stories** | **4★ absent, 5★ present** | `613470` body + reply `Katte` (Kain, Diana, Joy, Athena) | Single thread, 2 participants, internally consistent, and it explains a real player complaint. Recorded as a **structural gate claim**, not a stat. No conflict found. |
| **C10** | **Element-cycle naming** | four conventions | Fire/Ice/Lightning (`55626` vendor, `198374`); fire/water/lightning (`1260`, `24901`, `23265`); fire/electric/thunder (`193383`, `201598`); **scissor/paper/stone** (`138442`) | All four agree on the **cycle direction** once mapped. Recorded so a future pass does not read "water" as a 4th element. |

## 2.2 Identity / level / gear tokens — all unusable as coverage

**No hero HP/ATK/DEF tuple was recovered in §1.6, and none is claimed.** Every token
below is listed explicitly so that none is later mistaken for a stat.

| Token | Where | Why it is not coverage |
|---|---|---|
| `Diana`, `Captain`, `Sylvester`, `Sienna`, `Hermes`, `Karl`, `Mowgli`, `Rebecca`, `Nene`, `Akasha`, `Denali`, `Levi`, `Lantern`, `Lapis`, `Metis`, `Athena`, `Bruce`, `Hecate`, `Balian`, `Robin`, `Gerard`, `Loke`, `Vincent`, `Tyltyl`, `Balian`, `Westfield`, `Locke`, `Bear`, `Riko`, `Audrey`, `Genovia`, `Windblade`, `Selene`, `Alia`, `Celine`, `Leon`, `Juno`, `Junia`, `Lawrence`, `Harley`, `Crocus`, `Anemone`, `Calibur`, `Heidi`, `Joy`, `Dumble`, `Balian`, `Lunar Alia`, `Sparky`, `Athena` | §1.6 bodies | **Named as content only. No number is attached to any of them.** `215324` says "all her statistics have increased" about Diana **with no value**, and its screenshot of exactly that moment is one of the dead `565/324/215/` files. A name-only mention is the easiest way to manufacture a fake tuple; refused. |
| `Lapis 1-10 … Gerard 111-120` (`69900`) | dungeon→trace table | Level **bands**, not hunter levels. Not a stat. |
| `Lv.30`, `3★`, `24068`, `2879`, `1471`, `1149` | §1.7 `faq_19` | **Already recorded** as `051` in `051.md`. Zero new. |
| `23847 +4047`, `2866 +221`, `1103 +110`, `1522 +126`, `8.00 +1.72` | §1.7 `faq_09` | Card identity **unknown**. Gear state partially known (Weapon Lv.40 / Armor Lv.20 / Accessory Lv.20 / jewels Lv.5–10) but the card is not identified, so it is **not** a base tuple. The existing ledger already holds the HP/ATK/DEF triple from this same image as an anonymous reading; the Strength and AS deltas and the level tree are additions to *that* anonymous record, not new coverage. |
| `Radiant Speed Jewel Lv.15`, `ATK +29`, `+3.13/+0.72/+1.44/+0.50`, `40000 / 40` | §1.7 `faq_23` | Already in `GEAR.md` §2 except the removal cost. A **jewel instance**, not an accessory; the goal's accessory rows are per accessory *name* + item level, and jewels are a different item class. **No accessory credit.** |
| `19 / 37 / 110 / 437 / 2182`, `114 / 222 / 660 / 2622 / 13080` | §1.6.2 | **Run counts and fuel totals**, i.e. derived grind costs. They *imply* an EXP ladder but are not themselves stats. |
| `1k / 3k / 12k / 60k / 15k`, `5/15/45`, `7/25/60`, `9/30/80`, `5000/9000`, `30,000`, `40,000` | §1.6.6, §1.6.1, §1.6.7, §1.7 | **Economy**, not entity stats. |
| `8000`, `2000`, `4x`, `8x`, `16x`, `10`, `5.5`, `1/8`, `60 units`, `20`, `30`, `50 consecutive` | scattered | Game parameters and UI thresholds. Not entity stats. |
| `78 total`, `16 pulls`, `4,800 manda`, `250 manda`, `300`, `600k`, `9 hearts`, `180 crystals`, `280k rupees`, `300 points`, `250`, `75 points`, `4,000 points`, `40 people` | §1.6.4 | Recruitment / gem / guild economy. Not entity stats. |
| `2.0.5.0`, `2.6.5.0`, `VER. 1191`, `2017.11.21`, `410` | §1.6.4, §1.6.2, §1.6.7 | Patch/version/date identifiers. |

## 2.3 Identity statements worth recording even though they carry no numbers

These are **[PLAYER-REPORTED] / [VENDOR-AUTHORED] qualitative facts** about identities,
which the project's identity work may find useful even with no numeral attached:

- **`55618` (vendor):** the four roles are **Offense, Defense, Bomber, Helper** — the
  vendor term is **"Helper"**, and Bombers/Healers can only use their active skill
  **inside the ornithopter** while Offense/Defense use theirs **in the field**.
- **`215324` (vendor):** the **Experienced** hunter degree is the **3★** one; Diana
  needs **4★** for her second transcendence; a transcended hunter shows **one wing per
  transcendence**.
- **`24731` / `24901` / `22732`:** tier display names are **bronze / silver(or
  sliver) / gold / green(or emerald) / blue**.
- **`69900`:** twelve named trace bands; **Denali appears twice** (91-100 and 101-110).
- **`193383`:** "**The maximum unit rarity that you can get through the Lottery Mouse
  is 3**".
- **`201598`:** Vincent is the **Guru 3 "hidden hunter"**, "about **60k+ veteran
  points**".
- **`96417`:** **Lantern** grants the team a **critical chance boost** that is lost when
  he is knocked out, hence he belongs late in the formation.
- **`954`:** **Sylvester** skills *"Attack Increase"* / *"Basic Combo"*; **Sienna**
  skills *"Supporting Gunman"* / *"Weapons Expert"* / *"Making a Beehive"*.
- **`98323`:** the recruitment **BGM encodes the resulting tier** audibly.

## 2.4 Method notes — five things this lane learned the hard way

1. **The control gate must be able to fail.** The first run of the image batch aborted
   because the control could not write its file. Had the gate been "log the control and
   continue", the whole batch's 404s would have been fabricated evidence. **Encode the
   abort; do not merely perform the control.**
2. **HTTP `000` is not a result.** The archive returned transport failures on roughly
   half of all attempts at peak times; the same control URL needed 5 tries once. Every
   retry loop here discards `000` and re-requests. Any future lane reporting "404"
   without saying how `000` was handled is reporting an unknown.
3. **`matchType=domain` + `filter=` is not usable at this reliability**, while
   `matchType=prefix` is. The prior lane's positive control used the domain form; the
   result is still a valid statement about index content, but the query is not
   reproducible, and prefix form is what should be used going forward.
4. **Wayback rewrites `img src` whether or not the bytes exist.** Confirmed again here
   at scale: `199711`'s body contains 67 rewritten `im_`-form URLs and **0** of them
   resolve. Generalisation of `share-en-guide-2026-10-05.md` §2.2 from 11 URLs to 67.
5. **A `<a href>` to a live external document is a first-class source, and the archive
   is irrelevant to it.** Post `440600` is a two-line link post whose linked Google Doc
   is **live**, and its `export?format=html` carries **28 real images**. **The wayback
   machine is the wrong tool for a link farm.** Two sibling leads from the same lane
   (`46406`'s Google **Sheet**) turned out to be `HTTP 410 Gone` — link farms have a
   ~50% survival rate, so they are worth one probe each and no more.

## 2.5 Era discipline — three separate problems

### 2.5.1 Tag definitions
- **PRE-2019-09-05**: the older equipment/crystal balance era defined in
  [`stat-version-context.md`](stat-version-context.md).
- **POST-2019-09-05**: after the +50% / +30% / +50% equipment-crystal rebalance.
- **MIXED**: a document whose own creation and last-edit dates straddle the boundary.

### 2.5.2 What in §1.6 is which

| Content | Era | Basis |
|---|---|---|
| **§1.6.1 Transcendence table** (`215324`) | **PRE-2019-09-05** | Post dated 2017-11-21 |
| **§1.6.2 EXP ladder** | **PRE-2019-09-05** | Posts 2017-11-08 … 2017-11-13 |
| **§1.6.3 vendor stat-panel statement** | **PRE-2019-09-05** | 2017-05-31 |
| **§1.6.6 advancement costs** | **PRE-2019-09-05**, but see **C1** | 2017-05-23 … 2017-11-13 |
| **§1.6.7 fuel / AP / shop** | **PRE-2019-09-05** | 2017-05-22 … 2017-11-12 |
| **§1.6.8 dungeon trace bands** | **PRE-2019-09-05** | 2017-06-22 |
| **§1.6.9 vendor mechanics** | **PRE-2019-09-05** | 2017-06-05 |
| **§1.6.10 `401574`, `330982`** | **PRE-2019-09-05** | 2018-01-31, 2018-02-18 |
| **§1.7 the 28 FAQ images** | **MIXED** — see below | Document 2018-02-26 → last edit **2026-09-21** |

### 2.5.3 The FAQ document is three documents

The `440600` document is the one place where era handling is genuinely hard, and it is
split here rather than averaged:

- **Structural / vocabulary content** — the glossary, the role and stat definitions, the
  equipment 3-piece split, the 10/20/30/40 modification gates, the level-20 second
  jewel slot, the five jewel classes, the 3/6/9 Mirage Ruins modification-material
  stages. **Era-neutral** (these are architecture, and the moderator-attributed
  equipment block is first-party).
- **Awakening** (`A1=30/30k`, `A2=50/100k`, `A3=100/150k`, 9 hearts, "elemental
  hearts", 799 mouse points) — **POST**, because the document itself dates Awakening
  to "the last relevant update" and the button costs were live in 2021-2026.
- **Balance-ish numerals** — 16 pulls / 4,800 manda guarantees, 250-manda gem pull, 300
  gem cap, 600k refining, 450-490 farming bands, guild 300/250/75 and 4,000 points.
  **Treat as POST-2019-09-05 or later**, and note the document's own reference to
  "latest patch (2.6.5.0)" — which is *earlier* than the project's 2.8.0.1 target, so
  even the late content is **not** the 2.8.0.1 balance.
- The **"As of April 1st 2019"** Ruins-reward change is dated **in the text itself** and
  is the one explicitly boundary-anchored statement.

**Rule applied: nothing in §1.6 may be mixed with §1.7, and nothing in §1.7 may be
treated as the 2.8.0.1 balance.** This mirrors the caution already recorded in
`051.md` ("2018-2019 era values … a snapshot, not the 2.8.0.1 balance").

## 2.6 What this lane did **not** establish

- **No original XP curve, ordinary Raise cost, or 2.8.0.1 balance.** §1.6.2's ladder
  is community-reported and pre-rebalance. The project's existing fixture stands
  unchanged; this file records a *conflict*, not a correction.
- **No monster stat.** `69900` is a trace-source map. Nothing here identifies a monster
  or its HP/ATK/DEF.
- **No accessory row.** The `40000 / 40` jewel-removal cost is a **jewel** cost, and
  jewels are a separate item class from the accessory *names* the goal counts.
- **No claim that the `199711` guide's own version is current.** Its title says
  "[OUTDATED for Patch 1.2.0]" and its body says "Guide Updated for VER. 1191".
- **No transcription of `forum_en`.** 131 ids were counted; zero bodies were read.
- **`197134`'s 3 images and the other 24 unmatched FAQ images were located but not
  individually decoded** (§1.7). Their captions are in §5 so the gap is explicit.

---

# 3. Negative results preserved

| Target | Check | Result |
|---|---|---|
| **21 `share_en` attachment namespaces** (`565/*`, `567/*`) | index `matchType=prefix`, all statuses **+** direct byte fetch of 31 individual files across 19 of them | **21/21 zero rows; 31/31 individual files HTTP 404**, all 4,730–4,731-byte `3c21444f` Wayback error pages. **Control PASSING in the same session.** |
| Whole `/files/attach/images/565/` and `/567/` prefixes | 2 prefix CDX queries | **0 rows each** |
| `procFileDownload&module_srl=565` | 1 direct fetch of a real `procFileDownload` URL | **HTTP 404** (4,720 bytes). *Index query for this form is INCONCLUSIVE — see §1.3* |
| Board list rows 17 and 38–75 | 9 cached list pages parsed | **No captured list page contains them.** Titles for those ids are [UNKNOWN]; their bodies were still fetched. |
| `share_en/1494773` ("Damage Calculation", cited by the FAQ) | nearest-capture fetch | **HTTP 404** (4,629 bytes) — **not archived** |
| `bs.visualshower.com/en/849114` (official equipment FAQ, cited by the FAQ) | nearest-capture fetch | **HTTP 404** (4,610 bytes) — **not archived** |
| `46406`'s Google **Sheet** `1gJjMzB1…` (the "spreadsheet that will help everyone") | live `edit` then `export?format=csv` | **HTTP 410 Gone** — permanently deleted |
| `440600`'s Google **Doc** | live `export?format=txt` / `=html` | **36,493 B text + 31,038,481 B HTML with 28 real images.** The only live recovery of the lane. |
| `forum_en/192349` (cited by `199711`) | prefix CDX `forum_en/192349*` | **0 rows.** But `forum_en` itself has **131 distinct post ids** (§5) |
| Any **new** hero HP/ATK/DEF tuple | 28 images decoded | **ZERO.** All stat panels were already mined by prior rounds. |
| Any **new** accessory row | 28 images decoded | **ZERO** |
| Any **new** monster tuple | — | **ZERO** |

**Verdict: the `share_en` screenshot board is exhausted — a hard negative for pixels,
established with 21 control-verified namespaces instead of one. The board's *bodies*
were an unexploited resource and are now mined.**

---

# 4. Coverage disposition / files updated

- **New base-stat tuples: 0. New accessory rows: 0. New monster tuples: 0.**
  Hero **1/113 (0.9%)**, accessories **1/100 (1.0%)**, monsters **0/22 (0%)** —
  **unchanged.**
- **No coverage inflation.** 28 images were decoded; every one that contains a stat
  panel is already in `analysis/catalogue/stats/found/`. The "anonymous" readings from
  §1.7 remain anonymous and were routed to §2.2, not to `coverage.md`.
- **A label-order discrepancy was found and is flagged, not fixed.** `AGENTS.md`
  records `faq-image08`'s white values as "HP/ATK/DEF `2866 / 1522 / 1103`"; the KO
  panel's own field order is Strength/HP/ATK/DEF/AS, so the triple reads
  HP 2866, **DEF 1522**, **ATK 1103**. `AGENTS.md` was **not edited** by this
  subagent.
- **New numerals recorded but not credited:** jewel removal cost `40000 / 40`; the
  equipment/jewel level tree from `faq_09`; the anonymous panel's Strength
  `23847 +4047` and Attacking Speed `8.00 +1.72`.
- **Era:** §1.6 is **PRE-2019-09-05** and must not be mixed with post-rebalance values
  (§2.5.2). §1.7 is **MIXED 2018→2026** (§2.5.3).
- **Cross-lane leads recorded, not acted on** (§5): `forum_en` (131 ids), the two dead
  cited ids, the 24 unmatched FAQ images, and the `/en/` board.
- **Explicitly not changed:** no server, no fixture, no test, no APK, no seed, no
  emulator, no phone, no Ghidra, no native library read. The XP-curve and
  advancement-cost conflicts (C1, C2) are **flagged for a separate reviewed decision**.
  The project-wide rule in `AGENTS.md` §15 (recovered vs fixture vs unknown) is
  preserved: **§1.6.1 is the only vendor-authored content here, and even it is dated
  2017 and describes the 2.8.0.1-era-prebalance economy.**
- **Files written:** this file (new);
  `polluted-observations.md` (pointer subsection appended). `coverage.md`,
  `README.md`, the TSVs, `server-ts` and all seeds are **untouched**.

---

# 5. New leads this lane opened — none acted on

| # | Lead | Evidence | Suggested next step |
|---|---|---|---|
| **L1** | **`forum_en` — 131 distinct post ids, never enumerated by any prior pass.** A different board from `share_en` (the main forum vs the Tips board). | prefix CDX `bs.visualshower.com/forum_en`, HTTP 200, 66,888 B JSON, **4 rows min**; control PASS. Distinct ids include `100013`, `100257`, `10362`, `105776`… `121631`. | **Highest-value remaining lead.** Enumerate titles from the 18 archived `forum_en` root captures, then prioritise GUIDE/REVIEW/STATS titles. Same method, same control gate. |
| **L2** | **`share_en/1494773`** — a *Damage Calculation* topic by user "Cayenne Pepper", cited by the FAQ as the authoritative damage formula. **Not archived** (404). | §1.6.4 glossary, *Damage Calculation* entry; fetch 404 with control passing | Try other archives (archive.today, Common Crawl) or the author's own repost. **Would settle the damage formula, which nothing else here does.** |
| **L3** | **`bs.visualshower.com/en/849114`** — the official equipment FAQ, quoted at length *inside* the `440600` document. **Not archived** (404). | §1.6.4; fetch 404 with control passing | The quoted text is already captured in §1.6.4; only the images would be new. Low priority. |
| **L4** | **24 unmatched images in the `440600` FAQ.** Especially `faq_01`–`faq_04`, the **original Mirage Ruins / co-op loot screens** (the only source in the project for pre-2019-04 Ruins rewards), and `faq_07`, the **mileage scroll-count table** ("78 total to claim a legendary recruitment scroll"). | §1.7; captions in the extraction run | Decode and inspect these 24; the repo holds only 16 of the 28. |
| **L5** | **The `/en/` board** (`bs.visualshower.com/en/<id>`), a third board distinct from `share_en` and `forum_en`. | `849114` URL shape; §1.6.4 links | One prefix CDX census with a control before any spending. |
| **L6** | **`199711`'s 39 `vsfan.net` wiki icon URLs + the `analysis/VSFan/` tree already in the repo** — the community wiki that this corpus cites as its primary source. | §1.4 | The VSFan archive is already local; a stat-table sweep of it was done (`vsfan-hunter-stats-raw.tsv`, 67 numeric rows, all provenance-unknown). **Unresolved why those rows carry no level/gear context** — a re-pass with the `L1`/`L4` context could fix that. |
| **L7** | **`46406`'s "spreadsheet that will help everyone"** was a Google Sheet that is now `410 Gone`. | §2.4 item 5 | **Closed.** Recorded so it is not re-probed. |
| **L8** | ~~**Title recovery for board rows 17 and 38–75**~~ **DONE in this lane.** All 21 ids fetched and their titles read from the archived `<title>`: `138442` Guide - Blustone · `172181` Guide for newcomers · `173620` [Guide] Your first week in Blustone · `174414` BlackGuidebook Vol 1: How to Write A Guide and Stop the Apocalipse. · `175648` [Guide] What a new player should know. · `176367` [Guide] Hello Captains · `178267` Things I wish I knew (guide) · `178832` Game Review - Blustone · `185186` Pvp tips for new player · `188557` Tips from a 1 month player · `192223` A Beginner's Guide - by SyanL <3 · `192930` A simple guide for beginners · `570606` Denali or Tyltyl? · `588855` how do I use veteran tickets? · `601569` My Guide To You: Just The Beginning · `611579` I need some help!! · `613470` Fate? Webs and boosts · `630834` Offense team help · `637237` Help reform my team · `642013` Best character from walnut event for newbie? · `650463` Which of these should be my first 5*? | §1.6.11, §1.6.12 | **Two of these turned out to be genuinely new and are mined above** (`138442`, `613470`). The other 19 are short and low-numeric. **No new image namespace** was found among them — none carried an attachment, so the §1.3 negative stands unchanged. |
| **L9** | **Eleven community icon names now crosswalk to game material names.** `138442` resolves `Rusty metal fragments / sharp metal fragments / Magical Metal fragments`, `Broken shell / Unscathed shell / Invincible shell`, `Cold flame stone / burning flamestone / scorching stone`, `A wilted herb / fresh herbs / fruit bearing herb` — and the garbled **"So?shell" is `Unscathed Shell`**, which matches the `Unscathed_Shell.png` icon in `199711`'s hotlink list. | §1.6.11 | Directly usable by the project's skill-material item work. The mapping is `[ATT, DEF, Bomber, Healer] × [tier 1, tier 2, tier 3]` on `stage X1,X6 / X2,X7 / X3,X8 / X4,X9`. **Verify each name against a shipped string before adopting.** |