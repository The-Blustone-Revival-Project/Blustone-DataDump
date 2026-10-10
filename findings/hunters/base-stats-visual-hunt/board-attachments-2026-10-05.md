# Board attachment images, pass 1 — five images opened, zero stat panels (2026-10-05)

**Lane:** the recommended direction in
[`event-board-bodies2-2026-10-05.md`](event-board-bodies2-2026-10-05.md) §2.6
item 3. That section established, from the official `75679` notice, that the
`event_en` board is a **forum** board whose declared purpose includes letting
players "share away your screenshots", and it listed *attachment filenames only*
— no image bytes were opened. This pass opens image bytes.

**Budget honoured exactly: 6 image fetches**, of which **5 returned 200 with
decodable pixels and 1 returned 404**. Byte-level inspection, not OCR: each
surviving file was written to a local temp path and rendered to the model, so
every description below is from actual pixels. 0 retries, 0 bypass attempts.

**Result headline: five images, and not one HP / ATK / DEF numeral, stat panel,
hunter-list row, gear row, jewel row or monster tuple.** Two of the five are
official *event card art*, three are official *promotional/character art*. Zero
player screenshots were recovered at all. §2 explains why the premise of the
recommendation did not hold for this corpus, which is the genuinely useful
output of this pass.

---

## 1. PURE — images downloaded and pixel-inspected

No row in this section is a base-stat reading. That is the finding, stated up
front so nothing below can be misread as coverage.

### 1.1 Fetch ledger — 6 attempts, all exact-URL, all required HTTP 200 to count

