# namu `블루스톤/아이템` — original economy tables (16 tables, browser-rendered)

**Written:** 2026-10-08. **Source:** `https://namu.wiki/w/블루스톤/아이템`, rendered in
a browser, last modified **2026-08-27 03:29:25**. 18,011 chars, **16 `<table>`
elements**. Plain HTTP 403s; a browser is required.

Companion to `namu-first-party-mechanics-2026-10-08.md` (the prose/mechanics
pass). **Options with evidence, not instructions. Nothing applied.** Coverage
counters unmoved: heroes **1/113**, accessories **1/100**, monsters **0/22**.

---

## 1. Arena ranking reward ladder — COMPLETE, 28 rows

`순위 → 파이트칩` (rank → fight chips). This is a real, closed curve; the replica
carries `honor 10 / rating ±10 / six wins per league` as fixtures.

| rank | chips | rank | chips | rank | chips | rank | chips |
|---|---:|---|---:|---|---:|---|---:|
| 1 | **2500** | 131–180 | 1500 | 2121–2750 | 600 | 30000+ | 100 |
| 2 | 2400 | 181–240 | 1400 | 2751–3600 | 550 | | |
| 3 | 2300 | 241–320 | 1300 | 3601–4700 | 500 | | |
| 4–10 | 2200 | 321–420 | 1200 | 4701–6100 | 450 | | |
| 11–20 | 2100 | 421–550 | 1100 | 6101–8000 | 400 | | |
| 21–30 | 2000 | 551–720 | 1000 | 8001–10300 | 350 | | |
| 31–50 | 1900 | 721–950 | 900 | 10301–13500 | 300 | | |
| 51–70 | 1800 | 951–1250 | 800 | 13501–17500 | 250 | | |
| 71–100 | 1700 | 1251–1620 | 700 | 17501–23000 | 200 | | |
| 101–130 | 1600 | 1621–2120 | **650** | 23001–30000 | 150 | | |

Two step regimes: **−100** per band down to rank 100, then −50 to rank 1250, then
−50 again. The single **650** at 1621–2120 breaks the otherwise clean −50 ramp
(it sits between 700 and 600 where 650 is the arithmetic midpoint) — so it is
consistent, not an error.

**Arena tier rewards** (`달성 티어 → 파이트 칩`), 6 rows, **3 of them blank**:

| tier | chips |
|---|---:|
| 브론즈 Bronze | *(absent — footnote: you start at Bronze, so it can never be "achieved")* |
| 실버 Silver | **100** |
| 골드 Gold | *(blank)* |
| 에메랄드 Emerald | **150** |
| 메트론 Metron | *(blank)* |
| 만다 Mandaring | **200** |

The blanks are editorial gaps, **not** zero rewards. Do not publish 0 for them.

## 2. Hunter Search capsule costs — machine-readable, confirms §1 C4

| 헌터 등급 | 1성 | 2성 | 3성 |
|---|---:|---:|---:|
| 헬륨 소비량 (per entry) | **2** | **8** | **15** |
| 수색 가능 횟수 (entries) | **5** | **4** | **2** |
| **total** | **10** | **32** | **30** |

## 3. Enhancement (강화) material cost by level band — the Raise cost table

Four material families, each with **three grades**:

| Korean | romanisation | grades |
|---|---|---|
| 금속 조각 | metal scraps | 녹슨 rusty / 예리한 sharp / 신기한 wondrous |
| 등껍질 | shell | 부서진 broken / 멀쩡한 intact / 무적의 immutable |
| 화염석 | flame stone | 차가운 cold / 뜨거운 hot / 이글거리는 blazing |
| 약초 | herb | 시든 wilted / 싱싱한 fresh / 열매 맺은 fruiting |

Level bands `1~4 … 45~` with the grade-trio `low/mid/high`:

| band | 1~4 | 5~9 | 10~14 | 15~19 | 20~24 | 25~29 | 30~34 | 35~39 | 40~44 | 45~ |
|---|---|---|---|---|---|---|---|---|---|---|
| trio | 0/0/0 | 1/0/0 | 2/0/0 | 3/0/0 | 4/1/0 | 5/2/0 | 0/3/1 | 0/4/2 | 0/5/3 | 0/0/4 |

**Levels 1–4 cost NO material at all** — the first four Raise steps are free of
materials. The curve then shifts one grade up roughly every 10 levels.

> ### ⚠ HONESTY FLAG — the four tables are byte-identical
> 금속 조각, 등껍질, 화염석 and 약초 carry **exactly the same digits in the same
> order**. Two readings, and this research does **not** pick one:
> - **Genuine symmetry** — the game charges all four materials identically.
> - **Editorial duplication** — one table copy-pasted four times, which is a
>   pattern already proven in this project's corpora (12 duplicated archive core
> triples, 3 pairs identical across all 12 fields; and namu's own equipment
> tables render empty).
> **A single source page cannot distinguish these.** If it matters, it needs a
> second source. Treat "four materials cost the same" as **UNVERIFIED**.

## 4. Equipment upgrade (Forge) by level — PARTIAL, do not over-read

Rows: `도구 상자` (tool box) · `고급 도구 상자` (premium box) ·
`속성별 장비 개조 재료` (per-element mod materials: **번개 막대** lightning rod /
**냉각수** coolant / **인화성 물질** flammable substance) ·
`비용(루피) [할인여부]` (gold cost, with a guild-discount flag).

