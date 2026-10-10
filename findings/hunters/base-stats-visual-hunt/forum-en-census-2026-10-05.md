# `forum_en` board census — 3,193 English posts enumerated (the recorded 131 was a 24× undercount), 154 bodies read, the corpus is POST-rebalance, and it carries zero stat tables

**Lane:** the top open lead of
[`share-en-panels-2026-10-05.md`](share-en-panels-2026-10-05.md) §5 **L1** —
"`forum_en` — **131 distinct post ids, never enumerated by any prior pass.** A
different board from `share_en` (the main forum vs the Tips board)… **Highest-value
remaining lead.**" That file closed its own scope with §2.6: *"**No transcription
of `forum_en`.** 131 ids were counted; zero bodies were read."*

**This lane enumerates the board and reads bodies.** The headline is that 131 was
a **24× undercount**, and the second headline is that this board is the corpus
that can reach the **post-2019-09-05 balance era**, which `share_en` structurally
could not.

**Companion reading:** [`share-en-panels-2026-10-05.md`](share-en-panels-2026-10-05.md)
§1.6 for the method this inherits, and
[`vsfan-wiki-2026-10-05.md`](vsfan-wiki-2026-10-05.md) for the reminder that
**guides carry the economy tables** — confirmed here, and the reason §1.9/§1.10
are long.

---

## 0. HEADLINE

| # | Finding | Value | Where |
|---|---|---|---|
| **A** | **3,193 distinct English `forum_en` post ids**, from a fully paged CDX index (28 pages reported, 27 obtained, 49,550 rows). The recorded **131** is **24.4×** too small. | §1.2 | 
| **B** | **The board is multilingual** — `en` 25,938 rows, `zh-cn` 8,611, `jp` 6,249, `zh-tw` 4,171, `ko` 2,133, plus a `default` locale. **2,298 of 3,398 ids (67.6%) exist in more than one locale**, and 275 in all five. The English locale alone is sufficient; cross-locale corroboration is available at scale. | §1.3 |
| **C** | **The archive footprint of this board spans 2017→2023, dominated by 2019–2021.** `share_en` was **100% pre-2019-04**. Of the 154 posts read, **66 are POST-2019-09-05** by post date. This is the first English corpus in this project that can source the rebalanced era. | §1.4 |
| **D** | **`forum_en/192349` IS archived — the prior "0 rows" was a URL-form error.** But its content is **"Team Build Advice", not a damage calculation**; and the genuinely uncaptured damage-formula topic is `share_en/1494773`. Two separate corrections. | §1.5 |
| **E** | **`forum_en`'s attachment namespace is `175`** (path = `document_srl % 1000` / `document_srl // 1000`). The whole-namespace CDX sweep holds exactly **6** files, all 6 **retrieved with real pixels**. One of them is a genuine in-game UI screenshot — **Hunter Supply Office / Special Supply, captured 2021-02-04** — the **first pixel evidence for the Supply UI anywhere in this research effort**. | §1.6, §1.9.4 |
| **F** | **★ ZERO numeric HTML tables in 154 posts / 142,091 characters.** Not one `<table>` inside any post body. `share_en`'s economy tables do **not** have an equivalent here. | §1.11 |
| **G** | **★ A complete original-era team-building meta guide**, recovered from the *replies* of `192349`: a 9-hunter priority list with counter-relationships, three named deck archetypes with worked compositions, and transcendence guidance. **Zero numerals for stats, but the densest structural combat content found in any visual-research lane.** | §1.10 |
| **H** | **★ The one stat-adjacent reading in the whole corpus**: Vincent's **Fate** bonus is a **percentage on HP/ATK/DEF — 3/3/3 at 3★ rising to 6%/6%/6% (total 18) at 4★**, max reported as 12. This quantifies the **collection-bonus** system that the replica currently treats as neutral. | §2.1 |
| **I** | **Two "hidden"/gated hunters documented with independent corroboration**: **Vincent** (Guru 3, *no Fate with any other hunter*, not pullable from Rainbow scrolls) and **Robin** (natural 1★, Ice, tank, heals 400–1000/second). | §1.9.3, §2.2 |
| **J** | **★ Why the vsFan wiki's stat rows carry no level/gear context — answered from the wiki author's own post.** The author states stats were an aspiration he had not got to, and that **character renders** were what he most wanted. This closes an open question in `AGENTS.md` §98. | §1.9.5 |

**Coverage counters are UNCHANGED: hero 1/113 (0.9%), accessories 1/100 (1.0%),
monsters 0/22.** Nothing in §1 is a base-stat tuple and nothing in §2 is claimed
as one. The value delivered is a *mapped, dated, post-rebalance English corpus*
with its mechanics and economy mined, which the project did not have.

---

# 1. PURE — verbatim readings and the exact ledger

## 1.1 The positive-control gate — run first, pixel-decoded, and it aborted three times for real

Run **before any index query and before every batch**, per
`share-en-panels` §1.1. Control, unchanged:

```
http://web.archive.org/web/2021/https://bs.visualshower.com/files/attach/images/75605/303/534/001/725a8e175454a533e96dac68fc5fdb49.jpg
```

| Gate | HTTP | Bytes | Signature | Pixel decode | Verdict |
|---|---|---|---|---|---|
| Pass 1 — `tools/forum-en-fetch.py`, before the first index query | **200** | 57,414 | `ffd8ffe100184578` | JPEG **640×200**, **4,177 distinct colours** in the first 20,000 px | **PASS** |
| Pass 2 — before the 1,811-body batch | **200** | 57,414 | `ffd8ffe100184578` | — | **PASS** |
| Pass 3 — before the targeted 20-body batch | **200** | 57,414 | `ffd8ffe100184578` | — | **PASS** |
| Pass 4 — before the 188-image probe | **200** | 57,414 | `ffd8ffe100184578` | — | **PASS** |
| Pass 5 — before the 6 indexed-`175/` image fetches | **200** | 57,414 | `ffd8ffe100184578` | — | **PASS** |

`ffd8ffe100184578` = JPEG SOI + APP0/JFIF. The pixel decode is not decorative:
`share-en-panels` §2.4(4) warns that a plausible signature on a rewritten URL is
not evidence, and a 4,177-distinct-colour decode rules out an error page or a
solid placeholder.

**The gate fired, and it was correct, three times:**

1. `forum-en-fetch.py` aborted with `FileNotFoundError` on the queue path — caught
   before it could produce a batch.
2. The first polite list-page launch died in PowerShell `Tee-Object`:
   `Could not find a part of the path '…\get-list\_run.log'`, because the output
   directory did not yet exist. **Had the log been the only record, that run would
   have looked like a silent no-op.** Directory created, run re-issued.
3. **The polite fetcher's control returned `000` after 8 tries and the harness
   printed `CONTROL FAILED - zeros would be uninterpretable. ABORT.` and stopped.**
   That batch's zeros were therefore never produced, and no list page was ever
   fetched with a broken control. This is `share-en-panels` §2.4(1) working as
   designed: *"Encode the abort; do not merely perform the control."*

## 1.2 The census — 28 pages, 49,550 rows, 3,193 English ids

### The brief's single-shot query cannot enumerate this board

```
cdx?url=bs.visualshower.com&matchType=domain&collapse=urlkey&filter=original:.*forum_en.*&limit=20000
```

returns **HTTP 200 with exactly 20,000 rows — saturated at its own limit**, i.e. a
truncated prefix, not a census. It still yielded 2,175 ids, already 17× the
recorded 131.

**Partial correction to `share-en-panels` §2.4(3) and §5 L1.** That file recorded
the *domain* form as unreliable and recommended *prefix* form. That advice must be
split, because the two behaviours are different:

| Query form | HTTP | Rows | Verdict |
|---|---|---|---|
| `matchType=domain` + `filter=forum_en`, `limit=20000` | 200 | **20,000** | **Saturated/truncated**, but the **only** form that reaches the `document_srl` permalinks. Must be **paged**. |
| `matchType=prefix` on `/forum_en` | 200 | **585** | Works, but covers almost nothing: it is the `/forum_en/<id>` **path** form, which this archive barely captured (§1.5). |
| `matchType=prefix` on `/` + `filter=forum_en` | 200 | **0** | Useless. |

**Following §2.4(3) literally reproduces the 131-level undercount**, because prefix
form is reliable *and* nearly empty here. The domain form has to be paged.

`showNumPages=true` reported **28 pages** at `limit=2000`. 27 landed; **page 28
returned `000` on 20 direct tries and is recorded as INCONCLUSIVE** (§1.8).

### Why 49,550 rows is not 49,550 posts

`collapse=urlkey` gives one row per **distinct URL**, and this board's URLs are
combinatorial. Shape × language breakdown of all 49,550 rows:

| Shape | Rows | Meaning |
|---|---|---|
| `BODYPAGE` | **33,520** | `…&document_srl=<id>&page=N` — later pages of a long thread |
| `BODY` | **10,147** | `…&document_srl=<id>` canonical permalink — **the body-bearing form** |
| `COMMENT` | 3,368 | `act=dispBoardReplyComment&comment_srl=<id>` |
| `LIST` | 1,197 | `…&mid=forum_en&page=N` board list pages |
| `LISTOTHER` | 148 | `sort_index=` / `order_type=` variants |
| `OTHER` | 1,168 | `_filter=search&search_keyword=<URL-encoded Hangul>…` |

