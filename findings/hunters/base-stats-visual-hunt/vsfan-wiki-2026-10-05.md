# `vsfan.net` Blustone community wiki — archived harvest (2026-10-05)

**Lane:** ranked candidate **9** of
[`share-en-census-2026-10-05.md`](share-en-census-2026-10-05.md) §3 — the
`share_en` post `199711` hotlinks 54 `vsfan.net/wiki/images/…` assets, and the
wiki's own ITEM and HUNTER pages are a different, unmined corpus on a different
domain. This is the parallel English-language counterpart to the already
harvested Japanese `blustone.jp/hunter` 2019 database
([`archived-hunter-database-2019.md`](archived-hunter-database-2019.md)).

**Read this first.** This lane is **not** a clean negative. The wiki exists,
was archived in bulk, and **299 of 299 content pages were retrieved at HTTP
200**. It is also **not** a second copy of the Japanese database. It contains a
distinct data type the project did not previously have:

> **Three heroes carry an explicit `Life / Attack / Defense / Attack Speed`
> stat table captioned `Transcendence Level: 3`** — i.e. the one thing the 2019
> `blustone.jp` harvest explicitly lacked is **state context**, and the wiki
> supplies it.

Everything numeric in it is nevertheless held to the same bar as every other
observation in this goal: **no new base-stat coverage is claimed.** §3 states
the disposition precisely.

## Headline findings

| # | Finding |
|---|---|
| 1 | **Live `vsfan.net` is gone — NXDOMAIN**, verified against two working controls. The domain no longer resolves. |
| 2 | **The Wayback Machine holds it in bulk**: 4,054 CDX rows for the domain, 1,223 under `/wiki/`, of which **299 content-namespace pages returned retrievable bytes (299/299, HTTP 200)**. |
| 3 | It is a **MediaWiki** install (later mirrored to Miraheze as `vsfanwiki`, now also deleted — `vsfanwiki.miraheze.org` returns `Wiki not found`). Pages carry exact revision IDs (`oldid=NNNN`). |
| 4 | **57 hero pages** carry rarity / role / element / gender / race infoboxes. **All 57 map cleanly onto local catalogue card IDs.** |
| 5 | **11 hero pages carry a `Character Attributes` stat table.** 8 of them have only `Attack Speed` plus the 9 sub-stats — **the Life/Attack/Defense rows are absent from the wikitext, not blank.** 3 (Captain, Hermes, Riko) are complete. |
| 6 | **97 of 108** overlapping sub-stat fields match the 2019 `blustone.jp` database **exactly**. The 11 differences are precisely the 3 heroes' Life/Attack/Defense **plus** two `hp_regen` off-by-ones. This proves the wiki table and the JP table are the **same schema and same underlying data**. |
| 7 | Consequently the wiki's Life/Attack/Defense values are **Transcendence-Level-3 boosted**, and dividing by the JP values yields a candidate **≈1.27–1.30** transcendence multiplier on Life/Attack/Defense. §2.2. |
| 8 | **Equipment effect tables exist on 35 heroes but 106 of 216 rows are blank** — the editors wrote `Increases attack Lv.50` and left the magnitude empty. Exactly **two** rows were ever filled in (§1.8). |
| 9 | `List_of_Blustone_Items` carries a **28-row Hunter Trace table with per-trace star rarity and values (★=20 / ★★=100 / ★★★=300)**. The trace star count is a **third independent vote on hero rarity**, and it agrees with all other sources on **26 of 27** heroes. **[2026-10-05 `trace-rarity-vote-2026-10-05.md` §1.1–§1.4, §2.2: those three numerals sit in the `Value` column and are a per-trace rarity VALUE, NOT a recruitment threshold — NOT COMMENSURABLE with `collect_qty`.]** |
| 10 | Substantial **original-era economy data**: full gacha drop rates, the 12-rank veteran ladder, the Fight Club Shop price list, the skill-level cost table, the transcendence matrix, and Abyss/ruins costs. |
| 11 | **Jewels, Fishing and any GvG article are NOT in the archive** — 17 targeted CDX probes returned zero rows against a **working control** (§1.17). Monster coverage stays 0/22: the `Monsters` page is an **empty stub**. |

---

# 1. PURE

Everything in §1 is a verbatim reading of an archived page. Nothing here is a
base-stat tuple unless §1.6/§1.7 explicitly says so. Capture dates are the
Wayback timestamps. Where a value is absent from the source, that absence is
itself recorded rather than filled in.

## 1.1 Reachability — established first, with positive controls

The instruction was to settle live-vs-archived reachability *first* and to run
a positive control before any zero could be read as real. Both were done.

| # | Probe | Result |
|---|---|---|
| 1 | **CONTROL** `https://web.archive.org/` | **HTTP 200, 145,187 bytes** |
| 2 | **CONTROL** `https://example.com/` | **HTTP 200, 577 bytes** |
| 3 | `http://vsfan.net/` (follow redirects) | **curl exit 000** |
| 4 | `https://vsfan.net/` (follow redirects) | **curl exit 000** |
| 5 | `curl -I http://vsfan.net/` (headers only) | **`curl: (6) Could not resolve host: vsfan.net`** |
| 6 | `nslookup vsfan.net` | **`*** UnKnown can't find vsfan.net: Non-existent domain`** |
| 7 | `Resolve-DnsName vsfan.net` / `www.vsfan.net` | **no records returned** |

**Verdict: the live site is gone at the DNS layer (NXDOMAIN), not merely
refusing HTTP.** Two independent working controls on the same host and the same
moment prove the `000`/NXDOMAIN readings are about the domain, not the box. The
`curl (6)` message distinguishes this from the `000` transport failures seen
later against `web.archive.org` (§1.2).

## 1.2 The Wayback Machine holds the domain

| # | Probe | Result |
|---|---|---|
| 8 | **CONTROL** CDX `url=bs.visualshower.com&matchType=domain&collapse=urlkey&limit=20000` | **HTTP 200, 1,114,003 bytes** — the query method works |
| 9 | **CONTROL** CDX, exact `vsfan.net/wiki/List_of_Hunters` | **HTTP 200, 2 rows** (20190826082717, 20191114021317) |
| 10 | **CONTROL** CDX, exact `https://vsfan.net/wiki/Akasha` | **HTTP 200, 3 rows** (20190821024122, 20191015110220, 20191209033311) |
| 11 | CDX `url=vsfan.net&matchType=domain&collapse=urlkey&limit=20000` | **HTTP 200, 200,420 bytes, 4,054 rows** |
| 12 | — first four requests to the CDX API | **`curl 000` ×4 (transport)**; re-issued and all succeeded |

`cdx-vsfan-domain.json` status distribution over 4,054 rows:
**`200`: 3,978 · `301`: 4 · `302`: 9 · `403`: 4 · `404`: 58 · `-`: 1.**

Rows by top-level path segment: `wiki` **1,224**, `sc` 1,096, `site` 735,
`w` 520, `news` 102, `product` 96, `blog` 52, `img` 25, `templets` 23, then
long-tail numeric blog paths from 2010. **`/wiki/` rows by capture year:
2017 = 26, 2018 = 23, 2019 = 1,173, 2020 = 1** (1,223 rows plus header).

The 2010–2016 material is unrelated site content (a general `vsfan.net` web
presence with a numeric blog). **The game wiki is the 2017–2019 `/wiki/`
burst.**

## 1.3 Platform identification, and the Miraheze migration

The `/wiki/` namespace segments are unambiguous MediaWiki:
`Template:citation_style_documentation` (38), `module:citation` (15),
`special:contributions` (11), `module:category_handler` (10),
`module:protection_banner` (6), `template:episode_list` (3), `api.php` (2),
`load.php` (3), `skins` (4), `opensearch_desc.php`, `piwik.js`.

Archived `api.php`/`load.php` rows, verbatim:

```
20171216033746 200 application/xml https://vsfan.net/wiki/api.php?hidebots=1&urlversion=1&days=7&limit=50&action=feedrecentchanges&feedformat=atom
20171215103537 200 application/rsd+xml https://vsfan.net/wiki/api.php?action=rsd
20171215121622 200 text/css https://vsfan.net/wiki/load.php?debug=false&lang=en-gb&modules=mediawiki.legacy.commonPrint%2Cshared%7Cmediawiki.sectionAnchor%7Cmediawiki.skinning.interface%7Cskins.vector.styles&only=styles&skin=vector
20171215123157 200 text/css https://vsfan.net/wiki/load.php?debug=false&lang=en-gb&modules=site.styles&only=styles&skin=vector
20171215130239 200 text/javascript https://vsfan.net/wiki/load.php?debug=false&lang=en-gb&modules=startup&only=scripts&skin=vector
```

Every image in the 2019 captures points at **`static.miraheze.org/vsfanwiki/…`**,
i.e. the wiki had been **migrated from a self-hosted install to Miraheze**.
Live check of that successor:

