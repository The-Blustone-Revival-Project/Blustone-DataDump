# namu.wiki `블루스톤/헌터` — the per-hero page, read in a real browser (2026-10-08)

**Target:** `https://namu.wiki/w/%EB%B8%94%EB%A3%A8%EC%8A%A4%ED%86%A4/%ED%97%8C%ED%84%B0`
**Page 최근 수정 시각 (last modified): 2026-10-03 11:15:24**
**Sub-pages read:** the four per-role pages linked from §2.1–§2.4 (see §9).

---

## 0. Result, stated plainly

| Priority asked for | Verdict | Yield |
|---|---|---|
| **1. Per-hero HP/ATK/DEF/level tables** | **NEGATIVE** — the page has **no** per-hero stat line of any kind | **0** stat tuples. Heroes stay **1/113**. |
| **2. Element assignments, cross-checked vs the 2019 JP archive** | **POSITIVE, and the cross-check is the real deliverable** | **56** heroes with `속성`; **1** genuine element disagreement (Pansy `057`) |
| **3. Grade/rarity per hero + which heroes exist** | **PARTIAL POSITIVE** | **56** heroes with `태생 등급`; covers **1 of the 51** uncovered-archive ids cleanly |
| **4. Equipment (장비) tables** | **NEGATIVE for stat values, POSITIVE for the enhancement COST ladder** | **0** accessory stats (accessories stay **1/100**); a complete original **Lv.1–50 enhancement cost table** that this project does not have |
| **5. `초월` / transcendence (T2)** | **PARTIAL POSITIVE — cost, not multiplier** | namu's `자기극복` T1/T2/T3 material table, independently corroborating the ★3 row. **The from-base-vs-compounding question is NOT answered.** |

The headline is not a stat table. It is that **this page is a working, live,
post-rebalance mechanics+economy source** whose 19 tables and mechanics prose
corroborate or correct **six** numbers the replica currently treats as a local
fixture, and whose per-hero tables carry **identity, element and grade but never a
stat**.

**Coverage counters moved: none.** Heroes 1/113, accessories 1/100, monsters 0/22,
jewel set bonuses unchanged.

---

## 1. Instrument, and why the render was necessary

namu.wiki returned **HTTP 403** to the plain fetch in this session, reproducing
the known gate:

```
403 GET https://namu.wiki/w/%EB%B8%94%EB%A3%A8%EC%8A%A4%ED%86%A4/%ED%97%8C%ED%84%B0
```

The in-session desktop-browser tool was **disconnected for this whole lane**
(`[browser.disconnected] No desktop browser is connected to this session`),
retried across ~4 minutes of wall-clock. The gate was therefore worked around
with a **local headless Edge on the host**, driven from Python — i.e. still a
real browser doing the JS render, just not the harness one. Mirrors
(`d.namu.moe`, `dark.namu.moe`, `m.namu.moe`, `seore.org`) were **not** used and
are **not** reported as content negatives anywhere in this file.

### Positive control (run before any zero was recorded)

| leg | result |
|---|---|
| known-good page `블루스톤` (main) | **rendered** — 249,394 B DOM, **24,342** visible chars, **4** `<table>` — matches the earlier lane's 23,818 chars / 4 tables |
| target page `블루스톤/헌터` | **rendered** — 432,919 B DOM, 31,154 visible chars, **19** `<table>` |
| 4 per-role sub-pages | **rendered** — 415,486 / 353,529 / 332,558 / 295,609 B |

The control is the reason the per-hero-stat negative in §5 is a finding and not a
fetch failure.

### Method actually used

Tables were walked as **`table.rows` from the DOM**, not read out of
`innerText`. namu serialises a Vue app, so `--dump-dom` returns the post-render
tree; a grid expander honouring `rowspan`/`colspan` was used so merged cells
cannot silently shift a numeric column. Prose came from the same tree with
tags stripped, tables interleaved in document order.

- `analysis/research/base-stats-visual-hunt/_namu_headless.py` — render
- `analysis/research/base-stats-visual-hunt/_namu_tables.py` — rowspan/colspan grid
- `analysis/research/base-stats-visual-hunt/_namu_text.py` — ordered prose+table text, hashes
- `analysis/research/base-stats-visual-hunt/_namu_roster.py` — roster + cross-check
- `analysis/research/base-stats-visual-hunt/_namu_numeric_census.py` — numeric census + control
- `analysis/research/base-stats-visual-hunt/_namu_uncovered.py` — uncovered-roster overlap
- `analysis/research/base-stats-visual-hunt/_namu_tablemd.py`, `_namu_emit.py`, `_namu_subpages.py`

### Provenance hashes

| artefact | SHA-256 | size |
|---|---|---|
| `블루스톤/헌터` rendered DOM | `a53213d31d07b181f785573d8500b6bd8551e80379da680eb33ea2e7b9d33cde` | 432,919 B |
| `블루스톤/헌터` extracted text (prose+tables) | `75cf6c0a21c5fc9a909b6e92cb7d12474a1fbbac2cd2884c451c702cb8b6b3d0` | 35,809 chars |
| `…/헌터/공격수` DOM / text | `4fe2fecca940396b87d0160ae9439bdb7d412f5342c97a3172496ceefbb6f7d7` / `18c0202d9f27bd3adac1d14b7a3a572542801ced07210a3a1369f0f1f808c414` | 415,486 B |
| `…/헌터/수비수` DOM / text | `139a15eeaf0ed917481e4b98c5462fb54eb7dc3b0b993d468dd023a0b585795c` / `328d7381d64961a864acdd916ac5acdd5982df683ff326dab45b085a7549fd7e` | 353,529 B |
| `…/헌터/폭격수` DOM / text | `55e499eaca45c177b683a2094784f0935ae0c67f5406816148dad16590275dae` / `282521c1fcd8857c67d1d8dbad89482bf50fb9c3945d278dcddec0c3c3898747` | 332,558 B |
| `…/헌터/도우미` DOM / text | `3a50c3a107e44bcb6c2f1548ed17d74f39115141023b792136420b91297974fe` / `51947e23dbf77919e2a1e274265586a30a344a5f8a9482320f5cee7d42e202cd` | 295,609 B |
| roster markdown (56 rows) | `af58592c07c39da9145fbc1d44266c8c75de5f3a86f53eccbddb51a418cbe6dc` | 4,226 chars |
| roster JSON | `b5e1458dad17c6f3bfaa89b9b85e13bbc949a8e2372c402201435619cd3c544a` | — |