**A counting trap, recorded because it inflates naive counts.** 1,168 rows are
search-result pages carrying `search_target=user_name&document_srl=<id>`. A regex
of the form `document_srl=(\d+)` harvests an id from every one. An early pass of
this lane produced a spurious **3,398** "EN ids" before shapes were classified.
**After excluding search rows and non-EN locales the true English count is 3,193.**

## 1.3 The board is multilingual, and cross-locale corroboration is available at scale

Language, read from the `l=` parameter (absent ⇒ `default`):

| Locale | Rows | Distinct ids with a body capture |
|---|---|---|
| `en` | 25,938 | **3,193** |
| `zh-cn` | 8,611 | 1,540 (1,439 also EN) |
| `zh-tw` | 4,171 | 1,463 (1,372 also EN) |
| `jp` | 6,249 | 1,026 (992 also EN) |
| `ko` | 2,133 | 744 (728 also EN) |
| `default` | 2,448 | — |

All-locale id space **3,398**; EN-only **930**.

- **2,298 ids (67.6%) are available in more than one locale.**
- **275 ids are available in all five** — these are the official announcement posts,
  which are translated.

**Consequence for the base-stat goal, which was not previously known.** The
project's repo already holds Korean-language sources (vsFan's Korean in-game help,
the Namu captures). It did **not** need them: the **English** locale alone carries
25,938 rows and 3,193 posts. A future pass can pull the Japanese, Korean and both
Chinese versions of any of 2,298 posts from the index rows already on disk, at no
extra index cost. `census/locale-by-id.json` records the mapping.

## 1.4 Era — this board reaches the post-rebalance window; `share_en` could not

Per [`stat-version-context.md`](stat-version-context.md) the balance has two eras,
split at **2019-09-05**. `share-en-census` §2.6 established its corpus is
**100% pre-2019-04** — structurally incapable of supplying post-rebalance values.

Earliest archived capture per EN id (a **proxy for post date, not a post date** —
recorded as a proxy):

| First-capture year | 2017 | 2018 | **2019** | **2020** | **2021** | 2022 | 2023 |
|---|---|---|---|---|---|---|---|
| Ids | 52 | 611 | **1,186** | **729** | **502** | 78 | 35 |

By **actual post date**, the 154 posts read split **79 PRE-2019-09-05 / 66
POST-2019-09-05 / 7 undated**, by year: 2017 (49), 2018 (30), 2019 (34), 2020 (24),
2021 (8).

**This is the single most valuable structural fact in the lane.** `share_en`'s
dense economy tables — the EXP ladder, advancement costs, the 3×3 transcendence
matrix — are all **pre**-2019. `forum_en` is where a **post**-2019 corroboration
or contradiction of them could exist, and it is now enumerated and dated.

## 1.5 ★ Two corrections: `192349` is archived, and it is not the damage post

### 1.5.1 The prior "0 rows" was a URL-form error

`share-en-panels` §3 records: "`forum_en/192349` (cited by `199711`) — prefix CDX
`forum_en/192349*` — **0 rows.**"

**The id is present, with 19 captures.** From this lane's census:

```
192349: PRESENT caps=19 first=20180215142507 shapes=['BODY','COMMENT'] statuses=['200','302']
```

**Root cause: the `/forum_en/<id>` path form has essentially no archived captures.**
A sweep of all 28 paged CDX pages found **0 rows** matching `/forum_en` as a path,
and the separate `matchType=prefix` query on `/forum_en` returned 585 rows that are
the *board root* and `302` redirects, not post bodies. The body-bearing form is
`index.php?mid=forum_en&document_srl=<id>&l=en`.

So the prior query probed a URL form this archive does not hold and read the result
as an absence of the post. **This is the `share-en-panels` §2.4(4) trap in its
inverse form: a missing URL *form* is not evidence that the content is absent.**

### 1.5.2 But `192349` is "Team Build Advice", not a damage calculation

Fetched and read (71,316 bytes, HTTP 200):

> **`192349` · `Team Build Advice` · Zekharya · 2017.11.10 00:09 · 645 views · 4 replies**
>
> Hi i just started recently and as attached are the characters I have.
> Do you guys have any advice which character shld I turn 4 stars next?
> Meanwhile, im trying to get Akasha as my healer.
> Thanks!

**No damage formula.** The "damage calculation" topic is a *different* id —
`share_en/1494773` — which `share-en-panels` §5 **L2** already tested and which
returned a genuine **HTTP 404**. **That one remains uncaptured and this lane does
not close it.** `share-en-panels` §5 L2's own wording conflated the two ids; §1.5.1
and this subsection separate them.

**What `192349` actually contains is the best combat-structure recovery in this
lane** — §1.10.

## 1.6 ★ `forum_en`'s attachment namespace is `175`, and only 6 files in it exist

Derived from the bodies read, not guessed: the path scheme is
`<board-prefix>/<document_srl % 1000>/<document_srl // 1000>/<hash>.<ext>` — the
**same scheme `share_en` used**, where post `197745` → `565/745/197`.

| post | observed path | check |
|---|---|---|
| `100257` | `175/257/100/` | 100257 % 1000 = **257**, // 1000 = **100** ✔ |
| `104047` | `175/047/104/` | ✔ |
| `1172280` | `175/280/172/` | ✔ |
| `121631` | `175/631/121/` | ✔ |
| `192349` | `175/349/192/` | ✔ |

So **`forum_en` = prefix `175`**, and `share_en` = prefix `565`. The whole-namespace
CDX sweep of `/files/attach/images/` returns **178 rows** total; only **6** are
under `175/`, and they belong to posts that were **not** among the 154 read:

| Post implied | Index URL | CDX status | Bytes | Capture |
|---|---|---|---|---|
| **82631** | `175/631/082/001/8544f67b….jpg` | `image/jpeg` | 430,898 | 2019-08-19 |
| **225024** | `175/024/225/69198449….png` | `image/png` | 2,066,723 | 2021-02-04 |
| **794153** | `175/153/794/d748b4fb….gif` | `image/gif` | 370,995 | 2019-07-19 |
| **895176** | `175/176/895/95377a4b….gif` | `image/gif` | 154,804 | 2022-07-06 |
| **338327** | `175/327/338/d27f2623….gif` | `image/gif` | 107,356 | 2021-06-11 |
| **223712** | `175/712/223/fe3b36b7….jpg` | `text/html` (error page) | 433 | 2023-05-07 |

**All 6 were fetched. All 6 returned HTTP 200 with real, decodable pixels:**

| File | Bytes | Decoded | Verdict by eye |
|---|---|---|---|
| `225024` PNG | 2,070,695 | **PNG 750×1334** | ★ **REAL IN-GAME UI SCREENSHOT** — Hunter Supply Office (§1.9.4) |
| `82631` jpg | 449,607 | **JPEG 852×1136** | Fanart (Christmas costume, "BLUSTORN" watermark) |
| `223712` jpg | 36,563 | JPEG 800×450 | Fanart/meme (Futurama Fry reaction) |
| `794153` gif | 372,170 | GIF 498×280, 6 frames | Animation, character in a car |
| `895176` gif | 153,578 | GIF 400×385, 12 frames | Fanart painting |
| `338327` gif | 107,152 | GIF 318×318, 3 frames | Animation, smiling character |

**This generalises and sharpens `share-en-panels` §1.3.** That file found 21
`share_en` namespaces all dead. The equivalent fact here is stronger and different:
**the `175` namespace is not dead — it is nearly empty.** Six real files exist
across the entire board, and they are **only** retrievable because the *index*
listed them; every image referenced by a post body is 404 (§1.7).

## 1.7 The attachment hard negative — 188/188 HTTP 404, control passing

85 of the 154 posts read carry their own attachments, **188 distinct candidate
files**. Every one was fetched with the nearest-capture form `web/2018/<original>`
— which is form-independent, so a 404 means "no capture of this exact URL at any
timestamp", not "wrong timestamp".

**Result: `TOTAL 188 targets, tally={'404': 188}` — 188/188 HTTP 404, with zero
`000` transport failures and the positive control PASSING in the same session.**

All non-pixel responses were 4,727–4,742-byte Wayback error pages. **No PNG
(`89504e47`), JPEG (`ffd8ff`) or GIF (`47494638`) signature appears in any of them.**

**This is the most consequential negative in the lane, because the best candidate
was the best in the entire corpus.** Post **`380744` "Max trascendence Vincent"**
(Nishino, 2018-02-13, 361 views) has **9 images** and its body says, verbatim:

> I thought you guys would enjoy seeing his design **and stats**, so please have a
> look at him :)

All 9 are 404. Other posts whose *titles* promise a stat panel, likewise all 404:
`161786` "Bear's Skills" (7 imgs), `1146010` "Teresa Skillset" (5),
`1088269` "[Dark Jul] Oldman Kain #2: survival tips" (3), `1089102` "…#3: the
drumstick" (5), `1462016` "Blitz is broken part 2. **This time with pictures**" (3),
`1186694` "**Surprisingly low block chance**" (1), `942878` "[Vincent] How good is
he really?" (1).

**Wayback rewrote all 188 `img src` values into `im_` form whether or not the
bytes exist** — `share-en-panels` §2.4(4), now confirmed at 188× scale, and the
reason a rewritten URL is not evidence.

## 1.8 Bodies read — corpus, anchors, and a Wayback capture-substitution artifact

### Corpus

