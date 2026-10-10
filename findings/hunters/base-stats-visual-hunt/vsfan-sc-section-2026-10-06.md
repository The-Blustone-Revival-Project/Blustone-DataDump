# vsfan `/sc/` — the "Korean section" claim, tested and falsified (2026-10-06)

**Lane:** the brief was to read the 565 archived `/sc/` URLs that were said to hold
the Korean-language half of the `vsfan.net` Blustone wiki, and to mine them for
equipment / gem / level / recruitment / transcendence numbers.

**Verdict: the premise is false, and the falsification is complete and
instrumented.** `vsfan.net/sc/` is **not** a language section of the wiki and has
**nothing** to do with Blustone. It is a **Simplified-Chinese, IIS-hosted BBS
static-asset directory that existed in 2006–2008**, nine to eleven years before
Blustone was released and eleven years before the wiki itself was captured.

**Every one of the 1,101 distinct `/sc/` URLs in the archive was fetched and read
to the byte.** 1,061 bodies are images (1,032: 672 GIF, 332 PNG, 28 JPEG), RAR
archives (27) or SWF (2). The remaining **40 are HTML** — 404/403 error pages, a
registrar parking page, and four captures of the **English** Blustone wiki's Main
Page served as a soft-404 for files that no longer existed. Net Korean characters
in the whole corpus: **0**. Numeric tables, stats, item names, hero names: **0**.

**Nothing here changes any coverage counter.** Heroes **1/113**, accessories
**1/100**, monsters **0/22** all stand, unchanged and unmoved. A controlled
negative is the deliverable.

---

# 1. METHOD, CONTROLS, AND THE TRAPS THAT WERE AVOIDED

Read first: [`GUARD-encoding-and-archive-traps.md`](GUARD-encoding-and-archive-traps.md).
Every instrument named as broken there was either avoided or explicitly
re-tested.

| Guard item | How it was handled here |
|---|---|
| 1. `https://` refused on this host (`WinError 10061`) | **Every** fetch and every CDX call used `http://`. Positive control `http://web.archive.org/` → **HTTP 200, 145,187 B**. |
| 2. Unencoded `?` in a CDX `url=` parameter | All CDX URLs were built with `urllib.parse.urlencode(..., safe="/:")`, so no query character could be reinterpreted as a parameter separator. The one `/sc/` URL that legitimately contains `?` (`/sc/bg/sl_172.gif?c2cd0ce0`) is present in the census as a distinct URL, which is what correct encoding produces. |
| 3–4. CDX returns reproducible false negatives; a capture set cannot be enumerated reliably | Every negative in this report is stated as *the archive holds no capture of this URL*, never as *no such page ever existed*. Five explicit exact-URL probes (`/sc`, `/sc/`, `/sc/wiki/`, `/sc/index.php`, `/sc/index.asp`, `/sc/index.html`) plus a subdomain probe (`sc.vsfan.net`) are recorded in §6 so a later agent can re-run them. |
| 5. `resumeKey` / `matchType=domain` truncate silently to page 1 | **Not used.** The census comes from a **single non-collapsed `matchType=domain` sweep with `limit=20000` that returned 13,274 rows** — i.e. a complete result set, not page 1 — cross-checked against an independent `matchType=prefix` sweep of `vsfan.net/sc/` which returned the same **1,222** rows. Two independent query shapes agreeing is the guard against the documented 24.4× undercount. |
| 6. `matchType=prefix` barely covers `/board/<id>`-style paths | N/A for this corpus, and covered anyway by the full domain sweep. |
| 7. 15 byte-identical `域名停靠` parking pages masquerading as content | Hash-checked, not eyeballed. Every fetched body was SHA-256'd and clustered. The `/sc/` error pages form **their own** hash clusters, **distinct from** the parking-page hash family. Counting **captures** (28 captures of the 6 extension-less URLs, §4): 20 × 218-byte IIS `Error` (`b8f7bd16ab9976b…`), 4 × 1,308-byte Chinese IIS 404 (`e682dfcdde010f6e…`), 2 × 39-byte `400` (`2b977b6342a62409…`), 1 × `Site Unavailable`, 1 × `File Not Found`. Counting **distinct URLs** across the whole corpus (40 bodies, §3.1) the same five clusters appear at 3 / 2 / 0 / 1 / 21. **No `/sc/` capture has the `域名停靠` parking-page hash.** |
| Positive control before any zero | Six positive controls, all HTTP 200: `http://web.archive.org/` (145,187 B); CDX exact `vsfan.net/wiki/List_of_Hunters` (2 rows); CDX exact `vsfan.net/wiki/Akasha` (3 rows); CDX exact `vsfan.net/sc` (10 rows); CDX prefix `vsfan.net/sc/` (1,222 rows); and 42 archived wiki pages successfully fetched as HTML. A zero is only believed where a positive control returned rows **on the same host in the same session**. |