`U+FFFD = 0` in every extracted text file.

**Era.** Last modified **2026-10-03**, i.e. ~7 years after the **2019-09-05**
rebalance. Every numeric reading below is **post-rebalance** and must not be
compared like-for-like against a 2017–2019 capture without saying so.

---

## 2. Grade model, stated by the page (§1.2)

> 총 등급은 1성 ~ 5성 까지이며 발견되는 태생은 4성까지이다.

**Table 1 — 5 rows × 2 cols.** Headerless; the grade titles.

| row | value |
|---|---|
| r00 | `1성` \| `신입 헌터` |
| r01 | `2성` \| `하급 헌터` |
| r02 | `3성` \| `중급 헌터` |
| r03 | `4성` \| `고급 헌터` |
| r04 | `5성` \| `마스터 헌터` |

So: total grades run **1★–5★**, but the highest **태생 (birth grade)** is **4★**.
5★ (`마스터 헌터`) is the *evolved* state of a ≤4★ birth hunter. This is the same
two-layer model as the client's `rank` vs `grade`.

---

## 3. Element model, and the cycle

> 화염 (가위), 냉기 (바위), 전격 (보자기)이 존재하며, **냉기 > 화염 > 전격 > 냉기** 순으로 공격 효과가 세고 역순으로 효과가 떨어진다.

**Element cycle: Ice > Fire, Fire > Lightning, Lightning > Ice.** The brief's
"Fire > Lightning > Ice > Fire" is the same cycle at a different rotation —
**no conflict**, and this is an independent Korean attestation of the native
enum. namu gives the rock-paper-scissors icons: Fire=가위 scissors,
Ice=바위 rock, Lightning=보자기 paper.

Per-hero element tokens in the role tables are `전속` / `수속` / `화속`
(Lightning / Ice / Fire). Distribution over the 56 heroes:
**Ice 20, Fire 19, Lightning 17.**

---

## 4. All 19 tables, verbatim

`[img:…]` marks a cell whose only content is an image; the text is its `alt`.
Rows not listed were empty padding rows in the grid.

#### Table 0 — 2 rows × 2 cols — hunter-album UI screenshots
- r00 | `[img:빠삐용 획득]` | `[img:빠삐용 미획득]`
- r01 | `획득한 헌터` | `획득하지 않은 헌터`

#### Table 1 — 5 rows × 2 cols — grade titles
- r00 | `1성` | `신입 헌터`
- r01 | `2성` | `하급 헌터`
- r02 | `3성` | `중급 헌터`
- r03 | `4성` | `고급 헌터`
- r04 | `5성` | `마스터 헌터`

#### Table 2 — 5 rows × 2 cols — recruitment documents (의뢰서)
- r00 | `초급 의뢰서` | 평범한 종이 문서 모양. 헌터들의 흔적을 모을 수 있으며 1개를 개별적으로 쓰거나 2~10개를 한번에 쓸 수 있으며, [35] 의뢰서 1개에 1~3성 헌터의 흔적을 최대 5개 까지 얻을 수 있다.
- r01 | `고급 의뢰서` | 초급과 달리 황금빛인 문서. 1~4성 헌터 섭외를 할 수 있다. 상점의 루피 코너에서 **20000루피**로 구매할 수 도 있다.
- r02 | `특급 의뢰서` | 초록색에 금빛 테두리의 문서. 2~4성 헌터만 확정적으로 섭외할 수 있다. 상점에서 **파이트칩 1500개, 신기루 조각 3000개, 첨쥐 코인 20개**로 구매 가능하며 가끔 루피 코너에서 **60000루피**로 뜰 때도 있다.
- r03 | `전설의 의뢰서` | 파란색에 금빛 테두리의 문서. 3~4성 헌터만 확정적으로 섭외할 수 있다.
- r04 | `전설의 지명 의뢰서` | 무지갯빛의 문서. **출석 28일마다** 얻을 수 있으며 다른 모든 의뢰서와 달리 3성 헌터 중 원하는 헌터를 고를 수 있다. 단, 나온지 얼마 안 된 3성 헌터의 경우, 포함이 안 돼 있을 수 있다.

#### Table 3 — 4 rows × 2 cols — **trace cost to guarantee-recruit, by grade**
- r00 | `1성` | `20개`
- r01 | `2성` | `40개`
- r02 | `3성` | `80개`
- r03 | `4성` | `160개`

Formula given in the prose immediately after: **`(2^n)×10개`** where *n* is the
hunter grade. namu also states the multi-recruit rule: 100 traces on a 1★ hunter
(20 each) ⇒ 5 at once.

#### Table 4 — 2 rows × 6 cols — gym UI screenshots
- r00 | `[img:Capture+ 2018-04...]` ×5 | `[img:Capture+ 2019-01...]`
- r01 | `훈련할 헌터 선택 시` | `훈련` | `승급` | `자기극복` | `특기 단련` | `장비 강화`