| # | Probe | Result |
|---|---|---|
| 13 | `https://vsfanwiki.miraheze.org/w/api.php?action=query&meta=siteinfo&format=json` | **HTTP 404**, Miraheze's own error page: `<h1><b>Wiki not found</b></h1>` … `We couldn't find this wiki.` |

Miraheze itself answers normally, so the 404 is specific to this wiki: **both
the original domain and its Miraheze successor are gone.** The Wayback copy is
the only remaining copy found.

**Every retrieved page also carries its exact MediaWiki revision id** in the
`Retrieved from "https://vsfan.net/w/index.php?title=<Title>&oldid=NNNN"` footer
— a citable per-page revision handle independent of the crawl timestamp. The
full mapping is in §1.4's companion note at the end of this section.

## 1.4 Full fetch ledger — 299 of 299 pages retrieved

CDX `length` is the **compressed WARC record length**; `fetched bytes` is the
decompressed `id_` payload, hence the consistent ~8× ratio. **Every row below
returned HTTP 200.** Retrieval used the `id_` (raw, un-rewritten) form.
| page | oldid | capture (UTC) | CDX len | fetched bytes | HTTP | archive URL |
|---|---|---|---|---|---|---|
| `İşlemlerin_Tamamı_Memnuniyet_Odaklıdır` | 6366 | 2019-08-21 00:28:49Z | 7147 | 19814 | 200 | `https://web.archive.org/web/20190821002849id_/https://vsfan.net/wiki/%C4%B0%C5%9Flemlerin_Tamam%C4%B1_Memnuniyet_Odakl%C4%B1d%C4%B1r` |
| `A_Chill` | 5928 | 2019-08-21 00:38:50Z | 11063 | 48031 | 200 | `https://web.archive.org/web/20190821003850id_/https://vsfan.net/wiki/A_Chill` |
| `A_Chunk_Of_Metal` | 5995 | 2019-09-23 06:59:30Z | 11065 | 45734 | 200 | `https://web.archive.org/web/20190923065930id_/https://vsfan.net/wiki/A_Chunk_Of_Metal` |
| `A_Difficult_Partner` | 7499 | 2020-08-08 17:31:37Z | 11634 | 51394 | 200 | `https://web.archive.org/web/20200808173137id_/https://vsfan.net/wiki/A_Difficult_Partner` |
| `A_Groundbreaking_Upgrade` | 6147 | 2019-09-23 07:00:27Z | 11177 | 50223 | 200 | `https://web.archive.org/web/20190923070027id_/https://vsfan.net/wiki/A_Groundbreaking_Upgrade` |
| `A_Legendary_Man` | 6148 | 2019-08-21 00:56:12Z | 11189 | 48728 | 200 | `https://web.archive.org/web/20190821005612id_/https://vsfan.net/wiki/A_Legendary_Man` |
| `A_Secret_Request` | 6122 | 2019-09-23 08:00:45Z | 11376 | 54956 | 200 | `https://web.archive.org/web/20190923080045id_/https://vsfan.net/wiki/A_Secret_Request` |
| `A_Secret_Revealed` | 5751 | 2019-08-21 00:29:48Z | 8527 | 25262 | 200 | `https://web.archive.org/web/20190821002948id_/https://vsfan.net/wiki/A_Secret_Revealed` |
| `A_Train_and_a_Flower` | 5754 | 2019-08-21 03:34:50Z | 8540 | 25387 | 200 | `https://web.archive.org/web/20190821033450id_/https://vsfan.net/wiki/A_Train_and_a_Flower` |
| `Abyss_Area` | 5785 | 2019-08-26 08:14:54Z | 12799 | 50028 | 200 | `https://web.archive.org/web/20190826081454id_/https://vsfan.net/wiki/Abyss_Area` |
| `Acerola` | 7387 | 2019-08-26 07:31:58Z | 18446 | 137707 | 200 | `https://web.archive.org/web/20190826073158id_/https://vsfan.net/wiki/Acerola` |
| `Aircraft_Entrance` | 5003 | 2019-08-26 08:12:20Z | 10403 | 36679 | 200 | `https://web.archive.org/web/20190826081220id_/https://vsfan.net/wiki/Aircraft_Entrance` |
| `Akıllı_Bariyer_Ve_Benzeri_Uygulamalar` | 6333 | 2019-08-21 00:30:31Z | 7254 | 19474 | 200 | `https://web.archive.org/web/20190821003031id_/https://vsfan.net/wiki/Ak%C4%B1ll%C4%B1_Bariyer_Ve_Benzeri_Uygulamalar` |
| `Akasha` | 7376 | 2019-08-21 02:41:22Z | 21639 | 214068 | 200 | `https://web.archive.org/web/20190821024122id_/https://vsfan.net/wiki/Akasha` |
| `Akasha's_Choice` | 6234 | 2019-08-21 00:29:25Z | 11261 | 53534 | 200 | `https://web.archive.org/web/20190821002925id_/https://vsfan.net/wiki/Akasha%27s_Choice` |
| `Alfheimr's_Troublemakers` | 5745 | 2019-08-21 02:41:05Z | 9784 | 28220 | 200 | `https://web.archive.org/web/20190821024105id_/https://vsfan.net/wiki/Alfheimr%27s_Troublemakers` |
| `Amalgam's_Assignment` | 5760 | 2019-08-21 00:40:13Z | 8554 | 25432 | 200 | `https://web.archive.org/web/20190821004013id_/https://vsfan.net/wiki/Amalgam%27s_Assignment` |
| `An_Awkward_Encounter` | 5905 | 2019-09-23 06:59:18Z | 10714 | 43691 | 200 | `https://web.archive.org/web/20190923065918id_/https://vsfan.net/wiki/An_Awkward_Encounter` |
| `An_Encounter` | 5348 | 2019-08-21 00:29:39Z | 10719 | 41333 | 200 | `https://web.archive.org/web/20190821002939id_/https://vsfan.net/wiki/An_Encounter` |
| `An_Unexpected_Rescue` | 5383 | 2019-09-23 07:36:54Z | 10742 | 41374 | 200 | `https://web.archive.org/web/20190923073654id_/https://vsfan.net/wiki/An_Unexpected_Rescue` |
| `Another_One?` | 5343 | 2019-08-21 01:12:47Z | 10645 | 40415 | 200 | `https://web.archive.org/web/20190821011247id_/https://vsfan.net/wiki/Another_One%3F` |
| `Apollon` | 7403 | 2019-08-21 03:22:31Z | 15781 | 76677 | 200 | `https://web.archive.org/web/20190821032231id_/https://vsfan.net/wiki/Apollon` |
| `Artificial_Freedom` | 6072 | 2019-08-21 00:53:57Z | 11018 | 48172 | 200 | `https://web.archive.org/web/20190821005357id_/https://vsfan.net/wiki/Artificial_Freedom` |
| `Athena` | 2790 | 2019-08-26 07:11:04Z | 15142 | 85140 | 200 | `https://web.archive.org/web/20190826071104id_/https://vsfan.net/wiki/Athena` |
| `Audrey` | 4602 | 2019-08-21 02:41:30Z | 8774 | 26162 | 200 | `https://web.archive.org/web/20190821024130id_/https://vsfan.net/wiki/Audrey` |
| `Awake` | 5339 | 2019-09-20 18:14:45Z | 10716 | 42803 | 200 | `https://web.archive.org/web/20190920181445id_/https://vsfan.net/wiki/Awake` |
| `Balian` | 2224 | 2019-08-21 02:48:04Z | 15157 | 89998 | 200 | `https://web.archive.org/web/20190821024804id_/https://vsfan.net/wiki/Balian` |
| `Bear` | 7436 | 2019-08-26 07:00:34Z | 14993 | 80961 | 200 | `https://web.archive.org/web/20190826070034id_/https://vsfan.net/wiki/Bear` |
| `Beavergret` | 6205 | 2019-08-21 02:41:48Z | 7047 | 18690 | 200 | `https://web.archive.org/web/20190821024148id_/https://vsfan.net/wiki/Beavergret` |
| `Beckhen` | 7422 | 2019-08-21 02:43:08Z | 15698 | 88572 | 200 | `https://web.archive.org/web/20190821024308id_/https://vsfan.net/wiki/Beckhen` |
| `Beginning_of_the_Nightmare` | 5691 | 2019-08-26 07:13:49Z | 9818 | 36017 | 200 | `https://web.archive.org/web/20190826071349id_/https://vsfan.net/wiki/Beginning_of_the_Nightmare` |
| `Beyond_The_Bounds` | 7274 | 2019-08-21 02:41:13Z | 13603 | 62194 | 200 | `https://web.archive.org/web/20190821024113id_/https://vsfan.net/wiki/Beyond_The_Bounds` |
| `Bibi` | 7431 | 2019-08-21 02:47:59Z | 16090 | 83259 | 200 | `https://web.archive.org/web/20190821024759id_/https://vsfan.net/wiki/Bibi` |
| `Bizden_Fiyat_Almadan_Alışveriş_Yapmayın` | 6360 | 2019-08-21 01:25:17Z | 7251 | 19759 | 200 | `https://web.archive.org/web/20190821012517id_/https://vsfan.net/wiki/Bizden_Fiyat_Almadan_Al%C4%B1%C5%9Fveri%C5%9F_Yapmay%C4%B1n` |
| `Blood_Red_Canyon` | 3365 | 2019-08-26 06:58:31Z | 10631 | 37737 | 200 | `https://web.archive.org/web/20190826065831id_/https://vsfan.net/wiki/Blood_Red_Canyon` |
| `Blue_Wing_Valley` | 5873 | 2019-08-21 03:51:09Z | 10590 | 37518 | 200 | `https://web.archive.org/web/20190821035109id_/https://vsfan.net/wiki/Blue_Wing_Valley` |
| `Blustone` | 7273 | 2019-08-21 00:44:09Z | 11612 | 40597 | 200 | `https://web.archive.org/web/20190821004409id_/https://vsfan.net/wiki/Blustone` |
| `Boiler_Incident` | 5748 | 2019-08-26 07:21:50Z | 8508 | 25076 | 200 | `https://web.archive.org/web/20190826072150id_/https://vsfan.net/wiki/Boiler_Incident` |
| `Bright` | 7441 | 2019-08-26 06:57:40Z | 16925 | 85901 | 200 | `https://web.archive.org/web/20190826065740id_/https://vsfan.net/wiki/Bright` |
| `Broken_Memories` | 6174 | 2019-08-21 02:58:21Z | 9479 | 34513 | 200 | `https://web.archive.org/web/20190821025821id_/https://vsfan.net/wiki/Broken_Memories` |
| `Bruce_Bang` | 7321 | 2019-08-26 07:49:37Z | 17617 | 138201 | 200 | `https://web.archive.org/web/20190826074937id_/https://vsfan.net/wiki/Bruce_Bang` |
| `Burned_Forest` | 5868 | 2019-08-21 02:40:40Z | 10576 | 37395 | 200 | `https://web.archive.org/web/20190821024040id_/https://vsfan.net/wiki/Burned_Forest` |
| `Cake_of_Lantern` | 6368 | 2019-09-23 08:04:00Z | 11044 | 49911 | 200 | `https://web.archive.org/web/20190923080400id_/https://vsfan.net/wiki/Cake_of_Lantern` |
| `Calibur` | 7478 | 2019-08-26 08:05:06Z | 15295 | 79610 | 200 | `https://web.archive.org/web/20190826080506id_/https://vsfan.net/wiki/Calibur` |
| `Captain` | 2323 | 2019-08-21 02:51:53Z | 15892 | 97621 | 200 | `https://web.archive.org/web/20190821025153id_/https://vsfan.net/wiki/Captain` |
| `Challenge` | 5926 | 2019-09-23 07:00:45Z | 11009 | 47859 | 200 | `https://web.archive.org/web/20190923070045id_/https://vsfan.net/wiki/Challenge` |
| `Chaos!_Destruction!_Oblivion!` | 6084 | 2019-09-23 06:59:37Z | 11055 | 47573 | 200 | `https://web.archive.org/web/20190923065937id_/https://vsfan.net/wiki/Chaos!_Destruction!_Oblivion!` |
| `Clara` | 4501 | 2019-08-21 02:48:44Z | 10619 | 37001 | 200 | `https://web.archive.org/web/20190821024844id_/https://vsfan.net/wiki/Clara` |
| `Close_By` | 6038 | 2019-08-21 00:30:01Z | 10857 | 44371 | 200 | `https://web.archive.org/web/20190821003001id_/https://vsfan.net/wiki/Close_By` |
| `Coffee_Rabbit` | 4381 | 2019-08-26 06:57:49Z | 10321 | 35988 | 200 | `https://web.archive.org/web/20190826065749id_/https://vsfan.net/wiki/Coffee_Rabbit` |
| `Coffee_Rabbits` | 4381 | 2019-09-23 07:00:35Z | 10403 | 36355 | 200 | `https://web.archive.org/web/20190923070035id_/https://vsfan.net/wiki/Coffee_Rabbits` |
| `Contact_Lana` | 7466 | 2019-09-23 06:57:56Z | 6455 | 16667 | 200 | `https://web.archive.org/web/20190923065756id_/https://vsfan.net/wiki/Contact_Lana` |
| `Conversation_I'd_Like_To_Join` | 6117 | 2019-09-20 18:13:05Z | 11286 | 48964 | 200 | `https://web.archive.org/web/20190920181305id_/https://vsfan.net/wiki/Conversation_I%27d_Like_To_Join` |
| `Counseling_with_the_Dummy` | 6011 | 2019-09-23 07:47:02Z | 11072 | 48123 | 200 | `https://web.archive.org/web/20190923074702id_/https://vsfan.net/wiki/Counseling_with_the_Dummy` |
| `Crescent_Hill` | 5832 | 2019-08-21 03:58:13Z | 10597 | 37490 | 200 | `https://web.archive.org/web/20190821035813id_/https://vsfan.net/wiki/Crescent_Hill` |
| `Crimson_Chasm` | 3259 | 2019-08-26 08:10:47Z | 10677 | 37789 | 200 | `https://web.archive.org/web/20190826081047id_/https://vsfan.net/wiki/Crimson_Chasm` |
| `Crocus` | 7408 | 2019-08-21 02:54:19Z | 14166 | 65789 | 200 | `https://web.archive.org/web/20190821025419id_/https://vsfan.net/wiki/Crocus` |
| `Cryogenic_Abyss` | 4973 | 2019-08-21 02:40:57Z | 10407 | 36374 | 200 | `https://web.archive.org/web/20190821024057id_/https://vsfan.net/wiki/Cryogenic_Abyss` |
| `Cutting_Water_Bottles` | 5388 | 2019-09-23 06:59:09Z | 11099 | 47414 | 200 | `https://web.archive.org/web/20190923065909id_/https://vsfan.net/wiki/Cutting_Water_Bottles` |
| `Damacana_Sulara_Para_ödemeyin` | 6362 | 2019-09-23 07:25:14Z | 7200 | 19027 | 200 | `https://web.archive.org/web/20190923072514id_/https://vsfan.net/wiki/Damacana_Sulara_Para_%C3%B6demeyin` |
| `Dating_Consultant` | 6235 | 2019-09-23 08:11:01Z | 11470 | 54425 | 200 | `https://web.archive.org/web/20190923081101id_/https://vsfan.net/wiki/Dating_Consultant` |
| `Dawdly` | 6019 | 2019-08-21 00:40:57Z | 7015 | 18512 | 200 | `https://web.archive.org/web/20190821004057id_/https://vsfan.net/wiki/Dawdly` |
| `Denali` | 7315 | 2019-08-21 02:41:09Z | 20046 | 173092 | 200 | `https://web.archive.org/web/20190821024109id_/https://vsfan.net/wiki/Denali` |
| `Denali's_Letter` | 5914 | 2019-08-21 01:22:27Z | 11302 | 52754 | 200 | `https://web.archive.org/web/20190821012227id_/https://vsfan.net/wiki/Denali%27s_Letter` |
| `Dental_Market_Goldspeed_Evo_E16_Endodontik_Anguldurva` | 6354 | 2019-09-23 07:56:16Z | 9209 | 24000 | 200 | `https://web.archive.org/web/20190923075616id_/https://vsfan.net/wiki/Dental_Market_Goldspeed_Evo_E16_Endodontik_Anguldurva` |
| `Diana` | 7462 | 2019-08-26 08:19:56Z | 16916 | 90744 | 200 | `https://web.archive.org/web/20190826081956id_/https://vsfan.net/wiki/Diana` |
| `Dino` | 7396 | 2019-08-21 03:29:32Z | 15735 | 79574 | 200 | `https://web.archive.org/web/20190821032932id_/https://vsfan.net/wiki/Dino` |
| `Dumble` | 7425 | 2019-08-26 08:32:03Z | 15381 | 78329 | 200 | `https://web.archive.org/web/20190826083203id_/https://vsfan.net/wiki/Dumble` |
| `Dummy` | 6003 | 2019-09-23 07:17:58Z | 11135 | 47801 | 200 | `https://web.archive.org/web/20190923071758id_/https://vsfan.net/wiki/Dummy` |
| `Edison` | 5051 | 2019-08-21 00:30:36Z | 8329 | 24429 | 200 | `https://web.archive.org/web/20190821003036id_/https://vsfan.net/wiki/Edison` |
| `Edward` | 7429 | 2019-08-21 03:05:24Z | 15809 | 80879 | 200 | `https://web.archive.org/web/20190821030524id_/https://vsfan.net/wiki/Edward` |
| `Electric_Abyss` | 4980 | 2019-08-21 00:40:44Z | 10398 | 36368 | 200 | `https://web.archive.org/web/20190821004044id_/https://vsfan.net/wiki/Electric_Abyss` |
| `Element_Type` | 2091 | 2019-09-23 07:24:47Z | 12369 | 45850 | 200 | `https://web.archive.org/web/20190923072447id_/https://vsfan.net/wiki/Element_Type` |
| `Emerald_Canyon` | 3424 | 2019-08-21 03:13:09Z | 10617 | 37601 | 200 | `https://web.archive.org/web/20190821031309id_/https://vsfan.net/wiki/Emerald_Canyon` |
| `En_Kısa_Sürede_Kitaplar_Elinizde` | 6318 | 2019-08-21 00:31:16Z | 7325 | 19255 | 200 | `https://web.archive.org/web/20190821003116id_/https://vsfan.net/wiki/En_K%C4%B1sa_S%C3%BCrede_Kitaplar_Elinizde` |
| `Estelle` | 3112 | 2019-08-26 06:57:21Z | 10959 | 38607 | 200 | `https://web.archive.org/web/20190826065721id_/https://vsfan.net/wiki/Estelle` |
| `Eunhwa` | 4565 | 2019-08-21 02:39:47Z | 9546 | 34537 | 200 | `https://web.archive.org/web/20190821023947id_/https://vsfan.net/wiki/Eunhwa` |
| `Expedition_Area` | 3233 | 2019-08-26 07:02:39Z | 11142 | 38733 | 200 | `https://web.archive.org/web/20190826070239id_/https://vsfan.net/wiki/Expedition_Area` |
| `Experienced_Senior` | 6024 | 2019-09-20 18:14:20Z | 11216 | 49528 | 200 | `https://web.archive.org/web/20190920181420id_/https://vsfan.net/wiki/Experienced_Senior` |
| `Fight_Club` | 3210 | 2019-08-26 06:58:02Z | 10524 | 36909 | 200 | `https://web.archive.org/web/20190826065802id_/https://vsfan.net/wiki/Fight_Club` |
| `Fight_Club_Shop` | 5984 | 2019-08-21 02:41:17Z | 11149 | 42671 | 200 | `https://web.archive.org/web/20190821024117id_/https://vsfan.net/wiki/Fight_Club_Shop` |
| `Flamestone_Basin` | 3270 | 2019-08-21 03:12:57Z | 10608 | 37698 | 200 | `https://web.archive.org/web/20190821031257id_/https://vsfan.net/wiki/Flamestone_Basin` |
| `Flowers,_Blood_And_The_Maiden` | 6204 | 2019-09-20 18:40:20Z | 11329 | 51651 | 200 | `https://web.archive.org/web/20190920184020id_/https://vsfan.net/wiki/Flowers,_Blood_And_The_Maiden` |
| `Forest_of_the_Wanderers` | 6142 | 2019-08-21 03:16:10Z | 10595 | 37741 | 200 | `https://web.archive.org/web/20190821031610id_/https://vsfan.net/wiki/Forest_of_the_Wanderers` |
| `Garantili_Hizmet_Ayrıcalıkları` | 6364 | 2019-09-23 07:40:32Z | 7159 | 19244 | 200 | `https://web.archive.org/web/20190923074032id_/https://vsfan.net/wiki/Garantili_Hizmet_Ayr%C4%B1cal%C4%B1klar%C4%B1` |
| `Gerard` | 2403 | 2019-08-26 08:29:53Z | 16588 | 108544 | 200 | `https://web.archive.org/web/20190826082953id_/https://vsfan.net/wiki/Gerard` |
| `Germination` | 7310 | 2019-08-21 01:00:46Z | 9482 | 34310 | 200 | `https://web.archive.org/web/20190821010046id_/https://vsfan.net/wiki/Germination` |
| `Giant's_Shelter` | 3375 | 2019-08-26 07:30:39Z | 10622 | 37684 | 200 | `https://web.archive.org/web/20190826073039id_/https://vsfan.net/wiki/Giant%27s_Shelter` |
| `Golden_Abyss` | 4993 | 2019-08-21 02:56:13Z | 10409 | 36304 | 200 | `https://web.archive.org/web/20190821025613id_/https://vsfan.net/wiki/Golden_Abyss` |
| `Gray_Dawn` | 6247 | 2019-08-21 03:44:30Z | 9527 | 34524 | 200 | `https://web.archive.org/web/20190821034430id_/https://vsfan.net/wiki/Gray_Dawn` |
| `Gray_Valley` | 7451 | 2019-08-26 06:58:14Z | 10745 | 38010 | 200 | `https://web.archive.org/web/20190826065814id_/https://vsfan.net/wiki/Gray_Valley` |
| `Guide_to_Blustone` | 7465 | 2019-09-23 07:20:38Z | 16202 | 56316 | 200 | `https://web.archive.org/web/20190923072038id_/https://vsfan.net/wiki/Guide_to_Blustone` |
| `Gullveig` | 7432 | 2019-08-21 01:17:07Z | 15750 | 84096 | 200 | `https://web.archive.org/web/20190821011707id_/https://vsfan.net/wiki/Gullveig` |
| `Hızlı_Teslimat_Ve_Garanti_Kapsamı` | 6305 | 2019-09-23 06:59:45Z | 7404 | 19400 | 200 | `https://web.archive.org/web/20190923065945id_/https://vsfan.net/wiki/H%C4%B1zl%C4%B1_Teslimat_Ve_Garanti_Kapsam%C4%B1` |
| `Halloween_Abyss` | 6031 | 2019-08-21 02:58:27Z | 10342 | 36078 | 200 | `https://web.archive.org/web/20190821025827id_/https://vsfan.net/wiki/Halloween_Abyss` |
| `Hamster_Dostlarına_Müjdeli_Haber` | 6372 | 2019-09-20 18:16:17Z | 7232 | 19279 | 200 | `https://web.archive.org/web/20190920181617id_/https://vsfan.net/wiki/Hamster_Dostlar%C4%B1na_M%C3%BCjdeli_Haber` |
| `Handsome_Man_Found` | 6135 | 2019-08-21 00:49:19Z | 11104 | 53204 | 200 | `https://web.archive.org/web/20190821004919id_/https://vsfan.net/wiki/Handsome_Man_Found` |
| `Handsome_Vote` | 6236 | 2019-08-21 01:02:33Z | 11193 | 53049 | 200 | `https://web.archive.org/web/20190821010233id_/https://vsfan.net/wiki/Handsome_Vote` |
| `Harley` | 7394 | 2019-08-21 03:04:24Z | 14744 | 77526 | 200 | `https://web.archive.org/web/20190821030424id_/https://vsfan.net/wiki/Harley` |
| `Hawk_Turn_Highlands` | 6145 | 2019-08-21 03:00:56Z | 10581 | 37483 | 200 | `https://web.archive.org/web/20190821030056id_/https://vsfan.net/wiki/Hawk_Turn_Highlands` |
| `He's_Here!_Lantern_Is_Here!` | 5319 | 2019-09-23 06:58:35Z | 11433 | 50470 | 200 | `https://web.archive.org/web/20190923065835id_/https://vsfan.net/wiki/He%27s_Here!_Lantern_Is_Here!` |
| `Hecate` | 2434 | 2019-08-21 03:45:34Z | 16871 | 127568 | 200 | `https://web.archive.org/web/20190821034534id_/https://vsfan.net/wiki/Hecate` |
| `Heidi` | 7477 | 2019-08-21 02:40:44Z | 15638 | 79587 | 200 | `https://web.archive.org/web/20190821024044id_/https://vsfan.net/wiki/Heidi` |
| `Hem_Evinizi_Hem_De_Işyerinizi_Taşıyoruz` | 6284 | 2019-09-20 18:14:29Z | 7404 | 19591 | 200 | `https://web.archive.org/web/20190920181429id_/https://vsfan.net/wiki/Hem_Evinizi_Hem_De_I%C5%9Fyerinizi_Ta%C5%9F%C4%B1yoruz` |
| `Hem_Konfor_Hem_Tasarruf_Amaçlıyor` | 6337 | 2019-09-23 07:56:57Z | 7301 | 19258 | 200 | `https://web.archive.org/web/20190923075657id_/https://vsfan.net/wiki/Hem_Konfor_Hem_Tasarruf_Ama%C3%A7l%C4%B1yor` |
| `Hem_Sanat_Hem_De_Edebiyat_Dolu_Bir_Tarih` | 6331 | 2019-08-21 00:30:19Z | 7129 | 19141 | 200 | `https://web.archive.org/web/20190821003019id_/https://vsfan.net/wiki/Hem_Sanat_Hem_De_Edebiyat_Dolu_Bir_Tarih` |
| `Hem_Uygun_Fiyat_Hem_Yüksek_Kalite` | 6282 | 2019-09-23 08:01:12Z | 7345 | 19246 | 200 | `https://web.archive.org/web/20190923080112id_/https://vsfan.net/wiki/Hem_Uygun_Fiyat_Hem_Y%C3%BCksek_Kalite` |
| `Hermes` | 7349 | 2019-08-26 08:11:15Z | 16700 | 113204 | 200 | `https://web.archive.org/web/20190826081115id_/https://vsfan.net/wiki/Hermes` |
| `Hidden_Functions` | 6093 | 2019-09-23 06:58:11Z | 11252 | 49272 | 200 | `https://web.archive.org/web/20190923065811id_/https://vsfan.net/wiki/Hidden_Functions` |
| `His_and_Her_Bat` | 6100 | 2019-09-23 07:55:22Z | 10822 | 44547 | 200 | `https://web.archive.org/web/20190923075522id_/https://vsfan.net/wiki/His_and_Her_Bat` |
| `His_Past` | 6223 | 2019-08-21 00:42:19Z | 10983 | 45714 | 200 | `https://web.archive.org/web/20190821004219id_/https://vsfan.net/wiki/His_Past` |
| `Honorable_Warrior` | 5930 | 2019-08-21 01:29:19Z | 11030 | 48837 | 200 | `https://web.archive.org/web/20190821012919id_/https://vsfan.net/wiki/Honorable_Warrior` |
| `Human` | 4450 | 2019-08-21 00:44:04Z | 10050 | 34798 | 200 | `https://web.archive.org/web/20190821004404id_/https://vsfan.net/wiki/Human` |
| `Humans` | 4450 | 2019-09-23 07:52:43Z | 10044 | 34802 | 200 | `https://web.archive.org/web/20190923075243id_/https://vsfan.net/wiki/Humans` |
| `Hunter` | 2091 | 2019-08-26 07:21:45Z | 12255 | 45425 | 200 | `https://web.archive.org/web/20190826072145id_/https://vsfan.net/wiki/Hunter` |
| `Hunter_Gym` | 3172 | 2019-08-26 07:54:02Z | 10665 | 37428 | 200 | `https://web.archive.org/web/20190826075402id_/https://vsfan.net/wiki/Hunter_Gym` |
| `Hunter_Shop` | 3227 | 2019-08-26 07:30:11Z | 10506 | 36851 | 200 | `https://web.archive.org/web/20190826073011id_/https://vsfan.net/wiki/Hunter_Shop` |
| `Hunter_Supply_Office` | 6016 | 2019-08-21 01:12:35Z | 7874 | 26283 | 200 | `https://web.archive.org/web/20190821011235id_/https://vsfan.net/wiki/Hunter_Supply_Office` |
| `Hunter_Supply_Station` | 3191 | 2019-08-21 02:45:36Z | 10345 | 36312 | 200 | `https://web.archive.org/web/20190821024536id_/https://vsfan.net/wiki/Hunter_Supply_Station` |
| `Hunters` | 2091 | 2019-08-21 01:22:52Z | 12350 | 45750 | 200 | `https://web.archive.org/web/20190821012252id_/https://vsfan.net/wiki/Hunters` |
| `Hunters'_Drop_Rate` | 6231 | 2019-08-21 01:02:27Z | 7151 | 18719 | 200 | `https://web.archive.org/web/20190821010227id_/https://vsfan.net/wiki/Hunters%27_Drop_Rate` |
| `Hyuntae` | 4571 | 2019-08-21 01:32:32Z | 9570 | 34642 | 200 | `https://web.archive.org/web/20190821013232id_/https://vsfan.net/wiki/Hyuntae` |
| `Idiot_vs._Loan_Shark` | 6007 | 2019-08-21 00:50:31Z | 11191 | 54442 | 200 | `https://web.archive.org/web/20190821005031id_/https://vsfan.net/wiki/Idiot_vs._Loan_Shark` |
| `Ignoring_Orders` | 6042 | 2019-08-21 00:47:10Z | 11057 | 46598 | 200 | `https://web.archive.org/web/20190821004710id_/https://vsfan.net/wiki/Ignoring_Orders` |
| `Illusion?` | 5344 | 2019-08-21 01:25:09Z | 7068 | 21052 | 200 | `https://web.archive.org/web/20190821012509id_/https://vsfan.net/wiki/Illusion%3F` |
| `Infamous_Client` | 5917 | 2019-09-23 08:00:51Z | 11133 | 50066 | 200 | `https://web.archive.org/web/20190923080051id_/https://vsfan.net/wiki/Infamous_Client` |
| `Jack` | 3134 | 2019-08-21 03:08:30Z | 10988 | 38521 | 200 | `https://web.archive.org/web/20190821030830id_/https://vsfan.net/wiki/Jack` |
| `Jae` | 5651 | 2019-08-26 08:18:46Z | 9664 | 34683 | 200 | `https://web.archive.org/web/20190826081846id_/https://vsfan.net/wiki/Jae` |
| `Jang` | 5880 | 2019-09-23 07:40:44Z | 9519 | 34473 | 200 | `https://web.archive.org/web/20190923074044id_/https://vsfan.net/wiki/Jang` |
| `Ji_Hoon` | 5656 | 2019-08-21 03:11:11Z | 9551 | 34526 | 200 | `https://web.archive.org/web/20190821031111id_/https://vsfan.net/wiki/Ji_Hoon` |
| `Jina` | 5658 | 2019-08-21 03:05:31Z | 9512 | 34416 | 200 | `https://web.archive.org/web/20190821030531id_/https://vsfan.net/wiki/Jina` |
| `Joy` | 7456 | 2019-08-21 02:42:00Z | 16302 | 82549 | 200 | `https://web.archive.org/web/20190821024200id_/https://vsfan.net/wiki/Joy` |
| `Juno` | 7484 | 2019-08-26 08:13:48Z | 11954 | 46112 | 200 | `https://web.archive.org/web/20190826081348id_/https://vsfan.net/wiki/Juno` |
| `Kain` | 7460 | 2019-08-26 06:57:54Z | 18339 | 118382 | 200 | `https://web.archive.org/web/20190826065754id_/https://vsfan.net/wiki/Kain` |
| `Kalite_Ve_Hız_Bir_Arada_Sunuluyor` | 6352 | 2019-08-21 01:05:46Z | 7342 | 19219 | 200 | `https://web.archive.org/web/20190821010546id_/https://vsfan.net/wiki/Kalite_Ve_H%C4%B1z_Bir_Arada_Sunuluyor` |
| `Kaliteli_Ve_Uygun_Koşullarda_Hizmet_Deneyimi` | 6350 | 2019-09-23 08:03:04Z | 7147 | 19367 | 200 | `https://web.archive.org/web/20190923080304id_/https://vsfan.net/wiki/Kaliteli_Ve_Uygun_Ko%C5%9Fullarda_Hizmet_Deneyimi` |
| `Karl` | 7370 | 2019-09-23 07:55:50Z | 15751 | 94687 | 200 | `https://web.archive.org/web/20190923075550id_/https://vsfan.net/wiki/Karl` |
| `Karl_Steiner` | 7370 | 2019-08-21 00:53:32Z | 15690 | 94364 | 200 | `https://web.archive.org/web/20190821005332id_/https://vsfan.net/wiki/Karl_Steiner` |
| `Kripto_Para_Nedir_Nasıl_Kazanılır` | 6328 | 2019-09-20 18:11:53Z | 7143 | 19216 | 200 | `https://web.archive.org/web/20190920181153id_/https://vsfan.net/wiki/Kripto_Para_Nedir_Nas%C4%B1l_Kazan%C4%B1l%C4%B1r` |
| `Ladies'_Dinner` | 6079 | 2019-09-23 08:00:56Z | 11127 | 48831 | 200 | `https://web.archive.org/web/20190923080056id_/https://vsfan.net/wiki/Ladies%27_Dinner` |
| `Lana` | 3143 | 2019-08-26 07:07:58Z | 11124 | 38987 | 200 | `https://web.archive.org/web/20190826070758id_/https://vsfan.net/wiki/Lana` |
| `Lantern` | 7415 | 2019-08-21 02:58:13Z | 20996 | 173580 | 200 | `https://web.archive.org/web/20190821025813id_/https://vsfan.net/wiki/Lantern` |
| `Lapis` | 7350 | 2019-08-21 03:10:04Z | 16248 | 111618 | 200 | `https://web.archive.org/web/20190821031004id_/https://vsfan.net/wiki/Lapis` |
| `Last_Soldier` | 5890 | 2019-08-21 01:14:18Z | 11384 | 52989 | 200 | `https://web.archive.org/web/20190821011418id_/https://vsfan.net/wiki/Last_Soldier` |
| `Lead_Heart` | 6250 | 2019-08-26 06:57:25Z | 9531 | 34680 | 200 | `https://web.archive.org/web/20190826065725id_/https://vsfan.net/wiki/Lead_Heart` |
| `Leonardo` | 4531 | 2019-08-26 08:20:58Z | 8459 | 25044 | 200 | `https://web.archive.org/web/20190826082058id_/https://vsfan.net/wiki/Leonardo` |
| `Levi` | 2536 | 2019-08-21 02:42:04Z | 18408 | 156538 | 200 | `https://web.archive.org/web/20190821024204id_/https://vsfan.net/wiki/Levi` |
| `Lily_&_Lyla` | 7375 | 2019-08-21 02:40:23Z | 15099 | 75606 | 200 | `https://web.archive.org/web/20190821024023id_/https://vsfan.net/wiki/Lily_%26_Lyla` |
| `List_of_Blustone_Items` | 5115 | 2019-08-21 02:41:34Z | 18289 | 104950 | 200 | `https://web.archive.org/web/20190821024134id_/https://vsfan.net/wiki/List_of_Blustone_Items` |
| `List_of_Blustone_Stories` | 7461 | 2019-08-21 03:43:42Z | 43474 | 355828 | 200 | `https://web.archive.org/web/20190821034342id_/https://vsfan.net/wiki/List_of_Blustone_Stories` |
| `List_of_Hunters` | 7480 | 2019-08-26 08:27:17Z | 20898 | 210780 | 200 | `https://web.archive.org/web/20190826082717id_/https://vsfan.net/wiki/List_of_Hunters` |
| `Little_Brothers` | 6097 | 2019-08-21 00:29:52Z | 11012 | 48049 | 200 | `https://web.archive.org/web/20190821002952id_/https://vsfan.net/wiki/Little_Brothers` |
| `Locke` | 2735 | 2019-08-21 03:55:34Z | 15264 | 98656 | 200 | `https://web.archive.org/web/20190821035534id_/https://vsfan.net/wiki/Locke` |
| `Lottery_Mouse` | 3094 | 2019-08-26 06:56:59Z | 11100 | 39398 | 200 | `https://web.archive.org/web/20190826065659id_/https://vsfan.net/wiki/Lottery_Mouse` |
| `Main_Page` | 2082 | 2017-08-25 06:33:14Z | 8365 | 34622 | 200 | `https://web.archive.org/web/20170825063314id_/https://vsfan.net/wiki/Main_Page` |
| `Metis` | 2560 | 2019-08-26 07:44:48Z | 15775 | 101258 | 200 | `https://web.archive.org/web/20190826074448id_/https://vsfan.net/wiki/Metis` |
| `Midgard` | 4361 | 2019-08-21 03:34:29Z | 10282 | 35730 | 200 | `https://web.archive.org/web/20190821033429id_/https://vsfan.net/wiki/Midgard` |
| `Midgard_Ice_Zone` | 3342 | 2019-08-26 06:57:11Z | 10929 | 39071 | 200 | `https://web.archive.org/web/20190826065711id_/https://vsfan.net/wiki/Midgard_Ice_Zone` |
| `Midgard_Snowfields` | 3248 | 2019-08-21 03:37:03Z | 11040 | 39752 | 200 | `https://web.archive.org/web/20190821033703id_/https://vsfan.net/wiki/Midgard_Snowfields` |
| `Midnight_Prayer` | 6027 | 2019-09-23 07:02:12Z | 11136 | 49516 | 200 | `https://web.archive.org/web/20190923070212id_/https://vsfan.net/wiki/Midnight_Prayer` |
| `Missing_Cargo` | 6254 | 2019-08-26 07:33:34Z | 9543 | 34759 | 200 | `https://web.archive.org/web/20190826073334id_/https://vsfan.net/wiki/Missing_Cargo` |
| `Mister` | 6103 | 2019-08-21 00:30:23Z | 11297 | 52364 | 200 | `https://web.archive.org/web/20190821003023id_/https://vsfan.net/wiki/Mister` |
| `Monsters` | 5833 | 2019-09-23 07:00:11Z | 6359 | 16465 | 200 | `https://web.archive.org/web/20190923070011id_/https://vsfan.net/wiki/Monsters` |
| `Motivations` | 6043 | 2019-09-23 08:09:29Z | 10833 | 44416 | 200 | `https://web.archive.org/web/20190923080929id_/https://vsfan.net/wiki/Motivations` |
| `Mowgli` | 7346 | 2019-08-21 03:11:47Z | 16097 | 96712 | 200 | `https://web.archive.org/web/20190821031147id_/https://vsfan.net/wiki/Mowgli` |
| `Mowgli's_Forest` | 5908 | 2019-09-23 06:59:26Z | 10904 | 46326 | 200 | `https://web.archive.org/web/20190923065926id_/https://vsfan.net/wiki/Mowgli%27s_Forest` |
| `Mt._Black_Rock` | 3413 | 2019-08-21 00:50:17Z | 10622 | 37609 | 200 | `https://web.archive.org/web/20190821005017id_/https://vsfan.net/wiki/Mt._Black_Rock` |
| `Natalia` | 7393 | 2019-08-26 07:02:07Z | 15822 | 82181 | 200 | `https://web.archive.org/web/20190826070207id_/https://vsfan.net/wiki/Natalia` |
| `Need_Your_Love` | 6203 | 2019-08-21 00:44:12Z | 11072 | 47558 | 200 | `https://web.archive.org/web/20190821004412id_/https://vsfan.net/wiki/Need_Your_Love` |
| `Nene` | 2920 | 2019-08-21 00:31:20Z | 16355 | 96493 | 200 | `https://web.archive.org/web/20190821003120id_/https://vsfan.net/wiki/Nene` |
| `No_Escape` | 6268 | 2019-08-21 02:39:43Z | 10785 | 39134 | 200 | `https://web.archive.org/web/20190821023943id_/https://vsfan.net/wiki/No_Escape` |
| `No_Killing_Permitted` | 6202 | 2019-08-21 00:53:40Z | 11019 | 45835 | 200 | `https://web.archive.org/web/20190821005340id_/https://vsfan.net/wiki/No_Killing_Permitted` |
| `No_Spitting_Anywhere` | 6114 | 2019-08-21 01:28:59Z | 11132 | 48970 | 200 | `https://web.archive.org/web/20190821012859id_/https://vsfan.net/wiki/No_Spitting_Anywhere` |
| `Non-melting_Forest` | 3279 | 2019-08-21 02:40:28Z | 10614 | 37764 | 200 | `https://web.archive.org/web/20190821024028id_/https://vsfan.net/wiki/Non-melting_Forest` |
| `North_Highlands` | 3351 | 2019-08-21 03:17:19Z | 10619 | 37721 | 200 | `https://web.archive.org/web/20190821031719id_/https://vsfan.net/wiki/North_Highlands` |
| `Octavia` | 2944 | 2019-08-26 07:57:06Z | 15937 | 103787 | 200 | `https://web.archive.org/web/20190826075706id_/https://vsfan.net/wiki/Octavia` |
| `Ornithopter_Platform` | 3153 | 2019-08-26 08:28:00Z | 10319 | 36223 | 200 | `https://web.archive.org/web/20190826082800id_/https://vsfan.net/wiki/Ornithopter_Platform` |
| `Otomasyon_Sistemleri_Almanya’da_Oldukça_Popüler` | 6335 | 2019-08-21 00:44:48Z | 7290 | 19854 | 200 | `https://web.archive.org/web/20190821004448id_/https://vsfan.net/wiki/Otomasyon_Sistemleri_Almanya%E2%80%99da_Olduk%C3%A7a_Pop%C3%BCler` |
| `Our_Fate_In_The_Stars` | 5991 | 2019-08-21 00:34:26Z | 11093 | 49204 | 200 | `https://web.archive.org/web/20190821003426id_/https://vsfan.net/wiki/Our_Fate_In_The_Stars` |
| `PandaHawk` | 3217 | 2019-08-21 00:31:04Z | 11290 | 42232 | 200 | `https://web.archive.org/web/20190821003104id_/https://vsfan.net/wiki/PandaHawk` |
| `Pansy` | 7458 | 2019-08-21 02:49:53Z | 15601 | 77514 | 200 | `https://web.archive.org/web/20190821024953id_/https://vsfan.net/wiki/Pansy` |
| `Papillon` | 7427 | 2019-08-21 03:57:10Z | 16056 | 83627 | 200 | `https://web.archive.org/web/20190821035710id_/https://vsfan.net/wiki/Papillon` |
| `Parallel_Lives` | 6149 | 2019-08-21 01:31:17Z | 11394 | 54937 | 200 | `https://web.archive.org/web/20190821013117id_/https://vsfan.net/wiki/Parallel_Lives` |
| `Patch_0.9.3_(Blustone)` | 4244 | 2019-09-23 06:59:51Z | 11191 | 38929 | 200 | `https://web.archive.org/web/20190923065951id_/https://vsfan.net/wiki/Patch_0.9.3_(Blustone)` |
| `Patch_0.9.4_(Blustone)` | 4255 | 2019-09-23 07:17:04Z | 10781 | 37691 | 200 | `https://web.archive.org/web/20190923071704id_/https://vsfan.net/wiki/Patch_0.9.4_(Blustone)` |
| `Patch_0.9.5_(Blustone)` | 4258 | 2019-08-21 01:14:29Z | 10849 | 37748 | 200 | `https://web.archive.org/web/20190821011429id_/https://vsfan.net/wiki/Patch_0.9.5_(Blustone)` |
| `Patch_0.9.6_(Blustone)` | 4262 | 2019-09-20 18:09:46Z | 11154 | 38559 | 200 | `https://web.archive.org/web/20190920180946id_/https://vsfan.net/wiki/Patch_0.9.6_(Blustone)` |
| `Patch_0.9.7_(Blustone)` | 4268 | 2019-08-21 00:30:40Z | 10877 | 37853 | 200 | `https://web.archive.org/web/20190821003040id_/https://vsfan.net/wiki/Patch_0.9.7_(Blustone)` |
| `Patch_0.9.8.1_(Blustone)` | 4272 | 2019-09-23 07:31:06Z | 10591 | 37094 | 200 | `https://web.archive.org/web/20190923073106id_/https://vsfan.net/wiki/Patch_0.9.8.1_(Blustone)` |
| `Patch_0.9.8_(Blustone)` | 4269 | 2019-08-21 00:48:16Z | 10940 | 38284 | 200 | `https://web.archive.org/web/20190821004816id_/https://vsfan.net/wiki/Patch_0.9.8_(Blustone)` |
| `Patch_0.9.9_(Blustone)` | 4275 | 2019-08-21 01:10:21Z | 10824 | 37887 | 200 | `https://web.archive.org/web/20190821011021id_/https://vsfan.net/wiki/Patch_0.9.9_(Blustone)` |
| `Patch_1.0.0.3_(Blustone)` | 4287 | 2019-08-21 01:23:52Z | 10836 | 37942 | 200 | `https://web.archive.org/web/20190821012352id_/https://vsfan.net/wiki/Patch_1.0.0.3_(Blustone)` |
| `Patch_1.0.0_(Blustone)` | 4282 | 2019-09-20 18:45:55Z | 10993 | 38426 | 200 | `https://web.archive.org/web/20190920184555id_/https://vsfan.net/wiki/Patch_1.0.0_(Blustone)` |
| `Patch_1.0.1.0_(Blustone)` | 4479 | 2019-08-21 01:12:08Z | 11052 | 38301 | 200 | `https://web.archive.org/web/20190821011208id_/https://vsfan.net/wiki/Patch_1.0.1.0_(Blustone)` |
| `Patch_1.0.1.1_(Blustone)` | 4481 | 2019-08-21 00:29:56Z | 10599 | 36927 | 200 | `https://web.archive.org/web/20190821002956id_/https://vsfan.net/wiki/Patch_1.0.1.1_(Blustone)` |
| `Patch_1.0.2.0_(Blustone)` | 4484 | 2019-09-23 08:08:34Z | 11210 | 38792 | 200 | `https://web.archive.org/web/20190923080834id_/https://vsfan.net/wiki/Patch_1.0.2.0_(Blustone)` |
| `Patch_1.0.3.0_(Blustone)` | 4486 | 2019-09-23 06:59:14Z | 10864 | 38230 | 200 | `https://web.archive.org/web/20190923065914id_/https://vsfan.net/wiki/Patch_1.0.3.0_(Blustone)` |
| `Patch_1.0.4.0_(Blustone)` | 4487 | 2019-09-23 07:09:11Z | 10610 | 37072 | 200 | `https://web.archive.org/web/20190923070911id_/https://vsfan.net/wiki/Patch_1.0.4.0_(Blustone)` |
| `Patch_1.0.5.0_(Blustone)` | 4489 | 2019-08-21 01:07:55Z | 10813 | 37774 | 200 | `https://web.archive.org/web/20190821010755id_/https://vsfan.net/wiki/Patch_1.0.5.0_(Blustone)` |
| `Patch_1.0.6.1_(Blustone)` | 4491 | 2019-09-23 07:01:53Z | 10739 | 37522 | 200 | `https://web.archive.org/web/20190923070153id_/https://vsfan.net/wiki/Patch_1.0.6.1_(Blustone)` |
| `Patch_1.0.7.0_(Blustone)` | 4493 | 2019-09-23 06:58:30Z | 11148 | 38658 | 200 | `https://web.archive.org/web/20190923065830id_/https://vsfan.net/wiki/Patch_1.0.7.0_(Blustone)` |
| `Patch_1.0.7.2_(Blustone)` | 4494 | 2019-08-21 00:29:30Z | 10953 | 38278 | 200 | `https://web.archive.org/web/20190821002930id_/https://vsfan.net/wiki/Patch_1.0.7.2_(Blustone)` |
| `Patch_1.0.7.3_(Blustone)` | 4495 | 2019-09-23 07:18:03Z | 10720 | 37413 | 200 | `https://web.archive.org/web/20190923071803id_/https://vsfan.net/wiki/Patch_1.0.7.3_(Blustone)` |
| `Patch_1.0.8.0_(Blustone)` | 4251 | 2019-08-21 00:41:45Z | 11424 | 40120 | 200 | `https://web.archive.org/web/20190821004145id_/https://vsfan.net/wiki/Patch_1.0.8.0_(Blustone)` |
| `Patch_1.1.0.0_(Blustone)` | 4376 | 2019-09-23 06:57:20Z | 11103 | 38332 | 200 | `https://web.archive.org/web/20190923065720id_/https://vsfan.net/wiki/Patch_1.1.0.0_(Blustone)` |
| `Patch_1.1.1.0_(Blustone)` | 4591 | 2019-08-21 00:30:56Z | 11293 | 39387 | 200 | `https://web.archive.org/web/20190821003056id_/https://vsfan.net/wiki/Patch_1.1.1.0_(Blustone)` |
| `Patch_1.1.2.0_(Blustone)` | 5287 | 2019-09-23 07:15:23Z | 11179 | 40003 | 200 | `https://web.archive.org/web/20190923071523id_/https://vsfan.net/wiki/Patch_1.1.2.0_(Blustone)` |
| `Patch_1.1.3.0_(Blustone)` | 5662 | 2019-09-23 07:42:31Z | 11246 | 38993 | 200 | `https://web.archive.org/web/20190923074231id_/https://vsfan.net/wiki/Patch_1.1.3.0_(Blustone)` |
| `Patch_1.1.4.0_(Blustone)` | 5716 | 2019-08-21 01:35:51Z | 11250 | 38632 | 200 | `https://web.archive.org/web/20190821013551id_/https://vsfan.net/wiki/Patch_1.1.4.0_(Blustone)` |
| `Patch_1.1.5.0_(Blustone)` | 5897 | 2019-09-20 18:13:53Z | 11639 | 40608 | 200 | `https://web.archive.org/web/20190920181353id_/https://vsfan.net/wiki/Patch_1.1.5.0_(Blustone)` |
| `Patch_1.1.6.0_(Blustone)` | 6089 | 2019-08-21 00:46:44Z | 11031 | 37968 | 200 | `https://web.archive.org/web/20190821004644id_/https://vsfan.net/wiki/Patch_1.1.6.0_(Blustone)` |
| `Patch_1.1.7.0_(Blustone)` | 6090 | 2019-09-23 07:37:14Z | 10901 | 37610 | 200 | `https://web.archive.org/web/20190923073714id_/https://vsfan.net/wiki/Patch_1.1.7.0_(Blustone)` |
| `Patrone` | 7439 | 2019-08-26 07:55:47Z | 18361 | 122245 | 200 | `https://web.archive.org/web/20190826075547id_/https://vsfan.net/wiki/Patrone` |
| `Peppermint` | 3281 | 2019-09-23 07:53:26Z | 6447 | 16658 | 200 | `https://web.archive.org/web/20190923075326id_/https://vsfan.net/wiki/Peppermint` |
| `Pet_guidebook` | 6341 | 2019-09-23 07:59:45Z | 11160 | 51322 | 200 | `https://web.archive.org/web/20190923075945id_/https://vsfan.net/wiki/Pet_guidebook` |
| `Polar_Bear` | 4467 | 2019-08-21 02:57:36Z | 11353 | 42088 | 200 | `https://web.archive.org/web/20190821025736id_/https://vsfan.net/wiki/Polar_Bear` |
| `Polar_Bear_Greetings` | 5903 | 2019-09-23 06:59:58Z | 10996 | 47632 | 200 | `https://web.archive.org/web/20190923065958id_/https://vsfan.net/wiki/Polar_Bear_Greetings` |
| `Popüler_Olmak_Sizin_De_Hakkınız` | 6356 | 2019-08-21 00:28:55Z | 7416 | 19557 | 200 | `https://web.archive.org/web/20190821002855id_/https://vsfan.net/wiki/Pop%C3%BCler_Olmak_Sizin_De_Hakk%C4%B1n%C4%B1z` |
| `Post_Office` | 3198 | 2019-08-26 07:43:07Z | 10310 | 35981 | 200 | `https://web.archive.org/web/20190826074307id_/https://vsfan.net/wiki/Post_Office` |
| `Promises` | 5921 | 2019-08-21 00:36:00Z | 11015 | 48176 | 200 | `https://web.archive.org/web/20190821003600id_/https://vsfan.net/wiki/Promises` |
| `Proof_That_He's_Nice` | 6342 | 2019-08-21 00:29:35Z | 11443 | 55920 | 200 | `https://web.archive.org/web/20190821002935id_/https://vsfan.net/wiki/Proof_That_He%27s_Nice` |
| `Purchase` | 5987 | 2019-08-21 01:11:08Z | 10911 | 40550 | 200 | `https://web.archive.org/web/20190821011108id_/https://vsfan.net/wiki/Purchase` |
| `Rebecca` | 7447 | 2019-08-21 03:18:06Z | 18354 | 135119 | 200 | `https://web.archive.org/web/20190821031806id_/https://vsfan.net/wiki/Rebecca` |
| `Red` | 4231 | 2019-08-21 03:38:06Z | 10457 | 36315 | 200 | `https://web.archive.org/web/20190821033806id_/https://vsfan.net/wiki/Red` |
| `Riko` | 2615 | 2019-08-21 03:04:11Z | 15427 | 87653 | 200 | `https://web.archive.org/web/20190821030411id_/https://vsfan.net/wiki/Riko` |
| `Robin` | 2638 | 2019-08-26 08:19:27Z | 15719 | 96681 | 200 | `https://web.archive.org/web/20190826081927id_/https://vsfan.net/wiki/Robin` |
| `Roles` | 2091 | 2019-09-20 18:44:54Z | 12365 | 45781 | 200 | `https://web.archive.org/web/20190920184454id_/https://vsfan.net/wiki/Roles` |
| `Rotation_Area` | 5778 | 2019-08-21 02:47:55Z | 11341 | 42881 | 200 | `https://web.archive.org/web/20190821024755id_/https://vsfan.net/wiki/Rotation_Area` |
| `Santa_Clauster` | 7433 | 2019-08-26 07:02:45Z | 14823 | 80976 | 200 | `https://web.archive.org/web/20190826070245id_/https://vsfan.net/wiki/Santa_Clauster` |
| `Sapien` | 4450 | 2019-08-21 01:25:14Z | 9945 | 34481 | 200 | `https://web.archive.org/web/20190821012514id_/https://vsfan.net/wiki/Sapien` |
| `Sapiens` | 4450 | 2019-08-21 00:30:48Z | 10033 | 34806 | 200 | `https://web.archive.org/web/20190821003048id_/https://vsfan.net/wiki/Sapiens` |
| `Scar` | 7455 | 2019-08-21 03:57:19Z | 18342 | 123062 | 200 | `https://web.archive.org/web/20190821035719id_/https://vsfan.net/wiki/Scar` |
| `Schumann` | 3084 | 2019-08-21 01:14:58Z | 10620 | 37130 | 200 | `https://web.archive.org/web/20190821011458id_/https://vsfan.net/wiki/Schumann` |
| `Searching_for_Belle` | 5768 | 2019-08-21 00:29:15Z | 9416 | 28471 | 200 | `https://web.archive.org/web/20190821002915id_/https://vsfan.net/wiki/Searching_for_Belle` |
| `Seo_Hyun` | 5879 | 2019-08-21 00:29:07Z | 9531 | 34428 | 200 | `https://web.archive.org/web/20190821002907id_/https://vsfan.net/wiki/Seo_Hyun` |
| `Sienna` | 7414 | 2019-08-26 07:15:03Z | 18604 | 131971 | 200 | `https://web.archive.org/web/20190826071503id_/https://vsfan.net/wiki/Sienna` |
| `Silent_Forest` | 3401 | 2019-08-21 03:18:11Z | 10598 | 37592 | 200 | `https://web.archive.org/web/20190821031811id_/https://vsfan.net/wiki/Silent_Forest` |
| `Skills_Sharpened_By_Hardships` | 6206 | 2019-09-16 20:16:04Z | 11065 | 46250 | 200 | `https://web.archive.org/web/20190916201604id_/https://vsfan.net/wiki/Skills_Sharpened_By_Hardships` |
| `Skin_Care` | 6095 | 2019-09-23 07:00:20Z | 11141 | 50532 | 200 | `https://web.archive.org/web/20190923070020id_/https://vsfan.net/wiki/Skin_Care` |
| `Solid_and_Soft` | 6110 | 2019-08-21 01:24:13Z | 10824 | 45637 | 200 | `https://web.archive.org/web/20190821012413id_/https://vsfan.net/wiki/Solid_and_Soft` |
| `Stalker_vs._Loan_Shark` | 6075 | 2019-09-20 18:13:14Z | 11116 | 45817 | 200 | `https://web.archive.org/web/20190920181314id_/https://vsfan.net/wiki/Stalker_vs._Loan_Shark` |
| `Straitjacket` | 6244 | 2019-08-26 06:59:04Z | 9532 | 34647 | 200 | `https://web.archive.org/web/20190826065904id_/https://vsfan.net/wiki/Straitjacket` |
| `Strange_Woman` | 4362 | 2019-08-21 00:29:44Z | 7258 | 19235 | 200 | `https://web.archive.org/web/20190821002944id_/https://vsfan.net/wiki/Strange_Woman` |
| `Stubborn_Defense` | 6280 | 2019-09-23 07:15:11Z | 10963 | 49931 | 200 | `https://web.archive.org/web/20190923071511id_/https://vsfan.net/wiki/Stubborn_Defense` |
| `Sunny` | 7322 | 2019-08-21 03:06:44Z | 14990 | 67327 | 200 | `https://web.archive.org/web/20190821030644id_/https://vsfan.net/wiki/Sunny` |
| `Suspicious_Shop` | 7360 | 2019-08-21 02:40:10Z | 10539 | 37045 | 200 | `https://web.archive.org/web/20190821024010id_/https://vsfan.net/wiki/Suspicious_Shop` |
| `Sweet_Bombs` | 5900 | 2019-08-21 00:30:10Z | 10864 | 44016 | 200 | `https://web.archive.org/web/20190821003010id_/https://vsfan.net/wiki/Sweet_Bombs` |
| `Sylvester` | 2722 | 2019-08-21 01:03:28Z | 18859 | 164839 | 200 | `https://web.archive.org/web/20190821010328id_/https://vsfan.net/wiki/Sylvester` |
| `Take_Care_of_the_Teddies` | 5923 | 2019-09-23 07:01:26Z | 11242 | 52635 | 200 | `https://web.archive.org/web/20190923070126id_/https://vsfan.net/wiki/Take_Care_of_the_Teddies` |
| `Teddy_Bomber` | 2971 | 2019-08-21 03:44:51Z | 14931 | 82070 | 200 | `https://web.archive.org/web/20190821034451id_/https://vsfan.net/wiki/Teddy_Bomber` |
| `TeddyBomber` | 2971 | 2019-08-21 00:29:11Z | 15015 | 82423 | 200 | `https://web.archive.org/web/20190821002911id_/https://vsfan.net/wiki/TeddyBomber` |
| `The_Battle_Of_Survival` | 5999 | 2019-08-21 00:59:11Z | 10964 | 44849 | 200 | `https://web.archive.org/web/20190821005911id_/https://vsfan.net/wiki/The_Battle_Of_Survival` |
| `The_Belly_of_the_Beast` | 6264 | 2019-08-21 02:40:19Z | 9549 | 34919 | 200 | `https://web.archive.org/web/20190821024019id_/https://vsfan.net/wiki/The_Belly_of_the_Beast` |
| `The_Disobedient_Soldier` | 6035 | 2019-08-21 00:42:00Z | 10819 | 43065 | 200 | `https://web.archive.org/web/20190821004200id_/https://vsfan.net/wiki/The_Disobedient_Soldier` |
| `The_First_Ever_Hunter` | 6207 | 2019-09-16 20:53:05Z | 11619 | 48575 | 200 | `https://web.archive.org/web/20190916205305id_/https://vsfan.net/wiki/The_First_Ever_Hunter` |
| `The_First_Fight` | 6066 | 2019-09-23 07:51:40Z | 10867 | 46124 | 200 | `https://web.archive.org/web/20190923075140id_/https://vsfan.net/wiki/The_First_Fight` |
| `The_Gardener_in_the_Maze` | 5768 | 2019-08-21 02:54:00Z | 9506 | 28890 | 200 | `https://web.archive.org/web/20190821025400id_/https://vsfan.net/wiki/The_Gardener_in_the_Maze` |
| `The_Girl_Who_Wouldn't_Wake_Up` | 5756 | 2019-08-26 07:12:21Z | 8573 | 25683 | 200 | `https://web.archive.org/web/20190826071221id_/https://vsfan.net/wiki/The_Girl_Who_Wouldn%27t_Wake_Up` |
| `The_Gold_Medal` | 6367 | 2019-09-23 08:04:59Z | 11222 | 52048 | 200 | `https://web.archive.org/web/20190923080459id_/https://vsfan.net/wiki/The_Gold_Medal` |
| `The_Perfect_Automatic_Bread_Make` | 6358 | 2019-09-23 07:55:10Z | 11123 | 47237 | 200 | `https://web.archive.org/web/20190923075510id_/https://vsfan.net/wiki/The_Perfect_Automatic_Bread_Make` |
| `The_Poison_and_the_Cure` | 6173 | 2019-08-21 02:39:56Z | 10647 | 38561 | 200 | `https://web.archive.org/web/20190821023956id_/https://vsfan.net/wiki/The_Poison_and_the_Cure` |
| `The_Secret_Origin_of_Judecca` | 5758 | 2019-08-26 07:45:36Z | 8558 | 25636 | 200 | `https://web.archive.org/web/20190826074536id_/https://vsfan.net/wiki/The_Secret_Origin_of_Judecca` |
| `The_Story_of_the_Sword` | 6106 | 2019-09-23 08:02:20Z | 11139 | 50859 | 200 | `https://web.archive.org/web/20190923080220id_/https://vsfan.net/wiki/The_Story_of_the_Sword` |
| `The_Truth_Within_the_Silence` | 6261 | 2019-08-26 06:56:49Z | 9626 | 35227 | 200 | `https://web.archive.org/web/20190826065649id_/https://vsfan.net/wiki/The_Truth_Within_the_Silence` |
| `The_Voice_that_Lingers` | 6190 | 2019-08-26 08:05:28Z | 9415 | 28453 | 200 | `https://web.archive.org/web/20190826080528id_/https://vsfan.net/wiki/The_Voice_that_Lingers` |
| `Therapy` | 7423 | 2019-08-21 02:49:52Z | 15355 | 80057 | 200 | `https://web.archive.org/web/20190821024952id_/https://vsfan.net/wiki/Therapy` |
| `To_Each_Their_Own_Skill` | 5841 | 2019-09-23 07:44:27Z | 11171 | 48486 | 200 | `https://web.archive.org/web/20190923074427id_/https://vsfan.net/wiki/To_Each_Their_Own_Skill` |
| `Troublemaker` | 6060 | 2019-09-23 08:01:04Z | 11049 | 46017 | 200 | `https://web.archive.org/web/20190923080104id_/https://vsfan.net/wiki/Troublemaker` |
| `Tutanın_Kısmeti_Açılıyor` | 6370 | 2019-09-20 18:19:48Z | 7161 | 19325 | 200 | `https://web.archive.org/web/20190920181948id_/https://vsfan.net/wiki/Tutan%C4%B1n_K%C4%B1smeti_A%C3%A7%C4%B1l%C4%B1yor` |
| `Two_Ice` | 6120 | 2019-08-21 00:30:06Z | 11301 | 53586 | 200 | `https://web.archive.org/web/20190821003006id_/https://vsfan.net/wiki/Two_Ice` |
| `Tyltyl` | 7377 | 2019-08-21 02:41:26Z | 20798 | 173351 | 200 | `https://web.archive.org/web/20190821024126id_/https://vsfan.net/wiki/Tyltyl` |
| `Underwater_Diplomacy` | 5763 | 2019-08-21 03:14:23Z | 8533 | 25365 | 200 | `https://web.archive.org/web/20190821031423id_/https://vsfan.net/wiki/Underwater_Diplomacy` |
| `Universal_Repair` | 5391 | 2019-09-23 07:33:15Z | 11033 | 46883 | 200 | `https://web.archive.org/web/20190923073315id_/https://vsfan.net/wiki/Universal_Repair` |
| `Unknown` | 6118 | 2019-08-21 01:24:34Z | 6396 | 16476 | 200 | `https://web.archive.org/web/20190821012434id_/https://vsfan.net/wiki/Unknown` |
| `Unknown_Snowfields` | 4366 | 2019-09-23 07:59:02Z | 10322 | 36080 | 200 | `https://web.archive.org/web/20190923075902id_/https://vsfan.net/wiki/Unknown_Snowfields` |
| `Veteran_Status` | 6054 | 2019-09-23 07:12:36Z | 7453 | 21738 | 200 | `https://web.archive.org/web/20190923071236id_/https://vsfan.net/wiki/Veteran_Status` |
| `Vincent` | 7372 | 2019-08-21 03:56:45Z | 13034 | 52237 | 200 | `https://web.archive.org/web/20190821035645id_/https://vsfan.net/wiki/Vincent` |
| `VisualShower` | 1687 | 2019-08-21 02:41:38Z | 13145 | 59306 | 200 | `https://web.archive.org/web/20190821024138id_/https://vsfan.net/wiki/VisualShower` |
| `Volcanic_Abyss` | 4988 | 2019-08-21 00:30:14Z | 10412 | 36373 | 200 | `https://web.archive.org/web/20190821003014id_/https://vsfan.net/wiki/Volcanic_Abyss` |
| `Werewolf` | 4463 | 2019-08-21 00:30:27Z | 11439 | 42860 | 200 | `https://web.archive.org/web/20190821003027id_/https://vsfan.net/wiki/Werewolf` |
| `Werewolves` | 4463 | 2019-09-23 07:15:43Z | 11519 | 43201 | 200 | `https://web.archive.org/web/20190923071543id_/https://vsfan.net/wiki/Werewolves` |
| `West_Forest_Outskirts` | 7450 | 2019-08-21 01:05:55Z | 10771 | 38442 | 200 | `https://web.archive.org/web/20190821010555id_/https://vsfan.net/wiki/West_Forest_Outskirts` |
| `Westfield` | 3103 | 2019-08-21 00:31:00Z | 10930 | 38565 | 200 | `https://web.archive.org/web/20190821003100id_/https://vsfan.net/wiki/Westfield` |
| `When_You_Open_Your_Eyes` | 5770 | 2019-08-21 02:40:32Z | 9500 | 34721 | 200 | `https://web.archive.org/web/20190821024032id_/https://vsfan.net/wiki/When_You_Open_Your_Eyes` |
| `White_Island` | 6399 | 2019-08-21 02:40:06Z | 15937 | 85715 | 200 | `https://web.archive.org/web/20190821024006id_/https://vsfan.net/wiki/White_Island` |
| `White_Script_Engine` | 1673 | 2019-09-23 07:05:49Z | 6504 | 16978 | 200 | `https://web.archive.org/web/20190923070549id_/https://vsfan.net/wiki/White_Script_Engine` |
| `Who_am_I?` | 5346 | 2019-08-21 00:35:02Z | 10714 | 41186 | 200 | `https://web.archive.org/web/20190821003502id_/https://vsfan.net/wiki/Who_am_I%3F` |
| `Windblade` | 7369 | 2019-08-26 07:02:35Z | 14977 | 79203 | 200 | `https://web.archive.org/web/20190826070235id_/https://vsfan.net/wiki/Windblade` |
| `Witnesses` | 6258 | 2019-08-26 06:57:16Z | 9524 | 34713 | 200 | `https://web.archive.org/web/20190826065716id_/https://vsfan.net/wiki/Witnesses` |
| `Wolf's_Mouth` | 3390 | 2019-08-26 08:23:58Z | 10620 | 37588 | 200 | `https://web.archive.org/web/20190826082358id_/https://vsfan.net/wiki/Wolf%27s_Mouth` |
| `Wolf_Child` | 7464 | 2019-08-21 00:46:05Z | 7089 | 18029 | 200 | `https://web.archive.org/web/20190821004605id_/https://vsfan.net/wiki/Wolf_Child` |
| `Won't_Back_Down` | 5935 | 2019-08-21 00:41:40Z | 11171 | 49247 | 200 | `https://web.archive.org/web/20190821004140id_/https://vsfan.net/wiki/Won%27t_Back_Down` |
| `World's_Most_Dangerous_Package` | 6326 | 2019-08-21 01:22:00Z | 11051 | 46140 | 200 | `https://web.archive.org/web/20190821012200id_/https://vsfan.net/wiki/World%27s_Most_Dangerous_Package` |
| `Yatağınızı_ısıtacak_Seksi_Rus_Kızları` | 6316 | 2019-09-23 08:08:47Z | 7322 | 19972 | 200 | `https://web.archive.org/web/20190923080847id_/https://vsfan.net/wiki/Yata%C4%9F%C4%B1n%C4%B1z%C4%B1_%C4%B1s%C4%B1tacak_Seksi_Rus_K%C4%B1zlar%C4%B1` |
| `You_Again` | 6343 | 2019-10-14 11:14:07Z | 11139 | 50934 | 200 | `https://web.archive.org/web/20191014111407id_/https://vsfan.net/wiki/You_Again` |
| `Your_Future` | 5384 | 2019-08-21 00:54:02Z | 7482 | 26541 | 200 | `https://web.archive.org/web/20190821005402id_/https://vsfan.net/wiki/Your_Future` |
| `Your_Scarf` | 5911 | 2019-08-21 00:30:52Z | 10940 | 47219 | 200 | `https://web.archive.org/web/20190821003052id_/https://vsfan.net/wiki/Your_Scarf` |
| `Yuri` | 7426 | 2019-08-21 00:31:56Z | 15803 | 83202 | 200 | `https://web.archive.org/web/20190821003156id_/https://vsfan.net/wiki/Yuri` |
| `Zaman_Kaybetmeden_Işlem_Yapma_Kolaylığı` | 6339 | 2019-09-23 06:59:21Z | 7317 | 19763 | 200 | `https://web.archive.org/web/20190923065921id_/https://vsfan.net/wiki/Zaman_Kaybetmeden_I%C5%9Flem_Yapma_Kolayl%C4%B1%C4%9F%C4%B1` |
**Ledger totals: 299 pages, 299 HTTP 200, 0 failures.** Capture span
**2017-08-25 → 2020-08-08**; the game-content burst is **2019-08-21 → 2019-09-23**.