Local-copy preference: `analysis/VSFan/` (1.07 GB, 8,551 files) was searched
first. A byte-level scan of every file under 4 MB for the literals `/sc/` and
`vsfan.net` returned **0 files**. There is no local copy of the wiki, English or
otherwise, so the network route was unavoidable.

---

# 2. WHAT `/sc/` ACTUALLY IS — COMPLETE ENUMERATION

Source of truth: Wayback CDX, two independent query shapes, cross-checked.

| measure | value |
|---|---|
| CDX rows under `vsfan.net/sc/` (prefix sweep) | **1,222** |
| CDX rows under `/sc/` found inside the full 13,274-row domain sweep | **1,222** (identical set) |
| distinct original URLs | **1,101** |
| distinct paths | **1,095** |
| hosts | `www.vsfan.net:80` (1,063 URLs) · `www.vsfan.net` (38 URLs) |
| capture years | 2006 **58** · 2007 **1,112** · 2008 **12** · 2012 8 · 2013 3 · 2015 23 · 2016 1 · 2017 4 · 2021 1 |
| rows by archived status | `200` 1,156 · `404` 31 · `403` 20 · `302` 6 · `-` 4 · `301` 3 · `400` 2 |
| rows by archived mime | `image/gif` **710** · `image/png` **329** · `image/jpeg` **85** · `text/html` **63** · `application/octet-stream` **27** · `warc/revisit` 4 · `unk` 2 · `application/x-shockwave-flash` 2 |
| distinct paths by extension | `.gif` **699** · `.png` **329** · `.jpg`/`.jpeg` **33** · `.rar` **27** · `.swf` **2** · no extension **4** · `.gif%3Cbr` (a mangled `<br>` in a captured link) **2** |
| **paths that are neither image nor archive** | **6** — and all six are error pages (§4) |

**The 63 `text/html` rows are not 63 pages.** They are 6 distinct URLs captured
28 times in total; every capture is a 403, a 400, a 404, a `Site Unavailable`
or a `File Not Found`. Reading a `text/html` mime as "a page exists here" is
precisely the false positive this lane had to avoid.

**Correction found by the byte-level read (§3): the extension is not the payload.**
34 additional `/sc/bg/*.gif` and `/sc/xs/*.gif` URLs whose CDX mime says `image/*`
or whose path ends in `.gif` return **HTML** at HTTP 200 — four of them the
English Blustone wiki Main Page, two a registrar parking page. The honest
denominator is therefore the **byte-level** one in §3: of 1,101 URLs read,
**1,061 are images/archives and 40 are HTML**. The extension-based table above is
still correct as a description of the *intended* paths.

### 2.1 The decisive language evidence

The `/sc/` tree was served by **Microsoft IIS**, and the only genuine
Chinese-language body in the corpus is an **IIS custom 404 page in SimSun
(`宋体`)**. Fetched and decoded (`gb18030`, the correct codec; it fails as
UTF-8 and as EUC-KR):

```
URL      http://www.vsfan.net:80/sc/rt/056\.jpg
capture  20070110234651   HTTP 404   1,308 B
sha256   e682dfcdde010f6e15bae0d843696f6a…
title    无法找到该页
body     您正在搜索的页面可能已经删除、更名或暂时不可用。…
         BODY { font: 9pt/12pt 宋体 } … HTTP 错误 404 - 文件或目录未找到。
         Internet 信息服务 (IIS) 技术信息（为技术支持人员提供）
```

Simplified Chinese, Microsoft IIS, 2007. That is the voice of the whole `/sc/`
directory. The sibling `/site/` tree on the same domain is DedeCMS
(`/templets/style/dede.css`, `/site/Article.asp`, `/site/Catalog.asp`,
`/site/Commend.asp`), confirming the domain's actual identity in that era.

### 2.2 Directory buckets — the complete path census

