# Guide/event body retry lane — 2026-10-05

**Lane:** retry the three `blustone.jp` guide/event bodies recorded as empty in
`wayback-announce-2026-10-05.md` §2 (crystal guide, party-formation guide,
Fight Club 2018 World Championship reward detail) via spaced single-shot
Wayback fetches, plus one never-checked guide body surfaced by a fresh guide-
prefix census. Read alongside `wayback-blog-2026-10-05.md` (company page done,
Genovia single-capture confirmed, news/event 2020+ empty, TapTap/Inven
throttled) and `wayback-announce-2026-10-05.md` (two prose-body guides:
training 2019-12-11, rank-up 2019-11-13; three empties as above).

**Budget/method:** max 4 capture-body fetches, single-shot, no retry loops;
503/429 respected (none encountered — all bodies HTTP 200). CDX census queries
are not body fetches and are listed separately below. Bodies read via the
`id_` (original-bytes) variant and tag-stripped locally. No server/APK
changes. No TSV appends: no provenance-clean hero/monster rows exist.

## CDX census (5 queries, all HTTP 200, single-shot)

1. Crystal guide exact URL (`.../育成論/結晶`), `fl=timestamp,original,
   statuscode,digest`, `limit=20` → **1 row**: `20191210184203 ... 200
   FOWRWN7NWP2EASCTHGHG3YZUUM3YCA7I`. Single capture; no alternate body.
2. Party-formation exact URL (`.../育成論/キャラ編成例`), same shape →
   **1 row**: `20191216043116 ... 200 WB2QUP4TJWOQREUNOFYUKLV7FZEDB5A7`.
   Single capture; no alternate body.
3. FC championship detail exact URL (`.../イベント-ファイトクラブ2018
   ワールドチャンピオン-2`), same shape → **1 row**: `20191122162749 ...
   200 ZOKJI5U6VW43SKKE2FJGKTIJCDQP3334`. Single capture; no alternate body.
4. Event prefix (`blustone.jp/イベント*`, `collapse=urlkey`,
   `filter=statuscode:200`, `limit=60`) → **only the FC row above**. No other
   archived event detail exists; no 2020/2021 event page (consistent with
   `wayback-blog-2026-10-05.md` news/event censuses and the EV05
   `R_EPISODE.jet`-only finding).
5. Guide prefix (`blustone.jp/育成論*`, `collapse=urlkey`,
   `filter=statuscode:200`, `limit=60`) → **22 rows**: the 育成論 index
   (2019-03-31), the training guide + 3 attachments, the rank-up guide + 6
   attachments + 4 subpages (`/d`, `/rank1..4`), the crystal guide, the party-
   formation guide, and a **never-body-checked guide**: キャパ超越
   (capacity transcendence, `20190331201909`) + 2 attachments + 1 subpage
   (`/capa2`, 2019-12-16). The `/capa2` subpage and all attachments are
   recorded as URL-level leads only (over budget); the main キャパ超越 body
   is the 4th body fetch below.

## 1. PURE — bodies recovered (archive URL + capture date; numerals masked → §2)

### 1.1 キャパ超越 (capacity transcendence) guide — prose body RECOVERED