## 1.5 Hero infoboxes — 57 hero pages

The hero infobox is: epithet + name, "Blustone character", **Rarity** (literal
`★` glyphs), **Role** + icon, **Type** + icon, **Gender**, **Race**.

**Icon vocabulary, read from the `alt` attributes (verified, not assumed):**

| icon `alt` | meaning | pages carrying it |
|---|---|---|
| `1star-symbol.png` … `5star-symbol.png` | rarity, 1–5 | Rarity is literal text `★`; the star *images* appear in the skill table's rank column |
| `AttackIcon.png` | **Offense** | 19 |
| `DefenseIcon.png` | **Defense** | 15 |
| `BomberIcon.png` | **Bomber** | 12 |
| `SupportIcon.png` | **Support** | 11 |
| `FireIcon.png` | Fire | 19 |
| `ElecIcon.png` | **Electric** (= the catalogue's `Lightning`) | 19 |
| `IceIcon.png` | Ice | 19 |

`catalog_id` is resolved by exact normalised name match against
`analysis/catalogue/data/card-catalogue.tsv`. **57/57 hero pages matched a
catalogue row.** `Karl` and `Karl_Steiner` are duplicate pages for `012`;
`Teddy_Bomber` and `TeddyBomber` are duplicates for `025` — so **57 pages = 55
distinct characters.**

| wiki page | catalog | ★ | Role | Element | Gender | Race | oldid |
|---|---|---|---|---|---|---|---|
| Acerola | 030 | ★★ | Support | Electric | Female | *(blank)* | 7387 |
| Akasha | 008 | ★★★ | Support | Electric | Female | Werewolf | 7376 |
| Apollon | 055 | ★★★ | Bomber | Fire | Male | *(blank)* | 7403 |
| Athena | 027 | ★★★ | Defense | Fire | Female | *(blank)* | 2790 |
| Balian | 019 | ★ | Offense | Electric | Male | Werewolf | 2224 |
| Bear | 036 | ★★★ | Defense | Electric | Female | *(blank)* | 7436 |
| Beckhen | 051 | ★★★ | Offense | Ice | *(blank)* | *(blank)* | 7422 |
| Bibi | 040 | ★★★ | Offense | Electric | Female | *(blank)* | 7431 |
| Bright | 049 | ★★★ | Support | Fire | Male | *(blank)* | 7441 |
| Bruce Bang | 016 | ★ | Support | Ice | Male | Coffee Rabbit | 7321 |
| Calibur | 053 | ★★★ | Defense | Fire | Female | *(blank)* | 7478 |
| Captain | 009 | ★ | Defense | Electric | *(blank)* | *(blank)* | 2323 |
| Crocus | 058 | ★★★ | Support | Electric | Female | *(blank)* | 7408 |
| Denali | 013 | ★★ | Support | Fire | Female | Coffee Rabbit | 7315 |
| Diana | 031 | ★★★ | Bomber | Electric | Female | *(blank)* | 7462 |
| Dino | 054 | ★★★ | Bomber | Ice | Male | *(blank)* | 7396 |
| Dumble | 048 | ★★★ | Defense | Ice | Male | *(blank)* | 7425 |
| Edward | 041 | ★★★ | Defense | Electric | Male | *(blank)* | 7429 |
| Gerard | 005 | ★★ | Defense | Ice | Male | Sapien | 2403 |
| Gullveig | 039 | ★★★ | Bomber | Electric | *(blank)* | *(blank)* | 7432 |
| Harley | 046 | ★★★★ | Defense | Ice | Male | *(blank)* | 7394 |
| Hecate | 011 | ★ | Defense | Fire | Female | Sapien | 2434 |
| Heidi | 044 | ★★★ | Offense | Fire | Female | *(blank)* | 7477 |
| Hermes | 023 | ★★★ | Offense | Fire | Male | Coffee Rabbit | 7349 |
| Joy | 035 | ★★★ | Support | Fire | Female | *(blank)* | 7456 |
| Juno | 062 | ★★★ | Defense | Fire | Male | *(blank)* | 7484 |
| Kain | 029 | ★★★ | Defense | Electric | Male | *(blank)* | 7460 |
| Karl Steiner | 012 | ★★★ | Offense | Electric | Male | Werewolf | 7370 |
| Lantern | 001 | ★★★ | Bomber | Fire | Male | *(blank)* | 7415 |
| Lapis | 017 | ★ | Offense | Ice | Female | Werewolf | 7350 |
| Levi | 015 | ★★ | Bomber | Ice | Female | Robot / Werewolf | 2536 |
| Lily & Lyla | 047 | ★★★★ | Offense | Fire | Female | Coffee Rabbit | 7375 |
| Locke | 014 | ★ | Bomber | Ice | Male | Sapien | 2735 |
| Metis | 007 | ★ | Bomber | Fire | Female | Polar Bear | 2560 |
| Mowgli | 002 | ★★ | Offense | Electric | Male | *(blank)* | 7346 |
| Natalia | 037 | ★★★ | Offense | Ice | Female | *(blank)* | 7393 |
| Nene | 003 | ★★★ | Defense | Ice | Female | Polar Bear | 2920 |
| Octavia | 028 | ★★★ | Offense | Ice | Female | *(blank)* | 2944 |
| Pansy | 057 | ★★★ | Support | Electric | Male | *(blank)* | 7458 |
| Papillon | 043 | ★★★ | Defense | Ice | Female | *(blank)* | 7427 |
| Patrone | 033 | ★★★ | Bomber | Ice | Female | *(blank)* | 7439 |
| Rebecca | 021 | ★★ | Offense | Fire | *(blank)* | *(blank)* | 7447 |
| Riko | 024 | ★★ | Defense | Electric | *(blank)* | *(blank)* | 2615 |
| Robin | 018 | ★★ | Defense | Ice | Male | Sapien | 2638 |
| Santa Clauster | 042 | ★★★ | Offense | Fire | Male | *(blank)* | 7433 |
| Scar | 032 | ★★ | Offense | Ice | Male | *(blank)* | 7455 |
| Sienna | 020 | ★ | Bomber | Electric | Female | Sapien | 7414 |
| Sunny | 022 | ★★ | Support | Ice | Female | Sapien | 7322 |
| Sylvester | 006 | ★ | Offense | Fire | Male | Sapien | 2722 |
| Teddy Bomber | 025 | ★★ | Bomber | Fire | Female | Sapien | 2971 |
| Therapy | 050 | ★★★ | Support | Ice | Female | *(blank)* | 7423 |
| Tyltyl | 004 | ★ | Support | Fire | *(blank)* | *(blank)* | 7377 |
| Vincent | 010 | ★★★★ | Offense | Electric | *(blank)* | *(blank)* | 7372 |
| Windblade | 052 | ★★★★ | Offense | Electric | Male | *(blank)* | 7369 |
| Yuri | 045 | ★★★ | Offense | Ice | Female | *(blank)* | 7426 |

Rarity distribution: ★ 10, ★★ 12, ★★★ 31, ★★★★ 4.
Role: Offense 19, Defense 15, Bomber 12, Support 11.
Element: Electric 19, Fire 19, Ice 19 (**exactly 19/19/19 — a deliberate
balance the wiki reproduces exactly**).

## 1.6 Hero `Character Attributes` stat tables — 11 pages

**This is the most important content in the corpus.** Eleven hero pages carry a
`Stats` section. Structure: an optional `<caption>`, then
`Character Attributes`, `Stat Details: Attack`, `Stat Details: Defense`.

**Complete tables (3 pages) — captioned `Transcendence Level: 3`:**

| | Captain (`009`) | Hermes (`023`) | Riko (`024`) |
|---|---|---|---|
| caption | `Transcendence Level: 3` | `Transcendence Level: 3` | `Transcendence Level: 3` |
| **Life** | **2069** | **2275** | **2069** |
| **Attack** | **734** | **1218** | **868** |
| **Defense** | **1142** | **848** | **1047** |
| Attack Speed | 7 | 8 | 7 |
| Critical Damage Chance | 14% | 33% | 14 |
| Critical Damage | 180% | 200% | 185 |
| Armor Penetration | 1% | 0% | 0 |
| Block Chance | 33% | 14% | 33 |
| Block Resistance | 52% | 40% | 50 |
| Strengthen Elemental Attributes | 0% | 2% | 0 |
| Elemental Attack Resistance | 0% | 2% | 0 |
| Life Regeneration | 40 | 44 | 40 |

Raw HTML for Captain, verbatim (proves the values are real text, not artefacts):

```
<table class="wikitable" style="margin-right: 70px;">
<caption>Transcendence Level: 3 </caption>
<tbody><tr> <th colspan="4">Character Attributes </th></tr>
<tr> <td>Life</td> <td style="text-align:right;">2069</td> <td>Attack</td> <td style="text-align:right;">734 </td></tr>
<tr> <td>Defense</td> <td style="text-align:right;">1142</td> <td>Attack Speed</td> <td style="text-align:right;">7 </td></tr>
<tr> <th colspan="4">Stat Details: Attack </th></tr>
<tr> <td colspan="3">Critical Damage Chance </td> <td style="text-align:right;">14% </td></tr>
…
```

**Partial tables (8 pages) — `Life`/`Attack`/`Defense` rows are ABSENT from the
wikitext, not blank cells.** Raw Bear:

```
<h2><span class="mw-headline" id="Stats">…</h2>
<table class="wikitable" style="float:left; margin-right: 70px;"> <tbody>
<tr> <th colspan="4">Character Attributes </th></tr>
<tr> <td colspan="3">Attack Speed </td> <td style="text-align:right;">7 </td></tr>
```

i.e. after the `Character Attributes` header the table jumps straight to
`Attack Speed` with a single `colspan="3"` row. **There is no Life/Attack/
Defense row anywhere in the markup** — the editors transcribed only Attack
Speed and the nine sub-stats. Full readings:

| page | catalog | Attack Speed | Crit | Crit dmg | Pen | Block | Block dmg red. | Elem enhance | Elem resist | Life regen |
|---|---|---|---|---|---|---|---|---|---|---|
| Bear | 036 | 7 | 14 | 180 | 0 | 33 | 50 (Block Resistance) | 5 | 5 | 32 |
| Diana | 031 | 7 | 14 | 180 | 0 | 14 | 40 (Damage Reduction Block) | 5 | 5 | 38 |
| Joy | 035 | 7 | 14 | 180 | 0 | 14 | 42 (Damage Reduction Block) | 5 | 5 | 43 |
| Kain | 029 | 7 | 14 | 185 | 0 | 36 | 55 (Damage Reduction Block) | 5 | 5 | 45 |
| Lantern | 001 | 7 | 14 | 180 | 0 | 14 | 42 (Block Resistance) | 0 | 0 | 38 |
| Pansy | 057 | 7 | 14 | 185 | 0 | 14 | 40 (Damage Reduction Block) | 5 | 5 | 44 |
| Patrone | 033 | 7 | 14 | 185 | 0 | 14 | 40 (Block Resistance) | 5 | 5 | 38 |
| Scar | 032 | 8 | 33 | 200 | 0 | 14 | 40 (Damage Reduction Block) | 0 | 0 | 45 |

### 1.6.1 [2026-10-06 re-audit] every §1.6 cell re-verified against primary bytes — **no cell was wrong**

An earlier note,
[`transcendence-multiplier-2026-10-05.md`](transcendence-multiplier-2026-10-05.md)
§1.2, reported that **this** section transcribes Patrone `033`'s elemental
values as `0/0` and that re-running the §1.7 tally yields **95 equal / 13
different**. ~~"vsfan-wiki §1.6 records `0` / `0`"~~ — **RETRACTED
2026-10-06.** This section has always recorded **`5/5`** for Patrone, and the
archived page agrees with it. The `95/13` figure came from the adjudication's
own reading of this file, not from this file's contents.

**Primary source consulted, re-fetched 2026-10-06.** All eleven
`Character Attributes` tables were re-fetched from the Wayback Machine in `id_`
(raw, un-rewritten) form at the exact §1.4 ledger captures. Two positive
controls ran first: `https://web.archive.org/` → **HTTP 200 / 145,187 bytes**,
and an exact-match CDX query on `vsfan.net/wiki/List_of_Hunters` → **HTTP 200 /
3 rows**. Every fetch then returned **HTTP 200**, every **byte count equalled
the §1.4 ledger**, and every page's own footer `oldid=` equalled its ledger
`oldid`.

| page | catalogue | archive URL (`id_`) | capture (UTC) | oldid | bytes | sha256 (full) |
|---|---|---|---|---:|---:|---|
| Captain | `009` | `https://web.archive.org/web/20190821025153id_/https://vsfan.net/wiki/Captain` | 2019-08-21 02:51:53Z | 2323 | 97621 | `6bd38c4beeb0098782c295d5202b1bb828f4b3209cb7573a9655a74219624eb0` |
| Hermes | `023` | `https://web.archive.org/web/20190826081115id_/https://vsfan.net/wiki/Hermes` | 2019-08-26 08:11:15Z | 7349 | 113204 | `2f0cc53c0d127154cd65fb4307328c2fe764e1c80ac5051fddb5e90c6167a6ef` |
| Riko | `024` | `https://web.archive.org/web/20190821030411id_/https://vsfan.net/wiki/Riko` | 2019-08-21 03:04:11Z | 2615 | 87653 | `547ee5bb7e9fa931928c2a3bc39004295abf073a4b34d1e0f8936d26873d1b75` |
| Bear | `036` | `https://web.archive.org/web/20190826070034id_/https://vsfan.net/wiki/Bear` | 2019-08-26 07:00:34Z | 7436 | 80961 | `ef42081bc5f01853aa4136f2427638c69475ea6cd2cfd5f72a0521b1dee52db5` |
| Diana | `031` | `https://web.archive.org/web/20190826081956id_/https://vsfan.net/wiki/Diana` | 2019-08-26 08:19:56Z | 7462 | 90744 | `df05a520124cb5c98c0d40f5b5d382f93e00f68adf07d8be74c6964e660cc41e` |
| Joy | `035` | `https://web.archive.org/web/20190821024200id_/https://vsfan.net/wiki/Joy` | 2019-08-21 02:42:00Z | 7456 | 82549 | `5f47540bbc7d6ceb7a35fea25572d47ef8562d1c768f3a601445f727177fb47b` |
| Kain | `029` | `https://web.archive.org/web/20190826065754id_/https://vsfan.net/wiki/Kain` | 2019-08-26 06:57:54Z | 7460 | 118382 | `2cf3003f785d5f0172f0c5a00f18b466170fdef44ff35f5ac1d41d4724cf7a30` |
| Lantern | `001` | `https://web.archive.org/web/20190821025813id_/https://vsfan.net/wiki/Lantern` | 2019-08-21 02:58:13Z | 7415 | 173580 | `4bd2169a271e9624170b95c4ef6d25e582b26f919b820c718f09f130cd979ffc` |
| Pansy | `057` | `https://web.archive.org/web/20190821024953id_/https://vsfan.net/wiki/Pansy` | 2019-08-21 02:49:53Z | 7458 | 77514 | `c016f4210599c4be1447bd93c9f86ae6ba9aacd9b7a781371f83d9048c32eeee` |
| **Patrone** | `033` | `https://web.archive.org/web/20190826075547id_/https://vsfan.net/wiki/Patrone` | **2019-08-26 07:55:47Z** | **7439** | **122245** | `b78fab30a81f35bc3e69b10dc1eb652785fcf234c569a247ee0b0953a4620460` |
| Scar | `032` | `https://web.archive.org/web/20190821035719id_/https://vsfan.net/wiki/Scar` | 2019-08-21 03:57:19Z | 7455 | 123062 | `607b401dfa7ce3cea3f1e0ebc17d153c7bd32868efe720aa3b8a7b6b9502d70f` |

**Result of the re-audit — 0 data errors.**

| claim under audit | verdict |
|---|---|
| Patrone `033` `Strengthen Elemental Attributes` = **`5`** | **CONFIRMED** — wikitext cell is `5`, §1.6 records `5`, `[JP19]` reads `5` |
| Patrone `033` `Elemental Attack Resistance` = **`5`** | **CONFIRMED** — wikitext cell is `5`, §1.6 records `5`, `[JP19]` reads `5` |
| Patrone `033` `Life Regeneration` = **`38`** | **CONFIRMED** (the `…5 / 5 / 38` sequence is verbatim) |
| all 120 §1.6 cells (11 tables × the 9 sub-stats, plus 12 Life/Attack/Defense cells, plus 24 confirmed-absent Life/Attack/Defense cells) | **all exact** |
| the three complete tables carry `<caption>Transcendence Level: 3</caption>` and the eight partial tables carry **no** caption | **CONFIRMED** — each page has exactly **one** `Character Attributes` wikitable, so there is no second candidate table |
| `Life`/`Attack`/`Defense` are **absent** from the eight partial tables | **CONFIRMED** — no such row anywhere in the markup |
| the `Block Resistance` vs `Damage Reduction Block` label split | **CONFIRMED per page** — this transcription is exact, not normalised |
| "percent signs are inconsistent — Captain/Hermes write `14%`, the other nine write bare `14`" | **CONFIRMED** — `%` present on every sub-stat cell of Captain and Hermes, absent on Riko and all eight partial tables |
| §1.7's **108 comparisons / 97 equal / 11 different** | **CONFIRMED by independent recount from the re-fetched bytes** (below), *not* inherited |

**§1.7 recomputed 2026-10-06 from the primary wikitext, not from the tables
above: `108 comparisons · 97 equal · 11 different`.** Composition: **9
Life/Attack/Defense** (Captain `009` hp/atk/def, Hermes `023` hp/atk/def, Riko
`024` hp/atk/def) plus **2 `hp_regen` off-by-ones** (Captain `40` vs `41`, Riko
`40` vs `41`). A control leg over the nine sub-stats alone returns **99
comparisons / 97 equal / 2 different**, and the two differences are exactly
those two `hp_regen` cells — which is what licenses §1.7's sentence that
*"All Attack Speed, Critical Damage Chance, Critical Damage, Armor Penetration,
Block Chance, Block/Damage-Reduction, Element enhance/resist values match the
JP database exactly"* (that sentence lists eight fields and deliberately omits
`Life Regeneration`).