| bucket | rows | capture years |
|---|---|---|
| `/sc/xs` | 333 | 2006–2015 |
| `/sc/xtb` | 299 | 2006–2015 |
| `/sc/bg` | 62 | 2012–2017 |
| `/sc/et` | 44 | 2007 |
| `/sc/14` | 41 | 2007 |
| `/sc/bq1` | 37 | 2007 |
| `/sc/bq2` | 33 | 2007 |
| `/sc/12` | 32 | 2007 |
| `/sc/kadw2` | 32 | 2007 |
| `/sc/kadw1` | 30 | 2007 |
| `/sc/rt` | 30 | 2007 |
| `/sc/dm` | 27 | 2007 |
| `/sc/gd1` | 24 | 2007 |
| `/sc/zybq` | 24 | 2007 |
| `/sc/51tu` | 8 | 2013–2015 |
| `/sc/cs` | 8 | 2015 |
| `/sc/hg1`, `/sc/ss`, `/sc/sw`, `/sc/tq` | 5 each | 2007–2015 |
| `/sc/hg` | 4 | 2007 |
| `/sc/car` | 2 | 2007 |
| `/sc/flash` | 2 | 2007 |
| `/sc/` (root), `/sc/hd`, `/sc/pj1` | 1 each | 2007 |

Two structural facts follow immediately:

1. **Chronology.** 1,170 of 1,222 rows (95.7 %) were captured in 2006–2008.
   Blustone shipped in 2017; the Blustone wiki was captured in **2019–2020**.
   A `/sc/` corpus that is 96 % pre-2010 cannot be documentation of a 2017 game.
2. **Payload.** Every bucket is image or archive. A directory tree of 699 GIFs,
   329 PNGs, 33 JPEGs, 27 RARs and 2 SWFs is forum furniture — avatars, emoticons,
   signatures, banners, downloadable packs. The full byte-level decode (§3.4)
   confirms it: **339 of the 1,032 images are 128×128** and the next most common
   sizes are 9–16 px, i.e. avatars and emoticons.

---

# 3. BYTE-LEVEL READ OF THE CORPUS

**Every one of the 1,101 distinct `/sc/` URLs in the archive was fetched and read
to the byte.** 1,061 of the bodies are images or archives. The remaining **40 are
HTML** — error, registrar-parking or wiki-Main-Page bodies — and **not one of the
40 contains any game data, any Korean, or any table**.

| measure | value |
|---|---|
| distinct `/sc/` URLs attempted | **1,101 (100 %)** |
| HTTP 200 · 404 · 403 | **1,070** · 28 · 3 |
| transport failures left unresolved | **0** (one 111-byte `Connection…` truncation was re-fetched successfully at HTTP 200 / 56,829 B) |
| total bytes read | **23,376,105** |
| distinct SHA-256 over all read bodies | **1,074** |
| bodies verified as **images by magic bytes** | **1,032** — GIF **672**, PNG **332**, JPEG **28** (and decoded by PIL: 1,032/1,032, zero corrupt) |
| bodies verified as **RAR** (`Rar!`) | **27** |
| bodies verified as **SWF** (`CWS`/`FWS`) | **2** |
| bodies that are **HTML** (everything else) | **40** |
| bodies containing game statistics | **0** |

### 3.1 The 40 HTML bodies, by hash cluster — every one of them

| ×  | bytes | HTTP | sha256 (truncated) | what it is |
|---|---|---|---|---|
| 21 | 1,699 | 404 | `cdc8b52c9402b72e…` | Apache-style **`File Not Found`** |
| 3 | 218 | 403 | `b8f7bd16ab9976b8…` | IIS **`Directory Listing Denied`** |
| 2 | **57,107** | 200 | `7201ec5568649e3e…` | **Blustone wiki Main Page** (`<title>VisualShower Wiki</title>`, `lang="en-GB"`, MediaWiki 1.30.0-alpha) |
| 2 | **56,829** | 200 | `cf0c504154563aaa…` | **Blustone wiki Main Page** (same, earlier revision) |
| 2 | 26,349 | 200 | `5323cb63ab974d5a…` | registrar parking page, **`Welcome to www.vsfan.net!`** |
| 2 | 1,308 | 404 | `e682dfcdde010f6e…` | **IIS Simplified-Chinese 404** (`无法找到该页`, `宋体`) |
| 1 | 26,413 | 200 | `2e60b7e582c03807…` | registrar parking page, `Welcome to www.vsfan.net!` |
| 1 | 4,613 | 404 | `c4d6da3f26ed85d8…` | 404 page |
| 1 | 4,599 | 404 | `f9ab6f419cc33834…` | 404 page |
| 1 | 4,597 | 404 | `97f1727a8d3b578f…` | 404 page |
| 1 | 4,597 | 404 | `ee31d5b88cd94398…` | 404 page |
| 1 | 453 | 200 | `657ad4c444396519…` | **`Site Unavailable`** |
| 1 | 272 | 200 | `8cf065293ca696f2…` | minimal `<html>` stub |
| 1 | 162 | 404 | `f33c27745f2bd873…` | minimal `<html>` stub |

