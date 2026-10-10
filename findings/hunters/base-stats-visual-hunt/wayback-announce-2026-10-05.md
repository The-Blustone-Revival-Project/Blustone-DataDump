# Wayback announcement/guide mining — 2026-10-05

**Goal:** Mine Wayback for BLUSTONE announcements, guides, and CDN history.
Extract equipment/crystal rebalance numbers, event reward tables, gacha rates,
login/supply calendars, skill/hero intro stats. Tag every value pre/post
2019-09-05. Preserve archive URLs + capture dates + raw text.

**Era rule** (per `stat-version-context.md`): captures dated before 2019-09-05
are PRE-rebalance; captures after are POST-rebalance (values reflect the new
balance unless the page is stale). Values here are **rebalance/reward context
only** — they never count toward hero/jewelry/monster coverage.

**Key framing correction:** `blustone.jp` is a Japanese **fan walkthrough site**
(ブルーストーン公式攻略サイト = "official walkthrough site" in the fan-site
sense), not VisualShower's server. Its guides give real game-rule numbers but
no CDN/package strings. The actual official board, `bs.visualshower.com` (XE
board), is dead and barely archived.

## 1. Values recovered (era-tagged)

### 1.1 Equipment/crystal rebalance — POST-2019-09-05 (effective), full text

