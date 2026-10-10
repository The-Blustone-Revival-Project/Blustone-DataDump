# QooApp / ApkHere / TapTap small-build metadata audit (2026-10-05)

**Lane:** QooApp 2.1.7.3 listing + cards metadata, ApkHere 1.2.x–1.4.x
small-build metadata, TapTap version codes 28010/28000/27990, any sub-200MB
build that could hold pre-rebalance tuning.
**Result: negative.** No binary downloaded (all payloads ~95 MB–1 GB; binaries
stay out of git per tasking). No listing page exposes per-hero/per-monster/
per-item numeric rows. All version metadata below is listing-page data only.
Coverage impact: **none** (heroes 1/113, accessories 1/100, monsters 0/22,
unchanged). This file holds BOTH the pure findings (§1) and the impure/raw
tokens (§2) for this session.

Prior session: `old-apk-2026-10-05.md` (1.4.4.1 52-jet art/audio-only audit,
LEVELING shared tuning, version spine, server-side `/reference/*` conclusion).
This session extends its version spine with re-verified live metadata and
records the cheapest sub-200MB physical targets without fetching them.

## 1. Pure findings (listing metadata only, no binaries)

### 1.1 QooApp listing re-verified (live fetch 2026-10-05)

- **URL:** `https://apps.qoo-app.com/id/app/6128` (Indonesian locale page;
  English mirror at `/en/app/6128` shows the same build).
- **Title:** Blustone2 — "Blustone 2 - Anime Battle and ARPG Clicker Game".
- **Developer:** VisualShower Corp. Tags: ADV / Running / Arcade /
  Android / Mobile.
- **Pinned build:** Package `com.vshower.prd_sr`, Version **2.1.7.3**,
  Last Updated **2022-07-14**, APK Size **108.53 MB**, Requirements
  Android 4.4W+, Data pack N/A, "no longer in operation" banner.
- **Rating:** 4.1 from 124 ratings / 39 comments (unchanged from prior pass).
- **Download gate:** "Sign in & Download" / device-linked install flow —
  not attempted; no binary fetched, no login performed.
- **Description:** Indonesian store text (frozen-tundra treasure hunt,
  10+ taps/sec, 4-role team: offense/defense/bomber/healer, cinematic
  scenes). Content/marketing only, no stat rows.
- **Gallery:** 24 screenshots + 1 gameplay video thumbnail on the listing;
  thumbnails not opened frame-by-frame this pass (prior gallery audits cover
  the same promo/village/battle art classes; no stat panel is advertised).
- **Era tag:** 2022-07 = POST-rebalance (2019-09-05). Even as a physical
  target it would carry post-rebalance tuning, not pre-rebalance anchors.

### 1.2 QooApp Cards route (live fetch 2026-10-05)

- **URL:** `https://apps.qoo-app.com/en/app-card/6128`.
- **Contents:** exactly **one** shared game card, by `Wong Zi Xian`
  (user 20745640), dated **2020-07-04 11:28:12**, "Game Card created,
  1 cards shared". Player Name field reads `友`; introduction text is
  garbled (`？？？？为什么一直這樣子啊` — a user complaint, not game data).
  Card image did not render a stat panel in the fetched markup; like/share
  counters are 1/0.
- **Result:** no hero identity, no HP/ATK/DEF, no item data. Cards route is
  exhausted for this title (single entry, no stats).

### 1.3 ApkHere (cn.apkbe.com) history tail (live fetch 2026-10-05)

- **URL:** `https://cn.apkbe.com/app/com.vshower.prd_sr`; current head is
  **2.5.9.0**, size **104.3 MB**, updated **2020-09-18**, Android 4.4+,
  category role-playing.
- **History tail re-verified:** 67 dated entries from **1.2.1.1
  (2017-12-21)** to **2.5.9.0 (2020-09-18)**. Pre-rebalance (2017-2018)
  rows present: 1.2.1.1 → 1.2.9.x (8 rows), 1.3.0.0 → 1.3.9.x (11 rows),
  1.4.0.0 → 1.4.8.2 (12 rows), 1.5.0.2 (2018-11-15), 2.0.1.0 → 2.0.9.1
  (2018-11/2019-01). Post-rebalance rows: 2.1.1.0 (2019-02-23) onward.
  Full dated list matches the spine in `old-apk-2026-10-05.md` §1; no
  versions older than 1.2.1.1 are listed anywhere.
- **Per-build download routes** (`/down/com.vshower.prd_sr_<ver>_free`)
  were **not** fetched as binaries.
- **Metadata-reliability caveat (new):** the per-version down page for
  `1.4.4.1` (`/down/com.vshower.prd_sr_1.4.4.1_free`) shows a
  "coming-download" bot-gate page whose version/size/date block reads
  **1.4.4.1 / 104.3 MB / 2020-09-18** — i.e. it reuses the *current-head*
  (2.5.9.0) size and date template. Treat every ApkHere per-build size/date
  below the head row as **unverified template inheritance**, not a measured
  build fact. The locally held 1.4.4.1 APK measures 94,877,834 B, which
  contradicts the page's 104.3 MB and confirms the template reuse.

### 1.4 TapTap version codes (live fetch 2026-10-05)

- **URL:** `https://www.taptap.cn/app/49376/all-info` (青石之战).
- **Codes confirmed:** 2.8.0.1 = **28010** (2022-07-14), 2.8.0.0 = **28000**
  (2022-06-20), 2.7.9.9 = **27990** (2022-06-16). Changelogs for all three
  are the generic "优化游戏/改进稳定性，修复其它Bug" (optimize/stability,
  bug fixes) — no balance/stat notes.
- **Anchors:** vendor VisualShower Corp., supplier HONGKWANPARK, Android
  launch **2017-05-15** (matches the Inven soft-launch anchor in
  `polluted-observations.md`), Android 4.4+, Simplified Chinese + 4 more
  languages, in-app purchases present.
- **Result:** codes pin the late-version spine only; no downloadable old
  build, no stat content.

### 1.5 Sub-200MB build ranking (metadata only)

| Build | Size claim | Date | Era | Status |
|---|---|---|---|---|
| 1.4.4.1 (locally held) | 94,877,834 B measured | 2018-08-15 | PRE | Already audited: art/audio only (§old-apk §2) |
| 2.5.9.0 (ApkHere head) | 104.3 MB page claim | 2020-09-18 | POST | Not downloaded |
| 2.1.7.3 (QooApp pin) | 108.53 MB page claim | 2022-07-14 | POST | Not downloaded; sign-in gate |
| 1.2.1.1 (ApkHere tail) | page size unverified (template caveat) | 2017-12-21 | PRE | Oldest known mirror build; not downloaded |
| split base.apk + PADResource (Reddit Drive) | 93.7 MB + 902.7 MB | 2801-era | POST | Not downloaded |

- **Cheapest PRE-rebalance physical target:** ApkHere **1.2.1.1**
  (2017-12-21) — oldest mirrored build, predates the 2019-09-05 rebalance
  by ~21 months. Its per-build size is unverified (see §1.3 caveat) but the
  1.x family ships ~95–110 MB APKs.
- **Prior from `old-apk-2026-10-05.md` §5 still holds:** expect the same
  server-side-data architecture (art/audio/dialogue/help/shared tuning in
  the APK; per-entity numbers behind `/reference/*`). Low prior for embedded
  stat tables in ANY of these builds, pre- or post-rebalance.

### 1.6 Negative results diligently recorded

- QooApp download ma
...[truncated 3881 chars]