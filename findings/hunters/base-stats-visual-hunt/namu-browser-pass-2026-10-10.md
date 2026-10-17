# namu.wiki full browser pass — first successful render, 2026-10-10

**Lane goal.** The 2026-10-08 note (`namu-browser-partial-2026-10-08.md`) established
that `namu.wiki` renders fully in a real browser but only the main article was read
(23,818 chars; 290 links not followed). This lane finished that pass: the main
article in full, the `블루스톤/헌터` page, the `블루스톤/아이템` page, and all four
per-role pages (`공격수` / `수비수` / `폭격수` / `도우미`), each captured as rendered
`innerText` plus colspan/rowspan-aware table grids.

**Coverage counters are UNMOVED: heroes 1/113 · accessories 1/100 · monsters 0/22.**
No hero base-stat tuple was found — namu, like every other source, does not publish
HP/ATK/DEF. What this lane delivers instead is (a) an independent Korean identity
roster, (b) several complete original numeric tables, (c) the first per-skill effect
magnitudes in the corpus, and (d) second-source confirmations for two claims the
2026-10-09 audit marked thinly-evidenced.

## 1. Method and instrument notes

- **Render, never raw-fetch.** `browser.tabs.open` → `readyState === complete` →
  `document.body.innerText` + table grid extraction → JSON blob download →
  server-local file. Plain HTTP to namu returns 403; the mirrors
  (`m`/`d`/`dark.namu.moe`, `seore.org`) return 200 with a client-rendered shell
  and **zero article text** — so every prior "namu read" via mirrors was reading
  nothing. This is why the per-role pages (previously "165 slots, 0 values") had
  never actually been read.
- **Positive controls per page:** title contains `나무위키`, `최근 수정 시각`
  present, image/link counts non-zero. Page last-modified timestamps are recorded
  per capture below; they matter because this wiki is **live and post-dates the
  2019-09-05 rebalance**.
- **Table extraction fix:** `innerText` alone collapses merged cells. Tables were
  re-extracted with a colspan/rowspan grid algorithm (both fillings), saved as
  `*-tables-grid*.tsv`.
- **Known trap:** naive section counting double-counts the table of contents
  (TOC headers repeat body headers). Body must be located from the **last**
  occurrence of `1. 개요`.

## 2. Capture inventory (all under `namu-browser-2026-10-10/`)

| file | page | last-modified (on page) | content |
|---|---|---|---|
| `main-article.txt` | 블루스톤 | 2026-10-01 19:22:12 | 23,706 chars, sha256 `19290952708eefa2…` |
| `main-stages.txt` | 블루스톤 §3.2 | — | stage/version sections excerpt |
| `hunters-page.txt` | 블루스톤/헌터 | 2026-10-09 13:00:28 | 32,078 chars, sha256 `620bbd4e964dd2ac…` |
| `hunters-tables-grid2.tsv` | same | — | 19 tables, grid-aligned |
| `items-page.txt` | 블루스톤/아이템 | 2026-08-27 03:29:25 | 18,019 chars, sha256 `6530179d2630…` |
| `items-tables-grid.tsv` | same | — | 16 tables |
| `role-offense.txt` | /헌터/공격수 | 2026-08-20 09:56:09 | per-hunter skill sections |
| `role-defense.txt` | /헌터/수비수 | 2026-07-07 01:38:18 | idem |
| `role-bomber.txt` | /헌터/폭격수 | 2026-10-05 14:34:29 | idem |
| `role-support.txt` | /헌터/도우미 | 2026-08-03 13:56:37 | idem |
| `role-*-tables.tsv` | per role | — | materials tables |
| `namu-skill-effects-structured.tsv` | derived | — | 279 skill rows (name/category/description/effect) |
| `skill-effects-extracted.tsv` | derived | — | earlier text-line extraction (superseded) |

Hero sections captured: offense 23 hunters, defense 18, bomber 16, support 18 —
75 sections carrying Korean name, 태생 등급 (birth rarity) and 속성 (element),
i.e. an **independent Korean-language identity roster** for the 113-character
catalog.

## 3. Numeric tables recovered (all [COMMUNITY-SOURCED], era = live wiki)

### 3.1 Equipment upgrade cost curve, Lv 1→50 — complete

From `hunters-page.txt` §1.5 장비 강화 (tables 7–11). Per equipment level:
attribute material (번개 막대 / 냉각수 / 인화성 물질 — same count for all three
attributes, colspan-merged on the page), toolbox pair (도구 상자/고급 도구 상자),
and rupees:

| Lv | attr mat. | toolbox pair | rupees |
|---|---|---|---|
| 1–2 | 0 | 0/0 | 500 |
| 3–4 | 0 | 2/0 | 500 |
| 5–6 | 0 | 4/0 | 500 |
| 7–8 | 0 | 8/0 | 500 |
| 9 | 0 | 12/0 | 1000 |
| **10** | **1** | 0/0 | 5000 |
| 11–12 | 0 | 10/0 | 750 |
| 13–15 | 0 | 12/1 | 750 |
| 16–17 | 0 | 14/3 | 750 |
| 18 | 0 | 22/4 | 750 |
| 19 | 0 | 40/5 | 1500 |
| **20** | **6** | 0/0 | 10000 |
| 21–29 | 0 | 30/6 | 5000 |
| **30** | **25** | 0/0 | 40000 |
| 31–39 | 0 | 70/8 | 15000 |
| **40** | **50** | 0/0 | 100000 |
| 41–49 | 0 | 130/10 | 30000 |
| 50 | 0 | 130/10 | 30000 |

Attribute materials are consumed **only at the 10-level modification steps**
(10/20/30/40 → 1/6/25/50). This is the same curve the FAQ's single OCR sample
(`GEAR.md`: Lv49→50 ≈ 50,000 + 389/320 + 11/27) sits on, but the ** rupee figures
disagree** (30,000 here vs 50,000 there): the FAQ is a 2018-era capture, this wiki
is live. Era-tag both; do not merge.

### 3.2 Skill-training (특기 단련) materials — confirms existing bands

Per-position material (공격수 녹슨/예리한/신기한 금속 조각, 수비수 부서진/멀쩡한/무적의
등껍질, 폭격수 차가운/뜨거운/이글거리는 화염석, 도우미 시든/싱싱한/열매 맺은 약초) by
level band 1~4 … 45~50 as `0/0/0, 1/0/0, 2/0/0, 3/0/0, 4/1/0, 5/2/0, 0/3/1, 0/4/2,
0/5/3, 0/6/4`, plus 메트론 조각 1–5 by band. This independently reproduces the ten
trios the 2026-10-09 audit verified against namu item tables (§1(2)).

### 3.3 Transcendence (자기극복) cost ladder — two materials, 10× apart

| grade | T1 | T2 | T3 |
|---|---|---|---|
| 1★ | 5 / 50 | 15 / 150 | 45 / 450 |
| 2★ | 7 / 70 | 25 / 250 | — |
| 3★ | 9 / 90 | 30 / 300 | 80 / 800 |
| 4★ | 12 / 120 | 40 / 400 | 110 / 1100 |

(메트론 결정체 / 메트론 조각; the page notes the 10× ratio explicitly.) Opens at 3★.

### 3.4 Recruitment traces: `(2^grade) × 10`

1★ 20, 2★ 40, 3★ 80, 4★ 160 — with the formula stated on the page.

### 3.5 Missing-hunter search (헬륨 캡슐) costs

| hunter grade | helium | searches |
|---|---|---|
| 1★ | 2 | 5 |
| 2★ | 8 | 4 |
| 3★ | 15 | 2 |

### 3.6 Shop corners / recruitment tickets

고급 의뢰서 20,000 루피 (루피 코너); 특급 의뢰서 = 파이트칩 1500 + 신기루 조각 3000 +
첨쥐 코인 20 (or 60,000 루피 when it appears). 전설의 지명 의뢰서 every 28 attendance
days, pick any 3★.

### 3.7 Arena (파이트클럽) — the 31-band chip ladder, independently

`items-tables-grid.tsv` table 1 reproduces the ladder **exactly** as the 2026-10-09
audit re-derived it: 31 bands, deltas −100 ×18 (2500 → 700) then −50 ×12
(650 → 100), the −100 regime ending at the `1621–2120 → 650` band. This is the
**second independent source** the audit's item D3 asked for, and it settles
A1/A2 (28 rows / "boundary at rank 100" were both wrong) from a
non-handoff origin. Related: league = 6 wins to promote regardless of losses;
bronze→silver→gold→emerald→metron→manda; loss −8, win +15 rating points
(see §4).

### 3.8 Fight Club tier chip rewards

실버 100, 골드 100, 에메랄드 150, 메트론 150, 만다 200 (달성 티어 table).

## 4. Second-source confirmations (audit D-list items)

- **Arena rating ±15 / −8** (audit D5, previously single-source + a recorded
  refusal): the main article states it verbatim — 패배 시 승점 8점 하락, 승리 시
  15점 상승. The refusal in `fc-native` §1.4 still governs binding values into the
  server, but the "single community source" weakness is now closed.
- **Beckhen's Fight Club buff** (`LEVELING.jet` `b_00_01` whitelisting card `051`):
  the roster narratives state 파이트클럽 전용 +10% 공격/방어/생명력 for 백헨 —
  independent corroboration of the recovered stage whitelist.