- **Archive URL:**
  [2019-03-31 capture](https://web.archive.org/web/20190331201909/https://blustone.jp/%E8%82%B2%E6%88%90%E8%AB%96/%E3%82%AD%E3%83%A3%E3%83%91%E8%B6%85%E8%B6%8A)
  (`.../育成論/キャパ超越`). Raw 28,182 B, stripped text 989 chars:
  nav/title/footer plus a genuine prose how-to block (quoted below).
- **Era:** capture 2019-03-31 is **PRE-rebalance** (before 2019-09-05).
- **Original prose (numeric tokens masked; see §2 N1–N3):**

  > キャパ超越とは？
  > ★[N1]以上の同名キャラをかけ合わせれば、能力値のキャパを超越させて
  > さらに強化することができます。
  > キャパ超越はハンターをランクアップするごとに最大[N2]回まで可能で、
  > その都度基本能力値が上がるので、主力にしているハンターはなるべく
  > たくさん仲間にしましょう。
  > キャパ超越の手順
  > キャパ超越はジムで行おう
  > キャパ超越は、ミッドガルド内にあるジムで行います。
  > キャパ超越したいハンターを選択
  > Hunter Listからキャパ超越したい★[N3]以上のハンターを選び、
  > キャパ超越をタップ。
  > キャパ超越に必要なアイテムを確認
  > キャパ超越に使う同名で★[N1]以上のハンターとメトロン結晶体、
  > メトロンのカケラおよびルピーを確認し、キャパ超越をタップすれば完了です。

- **Translation (mine; numerals masked):** "What is capacity transcendence?
  Combining same-name characters of ★[N1] or higher lets you transcend the
  stat capacity and strengthen further. Per rank-up, transcendence is possible
  up to [N2] times, and base stats rise each time, so recruit as many copies
  as possible of your main hunters. Procedure: do it at the Gym — transcendence
  happens at the Gym inside Midgard. Select the hunter: from the Hunter List
  pick the ★[N3]+ hunter to transcend and tap Transcend. Confirm required
  items: confirm the same-name ★[N1]+ hunter(s), Metron crystals
  (メトロン結晶体), Metron fragments (メトロンのカケラ) and rupees, then tap
  Transcend to finish."
- **Status:** first prose recovery of the transcendence/limit-break loop from
  the fan-wiki lane. It names the facility (Gym in Midgard), the entry UI
  (Hunter List → tap), and the four material classes (same-name hunters,
  intact crystals, fragments, rupees — amounts unstated). No HP/ATK/DEF,
  cost table, or success-rate numbers appear on this page.

### 1.2 Confirmed-empty retries (negative results, preserved)

| # | Page | Archive URL | Result |
|---|---|---|---|
| 1 | 結晶 (crystal) guide | [2019-12-10](https://web.archive.org/web/20191210184203/https://blustone.jp/%E8%82%B2%E6%88%90%E8%AB%96/%E7%B5%90%E6%99%B6) | Raw 25,746 B, stripped 630 chars: title + nav + footer only. **Still empty.** |
| 2 | キャラ編成例 (party formation) | [2019-12-16](https://web.archive.org/web/20191216043116/https://blustone.jp/%E8%82%B2%E6%88%90%E8%AB%96/%E3%82%AD%E3%83%A3%E3%83%A9%E7%B7%A8%E6%88%90%E4%BE%8B) | Raw 26,130 B, stripped 646 chars: title + nav + footer only. **Still empty.** |
| 3 | FC 2018 World Championship reward detail | [2019-11-22](https://web.archive.org/web/20191122162749/https://blustone.jp/%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88-%E3%83%95%E3%82%A1%E3%82%A4%E3%83%88%E3%82%AF%E3%83%A9%E3%83%962018%E3%83%AF%E3%83%BC%E3%83%AB%E3%83%89%E3%83%81%E3%83%A3%E3%83%B3%E3%83%94%E3%82%AA%E3%83%B3-2) | Raw 27,055 B, stripped 645 chars: 2019-03-08 date stamp + nav/footer only. **Still empty; reward table not recovered.** |

All three empties are single-capture pages (CDX queries 1–3), so no alternate
timestamp can supply the missing bodies. The crawler evidently retained only
the WordPress chrome for these URLs (likely image/JS-rendered article content,
per the `wayback-announce-2026-10-05.md` §5 method note).

## 2. UNPURE — all numerals as impure tokens with era tags (NO coverage credit)

Every numeric token from §1.1, quarantined. None is a hero HP/ATK/DEF tuple,
jewel row, or monster stat; none changes any 70% threshold.

- **N1 — same-name material threshold ★3 (PRE):** `★3以上` (twice: intro line
  and materials line).
  [Source](https://web.archive.org/web/20190331201909/https://blustone.jp/%E8%82%B2%E6%88%90%E8%AB%96/%E3%82%AD%E3%83%A3%E3%83%91%E8%B6%85%E8%B6%8A),
  capture 2019-03-31. Rule/economy context: transcendence consumes same-name
  hunters of ★3+. Directionally consistent with Namu prose (self-overcoming
  opens at 3★) and the prior `Short RG47CcM7c20` reading (self-overcoming
  title context), but this page alone does not state duplicate counts,
  per-attempt costs, or stat deltas.
- **N2 — per-rank-up cap 3 times (PRE):** `最大3回` with
  `ランクアップするごとに` (per rank-up) and `その都度基本能力値が上がる`
  (base stats rise each time). Same source/capture. New numeric lead: the cap
  is per rank-up event, not lifetime — adjacent to (not merged with) Bahamut
  `snA=56` prose (each breakthrough ≈ +10% of ATK/DEF/HP; seven total copies;
  breakthrough rank retained on rank-up) and the Namu metron-pair tables.
  Do not arithmetically combine these unattributed sources into a cost curve.
- **N3 — selectable-hunter threshold ★3+ (PRE):** `★3以上のハンターを選び`
  (Hunter List selection step). Same source/capture. Entry-gate context only.
- **Material classes without amounts (PRE, prose only):** メトロン結晶体
  (intact Metron crystals) + メトロンのカケラ (Metron fragments) + ルピー
  (rupees). No quantities, no per-attempt table. Adjacent Namu §4.1 note
  (fragments consumed in self-overcoming in grade/count-varying amounts, no
  table) stays the only quantity-adjacent lead, itself unattributed.
- **Facility/location tokens (PRE, prose):** Gym (ジム) inside Midgard
  (ミッドガルド); entry via Hunter List. Mechanics context for the Gym UI
  lane, not stat evidence.
- **Zero numerals recovered from retries:** the crystal guide, party-formation
  guide, and FC championship detail contributed no numeric token; their
  negative results in §1.2 are the complete record.

## Coverage / throttling / files

- **Strict coverage unchanged:** heroes 1/113, accessories 1/100, monsters
  0/22. This lane recovered rule/economy prose only.
- **Throttling log:** 5 CDX queries + 4 body fetches, all HTTP 200. No
  503/429/timeout encountered; no fetch retried. Budget exhausted exactly
  (4/4 bodies).
- **Leads left (URL-level, unfetched):** `/capa2` subpage (2019-12-16),
  capa/training/rank-up attachments, rank subpages `/d`, `/rank1..4`,
  the 育成論 index body. The `/capa2` subpage is the highest-value next body
  (POST-era transcendence text to diff against this PRE-era page).
- **Files written:** this file (new);
  `polluted-observations.md` appended with the §2 impure tokens. No other
  file modified.