**One cosmetic defect found, in prose only, no data affected.** The two HTML
blocks quoted above are labelled *verbatim*, but their **interior newlines were
collapsed to spaces** when they were transcribed: the bytes read
`<caption>Transcendence Level: 3\n</caption>` and
`<td style="text-align:right;">734\n</td>`, where the blocks above show a
single space. ~~"Raw HTML for Captain, verbatim"~~ → **values and markup are
verbatim; internal whitespace is normalised.** The `…` elision and the trailing
`<td style="text-align:right;">7 </td>` in the Bear block are otherwise
accurate.

**Standing instruction.** Do **not** "repair" the Patrone row to `0/0` on the
strength of `transcendence-multiplier-2026-10-05.md` §1.2 — that instruction is
withdrawn. §1.6's Patrone row is correct as written. Nothing here moves a
coverage count: heroes **1/113**, accessories **1/100**, monsters **0/22**.

The 9 sub-stat labels are the same as the Japanese database's columns, mapped
`Critical Damage Chance`→`crit`, `Critical Damage`→`crit_damage`,
`Armor Penetration`→`penetration`, `Block Chance`→`block`,
`Block Resistance` **or** `Damage Reduction Block`→`block_damage_reduction`,
`Strengthen Elemental Attributes`→`element_enhance`,
`Elemental Attack Resistance`→`element_resistance`,
`Life Regeneration`→`hp_regen`.

