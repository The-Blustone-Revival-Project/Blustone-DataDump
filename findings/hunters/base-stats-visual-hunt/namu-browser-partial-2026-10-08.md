# PARTIAL — namu.wiki is reachable in a real browser, and the leads it reveals

**Written:** 2026-10-08. **Status: INCOMPLETE — do not treat as a finished result.**

A previous lane recorded that `namu.wiki` returns **HTTP 403** to plain HTTP and
that even the mirrors (`d.namu.moe`, `dark.namu.moe`, `m.namu.moe`, `seore.org`)
return only a client-rendered shell (~110 KB, no article text). A parent then
opened `namu.wiki` in an actual browser and the page **rendered fully**. So the
gate is real and the blocker was the instrument, not the content.

This file records what was extracted before the browser tooling became
unavailable. **The sub-pages were not visited.**

---

## 1. What was extracted

`https://namu.wiki/w/%EB%B8%94%EB%A3%A8%EC%8A%A4%ED%86%A4` — title
`블루스톤 - 나무위키`:

| property | value |
|---|---|
| rendered text | **23,818 chars** (the mirror-only shell exposed none of it) |
| links | **290** |
| images | **49** |
| `<table>` elements | **4** |
| `readyState` | `complete` |
| last modified | **2026-10-01 19:22:12** |

Extraction method: render, then read `document.body.innerText` and the DOM via
script evaluation in the page. Plain HTTP and mirror fetches cannot do this,
because namu builds the article client-side.

## 2. Why this matters — three specific, actionable leads

### 2.1 The page is **actively maintained**, so it carries POST-rebalance data

Last modified **2026-10-01**, i.e. ~7 years after the **2019-09-05** rebalance.
Every other numeric corpus in this project is a 2017-2019 capture and must be
era-tagged. This one is *current*. Where it disagrees with the 2019 sources, the
disagreement is itself the finding.

### 2.2 It has an explicit **구 버전 / 현재** (old version / current) split

The table of contents carries, under `3.2 스테이지`:

```
3.2.1. 구 버전      <- old version
3.2.2. 현재         <- current
```

**This is a direct lever on an unresolved contradiction in this project.** The
2017-05-22 source `23265` says *"Max level before advance is 20"*, which
contradicts the Lv.30 cap used everywhere else; a previous lane refuted the
proposed "a 2017 patch changed it" resolution by showing the wiki's transcribed
patch notes **never mention a hunter level cap**. A page that deliberately
separates 구 버전 from 현재 is exactly where a changed cap would be recorded.
**Go here first.**

### 2.3 An `아이템` (items) section exists, with 4 tables

The TOC has `5. 아이템`. Accessory coverage is **1/100** and every other avenue
is now exhausted — Miraheze swept exhaustively (1,567 revisions, 0 values),
namu per-role gear pages via mirrors (165 slots, 0 values), vsfan English and
`/sc/` corpora read, `share_en` closed by viewing all 28 images, 9,873 shipped
PNGs yield no calibratable icon. **A Korean-language items section with actual
tables has not been read.** The recurring editorial pattern (skills transcribed,
equipment left blank) may or may not hold here.

## 3. One genuine cross-title identity confirmation

The article states the game shares a worldview with **비욘드 더 바운즈**
(*Beyond the Bounds*, "BTB"), released by the same developer, and that **BTB's
protagonists 랜턴 (Lantern) and 네네 (Nene) appear in this game as hunters.**

That is independent Korean-language corroboration for two hero identities:

- **Lantern → `001`**
- **Nene → `003`**

Both already carry multiple shipped attestations (the `JOB_*` role tags, the
`CHAR_STR` description prose, and the 2019 JP archive), so this **adds a source
rather than resolving anything** — and it is an *identity* corroboration, not a
stat one. It does confirm the `001`/`003` mapping independently of the JP corpus,
which is worth having given how much weight those two rows carry.

Also noted on the page: the game released **2017-05-13**, developer and publisher
both **비주얼샤워 (VisualShower)**, platforms Android/iOS, rating 3세 이용가.

## 4. What was NOT done — the honest limits

- **Only the main article was read.** Its **290 links were not followed.** The
  hunter pages, the per-role equipment pages (공격수 / 수비수 / 폭격수 / 도우미),
  and the `아이템` sub-pages are all still unread.
- **No numbers were extracted.** The 4 `<table>` elements on this page were not
  parsed; the article is an overview, so they are likely infobox/category rows.
- **No stat line, and no coverage change.** Heroes **1/113**, accessories
  **1/100**, monsters **0/22** — all unmoved. A T2 transcendence panel was **not**
  found.
- The 49 images were not downloaded or examined.
- namu may gate deeper pages behind login; that was not tested.

## 5. How to finish it

A browser-capable agent should, in order:

1. Re-open `https://namu.wiki/w/블루스톤` and read **3.2.1 구 버전** and
   **3.2.2 현재** for the level cap (lead 2.2).
2. Open `5. 아이템` and its sub-pages; parse every `<table>` for item stat lines
   (lead 2.3). Crosswalk Korean item names against
   `charstr-items-2026-10-06.tsv` — that file localises **accessories only**
   (column index 3, `accessory_en`), so weapon/armour names cannot be
   crosswalked in Korean and identity must come from elsewhere.
3. Follow the per-role equipment pages and look for a stat column the mirrors did
   not render.
4. Search the whole namespace for `초월` (transcendence) — a **T2** panel remains
   the single highest-value missing measurement, because it decides whether the
   rungs scale from base (`T2 = ×1.20`) or compound (`T2 = ×1.2087`). See
   `t1-measured-1.0994-2026-10-08.md`.
5. Record the **edit date** of every page used, since this wiki is live and
   post-rebalance.

**Method requirements:** render before reading (never fetch raw HTML and expect
article text); note that mirrors expose only a shell, so `namu.wiki` itself in a
browser is the working path; run a positive control — confirm a known page
renders — before recording any zero; and take no screenshot as evidence without
zooming on the digits, per the `Lv. 1` / `Lv. 17` misread already recorded.

**Provenance required per reading:** URL, page last-modified date, and a hash of
the extracted text.
