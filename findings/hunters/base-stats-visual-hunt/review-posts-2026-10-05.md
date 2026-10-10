# `[Review]` posts and the `share_en` screenshot board — definitive census, zero pixels (2026-10-05)

**Lane:** the "HIGHEST-VALUE UNTRIED LEAD" recorded in
[`board-attachments-2026-10-05.md`](board-attachments-2026-10-05.md) §3: the
`[Review]` posts on `event_en` page 8 (`142946`…`148274`) and
`[Arena special rank reward] Rank 10/11` (`199340`, `199521`).

**Budget honoured exactly: 8 fetches, 0 retries, 0 bypasses.** Ledger in §1.1.
Seven are CDX index queries or post bodies; **one** returned a server error
(§1.1 row 7). **No image was fetched, so this pass contributes zero new pixel
evidence** — stated up front so nothing below can be misread as coverage.

**Headline, three findings:**

1. **Every `[Review]` post and both Arena posts are genuinely, definitively
   absent from the archive — under *all three* URL forms and *every* status
   code, not merely "no 200 row" as the prior pass recorded.** This upgrades a
   soft negative into a settled one (§1.3).
2. **The prior pass's lead was partly mis-attributed.** `148274` — cited as a
   `[Review]` post — is actually titled **"My guess"** and *is* archived. The 15
   real `[Review]` ids are all in `142946`–`147073`, and none is archived. The
   prior range's upper endpoint was simply the last row on the list page, not a
   `[Review]` post (§2.1).
3. **A much better corpus was found and left unopened, honestly because the
   budget ran out rather than because it was rejected.** `share_en` post
   `197745` ("Guide to Blustone") is a player-authored guide carrying **11 real
   in-game screenshots** in attachment namespace `565/745/197/`, which the
   prior pass never enumerated. §3.

---

## 1. PURE — verbatim pixel/body readings and exact census facts

Nothing in §1 is a base-stat reading. There are **no HP/ATK/DEF values** in this
pass because **not one image was opened**.

### 1.1 Fetch ledger — 8 attempts, HTTP status recorded for each

| # | Purpose | URL / query | HTTP | Bytes | Outcome |
|---|---|---|---|---|---|
| 1 | Domain census (broad) | `cdx?url=bs.visualshower.com&matchType=domain&collapse=urlkey&filter=statuscode:200&limit=30000` | 200 | 4,240,518 | 30,000 rows — **hit the limit, TRUNCATED** (see §2.4) |
| 2 | `event_en` census, 200 only | same + `filter=original:.*event_en.*&limit=20000` | 200 | 125,870 | **1,029 rows, not truncated** |
| 3 | `event_en` page-8 body | `web/20180403061645/http://bs.visualshower.com:80/index.php?mid=event_en&page=8` | 200 | 64,500 | list page, 23 titles recovered |
| 4 | `event_en` census, **all statuses** | same as #2 minus the `statuscode` filter | 200 | 137,075 | **1,125 rows, not truncated** |
| 5 | Post body `148274` | `web/20180816232655/…:80/index.php?mid=event_en&document_srl=148274&l=en` | 200 | 80,533 | body read; title **"My guess"** |
| 6 | `share_en` census | `…&filter=original:.*share_en.*&limit=20000` | 200 | 103,121 | **833 rows, not truncated**; 105 distinct ids |
| 7 | `share_en` list pages | `filter=original:.*share_en(&[a-z_]+=[a-z]*)?$\|.*share_en\?.*` | **500** | – | **server error — regex alternation rejected. Not counted as data.** Superseded: the needed rows were already in #6 |
| 8 | Post body `197745` | `web/20180227140354/http://bs.visualshower.com:80/share_en/197745` | 200 | 105,467 | **"Guide to Blustone"**, 11 screenshot attachments |

**No `302` or `404` was returned to an image fetch in this pass, because no
image fetch was attempted.** The prior pass's warning that *a CDX row does not
guarantee retrievable bytes* (§2.7 there) therefore remains **untested for
`565/745/197/`** — a live risk for the next lane, not a settled fact.

