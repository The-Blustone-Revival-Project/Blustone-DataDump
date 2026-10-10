# Wayback hunter sweep — 2026-10-05

Sweep of the Wayback Machine for BLUSTONE hunter stat pages covering the 51 IDs
in `uncovered-archive-roster-2019.tsv` with no numeric 2019-archive row.
Read alongside `archived-hunter-database-2019.md` / `.tsv` (62 rows),
`uncovered-archive-roster-2019.tsv` (51 missing), `coverage.md`, and the prior
fill lane `archive-jp-fill-2026-10-05.md`, which this pass independently
re-checks. No server/APK changes. No existing file was overwritten.

## CDX queries issued (all via `https://web.archive.org/cdx/search/cdx`)

1. `url=blustone.jp/hunter/<rarity-band>` (exact index URL),
   `fl=timestamp,original,statuscode`, `limit=50` → HTTP 200, 2 rows:
   - `20191015065805 …/hunter/レアリティ別 200`
   - `20191209130354 …/hunter/レアリティ別 200`
   Only two successful captures of the rarity-index URL exist. No later index
   revision that could add hunter pages.
2. `url=blustone.jp/hunter/*`, `fl=timestamp,original,statuscode`,
   `collapse=urlkey`, `filter=statuscode:200`, `limit=300` → HTTP 200,
   163 urlkeys. Filtering to profile-base shape
   (`/hunter/レアリティ別/<title>` with no further path segment) yields
   exactly **63 profile-base URLs** — the same 63 Japanese-title links
   harvested from the October 2019 index. Remaining urlkeys are attachment /
   image sub-routes (`/becken`, `/becken-s`, `/varian`, `/xenovia-s`, …),
   facet pages (`/タイプ別`, `/menu-c-attribute`, `/menu-c-type`,
   `/hunterguild`) and the bare `/hunter` hub. **No profile URL exists for
   any catalog ID 064–098 or any awakened `_1` variant.**
3. `url=bs.visualshower.com*` (and `document_srl=707457` variant),
   `collapse=urlkey`, `limit=100/20` → timed out / HTTP 503
   ("Temporarily Offline") on every attempt this pass. `coverage.md` already
   records the live-host result: HTTPS fails with an SSL protocol error and
   HTTP redirects to a GNAME domain-sale page for `visualshower.com`, so no
   Heidi (`document_srl=707457`) or Lily&Lala (`document_srl=426682`)
   character-intro post content was accessed. Failed capture, reason recorded;
   nothing inferred.
4. `url=blustone.jp/hunter/*` with `from=2020` → HTTP 200 with an empty body
   on the one attempt that returned (a retry 503'd under IA throttling).
   Consistent with no 2020+ hunter-profile captures; the empty-body result is
   weak evidence on its own and is NOT the basis for the closed-set claim —
   the collapsed full-census result in (2) is.
5. Genovia (`056`) single-profile CDX re-checks (exact encoded title URL, with
   and without `digest` field) → one HTTP 200 empty body, one timeout under
   IA throttling. Not independently re-verified this pass; the prior lane's
   result (single 200-capture `20191216052325`, `???` placeholders, already in
   the TSV as `non-numeric-core-stats`) stands uncontradicted.
6. `url=visualshower.com*` (company blog, no `bs.` subdomain) → HTTP 200;
   hits are unrelated company-blog posts, not hunter profiles. Not a stat
   source; noted only to distinguish it from the `bs.visualshower.com`
   character-intro posts in (3).

## taptap.io/post/73656 context

Already transcribed in `stat-version-context.md` (2019-09-04 post by `SmileV`,
effective after 2019-09-05): equipment +50%, 1–3★ crystal mains +30%, 4–5★
mains +50%, all crystal substats +50%, larger post-Lv.20 upgrade gains.
No per-hero, per-item, or per-monster values. Version-stratification context
only; no coverage credit and no re-fetch performed here.

## New 13-field rows transcribed this pass: 0

```
"listed_name"	"profile_title"	"role_ja"	"element_ja"	"rarity_on_draw"	"combat_power"	"hp"	"atk"	"def"	"speed"	"crit"	"crit_damage"	"penetration"	"block"	"block_damage_reduction"	"element_enhance"	"element_resistance"	"hp_regen"	"level"	"gear_state"	"fetch_status"	"source_url"	"catalog_id"	"identity_match"	"capture_timestamp"
(no data rows — no provenance-clean numeric profile exists for any of the 51 uncovered IDs)
```

Nothing was appended to `archived-hunter-database-2019.tsv`: there is no
provenance-clean row to append, and the existing 62 rows are untouched.

## Level/gear context

No index, profile, gallery, or listing page touched by any CDX hit in this
pass prints a hero level or states equipped vs associated gear. The
level/gear-unknown verdict on all 62 existing rows stands; all remain outside
strict coverage (rebalance anchors only). Strict hero coverage is unchanged
at **1/113 (`051`)**.

## Placeholder-only rows and failed captures

- `056` Genovia: placeholder-only (`???`), already in TSV; no alternate
  numeric capture found by any census to date.
- `bs.visualshower.com` (Heidi 707457, Lily&Lala 426682, Kalbaram 912433):
  failed captures — CDX throttled (timeout/503), live host unreachable
  (SSL error / domain-sale redirect). Contents unknown, no values inferred.
- IA throttling note: repeated CDX calls in one session return 503/timeout;
  space queries out or accept single-shot censuses. The two successful
  censuses above were one-shot queries, not scraped page bodies.

## Still-missing IDs: all 51 (disposition unchanged)

- 15 awakened variants (`004_1`, `005_1`, `009_1`, `010_1`, `011_1`,
  `017_1`, `019_1`, `020_1`, `021_1`, `024_1`, `026_1`, `034_1`, `038_1`,
  `056_1`, `086_1`): unfillable from this archive by design — profiles
  document draw-state hunters only; the empty ★5 index section plus the
  63-URL CDX census prove no awakened profile page was published there.
- 35 base IDs `064`–`098` (Geranium through Selene-Valentine): post-2019
  roster; no archive page exists. Need non-archive visual sources.
- `056` Genovia base: page exists but renders placeholders only.

## Files updated

- `analysis/research/base-stats-visual-hunt/wayback-hunter-2026-10-05.md`
  (this file; new). No other file modified.