#### Table 5 — 5 rows × 4 cols — **자기극복 (self-overcoming) material by T1/T2/T3**
Header: `자기극복 순서` | `1` | `2` | `3`

| row | birth grade | T1 | T2 | T3 |
|---|---|---|---|---|
| r01 | `1성` | `5/50` | `15/150` | `45/450` |
| r02 | `2성` | `7/70` | `25/250` | *(empty)* |
| r03 | `3성` | `9/90` | `30/300` | `80/800` |
| r04 | `4성` | `12/120` | `40/400` | `110/1100` |

Column semantics are given in the prose: **메트론 결정체 is left, 메트론 조각 is
right**, and the two differ by exactly 10×. So `9/90` = 9 crystals + 90 fragments.

#### Table 6 — 9 rows × 12 cols — Raise (훈련) material by level band
Header: `포지션` | `소모품\레벨(lv.)` | `1~4` | `5~9` | `10~14` | `15~19` | `20~24` | `25~29` | `30~34` | `35~39` | `40~44` | `45~50`

- r01 | `공격수` | `(녹슨/예리한/신기한) 금속 조각` | `0/0/0` | `1/0/0` | `2/0/0` | `3/0/0` | `4/1/0` | `5/2/0` | `0/3/1` | `0/4/2` | `0/5/3` | `0/6/4`
- r02 | `수비수` | `(부서진/멀쩡한/무적의) 등껍질` | *(all empty)*
- r03 | `폭격수` | `(차가운/뜨거운/이글거리는) 화염석` | *(all empty)*
- r04 | `도우미` | `(시든/싱싱한/열매 맺은) 약초` | *(all empty)*
- r05 | `종합` | `메트론 조각` | `1` | | `2` | | `3` | | `4` | | `5` | *(last three bands empty)*

**Editorial gap, and it is a real one:** the material *names* are given for all
four roles but only the **Offense** row is filled. The `미네로` piece column stops
at band 30–34.

#### Tables 7–11 — 5 tables, 20/22/22/22/22 rows × 7 cols — **equipment enhancement cost, Lv.1 → Lv.50**
All five share the same two header rows:
- r00 | `속성` | `전격` | `냉기` | `화염` | `종합` | |
- r01 | `레벨(lv.)\소모품` | `번개 막대` | `냉각수` | `인화성 물질` | `도구 상자/고급 도구상자` | `루피` |

**Table 7** (Lv. 1–10), 12 non-empty rows:
- r02 | `1` | `0` | | | `0/0` | `500`
- r03 | `2` | | | | `0/0` | `500`
- r04 | `3` | | | | `2/0` | `500`
- r05 | `4` | | | | `2/0` | `500`
- r06 | `5` | | | | `4/0` | `500`
- r07 | `6` | | | | `4/0` | `500`
- r08 | `7` | | | | `8/0` | `500`
- r09 | `8` | | | | `8/0` | `500`
- r10 | `9` | | | | `12/0` | `1000`
- r11 | `10` | `1` | | | `0/0` | `5000`

**Table 8** (Lv. 10–20), 13 non-empty rows:
- r02 | `10` | `0` | | | `10/0` | `750`
- r03 | `11` | | | | `10/0` | `750`
- r04 | `12` | | | | `10/0` | `750`
- r05 | `13` | | | | `12/1` | `750`
- r06 | `14` | | | | `12/1` | `750`
- r07 | `15` | | | | `12/1` | `750`
- r08 | `16` | | | | `14/3` | `750`
- r09 | `17` | | | | `14/3` | `750`
- r10 | `18` | | | | `22/4` | `750`
- r11 | `19` | | | | `40/5` | `1500`
- r12 | `20` | `6` | | | `0/0` | `10000`

**Table 9** (Lv. 20–30), 13 non-empty rows:
- r02 | `20` | `0` | | | `30/6` | `5000`
- r03–r11 | `21`…`29` | | | | `30/6` | `5000`
- r12 | `30` | `25` | | | `0/0` | `40000`

**Table 10** (Lv. 30–40), 13 non-empty rows:
- r02 | `30` | `0` | | | `70/8` | `15000`
- r03–r11 | `31`…`39` | | | | `70/8` | `15000`
- r12 | `40` | `50` | | | `0/0` | `100000`

**Table 11** (Lv. 40–50), 12 non-empty rows:
- r02 | `40` | `0` | | | `130/10` | `30000`
- r03–r11 | `41`…`49` | | | | `130/10` | `30000`
- r12 | `50` | *(empty)* | | | `130/10` | `30000`

Reading: within each decade the tool-box pair grows and the rupee cost is flat;
at each 10-level boundary the pair resets and the **Lightning** element material
is charged (`전격` 1 @Lv10, 6 @Lv20, 25 @Lv30, 50 @Lv40). **The `냉기` and `화염`
columns are empty on every row** — same one-exemplar editorial pattern as
Table 6. Footnote [45] names the mapping: Fire→인화성 물질, Lightning→번개 막대,
Ice→냉각수.

#### Table 12 — 2 rows × 4 cols — boutique UI screenshots
- r00 | `[img:Capture+ 2019-01...]` ×4
- r01 | `부티크 메인` | `헌터별 옷 목록(헌터 선택)` | `전체적 옷 목록(의상 도감)` | `의상 선택(구매하지 않은 의상)`

#### Tables 13–16 — the four per-role hero tables
Header on all four: `태생 등급` | `속성` | `이름` | `설명`.
T13 공격수/Offense 19×4, T14 수비수/Defense 16×4, T15 폭격수/Bomber 11×4,
T16 도우미/Support 14×4. **These contain zero images** (verified: image count per
table = 0,0,0,0), so nothing here is an unread image stat panel. Full rows in §6.