### 1.2 The `event_en` census, complete and untruncated

Query #4 (all statuses, `collapse=urlkey`) returned **1,125 rows**:

| Status | Rows |
|---|---|
| `200` | 1,013 |
| `302` | 112 |

Extracted distinct post ids: **267**. These cover board list pages, post bodies
(`/event_en/<srl>`) and permalink bodies (`index.php?mid=event_en&document_srl=…`),
including `dispBoardReplyComment` rows. The board list pages `page=1`…`page=24`
are all archived in both `?mid=event_en&page=N` and `?mid=event_en&l=en&page=N`
forms, so the board's own pagination is fully recoverable.

### 1.3 `[Review]` and Arena posts: the definitive negative

Exact-url CDX had previously reported "no 200 rows". Query #4 removes the
remaining doubt by covering **all statuses and all URL forms** at once:

| Post | Title as listed on page 8 | Rows in archive (any status, any form) |
|---|---|---|
| `147073` | `[Review] My Blustone Review` | **none** |
| `145851` | `[ Review ] : Thank You Enheim` | **none** |
| `145677` | `[Review] Getting addicted to this game!` | **none** |
| `145529` | `[Review] The Real Spook of Blustone's Guestbook: Checking In and Never Checking Out` | **none** |
| `145458` | `[Review] Blustone Review Event` | **none** |
| `144946` | `[Review] My review on an awesome game know as Blustone` | **none** |
| `144722` | `[Review] why everyone should play Blustone!` | **none** |
| `144703` | `[Review] My quick twitter review` | **none** |
| `144342` | `[Review] Spooky Blustone` | **none** |
| `144177` | `Review` | **none** |
| `144053` | `[Review] BluStone Review (Mostly just some quick thoughts)` | **none** |
| `143910` | `[Review] My New Favorite Mobile Game!` | **none** |
| `143356` | `[Review] Guestbook full of spook review` | **none** |
| `143120` | `[Review] My experience with Blustone` | **none** |
| `142946` | `[REVIEW] BLUSTONE REVIEW INSTAGRAM` | **none** |
| `199340` | `[Arena special rank reward] Rank 10/11` | **none** |
| `199521` | `[Arena special rank reward] Rank 10/11` | **none** |

**17 of 17 absent. Zero images, zero bodies, zero comments recoverable.**
`[Review]` is the single most-cited post *title family* on page 8 (15 of 23
rows) and the archive captured **none** of it. This is a hard archival negative,
not an untried lead, and it should not be re-attempted without a new source.

### 1.4 Page-8 list body, transcribed verbatim

From fetch #3, the 23 rows in board order, titles exactly as rendered:

```
623645 [Event] Lottery Mouse Likes Walnuts
608365 [Event] April's Recruiting HOT TIME!
608338 [Event] Unbelievable April Fool's Day Event!
607705 [Event] April Limited Package
607643 [Event] Estelle…Ts Special Offer
579793 [Event] Special Search for Papillon!
579746 [Event] Favorite Female Hunter Results
579733 [Event] Catch the New Hunter Bright!
75679  [Notice] How to Use the Events Section
148274 My guess
147972 My guess
147963 1.05/2.04
147784 1. 05/ 2. 04
147335 1.06/2.05
147073 [Review] My Blustone Review
145851 [ Review ] : Thank You Enheim
145677 [Review] Getting addicted to this game!
145529 [Review] The Real Spook of Blustone's Guestbook: Checking In and Never Checking Out
145458 [Review] Blustone Review Event
144946 [Review] My review on an awesome game know as Blustone
144722 [Review] why everyone should play Blustone!
144703 [Review] My quick twitter review
144342 [Review] Spooky Blustone
144177 Review
144053 [Review] BluStone Review (Mostly just some quick thoughts)
143910 [Review] My New Favorite Mobile Game!
143356 [Review] Guestbook full of spook review
143120 [Review] My experience with Blustone
142946 [REVIEW] BLUSTONE REVIEW INSTAGRAM
```

