# ApkHere tail + store-gallery spine audit (2026-10-05)

**Lane:** QooApp 24-screenshot gallery classes, ApkHere 1.2.1.1 / 1.4.x
listing rows, Stahuj / ProDroid / BrowserCam version rows for the spine.
**Result: negative for stats.** No binary downloaded, no login/gate bypassed,
no server/APK change. No listing page exposes per-hero/per-monster/per-item
numeric rows. Coverage impact: **none** (heroes 1/113, accessories 1/100,
monsters 0/22, unchanged).

Prior session: [`qooapp-apk-2026-10-05.md`](qooapp-apk-2026-10-05.md)
(QooApp 2.1.7.3 108MB POST pin, cards route exhausted, ApkHere 67-build
tail with template-size caveat, TapTap codes 28010/28000/27990, cheapest
PRE target 1.2.1.1 2017-12-21, server-side `/reference/*` conclusion).
This file re-verifies the listing rows live, screens the gallery classes,
and pins the store version spine. §1 is pure (listing metadata + gallery
classes screened); §2 holds every visible numeral/version anchor as impure.

## 1. Pure findings (listing metadata only, no binaries)

### 1.1 QooApp 24-screenshot gallery screened (live fetch 2026-10-05)

- **URL:** `https://apps.qoo-app.com/en/app/6128` (English mirror; same
  build as the Indonesian page in the prior pass).
- **Inventory:** exactly **24 screenshot thumbnails** (Screenshot 1–24) plus
  **1 gameplay-video thumbnail** (YouTube embed). All 24 carry the identical
  generic caption `Screenshot N: Blustone 2 - Anime Battle and ARPG Clicker
  Game`; no per-image titles, no stat-panel advertisement, no hero/item
  labels anywhere in the listing markup.
- **Classes:** **unresolvable from listing text alone.** The captions do not
  distinguish promo art, battle HUD, village, or roster panels, so no
  per-image class is assigned and none is inferred. Thumbnail pixels were not
  fetched (binaries stay out of git per tasking); the video was not played.
  Prior gallery audits of the same promo/village/battle art classes
  (`README.md`, `coverage.md`) already cover those classes with no stat
  panel found — this pass adds inventory, not pixels.
- **Listing pin (metadata):** package `com.vshower.prd_sr`, POST-rebalance
  build, sign-in/device-linked download gate not attempted.

### 1.2 ApkHere listing rows: 1.2.1.1 tail + full 1.4.x family (live fetch 2026-10-05)

- **URL:** `https://cn.apkbe.com/app/com.vshower.prd_sr`. History list
  re-verified live: **67 dated rows**, tail 1.2.1.1 (2017-12-21) → head
  2.5.9.0 (2020-09-18). Every row is a version + date + per-build
  `/down/com.vshower.prd_sr_<ver>_free` link; no row carries size, changelog,
  or stat content.
- **Tail row:** 12/21/2017: Blustone 1.2.1.1 — oldest mirrored build, cheapest
  PRE-rebalance physical target (predates 2019-09-05 by ~21 months).
  Not downloaded.
- **1.4.x family (all 16 rows, PRE-rebalance, none downloaded):**
  1.4.0.0 (06/22/2018), 1.4.0.2 (06/24/2018), 1.4.1.2 (06/30/2018),
  1.4.2.1 (07/13/2018), 1.4.2.4 (07/19/2018), 1.4.3.4 (07/31/2018),
  1.4.3.5 (08/03/2018), 1.4.4.0 (08/12/2018), 1.4.4.1 (08/15/2018),
  1.4.5.0 (08/24/2018), 1.4.6.1 (09/12/2018), 1.4.7.0 (09/23/2018),
  1.4.7.1 (10/06/2018), 1.4.7.2 (10/07/2018), 1.4.8.1 (10/15/2018),
  1.4.8.2 (10/19/2018).
- **Family-count correction:** this live fetch counts 1.2.x = 11 rows,
  1.3.x = 14 rows, 1.4.x = 16 rows (total still 67). The prior file's
  `8 / 11 / 12` breakdown in §1.3 is superseded; the 67 total, the tail/head
  versions, and the template-size caveat stand.
- **Template-size caveat reconfirmed:** only the head row carries a size/date
  block; per-build sizes below the head remain unverified template
  inheritance (prior pass proved it with the 1.4.4.1 down page vs the
  measured 94,877,834 B local APK). No per-build size is quoted as fact.
- **ApkHere gallery:** 3 snapshot images (`snapshots/1–3.jpg`), generic
  presentation, uninspected (no binary fetch). Description text is the
  standard frozen-tundra / 10-taps / 4-role-team marketing copy — content,
  not stats.