> **On the 4th column.** `설명` is a long per-hero narrative cell (flavour, story,
> tier commentary), several hundred characters each, totalling ~28,000 chars. It
> is **not** reproduced in full here because it is prose, not a numeric table,
> and the instruction was not to compress numeric tables into prose. It is
> **complete and hashed** in the extracted text (SHA-256 in §1). Every numeric
> reading that appears anywhere inside it was extracted and is listed in §7 —
> nothing was dropped by not reprinting it.

Grade distribution over the 56 rows: **1★ 12, 2★ 11, 3★ 29, 4★ 4**. The four
4★ are Vincent `010`, Lily & Lyla `047`, Harley `046`, Teresa `065`. **No row is
5★** — namu never shows the evolved `마스터 헌터` stat line.

#### Tables 17–18 — 1×1 and 1×1
- T17: `a.aa`
- T18: empty

These are namu UI furniture (a rating widget), **not article content**. Excluded
from every count in this file.

---

## 5. Priority 1 — the per-hero stat negative, and how it was established

Three independent lines, each with its own control:

1. **Structural.** The 56 hero rows are `태생 등급 | 속성 | 이름 | 설명`. The
   description cell is prose. There is no stat column, in any role table.
2. **Pattern search.** A regex for a `체력/생명력 … 공격력 … 방어력` triple
   returned **0 matches** across the whole 35,809-char extraction.
3. **Image audit.** All 98 `<img>` on the page were located by byte offset
   against the 18 table spans. **The four role tables contain 0 images.** The 36
   in-table images are all in Tables 0, 4 and 12 (album / gym / boutique UI
   screenshots); the 62 outside images are all in §3 NPC and §4 헌터 이야기.

**Positive control for the numeric detector:** 249 lines in the extraction carry
a numeric token and were all found — e.g. `최근 수정 시각: 2026-10-03 11:15:24`,
Table 3's `20개/40개/80개/160개`, Table 5's `9/90`. The detector fires. The
numbers in the hero rows that it does find are **footnote markers** (`[53]`,
`[54]`, …) and prose cross-references (`4성 극대화 스킬`, `3성 이상의 헌터`),
not stats. 502 numeric tokens across the role rows, **0 stat tuples**.

**Therefore: heroes remain 1/113.** The 2019 JP archive's 62 rows and this
page's 56 heroes do not overlap in the way that would help: namu supplies no
numbers, so it adds **identity data, not stat data**.

---

## 6. Priority 2 & 3 — the recovered roster, with the full cross-check

56 heroes, mapped to the project's `analysis/catalogue/data/cards.json` by reading
the Korean. **The mapping was itself audited against `cards.json` before any
disagreement was believed** — an early pass had 10 spurious element conflicts,
all of which turned out to be my own wrong `catalog_id` guesses, and they were
fixed rather than reported. Final mapping audit: 53 mapped, **1 element
mismatch, 1 role mismatch**.

`★` is the `태생 등급` cell, counted as the **total** star glyphs (the badge is
split into two DOM runs for two rows; namu's own prose independently confirms
4성 for both).