- **Rage rule with its two exceptions**: 보통 공격수/수비수 3, 폭격수/도우미 4,
  with 릴리&랄라 and 곰 named as the 4-rage exceptions — matching the recovered
  role→rage cross-validation (036, 047) exactly.
- **Element cycle**: 냉기 > 화염 > 전격 > 냉기 (Ice > Fire > Lightning > Ice).
- **50 expedition stages as of 2019**, 10 per region × 5 regions — matches
  `LEVELING.jet` chunk 0 and the earlier namu citation.

## 5. First per-skill effect magnitudes in the corpus

The per-role pages carry a `특기 효과:` field per skill. It is filled for only a
handful of hunters (blank for most; the support page's fields could not be read
at all — see §7). Recovered values, verbatim:

| hero | skill | effect |
|---|---|---|
| 백헨 `051` | 꼬꼬댁!! 꼬꼬! (극대화) | 피해량 ~9046 |
| 백헨 `051` | 극한의 속도감소 → 공격 속도 증가 | 공격 속도 ~20.00% |
| 백헨 `051` | 작고 가벼운 자 | 지속 시간 0.51~1.00초 |
| 백헨 `051` | 죽음의 날개짓 | 방어력 ~30.00% |
| 백헨 `051` | 파이트클럽의 수호자 | 막기 확률 ~30.00% |
| 모글리 `002` | (3초마다 피해면역) | 지속 시간 0.51~1.00초 |

**Calibration note for the skill-magnitude fixture.** `INDEX.md` §7.2 marks skill
`value`/`value_up` as `[INFERRED-FIXTURE]` (fixture: value ~1000–3000 at Lv.1).
Beckhen's recovered Lv.30 nude ATK is 1471 and his rank is 3★, so the shipped
formula `-1*(stat*(8+2*rank))*(value+value_up*skill_level)/10000` gives a
multiplier base of `1471 × 14 = 20,594`. `~9046 / 20,594 ≈ 0.439`, i.e.
`(value + value_up × L) ≈ 4390` at whatever skill level the wiki screenshotted
(level not stated). That is the first numeric anchor for the fixture — it rules
out the low end (~1000–3000 at any level if the reading is near max level) but
does not determine `value` vs `value_up` split. Treat as one observation
[COMMUNITY-SOURCED], level unknown.

Also from the bomber narratives: 걸베이그 `039` passive +7.5% ally attack speed;
헤르메스 `023` +15%; stated stacking to 22.5% (and 37.5% with Karl's self-buff).
These are team-buff magnitudes, not per-card base stats.

## 6. Corrections to prior findings

1. **"Base Attack Speed 8.00 on two cards → plausibly a game-wide constant"
   [DERIVED, n=2] is now REFUTED as a constant.** The roster narratives give
   덤블 `048` 공격속도 6 and 칼슈타이너 `012` 공격속도 7 (노 스킬 상태).
   Two independent values ≠ 8.00 from the same source class. Attack speed is
   per-card; the n=2 "constant" reading must be struck. (The 8.00 observations
   themselves stand; only the constant inference fails.)
2. **Arena ladder row count / step boundary** — see §3.7; the namu items table is
   the second source and agrees with the audit, not with the handoff.
3. **Equipment Lv49→50 cost** — the 30,000-rupee reading here vs the FAQ's
   ~50,000 is an era difference (live wiki vs 2018 capture), not a conflict to
   resolve. Record both with dates.

## 7. Instrument limits (recorded, not worked around)

- **Support page skill fields are unreadable**: zero elements matching the
  `특기 효과` selector; its `innerText` shows the labels with blank values and
  blank 무기/방어구/장신구 values. Content may be image-only. Not a content
  negative for support skills — an instrument gap.
- **Effect values exist for only ~6 of 279 captured skills.** The blank ones are
  honest blanks in the wiki, not extraction failures (verified against DOM).
- **No hero base stats anywhere on namu.** The wiki publishes identity, skill
  text, and cost curves — never HP/ATK/DEF. The 62-row 2019 JP archive remains
  the only numeric hero-stat corpus, and its level/gear context is still the
  blocker to strict coverage.
- **No accessory stat values.** Accessories stay 1/100 (Jack only).
- TOC double-count trap (§1) — any future parser must anchor the body at the
  last `1. 개요`.

## 8. What this lane suggests next

1. **`블루스톤/헌터/이야기` sub-page** (linked from the support page header,
   never opened): hunter story text; identity/lore only, low stat value.
2. **Main article §6.2 후속작 발표** (sequel announcement) — captured in
   `main-article.txt`; review for version history that could era-tag other
   captures.
3. The two background lanes launched with this pass (blustone.jp `/archives/`,
   BTB official site) — see their reports.
4. A Korean search-engine cache pass for equipment-panel screenshots is now the
   only remaining accessory vector; namu itself has no item stat lines.