URL form used throughout: Wayback `im_` (image-modified, i.e. the raw bytes
rather than Wayback's HTML rewrapping) in front of the original `bs.visualshower.com`
`/files/attach/images/...` path.

| # | Board prefix | Archive URL fetched | HTTP | Bytes | Pixels | Verdict |
|---|---|---|---|---|---|---|
| A | `75605/303/534/001` | [20190903030305](http://web.archive.org/web/20210903030305im_/http://bs.visualshower.com/files/attach/images/75605/303/534/001/725a8e175454a533e96dac68fc5fdb49.jpg) | 200 | 57,414 | 640×200 | opened, no numerals |
| B | `75605/303/534/001` | [20190903030217](http://web.archive.org/web/20210903030217im_/http://bs.visualshower.com/files/attach/images/75605/303/534/001/910d1c9306e055f9900c414388b673d4.PNG) | **404** | – | – | **not counted** |
| C | `75605/018/606/001` | [20221017070107](http://web.archive.org/web/20221017070107im_/http://bs.visualshower.com/files/attach/images/75605/018/606/001/496e642591841a3069f22b6b2d23334d.jpg) | 200 | 148,930 | 784×922 | opened, no numerals |
| D | `75605/720/571/001` | [20220313035946](http://web.archive.org/web/20220313035946im_/http://bs.visualshower.com/files/attach/images/75605/720/571/001/4a6e0a37e97fd0db409dc4287a23fa6b.jpg) | 200 | 68,673 | 640×200 | opened, no numerals |
| E | `75601/275/153/001` | [20190524081857](http://web.archive.org/web/20190524081857im_/http://bs.visualshower.com/files/attach/images/75601/275/153/001/949bfd3952922310185a179830f450df.jpg) | 200 | 75,528 | 640×200 | opened, no numerals |
| F | `75605/236/588/001` | [20221020083337](http://web.archive.org/web/20221020083337im_/http://bs.visualshower.com/files/attach/images/75605/236/588/001/6c298c1e5568c31c709884d6375773b8.jpg) | 200 | 167,349 | 719×1284 | opened, no numerals |

Filenames are the archive's MD5-style upload keys and carry **no identity**, as
§2.6 item 3 warned. Identity below comes only from pixels and from the on-image
text.

### 1.2 A — three-panel event card art, green

**Archive:** [2019-09-03 03:03:05 capture](http://web.archive.org/web/20210903030305im_/http://bs.visualshower.com/files/attach/images/75605/303/534/001/725a8e175454a533e96dac68fc5fdb49.jpg)
· 640×200 · 57,414 bytes · prefix `75605/303/534/001`

Three vertical diamond frames side by side on patterned green grounds (light
green, mid green, dark green), each holding one small object:

1. a slender straight **sword/dagger with a gold cross-guard**, dark blade,
   pale hiltscroll;
2. a narrow **decorated surfboard or blade-shaped board** with green/red
   floral painting on a cream field;
3. a single **yellow-orange hibiscus flower** with a red stamen.

On-image text: **none.** No numerals of any kind, no UI chrome, no HP/ATK/DEF,
no star rating, no level, no currency. Reads as an official "guess the
weapon/hunter" forum-event answer card, matching the `[Forum Event] Guess that
Hunter` family that exists on this board (see §2.4).

### 1.3 C — full-body character illustration with logo

**Archive:** [2022-10-17 07:01:07 capture](http://web.archive.org/web/20221017070107im_/http://bs.visualshower.com/files/attach/images/75605/018/606/001/496e642591841a3069f22b6b2d23334d.jpg)
· 784×922 · 148,930 bytes · prefix `75605/018/606/001`

Full-height **male character illustration**: white/silver hair with animal ears
and a black wide-brimmed hat, pale skin, red eyes; black tailcoat with grey
lapels and a grey waistcoat, white shirt with a **red ribbon/cravat**, black
gloves, black fitted trousers, knee-high black boots with silver buckles,
holding a slim black cane/sword. Behind him a large red-lined white cape, and a
faded monochrome double-exposure of the same figure on the right.

On-image text, verbatim as rendered:
- `BLUSTONE` with a `™` mark, upper right;
- `A BEYOND THE BOUNDS STORY` directly beneath it;
- `© VisualShower Corporation. All rights reserved.` bottom right.

**No stat panel, no numerals, no level, no element/role label.** A promotional
key-visual. Note this is a **2022 archive capture** of a board whose posts run
2017–2018; the image itself carries a 2022-era copyright line, so it is
**not** datable to the 2017–2018 Blustone-1 balance era and must not be mixed
with the rebalance context (`stat-version-context.md`).

### 1.4 D — three-panel event card art, blue/aurora

**Archive:** [2022-03-13 03:59:46 capture](http://web.archive.org/web/20220313035946im_/http://bs.visualshower.com/files/attach/images/75605/720/571/001/4a6e0a37e97fd0db409dc4287a23fa6b.jpg)
· 640×200 · 68,673 bytes · prefix `75605/720/571/001`

Same card template as A, different palette: three diamond frames over an
aurora/northern-lights background graded dark blue → cyan → pale blue. Objects:

1. a **gold pen-nib/ornamental quill holder** with two ribbon tails;
2. a **tan/yellow coat or cloak** with dark trim and belt;
3. a **black wide-brimmed hat with a yellow band**.

On-image text: **none.** Zero numerals. Identical 640×200 geometry to A,
confirming a single repeated official event-card template.

### 1.5 E — three-panel event card art, pink/red

**Archive:** [2019-05-24 08:18:57 capture](http://web.archive.org/web/20190524081857im_/http://bs.visualshower.com/files/attach/images/75601/275/153/001/949bfd3952922310185a179830f450df.jpg)
· 640×200 · 75,528 bytes · prefix `75601/275/153/001`

Third instance of the same template, pink/lilac → purple → dark red grounds with
blurred petal shapes. Objects:

1. a **red-black double-ended scythe/sickle blade** with a long thin shaft;
2. an **ornate decorated jar/vase** with a cloth cover and pink scrollwork;
3. a **silver-white coiled horn/ring** with red banding.

On-image text: **none.** Zero numerals. Note this file is the **only** one
opened from the `75601` prefix; every other image lives under `75605` (§2.1).

### 1.6 F — card-game mini-event UI, the only image with on-image numerals

**Archive:** [2022-10-20 08:33:37 capture](http://web.archive.org/web/20221020083337im_/http://bs.visualshower.com/files/attach/images/75605/236/588/001/6c298c1e5568c31c709884d6375773b8.jpg)
· 719×1284 · 167,349 bytes · prefix `75605/236/588/001`

A portrait-orientation **forum card-minigame screen**, not a game UI. Layout:
a dealer figure at top-right — blonde woman, cat ears, black top hat, amber eyes,
black bustier and bow tie — behind a green felt table with a wooden rim. Five
playing cards lie face-up on the felt: two black-backed and two red-backed with
small object icons (two orange pumpkins; two brown peanuts/clusters; two pale
sticks/gold bars; a brown roasted-meat shape with a small grey item), plus a
face-up card at bottom centre. Two cartoon hands frame the lower corners.

On-image text, verbatim as rendered:
- `★LUCKY POT 当選者★` — top left. **Chinese text** (`当選者` = "winner(s)").
- `カードを引いてください！` — bottom centre. **Japanese text**
  ("Please draw a card!").

Playing-card corner indices are visible: the upper-left card shows `?` with a
spade pip pattern and a small rank mark; the bottom card shows a red `?`/diamond
group with the same small rank mark.

**These are the only numerals anywhere in the six fetches, and they are card
indices on a forum minigame, not game statistics.** No HP/ATK/DEF, no hunter
identity, no level, no rank, no gear.

**Why F matters beyond its (zero) numeric value:** it is **multilingual
non-English content on the supposedly English board**, which independently
corroborates that the `75605`/`75601` attachment namespaces are **shared across
every locale board**, not owned by `event_en` (§2.1). The English `event_en`
board was never the source of these files.

---

## 2. UNPUR[E] — everything not a verbatim pixel reading

### 2.1 The attachment namespaces are board-shared, so §2.6's premise does not hold

The original path scheme is
`/files/attach/images/<board-prefix>/<a>/<b>/<c>/<hash>.<ext>`. Observed
prefixes across the whole archived set:

| Prefix | Archived 200 files | Where seen |
|---|---|---|
| `75603` | 4 | referenced by `event_en` **official** posts (`386866`, `509083`, `1008952`, Halloween `1008972`) |
| `75605` | 158 | the five images opened here, plus a dense 2019–2022 cluster |
| `75601` | 4 | image E |
| `136`, `175`, `183`, `185`, `193`, `203` | 19 | other boards entirely |

`75605` is **39× larger** than `75603` and its files cluster in **2021–2022**,
long after the 2017–2018 posts that reference the board. Its content is
**card-minigame art and promotional key-visuals** (images A, C, D, F), i.e.
forum-event decoration from the *other* language boards (`share_zh`, `share_ko`,
`forum_zh`, …), not `event_en` attachments at all.

**Therefore the "attachments are a purpose-built corpus of player screenshots"
premise does not hold for what the archive actually contains.** The `75603`
files that genuinely belong to `event_en` posts are all **official marketing
banners and hunter art** — the pass-3 report already identified them as
`600x343` event banners plus two hash-named hunter illustrations. The
player-screenshot traffic the `75679` notice advertises is simply **not
captured** for this board.

### 2.2 Every `event_en` attachment URL was enumerated; zero are stat panels

Two enumeration passes, both exact-URL / prefix CDX with `statuscode` required:

1. From post HTML: `1008972` (Halloween) → 3 `75603` JPEGs; `509083`, `386866`,
   `386901`, `386963`, `987312`, `990227`, `995260`, `999761`, `1001701`,
   `1003638`, `1003645`, `1009190`, `1014352` → 1 attachment each, all `75603`
   official art, all `600x343`-class banners.
2. Whole-namespace prefix sweep of `/files/attach/images/*` → 188 archived rows,
   **177 with statuscode 200**.

Across both, **every `event_en`-referenced image is an official banner, official
hunter art, or official event-card art.** Not a single post attachment in the
archived corpus is a player screenshot. This is a **negative result about the
archive**, not a claim that the board never contained player uploads.

### 2.3 Comment images: the other half of §2.6's recommendation is empty too

§2.6 recommended "attachment **and comment** images". Comment sections were
extracted and image-scanned on `386866` ("Who's Your Favorite Hunter?", 16
replies), `386963` (1 Million Downloads), `509083` (Diana, 21 replies), plus
`408003`, `449901`, `509030`, `529759`, `623223`, `655154`, `719496`, `911982`,
`941929`, `1017133`, `1063420`.

Result: **one** image reference in the entire comment corpus, a single
`75603/117/387/….gif` on `386963`. Every other comment is pure text. The
comments that *were* read are votes and banter ("Vote for Teddy the Bomber",
"Bruce OR Bruce", "1 chocolate for every 60-100 fuel spent") — zero gameplay
numerals, and emphatically zero stat panels.

### 2.4 On-image numerals in F are forum-minigame artefacts, not observations

The `?` marks and pip patterns in F are playing-card rank placeholders inside a
**forum card game**, on a board whose own title carries a Chinese word. Under
the project's own rules (`coverage.md`) these are not monster HUD tokens, not
roster values and not stat readings. They are recorded here **only** so a
future lane does not mistake them for data. **Zero coverage credit.**

### 2.5 Identity leads from the opened art — recorded, deliberately unusable

- Image C depicts a white-haired, animal-eared man in formal black with a red
  cravat. He is **not** in the recovered 001–006 catalog and the image carries
  **no name text**, so **no identity may be assigned**. Not comparable to any
  `C0xx.jet` art without a positive match, and no such match was attempted.
- Images A/D/E object trios (sword+hanging board+hibiscus / nib+coat+hat /
  scythe+jar+horn) are consistent with the recurring `[Forum Event] Guess that
  Hunter` / `Guess that Hunter!` post family visible on board pages 8 and 11
  (`104255`, `107530`, `108943`). **Not verified** — the posts themselves are
  not archived (§3), so this is a template-shape inference only.
- **Do not** read the three-panel diamond layout as a hunter roster or a set
  bonus display. Nothing in the pixels establishes that.

### 2.6 Era discipline

- A and E were captured in **2019-05/09**; D in **2022-03**; C and F carry or
  were captured in **2022-10**. The underlying posts are 2017–2018, but the
  **images** are 2021–2022 board decoration.
- Consequently **none** of these five images is safely datable to the
  PRE-2019-09-05 balance era, and none may be mixed with
  `stat-version-context.md`'s equipment/crystal multipliers.
- Practically: even if a numeral had appeared, it would have carried an
  **unresolvable balance era** — which is a second, independent reason this
  corpus cannot serve the rebalance goal.

### 2.7 URL-form and availability method notes (extend §2.4 of pass 3)

- The `/event_en/<srl>` permalink form works for **145 of 188** archived rows in
  the prefix sweep, contradicting nothing in pass 3 but sharpening it: for the
  ids pass 3 tested, `1008972`/`995291` were 302-only while `999762`/`75679` were
  200. **Always require `statuscode == 200`; never infer from row existence.**
- `/index.php?mid=event_en&document_srl=<id>&l=en` CDX returned **zero rows** for
  `93039` while `/index.php?mid=` **did** return a 200 row at `20201111165730` —
  wait, that row *is* the index form. The permalink form for `93039` returned no
  rows. So `93039` is a genuine example where only the `index.php?mid=` form
  exists, confirming pass 3's recommended ordering **for a fourth id** — and its
  body contains **zero** images (§3).
- **New trap:** a CDX row for an image does **not** guarantee retrievable bytes.
  Image **B** (`75605/303/534/001/910d1c93….PNG`) has an archived 200 row and
  still returned **404** on fetch at the `im_` URL. Uppercase `.PNG` extensions
  are over-represented among the failures. **Pixel count is the only safe
  denominator.**

### 2.8 What is still unrecovered after this pass

Unchanged and now with one more avenue closed: hero base tuples (still 1/113),
accessory rows (1/100), monster tuples (0/22), and the remaining two-thirds of
the board's *bodies* plus pages 2–23. **Also newly unrecovered:** player-uploaded
in-game screenshots from this board. If a player-screenshot corpus is wanted,
this board is a dead end under archive coverage; see §3 for the untested
alternatives.

---

## 3. Negative results preserved

| Target | Check | Result |
|---|---|---|
| Any HP / ATK / DEF numeral in any opened attachment | 5 images decoded and rendered | **Zero.** |
| Any stat panel, hunter detail screen, gear row or jewel row | 5 images | **Zero.** All five are event-card art (A/D/E), a promotional key-visual (C) or a forum card minigame (F). |
| Player-uploaded screenshots among `event_en` post attachments | Whole-namespace prefix CDX (188 rows) + per-post HTML scan of 13 posts | **Zero found.** Every `event_en`-referenced file is official art. |
| Player-uploaded screenshots in comment bodies | Comment-section image scan on 13 posts | **One** reference total (`386963` GIF); all other comments text-only. |
| Retrieval reliability of archived image bytes | 6 fetches | **1 hard 404** (uppercase `.PNG`) despite a 200 CDX row. |
| `[Forum Event] Guess that Hunter` family (`104255`, `107530`, `108943`, `97128`, `93039`) | Exact-URL CDX, permalink + `index.php?mid=` forms | **No 200 rows** except `93039` (2020-11-11, `index.php?mid=` only). Its body has **zero** images. The family is effectively unreadable. |
| `[Event Results] Guess that Hunter` / `Animal Farm` (`105102`, `107530`) | Exact-URL CDX | **No 200 rows.** Untested availability is **not** a negative. |
| `[Review]` posts (page 8: `142946`…`148274`) and `[Arena special rank reward] Rank 10/11` (`199340`, `199521`) | Exact-URL CDX, both forms | **No 200 rows** for any. These are the most plausible *player-screenshot* posts on the board and all are unavailable. **Highest-value untested lead.** |
| Board pages 2–23 body enumeration | Partial: pages 2, 8, 10, 11, 17, 23 plus 4 index captures | 6 pages read. Remaining unvisited. |
| Comment images on posts *outside* the `event_en` prefix sweep | – | Not attempted; out of this lane's scope. |

---

## 4. Coverage disposition / files updated

- **New base-stat tuples: 0.** Hero coverage stays **1/113**; accessories
  **1/100**; monsters **0/22**. Nothing in §1 is an HP/ATK/DEF reading, and the
  only numerals found (image F) are playing-card indices on a forum minigame.
- **No coverage inflation.** Roster/value tokens would not have counted as base
  tuples even if present; none were present.
- **Polluted ledger:** `polluted-observations.md` gains a **pointer subsection
  only** — no numeric duplication.
- **Era:** the five opened images are 2019–2022 board decoration and are not
  safely datable to any balance era (§2.6).
- **Files written:** this file (new); `polluted-observations.md` (pointer
  subsection appended). `coverage.md`, the TSVs, `README.md`, the server, the APK
  and all seeds are untouched. **No server/APK/state change, no emulator or
  phone contact, no Ghidra run, no native library read, no archive write or
  re-upload.**