The list page contains **no content thumbnails at all** — only site chrome
(`pv-account-title` sprites, `layouts/sr/img/*`, and XE template icons). So the
board list can never itself yield a stat panel.

### 1.5 Post body `148274` — read in full, and it is not a `[Review]` post

Title: **`My guess - Blustone`**. Dated `2017.10.17 11:27`, `Views 30`,
`Votes 0`, `Reply 1`.

Body text, verbatim as rendered:

```
My guess
[1]
Denner
Lv. 1
0/100
```

The only image is a **90×90 avatar thumbnail**,
`/files/thumbnails/382/148/90x90.crop.jpg` — an XE profile thumbnail, not
game content. **No gameplay screenshot, no stat panel, no numerals beyond the
author's own `Lv. 1` / `0/100` guess entry.**

`Denner` is a name not present in the recovered 001–006 catalog, so **no
identity may be assigned**, and `0/100` is a forum-guess value with no stat
meaning.

### 1.6 Post body `197745` ("Guide to Blustone") — 11 in-game screenshots

Fetch #8, `share_en/197745`, title **`Guide to Blustone - Blustone`**, dated
`2017.11.12 01:32`, `Views 1571`, `Votes 0`, `Reply 5`. Author signature:

```
Guide to Blustone [5]
Alaiko
Lv. 8 25/100
Cyana, Fin, KronX and Father are my hyper boosters
```

Opening text, verbatim:

> Hello there, new player and welcome to the world of Blustone! It might be a
> little intimidating and confusing being in that strange land at first. I will
> try to make this guide as detailed and comprehensive as possible so that you
> will have some sense of how to play the game in both PvE and PvP. 1. PvE
> Section You start off your journey by beginning with PvE. For the PvE section,
> there are three main activities you can engage in - cruises, abysses, and
> hidden and normal …

**This is a player-authored gameplay guide, i.e. exactly the document class that
tends to embed stat panels, hunter lists and gear screens.** It references
**eleven distinct in-game screenshots**, all under attachment prefix
`565/745/197/`:

| # | Original filename | Implied subject (from filename/alt only — **no pixels seen**) |
|---|---|---|
| 1 | `1c121be82d8bfcf6f5ab9e704adb1d07.png` | unknown |
| 2 | `41fd313eed657cfd55a0c1968678dc4f.png` | unknown |
| 3 | `44c11f2135810d1b39c8646ff18f6785.png` | unknown |
| 4 | `5c3dc1b9bba2d43a3ac4cc7f9d529b2b.png` | unknown |
| 5 | `7c7ce8d6b217c490a75f87cc75c26377.png` | unknown |
| 6 | `9997745206a3c799fe23b1c3e8a9b652.png` | unknown |
| 7 | `9d762be979e9f465ee7b5a991d770294.png` | unknown |
| 8 | `a108de5ae785015eb93dfe436b4a5661.png` | unknown |
| 9 | `b54f4b1bb263bf863200f61539122323.png` | unknown |
| 10 | `c74645562f4808918731bb2ba9fae268.png` | unknown |
| 11 | `d08e6de796029e3efe615dc2e98a4de6.png` | unknown |

Plus these **named** in-image filenames, which are the guide's own section
captions and are the only subject hints available:

```
Arena.png            Club.png            Cruise_beginning.png
Cruising.png         Gym.png             Ruins.png
Screenshot_2017-11-11-07-17-55.png
Screenshot_2017-11-11-14-45-20.png
Screenshot_2017-11-11-14-46-11.png
Screenshot_2017-11-11-14-46-43.png
Screenshot_2017-11-11-15-07-52.png
```

**Honest status: none of these 11 (or 16, counting the named ones) images was
fetched or rendered.** `Gym.png`, `Arena.png` and `Club.png` are the most likely
to contain stat panels by subject, but that is a **filename inference, not a
pixel reading**, and it is recorded as a lead only (§3).

---

## 2. UNPUR[E] — everything that is not a verbatim reading

### 2.1 Correction: `148274` was mis-attributed, and the prior negative was under-specified

