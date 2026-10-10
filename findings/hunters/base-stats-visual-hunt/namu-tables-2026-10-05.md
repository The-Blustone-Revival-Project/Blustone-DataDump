# Namu mirror exact table transcriptions (2026-10-05)

**Sources:** `https://d.namu.moe/w/블루스톤/헌터` (mirror HTTP 200, fetched
2026-10-05; page last-modified 2026-08-13, content spans 2017–2021) and
`https://d.namu.moe/w/블루스톤` (mirror HTTP 200, same day).
**Method:** raw-HTML table-cell extraction (not the lossy text rendering that
collapsed the grid in the first pass). Rows are transcribed cell-by-cell;
rowspan-merged cells are noted, not invented.

**Era:** ERA-UNRESOLVED for every table below. The wiki text is undated except:
equipment enhancement "added 6/22" (year unstated), stim@s change ~2019-04
(pre-rebalance), rollback narrative 2021-09 (post). **Do not normalize any
value against the 2019-09-05 rebalance.** No HP/ATK/DEF base tuple here; this
file is economy/progression context for rebalance estimates only.

**Status:** No coverage-count change (heroes 1/113, accessories 1/100,
monsters 0/22). No server/APK change.

---

## 1. Equipment enhancement grid, levels 1–50 (헌터 page §1.5)

Prose rules (same page): enhancement added 6/22 (year unstated); unlocks at
4★; per hunter 3 equipment pieces; levels 1–2 cost rupees only; from level 3
toolboxes required (`도구 상자/고급 도구상자` normal/advanced pair); remodel
(개조) every 10 levels needs the hunter's element material (전격 번개 막대 /
냉기 냉각수 / 화염 인화성 물질); remodel re-trims the frame
(동, 은, … order); guild discount (협회 보너스, single-digit %) applies except
on remodel.

Table structure: 5 blocks of 10 levels. Body rows carry
[level | element-material qty (one merged column — only one element applies
per hunter) | toolbox normal/advanced | rupees]. Each block's boundary row
carries the element-material count + large rupee cost + `0/0` toolboxes =
the remodel row. Boundary levels (10/20/30/40) appear TWICE with different
numbers (remodel row ending one block, base row starting the next) —
transcribed literally; whether row N means "cost to reach N" vs "remodel at
N" is unresolved, do not collapse the duplicates.

### Block 1 (levels 1–10)

| lv | element | toolbox n/a | rupees |
|----|---------|-------------|--------|
| 1 | 0 | 0/0 | 500 |
| 2 | (cell absent) | 0/0 | 500 |
| 3 | (cell absent) | 2/0 | 500 |
| 4 | (cell absent) | 2/0 | 500 |
| 5 | (cell absent) | 4/0 | 500 |
| 6 | (cell absent) | 4/0 | 500 |
| 7 | (cell absent) | 8/0 | 500 |
| 8 | (cell absent) | 8/0 | 500 |
| 9 | (cell absent) | 12/0 | 1000 |
| 10 remodel | 1 | 0/0 | 5000 |

### Block 2 (levels 10–20)

| lv | element | toolbox n/a | rupees |
|----|---------|-------------|--------|
| 10 | 0 | 10/0 | 750 |
| 11 | (absent) | 10/0 | 750 |
| 12 | (absent) | 10/0 | 750 |
| 13 | (absent) | 12/1 | 750 |
| 14 | (absent) | 12/1 | 750 |
| 15 | (absent) | 12/1 | 750 |
| 16 | (absent) | 14/3 | 750 |
| 17 | (absent) | 14/3 | 750 |
| 18 | (absent) | 22/4 | 750 |
| 19 | (absent) | 40/5 | 1500 |
| 20 remodel | 6 | 0/0 | 10000 |

### Block 3 (levels 20–30)

| lv | element | toolbox n/a | rupees |
|----|---------|-------------|--------|
| 20 | 0 | 30/6 | 5000 |
| 21–29 | (absent) | 30/6 each | 5000 each |
| 30 remodel | 25 | 0/0 | 40000 |

### Block 4 (levels 30–40)

| lv | element | toolbox n/a | rupees |
|----|---------|-------------|--------|
| 30 | 0 | 70/8 | 15000 |
| 31–39 | (absent) | 70/8 each | 15000 each |
| 40 remodel | 50 | 0/0 | 100000 |

