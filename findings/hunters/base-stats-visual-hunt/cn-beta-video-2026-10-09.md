# CN-server beta playthrough — deep pass (2026-10-09)

**Lane:** the single most promising unfinished artefact from the Chinese hunt —
`av38052023` / `BV12t411v71Y` 《国服疾风小侠公测试玩》, uploaded **2018-12-13**.

**Verdict up front, three parts:**

1. **The artefact was broken and is now whole.** The copy the previous lane
   called "1796.1 s, decoded" is a **40.96 % truncated download**. I completed
   it. **1070 s of gameplay that no one had ever looked at** turned out to
   contain two of the most stat-bearing screens in the video.
2. **A real, controlled CN-beta balance result:** 战斗力 (combat power) is an
   **exact linear function of level** for a fixed hero —
   `战力 = 293 + 7 × (level − 1)` — verified on **four** levels (1, 2, 4, 8)
   with **zero residual**.
3. **The headline target is still a negative.** Across **every second of all
   1796 s** the video contains **no HP/ATK/DEF panel and no equipment screen**.
   Hero coverage stays **1/113**; accessory coverage stays **1/100**. This is a
   *controlled* negative (see §3), not an unsearched one.

---

## 0. Headline correction: the file was truncated

The previous lane recorded this video itself as a failure and then used it as
if it were complete. Both records are in its own log
(`%TEMP%\opencode\zh\vids\_dl.json`):

```json
{"aid":"av38052023","ok":false,"bytes":0,
 "error":"ChunkedEncodingError: ('Connection broken:
   IncompleteRead(2514471 bytes read, 515802410 more expected)'…)",
 "expect_bytes":518316881,"timelength_ms":1796100}
```

`bytes: 0`, `ok: false` — and yet the notes table lists
"212 205 568 | 1280×720, 1796.1 s" as a *decoded* video.

**Container probe** (`cnbeta-container-probe.py boxes`) settles it:

| box | offset | size | ends at | complete |
|---|---:|---:|---:|---|
| `ftyp` | 0 | 32 | 32 | yes |
| `moov` | 32 | 2 288 413 | 2 288 445 | yes |
| `mdat` | 2 288 453 | **516 028 428** | 518 316 881 | **NO** |

The file on disk is **212 205 568 B**. The `mdat` header demands
**518 316 881 B**. The `moov` is complete and `faststart`-style, so `ffprobe`
happily reports `duration=1796.1` and `nb_frames=53831` — **all of that is
container metadata, not decodable pixels.**

Decodable extent, measured not assumed:

```
ffmpeg -i … -vf fps=1  →  727 frames, then
[in#0 @ …] stream 0, offset 0xca60325: partial file
ffmpeg -f null -       →  thousands of "non monotonically increasing dts"
```

**212 205 568 / 518 316 881 = 40.96 %.** The prior lane's own frame directory
for this video holds 182 JPEGs spanning **t = 20…724 s** — it never had the rest
of the video and could not have.

The report's "511 frames were extracted at 4 s granularity" was **across the
whole corpus**, not this video. Per-video it was 182 frames over 40 % of the
runtime. Its "currently dialogue-only in its frames, but complete and
re-analysable" was wrong on both counts: not complete, and dialogue was only
40 % of the story.

### 0.1 Completion

`cnbeta-resume.py` — the prior lane's own recorded method (resumable 512 KiB
ranged slicing under the documented 1 MiB CDN cliff, one `requests.Session`,
`Accept-Encoding: identity`, `playurl` re-sign on stall). The truncated original
was **copied, never mutated**, so the truncation evidence survives.

```
start have=212205568 / 518316881  (40.94%)
…
stopped: have=518316881 / 518316881 (100.00%) after 1897s
sha256(518316881 B) = 779e73479249c1525a5ca79fc89450e16688cd67edfca6e069f49d5640cd79db
```

Verified after completion: `nb_frames=53831`, `duration=1796.1`,
`size=518316881` — the container's claims and the bytes now agree.

---

## 1. Structure and instrumentation

### 1.1 The video is pillarboxed — this halves effective resolution

The stream is 1280×720, but the recording is a **portrait phone**. Measured
active region (`cnbeta-activebox.py`, 11 sample frames):

| | value |
|---|---|
| container | 1280 × 720 |
| **active game region** | **818 × 720** at offset `(436, 0)` |
| pillarbox | 436 px each side = **68 % of the frame is black bar** |
| control: bar mean luminance | 0.5–1.1 |
| control: active-region mean luminance | 19.8–107 |

Reading digits off the raw frame wastes two-thirds of the image. **Every crop in
this note is taken from the active region and scaled ≥ 4×.**