`board-attachments-2026-10-05.md` §3 lists "`[Review]` posts (page 8:
`142946`…`148274`)". Page 8 (fetch #3) shows **`148274` is "My guess"**, a
member of the recurring *Guess that Hunter* family — not a review. It is also
**archived with a 200 body**, which I fetched and read (§1.5).

So the prior pass's "no 200 rows for any" was **wrong about `148274`** while
being right about the other ids. Two distinct causes, and both matter:

1. **Mis-attribution:** the range endpoint was the last row on the list page.
2. **URL-form blind spot:** archived URLs are stored **with an explicit `:80`**
   (`bs.visualshower.com:80/index.php?mid=event_en&document_srl=…`). The prior
   pass's exact-url queries omitted the port. CDX normally canonicalises this,
   so it is *not* proven to be the cause — but it is the one form difference
   visible in the census, and it is why this pass used a domain-wide filtered
   sweep instead of exact-url lookups.

The net effect is the same for the goal — 15 of 15 real `[Review]` posts really
are absent — but the evidence is now **status-independent and form-independent**,
not "no 200 row seen".

### 2.2 `[Review]` posts would probably not have helped even if archived

An honest reading of the titles: these are **App Store / Google Play review
posts** ("Getting addicted to this game!", "My quick twitter review",
"BLUSTONE REVIEW INSTAGRAM", "why everyone should play Blustone!"). They are
player *review copy*, not gameplay documentation. The prior pass ranked them the
"classic stat-panel source"; the titles suggest that ranking was optimistic.
`share_en/197745` — a **guide** — is a structurally better bet, which is why §3
redirects there. This is a judgement, not a fact about unarchived content.

### 2.3 A second attachment namespace exists and the prior sweep never touched it

The prior pass swept `/files/attach/images/*` only. Two further namespaces are
present in the archived set (from the cached censuses, §1.1 rows 1/6):

| Namespace | Rows seen | What it is |
|---|---|---|
| `/files/attach/images/<prefix>/…` | 178 (truncated sweep) | post attachments — the prior pass's whole corpus |
| `/files/thumbnails/<a>/<b>/001/90x90.crop.jpg` | 4 | XE **profile** avatars, always `90x90.crop.jpg` |
| `/files/cache/…` | 41 | XE internal cache, not content |

`/files/thumbnails/` is **useless for this goal** — `90x90` crops cannot hold a
stat panel. Recording it so a future lane does not re-sweep it expecting
content. Note the attachment prefixes seen in the truncated broad sweep are
`175` (365 rows), `136` (243), `75603` (36), **`565` (27)**, `173` (9), `195` (1)
via `procFileDownload&module_srl=…`; **`565` is `share_en`'s own prefix** and
is exactly where the 11 guide screenshots live.

### 2.4 Method limits of this pass, stated so they are not over-read

- **Fetch #1 was truncated at my own 30,000-row limit** and `event_en` rows
  appeared as late as index 28,925. Every `event_en` conclusion here therefore
  rests on fetches **#2 and #4**, which were untruncated (1,029 / 1,125 rows).
  Do not cite the broad sweep for any `event_en` claim.
- **`collapse=urlkey` returns one row per URL**, so per-id multiple-capture
  counts are unavailable here. Fine for existence, not for capture history.
- **`share_en` list-page pagination is incomplete:** `page=1`…`page=9` exist in
  two param forms, but pages **10+ are absent**, so the board's full post list is
  **not** recovered — only the 105 ids that happen to have archived bodies.
- **No OCR was performed and no image was opened.** Every subject attribution in
  §1.6 is filename-based and explicitly labelled as such.
- The failed fetch **#7** contributed nothing; all `share_en` list-page facts
  cited here come from fetch #6's cache.

### 2.5 Era note for any future use of the `share_en` guide

`197745` is dated **2017-11-12**, i.e. **pre-2019-09-05** and therefore in the
balance era described by [`stat-version-context.md`](stat-version-context.md).
If its screenshots do contain stat panels, they belong to the **older**
equipment/crystal balance and **must not** be mixed with post-2019 values. This
makes the corpus valuable *and* easy to misuse.