- **Source (live page, same content as archived post):**
  [TapTap post 73656](https://www.taptap.io/post/73656), `[公告] 結晶、裝備相關變更事項預告`,
  posted **2019-09-04** by `SmileV`, effective **after 2019-09-05**. Traditional
  Chinese. Raw key sentences preserved below; translation is mine.
- **Equipment (POST):**
  - Equipment stat values **+50% on the existing base** (裝備能力值將在原有能力值的基礎上上調50%).
  - **Fractional/decimal-point stat increments removed** (no more sub-1-point rises).
  - **After equipment-modification stage 2 (equipment level 20+), upgrades gain
    much larger increases** (2階段之後/裝備20級之後大幅上升).
- **Crystals/jewels (POST):**
  - Buffed: ATK, DEF, HP, elemental enhancement, elemental resistance,
    penetration. Small buff: crit chance, crit damage, block chance,
    block-damage reduction.
  - Main-stat option frequency rebalanced (fixes repeated options after the
    main stat is fixed; more distinct options visible).
  - Main stats: **★1–★3 +30%**, **★4–★5 +50%** (研磨/polish growth raised).
  - **All substats +50%**; substat upgrade amounts **fixed at the maximum**
    (previously random within a range).
  - **All set bonuses raised** to match — **no exact amounts given**.
- **Gating note:** the post says players must update to the latest version or
  the changes may not apply — a version-sensitive rollout, consistent with
  treating dated screenshots as era-specific.
- **Status:** Extends (does not contradict) `stat-version-context.md`. New
  details vs that file: the Traditional-Chinese original wording, the
  fractional-removal rule, the equip-Lv20 stage-2 breakpoint, the per-stat
  buff list (penetration in the large-buff group; crit/block in the small-buff
  group), the main-stat frequency fix, and the fixed-at-max substat rule.

### 1.2 Training rules — POST-2019-09-05

- **Source:**
  [トレーニング capture 2019-12-11](https://web.archive.org/web/20191211104454/https://blustone.jp/%E8%82%B2%E6%88%90%E8%AB%96/%E3%83%88%E3%83%AC%E3%83%BC%E3%83%8B%E3%83%B3%E3%82%B0)
  (1 capture only).
- **Rules:** Training is done at the Gym; up to **5 partner hunters consumed per
  session** (1回で最大5人); **★1–★2 partners recommended** as fodder; max-level
  hunters proceed to rank-up.
- **Status:** Rule context only. Consistent with the local 5-partner cap; the
  ★1–★2 fodder recommendation matches the recovered source-hunter whitelist
  direction. No costs/XP numbers on this page.

### 1.3 Rank-up rules — POST-2019-09-05

- **Source:**
  [ランクアップ capture 2019-11-13](https://web.archive.org/web/20191113131941/https://blustone.jp/%E8%82%B2%E6%88%90%E8%AB%96/%E3%83%A9%E3%83%B3%E3%82%AF%E3%82%A2%E3%83%83%E3%83%97)
  (4 captures 2019-03-31–2019-11-13; body read from the Nov capture).
- **Rules:**
  - Rank-up possible up to **★5** for every hunter; ★1-drawn hunters can be
    raised a long way.
  - Material rule: **same-star-count partners of the same ★ rank** —
    e.g. ★3→★4 needs **three ★3 partners**. (Matches the local "source count
    equals current rank" community rule.)
  - On rank-up, **level resets to 1**, max level and ★ rise, a **new skill is
    learned**, and **★4+ unlocks equipment**.
  - **Batch rank-up**: ★1–★2 hunters can rank up via the batch function
    **without reaching max level**.
  - Economy: releasing a ★3 hunter yields **8 Chu-coins (チュウコイン)**,
    which buys **two ★3 trainers** at the Secret Market — cheaper than
    consuming the ★3 directly. Recommends feeding rank-up-made ★3s instead of
    natural ★3s.
- **Status:** Rule/economy context only. The ★3→8-coins→2-trainers rate and the
  ★4-equipment-unlock rule are new numeric leads; original-server proof and
  version stability are unestablished.

### 1.4 Launch context — PRE-2019-09-05 (2017-05-15)

- **Source:** [Inven launch article](https://www.inven.co.kr/webzine/news/?news=177783),
  `news=177783`, dated **2017-05-15** (live page read; Wayback has
  2017-10-10, 2017-12-16, 2022-12-05, 2024-04-20 captures).
- **Facts:** Singapore **soft launch April 2017**; hybrid tap×RPG genre claim;
  producer Kim Jong-guk (김종국) quote on speed/impact action; **White Island
  (하얀섬) collaboration**: all White Island Season 2 season-pass buyers receive
  heroine **Min Hae-sun (민해선)** as a playable Blustone hunter.
- **Status:** Version-history anchor only (earliest dated Korean press record
  found in this pass). No stats, rates, or rewards with numbers.

### 1.5 Event index — PRE-2019-09-05 (Feb–Mar 2019 posts)

- **Source:**
  [Event category capture 2019-12-09](https://web.archive.org/web/20191209131405/https://blustone.jp/category/event)
  (2 captures: 2019-10-15, 2019-12-09).
- **Event titles + post dates (no bodies):** Jack's treat (2019-03-08); Fight
  Club 2018 World Championship rewards & SNS share event (2019-03-08); NEW ★4
  hunter Elise capture (2019-03-01); March-limited package (2019-03-01);
  red-panda bamboo-leaf airlift (2019-03-01); new ancient-costume boutique
  festival (2019-02-15); Audrey's pub repair project (2019-02-15); Clara's
  exciting weekend (2019-02-15); Valentine chocolate war (2019-02-13); 2019
  Midgard hunting sports festival (2019-02-12); Slow's special service
  (2019-02-12); Estelle's special proposal (2019-02-08); Chusen likes walnuts
  (2019-02-08); mirage weekend hot-time (2019-02-08); most-popular-hunter
  results (2019-02-08).
- **Status:** Event-existence/calendar leads only. Detail-page bodies are
  empty in the archive (see §2), so **no reward tables or rates recovered**.

### 1.6 Facility/guide index — PRE-2019-09-05 (2019-03-31 top page)

- **Source:**
  [Top-page capture 2019-03-31](https://web.archive.org/web/20190331231146/https://blustone.jp/)
  (5 captures 2019-03-31–2019-12-09).
- **Facilities named:** Boutique, Detective Agency, Gym, Market, Excavation
  Association (発掘協会), Fight Club, Crystal Mining, Equipment Enhancement,
  Hunter Guild. Training-priority links: ★5 rearing, キャパ超越
  (capacity transcendence), Training, Rank-up. Currency/material guides linked:
  Manda, fuel, rupee, equipment-enhancement materials, skill-training
  materials, Metron crystal collection.
- **Status:** System inventory only; no numbers. Confirms the guide pages
  worth future capture checks.

## 2. Captures checked with NO usable numbers (negative results preserved)

| Target | Archive URL / check | Result |
|---|---|---|
| `blustone.jp` 結晶 (crystal) guide | [2019-12-10](https://web.archive.org/web/20191210184203/https://blustone.jp/%E8%82%B2%E6%88%90%E8%AB%96/%E7%B5%90%E6%99%B6) | Title only; body empty. No values. |
| `blustone.jp` キャラ編成例 (party formation) | [2019-12-16](https://web.archive.org/web/20191216043116/https://blustone.jp/%E8%82%B2%E6%88%90%E8%AB%96/%E3%82%AD%E3%83%A3%E3%83%A9%E7%B7%A8%E6%88%90%E4%BE%8B) | Title only; body empty. No values. |
| Fight Club 2018 World Championship reward event detail | [2019-11-22](https://web.archive.org/web/20191122162749/https://blustone.jp/%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88-%E3%83%95%E3%82%A1%E3%82%A4%E3%83%88%E3%82%AF%E3%83%A9%E3%83%962018%E3%83%AF%E3%83%BC%E3%83%AB%E3%83%89%E3%83%81%E3%83%A3%E3%83%B3%E3%83%94%E3%82%AA%E3%83%B3-2) | Date stamp only (2019-03-08); body empty. **Reward table not recovered.** |
| `blustone.jp/category/event` 2020/2021 listings (EV05 schedule) | CDX: only 2019-10-15 + 2019-12-09 captures exist | **No 2020/2021 event pages in the archive.** EV05 schedule evidence remains the exported `R_EPISODE.jet` (per AGENTS §91), not the web. |
| `bs.visualshower.com` board/notices | CDX domain sweep: only XE file-download URLs + 2017 root 302 captured | Board documents uncaptured. Namu-linked doc IDs 707457 (Heidi), 426682 (Lily & Lala), 912433 (Kalbaram) have **no captures**. Official posts remain inaccessible (consistent with README §39 note). |
| Namu hero-page history | CDX: `namu.wiki/w/블루스톤*` returns 403-only rows | Archive blocked; **no page history mined**. |
| HungryApp review | CDX: no captures of `pid=85749` | No archive; live page already screened (README). |
| `blustone.jp` マンダ (Manda) guide | CDX: no captures | Unarchived. |
| Gacha rates / login-supply calendars | Not found on any checked page | **Not recovered in this pass.** |

## 3. CDN / package-version strings (server-replica side note)

- **No CDN URLs, reslist stamps, or package manifests found on any checked web
  page.** The fan wiki never carried client transport data.
- **Client version strings collated from existing store-listing evidence**
  (already in README/coverage; repeated here as the version spine for future
  CDN archaeology): `1.1.9.4` (PDALIFE), `1.4.4.1` (VSFan APK), `2.0.5.1`
  (BrowserCam, 2018-08-22), `2.1.7.3` (QooApp), `2.5.7.0` (Stahuj),
  `2.7.9.2` (ProDroid), `2.8.0.1` (TapTap/Aptoide/Uptodown, 2022-07-14/15).
- **Future lead (not pursued):** APKPure/APKCombo/TapTap version histories may
  host dated APKs whose `reslist`/CDN defaults predate the replica's
  1634661+ stamps. No APK was downloaded in this pass.

## 4. Files updated

- This file (new).
- `polluted-observations.md`: appended §"Announcement/guide numeric context
  (rebalance/reward leads, no coverage credit)" summarizing §§1.1–1.3 + event
  negative result.

## 5. Method note

CDX queries via `web.archive.org/cdx/search/cdx` (http for bulk, https for
filtered); page reads via `web.archive.org/web/<timestamp>/<url>` with text
format. `blustone.jp` article bodies are frequently empty in the archive
(title/nav/footer only) — likely image- or JS-rendered content the crawler did
not retain. Prefer guide pages with prose bodies (トレーニング,
ランクアップ) and treat title-only captures as negative evidence, not absent
pages.