### 1.2 Instrument bugs caught before any zero was recorded

Three real defects, each found by a control rather than by inspection:

1. **The prior lane's frame extractor never worked.** Its
   `frames/av38052023_*/f_%06.1f.jpg` is a **literal filename** — `%06.2f` is
   not a valid image2 pattern, so ffmpeg wrote **1** frame and errored. The
   `t%06.2f.jpg` files beside it came from a different, per-timestamp pass.
2. **`np.asarray(PIL_image)` returns a view into a buffer freed on close.**
   Reading features inside a `with Image.open(...)` block produced
   `mean` luminance collapsing to ~0.004 on frames that were plainly not dark.
   No exception; a silent wrong measurement. Fixed to `np.array()` (a copy) and
   re-verified: real frames measure 30–108.
3. **`bilibili` search's discriminator key is `result_type` (snake_case).** My
   first parser used `resultType` (camelCase); the key does not exist, so every
   block was skipped and a healthy API returned a flawless-looking zero. Only
   the control query caught it.

Feature controls, re-run after the fix (all six non-degenerate):
`mean 0.61–125.09`, `edge 0.0039–0.1077`, `pale 0.0008–0.4971`,
`darkbot 0.5037–1.0`, `textrows` 21–141, `uniq` 92–13 163.

---

## 2. What the video contains

29 non-black scenes in t=0…726 (scene-cut segmentation on full-black fades),
plus a continuous second half. **126 contact sheets** built from the cropped
active region, **0 undecodable cells**.

| span | content |
|---|---|
| 0–200 | story dialogue, two tutorial battles, one result screen |
| 200–330 | party-exchange tutorial, more dialogue and battles |
| 330–470 | long story scene, expedition map, **login-reward screen** |
| 470–570 | **gacha → 详情信息 detail screen → player-feedback panel** |
| 570–727 | long battle sequence with skill cut-ins, prep screen |
| **727–1150** *(never seen before)* | further battles, **two more result screens** |
| 1150–1400 | battles, story dialogue |
| **1400–1460** *(never seen)* | **训练队员 — the training screen** |
| 1460–1700 | dialogue, village, **quest list with reward quantities** |
| **1700–1796** *(never seen)* | **寻找猎人 Find-Hunter trace screen + 聘请猎人 gacha banner** |

It is a **beta first-session playthrough**: tutorial, ~8 story conversations,
several Snowfield stages, a first gacha pull, village/Hunter-List navigation,
one training action, and the recruitment menus. **It is not a gear showcase**,
which is exactly why the negative in §3 is believable.

---

## 3. THE HEADLINE TARGET: a controlled negative

**No HP/ATK/DEF stat panel exists anywhere in 1796 s.**

Coverage is complete by construction: **frames extracted at 1 Hz across the
entire runtime** — t = 0…726 (727 frames) and t = 700…1795 (1096 frames),
union **t = 0…1795 = every single second, 1796 frames**.

Three screens come closest, and all three fail the project's gear classifier:

### 3.1 详情信息 "Detail Information" — t = 536…544 s

The only screen in the video whose title is a stat-panel title.

| field | reading |
|---|---|
| title | 详情信息 |
| name | 顶尖厨师 / **蒂希尔** (Tishil) |
| type + element | two badges only (no text) |
| **战斗力** | **210** |
| level | **Lv. 1** |
| grade | 新手猎人 ("Rookie Hunter") |

**Gear classification: N/A — this is not a stat panel.** It contains **no
HP/ATK/DEF**, **no 基本能力値 block**, and **no equipment slots are displayed at
all** (so "visibly empty" cannot even be asserted — the widget is absent). It is
a roster summary card: identity, two badges, one composite rating, level, grade.

Under the adversarial heading rule this is doubly disqualified: the heading
`详情信息` is not `基本能力値`, and the one number it carries is a composite.

### 3.2 Post-battle result screens — t = 705 s and t = 1100 s

Per-hero **Lv + 战斗力**, three star conditions, gold and item rewards.
**No HP/ATK/DEF, no equipment slots, no level gauge.** Per the coverage
definitions these are composite ratings, not base tuples.

### 3.3 训练队员 "Train Member" — t = 1420…1450 s