### 2.6 Identity/level tokens in this pass, all unusable

| Token | Where | Why it is not coverage |
|---|---|---|
| `Denner`, `Lv. 1`, `0/100` | `148274` body | forum-guess entry; name not in recovered catalog; no gear context |
| `Alaiko`, `Lv. 8 25/100` | `197745` signature | author profile, not a hunter stat |
| `Cyana, Fin, KronX`, `Father` | `197745` signature | "hyper boosters" — team composition only, no stats |
| `1571` / `30` views, `0` votes | both bodies | forum counters |
| `2017.10.17`, `2017.11.12`, `2017.11.11` | bodies/filenames | dates |

**Zero base-stat tuples. Zero monster tuples. Zero accessory rows.** Hero
coverage stays **1/113**, accessories **1/100**, monsters **0/22**.

---

## 3. Recommended next lane (not attempted — budget exhausted)

**`share_en/197745`'s 11 screenshots, then a `share_en` sweep.** Concretely:

1. Fetch the 11 `565/745/197/*.png` files at
   `web/20180227140354im_/http://bs.visualshower.com/files/attach/images/565/745/197/<hash>.png`,
   requiring **HTTP 200 and decodable pixels** — the prior pass proved a 200 CDX
   row can still 404. **Pixel count is the only safe denominator.**
2. Prioritise `Gym.png`, `Arena.png`, `Club.png` by subject inference, but
   **verify by pixel, never by filename**.
3. Then sweep the other 104 archived `share_en` posts for the `565` prefix —
   the guide is very unlikely to be the only screenshot-bearing player post, and
   this board was **never enumerated** by any prior pass.
4. Record every reading with explicit identity / level / gear / jewel / skill
   state, and route anything ambiguous to `polluted-observations.md`.

Expected value: **materially higher than anything left on `event_en`**, which is
now exhausted for player screenshots (§1.3, and pass 3's §2.2).

---

## 4. Negative results preserved

| Target | Check | Result |
|---|---|---|
| Any `[Review]` post body (`142946`…`147073`, 15 ids) | Domain-wide CDX, **all statuses**, all 3 URL forms | **17/17 incl. Arena: zero rows.** Hard negative. |
| `[Arena special rank reward] Rank 10/11` (`199340`, `199521`) | Same | **Zero rows.** |
| Content thumbnails on `event_en` list pages | Page-8 body parsed | **None** — site chrome only. |
| Player screenshot in `148274` | Body fetched (200) | **None** — one 90×90 avatar thumbnail. Title is "My guess", not `[Review]`. |
| `share_en/197745` screenshots | Body fetched (200), **bytes not fetched** | **11 in-game screenshots referenced, 0 opened.** Unresolved. |
| `share_en` post corpus | CDX, all statuses | **105 distinct ids**, 833 rows — **never enumerated by any prior pass.** Unexploited. |
| `/files/thumbnails/` as a content source | Cached census | 4 rows, all `90x90.crop.jpg` avatars — **structurally incapable** of holding a stat panel. |
| Retrieval reliability of `565/745/197/` image bytes | Not attempted | **Untested.** Prior pass's "200 row ≠ retrievable bytes" risk still open here. |

---

## 5. Coverage disposition / files updated

- **New base-stat tuples: 0.** No image was opened. Hero **1/113**,
  accessories **1/100**, monsters **0/22** — unchanged.
- **No coverage inflation.** Filename-based subject guesses were explicitly
  excluded from §1 and quarantined in §3.
- **`polluted-observations.md` gains a pointer subsection only** — no numeric
  duplication, since there are no numeric readings to record.
- **Era:** the one genuinely promising corpus is **pre-2019-09-05** (§2.5) and
  must be read under that era's balance.
- **Files written:** this file (new); `polluted-observations.md` (pointer
  subsection appended). `coverage.md`, `README.md`, the TSVs, `server-ts`, the
  APK and all seeds are **untouched**. **No server/APK/state change, no emulator
  or phone contact, no Ghidra run, no native library read, no archive write,
  no re-upload, no login, no form submission.**