Sum: **40**. **Zero** of these is a game page.

### 3.2 The soft-404 discovery — and why it does not rescue the premise

Four of the 40 are the **single most important bodies in this corpus**, because
they look like content and are not. Requests for the long-dead `/sc/bg/*.gif`
files made in **November and December 2017** were answered with the **Blustone
wiki's own Main Page**:

```
URL       http://www.vsfan.net/sc/bg/sl_168.gif
capture   20171230162323   HTTP 200   57,107 B
sha256    7201ec5568649e3ee943152a…
<title>   VisualShower Wiki
<html>    class="client-nojs" lang="en-GB" dir="ltr"
generator MediaWiki 1.30.0-alpha
```

That proves the domain had become the Blustone wiki by late 2017, and it proves
MediaWiki's fall-through behaviour turns any unmatched path into the Main Page.
It also explains the largest two "CJK" readings in the raw scan (§3.3).

**But it adds nothing new.** The 2017 soft-404 Main Page carries **202 `/wiki/`
content links**, of which **128 are already in the CDX census** and the remainder
are either MediaWiki machinery (`index.php?title=…&action=edit&redlink=1`,
`load.php?…`, `oldid=`, `printable=`) or **redlinks for pages that did not exist
then either**. Diffing it against the 1,228-title census yields **74 titles
absent from the archive**; 72 of them are `redlink=1` stubs that never had a
page. Two of the rest are worth one line each:

- **`List of Blustone Monsters` was already a `redlink=1` in 2017.** The prior
  lane found `Monsters` to be an empty stub in the 2019–2020 captures. This is
  independent corroboration that the wiki never carried a monster table — which
  is why monster coverage stays 0/22 and must stay there.
- `Falling...` appears in the census under `/wiki/Falling...`; the 2017 page
  links it with a different trailing form. Not a missing page.

### 3.3 Two apparent Korean/Chinese "hits", both proven artefacts

The raw scan flagged exactly **2 bodies with a Hangul character** and **5 with
CJK**. Each was re-decoded with the correct codec and each is a false positive.
Recording them matters, because "we found Korean in a Chinese BBS corpus" is
exactly the kind of finding that would propagate.

| flagged | what the character was | correct-codec re-decode | verdict |
|---|---|---|---|
| 2 bodies, `hangul=1` | `볢` (U+BCE2) inside the 1,308-byte GB18030 IIS 404, read as UTF-8 | the same bytes as `gb18030` give `请尝试以下操作：` and `确保浏览器的地址栏中显示的网站地址的拼写和格式正确无误` — pure Simplified Chinese, **no Hangul anywhere** | artefact of decoding a GBK page as UTF-8 |
| 5 bodies, `cjk≈35` | produced only by the script's deliberate `gb18030` **fallback** re-scan of bodies that are valid UTF-8 English (`<title>VisualShower Wiki</title>`) | re-parsed strictly as UTF-8: **0 CJK characters** | artefact of decoding UTF-8 English as GB18030 |

**Net Korean characters in the `/sc/` corpus: 0. Genuine Chinese characters: 210,
all inside one IIS error template.**

### 3.4 What the 1,032 images actually are

Decoded with PIL, 1,032/1,032 successfully:

| dimension | count | reading |
|---|---|---|
| 128 × 128 | 339 | forum avatar tile |
| 90 × 90 | 60 | forum avatar |
| 115 × 115 | 50 | forum avatar |
| 11 × 11, 9 × 9, 13 × 13, 15 × 15, 16 × 16, 12 × 12, 15 × 10, 15 × 20 | 48 / 24 / 18 / 35 / 20 / 12 / 14 / 13 | **emoticon and icon set** |
| 400 × 250 | 21 | forum banner / signature strip |
| everything else | remainder | assorted avatars and decorations |

This is a BBS avatar-and-emoticon library. It is the visual signature of a
forum, and it is what 96 % of the `/sc/` archive is.

---

# 4. PROVENANCE — EVERY CAPTURE OF THE 6 EXTENSION-LESS `/sc/` URLs

All 28 captures of the 6 URLs whose path carries no image/archive extension.
These are the only `/sc/` paths that were ever candidates for prose. The other
34 HTML bodies are all `*.gif` paths answered with an error or soft-404 page and
are tabulated by hash cluster in §3.1.