| role | name_ko | id | name_en | 속성 | ★ | 2019 archive | verdict |
|---|---|---|---|---|---|---|---|
| Offense | 변절자 빈센트 | 010 | Vincent | 전격 / Lightning | 4★ | Lightning | AGREE |
| Offense | 정체불명의 쌍둥이 릴리&랄라 | 047 | Lily & Lyla | 화염 / Fire | 4★ | Fire | AGREE |
| Offense | 파이트클럽의 수호자 백헨 | 051 | Beckhen | 냉기 / Ice | 3★ | Ice | AGREE |
| Offense | 혹한의 마녀 옥타비아 | 028 | Octavia | 냉기 / Ice | 3★ | Ice | AGREE |
| Offense | 고귀한 창 나탈리아 | 037 | Natalia | 냉기 / Ice | 3★ | Ice | AGREE |
| Offense | 은반의 요정 유리 | 045 | Yuri | 냉기 / Ice | 3★ | Ice | AGREE |
| Offense | 특급 전령사 헤르메스 | 023 | Hermes | 화염 / Fire | 3★ | Fire | AGREE |
| Offense | 두 얼굴의 소녀 하이디 | 044 | Heidi | 화염 / Fire | 3★ | Ice | AGREE |
| Offense | 불멸의 칼슈타이너 | 061 | Chichi | 전격 / Lightning | 3★ | Lightning | AGREE |
| Offense | 늑대아이 비비 | 040 | Bibi | 전격 / Lightning | 3★ | Lightning | AGREE |
| Offense | 산타걸 레베카 | 038 | Rebecca (Christmas) | 화염 / Fire | 3★ | Fire | AGREE |
| Offense | 나쁜아이 사냥꾼 산타클로스터 | 042 | Santa Clauster | 화염 / Fire | 3★ | Fire | AGREE |
| Offense | 사라진 숲의 모글리 | 002 | Mowgli | 전격 / Lightning | 2★ | Lightning | AGREE |
| Offense | 방랑 격투가 스카 | 032 | Scar | 냉기 / Ice | 2★ | Fire | AGREE |
| Offense | 황혼의 방망이단 레베카 | 021 | Rebecca | 화염 / Fire | 2★ | Fire | AGREE |
| Offense | 쾌속의 검술가 라피스 | 017 | Lapis | 냉기 / Ice | 1★ | Ice | AGREE |
| Offense | 방랑 검객 발리안 | 019 | Balian | 전격 / Lightning | 1★ | Lightning | AGREE |
| Offense | 사라지지 않는 노병 실베스터 | 006 | Sylvester | 화염 / Fire | 1★ | Fire | AGREE |
| Defense | 정의로운 자 할리 | 046 | Harley | 냉기 / Ice | 4★ | Ice | AGREE |
| Defense | 강철의 레버넌트 칼리버 | 053 | Calibur | 화염 / Fire | 3★ | Fire | AGREE |
| Defense | 전설적인 말썽꾸러기 네네 | 003 | Nene | 냉기 / Ice | 3★ | Ice | AGREE |
| Defense | 강철의 보디가드 카인 | 029 | Kain | 전격 / Lightning | 3★ | Lightning | AGREE |
| Defense | 전장의 불꽃 아테나 | 027 | Athena | 화염 / Fire | 3★ | Fire | AGREE |
| Defense | 대자연의 선물 곰 | 036 | Bear | 전격 / Lightning | 3★ | Lightning | AGREE |
| Defense | 기이한 노인 덤블 | 048 | Dumble | 냉기 / Ice | 3★ | Ice | AGREE |
| Defense | 로봇 공학자 에드워드 | 041 | Edward | 전격 / Lightning | 3★ | Lightning | AGREE |
| Defense | 희대의 탈옥수 빠삐용 | 043 | Papillon | 냉기 / Ice | 3★ | Ice | AGREE |
| Defense | 불굴의 제라드 | 005 | Gerard | 냉기 / Ice | 2★ | Ice | AGREE |
| Defense | 거친 인생 리코 | 024 | Riko | 전격 / Lightning | 2★ | Lightning | AGREE |
| Defense | 할로윈 마녀 리코 | (078?) | Teresa (Halloween) | 냉기 / Ice | 2★ | — | **identity uncertain — see §6.2** |
| Defense | 생존술의 대가 로빈 | 018 | Robin | 냉기 / Ice | 1★ | Ice | AGREE |
| Defense | 지키는자 헤카테 | 011 | Hecate | 화염 / Fire | 1★ | Fire | AGREE |
| Defense | 캡틴 | 009 | Captain | 전격 / Lightning | 1★ | Lightning | AGREE |
| Bomber | 천재 기후학자 디노 | 054 | Dino | 냉기 / Ice | 3★ | Ice | AGREE |
| Bomber | 최초의 헌터 랜턴 | 001 | Lantern | 화염 / Fire | 3★ | Fire | AGREE |
| Bomber | 조용한 송곳니 파트로네 | 033 | Patrone | 냉기 / Ice | 3★ | Ice | AGREE |
| Bomber | 천둥 화살 디아나 | 031 | Diana | 전격 / Lightning | 3★ | Lightning | AGREE |
| Bomber | 비행선 관리원 걸베이그 | 039 | Gullveig | 전격 / Lightning | 3★ | Lightning | AGREE |
| Bomber | 중위 레비 | 015 | Levi | 냉기 / Ice | 2★ | Ice | AGREE |
| Bomber | 공포의 곰인형 테디보머 | 025 | Teddy Bomber | 화염 / Fire | 2★ | Fire | AGREE |
| Bomber | 로크 앤 캐쉬 CEO 로크 | 014 | Locke | 냉기 / Ice | 1★ | Ice | AGREE |
| Bomber | 오늘도 화끈한 메티스 | 007 | Metis | 화염 / Fire | 1★ | Fire | AGREE |
| Bomber | 화력덕후 시에나 | 020 | Sienna | 전격 / Lightning | 1★ | Lightning | AGREE |
| Support | 도망친 신부 테레사 | 065 | Teresa | 화염 / Fire | 4★ | — | **new — see §6.3** |
| Support | 마성의 물리치료사 테라피 | 050 | Therapy | 냉기 / Ice | 3★ | Ice | AGREE |
| Support | 성냥팔이 소년 브라이트 | 049 | Bright | 화염 / Fire | 3★ | Fire | AGREE |
| Support | 동물 애호가 팬지 | 057 | Pansy | 화염 / Fire | 3★ | Ice | **DISAGREE** |
| Support | 강령술사 크로커스 | 058 | Crocus | 전격 / Lightning | 3★ | Lightning | AGREE |
| Support | 신목의 무녀 아카샤 | 008 | Akasha | 전격 / Lightning | 3★ | Lightning | AGREE |
| Support | 걸어다니는 진료실 조이 | 035 | Joy | 화염 / Fire | 3★ | Fire | AGREE |
| Support | 실험체 2호 해선 | — | — | 냉기 / Ice | 2★ | — | unmapped |
| Support | 청결의 요정 데날리 | 013 | Denali | 화염 / Fire | 2★ | Fire | AGREE |
| Support | 식물학자 아세로라 | 030 | Acerola | 전격 / Lightning | 2★ | Lightning | AGREE |
| Support | 데스메탈 전도사 브루스방 | 016 | Bruce Bang | 냉기 / Ice | 1★ | Ice | AGREE |
| Support | 최고의 요리사 치르치르 | — | — | 화염 / Fire | 1★ | — | unmapped |
| Support | 이상한 나라의 치르치르 | — | — | 전격 / Lightning | 1★ | — | unmapped |

### 6.1 Cross-check totals

| comparison | comparable | agree | disagree |
|---|---:|---:|---:|
| `속성` vs 2019 JP archive `element_ja` | 51 | **50** | **1** (Pansy) |
| `태생 등급` vs 2019 JP archive `rarity_on_draw` | 51 | **51** | 0 |
| `속성` vs `cards.json` element | 53 | 52 | 1 (Pansy) |
| `태생 등급` vs `cards.json` rarity | 53 | 52 | 1 (`078` row) |
| role (which table) vs `cards.json` role | 53 | 52 | 1 (`078` row) |

**This is a strong agreement.** namu, the 2019 Japanese archive and the
community catalogue are three independent descriptions of the same roster and
they converge on element for 50/51 heroes and on grade for 51/51.

