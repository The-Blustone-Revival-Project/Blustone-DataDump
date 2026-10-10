# Official-post retry lane — `bs.visualshower.com` events, Inven/TapTap/Namu snapshots (2026-10-05)

**Lane:** Wayback CDX/availability retry for `bs.visualshower.com` notices/events
2017–2021, `blustone.jp` news/event pages (EV05 2020/2021), TapTap/Inven article
snapshots, Namu page histories. Extract rebalance numbers, event reward tables,
gacha/attendance rules with archive URLs + capture dates + era tags.
**Era rule** (`stat-version-context.md`): captures before 2019-09-05 are
PRE-rebalance; after are POST-rebalance. Values here are **economy/event
context only — never hero/jewelry/monster coverage**.

Read alongside `wayback-announce-2026-10-05.md` (TapTap rebalance full text,
training/rank-up guides, event-index titles, "board documents uncaptured") and
`wayback-blog-2026-10-05.md` (company-site sweep, empty 2020+ news/event
censuses, throttled TapTap/Inven CDX). This lane **corrects one prior
negative**: `bs.visualshower.com` `event_en` board documents ARE archived with
full bodies — only the character-intro `document_srl` posts remain uncaptured.

## 1. Values recovered (all PRE-rebalance, Oct 2018 official events)

### 1.1 [Event] Lottery Mouse Likes Walnuts! — full reward table