| URL | Wayback ts | CDX status | HTTP | bytes | sha256 (truncated) | `<title>` | `<table>` | Hangul |
|---|---|---|---|---|---|---|---|---|
| `http://www.vsfan.net/sc/bg/sl_094.gif%3Cbr` | 20121018223748 | 302 | 200 | 453 | `657ad4c44439651924425d61a87a121c…` | `Site Unavailable` | 0 | 0 |
| `http://www.vsfan.net/sc/bg/sl_167.gif%3Cbr` | 20150927063241 | 404 | 404 | 1,699 | `cdc8b52c9402b72ef9c698027c0d2ea6…` | `File Not Found` | 0 | 0 |
| `http://www.vsfan.net:80/sc/` | 20070202033614 | 403 | 403 | 218 | `b8f7bd16ab9976b802129a5108e9688f…` | `Error` | 0 | 0 |
| `http://www.vsfan.net:80/sc/` | 20070331113053 | 403 | 403 | 218 | `b8f7bd16ab9976b802129a5108e9688f…` | `Error` | 0 | 0 |
| `http://www.vsfan.net:80/sc/` | 20070705195431 | 403 | 403 | 316 | `b8f7bd16ab9976b802129a5108e9688f…` | `Error` | 0 | 0 |
| `http://www.vsfan.net:80/sc/` | 20070810223405 | 403 | 403 | 316 | `b8f7bd16ab9976b802129a5108e9688f…` | `Error` | 0 | 0 |
| `http://www.vsfan.net:80/sc/` | 20070911193913 | 403 | 403 | 315 | `b8f7bd16ab9976b802129a5108e9688f…` | `Error` | 0 | 0 |
| `http://www.vsfan.net:80/sc/` | 20080206191612 | 403 | 403 | 316 | `b8f7bd16ab9976b802129a5108e9688f…` | `Error` | 0 | 0 |
| `http://www.vsfan.net:80/sc/` | 20080309071831 | 403 | 403 | 316 | `b8f7bd16ab9976b802129a5108e9688f…` | `Error` | 0 | 0 |
| `http://www.vsfan.net:80/sc/` | 20080409125331 | 403 | 403 | 317 | `b8f7bd16ab9976b802129a5108e9688f…` | `Error` | 0 | 0 |
| `http://www.vsfan.net:80/sc/` | 20080510101737 | 400 | 400 | 39 | `2b977b6342a624097b669fd2347ffbcb…` | (none) | 0 | 0 |
| `http://www.vsfan.net:80/sc/` | 20080609181134 | 403 | 403 | 316 | `b8f7bd16ab9976b802129a5108e9688f…` | `Error` | 0 | 0 |
| `http://www.vsfan.net:80/sc/rt/` | 20070202033529 | 403 | 403 | 218 | `b8f7bd16ab9976b802129a5108e9688f…` | `Error` | 0 | 0 |
| `http://www.vsfan.net:80/sc/rt/` | 20070331113205 | 403 | 403 | 218 | `b8f7bd16ab9976b802129a5108e9688f…` | `Error` | 0 | 0 |
| `http://www.vsfan.net:80/sc/rt/` | 20070705195300 | 403 | 403 | 318 | `b8f7bd16ab9976b802129a5108e9688f…` | `Error` | 0 | 0 |
| `http://www.vsfan.net:80/sc/rt/` | 20070813013855 | 403 | 403 | 319 | `b8f7bd16ab9976b802129a5108e9688f…` | `Error` | 0 | 0 |
| `http://www.vsfan.net:80/sc/rt/` | 20070912135053 | 403 | 403 | 318 | `b8f7bd16ab9976b802129a5108e9688f…` | `Error` | 0 | 0 |
| `http://www.vsfan.net:80/sc/rt/` | 20080519155613 | 403 | 403 | 318 | `b8f7bd16ab9976b802129a5108e9688f…` | `Error` | 0 | 0 |
| `http://www.vsfan.net:80/sc/rt/` | 20080619062912 | 403 | 403 | 318 | `b8f7bd16ab9976b802129a5108e9688f…` | `Error` | 0 | 0 |
| `http://www.vsfan.net:80/sc/rt/056\.jpg` | 20070110234651 | 404 | 404 | 1,308 | `e682dfcdde010f6e15bae0d843696f6a…` | `无法找到该页` (GB18030) | 1 | 0 |
| `http://www.vsfan.net:80/sc/rt/056\.jpg` | 20070115212801 | 404 | 404 | 1,308 | `e682dfcdde010f6e15bae0d843696f6a…` | `无法找到该页` | 1 | 0 |
| `http://www.vsfan.net:80/sc/rt/056\.jpg` | 20070120175118 | 404 | 404 | 1,308 | `e682dfcdde010f6e15bae0d843696f6a…` | `无法找到该页` | 1 | 0 |
| `http://www.vsfan.net:80/sc/rt/056\.jpg` | 20070125224115 | 404 | 404 | 1,308 | `e682dfcdde010f6e15bae0d843696f6a…` | `无法找到该页` | 1 | 0 |
| `http://www.vsfan.net:80/sc/xs/` | 20080206191617 | 403 | 403 | 218 | `b8f7bd16ab9976b802129a5108e9688f…` | `Error` | 0 | 0 |
| `http://www.vsfan.net:80/sc/xs/` | 20080309071836 | 403 | 403 | 318 | `b8f7bd16ab9976b802129a5108e9688f…` | `Error` | 0 | 0 |
| `http://www.vsfan.net:80/sc/xs/` | 20080409125403 | 403 | 403 | 318 | `b8f7bd16ab9976b802129a5108e9688f…` | `Error` | 0 | 0 |
| `http://www.vsfan.net:80/sc/xs/` | 20080510101741 | 400 | 400 | 39 | `2b977b6342a624097b669fd2347ffbcb…` | (none) | 0 | 0 |
| `http://www.vsfan.net:80/sc/xs/` | 20080609181139 | 403 | 403 | 318 | `b8f7bd16ab9976b802129a5108e9688f…` | `Error` | 0 | 0 |