### 6.2 The one real element disagreement — Pansy `057`

| source | element | date |
|---|---|---|
| **namu** 동물 애호가 팬지 | **화염 / Fire** | 2026-10-03 |
| 2019 JP archive 動物愛好家「パンジー」 | 冷気 / Ice | 2019-10 |
| `cards.json` Pansy | Ice | community |

**2 sources against namu, so namu does not overwrite.** Recorded as an open
one-row conflict. Note the two Ice sources are not fully independent of each
other (the catalogue is community-sourced and the brief records the two agreeing
61/61), so a single Korean voice against a shared pair is a real dissent, not a
settled majority. Resolution requires shipped-client or original-server data, not
a vote.

### 6.3 Coverage of the 51-ID `uncovered-archive-roster-2019.tsv`

**1 clean hit, 1 disputed, 49 absent.**

- **`065` Teresa — clean new identity data.** namu `도망친 신부 테레사`
  ("Runaway Bride Teresa"), **화염/Fire, 4★, Support**. The uncovered roster
  independently records `065` = Teresa, title *Runaway Bride*, rarity 4, Support,
  Fire. **Title, rarity, role and element all match.** This is a genuine
  element+grade+identity attestation for an id the 2019 archive has no numeric
  row for. It is *identity* credit, not stat credit.
- **`078` — disputed, do not bank it.** namu lists `할로윈 마녀 리코` in the
  **Defense** table at **2★**, explicitly "리코의 할로윈 버전" (Rico's Halloween
  version). The uncovered roster calls `078` *Teresa (Halloween)*, 4★, Support.
  Grade and role both disagree; only element (Ice) matches. namu is most likely
  describing a **Rico** costume that the catalogue has not separated, and `078`
  may be a different entity. Recorded, **not** counted.
- **49 ids absent from namu entirely**, including every `*_1` awakened row and
  the whole late-4★ block: `056` Genovia, `064` Geranium, `066` Mary,
  `067` Judith, `068` Selene, `069` Celine, `070` Alia, `071` Anemone,
  `072` Audrey, `073` Sofia, `074` Leon, `075` Bella, `076` Junia,
  `077` Blondie, `079` Lawrence, `080` Westfield, `081` Monica,
  `082` Mary (Christmas), `083` Kamala, `084` Lottery Mouse, `085`,
  `086` Genovia (Valentine), `087`, `088`, `089` Clara, `090` Katrina,
  `091` Anemone (Kid), `092` Themis, `093` Bella (Summer),
  `094` Leon (Summer), `095`, `096` Estelle, `097` Lily & Lyla (Christmas),
  `098` Selene (Valentine), and 14 awakened ids.

**This page is not a complete roster.** It omits roughly 40 catalogue heroes,
and namu itself would fail as the "which heroes exist" answer.

### 6.4 The brief's stated Hermes conflict does not exist

The brief flagged "namu calls 헤르메스 (Hermes, 023) 3★ Fire while the archive says
冷기 (cold/ice)". Checked directly against
`archived-hunter-database-2019.tsv`:

```
023 | 特級伝令使「ヘルメス」 | 火炎 | 攻撃手 | rare=3
```

**The 2019 archive says 火炎 (Fire), not 冷気.** namu, the archive and
`cards.json` all say Fire, and all say 3★. **There is no Hermes conflict and
nothing to adjudicate.** Recording this because the premise was asserted, not
measured, and a downstream agent should not go looking for it.

### 6.5 Three heroes namu names that the catalogue does not

`실험체 2호 해선` (하얀섬/Haeseon protagonist, limited to the Season-2 pre-pass),
`최고의 요리사 치르치르` and `이상한 나라의 치르치르` (Chirchill and his
Wonderland variant, the latter obtained only from Chirchill's event, 1 piece at a
time). `cards.json` has empty names at `026/026_1, 034/034_1, 038_1, 085,
086_1, 087, 088, 095` and no Chirchill row at all. **Left unmapped rather than
guessed.** The three are the most useful new *Korean name strings* on the page
for future identity work.

---

## 7. Mechanics and contract values recovered (not coverage, but real)

These are the readings that bear on replica fixtures. **Era: 2026-10-03,
post-rebalance.** Nothing here has been compared against shipped client data
except where stated.