### Block 5 (levels 40–50)

| lv | element | toolbox n/a | rupees |
|----|---------|-------------|--------|
| 40 | 0 | 130/10 | 30000 |
| 41–49 | (absent) | 130/10 each | 30000 each |
| 50 | (empty) | 130/10 | 30000 |

Grid readable summary (per-level toolbox, rupees; remodel rows starred):
1–2: 0/0, 500 · 3–4: 2/0, 500 · 5–6: 4/0, 500 · 7–8: 8/0, 500 ·
9: 12/0, 1000 · *10: elem 1, 0/0, 5000* ·
10–12: 10/0, 750 · 13–15: 12/1, 750 · 16–17: 14/3, 750 · 18: 22/4, 750 ·
19: 40/5, 1500 · *20: elem 6, 0/0, 10000* ·
20–29: 30/6, 5000 · *30: elem 25, 0/0, 40000* ·
30–39: 70/8, 15000 · *40: elem 50, 0/0, 100000* ·
40–50: 130/10, 30000 (lv50 element cell empty in source).

---

## 2. Self-overcoming (자기극복) metron table, exact (헌터 page §1.5)

Header: `자기극복 순서 | 1 | 2 | 3`. Cells are `결정체/조각`
(crystal/fragment); fragment is exactly 10× crystal in every cell.
3★+ unlock; same-grade hunter + metron per step (타게임의 초월 analogue).

| grade | step 1 | step 2 | step 3 |
|-------|--------|--------|--------|
| 1★ | 5/50 | 15/150 | 45/450 |
| 2★ | 7/70 | 25/250 | (empty) |
| 3★ | 9/90 | 30/300 | 80/800 |
| 4★ | 12/120 | 40/400 | 110/1100 |

Note: 2★ has only 2 steps in the source (third cell empty), all others 3.
5★ row does not exist in the source.

---

## 3. Skill training (특기 단련) material table, exact (헌터 page §1.5)

Prose: metron-based; from skill level 5 a role material is also required, +1
per 5 levels; hunter grade raises skill max level by 10 per grade.
Header bands: `1~4 | 5~9 | 10~14 | 15~19 | 20~24 | 25~29 | 30~34 | 35~39 |
40~44 | 45~50`.

Attacker row (fully populated; defender/bomber/helper rows show label cells
only — the numeric grid is rowspanned from this row in the wiki source, i.e.
quantities are SHARED across roles, materials differ):

- 공격수 (녹슨/예리한/신기한)금속 조각:
  `0/0/0 | 1/0/0 | 2/0/0 | 3/0/0 | 4/1/0 | 5/2/0 | 0/3/1 | 0/4/2 | 0/5/3 | 0/6/4`
- 수비수 (부서진/멀정한/무적의)등껍질 — quantities per shared grid above
- 폭격수 (차가운/뜨거운/이글거리는)화염석 — quantities per shared grid above
- 도우미 (시든/싱싱한/열매 맺은)약초 — quantities per shared grid above
- 종합 메트론 조각: `1 | 2 | 3 | 4 | 5` — only FIVE values for TEN bands in
  the source; band pairing is unresolved (recorded literally, do not split).
  **[pairing RESOLVED 2026-10-05 per `transcendence-skill-cost-2026-10-05.md`
  §2.3/§2.4 and its §2.13 item 1: the fragment row bands at 10 levels while the
  material row bands at 5, so the short row is a coherent merged-cell artefact,
  not a source error — decadal 1–9→1, 10–19→2, 20–29→3, 30–39→4, 40–49→5, agreed
  by [EN-2017] and [NAMU], with level 50 → 5 from [NAMU] alone. The "do not
  split" instruction is superseded for the fragment row only; the literal
  transcription above stays valid as a reading of what the wiki stores.]**

---

## 4. Fight Club tier rewards (메인 page §3.2.2, footnote `(티어)보상`)

Tier order: 브론즈, 실버, 골드, 에메랄드, 메트론, 만다(린). Tier-up = 6 wins
regardless of losses (`한 리그(티어) 당 6번 승리`); re-clearing 6 wins inside
만다린 re-awards the 만다린 reward. Settlement + reset every Sunday.