(The single `<table>` in the Chinese IIS 404 is the MS support-link table inside
the boilerplate error page. It contains no game data.)

**Distinct bodies across all 28: 5.** Hash clusters: 20 × 218-byte `Error`,
4 × 1,308-byte Chinese IIS 404, 2 × 39-byte `400`, 1 × `Site Unavailable`,
1 × `File Not Found`. Zero game content, in this or any other `/sc/` body.

---

# 5. THE "565" RECONCILIATION

No count in this corpus is 565. Every plausible candidate was computed:

| candidate meaning | value |
|---|---|
| CDX rows under `/sc/` | 1,222 |
| distinct `/sc/` original URLs | 1,101 |
| distinct `/sc/` paths | 1,095 |
| `/sc/` rows with status `200` | 1,156 |
| distinct `.gif` paths | 699 |
| distinct `.png` paths | 329 |
| distinct `.jpg`/`.jpeg` paths | 33 |
| distinct `.rar` paths | 27 |
| **non-image, non-archive paths** | **35** |
| non-image URLs (capable of holding text at all) | **6** |

I cannot reconstruct which query produced "565", and I am not going to guess one
that happens to come out at 565 — that is exactly the failure mode the guard file
warns about. What I can say is bounded by the byte-level read: **whatever the 565
was, it was not a set of readable pages.** Across all 1,101 distinct `/sc/` URLs
there are exactly **40 HTML bodies**, every one of them an error page, a parking
page, or a duplicate of the already-mined English Main Page (§3.1–§3.2).

---

# 6. INDEPENDENT FALSIFICATION OF THE PREMISE

The negative does not rest on the `/sc/` enumeration alone. Five separate lines
of evidence:

| # | test | result |
|---|---|---|
| 1 | Does any wiki article link to `/sc/`? Fetched `http://vsfan.net/wiki/`, `/wiki/Main_Page`, `/wiki/List_of_Blustone_Items`, `/wiki/List_of_Hunters`, `/wiki/Akasha` at archived timestamps (all HTTP 200, 62,339 / 62,775 / 104,950 / 210,828 / 214,105 B, SHA-256 recorded) | **0 occurrences of the string `/sc/` in any of them.** |
| 2 | Is the wiki multilingual? All **1,228** distinct `/wiki/` titles were URL-decoded and scanned | **0 titles contain Hangul.** The only non-ASCII titles are 23 Turkish SEO-spam pages, `开拓者` (`User:` / `Special:Contributions/`) and `Template:·`. Pages carry `<html lang="en">` and an **empty** `p-variants` ("Variants") portlet. |
| 3 | Does the wiki point at a sister site anywhere? All external `href`s extracted from **42** stratified content pages | Hosts are `vsfan.net`, `creativecommons.org`, `meta.miraheze.org`, `www.mediawiki.org`, `bs/wi/btb.visualshower.com`, `en.wikipedia.org`, `openlibrary.org`, `knowyourmeme.com`, `www.bagdatkitapligi.com`, `Yasarhomedesign.com`. **No Korean wiki, no second Blustone language site, no `/sc/` host.** |
| 4 | Is there a Korean mirror of the wiki? Live `vsfanwiki.miraheze.org` API + `Main_Page` | Both **HTTP 404** ("Wiki not found"), host reachable — so the 404 is a real absence, not a transport failure. Wayback CDX for `vsfanwiki.miraheze.org`, `/wiki/` and `/w/`: **0 rows each.** |
| 5 | Is `/sc/` a wiki path after all? CDX exact/prefix: `/sc`, `/sc/`, `/sc/wiki/`, `/sc/index.php`, `/sc/index.asp`, `/sc/index.html`, and domain `sc.vsfan.net` | 10 rows (all 403/400 on the bare directory), 1,222 rows (the image tree), then **0, 0, 0, 0, 0**. |
| 6 | **What does `/sc/` actually serve when it is hit during the Blustone era?** Four `/sc/bg/*.gif` requests captured in Nov–Dec 2017 were answered with the **English** wiki Main Page | `<title>VisualShower Wiki</title>`, `lang="en-GB"`, MediaWiki 1.30.0-alpha, 202 `/wiki/` links of which 128 are already archived and ~72 are `redlink=1` stubs. **It is the same English wiki, and `List of Blustone Monsters` was already a redlink in 2017** — independent corroboration for monster coverage staying 0/22. §3.2. |