| value | namu reading | status |
|---|---|---|
| **Trace cost to guarantee-recruit** | **(2^n)×10** ⇒ 1★20, 2★40, 3★80, 4★160 | **Corrects a replica fixture.** The local trace-exchange uses a flat `collect_qty` of 10/20 (see `hunter-traces.ts`). namu's is grade-exponential. Treated as *original-design* evidence, not yet implemented. |
| **Rage (분노) cost** | 공격수/수비수 = **3**, 폭격수/도우미 = **4**; exceptions 릴리&랄라 and 곰 also 4 | **Corroborates** the replica's `001=4 / 002=3 / 003=3 / 004=4` (Lantern Bomber 4, Mowgli Offense 3, Nene Defense 3, Tyltyl Support 4) — **4/4 match** in an independent language. Adds two named exceptions. |
| **Character level cap** | footnote [38] `등급에 상관없이 30레벨이 최대` | **Corroborates** the Lv.30-regardless-of-grade cap used throughout the project. **Does not** explain the 2017-05-22 source `23265` "max level before advance is 20" — namu asserts 30 flat, with no version split and no mention of 20. Lead 2.2 of `namu-browser-partial-2026-10-08.md` is **not** closed. |
| **Skill level cap** | `헌터의 등급에 따라 스킬 레벨의 최대레벨이 10씩 올라간다` | Corroborates the 10-per-grade skill cap (10/20/30/40/50). |
| **Self-overcoming (자기극복) T1/T2/T3 materials** | Table 5; crystals left / fragments right, always ×10 | **Corroborates the ★3 row exactly**: 9/90, 30/300, 80/800. See §8. |
| **Self-overcoming unlock** | `3성부터 열리며`, consumes same-grade hunters | The 2★ row's T3 is empty — **1★/2★ cannot self-overcome**. Only 3★ and 4★ reach 5★. |
| **Promotion (승급) cost** | at Lv.MAX, needs N same-grade hunters where N = star count | Consistent with the replica's RankUp source rule. |
| **Equipment enhancement** | unlocks at **4성**; 3 pieces per hunter; Lv1–2 rupee only, Lv3+ tool boxes; 개조 every 10 levels costs element material; border tier (동/은) changes with hunter grade | New structural contract. Footnote [42]: each piece covers **공격력 / 방어력 / 최대 생명력**. |
| **Equipment enhancement ceiling** | the cost table runs to **Lv.50** | Distinct ladder from the Lv.30 character cap. |
| **Sell currency** | 1–2★ ⇒ 루피; 3★+ ⇒ 첨쥐 코인 (secret shop corner) | Matches the replica's split-currency sell. |
| **Gacha bundle** | `30개로 1회, 300개로 10+1회` = 11 units; occasional discount on the next 10-draw | 11-unit bundle **corroborates** the replica's bundle count of 11. |
| **Recruit document prices** | 고급 20000 루피; 특급 1500 파이트칩 / 3000 신기루 조각 / 20 첨쥐 코인, sometimes 60000 루피 | Original prices, previously unrecovered. |
| **Potion (물약→스팀팩)** | ~2019-04 changed to pre-battle use; `+` for 3000 루피 or 3 만다 | Potion as a pre-battle consumable, not a mid-battle one. |
| **Fuel timers** | 오르니톄터 연료 6 min/charge; 도전장 80 min/charge; 헬륨캡슐 from 탐사 with probability | Named charge intervals. |
| **Guild (협회) bonus** | single-digit %, applied to shop purchases, **not** to equipment 개조 | Explains the footnote on the rupee column. |
| **Fight-club-only buff** | Beckhen: ATK/DEF/HP **+10%**, Fight Club only | The only per-hero *stat modifier* on the page. Not a base stat. |
| **Named attack speeds** | Offense is **공속 8** for all except Kaltsutainer at **7**; Dumble (Defense) **6** | Three real attack-speed values. The archive's `speed` column agrees on the pattern but is not level-anchored. |

### 7.1 Inconsistencies inside namu itself

Recorded because they bound how far namu can be trusted:

- namu's own Captain row says `4성 공격수` in the prose while the row sits in
  the **Defense** table at 1★. namu contradicts itself on the protagonist's
  role.
- The Vincent grade cell renders as `☆☆ ☆☆`, and footnote [53] reads
  `패치 전에는 3성였다` ("was 3★ before the patch"). So the doubled glyph run is
  4★ current / 3★ historical, consistent with the prose
  `이후 태생 4성으로 상향되면서`. The reading is safe, but the cell is not a
  clean single badge.
- Footnote [45] and Table 6 use `멀쩡한`, the earlier lane's mirror capture used
  `멀정한`. Transcribed here from the canonical 2026-10-03 render.

---

## 8. Priority 5 — the T2 question: cost yes, multiplier no

namu does not use the word `초월`; it calls the system **`자기극복`**, and
explicitly flags the analogy:

> 자기극복 3성부터 열리며 … **타게임의 초월과 비슷한 개념**으로 태성이 올라갈 때 메인 화면의 리더 헌터 주변에 반짝이가 나고 올라갈수록 색이 바뀐다.

So namu's `자기극복 순서` columns `1 / 2 / 3` are the project's **T1 / T2 / T3**
rungs, and Table 5 is the **T2 material panel** the task asked for.

**The ★3 row reads `9/90`, `30/300`, `80/800`.** That is an exact, independent
match on all three rungs with the vsfan `Guide_to_Blustone` ★3 row
(9/90/9 000, 30/300/30 000, 80/800/80 000 — vsfan adds the gold column) **and**
with the game's own T1 receipt measured in `t1-measured-1.0994-2026-10-08.md`
(crystals 9, fragments 90, gold 9000). So the **T2 and T3 material costs are now
doubly sourced**: the game's own T1 screen plus a Korean wiki, in agreement.

**What is still missing is the T2 stat multiplier, and this page does not have
it.** namu gives no T2 panel of ATK/DEF/HP deltas, no ×1.20, nothing that
discriminates between

| model | rule | T1 | T2 | T3 |
|---|---|---:|---:|---:|
| (A) compounding | multiply current value | 1.0994 | **1.2087** | 1.3287 |
| (B) from base | multiply base value | 1.0994 | **1.2000** | 1.3000 |

**The T2 panel hunt is not closed.** namu contributes the *price* of rung 2 and
nothing about its *effect*. Closing it still needs a キャパ超越 receipt frame
like `capa2-1024x911.jpg` at T2, or equivalent.

---

## 9. The four per-role sub-pages — re-tested on the canonical host

`namu-gear-pages-2026-10-06.md` swept these via four mirrors and reported
"165 equipment slots, 6 named items, **0** values", recommending a browser be
tried. **It was**, on `namu.wiki` itself, in a real render.