### 1.3 Stahuj.cz version row (live fetch 2026-10-05)

- **URL:** `https://www.stahuj.cz/android/hry/dobrodruzne/blustone/`.
- **Row:** Blustone **2.5.7.0**, author VisualShower Corp., POST-rebalance,
  Czech listing with the standard marketing description and permission
  boilerplate. Languages EN/CN/JP/KR. No changelog, no stat content.
- **Gallery:** 4 preview thumbnails on the main page plus a `7 náhledů`
  (7-preview) gallery page; all carry the generic alt `Blustone - náhled`.
  Prior audit visually inspected all 7 (images 1–6 promo/battle art, image 7
  village; no stat panel) — that inspection stands and is not repeated here;
  this pass screens listing structure only.

### 1.4 ProDroid version row (live fetch 2026-10-05)

- **URL:** `https://prodroid.org/5661-blustone`.
- **Row:** BLUSTONE **2.7.9.2**, VisualShower Corp., role-playing,
  POST-rebalance. Download requires site login; not attempted, nothing
  fetched. Description is Russian marketing copy (hunter team, Hunter Guild,
  Fight Club, trace search, Ice Fishing) — content, not stats.
- **Gallery:** 7 thumbnails, all with the identical generic alt `Screenshot
  BLUSTONE`, plus 1 YouTube thumbnail. No per-image captions, so classes are
  unresolved from listing text; pixels not fetched (prior pass hit a 403 on
  the image CDN; this pass makes no image request at all). No values inferred.

### 1.5 BrowserCam version row (live fetch 2026-10-05)

- **URL:** `https://www.browsercam.com/apk/com.vshower.prd_sr/` now returns
  **HTTP 404** — the listing is gone.
- **Spine value (archived, unchanged):** version 2.0.5.1, listing updated
  2018-08-22 (PRE-rebalance), 3 screenshots previously inspected (promo art,
  battle montage, fishing scene; no stats) per `README.md` / `coverage.md`.
  The 404 changes nothing about that archived evidence; no replacement
  source was sought.

### 1.6 Negative results diligently recorded

- 24 QooApp captions inventoried, 0 classifiable from text; video not played.
- 67 ApkHere rows inventoried (tail + 1.4.x family transcribed above),
  0 with stat content; no binary fetched.
- Stahuj / ProDroid rows pinned from live markup; galleries structure-only.
- BrowserCam listing confirmed dead (404); archived inspection stands.
- Server-side `/reference/*` conclusion from the prior pass stands: low prior
  for embedded per-entity stat tables in ANY mirrored build, pre- or
  post-rebalance.

## 2. Impure tokens (version anchors and visible numerals — NOT base stats)

Every token below is listing-page metadata or marketing text preserved for
spine/rebalance-era use only. None is a hero base tuple, accessory row, or
monster HP/ATK/DEF value. No coverage credit.

- **QooApp pin:** `2.1.7.3` / `108.53 MB` / `2022-07-14` / rating `4.1` from
  `124` ratings / `39` comments; Android `4.4W+`; package `com.vshower.prd_sr`.
  Gallery: `24` screenshots + `1` video, video ID `5PyrPVT_Ofs`.
  Source: `https://apps.qoo-app.com/en/app/6128`.
- **ApkHere head:** `2.5.9.0` / `104.3 MB` page claim / `2020-09-18` /
  Android 4.4+. Tail: `1.2.1.1` / `12/21/2017`. 1.4.x boundary rows:
  `1.4.0.0` `06/22/2018` … `1.4.8.2` `10/19/2018` (full 16-row date list in
  §1.2). Total `67` rows. Per-build sizes below head unverified (template).
  Source: `https://cn.apkbe.com/app/com.vshower.prd_sr`.
- **Stahuj row:** `2.5.7.0` / `103 MB` / updated `17. 2. 2020` / rating `3`;
  `4` page thumbs + `7`-preview gallery page.
  Source: `https://www.stahuj.cz/android/hry/dobrodruzne/blustone/`.
- **ProDroid row:** `2.7.9.2` / `1.08 GB` page claim / updated `29 Nov 2024` /
  rating `5.0` from `1` vote; `7` thumbs + `1` video (`vsiZlUIOg_E`);
  description claims `90` huntresses (marketing text, not a catalog count).
  Source: `https://prodroid.org/5661-blustone`.
- **BrowserCam (archived):** `2.0.5.1` / listing update `2018-08-22`;
  live URL now `404`.
- **Era tags:** 1.2.1.1, all 1.4.x, 2.0.5.1 = PRE-rebalance (before
  2019-09-05); 2.5.7.0, 2.5.9.0, 2.1.7.3, 2.7.9.2 = POST-rebalance.