**Percent signs are inconsistent** — Captain/Hermes write `14%`, the other nine
write bare `14`. §2 records this as a formatting inconsistency, not a unit
difference, because the values coincide exactly with the JP database's
unitless integers.

## 1.7 Cross-source validation against the 2019 Japanese database

Comparing all 11 wiki stat tables against
[`archived-hunter-database-2019.tsv`](archived-hunter-database-2019.tsv) by
catalogue ID:

**108 field comparisons · 97 equal · 11 different.**

| hero | field | wiki | JP 2019 | ratio |
|---|---|---|---|---|
| Captain `009` | hp | 2069 | 1624 | 1.274 |
| Captain `009` | atk | 734 | 628 | **1.169** |
| Captain `009` | def | 1142 | 893 | 1.279 |
| Captain `009` | hp_regen | 40 | 41 | — |
| Hermes `023` | hp | 2275 | 1750 | **1.300** |
| Hermes `023` | atk | 1218 | 937 | **1.300** |
| Hermes `023` | def | 848 | 653 | **1.299** |
| Riko `024` | hp | 2069 | 1624 | 1.274 |
| Riko `024` | atk | 868 | 682 | 1.273 |
| Riko `024` | def | 1047 | 821 | 1.275 |
| Riko `024` | hp_regen | 40 | 41 | — |