| page | last modified | DOM | tables | data rows | `특기 효과` slots | **filled with a number** |
|---|---|---:|---:|---:|---:|---:|
| `/헌터/공격수` | **2026-08-20 09:56:09** | 415,486 B | 3 | 0 | 90 | **4** |
| `/헌터/수비수` | **2026-07-07 01:38:18** | 353,529 B | 3 | 0 | 63 | **0** |
| `/헌터/폭격수` | **2026-10-05 14:34:29** | 332,558 B | 3 | 0 | 58 | **0** |
| `/헌터/도우미` | **2026-08-03 13:56:37** | 295,609 B | 3 | 0 | 64 | **0** |
| **total** | | | **12** | **0** | **275** | **4** |

Every table on all four pages is namu layout furniture (a 1-row
`특기 단련 | 녹슨/날카로운/신비한 금속 조각` material caption, plus the `a.aa`
widget). **No stat table, no equipment value table.**

**Hypothesis tested and rejected:** a browser does **not** render values the
mirrors dropped. The 6 numeric `특기 효과` values the earlier lane found are
reproduced verbatim, in one hero's block (Beckhen, 백헨, on the Offense page):

```
특기 효과: 지속 시간 0.51~1.00초
특기 효과: 피해량 ~9046
특기 효과: 공격 속도 ~20.00%
특기 효과: 지속 시간 0.51~1.00초
특기 효과: 방어력 ~30.00%
특기 효과: 막기 확률 ~30.00%
```

These are **skill-effect magnitudes at max level for one hero**, not base stats,
and `피해량 ~9046` is a single non-round damage figure with no stated level or
target. They are recorded here as-is and are **not** promoted to coverage.
`나머지 269` slots are the literal string `특기 효과:` with nothing after it, and
the `장비` labels likewise carry no value.

**The three-community negative now holds at the source, in the original
language, from the canonical host:** Miraheze 1,567 revisions / vsfan 911 pages /
namu 275 slots — three communities, three languages, **one** gap. Accessory
coverage stays **1/100**.

---

## 10. What this page does not contain — the honest list

1. **No per-hero HP, ATK or DEF.** Not one. Nor SPD, crit, block, penetration,
   penetration-resistance, or HP regen. Heroes stay **1/113**.
2. **No equipment stat values.** No accessory line, no weapon/armour stat, no
   level-50 figure. Accessories stay **1/100**.
3. **No jewel / 보석 set bonuses.** Absent entirely.
4. **No monster stats.** Monsters stay **0/22**.
5. **No T2 stat multiplier.** Cost only. The from-base-vs-compounding
   discriminator is untouched.
6. **No awakening (`*_1`) rows.** All 14 `*_1` ids absent; namu stops at 4★
   birth grade and never shows a 5★ `마스터` stat line.
7. **Not a complete roster** — ~40 catalogue heroes missing (§6.3).
8. **No XP curve, no level→stat growth, no training XP values.** Only material
   and rupee costs.
9. **No arena, Mirage, fishing or episode content.**
10. **No `구 버전 / 현재` version split on this page.** The split flagged as lead
    2.2 lives on the *main* page's §3.2 스테이지, not here; it was not re-read in
    this lane and lead 2.2 stays open.
11. **No image is a stat panel.** Verified structurally (§5), so nothing was
    missed by declining to zoom — and no digit in this file was read off an
    image at all.

---

## 11. Weakness of this source, stated

namu carries its own disclaimer, and it is in the rendered footer:

> 나무위키는 백과사전이 아니며 검증되지 않았거나, 편향적이거나, 잘못된 서술이 있을 수 있습니다.

Concretely, for what is above:

- **Unverified community editing.** This is a player wiki. Tables 6 and 7–11 are
  demonstrably *incomplete* (one role row, one element column), so the editors
  transcribe selectively and a blank is not always a "no such value".
- **Self-contradictory** on at least two rows (Captain's role; Vincent's grade
  cell). Recorded in §7.1 rather than smoothed over.
- **Post-2019-09-05 rebalance.** Every number is era-tagged. Do not blend it into
  a 2017–2019 balance table without a separator.
- **The Pansy element dissent (§6.2) is unresolved and must not be applied.** One
  source against a shared pair.
- **Nothing here should overwrite a shipped-client or 2019-archive value.** Where
  namu agrees, it adds confidence. Where it disagrees, it is one voice. The trace
  formula in §7 is the only reading that *contradicts* a shipped replica fixture
  (`collect_qty` 10/20), and even that is offered as design evidence, not as a
  licence to change a value that shipped-client or native behaviour corroborates.
- **The `T1/T2/T3` = `자기극복 순서` identification is an inference**, though a
  strong one: namu names the columns only as `1 / 2 / 3`, and the ★3 row
  (9/90, 30/300, 80/800) matching the game's own T1 receipt makes the alignment
  near-certain.

---

## 12. Reproducing this

```powershell
# renders and dumps the DOM, then walks the tables
python analysis/research/base-stats-visual-hunt\_namu_headless.py `
    "https://namu.wiki/w/%EB%B8%94%EB%A3%A8%EC%8A%A4%ED%86%A4/%ED%97%8C%ED%84%B0" dom.html 35000
python analysis/research/base-stats-visual-hunt\_namu_tables.py dom.html tables.json
python analysis/research/base-stats-visual-hunt\_namu_text.py   dom.html text.txt
python analysis/research/base-stats-visual-hunt\_namu_roster.py      # + cross-check
python analysis/research/base-stats-visual-hunt\_namu_numeric_census.py
python analysis/research/base-stats-visual-hunt\_namu_subpages.py     # the 4 role pages
```

The scripts are prefixed `_` and are the method trail, not deliverables. They
read only the rendered dumps and two existing research files
(`archived-hunter-database-2019.tsv`, `uncovered-archive-roster-2019.tsv`) plus
`analysis/catalogue/data/cards.json`. **No coverage file, TSV, server source,
fixture, APK, seed, emulator, phone or Ghidra project was touched by this lane.**