- **Archive:**
  [2018-10-25 capture](http://web.archive.org/web/20181025015633/http://bs.visualshower.com:80/?mid=event_en&document_srl=1003633&l=en)
  of `http://bs.visualshower.com:80/?mid=event_en&document_srl=1003633&l=en`.
  Post by `Natara`, dated **2018.10.12 14:56**, views 483, votes 3.
  Capture date 2018-10-25; post/event period **Oct 12th 15:00 ~ Oct 26th 15:00
  (UTC+9)**. Era: **PRE-rebalance**.
- **How to get walnuts (verbatim):**
  - Clear 5 General Stages → 1 walnut (**dispatching counts**)
  - Clear 1 Hunter Search → 3 walnuts
  - Clear 1 Abyss → 5 walnuts
  - Use 1 scroll to recruit → 6 walnuts (excludes Evaluation Request)
  - Use Manda to recruit → 45 walnuts
- **Event rewards (verbatim):** exchange walnuts for a trace box at **95 or
  125 walnuts**. Each box normally holds **2~4 traces**, "but a lucky person
  might get **40 traces** from one box!"
  - Box with Crocus' Traces (**125**)
  - Box with Apollon's Traces (**95**)
  - Box with Dino's Traces (**95**)
  - Box with Calibur's Traces (**95**)
  - Box with Therapy's Traces (**95**)
- **Precaution (verbatim):** "all items must be exchanged before the end of
  the event period!"
- **Player replies preserved (3):** `RaynerSin` asks why Therapy traces are
  still offered while Heidi traces are gone / whether Heidi ruins come soon;
  `HaunterKing10` asks for Nene traces ("she can be hard to get").
- **Status:** Original October-2018 event economy. Cross-checks (not
  overwrites) for local fixtures: Search-earn 3 walnuts/search vs local
  AIRSHIP_TICKET 1/victory; trace boxes 95/125 currency for 2–4 traces vs
  local `collect_qty` 10/20; "dispatching counts" is an original
  auto/dispatch-credit rule; scroll-vs-Manda recruit earn split (6 vs 45)
  parallels the native single/bundle price scale.

### 1.2 [Event] Jack's Treat! — full Fight Club reward ladder

- **Archive:**
  [2018-10-25 capture](http://web.archive.org/web/20181025175725/http://bs.visualshower.com:80/?mid=event_en&document_srl=1008954&l=en)
  of `http://bs.visualshower.com:80/?mid=event_en&document_srl=1008954&l=en`.
  Post by `Natara`, dated **2018.10.19 15:01**, views 369, votes 2.
  Event period **Oct 19th 15:00 ~ Nov 2nd 15:00 (UTC+9)**. Era:
  **PRE-rebalance**.
- **Participation (verbatim):** enter Fight Club battles to earn points, then
  trade points for materials; plus a Cumulative Victories Reward on total FC
  wins.
- **Point exchange (verbatim):** **5 points per Fight Club use**; **30 points
  → 30 Fuel or 1 Challenge Invitation**.
- **Cumulative Victories Reward (verbatim, one-time each):**
  - 5 wins → 4 Challenge Invitations
  - 10 wins → 1 Elite Request
  - 15 wins → 30 Metron Fragments
  - 20 wins → 120 Fuel
  - 30 wins → 10000 Rupees
  - 40 wins → 1 Metron Crystal
  - 50 wins → 50 Manda
  - 65 wins → 20000 Rupees
  - 80 wins → 3 Metron Crystals
  - 100 wins → 1 Special Request
- **Player reply preserved (1):** `빈신` asks whether finishing loops or
  restarts (unanswered in the capture).
- **Status:** Original FC-event payout ladder. Cross-checks only: 120 Fuel /
  10000+20000 Rupees / 50 Manda / Metron crystals+fragments / Elite+Special
  request tickets vs local FC settlement fixtures (honor 10, rating ±10);
  Challenge Invitation is an original FC consumable; Elite/Special Request
  match the Namu request-ticket taxonomy (고급/특급).

### 1.3 Board index — Sept–Oct 2018 event calendar (titles/dates/views)

Both captures embed the `event_en` article list (page 1 of 23), giving a
dated official event calendar beyond the two bodies read:

- Sticky: [Event] Halloween in Midgard! [7] — Natara, 2018.10.19, 3251/3669
  views (two captures disagree on the counter)
- Sticky: [Event] Jack's Treat! [1] — Natara, 2018.10.19
- Sticky: [Event] Lottery Mouse Likes Walnuts! [3] — Natara, 2018.10.12
- Sticky: [Event] October Package [3] — Natara, 2018.09.28, 6176/6219 views
- Sticky: [Notice] How to Use the Events Section [9] — VSpang, 2017.07.05
- #440 [Event] Which Witch? Riko? [0] — PTS-Vincent, 2018.10.19
- #439/#436/#432/#426 Lottery Mouse's Amazing Gifts [0]/[0]/[1]/[0] — Natara,
  2018.10.15/10.08/10.01/09.17 (recurring gift series)
- #438 [Event] Westfield's Boxing Gloves [0] — Natara, 2018.10.12
- #437/#433/#430 Clara's Surprise Weekend Gift [0]/[0]/[2] — Natara,
  2018.10.12/10.05/09.28 (recurring series)
- #435 [Event] Find Shiny Gemstones! [7] — Natara, 2018.10.05
- #434 [Event] Schumann's Marvelous Lootbox [0] — Natara, 2018.10.05
- #431 [Event] October Limited Recruiting Hot Time! [7] — Natara, 2018.09.28
- #429 [Event] The More the Better by Lottery Mouse! [3] — Natara, 2018.09.28
- #428 [Event] Estelle's Special Offer [1] — Natara, 2018.09.21
- #427 [Event] Midgard Fall Festival Event! [12] — Natara, 2018.09.20, 10348
  views (highest in the visible window)
- #425 [Event] Tyltyl's What's in the Box? [3] — Natara, 2018.09.17
- Board pagination: **/ 23 pages** — the visible window is a fraction of the
  archived board. Future lanes can mine further `document_srl` bodies from
  this index without new CDX discovery.
- **Status:** Calendar/existence leads only. No reward numbers beyond §§1.1–1.2.

## 2. Captures checked with NO new values (negative results preserved)

| Target | Check | Result |
|---|---|---|
| Namu-linked char-intro posts 707457 (Heidi), 426682 (Lily&Lala), 1082853 (Chichi), 912433 (Kalbaram) | Availability API 2026-10-05: `archived_snapshots: {}` for 707457 (this lane); prior lane CDX `[]` for all four | **No archived copy. Remains unresolved.** Consistent with `striker-videos-2026-10-05.md` §Official retry. |
| `bs.visualshower.com` filtered CDX (`mid=notice`, `filter=original:.*mid.*notice.*`) | CDX HTTP 503 | Throttled; recorded, no bypass, no retry loop. Exact-URL CDX works (see §3 method note); the failure is query-shape-specific, not proof of absence. |
| `blustone.jp` news/event 2020+ (EV05 2020/2021 web schedule) | Availability: `/news` closest = 2019-12-08 capture; `/event` = `{}`; prior lane 2020+ CDX censuses empty | **No 2020/2021 event pages in the archive.** EV05 schedule evidence remains the exported `R_EPISODE.jet` (AGENTS §91), not the web. |
| `blustone.jp/news` 2019-12-08 body | Text fetch: Mar 2019 guide/video titles only (Metron-crystal guide, helper guide, Dino guide, 4-koma, gameplay videos) | Guide-index context; **no reward tables, no 2020 content**. |
| `blustone.jp/hunter` index bodies (2019-03-31/10-15/12-09) | Text fetch 2019-10-15: nav/index only, JS-rendered list | No values; profile rows already harvested in `archived-hunter-database-2019.tsv` (62 rows). |
| Inven launch `news=177783` snapshot | Availability API = `{}` (false negative — see §3); CDX exact-URL = **4 captures**: 2017-10-10, 2017-12-16, 2022-12-05, 2024-04-20, all 200 | Captures exist; body not re-fetched (live page already logged in README/coverage). No new numbers this lane. |
| Inven interview `news=212307` snapshot | Availability API = `{}` (same false negative); CDX exact-URL = **1 capture**: 2019-10-17, 200 | Capture exists; body not fetched (article already logged; embedded video previously throttled). |
| TapTap post 73656 snapshot | Availability = `{}`; CDX exact-URL = **timeout ×2** (this lane; +1 prior lane) | **No snapshot verified.** Live transcription in `stat-version-context.md` / `wayback-announce-2026-10-05.md` §1.1 stands. |
| Namu page histories (`namu.wiki/w/블루스톤/헌터`) | Availability = `{}`; direct fetch 403 known; prior CDX = 403-only rows | **No page history mined.** |
| HungryApp `pid=85749` snapshot | Prior CDX: no captures | Not re-queried (broad-CDX timeout risk); live page already screened. |
| Gacha prices / attendance calendars on official board | Not found on any checked page | **Not recovered in this pass.** Gacha 30/300 rule stays Namu-text + native-constant evidence. |

## 3. Method notes (for the next retry lane)

- **Availability API false-negatives on query-string URLs:** it returned `{}` for
  both Inven `news=` URLs that CDX then proved captured (4 + 1 rows). Never
  treat availability-`{}` as no-capture for `?`-URLs; always confirm with an
  exact-URL CDX query.
- **Exact-URL CDX beats filtered/wildcard CDX under throttling:** broad
  `blustone.jp*` / `inven.../news*` / `taptap.io/post/73656` queries timed out
  or 503'd, while exact-URL queries (`inven...?news=177783`,
  `blustone.jp/hunter` + `from/to`) returned rows. Prefer exact URLs; keep
  bulk sweeps small (`limit≤100`, `collapse=urlkey`).
- **XE-board capture bodies render fully as text:** both `event_en` bodies
  carried complete post text plus the article-list sidebar — the sidebar is
  itself a dated event calendar (§1.3). One body fetch ≈ one reward table +
  ~15 calendar entries.
- **Throttle log:** TapTap CDX timeout ×2, Inven CDX 503 ×1 (prior lane),
  `mid=notice` filtered CDX 503 ×1, broad-domain CDX timeouts ×4. No query
  retried after failure except TapTap exact-URL (1 spaced retry, failed
  again — left alone). No bypass attempted. Total CDX calls this lane: ~12.
  Total capture-body fetches: 4 (2 event bodies + news/hunter index).

## 4. Coverage disposition / files updated

- **New base-stat tuples: 0.** Hero coverage stays 1/113; accessories 1/100;
  monsters 0/22. Both recovered tables are event *economy* (earn rates,
  point exchanges, victory ladders), not HP/ATK/DEF.
- **New polluted-ledger rows:** none — event currency/trace-box/fuel/rupee/
  Manda/request-ticket values are economy context, not hero readings. The
  ledger gets a pointer subsection only (no numeric duplication).
- **Files updated:** this lane log (new); `polluted-observations.md` (pointer
  subsection). `coverage.md`, TSVs, server/APK untouched.
- No server/APK/state changes.