All **Attack Speed, Critical Damage Chance, Critical Damage, Armor
Penetration, Block Chance, Block/Damage-Reduction, Element enhance/resist
values match the JP database exactly**, for all 11 heroes. That is what
establishes these as the same data — and it makes the 11 differences
meaningful rather than random. Interpretation is deferred to §2.1–§2.4.

Also compared, hero **identity metadata** (star / role / element) for all 57
heroes against the JP database: **55 of 57 agree on all three fields.** The
two that do not are `Pansy` (element) and `Robin` (rarity) — both analysed in
§2.5 and §2.7.

## 1.8 Equipment tables — 216 rows, only two values ever filled in

35 hero pages carry a `Type / Description / Effect` table with Weapon, Armor,
Accessory rows. **216 rows total: 106 have `Lv.50` and an empty value; 2 have a
value; the remainder are the row pairs' description cells.**

The blank rows are literally `Increases attack Lv.50` followed by two
non-breaking spaces — the editors left the magnitude empty:

```
Increases attack <b><span …>Lv.</span><span …><i>50</i></span></b>&#160;&#160;</p>
```

The **only two filled values in the entire corpus** — raw HTML confirmed:

```
Beckhen | Weapon   | Chicken Feet | Increases attack Lv. 50  134
Yuri    | Weapon   | Skate Shoes  | Increases attack Lv. 50  134
```

## 1.9 Skill tables — 570 rows, 145 carry Lv.50 numerals

Each hero has a 5-slot skill table with columns
`Hunter Rank / (icon) / Description / Effect / Activation / Target`. The rank
column pairs a star-symbol image with the rank name **Experienced Hunter**,
**Proficient Hunter**, **Master Hunter** (this triple is the same naming the
GameAppCH screenshot in `coverage.md` uses). **145 of 570 rows carry a numeral**,
always introduced by `Lv. 50`:

Distinct numeral tokens and their frequencies: `15%` 29, `10%` 26, `30%` 24,
`35%` 10, `20%` 9, `15.00%` 7, `2.50 Sec.` 6, `60%` 3, `3 Sec.` 3, `5%` 1,
`40%` 2, `50%` 2, `100%` 2, `2 Sec.` 1, `4 Sec.` 1, `6%` 2, `24.99%` 2,
`12.5%` 1, `0.6%` 1, `50.00%` 1, `7.54%` 1, `80%` 1, `93.06%` 1,
`20.00%` 1, `24.99%`, `1 Serving`-adjacent noise excluded.

Worked example, Akasha's table verbatim:

| Hunter Rank | Skill | Effect | Activation | Target |
|---|---|---|---|---|
| Experienced Hunter | Reflection Prayer | Recovery over time | Active | Team |
| Experienced Hunter | Attack Speed Increase | Temporarily increases attack speed `Lv. 50` **30%** | Follows active | Field teammate |
| Experienced Hunter | Public Health | Increased maximum health `Lv. 50` **10%** | Passive | Team |
| Proficient Hunter | Immunity | Temporary immunity to all attacks. `Lv. 50` **3.00 Sec.** | Follows active | Forward |
| Master Hunter | An Enchantress' Blessing | Increased defense `Lv. 50` **15%** | Passive | Team |

Two anomalies are preserved rather than tidied: Nene's
`Continuous Physical Recovery … Lv. 50 163.92 hp` (a raw HP number in a skill
effect) and the stray `60px` tokens on the `List_of_Hunters` rows for Pansy and
Juno, which are broken image-width markup rendered as text.

## 1.10 `List_of_Blustone_Items` — full numeric tables

Capture `20190821024134`, oldid `5115`. Twelve tables. Nine carry numerals.

**Metron / currency values:**

| Name | Areas Available | Usage | Value |
|---|---|---|---|
| Metron Fragment | All areas | Used in levelling all skills | **10** |
| Metron Crystal | Cryogenic Abyss, Electric Abyss and Volcanic Abyss | Used in the upcoming transcendence feature | **1000** |

**Hunter Materials (4 tables × 3 tiers, all values identical per tier):**