Populated cells only:

| level band | 도구 상자 | 비용(루피) |
|---|---|---|
| 1–10 | 0, 2, 4, 8, 12, 0 | 500, 1000, 5000 |
| 11–20 | *(blank)* | 1500 (at lv11) |
| 21–30 | blank | blank |
| 31–40 | blank | blank |
| 41–50 | blank | blank |

**Cell alignment is ambiguous** — with 10 header columns and 6 filled values it is
not determinable which level each number belongs to. Report the *existence* of
gold costs (500 / 1000 / 5000 / 1500) and the level-50 cap, **not** a per-level
schedule. Only lv1–11 is filled; lv12–50 are editorial blanks.

Note: the header switches from `개조 재료` (modification) at lv1–20 to
`강화 재료` (enhancement) at lv21–50 — **two distinct upgrade tiers**, mirroring
the project's own naive-vs-Lv20+ growth split.

## 5. Market shop corner prices

| shop | gold price | fight-chip price |
|---|---:|---:|
| 루피 코너 (Rupee corner) | **20000** | — |
| 파이트칩 코너 (Fight-chip corner) | **500** | **1500** |
| 신기루 코너 (Mirage corner) | **1000** | **3000** |
| 비밀 코너 (Secret corner) | **5** | **20** |

The main page adds that the gold and fight-chip corners **rotate their listings
on a timer**. A **5-gold** secret corner exists, which is far below every other
price here — worth a sanity check against any shop fixture.

## 6. Fishing — the honest ceiling on this source

**Section `6.3 낚시` prose:** fishing exists mainly to earn **루피**; non-fish
items drop too, "대표적으로 **메트론 결정체**이며 얻을 확률이 극악이다" (Metron
crystals, extremely rare).

**Critical mechanic change, first-party:**
> "예전에는 물고기를 얻고 보관했다가 플레이어가 원할 때 판매할 수 있었지만 언제부터인지
> **물고기를 낚자마자 바로 판매가 된다**."

Fish used to be **caught and stored, then sold on demand**; at some point they
became **sold immediately on capture**. That is a real content/UX change and it
matters for any inventory design — the project's fishing model keeps catch
inventory.

**Tables 14 and 15 — the fish lists — are EMPTY** (single `a.aa` header, no rows).
Same editorial gap as the community wikis. A namu site search for a fishing page
returns **0 results**, and the search UI itself works (so this is a real zero, not
the unindexed-search trap that affects Miraheze).

**Therefore: namu yields fish NAMES and an ORDER, but no `fish_id`, no prices, and
no grades.** For the project's open `ParsePrice` contract — which wants
`fish_id/b_price/s_price/g_price` — **namu cannot supply the ids.** It does supply
the six names from the main page and, usefully, that fish are auto-sold. See
`namu-first-party-mechanics-2026-10-08.md` §3.4 for the names and ordering.

## 7. Also recovered from this page

- **Traces are organised by grade** — document sections `5.1 1★ / 5.2 2★ / 5.3 3★ / 5.4 4★`.
  This matches the Mirage shop selling specifically **3성 헌터 흔적**, and the
  recruitment text "등급에 따라 다른 일정 개수". So **trace exchange is
  grade-gated**, which is the axis `trace-rarity-vote-2026-10-05.md` found
  non-commensurable with the vsfan `Value` column. **A grade axis exists and is
  separate from the worth axis** — the two should not be merged.
- Trace flavour text is per-hunter and sometimes encodes lore: **곰의 흔적** is
  "a torn trace left by a bear that was clearly eating something… **it looks like
  a Metron sweetfish (메트론 은어)**". That is an independent in-fiction
  confirmation of the Metron sweetfish as a real, named catchable.
- **2019/06/14 patch** changed some item designs — an era marker to add.
- **Boutique tickets**: some cosmetics are obtainable *only* with a
  **부티크 티켓**, others only with manda; the Mirage corner sells boutique
  tickets at a high price (author guesses "around 6000(?)" — explicitly hedged,
  do not treat as data).
- Footnote [8] ties **특기 강화, 자기극복** together; the earlier pass already
  placed 자기극복 at 3★.

## 8. Method, provenance, limits

**Read:** one page, rendered, `document.body.innerText` for prose and direct DOM
`table.rows` walking for tables — `innerText` alone **collapses the fish tables
and reorders footnotes**, so a text-only pass would have missed §1–§5 entirely.

**Not read:** sub-pages of this document; the `5. 헌터 흔적` trace lists beyond
their headings; the equipment catalogue itself. **No screenshots were used** —
every number above is read from DOM cell text, which is stronger than OCR here.

**Provenance per table:** `tables[i]` index, page last-modified **2026-08-27
03:29:25**, URL above. Save the extracted JSON alongside if you need to re-verify.

**Era:** modified 2026-08-27, so post-2019-09-05 rebalance and post-2019/06/14.
Where these disagree with 2019 corpora, that is the likely reason.

**Not claimed:** no per-level Raise/Forge schedule (§4 is ambiguous), no
per-material differentiation (§3), no fish ids or prices (§6), no tier rewards
for the three blank tiers (§1).