| Quantity | Value |
|---|---|
| Captures fetched | **166** |
| Records with a post body (`document_<id>_<cid> xe_content`) | **162** |
| **Distinct actual posts** | **154** |
| Distinct posts also present in the EN census | **154 / 154** (self-verifying) |
| Captures that were board-root or error pages | 4 (`1212`, `897470` = board root "Forums"; `1739`, `2310` = 4.7 kB error pages) |
| Body characters | **76,603** |
| Reply characters | **65,488** |
| **Total** | **142,091** |
| Numeral tokens (body + replies) | **911** |
| Distinct hunter-identity tokens | **44** |
| **Posts containing an HTML `<table>`** | **0** |

**★ Wayback served a different capture than requested, 10 times.** Ten files
resolved to a post id other than the URL's own `document_srl`. The parser keys
`id` off `data-docsrl`, so the substitution is self-detecting, and **8 of the 10
collapse onto a single post** (`1172280`, the Anemone notice), giving
162 records → **154 distinct posts**. The other two are `1147427` and `1178349`.

**This is a methodological point worth carrying: a fetch ledger keyed on the
*requested* URL would have reported 166 distinct posts and mis-attributed ten of
them.** Capture substitution is real and must be detected from the payload.

### Parsing anchors — every field read from a verified markup anchor, nothing inferred

| Field | Anchor (verified in raw HTML) |
|---|---|
| post id | `<div class="rd …" data-docsrl="…">` |
| title | `<h1 class="np_18px">`, trailing `[N]` reply count stripped; fallback `<meta property="og:title">` minus `" - Blustone"` |
| author | `<meta property="og:article:author" content="…">` |
| date/time | `<span class="date m_no">YYYY.MM.DD HH:MM</span>` |
| views | `<span>Views <b>N</b></span>` |
| body | `<div class="document_<pid>_<cid> xe_content">…</div>` |
| replies | `<div class="comment_<pid>_<cid> xe_content">…</div>` |
| also available | `<meta name="description">`, `<meta name="keywords">`, `<link rel="canonical">` |

**One real parser bug, found and fixed, recorded because it silently inflated text.**
Content divs are terminated by `<!--AfterDocument(…)-->` **or**
`<!--AfterComment(…)-->`. Matching only `AfterDocument` makes every **reply** run
to end-of-file, dragging page chrome and its images in with it: on the first 19
captures that produced **37,062 characters of reply text where there are 10,415** —
a 3.6× inflation — plus a spurious "9 images on post 1203" that did not exist.
After the fix: **0 spurious images**. Recorded because a parser that
over-collects produces **false positives**, which are worse than zeros.

### Distribution of what was read, for honesty about coverage

| Era (post date) | Posts | | Year | Posts |
|---|---|---|---|---|
| PRE-2019-09-05 | 79 | | 2017 | 49 |
| **POST-2019-09-05** | **66** | | 2018 | 30 |
| undated | 7 | | 2019 | 34 |
| | | | 2020 | 24 |
| | | | 2021 | 8 |

## 1.9 ★ The recoveries — verbatim, per source

### 1.9.1 Vendor-authored content: three official accounts, not one

`share-en-panels` §1.6 established `VSpang` as vendor-authored on `share_en`. This
board has **three** official accounts.

**`VSpang`** — the pre-release notice, and 46 replies of support answers.
Post `272`, **2017.02.22 14:42, 749 views**, body opening verbatim:

> Hello Blustone players!
> Welcome! You are currently playing an exclusive Early Access version of
> VisualShower's latest game, Blustone.
> What is Early Access?
> VisualShower believes in providing a service that grows by listening to our user
> feedback instead of a closed service. Therefore, we've decided to give limited
> game access to one special country. […]

**★ Reply to `Kaex` — a first-party statement of the damage model's shape, and of
the advancement gate. This is the most load-bearing vendor text in the lane:**

> Hi Kaex, we apologize some things were not made clear. **The damage you take is
> based on as time goes on, the enemy's attack, your character's defense, and the
> enemy's and your character's elemental attributes.** You can rank up to the next
> **Hunter Grade** by leveling up to **four "dots"** you see next to your stars.
> Then you can go to the **Hunter Gym** to advance your character. Be aware that the
> character you use in your **advancement match will be spent (i.e. sacrificed)**.
> Please let us know if you have any questions about the game feature in the Tips
> section of the forums!

Three claims, all **[VENDOR-AUTHORED]**:

1. **The damage model has four inputs**: elapsed time, the enemy's attack, the
   player's character's defence, and both characters' elemental attributes. **No
   coefficients.** This constrains the *shape* of the formula that
   `share-en-panels` §5 L2 wanted and that the uncaptured `share_en/1494773` was
   supposed to settle. A four-factor, element-inclusive, time-decaying model.
2. **Advancement requires "four dots"**, then the Hunter Gym, and the match
   character is **sacrificed**. This is a **first-party confirmation of the
   advancement gate** that `share-en-census` §2.4 warned must not be confused with
   the max-level question, and it agrees with `24901`'s prose "4 dots and 5
   diamonds" (`share-en-panels` §1.6.11). It does **not** settle conflict **C2**
   (max level 20 vs 30) — dots and level are different quantities.
3. The vendor's own term for a grade is **"Hunter Grade"**; the training screen is
   the **"Hunter Gym"**.

**★ Reply to a fuel-meter observation — community/vendor corroboration of a native
timing model.** Player, in the same thread:

> A small suggestion: I realized **the fuel on the bottom right is the time limit**,
> but it would really help if we could see the time in seconds too.

Vendor reply:

> Hello, thank you for your suggestions! We have informed our developers of your
> adding "seconds" comment. We will be adding an inventory option in the future so
> that you can view all the items and characters you own.

**This corroborates `AGENTS.md` §16.4**, where native analysis concluded *"the
battle ends on the timer, not on the monster dying"* and that
`*(this+0x2c)+0x22c` (the time limit) is **[UNKNOWN]**. A 2017 player independently
identified the **fuel meter as the time limit**, and the vendor acknowledged a
request to display it **in seconds**. The in-battle fuel meter is therefore
confirmed as the battle clock, by player observation plus vendor acknowledgement,
independent of the native read.

**`Master`** — a second official account, appearing **only** on `forum_en`.
Post `404`, 2017.03.31 23:03, whole body verbatim:

> Hello Captain!
> Blustone has finally launched its first release in Singapore!
> We are very excited to be able to present Blustone to you all after our long
> developmental period.
> We hope you enjoy the very first release of Blustone, and please feel free to
> leave any feedback you might have.
> Thank you, […]

Post `405`, 2017.03.31 23:04, whole body verbatim:

> Hello captain!
> Now we are preparing iOS Version and will be launched next week.
> We are doing our best now, so please wait a moment.
> Thank you.

And in `1955` (2017.05.13):

> Hello, the previous **v1.0.0** patch notes were deleted because of the long delay
> of the update :( The patch notes are back up in the News section of the forums
> now.

**Two structural facts:** the `[Notice]` board **doubles as official patch-note
hosting**, and those notes were **deleted and restored** during 2017 — so an absent
patch-notes page is not evidence the notes never existed.

**`Natara`** — a third official account, running a **numbered wallpaper series**
that is effectively a **hunter release ledger**. Recovered posts, verbatim titles:

| Post | Date | Title |
|---|---|---|
| `1149217` | 2019.05.10 | `[Notice] Celebrate Teresa's Introduction! Blustone 2 Wa…` |
| `1165788` | 2019.06.13 | `[Notice] Blustone 2 Wallpaper Part 2! "Mary, The Little Reaper" & "Judith, The Red Shadow"` |
| `1166196` | 2019.06.14 | `[Notice] Blustone 2 Wallpaper Part 3! "Celine, Diva of Midgard" & "Electrotherapist, Alia"` |
| `1172280` | 2019.06.28 | `[Notice] Blustone 2 Wallpaper Part 4! "Anemone, the Great General of Polar Bear" Giveaway!` |
| `1182054` | — | `[Notice] Blustone 2 Wallpaper Part 5! "Ancient Swimsuit…` |
| `1203940` | 2019.08.23 | `[Notice] Blustone 2 Wallpaper Part 7! "Leon, the Veteran Army Surgeon"` |
| `1208305` | 2019.08.30 | `[Notice] Blustone 2 Wallpaper Part 8! "Bella, the Dancing Sword" Givea…` |
| `1313853` | 2020.01.23 | `[Notice] Blustone 2 Wallpaper – Background Collection` |
| `1341491` | 2020.03.31 | `[Notice] Blustone 2 Wallpaper Part 21! "Clara, the Mail…` |
| `1369301` | 2020.05.21 | `[Notice] Blustone 2 Wallpaper Part 23! "Anemone, the Li…` |
| `1380849` | 2020.06.12 | `[Notice] Blustone 2 Wallpaper Part 24! "Themis, the Mon…` |
| `1387438` | 2020.06.26 | `[Notice] Blustone 2 Wallpaper Part 25! "Bella, the Mids…` |
| `1403522` | — | `[Notice] Blustone 2 Wallpaper Part 26! "Leon, the Lifeg…` |
| `1430622` | 2020.09.10 | `[Notice] Blustone 2 Wallpaper Part 28! "Midgard's Fines…` |
| `1476314` | 2020.12.24 | `[Notice] Blustone 2 Wallpaper Part 29! "Lily & Lyla, th…` |
| `1485930` | 2021.02.10 | `[Notice] Blustone 2 Wallpaper Part 30! "Valentine Selen…` |

`1172280`'s body, verbatim, confirming a **★4 hunter**:

> To welcome our New Hunter's arrival in Midgard, we will be giving out a new
> Blustone 2 desktop wallpaper, the images of "Anemone, the Great General of Polar
> Bear!"
>
> **Have fun in Midgard with the new ★4 Hunter, "Anemone, the Great General of
> Polar Bear!"**
>
> 1. "Anemone, the Great General of Polar Bear" Single Monitor Wallpaper(1920x1200)
> 2. "Anemone, the Great General of Polar Bear" Single Monitor Wallpaper(1920x1200) / Black Background

`1203940` likewise: *"Have fun in Midgard with the new ★4 Hunter **'Leon, the
Veteran Army Surgeon!'**"*.

**So: Anemone, Leon, Teresa, Mary, Judith, Celine, Alia, Bella, Clara, Themis,
Audrey, Lawrence, Lunar, Westfield and Selene are all attested hunter identities
from official notices, with Anemone / Leon / Teresa explicitly ★4.** This is
**identity and grade evidence, not stats.** Note the Anemone/Leon/Bella notices are
**mid-2019, i.e. 2–3 months PRE-2019-09-05**, so their ★4 grades are
pre-rebalance-era statements and must be tagged as such.

### 1.9.2 ★ Vincent — no Fate, Guru 3, and the only stat-adjacent numerals in the corpus

Two independent posts, two independent authors, eight months apart.

**Post `380744` — Nishino, 2018.02.13 07:19, 361 views. Whole body, verbatim:**

> I have the first and currently only **max trascendence Vincent** of the English
> Community. I thought you guys would enjoy seeing his design and stats, so please
> have a look at him :)
>
> He **shares no recruitment message** and **has no fates with any other hunter**.
> Also, as he's considered a special character, **you cannot pull it from Legendary
> Selection (Rainbow) scrolls**, and he has a **Guru 3 reputation requirement to
> unlock**.