**战斗力上升 370 → 497**, a consumed source card, **训练 cost 0**.
The original training screen with its **source-is-consumed** rule stated on
screen: 被选择为训练对象的猎人会消失 ("the hunter chosen as a training target
will disappear"). No HP/ATK/DEF, no equipment slots.

**Result: heroes stay 1/113, accessories stay 1/100, monsters stay 0/22.**
No reading from this video moves a coverage counter. Per the task rules
everything below stays in UNPURIFIED unless identity, level **and** gear state
are all established — for the 战力 readings, **gear state is never established**,
so they are polluted observations by construction, not base coverage.

---

## 4. The one genuinely strong result: 战斗力 is exactly linear in level

Four readings of **the same hero** (blond, gold/yellow element badge) at four
levels, taken from three different scenes, at 5×–7× zoom:

| level | 战斗力 | timestamp | shot |
|---:|---:|---|---|
| 1 | **293** | t = 85 s | `claim-C08-power-pre.png` |
| 2 | **300** | t = 87 s | `claim-C09-power-post.png` |
| 4 | **314** | t = 705 s | `claim-C05-victory-heroes.png` |
| 8 | **342** | t = 1100 s | `claim-C18-victory3-heroes.png` |

Fit `战力 = 293 + 7 × (level − 1)`:

```
Lv 1 -> 293.0   observed 293   residual 0
Lv 2 -> 300.0   observed 300   residual 0
Lv 4 -> 314.0   observed 314   residual 0
Lv 8 -> 342.0   observed 342   residual 0
```

**Exact, zero residual, across levels 1→8.** The t = 87 s frame also shows the
game's own delta glyph **▲ 7**, i.e. the client agrees with the fitted slope.

This is a **clean, self-consistent CN-beta balance statement**: for a fixed hero
with no gear change, the composite rating rises **exactly +7 per level**.

**What it is not.** It does **not** license a CN-vs-global balance claim
(§6), and it says nothing about HP/ATK/DEF — the project's own
`t1-measured-1.0994` already proved 战力 is not linear in the three stats. That
a composite can be linear in *level* while non-linear in the underlying stats is
expected and consistent: the stats themselves grow linearly with level.

**And power is emphatically not a function of level alone across heroes.** In
one frame (t = 1100 s, 6× zoom) three heroes read **Lv. 8 → 342**,
**Lv. 5 → 226**, **Lv. 2 → 713**. A Lv. 2 out-rating a Lv. 8 by 2× means the
composite is hero-specific — grade and gear state dominate. That is precisely
why these cannot become base tuples.

---

## 5. Every stat-bearing frame, with timestamps

All at ≥ 4× zoom of the active region. **Gear column** per the project's rule:
a panel is gear-free only if equipment slots are *visibly empty*.

| # | t (s) | screen | readings | gear class |
|---|---|---|---|---|
| 1 | 85 | result screen | hero **Lv. 1**, **战力 293** | no gear slots shown → **not gear-free** |
| 2 | 87 | result screen | hero **Lv. 2**, **战力 300**, **▲ 7**, 队伍等级 1 | no gear slots shown |
| 3 | 87 | result screen | 获得卢比 **+ 47**, 下一地区 | — |
| 4 | 116 | battle HUD | enemy **450 ×2**, ice badge; ammo **0**, coin **24** | n/a (wave bar) |
| 5 | 449 | login reward | **第1天 卢比 ×10000**; 第2天 稀世越狱犯 芭比蝶; 第3天 芭比蝶的痕迹 **×10** | n/a |
| 6 | 449 | result screen | 获得卢比 **+ 30** (earlier frame, same scene) | — |
| 7 | 536–544 | **详情信息** | 蒂希尔, **战力 210**, **Lv. 1**, 新手猎人 | **no equipment widget at all** |
| 8 | 665 | battle HUD | enemy **562 ×6** | n/a |
| 9 | 671 | skill cut-in | **料理治愈法** ("Culinary Cure"), enemy **428 ×4** | n/a |
| 10 | 683 | skill cut-in | **闪电击** ("Lightning Strike") | n/a |
| 11 | 705 | result screen | **Lv. 4 → 314**, **Lv. 1 → 210**; 队伍等级 **2** | no gear slots shown |
| 12 | 705 | result screen | stars **任务完成 / 60秒以内完成 / 全体生存** (all gold) | — |
| 13 | 716 | 战斗准备 | 米德加尔特雪原 **第2区**, ★★★, **AP 97/61**, 战斗开始 cost **6** | — |
| 14 | 716 | 战斗准备 | **我方队员 536 VS 预想敌军 860** | — |
| 15 | 716 | 战斗准备 | enemy levels **5 / 5 / 10**; player **5 / 2** | — |
| 16 | 1100 | result screen | **Lv. 8 → 342**, **Lv. 5 → 226**, **Lv. 2 → 713**; 队伍等级 2; 卢比 **+57**; item **×2** | no gear slots shown |
| 17 | 1125 | battle HUD | enemy **1125 ×5** | n/a |
| 18 | 1130 | battle HUD | enemy **1047 ×4** | n/a |
| 19 | 1135 | battle HUD | enemy **741 ×4** | n/a |
| 20 | 1420–1450 | **训练队员** | gold **11027**, 战力上升 **370 → 497** (t=1450: → **503**), 训练 cost **0** | no gear slots shown |
| 21 | 1445 | training sources | **Lv. 9 → 242**, **Lv. 5 → 738**, both 探险中 | — |
| 22 | 1695–1720 | quest list | 追讨达成奖励 **0/7 → 1/7 → 4/7**, rewards **×5 ×1 ×20**; 确认出庭 **×1000**; 完美地区 **×30**; 获取活动奖励 **×5**; 特殊训练 **×10**; 购买商品 **×1000**; 我是爱的重大伤痕 **10/10**, …采薇… **60/100** ⚠ | — |
| 23 | 1735 | **寻找猎人** | 攻击手 **1/1**, bonus **1.0%**, per-hero thresholds **0/160**, **0/80** | — |
| 24 | 1745 | **聘请猎人** | 聘请 **30** (single), 聘请 **10+1 = 300**, badge **★2 1名或以上 100%确定** | — |
| 25 | 1750 | 收取猎人痕迹 | **1次投票 ×1**, **4次投票 ×4** | — |
| 26 | 1785 | village | gold **33027**, item **12** | — |
| 27 | 1790 | village | AP **166/61**, tickets **6/6** | — |

⚠ = row 22 was read from a contact sheet, **not** re-verified at zoom; treat
those particular figures as unconfirmed. Every other row is backed by a named
`claim-C*.png` / `still-*.png` at ≥ 4×.

### 5.1 Two systems the project has not previously characterised

- **寻找猎人 "Find Hunter" (t = 1735 s)** — a trace-based recruitment screen:
  *"收集痕迹聘请新的猎人"* (collect traces to hire new hunters), a per-role
  progress **1/1**, a **1.0 %** bonus, and **per-hero trace thresholds**
  (**0/160**, **0/80**) with a 获得资讯 ("obtain intel") button per card.
  Nine named heroes are listed (Lv. 1, grayscale/unowned). This is a distinct
  axis from `/shop/PieceExchange` in the replica.
- **聘请猎人 "Hire Hunter" (t = 1745 s)** — the gacha banner, with
  **single 30** and **bundle 10+1 for 300**, and a guarantee badge
  **★2 1名或以上 100%确定** ("100 % guaranteed at least one ★2"). This
  **independently corroborates the project's 30 / 300 prices** from a completely
  independent source, and the 10+1 bundle shape, on the **CN-beta build**.

---

## 6. CN-beta balance differences

**No CN-vs-global divergence is established, and none is claimed.**

What *can* be said:

1. **Era.** Uploaded 2018-12-13, and the in-game feedback panel (t ≈ 553 s)
   carries player timestamps of **2018-12-12 / 2018-12-13**. This sits
   **before the 2019-09-05 rebalance** (`stat-version-context.md`), so every
   reading here is **pre-rebalance**.
2. **The third star condition differs.** The CN beta shows
   **任务完成 / 60秒以内完成 / 全体生存** (mission complete / within 60 s /
   **all survive**). The project's 2.8-era capture shows
   *Mission Complete / Under 60s / **1 Straggler or Less***. The third condition
   is **全体生存** here. This may be a beta-era change or a per-stage condition
   set; one frame cannot distinguish those, and I did not chase it.
3. **Over-cap fuel is visible**: **97/61** (t = 716 s) and **166/61** (t = 1790 s).
   Independent corroboration of the overflow display.
4. **Why no divergence claim.** A CN-vs-global comparison needs the *same* hero
   at the *same* level in both builds with gear separated. This video supplies
   the CN side only. The archive's 战力 values carry `level: not shown` on
   63/63 rows, so they cannot be joined to these levels. Comparing 210–738
   (beta, early game) against the archive's 8000-range would be meaningless.

---

## 7. Controlled negatives: what this video does *not* contain

Each is a real negative because the instrument is positively controlled:

| absent | control proving the search would have found it |
|---|---|
| **HP / ATK / DEF stat panel** | 详情信息 opened at t = 538 s and read at 5×; the `pale`/`edge` screen triage ran over all 1796 frames and its top-ranked candidates were all inspected |
| **equipment / accessory screen** | the same; no frame in 1796 s shows an equipment slot, an inventory grid, or an item thumbnail list with stat rows |
| **T2 transcendence panel** | not present; consistent with the prior lane's negative, now on the **full** runtime rather than 40 % of it |
| **level/EXP cost table** | the training screen (t = 1445 s) shows **训练 cost 0** with the cost carried by the consumed source, not a gold table; no EXP curve appears anywhere |
| **gacha rate table** | the gacha banner gives **prices and a guarantee badge**, never percentages |

---

## 8. The other two open leads: both instruments still broken

### 8.1 QooApp — still an instrument fault, not a content negative

| request | status | bytes |
|---|---|---|
| `/search?q=疾风小侠` (the CN title) | **500** | 785 |
| `/search?q=zzq9x7notarealgame` (nonsense) | **500** | 785 |
| `https://www.qooapp.com/` (homepage) | **500** | 785 |

**Identical response for a real query, a nonsense query and the homepage.**
That is the signature of a dead origin, not of absent content. The avenue stays
**open, not closed** — exactly as the prior lane correctly recorded.

### 8.2 bilibili search — **newly broken; the prior lane's corpus method no longer validates**

This is the instrument that carried the entire Chinese hunt. Its control was
`明日方舟` → 78 rows, *plus* the observation that transliterations
(`布路斯通`) return unrelated results — i.e. it **demonstrably filtered**.

**It no longer filters.** Measured:

| query | rows | sha1(aids) |
|---|---:|---|
| `明日方舟` (must return thousands) | 20 | `d5c7f076b666` |
| `zzq9x7notarealgame` | 20 | `c094ad5f6d26` |
| `qqzzxx99887` | 20 | `3704f5f521e3` |
| `疾风小侠` | 20 | `f146b488adbc` |
| `Blustone` | 20 | `e7e2b85c9913` |

**Pure gibberish returns 20 plausible video rows**, with **0/20 overlap** with a
real query's results. The endpoint is serving a generic feed.

**Consequence:** a naive re-run produced **175 unique aids, 173 "not already
downloaded"** — and reading their titles shows they are content-farm noise:
疾风小侠 as a ship name in 碧蓝航线/明日方舟, 青石 as a *gemstone* and a
*stone-cutting* business, 装备 as *outdoor gear*, plus NSFW and fishing spam.
**I report zero of them as leads.** Any future bilibili search must carry a
**negative control on gibberish**, which the prior lane's method did not.

---

## 9. Coverage summary

| | |
|---|---|
| container | 1280×720, portrait phone pillarboxed, **active 818×720** |
| runtime examined | **1796.1 s = 100 %**, at **1 Hz** |
| frames extracted | **1796** (727 from the old file + 1096 from the completed file, 27 s overlap) |
| contact sheets built | **126** (98 first half + 28 tail), **0 undecodable cells** |
| claims re-verified at ≥ 4× zoom | **21** |
| scenes classified | 29 (first half) + full continuous pass (tail) |
| frames the prior lane had | 182, covering 40 % |

**Coverage counters unmoved: heroes 1/113, accessories 1/100, monsters 0/22.**

---

## 10. Artifacts written

Frames and sheets are in `analysis/research/base-stats-visual-hunt/cnbeta-frames-2026-10-09/`
(284 files, 63.4 MB):

- `SCENE-OVERVIEW.jpg` — one frame per scene, all 29
- `sheets-crop/` (98) — first half, active-region crop, timestamp-labelled
- `sheets-tail/` (28) — the never-before-seen half
- `claim-C*.png` (21) — every numeric claim at ≥ 4×, captioned with t, crop rect, scale
- `still-*.png` (16) — full-resolution active-region stills
- `findings.tsv`, `scenes.csv`, `frame-features-1hz.csv`, `frame-change-1hz.csv`,
  `frame-features-tail.csv`, `active-box.txt`

Scripts (read-only against the video; they write only under `%TEMP%` and the
frame folder): `cnbeta-extract.py`, `cnbeta-container-probe.py`,
`cnbeta-resume.py`, `cnbeta-triage.py`, `cnbeta-map.py`, `cnbeta-scenes.py`,
`cnbeta-sheet.py`, `cnbeta-activebox.py`, `cnbeta-locate.py`,
`cnbeta-rows.py`, `cnbeta-claims.py`, `cnbeta-tail-triage.py`,
`cnbeta-tail-sheet.py`, `cnbeta-followups.py`.

**Not touched:** `coverage.md`, `polluted-observations.md`, any TSV, `README.md`,
`server-ts`, fixtures, APK, seeds, emulator, phone, Ghidra. The completed video
lives in `%TEMP%\opencode\cnbeta\`; the truncated original was copied, not
modified.