| Material | Tier | Areas (excerpt) | Used by | Value |
|---|---|---|---|---|
| Rusty / Sharp / Unusual Metal Piece | 1 / 2 / 3 | Electric Abyss; Areas 1-86 … 91-116 | Offense skills 5-30 / 20-50 / 30-50 | **10 / 50 / 250** |
| Broken / Unscathed / Invincible Shell | 1 / 2 / 3 | Cryogenic Abyss; Areas 2-87 … 92-117 | Defense skills 5-30 / 20-50 / 30-50 | **10 / 50 / 250** |
| Cold / Burning / Scorching Flamestone | 1 / 2 / 3 | Areas 3-88 … 93-118 | Bomber skills 5-30 / 20-50 / 30-50 | **10 / 50 / 250** |
| Withered / Fresh / Fruit-Bearing Herb | 1 / 2 / 3 | Areas 4-89 … 94-169 | Support skills 6-30 / 21-50 / 31-50 | **10 / 50 / 250** |

**Hunter Traces — 28 rows, the single most useful numeric table here.** Header:
`Image / Name / Description / Rarity / Areas Available / Value`.

| Name | Rarity | Areas Available | Value |
|---|---|---|---|
| Acerola's Trace | ★★ | Evaluation Request, Rotation Area | 100 |
| Akasha's Trace | ★★★ | Evaluation Request, Fight Club Shop | 300 |
| Athena's Trace | ★★★ | Evaluation Request, Abyss Area | 300 |
| Balian's Trace | ★ | Silent Forest, Evaluation Request, Hunter Shop | 20 |
| Bruce Bang's Trace | ★ | North Highlands, Evaluation Request, Hunter Shop | 20 |
| Denali's Trace | ★★ | Crimson Chasm and Flamestone Basin, Evaluation Request, Fight Club Shop, Rotation Area | 100 |
| Gerard's Trace | ★★ | Non-melting Forest, Crescent Hill, Evaluation Request, Fight Club Shop, Rotation Area | 100 |
| Hecate's Trace | ★ | Wolf's Mouth, Evaluation Request, Fight Club Shop | 20 |
| Hermes's Trace | ★★★ | Evaluation Request, Abyss Area | 300 |
| Kain's Trace | ★★★ | Evaluation Request, Limited Abyss Area Event | 300 |
| Karl Steiner's Trace | ★★★ | Evaluation Request, Abyss Area | 300 |
| Lantern's Trace | ★★★ | Evaluation Request, Fight Club Shop, Abyss Area | 300 |
| Lapis's Trace | ★ | Midgard Snowfields, Evaluation Request, Hunter Shop | 20 |
| Levi's Trace | ★★ | Burned Forest, Blue Wing Valley, Evaluation Request, Hunter Shop, Midgard Snowfields | 100 |
| **Locke's Trace** | **★** | Giant's Shelter, Evaluation Request, Hunter Shop | **100** ⚠ |
| Metis's Trace | ★ | Midgard Ice Zone, Evaluation Request, Hunter Shop | 20 |
| Mowgli's Trace | ★★ | Evaluation Request, Fight Club Shop, Rotation Area | 100 |
| My Trace (Captain) | ★ | Hunter Shop | 20 |
| Nene's Trace | ★★★ | Evaluation Request, Fight Club Shop, Abyss Area | 300 |
| Octavia's Trace | ★★★ | Evaluation Request, Abyss Area Event | 300 |
| Rebecca's Trace | ★★ | Evaluation Request, Fight Club Shop, Rotation Area | 100 |
| Riko's Trace | ★★ | Evaluation Request, Fight Club Shop, Rotation Area | 100 |
| **Robin's Trace** | **★** | Emerald Canyon, Evaluation Request, Hunter Shop | 20 |
| Sienna's Trace | ★ | Mt. Black Rock, Evaluation Request, Hunter Shop | 20 |
| Sylvester's Trace | ★ | Blood Red Canyon, Evaluation Request, Hunter Shop | 20 |
| Teddy Bomber's Trace | ★★ | Evaluation Request, Hunter Shop, Rotation Area | 100 |
| Tyltyl's Trace | ★ | Evaluation Request, Hunter Shop | 20 |

Non-trace item tables carry **no numbers**: Challenge Invitation, Fight Chip,
Manda, Ornithopter Fuel, Rupee, Veteran Points, Stimpack, and the four Request
types (2~3★, 3★, Elite, Evaluation) are name + prose description + acquisition
+ usage only.

## 1.11 `Fight_Club_Shop` — price table

Capture `20190821024117`, oldid `5984`. "You can buy items with Fight Chip.
Fight Club Shop is replenished every 12h."

| Name | Number | Cost |
|---|---|---|
| Lantern's Trace | 2 | 150 |
| Akasha's Trace | 2 | 150 |
| Metron_Crystal | 1 | 1000 |
| 2-3 Star Request | 1 | 1500 |
| Elite Request | 1 | 500 |
| 2 star hunter's trace | 2 | 75 |
| Advanced skills advancement items | 3 | 25 |
| Expert skills advancement items. | 3 | 75 |

## 1.12 `Veteran_Status` — the 12-rank ladder

Capture `20190923071236`, oldid `6054`.

| | Beginner 1 | Beginner 2 | Beginner 3 | Professional 1 | Professional 2 | Professional 3 | Expert 1 | Expert 2 | Expert 3 | Guru 1 | Guru 2 | Guru 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Points | 20 | 40 | 80 | 160 | 320 | 640 | 1280 | 2560 | 5120 | | | |
| Fuel Recharge | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 13 | 15 | 17 | 19 |
| Invitation Recharge | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 13 | 15 | 17 | 19 |
| Ruppee Recharge | 7 | 6 | 8 | 9 | 10 | 11 | 12 | 13 | 15 | 17 | 19 | 21 |
| Special Support Fuel | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 5 | 10 | 10 | 15 | 15 |
| Special | Able to renew item in the store | Able to receive misssed supplies *(sic)* | Auto-combat 10 consecutive times | Able to renew the Fight Club Shop | | Auto-combat 50 consecutive times | | | | | | Get Hidden Hunter |

Prose, verbatim: `Become Guru3 need 40 960 Veteran Points` ·
`If you are a F2P player you can gain at last 40 points per days with Daily
Goals/Rewards =1 024 Days` · `Your Veteran level change the circle around your
avatar.`

## 1.13 `Hunters'_Drop_Rate` — gacha rates

Capture `20190821010227`, oldid `6231`. Verbatim:

```
Drop Rate in Elite Requests
3★ - 4.76%   2★ - 19.05%   1★ - 76.19%

3★ ranks are divided into [Pre-existing] and [New], and hunters a divided based
on their release date. Half of 3★ hunters that have been released recently are
categorized into [New] and the other half is categorized into [Pre-existing].
(In case there is an odd number of 3★ hunters in total, there will be one more
hunter in [Pre-existing] than [New].)

The percentage of [New] and [Pre-existing] are separated as follows.
3★ [New] - 40%   3★ [Pre-existing] - 60%
The number of [New] and [Pre-existing] is the same and it will be kept the same
or with a difference of 1, so the difference between acquisition is about
1.4~1.6 times.

Drop Rate in 2★ Requests
3★ - 14.23%   2★ - 85.77%

Similar to Elite Requests, 3★ hunters are divided into [New] and [Pre-existing]
and is 40% and 60% respectively.

Drop Rate in 3★ Requests
Only 3★ hunters appear in 3★ Requests. …

<Event Hunters & Hidden Hunter>
There are certain hunters that do not appear in all players' Elite Requests and
only appear for players that have that certain hunter. There are currently one
2★ hunter and one 3★ hunter that applies to this condition. … However, the 3★
hidden hunter is always categorized into [New], regardless of his release date.
```

## 1.14 `Guide_to_Blustone` — training, transcendence, abyss, arena

Capture `20190923072038`, oldid `7465`. **This page independently reproduces the
share_en transcendence matrix from §2.2.3 of
[`share-en-census-2026-10-05.md`](share-en-census-2026-10-05.md) — a second,
independent transcription of the same official costs.**

**Skill-level cost table (verbatim):**

| Level | Cost |
|---|---|
| 1 - 4 | 100 Rupees, 1 Metron Fragment |
| 5 - 9 | 200 Rupees, 1 Metron Fragment, 1 Bronze tier materials |
| 10 - 14 | 300 Rupees, 2 Metron Fragments, 2 Bronze tier materials |
| 15 - 19 | 400 Rupees, 2 Metron Fragments, 3 Bronze tier materials |
| 20 - 25 | 500 Rupees, 3 Metron Fragments, 4 Bronze tier materials, 1 Silver tier Material |
| 26 - 29 | 600 Rupees, 3 Metron Fragments, 5 Bronze tier materials, 2 Silver tier Materials |
| 30 - 34 | 700 Rupees, 4 Metron Fragments, 3 Silver tier materials, 1 Gold tier Materials |
| 35 - 39 | 800 Rupees, 4 Metron Fragments, 4 Silver tier materials, 2 Gold tier Materials |
| 40 - 44 | 900 Rupees, 5 Metron Fragments, 5 Silver tier materials, 3 Gold tier Materials |
| 45 - 49 | 1000 Rupees, 5 Metron Fragments, 6 Silver tier materials, 4 Gold tier Materials |

**The last row is `45 - 49`, which implies a skill cap of 50** — matching the
project's 10-per-grade × 5-grade = 50 fixture convention.

**Transcendence matrix (verbatim, matches `share_en/215324` exactly):**

| base | step | Metron Crystals | Rupees | Metron Fragments | duplicate |
|---|---|---|---|---|---|
| Natural 1-star | T1 / T2 / T3 | 5 / 15 / 45 | 5,000 / 15,000 / 45,000 | 50 / 150 / 450 | 1 / 2 / 3 |
| Natural 2-stars | T1 / T2 / T3 | 7 / 25 / 60 | 7,000 / 25,000 / 60,000 | 70 / 250 / 600 | 1 / 2 / 3 |
| Natural 3-stars | T1 / T2 / T3 | 9 / 30 / 80 | 9,000 / 30,000 / 80,000 | 90 / 300 / 800 | 1 / 2 / 3 |

`For the second and third transcendence, your base hunter needs to be at least
4-stars and 5-stars respectively. The duplicate hunters however only need to be
3-stars.`

**Star-up fodder counts (matches `share_en` 138442/24901):** 1★→2★ one 1★;
2★→3★ two 2★; 3★→4★ three 3★; 4★→5★ four 4★.

**Abyss / Ruins economics (verbatim numerals):** five Abysses (Electric =
Offense materials, Cryogenic = Defense, Volcanic = Bomber, Golden = gold +
Healer materials, Metron = fragments only); one attempt per day; reset costs
`30,000 Rupees or 30 Manda`, more resets at higher veteran level with rising
cost. Stage rewards: `stage 5 … 3 metron crystals per run`, `stages 3 and 4
give you 2`, `stages 1 and 2 only give you 1`. Ruins: `there are 4 waves`,
`each of these ruins costs 20 fuel`, and only natural 3-stars
`Hermes, Karl, Nene and Athena` yield traces.

**Cruise / dispatch mechanics (verbatim):** `the best areas to train are at
level 36 - 40 … it is the last region where you spend 6 fuel per run (the next
region costs 7 fuel)`; best upper band `level 96 to 100`. Material tier is
decided by the level's last digit: `1 or 6` → Offense, `2 or 7` → Defense,
`3 or 8` → Bomber, `4 or 9` → Healer, `5 or 0` → no materials. This **corroborates**
`share_en/197745`'s "levels ending in 5 or 0 cost more" from an independent
source.

**Arena (verbatim, no numerals but two recovered mechanics):**
`fights in arena are automatic and do not use skills. As such, only the 3rd and
5th skills of all hunters apply in arena`; and the **element cycle** —
`Fire is strong against electric, electric is strong against ice and ice is
strong against fire`.

## 1.15 `List_of_Hunters` — the 54-row roster

Capture `20190826082717`, oldid `7480`. A `sortable` table with 54 data rows:
`Rarity / Hunter / Element / Role / Active Skill / Skill 2 (after active) /
Role Skill (passive) / Skill 4 (after active) / Skill 5 (passive)`.

The Rarity/Element/Role columns are **icons**, so their text extraction is empty
by design; the values were recovered from the `alt` attributes (§1.5). E.g.
row 1 = `1star-symbol.png` / `Captain` / `ElecIcon.png` / `DefenseIcon.png` /
`Attack skill` / `Block chance up` / `Defense up` / `Speed up` /
`Armour Penetration`; row 2 = `4star-symbol.png` / `Vincent` / `ElecIcon.png` /
`AttackIcon.png`; row 3 = `3star-symbol.png` / `Lantern` / `FireIcon.png` /
`BomberIcon.png`.

The same page's navbox gives a role × element roster grid:

| | Electricity | Fire | Ice |
|---|---|---|---|
| Offense | Balian, Bibi, Karl Steiner, Mowgli, Vincent, Windblade | Heidi, Hermes, Rebecca, Lily & Lyla, Santa Clauster, Sylvester | Beckhen, Lapis, Natalia, Octavia, Scar, Yuri |
| Defense | Bear, Captain, Edward, Juno, Kain, Riko | Athena, Calibur, Hecate | Dumble, Gerard, Harley, Nene, Papillon, Riko, Robin |
| Bomber | Diana, Gullveig, Sienna | Apollon, Lantern, Metis, Teddy Bomber | Dino, Levi, Locke, Patrone |
| Support | Acerola, Akasha, Crocus, Tyltyl | Bright, Denali, Joy, Tyltyl | Bruce Bang, Pansy, Sunny, Therapy |

**The navbox omits Riko from Defense/Ice, Apron/`Dumble` from Defense/Fire is
absent, and lists Riko and Tyltyl in two cells each** — a navbox maintenance
error, not a data claim. The 54-row sortable table is the better source.

## 1.16 Pages that are empty, stale, or redirects

| page | capture | oldid | finding |
|---|---|---|---|
| `Monsters` | 20190923070011 | 5833 | **Empty stub — zero tables, zero prose.** Monster coverage is unobtainable here. |
| `Hunter`, `Hunters`, `Roles`, `Element_Type` | 2019-08-21 → 2019-09-23 | **all `2091`** | Same revision under four titles — they are redirects. Body is a **stale 2017-era page**: "At present, there are **30 unique Hunters** available for recruitment", with role lists naming only ~10 per role. Superseded by `List_of_Hunters`' 54 rows. **`Element_Type` therefore carries no separate element documentation.** |
| `List_of_Blustone_Stories` | 20190821034342 | 7461 | 355,828 bytes but **pure table of contents** — per-character groupings of "Fate (Part 1..3)", "Your Journey Thus Far", "Missions", "Story", "Conversations". **No numerals, no stats.** |
| `Main_Page` | 20170825063314 | 2082 | Earliest capture, 2017 — predates the game-content burst. |

## 1.17 Settled negatives — each verified against a working control

The link graph of all 299 pages contains **2,449 distinct internal link
targets** (1,411 namespace, 1,038 article-shaped), of which **941 article
titles are linked but not in the archived 299**. Most are story/dialogue pages.
The important absences were probed directly:

| # | Probe (CDX exact-URL) | rows |
|---|---|---|
| — | **CONTROL** `vsfan.net/wiki/List_of_Hunters` | **2** ✔ |
| — | **CONTROL** `https://vsfan.net/wiki/Akasha` | **3** ✔ |
| 14 | `vsfan.net/wiki/Jewels` (**linked 227×**, in the navbox "Groups, objects and events") | **0** |
| 15 | `vsfan.net/wiki/Arena` | 0 |
| 16 | `vsfan.net/wiki/Mirage_Ruins` | 0 |
| 17 | `vsfan.net/wiki/Mirage_Ruins_Shop` | 0 |
| 18 | `vsfan.net/wiki/Metron` | 0 |
| 19 | `vsfan.net/wiki/Metron_Abyss` | 0 |
| 20 | `vsfan.net/wiki/Fishing` | 0 |
| 21 | `vsfan.net/wiki/Fish` | 0 |
| 22 | `vsfan.net/wiki/GvG` | 0 |
| 23 | `vsfan.net/wiki/Guild_War` | 0 |
| 24 | `vsfan.net/wiki/Set` | 0 |
| 25 | `vsfan.net/wiki/Events` | 0 |
| 26 | `w/index.php?title=Jewels` | 0 |
| 27 | `w/index.php?title=Arena` | 0 |
| 28 | `w/index.php?title=Fishing` | 0 |
| 29 | `w/index.php?title=Mirage Ruins` | 0 |

Both URL forms were tried for the key titles, and the controls returned rows in
the same run, so these zeros are real absences rather than a broken query.

- **Jewels: not archived, in either URL form.** The `Jewels` article is linked
  227 times from the navbox and exists, but its bytes were never captured. The
  jewelry dataset therefore gains nothing here and its 12 historical
  set-bonus families remain the ceiling.
- **Fishing: no article exists at all**, in the archive or in the link graph.
  The only `fish`/`bait`/`fishing` hits are 4 story-dialogue pages
  (`Harley`, `Therapy`, `The_Voice_that_Lingers`, `List_of_Blustone_Stories`).
- **GVG: no article exists.** `gvg` and `guild war` return **zero hits across
  all 299 pages**. Arena is documented only as `Fight Club` + a short PvP
  strategy section inside `Guide_to_Blustone`.

**Corpus-wide numeral scan.** Nine patterns (`HP`/`ATK`/`DEF`/`Health`/`Attack`/
`Defense` adjacent to a numeral, in both orders) over the tag-stripped text of
all 299 pages returned **15 hits total**, and every one is accounted for:
12 are the `Life/Attack/Defense` rows of the three complete tables, one is
Nene's `163.92 hp` skill effect, and two are `Roles`/`Element_Type`/`Hunter`
heading text ("has the highest defense and health"). **There is no other
statistic anywhere in the corpus.**

---

# 2. UNPUR