**Post `942878` — Maeko暁, 2018.08.04 08:29, 299 views.** The Fate exchange, verbatim
from the replies:

> **[6]** Fate to 16? **He has no story and Fate is total of 9 (3,3,3)** So confused @.@
>
> **[8]** EDIT: It is now showing **6% HP 6% ATK 6% DEF instead of 3,3,3 (Total:18)**
>
> **[9]** but no clue if that will increase further or that is maxed for now?
>
> **[10]** Fates are hidden. **His max is 12 right now.**
>
> **[11]** But when someone mentions fates, it makes me think of **the page which
> shows the increase to base stats** as I stated so how are they hidden if it shows
> I am getting a **6% increase to the 'fates'** in 'fate' tab?
>
> **[12]** Probably because **your at 4\* right now**
>
> **[13]** The fate stories are hidden so you don't know who the fate is shared
> with, but **you will unlock the bonuses when you 5\* the right hunters.**

**And from the body, verbatim:**

> I know what his skills do but never used in PvE not PvP […]. I remember the days
> when he was **a natural 3\*** but now he is **a 4\*** (and you get given him in T1..)

Reply [3]: *"Soon as you hit **G3**, in mail you get a **T1** of him"*.

**Corroborated structural facts (§2.2 for the numerals):**

| Claim | Sources | Status |
|---|---|---|
| Vincent is awarded at **Guru 3** | `942878` (2018.08), `380744` (2018.02), plus `share_en` `201598`/`192223` and the `440600` FAQ | **Multi-source.** Note `380744` says *Guru 3 reputation requirement*, `942878` says a T1 arrives **in mail** at G3 — a gate vs a delivery, both consistent |
| Vincent has **no Fate with any other hunter** | `380744` "has no fates with any other hunter"; `942878` [6] "He has no story" | **2 independent sources, 6 months apart.** Strong |
| Vincent is **not obtainable from Rainbow/Legendary Selection scrolls** | `380744` | Single source |
| Vincent was **natural 3★, later 4★** | `942878` "a natural 3\* … now he is a 4\*" | Single source, but a *retrospective change statement*, which is the strongest kind a player can make |
| **Fate bonuses are percentages on HP/ATK/DEF** | `942878` [8][11] | **Single source, and the only stat-adjacent reading in 154 posts.** §2.1 |

**The images that would have shown "his design and stats" are 404** (§1.7).

### 1.9.3 ★ Robin — a gated natural 1★, with per-hunter power readings

Post `1128163`, `_Hasaky_`, **2019.03.26 01:41**, 218 views. This is the densest
single combat-analysis post in the corpus. Verbatim:

> **Robin is 1-star ice hunter with class of tank and high heal potential. Usually
> about 400-1000 per second if his supper is activated.** If he is upgraded he can
> be terror of any attackers in PVP and powerful hunter in PVE. Because he is 1-star
> he can be easily obtained and upgraded to **T3 (Transedence lv3)**. But he
> **leaks in** and health point (for tank)
>
> Because of his rarity, high heal, decent damage and class type. He is must have
> for any new player. If he want to proceed to higher ranks in fight club. After he
> is upgraded to 5-stars he can time out or even defeat team of 5 hunters on his
> own. **For compare I tried to attack Robin with 18k - 19k power points with Bear
> (19k) Diana (12k) Hermes (18k) Patrone (13k) and Octavia (10k)** and not even
> Robin timed out me […]
>
> There are few ways of countering Robin. First and the best is to take away his
> heal. There are three hunters that can do that and they are **Athena, Apolon and
> Genovia** […] **Athena** […] she can not consistently take away his heal because
> it's **4th skill** but she is **fire type** so she can't stay in fight with him
> for long time. **Apolon Is fire type too but he is bomber** […] **The best counter
> for Robin is Genovia she is Ice type** she can consistently remove his heal […]
> but **Genovia is 4-star hunter** so she is rare […]

Replies, verbatim:

> **[4]** **Robin only takes one second** stun/attack disable/debuffs/bleed
>
> **[6]** Windblade is also a good counter since **his bleed never goes away**
> sadly he's like Genovia, **nat 4\***
>
> **[9]** His heal is already like life steal. **It scales with his attack power**,
> which makes him ridiculously hardy combined with his **new ability to remove all
> harmful effects every second**.
>
> **[1]** Same can be said with **beckhen**. It is unlike every other **3\* attacker**
> […] It seems more like a 4\* grade hunter.
>
> **[2]** If we were to talk about imbalance, perhaps we could also look into
> **Bruce**. Why? **Heals more than every other 3\* healer**

**Structural facts recovered** (numerals in §2.2): Robin = natural **1★**, **Ice**,
**tank**, heals **400–1000/second**, heals scale with attack, **1 second** stun
immunity, removable via **skill 4**; counters **Athena** (Fire), **Apollo** (Fire,
Bomber), **Genovia** (Ice, 4★), **Windblade** (natural 4★, permanent bleed);
**Beckhen** = 3★ attacker, **Bruce** = 3★ healer.

**Note `Beckhen` is catalog `051`** — the project's one existing verified hero row
(`analysis/catalogue/stats/051.md`). This post independently corroborates his
**3★ attacker** grade, and is a candidate cross-check against that row.

### 1.9.4 ★★ The Hunter Supply Office screenshot — the first pixel evidence for the Supply UI

`175/024/225/6919844985c0035f970483177d9a6bf4.png`, post **`225024`**,
captured **2021-02-04** — i.e. **POST-2019-09-05 era**, which is exactly the window
`share_en` could not reach. Decoded **PNG 750×1334**, a phone screenshot, inspected
by eye.

**What it shows, verbatim UI strings:**

- Browser title bar: `Beelzbub : Captain Beelzbub ha…`
- Screen title: **`Hunter Supply Office`**
- **Three tabs:** **`Attendance Supply`**, **`Activity Supply`**, **`Special Supply`**
  (the third carries a **red notification dot** and an underline in red, i.e. it is
  the selected tab)
- Rows: a first row titled `Lootbox` (partially scrolled), then **five** rows titled
  **`Schumann's Marvelous Lootbox`**
- Each row carries: an **NPC portrait** (a rabbit-eared character with round glasses
  and a pale brimmed hat), a red **`Reward`** button, and an item icon with a
  **×10** quantity
- Four distinct item icons are visible: a brown/wood form, a dark cube, and two
  identical gold plant-like forms
- Top-left back chevron, top-right home icon

**Why this matters to the project, stated precisely.** `AGENTS.md` §28–§30 and §90
reconstructed Supply from native parsers: `/reference/V2_GetSupply` with REF arrays
`attend`, `attend_progress`, `attend_newbie`, `activity`, `login_bonus`; INST with
`login_bonus`; and later `RefreshSpecialList` / `SpecialListReward` for Special
Supply. **The native tab labels in this screenshot match that reconstruction's three
families in order** — Attendance, Activity, Special — which is independent
corroboration of the model's *shape* from a post-rebalance real device.

Two specific gaps it fills or narrows:

1. **`login_bonus` has no visible tab of its own.** The native screen shows exactly
   **three** tabs. `AGENTS.md` §83 established that `Supply28D` reads
   `LOGINBONUS` and calls `RequestLoginReward` → `/supply/LoginBonusReward`. So
   login bonus is **not a tab on the Supply screen** — it is invoked from the
   Supply-28D path. That is a real constraint the current model does not state.
2. **The Special Supply row shape is now visual**: *portrait · title · `Reward`
   button · one item icon with a ×10 quantity*. `AGENTS.md` §90's
   `SpecialListReward` returns `item[]`, `card[]`, `gem[]`, `skin[]` and a numeric
   `target_inst_id[]`. The screenshot shows **per-row item icons with quantities**,
   which is consistent, and it shows the reward is **claimed per row via a button**,
   not via a "Receive All" on this screen.