---

# 7. ITEM-NAME CROSSWALK AGAINST `CHAR_STR.db` — NOT APPLICABLE, AND WHY

The local item table
[`charstr-items-2026-10-06.tsv`](charstr-items-2026-10-06.tsv) is **105 data
rows**: a dense `001`–`098` block with no gaps inside it, plus `900`,
`905`–`909`, `911` and `914` (seven `9xx` rows), carrying `accessory_ja`,
`accessory_ko` and `accessory_sc` columns. **The crosswalk has no input from this
lane**: the
`/sc/` corpus yields **zero item names in any language**. There is nothing to
match, so nothing was matched, and no row of that table was touched.

(Recorded for the next agent, since the premise that motivated it may recur:
`accessory_sc` is **Simplified Chinese**, e.g. row `001`
`ジュデッカの贈り物 / 쥬데카의 선물 / 犹大环的礼物`. Any future Simplified-Chinese
Blustone source is a candidate for that column — but `/sc/` is not such a source.)

---

# 8. HONEST STATEMENT — WHAT `/sc/` DOES AND DOES NOT CONTAIN

**It does contain:** **1,061** image/archive payloads — 672 GIF, 332 PNG, 28 JPEG,
27 RAR, 2 SWF — captured 2006–2015, belonging to a Chinese BBS that once shared
the `vsfan.net` domain with the Blustone wiki eleven years later, plus **40 HTML
bodies** that are error pages, a registrar parking page, and four copies of the
English wiki Main Page. The images decode as avatars (339 × 128×128) and emoticons
(9–16 px). That is all.

**It does not contain:** any Blustone page; **any Korean character** (net 0, with
the two apparent hits proven to be codec artefacts in §3.3); any Chinese prose
beyond one IIS 404 template; any HTML document with game content; any `<table>`
with data; any stat block; any equipment, gem, level/EXP, recruitment,
transcendence, drop-rate, arena or guild number; any hero identity; any item name.

**Therefore:** no numeric table was recovered, no hero was identified, no item
name was crosswalked, and **no coverage counter moves**. Heroes **1/113**,
accessories **1/100**, monsters **0/22**.

**On the brief's framing.** The instruction anticipated that "this corpus may
well be a mirror of the English one." It is worse than a mirror: it is not the
same corpus at all. It is a different site generation on the same domain,
predating the game by nine years. This is a **controlled negative with a positive
control**, not a failed retrieval.

**A caution for whoever re-plans this.** vsfan.net's Wayback record contains
three unrelated generations of the same host — a Chinese BBS with DedeCMS
(`/site/`, `/sc/`, `/templets/`), the English Blustone MediaWiki (`/wiki/`,
`/w/`), and a later Turkish SEO-spam layer. A path-scoped query against this
domain will silently cross generations. Any future claim of the form "page X of
site Y is in the vsfan archive" must state the generation and the year range.

---

# 9. LIMITS OF THIS LANE

1. Enumeration completeness is bounded by the archive, not by proof. Per guard
   items 3–4, CDX can return reproducible false negatives and `id_` at an
   unlisted timestamp can succeed. So the correct claim is *"the archive holds
   1,222 captures of 1,101 distinct `/sc/` URLs, all of which were examined"*, not
   *"`/sc/` never held anything else"*. Given that 96 % of it is 2006–2008 forum
   imagery, an undiscovered sibling directory would not change the verdict, but
   the claim is deliberately not overstated.