Everything in §2 is a numeral with unresolved identity, level, gear or unit
state, or with an era caveat. **None of it counts toward base-stat coverage.**

## 2.1 The three complete tuples are Transcendence-Level-3, not base

Captain, Hermes and Riko have `Life / Attack / Defense` — but their table is
captioned **`Transcendence Level: 3`**. These are therefore **boosted,
advanced-state values**, and the coverage ledger is explicit that a
level/rank-adjusted value counts only if the goal ledger calls it adjusted *and*
there is enough exact evidence to derive the base value. The caption supplies
the state but **not the level, not the rank, and not the equipped state**, and
§2.2 shows the implied multiplier is not yet pinned. So they are held here.

The saving grace is that §1.7 proves the rest of those tables is identical to
the 2019 Japanese database, so these three heroes are **not new identities** —
they are the same heroes with a *stated* boost state attached to values the
project already holds unboosted.

## 2.2 Candidate transcendence multiplier ≈ 1.27–1.30 on Life/Attack/Defense

Dividing the wiki's T3 values by the JP database's values:

| hero | hp ratio | atk ratio | def ratio |
|---|---|---|---|
| Hermes | **1.300** | **1.300** | **1.299** |
| Captain | 1.274 | **1.169** ← outlier | 1.279 |
| Riko | 1.274 | 1.273 | 1.275 |

**Hermes is a clean ×1.30 on all three fields.** Riko is internally consistent
at ≈1.274. Captain is consistent on hp/def (1.274/1.279) but its **Attack
breaks the pattern at 1.169**.

So the evidence supports a **transcendence-3 multiplier of roughly ×1.27–1.30
on Life/Attack/Defense**, but **not to three significant figures**, and not
uniformly across the three heroes. Two readings are possible and this pass
cannot separate them:

1. the true multiplier is ≈1.30 and Captain/Riko's underlying JP values are
   themselves slightly mis-transcribed; or
2. the multiplier differs per hero or per field.

**Do not implement ×1.30.** It is a one-decimal observation over three heroes
with one visible anomaly. Recorded as a rebalance lead only.

This is also the **only** evidence in the project tying a transcendence step to
a numeric stat change — `share-en-census-2026-10-05.md` §2.2.3 recovered the
transcendence *costs* but explicitly noted it said nothing about stat growth.

## 2.3 Captain's Attack ratio is an unresolved anomaly

`734 / 628 = 1.169`, against 1.274–1.300 for every other ratio in the table.
Candidate explanations, none demonstrated: a wiki transcription error in either
the 734 or the JP 628; a field-specific transcendence rule; or a rounding
artifact. **Unresolved.** Recorded so it is not silently smoothed away.

## 2.4 `hp_regen` off-by-one on Captain and Riko

Both read **40** on the wiki; the JP database reads **41** for `009` and `024`.
Every other sub-stat matches exactly, and the eight partial tables' `Life
Regeneration` values match their JP counterparts exactly. So this is a real
1-point discrepancy on two heroes, not a units artefact. Possible cause: a
patch-era edit between the two captures, or a transcription slip.
**Unresolved; the JP value is not superseded.**

## 2.5 Pansy element: wiki says Electric, two sources say Ice

| source | Pansy element |
|---|---|
| vsfan wiki infobox (2019-08-26, oldid 7458) | **Electric** |
| 2019 `blustone.jp` (`057`, 守備手/冷気) | Ice |
| local catalogue (`057`) | Ice |

Two against one. The wiki is the outlier. However the wiki's **own navbox**
places Pansy under **Support/Ice**, contradicting its own infobox — so the
error is *inside* the wiki and most likely an infobox slip. **Record the
conflict; do not resolve it by fiat.** Note this hero also has no JP numeric row
problem — her 9 sub-stats match exactly.

## 2.6 Race terminology: `Sapien` vs `Human` (not a data conflict)

Eleven heroes carry `Sapien` in the wiki where the catalogue says `Human`:
Gerard, Hecate, Locke, Robin, Sienna, Sunny, Sylvester, Teddy Bomber, and
(partially) Levi (`Robot / Werewolf` vs `Werewolf`). The wiki has dedicated
`Sapien`/`Sapiens`/`Humans`/`Human` pages all sharing **oldid 4450**, i.e.
**`Sapien` is a redirect to `Human`** — they are the same value under two
labels. **Not a discrepancy; a naming difference.** Recorded so it is not
counted as a conflict.

## 2.7 Robin's rarity: the wiki infobox is the outlier, three sources agree against it

The trace table supplies an independent rarity read, because a trace's star
count is a property of the material:

| hero | trace ★ | wiki infobox ★ | catalogue ★ | JP 2019 ★ | all four agree |
|---|---|---|---|---|---|
| **Robin** | **1** | **2** | **1** | **1** | **✗** |
| all other 26 traced heroes | = infobox | = catalogue | = JP | — | **✓** |

**26 of 27 agree on all four sources.** Robin's trace is ★ (= 1★ material,
value 20), matching the catalogue and the JP database; only the Robin
**infobox** says ★★. Since three independent sources — including the wiki's own
trace table — say 1★, **the Robin infobox ★★ is most likely a wiki error and
the catalogue/JP value of 1★ is better supported.** Flagged for the parent's
catalogue decision; this pass does not edit the catalogue.

## 2.8 Locke's trace value breaks the wiki's own Value↔Rarity rule

Within §1.10's table the mapping is perfectly consistent in 26 of 27 rows:

- ★ → **20** (Balian, Bruce Bang, Hecate, Lapis, Metis, Captain, Robin, Sienna, Sylvester, Tyltyl)
- ★★ → **100** (Acerola, Denali, Gerard, Levi, Mowgli, Rebecca, Riko, Teddy Bomber)
- ★★★ → **300** (Akasha, Athena, Hermes, Kain, Karl Steiner, Lantern, Nene, Octavia)

**The single exception is `Locke's Trace`, marked ★ but priced 100.** Either its
rarity should be ★★ or its value should be 20. The wiki does not say which.
Recorded as an internal inconsistency; **no value is adopted.**

~~This mapping is directly usable by the replica's
`/shop/PieceExchange` work, where the published trace thresholds are currently
**local fixtures** — but note §2.7's warning that Locke's own row is the
unreliable one.~~

**[RETRACTED 2026-10-05 — `trace-rarity-vote-2026-10-05.md` §1.1–§1.4, §2.2,
§2.6. Kept struck, not deleted.]** The juxtaposition was a **category error**.
The column header is `Image / Name / Description / Rarity / Areas Available /
Value`; the numeral lives in **`Value`**, a **per-trace-item worth** ("what one
trace is worth"), and this table has **no "required" / "amount" / "quantity" /
"threshold" / "cost" / "exchange" column anywhere**. `collect_qty` is a
**different physical kind of quantity**: traces **required per hunter**,
consumed as a **divisor** (`max hunters = floor(owned_qty / collect_qty)`,
`Gce1252..1262`). Unit price vs divisor ⇒ **NOT COMMENSURABLE**; the shared
numeral **20** at 1★ is a **coincidence of the numeral, not a shared quantity**.
This wiki's own use of the same column on the same page confirms "value":
Metron Fragment `Value 10` while skills consume 1–5; Metron Crystal `Value 1000`
is literally the `Fight_Club_Shop` price; Hunter Materials `10 / 50 / 250` while
skills consume 1–6. §2.8's `Locke` ★ priced **100** is the one row in 27 that
breaks the page's own rule, which is the ordinary signature of a person
estimating in a **price column** rather than transcribing a designed threshold.
**This mapping is therefore NOT usable against `/shop/PieceExchange` or
`collect_qty` 10/20.** The original §2.7 cross-reference warning about the
`Locke` row is retained above; the usability claim is withdrawn.

## 2.9 Two catalogue typos the wiki corrects

The wiki's accessory name for Windblade is `Unknown Shemagh`; the local
catalogue has **`Uknown Shemagh`** — a typo (missing `k`). The wiki is correct.
Similarly `Lyla's Cheer Cure` (wiki) vs `Lyla's Cheer Pom Poms` (catalogue) is
a genuine name variant that the game itself distinguishes (Lily's weapons,
Lyla's accessory). **One real catalogue typo identified; no edit made here.**

## 2.10 Duplicate wiki pages

`Karl` and `Karl_Steiner` are the **same revision (oldid 7370)**; `Teddy_Bomber`
and `TeddyBomber` are the **same revision (oldid 2971)**. They are redirects,
not distinct characters. **57 hero pages = 55 distinct characters.** Any count
built on "57" is wrong; the correct denominator contribution is 55.

Juno's page is also the one hero whose equipment names are literal
`???` placeholders (`???` / `???` / `???`) where the catalogue has `Monkey
Wrench` / `Protective Goggles` / `Tool Kit`. Another un-filled transcription.

## 2.11 Skill `Lv. 50` percentages — well-anchored identity, but not base stats

These are the cleanest numerals in the corpus: **identity is solid** (a named
hero page, not a portrait), **level is stated** (`Lv. 50`), and the value is
**not gear-dependent**. But they are *skill effect magnitudes*, not hero
attributes, so they fall outside the HP/ATK/DEF tuple the ledger counts.

Their real value is different: they are **the only community-sourced mapping
from a hero to a specific skill effect number**, which is precisely the gap
`server-ts/src/skills.ts` fills with fixtures. Two cautions:

- The **`Lv. 50` label is unqualified**. If it is max skill level rather than
  the level at which the number was read, the figures need not be reachable at
  other levels. Unresolved.
- The mixed `14%` / `14` formatting (§1.6) is unexplained. The values agree
  with the JP database's unitless integers, so a `%` reading is likely, but the
  corpus does not prove the unit for the bare-number pages.

## 2.12 The two equipment values (134) — same number on two different weapons

Beckhen's `Chicken Feet` and Yuri's `Skate Shoes` both read
`Increases attack Lv. 50 134`. Two independent weapon items sharing an exact
value is possible but unusual, and it is the **only** place in the corpus where
an accessory/weapon magnitude was ever entered. It is also **not base stats** —
it is one gear slot's contribution at Lv.50, on an otherwise unknown build.

Per the rule that a hero identity is never inferred from a portrait: these are
**textual** identifications from the equipment table, cross-checked against the
catalogue's `weapon` column, which agrees on both. That is the strongest form
of item identity available here. But the **gear build, level of the hero, and
whether the hero was otherwise equipped are all unknown**, so this cannot
become an accessory-coverage row. It is the first per-item attack magnitude
recovered outside the `Jack / Max HP 260 @ Lv.50` row, and it is filed as a
lead only.

## 2.13 Era tags — every stats reading is PRE-rebalance

Per [`stat-version-context.md`](stat-version-context.md), the official balance
change "took hold after 2019-09-05" (equipment +50%, crystal main +30%/+50%,
substats +50%).

| reading | capture | era |
|---|---|---|
| **All 11 `Character Attributes` tables** | 2019-08-21 and 2019-08-26 | **PRE-2019-09-05** |
| `List_of_Hunters` 54-row roster | 2019-08-26 | PRE |
| `List_of_Blustone_Items` trace table | 2019-08-21 | PRE |
| `Hunters'_Drop_Rate` | 2019-08-21 | PRE |
| `Fight_Club_Shop` prices | 2019-08-21 | PRE |
| Beckhen's / Yuri's equipment `134` | 2019-08-26 / 2019-08-21 | PRE |
| `Veteran_Status` ladder | 2019-09-23 | **POST** |
| `Guide_to_Blustone` (skills, transcendence) | 2019-09-23 | **POST** |

**Every base-stat-adjacent reading is from 2019-08-21/26, i.e. before the
rebalance threshold.** They are therefore internally consistent with each other
and with the JP database, which is why §1.7's 97/108 agreement is meaningful —
but they describe **pre-2019-09-05 balance**, not 2.8.0.1. Note also that some
pages have later captures (Akasha 2019-10-15 and 2019-12-09; List_of_Hunters
2019-11-14); this pass used the **earliest** capture per URL, so §1.4's ledger
is a pre-threshold snapshot by construction.

## 2.14 What this wiki does **not** contain

Stated plainly, because these are the things a reader might assume it holds:

- **No nude/base HP·ATK·DEF for 54 of the 55 heroes** it documents.
- **No accessory/jewel stat table.** `Jewels` was never archived. The two
  equipment values in §2.12 are hero-specific weapon rows, not an item catalog.
- **No monster statistics whatsoever** — the `Monsters` page is an empty stub.
- **No fishing content**; **no GVG content**; no arena stat tables (the Arena
  article was never archived either — only `Fight Club` and a PvP prose section
  exist).
- **No per-level growth curve.** No source here relates a stat to a level, so
  the project's `100 × (level−1)` XP curve and stat growth remain unsupported.
- **No player-screenshot evidence.** Unlike `share_en`, the wiki is text-first;
  its images are 20–110 px icons and official renders, and the `565`/`567`
  namespace gap that killed the `share_en` image lane **does not apply here**.

## 2.15 Method limits

- **`collapse=urlkey` returns one row per URL**, so per-page multi-capture
  history is unavailable. The 299-page ledger uses the **earliest** capture per
  URL. Where later captures exist they were not mined, so **newer revisions
  may carry more Stats tables or filled-in equipment cells** — this is the most
  likely place a future pass would gain.
- **The corpus is what one 2019-08/09 crawl saw.** 941 linked article titles
  are unarchived, and the archive's per-page content is a snapshot of an
  actively-edited wiki; the equipment tables (§1.8) and the 8 partial stat
  tables (§1.6) are demonstrably *incomplete transcriptions*, not evidence of
  absent game data. **The wiki's silence is not the game's silence.**
- **`<` and `>` inside prose survive as `&lt;`/`&gt;`** in the raw wikitext and
  were left as-is in the §1.10/§1.13 transcriptions rather than silently
  normalised, because they mark template boundaries.
- **Icon→meaning mapping was verified, not assumed**: `alt` attributes were read
  for every role/element/rarity cell, and the icon vocabulary is closed
  (4 roles, 3 elements, 5 star symbols — §1.5) with no unexplained members.
- **No identity was inferred from a portrait.** Every hero and item name in
  §1 comes from page text and was checked against the local catalogue.
- **All fetches were GET-only reads of `web.archive.org`.** No archive write,
  no `savepagenow`, no form submission, no login. No project server, APK,
  emulator, phone, or `server-ts` change was made. The only writes were this
  file and scratch files under the temp directory.

---

# 3. Coverage disposition

| Dataset | Before | After | Change |
|---|---|---|---|
| Hero base stats | 1 / 113 (0.9%) | **1 / 113 (0.9%)** | **0** |
| Jewel set bonuses | 12 / 12 historical families | unchanged | 0 |
| Mounted jewel panels | 6 / 6 observed samples | unchanged | 0 |
| Accessories | 1 / 100 distinct names | **1 / 100** | **0** |
| Monsters | 0 / 22 | **0 / 22** | **0** |

**No new base-stat tuples. No coverage inflation.** Every §2 reading is
quarantined from the strict ledgers for the reasons stated per item: unknown
level/rank/gear (§2.1, §2.11, §2.12), an unresolved multiplier (§2.2, §2.3), or
an outright conflict (§2.4, §2.5, §2.7, §2.8).

**What this lane actually delivered**, in order of value to the project:

1. **State context the JP database lacked** — an explicit
   `Transcendence Level: 3` caption on three complete stat tables, and a
   candidate ≈1.27–1.30 T3 multiplier on Life/Attack/Defense (§2.2). This is
   the project's first community-sourced link between a transcendence step and a
   stat change.
2. **Schema proof** — 97/108 exact agreement with the 2019 JP database
   establishes the two corpora measure the same thing, which retroactively
   strengthens the 62 existing archive candidate tuples.
3. **55-hero rarity/role/element corroboration** across four independent
   sources, agreeing on all but two heroes (§1.7, §2.5, §2.7) — plus a
   concrete recommendation that the catalogue is right about Robin's 1★.
4. **A trace rarity + value table** (★=20 / ★★=100 / ★★★=300, 27 rows)
   ~~that can replace the replica's local `PieceExchange` threshold fixtures~~,
   with the Locke caveat (§2.8). **[2026-10-05 — the "can replace" claim is
   RETRACTED per `trace-rarity-vote-2026-10-05.md` §1.1–§1.4/§2.2: `Value` is
   a per-trace rarity VALUE and is NOT COMMENSURABLE with the `collect_qty`
   threshold (divisor). It replaces nothing. It does contribute the §2.7 Robin
   rarity reading on a separate axis.]**
5. **Original-era economy data** — gacha drop rates, the veteran ladder, Fight
   Club Shop prices, the skill cost table with its implied level-50 cap, the
   transcendence matrix, Abyss/ruins costs, and the fire→electric→ice→fire
   element cycle (§1.11–§1.14).
6. **Three settled negatives** — jewels, fishing and GVG are absent from the
   archive, proven against working controls (§1.17), so those lanes should not
   be re-attempted here.

**Suggested next step, if this lane continues:** mine the **later** captures of
the 11 hero pages. All 11 were read at their 2019-08-21/26 revision; Akasha has
captures at 2019-10-15 and 2019-12-09, and `List_of_Hunters` at 2019-11-14. If
the equipment cells and the 8 partial `Character Attributes` tables were filled
in later, a post-rebalance second reading would exist and could be separated
from the pre-threshold one.

**Files written:** this file only. `polluted-observations.md` is
**deliberately not appended to** — the parent mirrors this lane's numeric
observations into that ledger. `coverage.md`, `README.md`, `coverage.tsv`, the
archive TSVs, `analysis/catalogue/`, `server-ts`, and all APK/seed material are
**untouched**.