**It contains no hunter, monster, item or jewel statistic.** It is UI-structure
evidence for Supply only, and it is the single piece of pixel evidence this lane
produced.

### 1.9.5 ★★ Why the vsFan wiki's stat rows carry no level/gear context — answered

`share-en-panels` §5 **L6** named the `analysis/VSFan/` tree the best surviving
lead and recorded, as *unresolved*, why its 67 numeric hunter rows carry no
level/gear context. `AGENTS.md` §98 repeats the same open question.

**Post `102567` — Spondyl, 2017.08.21 23:07, 1,638 views — is the wiki's own
announcement, and it answers the question.** Verbatim from the body:

> I've been meaning to post about this for a while but I've been working on building
> a wiki for the VisualShower games over at **https://vsfan.net/wiki**.
> **I've got almost all of the Hunters scaffolded out (except those I don't have)
> as a starting point** but there's still a bunch that will take me ages to plow
> through. Well, that and a wiki isn't designed for just one person ;)
> […]
> Unfortunately, I haven't had any time (or users) to write meta-guides about what
> needs doing or how things are generally styled.

And the decisive exchange, verbatim — a community member asks about stats and the
author answers:

> **[6]** Are you planning on just getting **max 5\* units stats**, skill, story info,
> sounds great making that wiki
>
> **[7]** Well, **ideally that'd be nice!** I'm not sure how best to store the story
> info on the wiki but more complicated stuff like that I was going to store on the
> fansite
>
> **[8]** For example, I could have every Hunter as an entity with stories and skills
> tied to them rather than it being static text you have to update every time […]
>
> **[16]** Much appreciated! **The main things at this point that I'd love to get my
> hands on are character renders** as you know, haha.
>
> **[17]** We can take screenshots and stitch them together for larger scenes […]
> but you can't beat the original art y'know.
>
> **[18]** I did look into trying to datamine some stuff but **it's all locked up
> tight and would uhh \*cough\* be a violation of the TOS** y'know

**The answer:** the wiki's hunter entries were **"scaffolded out … as a starting
point"** — structure and text, not systematically captured numbers. **Stats were an
aspiration the author had not yet reached ("ideally that'd be nice"), and what he
most wanted was *character renders*.** He also explicitly declined to datamine
because he read it as a TOS violation.

**Therefore the 67 numeric rows in `vsfan-hunter-stats-raw.tsv` are not a systematic
stat capture.** They are opportunistic entries, and **their lack of level/gear
context is explained by the source's own state of completion — it is not an artefact
of this project's transcription, and no re-pass over the wiki can recover the
missing context, because the context was never recorded.**

Two further leads from the same thread:

> **[12]** There was at least one attempt at Wiki before at
> **http://blustone.wikia.com/wiki/Blustone_Wiki** but it never went anywhere
> unfortunately.
>
> **[22]** I made a wiki and whole setup on **Amino** if anyone is interested in
> helping out or learning more about Blustone and visualshower :)

## 1.10 ★★ `192349`'s replies — the complete original-era meta guide

This is the densest structural combat content in any visual-research lane, and it
lives in the **replies**, not the body. Verbatim, in order.

**Priority ranking — "From most important to least."**

> 1) **Hermes** (Anti Captain/Kain/Vincent, good for defending, excellent to destroy healers/clear cruise+excavation)
> 2) **Levi** (Anti Athena+Denali rotations, which is too common nowadays)
> 3) **Diana** (Anti Nene/Akasha+Good team buff)
> 4) **Captain** (Anti Athena when supported by Hermes/Levi, good for defence)
> 5) **Lantern** (Anti Akasha/Captain/Kain)
> 6) **Athena** (Good Defence)
> 7) **Nene** (Excellent for cruise and excavation, kind of average for arena)
> 8) **Denali** (Cheap, easy to trascend, good defence)
> 9) **Akasha** (Cruise memes, average defence)
>
> Start with the ones you have available (Captain Diana Denali) to make them **4\*-5\***
> then try to make Hermes Levi a maximum priority.

**Meta state and guidance:**

> Defence is too weak in the game right now. **Focus on offensive.** You don't need
> to make a Lapis or Scar/Octavia if you have Captain supported with Hermes Levi.
>
> **Use Denali as your first trascended healer.** Easy to gather, cheap, and good
> passives. **Acerola is disappointing…**
>
> You must get Levi and Hermes/Captain ASAP to **5\*** and try to **trascend**,
> otherwise Athena+Denali/Akasha rotations will be impossible to beat.
>
> I'd suggest making a Spear deck then try to finish one of the other 2 main decks
> as you climb up ranks.

**Three named deck archetypes — "there are 3 kinds":**

> **1] Spear** (You can use as both offensive + defensive teams. Composed usually by
> Captain+Hermes+2 bombers)
> Works as a cheap yet still damaging combo for starting in Arena. **Not good for
> protecting arena ranks between 1-50.**
> Examples:
> - Captain + Hermes + Levi + (Lantern or Diana)
> - Lapis/Scar + Hermes + Diana + (Lantern or Levi)
>
> **2] Defensive** (Two Defenders + 2 Healers/Two Defenders + Hermes + 1 Healer/3
> Defenders+1 Healer). Also known as **Stalling Decks**. Quite good to help preserve
> positions in Arena during sundays.
> Examples:
> - Captain + Athena + Nene + Denali
> - Nene + Athena + Captain + Denali (or Hermes)
> - Captain + Nene + Athena + Akasha (can also swap Akasha for a troll Hermes)
>
> **3] Critical** (Your main offensive team. Composed by 1/2 attackers or captain +
> 2/3 bombers). Great for cruise/excavation/beating any arena defence
> Example:
> - Hermes/Karl/Lapis + Lantern + Diana + Levi

