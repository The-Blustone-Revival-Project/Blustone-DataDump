# Wayback company-blog / news / snapshot lane — 2026-10-05

Lane: `visualshower.com` company blog 2017–2019 sweep for Blustone posts,
Genovia (`056`) single-capture alternate window, `blustone.jp` news/event
2020+ single-shot censuses, TapTap/Inven snapshot check for hunter stat tables.
Read alongside `wayback-hunter-2026-10-05.md` (CDX: exactly two 200 index
captures 20191015/20191209, 163 urlkeys = 63 profiles, no 064–098/awakened
pages, `bs.visualshower` throttled 503, Genovia single capture placeholders)
and `archive-jp-fill-2026-10-05.md`. No server/APK changes. No TSV appends:
no provenance-clean rows exist. Queries were single-shot and spaced; 503/429
responses were recorded with no bypass and no retry loop.

## CDX queries issued (all via `https://web.archive.org/cdx/search/cdx`)

1. `url=visualshower.com*`, `from=2017&to=2019`,
   `fl=timestamp,original,statuscode`, `collapse=urlkey`,
   `filter=statuscode:200`, `filter=original:.*lustone.*`, `limit=50`
   → HTTP 200, **4 rows**:
   - `20190413074438 http://www.visualshower.com/blustone-blacklist-20180502/ 200`
   - `20190413074447 http://www.visualshower.com/blustone-blacklist-20180502/feed/ 200`
   - `20170522232250 http://www.visualshower.com:80/game/blustone/ 200`
   - `20170609030603 http://www.visualshower.com/game/blustone/feed/ 200`
   Company game page + one blacklist notice (+ feeds). No hunter-profile or
   stat-table URL among the hits. This distinguishes the company site
   (`visualshower.com`, corporate/game pages) from the unreachable
   `bs.visualshower.com` character-intro posts (Heidi `document_srl=707457`,
   Lily&Lala `426682`, Kalbaram `912433`), which remain failed captures per
   `wayback-hunter-2026-10-05.md` §3.
2. Genovia (`056`) alternate-window re-check: exact encoded profile URL
   (`.../hunter/レアリティ別/贖罪の「ジェノビア」`), `from=2019&to=2021`,
   `fl=timestamp,original,statuscode,digest`, `limit=20` → HTTP 200, **1 row**:
   - `20191216052325 .../ジェノビア」 200 CA342SZZYEWUVE3GHVW5SURBYCO7GXGZ`
   Confirms the prior lane: a **single** 200-capture, digest-stable, already
   harvested as `???` placeholders (`non-numeric-core-stats` in
   `archived-hunter-database-2019.tsv`). No alternate numeric capture exists
   in the 2019–2021 window. No TSV change.
3. `url=blustone.jp/news*`, `from=2020`, `collapse=urlkey`,
   `filter=statuscode:200`, `limit=50` → **empty body** (HTTP-level OK, zero
   rows). Consistent with no 2020+ news captures; weak evidence on its own,
   recorded only as a single-shot census result, not a closed-set claim.
4. `url=blustone.jp/event*`, `from=2020`, same shape → **empty body**, same
   qualification as (3). No event-page stat source surfaced.
5. `url=taptap.io/post/73656` (2019-09-04 rebalance post, already transcribed
   in `stat-version-context.md`), `fl=timestamp,original,statuscode,digest`,
   `limit=20` → **request timed out** under IA throttling. Recorded as a
   failed snapshot check; nothing inferred. Existing transcription stands:
   equipment +50%, 1–3★ crystal mains +30%, 4–5★ mains +50%, all crystal
   substats +50% — version-stratification context only, no per-hero values,
   no coverage credit.
6. `url=inven.co.kr/webzine/news/*212307*` (2018-12-20 Blustone 2 interview,
   already logged in `coverage.md`), `limit=20` → **HTTP 503** from the CDX
   endpoint. Recorded as throttled; no bypass, no further retries this lane.
   Existing entry stands (title-lineage context only, embedded video
   previously throttled, no stat values).

## Capture-body check (1 page, read-only)

- `https://web.archive.org/web/20170522232250/http://www.visualshower.com/game/blustone/`
  (the 2017 company game page from query 1) → renders corporate page:
  genre RPG, development Feb 01 2007, published May 13 2017, iOS/Android,
  self-published; Korean tagline/description paragraphs; press links
  (Inven, HungryApp launch coverage); SCREENSHOT section headers. **No hero
  roster, no HP/ATK/DEF panel, no jewel/accessory or monster tuple.** Not a
  stat source. The blacklist/feed URLs from query 1 were not body-fetched:
  notice/feed pages are not plausible 13-field stat sources and further
  fetches would risk throttling the shared CDX session.

## New 13-field rows transcribed this pass: 0

No provenance-clean numeric profile exists for any of the 51 uncovered IDs in
this lane's sources. Nothing was appended to
`archived-hunter-database-2019.tsv`; the existing 62 rows are untouched.
Strict hero coverage is unchanged at **1/113 (`051`)**.

## Level/gear context

No page touched in this lane (company game page, CDX hit lists, empty
news/event censuses, failed TapTap/Inven snapshot checks) prints a hero level
or states equipped vs associated gear. The level/gear-unknown verdict on all
62 existing archive rows stands; all remain outside strict coverage
(rebalance anchors only).

## Still-missing IDs: disposition unchanged (51)

- 15 awakened variants (`004_1`, `005_1`, `009_1`, `010_1`, `011_1`, `017_1`,
  `019_1`, `020_1`, `021_1`, `024_1`, `026_1`, `034_1`, `038_1`, `056_1`,
  `086_1`): unfillable from archive sources by design (draw-state profiles
  only; empty ★5 index section; 63-URL census).
- 35 base IDs `064`–`098` (Geranium through Selene-Valentine): post-2019
  roster; no archive page exists. Need non-archive visual sources.
- `056` Genovia base: single capture `20191216052325`, placeholders only,
  digest `CA342SZZYEWUVE3GHVW5SURBYCO7GXGZ`; already in TSV as
  `non-numeric-core-stats`.

## Throttling log

- TapTap CDX: timeout (1 attempt, no retry).
- Inven CDX: HTTP 503 (1 attempt, no retry).
- `blustone.jp` news/event 2020+ censuses returned empty bodies (not errors);
  not re-queried.
- No query was retried after a failure; no bypass was attempted. Total CDX
  calls this lane: 6. Total capture-body fetches: 1.

## Files updated

- `analysis/research/base-stats-visual-hunt/wayback-blog-2026-10-05.md`
  (this file; new). No other file modified.