| tier | 파이트칩 | 녹색 만다 |
|------|----------|-----------|
| 실버 | 100 | 2 |
| 골드 | 100 | 2 |
| 에메랄드 | 150 | 2 |
| 메트론 | 150 | 2 |
| 만다린 | 200 | 2 |

Note: 브론즈 has NO entry in the source footnote (entry on first tier
unrecorded, not zero-claimed).

---

## 5. Fight Club rank rewards, ranks 1–30000+ (메인 page §3.2.2, footnote `(순위)보상`)

Rank by 승점 (win ≈ +15, loss ≈ −8; defense loss −5~6; revenge-loss/forfeit
−8). Sunday settlement; payout after settlement only.

| rank | 파이트칩 | + bonus |
|------|----------|---------|
| 1 | 2500 | 녹색 만다 800 |
| 2 | 2400 | 녹색 만다 650 |
| 3 | 2300 | 녹색 만다 600 |
| 4–10 | 2200 | 녹색 만다 550 |
| 11–20 | 2100 | 녹색 만다 500 |
| 21–30 | 2000 | 녹색 만다 475 |
| 31–50 | 1900 | 녹색 만다 450 |
| 51–70 | 1800 | 녹색 만다 425 |
| 71–100 | 1700 | 녹색 만다 400 |
| 101–130 | 1600 | 녹색 만다 375 |
| 131–180 | 1500 | 녹색 만다 350 |
| 181–240 | 1400 | 녹색 만다 320 |
| 241–320 | 1300 | 녹색 만다 300 |
| 321–420 | 1200 | 녹색 만다 275 |
| 421–550 | 1100 | 녹색 만다 250 |
| 551–720 | 1000 | 녹색 만다 **255** (sic — breaks the descending 250→200 run; preserved literally, likely wiki typo, do not smooth) |
| 721–950 | 900 | 녹색 만다 200 |
| 951–1250 | 800 | 녹색 만다 175 |
| 1251–1620 | 700 | 녹색 만다 150 |
| 1621–2120 | 650 | 녹색 만다 125 |
| 2121–2750 | 600 | 녹색 만다 100 |
| 2751–3600 | 550 | 녹색 만다 75 |
| 3601–4700 | 500 | 녹색 만다 50 |
| 4701–6100 | 450 | 고급 의뢰서 3 |
| 6101–8000 | 400 | 고급 의뢰서 2 |
| 8001–10300 | 350 | 고급 의뢰서 1 |
| 10301–13500 | 300 | 오르니톱터 연료 쿠폰 5 |
| 13501–17500 | 250 | 오르니톱터 연료 쿠폰 4 |
| 17501–23000 | 200 | 오르니톱터 연료 쿠폰 3 |
| 23001–30000 | 150 | 오르니톱터 연료 쿠폰 2 |
| 30000 Under (below 30000) | 100 | 오르니톱터 연료 쿠폰 1 |

Bonus-currency break points: green manda ends at 4700; 고급 의뢰서
4701–10300; fuel coupons below 10301.

---

## 6. Helium capsule costs, exact (메인 page §2.1 용어)

- 1★: 5 entries × 2 capsules (total 10)
- 2★: 4 entries × 8 capsules (total 32)
- 3★: 2 entries × 15 capsules (total 30)

(Corrects lane-log §2 compression which omitted the 2★ row.)

---

## 7. Seore attacker Capture batch — retry status (STILL UNRESOLVED)

Target: `Capture+_2019-01-25-23-49-07.png` (Lapis, attacker §2.1.1).
New attempts this lane (no bot-wall bypass — normal fetches only):

1. `dark.namu.moe` file page → HTTP 200 but metadata-only (license/ fair-use
   notice, zero `<img>` pixel URLs); same broken-image result as `d.namu.moe`.
2. Wayback **availability API** for the file pattern → HTTP 200,
   `archived_snapshots: {}` (empty — no capture; distinct from the earlier
   CDX 429, and still no pixels).
3. Web search for the exact filename + 블루스톤/라피스 → zero results; no
   third-party host carries the file.

Lead remains open; no values inferred. The 28-filename Seore attacker index
(2019-01-25/26 batch) stands as the locator; pixels unavailable from every
public route tried to date.