**What this is, and is not.** It is a **counter-matrix and deck-composition
structure** for the pre-2019 meta: a hunter→hunter counter relation, a role
distribution per archetype, and a named-rotation problem ("Athena+Denali/Akasha
rotations"). It contains **no stat value of any kind**, and no hunter's level, rank
or equipment. It is **not** a base-stat reading and is not credited as one.

**Why it is still valuable to the project.** `AGENTS.md` §19 recovered the role
enum natively (1 Offense, 2 Defense, 3 Bomber, 4 Support). This post independently
confirms the four-role taxonomy in play terms ("attackers", "bombers", "Defenders",
"Healers") and gives the **counter-relations** that the replica's combat model does
not have at all. It also independently corroborates `AGENTS.md` §24's "Denali" and
"Loki"-band material context (`69900` in `share-en-census` §1.6.8 places Denali
traces at levels 91–110 — consistent with "easy to gather").

**Two new identities** appear here and nowhere else in the corpus read:
**Scar** and **Octavia**.

## 1.11 ★★ The central negative — zero numeric tables in 154 posts

**`posts containing an HTML <table>: 0`** across 154 posts / 142,091 characters.
The table-aware scanner (`tools/forum-en-scan.py`) walks every `xe_content` div,
parses all `<table>/<tr>/<td>` structures, and requires ≥2 non-empty rows to count
a table. **It found none.**

This is a **hard negative and it is the most useful thing in this file after the
census itself**, because it settles what kind of board this is:

| | `share_en` | `forum_en` |
|---|---|---|
| Character | **guide / tips board** — authored walkthroughs | **main forum** — questions, answers, official notices, fanart, drama |
| Posts | 105 | **3,193 (EN)** |
| Body chars | 166,838 | 142,091 (**154 posts**, a 9.8% sample) |
| Posts with an HTML table | several, incl. the **official Transcendence 3×3 matrix** | **0** |
| Recovered economy tables | **6+ corroborated ladders** (EXP, advancement, transcendence, shop, dispatch, skill costs) | **none as tables**; numerals appear as prose in replies |

**So `share_en` was the right board for economy tables and `forum_en` is not.** The
task brief's premise that guide bodies would prove more valuable than images is
**confirmed for `share_en` and does not transfer to `forum_en`** — the equivalent
value on `forum_en` came from **official notices** (§1.9.1), **community meta
analysis** (§1.10, §1.9.3) and **one UI screenshot** (§1.9.4), not from tables.

The numerals that *do* exist (§2) are scattered prose figures, and are usable as
polluted observations, not as tables.

## 1.12 What this lane did **not** obtain

- **1,811 canonical bodies were queued; 154 distinct posts were read** (9.8%). The
  queue, the prioritiser (`tools/forum-en-rank.py`) and the polite fetcher all exist
  and are documented. The prioritiser needs board **list** pages, and those could
  not be retrieved (§1.1 gate 3), so **ranking was never applied** — the 154 are
  the head of an id-ordered queue, weighted only by capture count and era spread.
- **Zero of `192349`'s, `380744`'s or the other promising posts' images** — 188/188
  404 (§1.7).
- **`share_en/1494773`**, the genuinely uncaptured *Damage Calculation* topic,
  remains uncaptured. Not closed.
- **`CDX page 28`** — 20 tries, `000`. INCONCLUSIVE.
- **No non-English body** was read, though 2,298 ids are available in other locales.
- **No 2.8.0.1 balance.** The newest post read is 2021.11.

## 1.13 Completeness and negative-result register

| Target | Check | Result |
|---|---|---|
| `forum_en` EN census | domain+filter paged, `showNumPages` → 28 pages | **3,193 EN ids** from 27/28 pages. **Recorded 131 corrected, 24.4×** |
| CDX page 28 | 20 direct tries | **`000`. INCONCLUSIVE**, not zero |
| Board-level completeness (posts ever posted) | — | **Unknown.** 3,193 = every EN post with an archived capture, **not** every post that existed. Same limit `share-en-census` §1.3 records for `share_en` |
| `/forum_en/<id>` path form | sweep of all 28 paged pages + prefix query | **0 body rows.** Effectively unarchived — **the cause of the prior `192349` zero** |
| `forum_en/192349` | census + fetch | **PRESENT, 19 captures; body read.** "Team Build Advice". Prior "0 rows" **retracted** as a form error |
| `forum_en/105776` (listed by `share-en-panels` L1 as a distinct id) | EN census | **ABSENT.** Likely non-EN locale; not a negative on the post |
| **`forum_en` attachment bytes (188 files, 85 posts)** | nearest-capture `web/2018/` fetch, all statuses | **188/188 HTTP 404**, **zero `000`**, 4,727–4,742-byte error pages, **control PASS in the same session. HARD NEGATIVE** |
| `175` namespace existence | whole-namespace CDX sweep | **6 rows exist**; **6/6 fetched, HTTP 200, real pixels decoded** |
| Those 6 images, by eye | decoded and inspected | **1 real in-game UI screenshot** (Supply, 2021-02-04); **5 fanart/meme.** **Zero stat panels** |
| Numeric HTML table in a body | table-aware scan of all `xe_content` divs, 154 posts | **ZERO.** §1.11 |
| Any HP/ATK/DEF **base** tuple | 154 posts + 6 images | **ZERO.** |
| Any stat-adjacent numeral | 154 posts | **1 post** (`942878`), and it is a **collection-bonus percentage**, not a base stat. §2.1 |
| `share_en/1494773` ("Damage Calculation") | — | **Still uncaptured.** Not closed by this lane |

---

# 2. UNPURE — every numeral, tagged, with nothing promoted

Nothing in §2 is claimed as a base stat. Every entry carries its
**identity / level / gear / era** state so a later pass cannot mistake one for a
base tuple. Era per
[`stat-version-context.md`](stat-version-context.md): **PRE** = post dated before
2019-09-05; **POST** = on/after; **MIXED** = document straddles the boundary.

**Counts:** 911 numeral tokens across 154 posts; 1 post with a stat-adjacent hit;
40 posts with economy-adjacent numerals; 85 posts with attachments (188 refs, all
404); 44 distinct identity tokens.

## 2.1 ★ The one stat-adjacent reading — Fate/collection bonus percentages

| Quantity | Value | Identity | Level | Gear | Era | Source |
|---|---|---|---|---|---|---|
| Fate bonus on **HP** | **`3,3,3` → `6%`** | Vincent | 3★ then 4★ | **not stated** | **PRE** (2018-08-04) | `942878` [6][8][11][12] |
| Fate bonus on **ATK** | **`3,3,3` → `6%`** | Vincent | 3★ then 4★ | not stated | **PRE** | same |
| Fate bonus on **DEF** | **`3,3,3` → `6%`** | Vincent | 3★ then 4★ | not stated | **PRE** | same |
| Total across the three | **`9` → `18`** | Vincent | 3★ then 4★ | not stated | **PRE** | `942878` [6][8] |
| Stated maximum | **`12`** | Vincent | 4★ | not stated | **PRE** | `942878` [10] |

**Why this is NOT base-stat coverage, stated precisely.** These are **collection /
Fate bonuses displayed on a "fate" tab**, i.e. **percentages applied on top of a
hunted card**, read at an unstated level with unstated equipment. They are a
*modifier*, not a base value, and they are in the same numeric neighbourhood (6%)
that a base reading would occupy. **The danger is exactly that a `6` here could be
mistaken for a stat.** It must not be.

**It is still a real, previously unrecorded mechanic**, and it bears directly on the
project: `AGENTS.md` §24 says *"Original collection bonuses remain neutral"* and
`share-en-panels` §1.6.12 records conflict **C8** (do Fate bonuses survive
sacrificing the hunter?) with no magnitude known. **This is the first quantified
statement of what a Fate bonus is.**

**Internal inconsistency, recorded not resolved.** `3,3,3` total 9 vs `6%,6%,6%`
total 18 vs a stated "max is 12". Three figures for one quantity in one thread.
Reply [12]'s "Probably because your at 4\* right now" offers a grade-scaling
explanation for the 3→6 step but not for 6 vs 12. **Unresolved.** The `6%` is
additionally ambiguous as `6` or `0.06`; the post says `%` and nothing more.

## 2.2 Per-hunter numerals — all identity-bearing, none with level/gear

| Value(s) | Hunter(s) | Field | Level | Gear | Era | Source |
|---|---|---|---|---|---|---|
| **`19k`, `12k`, `18k`, `13k`, `10k`**; team `18k–19k` | **Bear, Diana, Hermes, Patrone, Octavia** | **team "power points"** | **not stated** | **not stated** | **PRE** (2019-03-26) | `1128163` |
| **`400`–`1000` per second** | **Robin** | **heal rate** (super active) | not stated | not stated | **PRE** | `1128163` |
| **`1` second** | **Robin** | stun / attack-disable / debuff / bleed immunity | n/a | n/a | **PRE** | `1128163` [4] |
| **`75`** HP/second | Robin | *author's own proposed nerf*, not original | n/a | n/a | **PRE** | `1128163` |
| **`5%` of damage** | Robin | *author's proposed life-steal*, not original | n/a | n/a | **PRE** | `1128163` |
| `4`th skill | Robin's heal-removal is on Athena's **skill 4** | skill slot | n/a | n/a | **PRE** | `1128163` |
| `3★` attacker; `4★`-grade-like | **Beckhen** (= catalog `051`) | grade | 3★ | not stated | **PRE** | `1128163` [1] |
| `3★` healer; heals more than every other 3★ healer | **Bruce** | grade | 3★ | not stated | **PRE** | `1128163` [2] |
| natural `4★`; bleed never expires | **Windblade** | grade | nat 4★ | not stated | **PRE** | `1128163` [6] |
| `4★`; Ice; heal-removal | **Genovia** | grade/element | 4★ | not stated | **PRE** | `1128163` |
| Fire; healer; inconsistent skill-4 heal removal | **Athena** | element/role | not stated | not stated | **PRE** | `1128163` |
| Fire; Bomber | **Apollo** (spelled *Apolon*) | element/role | not stated | not stated | **PRE** | `1128163` |
| **`3000`** HP ("roughly 3000 or less hp") | **Lantern**'s extended special / crit observed to fire below this | HP threshold, enemy identity unknown | not stated | not stated | **PRE** (2017-09-14) | `115915` |
| `2000` — *skill name* "Death Metal 2000" | **Bradley** | skill NAME, not a value | n/a | n/a | **PRE** (2017-09-19) | `119662` |
| `Attacker Class, Fire Elemental` | **Bradley** | role/element | n/a | n/a | **PRE** | `119662` |
| "same hp value", "close to your def value" | **Bibi** vs **Riko** | HP/DEF compared | not stated | **stated as partial**: Riko jewels only **level 6**, "not her end-game jewels"; equipment "still needs work" | **PRE** (2018-09-01) | `975926` [5][6] |
| **`6%`**–**`8%`** stat raise per transcendence; "healing is partially stat based" | **Acerola** (the observation); **Joy/Akasha** discussed | **transcendence magnitude**, player best-guess, **quoted from a third user** | not stated | not stated | **PRE** (2018-02-04) | `342288` [4] |
| `3★`, `4★`→`5★` | **Vincent** | grade history: natural 3★ **later** 4★ | 4★ | not stated | **PRE** (2018-08-04) | `942878` |
| natural `3★` | **Akasha, Kain, Karl** | "Normally when I pull 3☆ It would be Akasha, Kain or Karl" | n/a | n/a | **PRE** (2018-09-19) | `988349` |

**Explicitly NOT stat values, listed so they cannot drift into a stat table:**
`400`–`1000`/s is a **heal rate**; `75` HP/s and `5%` life-steal are the *author's
own nerf suggestions*, not observations of the shipped game; `3000` is an
**enemy's** HP, not Lantern's; `2000` is part of a skill **name**; `5%`–`8%` is a
third-hand player guess at a **percentage modifier**; `14`/`8` in §2.3 are
**Fight Club rating deltas**.

## 2.3 Economy and system numerals (not entity stats)

### Fight Club — the rating ladder and the win/loss deltas ★ POST-rebalance

`1422177`, **2020-08-24**, verbatim:

> The points are Fight Club points. **The average player will have about 1000, but
> that number rises exponentially from there, reaching 1500 just before top 100,
> 2000 by about 50-60th, and 3k-4K in top 10. You get 14 for each FC win, and lose
> 8 for every loss.** At the end of the week your points lower by […]

| Quantity | Value | Era |
|---|---|---|
| Average player FC rating | **~1000** | **POST** |
| Rating just before top 100 | **1500** | **POST** |
| Rating at rank ~50–60 | **2000** | **POST** |
| Rating in top 10 | **3000–4000** | **POST** |
| **Points gained per FC win** | **+14** | **POST** |
| **Points lost per FC loss** | **−8** | **POST** |
| Weekly decay | "lower by […]" — **value cut off in the capture** | POST |

**Bearing on the project, stated as a conflict not a correction.**
`AGENTS.md` §45 built Fight Club with "BP1 per accepted active attempt, honor10,
rating±10" — **all local fixtures**. This post gives **original-era** values of
**+14/−8** and a **distribution ladder**. It is a single source and the thread is
truncated, so **nothing is adopted here**; it is recorded as the first concrete
original-era FC rating evidence located.

### Login Bonus / daily rewards — the original cadence ★ POST-rebalance

`1422054`, **2020-08-24**, verbatim:

> firstly **there are no free daily pulls. You get scrolls weekly, from daily sign in
> with increasing star as you progress in the month with a 10+1 in the third week.**

and, on the other recruitment route:

> Another way to recruit would be from traits that you have collected through the
> "cruise" missions, you can recruit hunters from **suspicious mouse guy** when
> you've collected enough traits for that specific hunter.

| Quantity | Value | Era |
|---|---|---|
| Free **daily** pulls | **none** | **POST** |
| Scroll cadence | **weekly**, via daily sign-in | **POST** |
| Star grade | **increases as you progress within the month** | **POST** |
| **Week 3** reward | **a 10+1** | **POST** |
| Trace-based recruitment NPC | **"suspicious mouse guy"** | **POST** |

**Bearing on the project.** `AGENTS.md` §83 implemented Login Bonus as a **LOCAL
28-entry 100-gold/calendar** with no catch-up, and noted "original
economics/cadence unknown". **The cadence is now known structurally: weekly,
grade-increasing through the month, 10+1 at week 3.** The *amounts* remain unknown.

### Awakening gate and the level-30 cap ★ POST-rebalance

`1478354`, **2021-01-04**, verbatim, on adding the "fire heart" to Rebecca:

> **Get her to 5\*, level 30 and you'll get the option to awaken her**

| Quantity | Value | Era |
|---|---|---|
| Awakening prerequisites | **5★ + level 30** | **POST (2021)** |

**Bearing on the project.** `AGENTS.md` §24 records "ordinary CHARACTER cap 30
regardless grade is explicit historical community evidence (Namu footnote 36 plus
2018 Lv.30 MAX screenshot)" and separately notes "Final 2.8.0.1/awake caps remain
unpinned". This is a **2021 English-language statement that level 30 is the
awakening gate** — i.e. the cap survives into the post-rebalance era. It does **not**
by itself prove the 2.8.0.1 cap.

### Recruitment, gacha and trace thresholds

| Value | What | Era | Source |
|---|---|---|---|
| **`40` traces** to unlock a **2★** hunter | **Witch Riko** | PRE (2018-09-01) | `975926` [2] |
| up to **`80` traces** if very lucky; rarer for a natural 4★ | trace drop | POST (2020-07-29) | `1407105` |
| **`100`++ pulls**; `20`++ pulls hoped sufficient | Witch Riko guaranteed banner | PRE (2017-10-24) | `154691` |
| **`100`++ pulls, nothing** | the Diana event, same author | PRE | `154691` |
| `1★` normally per scroll/manda/10+1; `50` elites used | pull distribution | PRE (2018-09-19) | `988349` |
| **`11×` 10+1 pulls** without a natural 4★ | Christmas banner | POST (2020-01-24) | `1314872` |
| `4*` selection scroll **monthly** | veteran/daily reward | POST (2020-07-02) | `1393319` |
| `4*` trans tickets purchasable only with **green** Manda | transcendance tickets | PRE (2019-04-18) | `1140439` |
| **"Buy fragments"** advised over 10+1 | Twins banner | PRE (2018-02-25) | `436737` |
| `300%` rate-up question for Papillon | event banner | PRE (2018-01-29) | `323248` |

### Fuels, timers and rewards

| Value | What | Era | Source |
|---|---|---|---|
| **+400%** and **+200%** auto-battle-time increases (two veteran tiers) | auto-combat | PRE (2017-08-17) | `100013` |
| **1 fuel ticket = 1 hour** of fuel time; `7` used per night, `1` per `3` hr | fuel ticket | PRE | `100013` [8] |
| `45` fuel from attendance + daily quest | fuel sources | PRE (2018-01-29) | `323248` |
| **`33k rupee`** + "big metron" from a daily abyss run at **stage 8** | abyss reward | POST (2020-07-02) | `1393319` |
| **`300` fuel → `15` socks; `500` fuel → `35` socks**, same team | fishing sock rate | POST (2019-12-23) | `1294485` |
| `18k` fuel spent before finding the sock-drop-rate thread | fishing | POST (2019-12-25) | `1296754` |
| `100` tokens, `150` manda — reward difference in a rank war | FC | POST (2021-03-02) | `1489782` |
| `700`+ points lost to one opponent | FC | POST | `1489782` |
| Metron Crystal / nat 4 scrolls obtainable from fishing | fishing reward | POST (2021-03-24) | `1493736` |
| Metron Fragments `250`/`300`/`600`; Manda `30`/`150`/`300`/`600` | *author's own* proposed event costs | PRE (2019-05-12) | `1150964` |
| Fuels `300`/`600`; 4★/5★ target range; disqualify below **level 40-45** | *author's own* community challenge | PRE (2019-05-24) | `1156929` |
| `50k` rupee → `0` overnight | bug report, not a designed value | PRE (2017-04-24) | `1532` |
| story mode "currently only till **level 90**" | campaign cap, 2017 | PRE | `3698` |
| `5`/`5` "proven to work" draws | banner anecdote | PRE | `110527` |

**Version identifiers, not values:** `0.9.9`, `1.0.0`, `1.0.0.3`, `1.0.1.0`,
`1.00` (posts `272`, `1955`, `2198`).

## 2.4 Identity tokens attested — 44, all without base stats

`captain` ×68 · `anemone` ×58 · `bear` ×55 · `karl` ×48 · `kain` ×37 · `athena` ×25
· `joy` ×24 · `vincent` ×22 · `celine` ×21 · `alia` ×20 · `diana` ×20 · `hermes`
×20 · `nene` ×19 · `lantern` ×17 · `robin` ×17 · `denali` ×15 · `leon` ×15 ·
`akasha` ×14 · `riko` ×14 · `genovia` ×12 · `levi` ×12 · `bruce` ×10 · `tyltyl` ×9 ·
`lapis` ×8 · `patrone` ×8 · `windblade` ×6 · `audrey` ×5 · `rebecca` ×5 · `selene`
×5 · `scar` ×4 · `heidi` ×3 · `lawrence` ×3 · `locke` ×3 · `bradley` ×2 · `sienna`
×2 · `sylvester` ×2 · `balian` ×1 · `crocus` ×1 · `harley` ×1 · `junia` ×1 ·
`juno` ×1 · `lunar` ×1 · `mowgli` ×1 · `teddy` ×1

**Two of these are new to the project's identity work** and appear in the meta guide
only: **Scar** and **Octavia** (§1.10). **Apollo** appears in `1128163` under the
misspelling *Apolon*.

**Not coverage.** Every token above is a name in prose. §2.2 is the complete list
of the ones with any numeral attached, and none of those numerals is a base stat.

## 2.5 ★ False positives this lane produced and rejected — recorded so they are not re-derived

Four, all caught by construction:

1. **`bear` ×55 is mostly NOT the `036` hunter.** An identity sweep matched the
   token 55 times, but the largest contributor is **Natara's notice title
   "Anemone, the Great General of Polar Bear"** — "Bear" inside a *title*, in
   every one of `1172280`'s many duplicate captures. Treating `bear` as a hunter
   hit here would manufacture a false identity record. The genuine hunter uses in
   this corpus are `1128163` (Bear 19k power) and `1128163`/`154691`-era discussions.
2. **10 capture substitutions.** Ten requested URLs served a **different** post
   than their own `document_srl` (§1.8), 8 of them collapsing onto `1172280`. A
   fetch ledger keyed on the *requested* URL would report 166 distinct posts and
   mis-attribute ten.
3. **1,168 search-result rows.** `document_srl=(\d+)` matches
   `_filter=search&search_keyword=…&document_srl=<id>`, producing a spurious 3,398
   "EN ids" before shape classification (§1.2).
4. **CDX column offset.** In default CDX json output `r[3]` is `mimetype`, **not**
   `statuscode`; `statuscode` is `r[4]`. An early pass recorded "index status==200
   only: 0" purely because of this, which read like a total failure and was not.

## 2.6 Source conflicts found in this lane — none resolved

| # | Quantity | Values | Sources | Assessment |
|---|---|---|---|---|
| **F1** | Vincent's Fate-bonus magnitude | `3,3,3` total 9 · `6%,6%,6%` total 18 · "max is 12" | `942878` [6][8][10], one thread, one author | **Unresolved, single author.** Grade-scaling is offered for 3→6 but not for 6 vs 12. Also ambiguous whether `6%` means 6 or 0.06 |
| **F2** | Vincent's grade | natural **3★** → now **4★** | `942878` "I remember the days when he was a natural 3\* but now he is a 4\*" | Single source, but a retrospective *change* statement, which is the strongest form a player report can take. Not contradicted anywhere in 154 posts |
| **F3** | Vincent's Guru-3 delivery | "Guru 3 **reputation requirement** to unlock" vs "at G3, **in mail** you get a T1" | `380744` (2018.02) vs `942878` [3] (2018.08) | Both consistent (gate + delivery). `share-en-census` §2.2.6 has the same two framings. **Not a conflict** |
| **F4** | Percent-scale magnitude of a "grade" increase | Fate ≈ **6%** (`942878`) vs transcendence ≈ **5–8%** (`342288`) | two posts, 6 months apart | **Not necessarily a conflict** — different systems (collection bonus vs duplicate fusion) that can share a scale. Recorded so a future pass does not merge them |
| **F5** | "Auto-battle times" increase | **+400%** complained of, **+200%** proposed | `100013`, one post | Two veteran tiers are the likely reading, matching `share-en-panels` §1.6.9's "Auto-Combat 10 Times / Auto-Combat 50 Times". **Unconfirmed mapping** — not asserted |
| **F6** | Fight Club rating deltas vs the replica's fixtures | original-era **+14/−8** (`1422177`, POST) vs replica **rating±10** (`AGENTS.md` §45) | one forum source vs one local fixture | **Conflict recorded, nothing adopted.** The replica's values are explicitly fixtures; this is a single truncated source |
| **F7** | Robin's tier | natural **1★** (`1128163`) upgraded to **5★** | one post | Internally consistent (natural grade vs final grade). Not a conflict |
| **F8** | Login Bonus cadence | **weekly, 10+1 at week 3** (`1422054`, POST) vs replica **daily 28-entry calendar** (`AGENTS.md` §83) | one forum source vs one local fixture | **Conflict recorded, nothing adopted.** The replica's calendar is explicitly LOCAL. §2.3 |

## 2.7 Era discipline — applied to every entry above

- **§2.2** is **PRE-2019** throughout. The single densest combat post
  (`1128163`) is **2019-03-26**, i.e. **~5 months before** the rebalance boundary,
  and must not be read as post-rebalance balance. `1172280` (Anemone ★4,
  2019-06-28) and `1203940` (Leon ★4, 2019-08-23) are likewise **pre**.
- **§2.3** splits cleanly: the FC ladder (+14/−8, 1000/1500/2000/3k-4k), the Login
  Bonus cadence, the `4*` selection scroll, the abyss `33k` rupee, the sock rates
  and the Awakening 5★+Lv.30 gate are **all POST**. The auto-battle percentages,
  fuel-ticket hour, `40`-trace threshold, `100`++-pull banners, `50k`-rupee bug and
  level-90 campaign cap are **all PRE**.
- **§1.9.4's Supply screenshot is POST (2021-02-04)** — the only pixel evidence in
  this file, and in the right era.
- **Nothing here is 2.8.0.1 balance.** The newest post read is **2021.11.23**, and
  the project targets APK 2.8.0.1. Consistent with `051.md`'s standing caution
  ("2018-2019 era values … a snapshot, not the 2.8.0.1 balance").

---

# 3. Negative results preserved

| Target | Check | Result |
|---|---|---|
| Numeric HTML table in a post body | table-aware scan of every `xe_content` div, 154 posts / 142,091 chars | **ZERO.** The central finding, §1.11 |
| **Any hero base HP/ATK/DEF tuple** | 154 posts + 6 decoded images | **ZERO** |
| Any accessory row | 154 posts | **ZERO** |
| Any monster tuple | 154 posts | **ZERO** |
| Any stat panel image | 188 attachment URLs, 85 posts | **188/188 HTTP 404**, zero `000`, **control PASS in the same session. Hard negative** |
| The 6 indexed `175/` files | fetch + decode + inspect | 6/6 real pixels; **1 real UI screenshot** (Supply), **5 fanart/meme**; **0 stat panels** |
| A damage formula | `192349` read; `share_en/1494773` re-checked | **No formula.** `192349` is team advice; `1494773` still 404. **Vendor's four-factor shape recovered instead** (§1.9.1) |
| A systemically-captured vsFan stat table | wiki author's own announcement read | **Does not exist.** Stats were an aspiration; renders were the priority. §1.9.5 |
| The recorded board size | paged CDX census | **3,193 EN ids, not 131.** 24.4× correction |

---

# 4. Coverage disposition / files updated

- **New base-stat tuples: 0. New accessory rows: 0. New monster tuples: 0.**
  Hero **1/113 (0.9%)**, accessories **1/100 (1.0%)**, monsters **0/22** —
  **UNCHANGED.**
- **No coverage inflation.** The 6 decoded images contain no stat panel. The one
  stat-adjacent reading (Fate percentages) is a *modifier* on a card of unstated
  level and gear and is quarantined in **§2.1**, deliberately away from
  `coverage.md`.
- **Era:** §1.9.1's Anemone/Leon/Teresa ★4 notices are **PRE-2019-09-05**;
  §1.9.4's Supply screenshot and §2.3's FC/Login-Bonus/Awakening/sock/abyss rows
  are **POST**. Nothing is 2.8.0.1 balance.
- **`polluted-observations.md` NOT touched**, per the parent's instruction that it
  mirrors. §2.1/§2.2/§2.3 are the material to mirror.
- **Not changed:** no server, no fixture, no test, no APK, no seed, no LevelDB, no
  emulator, no phone, no Ghidra, no native library read, no archive write, no
  re-upload, no login, no form submission, no catalog row. All fetches were
  **GET-only reads of `web.archive.org`**. All file writes are Python or the
  `write`/`edit` tools — **no PowerShell `Set-Content`** anywhere, per
  [`GUARD-encoding-and-archive-traps.md`](GUARD-encoding-and-archive-traps.md).
- **Files written:** this file (new). Tooling: `tools/forum-en-cdx.py`,
  `tools/forum-en-census.py`, `tools/forum-en-cdx-one-page.py`,
  `tools/forum-en-classify.py`, `tools/forum-en-merge-pages.py`,
  `tools/forum-en-queue.py`, `tools/forum-en-queue-targeted.py`,
  `tools/forum-en-fetch.py`, `tools/forum-en-fetch-concurrent.py`,
  `tools/forum-en-fetch-polite.py`, `tools/forum-en-fetch-small.py`,
  `tools/forum-en-parse.py`, `tools/forum-en-parse-lists.py`,
  `tools/forum-en-scan.py`, `tools/forum-en-numerals.py`,
  `tools/forum-en-identities.py`, `tools/forum-en-locales.py`,
  `tools/forum-en-img-queue.py`, `tools/forum-en-probe-images.py`,
  `tools/forum-en-probe.py`, `tools/forum-en-gif-frames.py`,
  `tools/forum-en-rank.py`, `tools/forum-en-check.py`,
  `tools/verify-control-pixels.py`. All fetched material under gitignored
  `recovered-assets/forum-en-2026-10-05/`.
- **Untouched:** `coverage.md`, `README.md`, `polluted-observations.md`,
  `coverage.tsv`, the archive TSVs, `server-ts`, all seeds.

---

# 5. Leads this lane opened — none acted on

| # | Lead | Evidence | Next step |
|---|---|---|---|
| **M1** | **★ 3,039 unread EN posts** (3,193 census − 154 read = **97.2% of the board still unmined**). The queue, prioritiser and polite fetcher all exist. | §1.2, §1.12 | Apply `tools/forum-en-rank.py` once list pages are retrievable, then work the top 500. **The single highest-value remaining action in this corpus.** |
| **M2** | **★ The 2,298 multi-locale ids.** Japanese/Korean/Chinese bodies for 2,298 posts are one index row each and are already on disk. | §1.3, `census/locale-by-id.json` | Fetch `zh-cn`/`jp` bodies for the numeric-bearing EN posts to test whether community *guidance* was clearer in another language. Especially relevant because the repo already holds Korean sources |
| **M3** | **★ `275` posts exist in all five locales** — the official `Natara`/`VSpang`/`Master` announcement series, translated. | §1.3 | Mine them for **patch notes and balance-change announcements**. The vendor's own changelog would directly constrain the **2019-09-05 rebalance** that `stat-version-context.md` dates only from a TapTap announcement |
| **M4** | **`225024`'s Supply screenshot is real and post-rebalance.** Its post body was not read (that post is outside the 154). | §1.9.4 | Read post `225024`'s body and the neighbouring indexed-image posts (`82631`, `794153`, `338327`, `895176`, `223712`) — they are the **only** forum_en posts known to have live attachments |
| **M5** | **Fight Club original-era ladder** (+14/−8; 1000/1500/2000/3k-4k) from one truncated source. | §2.3 | Find a second source. `AGENTS.md` §45's ±10 is an explicit fixture; nothing should move without corroboration |
| **M6** | **Login Bonus cadence** (weekly, grade-increasing, 10+1 at week 3). | §2.3 | Corroborate, then reconcile against `AGENTS.md` §83's LOCAL 28-entry daily calendar. **A cadence change, not a number change, so it is comparatively safe — but it is still one source** |
| **M7** | **Awakening gate = 5★ + Lv.30**, stated in 2021. | §2.3 | A second post-2019 source would move this from "historical community evidence" to era-anchored evidence |
| **M8** | **Transcendence magnitude ≈ 5–8%** (third-hand player guess). | §2.3, F4 | A first-hand measurement would materially constrain the RankUp fixture in `AGENTS.md` §29 |
| **M9** | **`share_en/1494773` "Damage Calculation"** — still uncaptured, and now known to be a *different id* from `forum_en/192349`. | §1.5 | Try archive.today / Common Crawl, or the "Cayenne Pepper" author's repost. The vendor's four-factor shape (§1.9.1) is the best substitute found so far |
| **M10** | **A second community wiki**: `blustone.wikia.com` ("never went anywhere") and an **Amino** wiki, both named by the vsFan author. | §1.9.5 | One archive probe each. §1.9.5 is the worked example of why a dead wiki's *own announcement* is worth reading first |
| **M11** | **Unmined `[Notice]` sub-series** recovered incidentally: parts 5, 21, 23, 24, 25, 26, 28, 29, 30 and the Background Collection. Several were truncated mid-title. | §1.9.1 | Read those posts in full; they are the continuation of the official **hunter-release ledger** and would extend Anemone/Leon/Bella/Teresa with more dated ★4 confirmations |