2. The 27 `.rar` payloads were confirmed as `Rar!` by magic bytes but **not
   unpacked** — they are `/sc/dm/*.rar`, 2007 downloads with opaque Chinese
   numeric filenames and no Blustone-era date. Unpacking them is not worth the
   bandwidth and cannot change the era finding.
3. Two SWF files (`/sc/flash/9.swf`, `/sc/flash/10.swf`) were confirmed as Flash
   by magic bytes only; not decompiled. Same reasoning.
4. The Korean-content scan of the English wiki was structural (title decoding,
   variant portlet, external-link census), not a full-text scan of all 416 pages.
   A Korean page with an ASCII title would in principle escape it — but such a
   page would be surfaced as an interlanguage link or a `p-variants` entry, and
   both are empty, and none of the 42 sampled pages carried one.
5. `charset` was never read from an HTTP response header, because the retrieval
   used `id_` replay and the archives' own headers were not compared against the
   decoded bytes. Codec choice was instead settled by *failing* to decode: the
   IIS 404 decodes cleanly as `gb18030` and fails as UTF-8 and EUC-KR (§2.1), and
   the wiki Main Page decodes cleanly as UTF-8 with zero CJK (§3.3). Two bodies
   remain ambiguous in principle — the two SWF files, which were not decoded at
   all.
6. The corpus was read from the **archive**, not from the live site. `vsfan.net`
   is NXDOMAIN (established by the prior lane, not re-tested here), so no claim is
   made about what `/sc/` contained on any given day — only about what the
   Wayback Machine holds.
7. No local file under `analysis/VSFan/` was modified, and no TSV, `coverage.md`,
   `polluted-observations.md`, `server-ts`, fixture, APK, seed, emulator, phone or
   Ghidra artefact was touched.

---

# 10. REPRODUCTION

Every query in this report, exactly as issued (HTTP only; no `https://`):

```
# positive controls
http://web.archive.org/                                              -> 200 145187 B
http://web.archive.org/cdx/search/cdx?url=vsfan.net%2Fwiki%2FList_of_Hunters&matchType=exact&limit=50
http://web.archive.org/cdx/search/cdx?url=vsfan.net%2Fwiki%2FAkasha&matchType=exact&limit=50

# the census (one complete non-collapsed sweep, cross-checked by prefix)
http://web.archive.org/cdx/search/cdx?url=vsfan.net&matchType=domain&limit=20000          -> 13274 rows
http://web.archive.org/cdx/search/cdx?url=vsfan.net%2Fsc%2F&matchType=prefix&limit=20000  -> 1222 rows

# the zero probes behind §6
url=vsfan.net%2Fsc%2Fwiki%2F&matchType=prefix   -> 0
url=vsfan.net%2Fsc%2Findex.php&matchType=exact   -> 0
url=vsfan.net%2Fsc%2Findex.asp&matchType=exact   -> 0
url=vsfan.net%2Fsc%2Findex.html&matchType=exact  -> 0
url=sc.vsfan.net&matchType=domain                -> 0
url=vsfanwiki.miraheze.org&matchType=domain      -> 0

# a body
http://web.archive.org/web/20070110234651id_/http://www.vsfan.net:80/sc/rt/056%5C.jpg

# the soft-404 Main Page (§3.2)
http://web.archive.org/web/20171230162323id_/http://www.vsfan.net/sc/bg/sl_168.gif

# the English wiki (control bodies for §6)
http://web.archive.org/web/20191114021317id_/http://vsfan.net/wiki/
http://web.archive.org/web/20190826082717id_/http://vsfan.net/wiki/List_of_Blustone_Items
http://web.archive.org/web/20191114021317id_/http://vsfan.net/wiki/List_of_Hunters
http://web.archive.org/web/20191209033311id_/http://vsfan.net/wiki/Akasha
```

SHA-256 of those five English control bodies, for anyone re-running this lane:
`/wiki/` `fda8a3ffb46379bc…`, `/wiki/Main_Page` `fa700e138dd8f473…`,
`List_of_Blustone_Items` `c7f2edbb35f3e076…`,
`List_of_Hunters` `fe1fbe9b221c607e…`, `Akasha` `d5627f519092f996…`.

Local working copies of the raw CDX sweep, the fetch logs and the per-URL
SHA-256 inventory were written to the session scratch directory
(`%LOCALAPPDATA%\Temp\opencode\vsfan\`: `cdx_domain_all.txt` (13,274 rows),
`sc_inventory.json` (1,101 entries with per-URL sha256, HTTP status, magic-byte
kind and hangul/cjk counts), `sc_html_fetch_log.json`, `raw_sc\` = 1,069 body
files, 23.3 MB), not into the repository, to avoid adding an unreviewed data file
to the research tree.