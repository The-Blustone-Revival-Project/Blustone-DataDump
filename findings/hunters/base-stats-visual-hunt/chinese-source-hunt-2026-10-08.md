# Chinese-language source hunt — 2026-10-08

**Lane:** the first systematic pass over Chinese sources. Everything else this
project has mined is Japanese, Korean or English.
**Verdict up front:** Chinese sources yield **real but shallow** material — a
confirmed Chinese localization, a handful of hard economy/UI numbers, and a
**documented negative on both headline targets**. No coverage counter moves.

| target | outcome |
|---|---|
| **1. Equipment / accessory stat lines** | **NEGATIVE.** No Chinese source transcribes accessory values. Accessory coverage stays **1/100**. |
| **2. T2 transcendence observation** | **NEGATIVE.** No Chinese T2 panel exists either. The word 超越 was found in *promotional copy*, not a stat panel. |
| **3. Per-hero base stats** | **NEGATIVE for base tuples.** Heroes stay **1/113**. Some 戰鬥力 (power) readings were recovered — all composite, all polluted. |
| **4. Any numeric table** | **PARTIAL POSITIVE.** Recovered a small set of real, dated Chinese economy/UI numbers (§5). Includes a shop-purchase **1600 %** bonus reading and an event banner with a **4★×3** hiring-card offer. |

---

## 0. Method and instrument state (read this before trusting any zero)

Every negative below was gated on a **positive control**. **Seven** instrument
families failed their controls (§0.1) and their zeros are therefore **void,
not negatives** — this is the project's own GUARD rule, and it fired repeatedly
enough here that most of the obvious avenues were disqualified rather than
answered. Only the one channel in §0.2 passed, and it carried the entire hunt.

### 0.1 Instruments that FAILED their control (zeros void)

| instrument | control result | why it failed |
|---|---|---|
| **bing.com / bing-cn** | **FAIL** — `明日方舟` (a query that must return thousands of results) returned `class="b_no"`, 0 result blocks, and an 854 B RSS channel containing **zero** `<item>` elements | Serves a JS-only shell to non-browser clients |
| **baidu.com / m.baidu.com** | **FAIL** — returned `网络不给力，请稍后重试` ("network weak, retry later") | Anti-bot interstitial |
| **so.com (360)** | **FAIL** — returned 6 850 B with **zero** `res-title` elements | Anti-bot interstitial |
| **sogou / 07073 / 18183 / doyo / 4399 / ali213 / 18game** | **FAIL** — 403, 404, 0 B or SSL error on the control | blocked / dead endpoints |
| **qooapp.com** | **FAIL** — HTTP **500**, 4 618 B, ASCII marker `QooApp` absent | Server-side error, **not** a content negative. QooApp was named in a video description, so this avenue remains **open, not closed**. |
| **9game AJAX** (`/tpl/pc2/search/search_result_ajax.html`) | **FAIL** — HTTP 200 but **0 B** body | The control gate correctly refused to emit a zero |
| **zh.moegirl.org.cn** | **FAIL** — CDX returned the Internet Archive's **"Temporarily Offline"** page (11 832 B) | The GUARD-18 hash-check trap, caught |

### 0.2 Instrument that PASSED and carried the whole hunt

**`api.bilibili.com/x/web-interface/search/all/v2`** — the only search channel
that (a) returns structured JSON server-side and (b) passed `明日方舟` with
**78 result rows**. It also demonstrably *filters*: `Blustone2` returns four
genuinely game-related videos while `布路斯通` and `布鲁斯通` (plausible
transliterations) return unrelated results. That asymmetry is what makes its
zeros meaningful.

### 0.3 Two new archive/transport traps found

1. **`wiki.biligame.com` is a SOFT-404 CATCH-ALL.** Four different paths —
   `/blustone/`, `/yxlm/`, `/zzzznotarealwiki12345/`, `/首页/` — all returned
   **HTTP 200, 1 402 068 B, identical sha256 `90352f0b54c9042f…`**. A naive
   "200 OK, 1.4 MB of Chinese wiki" reading would have been a rich false
   positive. **Always hash-check a biligame path against a nonsense path.**
2. **bilibili's CDN truncates at exactly 1 048 576 B (1 MiB).** A single GET dies
   with `IncompleteRead(1117739 bytes read, …)`. This looks exactly like a rate
   limit and is not one. It also *fails non-uniformly* — at the time of
   measurement offset 0/262144/524288/2097152… all served fine while
   1048576/1310720 returned 0 B or 503. Resumable 512 KiB ranged slicing with
   keep-partial plus a `playurl` re-sign on stall recovered **11 of 13**
   videos byte-exact. **Do not read a bilibili media failure as "no video".**
3. **`https://` for web.archive.org** behaved per GUARD-1 as documented: `http://`
   CDX answered normally (`blustone.jp` 200 / 678 B) while `id_` fetches at
   guessed timestamps returned 404 — consistent with GUARD-4 ("a capture set
   cannot be enumerated reliably").

---

## 1. THE headline result: the Chinese game identity

Chinese players knew this game by a **different name than 蓝色石**:

| name | where it appears | note |
|---|---|---|
| **疾风小侠** | uploader tags, video titles, CN-server beta videos | the marketed CN title; still in use as late as 2025 (in spam) |
| **青石之战** | uploader tags, description text | "Blue Stone Battle" |
| **青石** | uploader tags | short form |
| **Blustone / Blustone2** | titles, and inside the **2021-07** playthrough's own tags | international build, played by the same community |

**This is the single most useful finding of the pass.** Searching `蓝色石` alone
returns almost nothing; the CN community indexed the game as **疾风小侠 /
青石之战 / 青石**. `蓝色石` is the transliteration of the Korean title
(블루스톤), which Chinese distribution apparently did **not** use as the product
name. Any future Chinese search must use all four strings.

### 1.1 Era tags

| era | evidence | build |
|---|---|---|
| 2017-10 → 2018-08 | earliest videos (Bahamut 2017-10-13; 宣传片1 2018-08-01) | original 2017 line |
| **2018-09 → 2018-12** | 国服疾风小侠公测试玩 (2018-12-13), 【疾风小侠】超越极限 (2018-09-20) | **Chinese national-server beta** — the era with the most machine-translatable UI |
| 2019 → 2021 | 抽卡合集 (2019-03-10), 青石之戰 (2019-09-05), Blustone青石 JJC (2021-01-12) | international build, Chinese community |
| **2021-07 → 2022-09** | the 角色故事 (character-story) serial by 乛ㅂ乛 | international Blustone 2, played by a Chinese player |
| 2025-04 → 2026-06 | "T0 阵容/角色强度榜/礼包兑换码" batch | **content farm — see §6, not evidence** |

The 2018-09/12 CN beta window sits **before** the 2019-09-05 rebalance, so any
number from it is **pre-rebalance** and must not be mixed with post-rebalance
data (cf. `stat-version-context.md`).

---

## 2. The credible corpus — 36 videos found, 13 downloaded and verified

Enumeration used 26 tag/terminology queries. Full unique list is in
`bili_full.py`; the ones actually retrieved and hash-verified:

| aid | date | title (verbatim) | bytes | sha256 (16) | decoded |
|---|---|---|---|---|---|
| av15457803 | 2017-10-13 | 《Blustone》手機遊戲介紹 (Bahamut) | 87 457¹ | `1c7d701a5b89dbce`¹ | — |
| av22075032 | 2018-04-14 | Blustone各属性深渊之攻手材料8（嫖暗主版） | 3 762 941 | `9a12e768d01b1ca2` | 360×480, 76.7 s |
| av28305037 | 2018-08-01 | blustone宣传片1 | 36 039¹ | `7866339b5df2cc38`¹ | — |
| av32093561 | 2018-09-20 | 【疾风小侠】超越极限的Speed Action！ | 119 370¹ | `a4444c74d2151aa7`¹ | — |
| av35029046 | 2018-10-31 | 疾风小侠 | 1 048 576 | — | 1080×1920, 29.7 s (truncated) |
| av37850401 | 2018-12-10 | blustone 2 | 58 121¹ | `84addcb6defc09e5`¹ | — |
| **av38052023** | **2018-12-13** | **国服疾风小侠公测试玩** | **212 205 568** | `98e252aaec7f3750` | **1280×720, 1796.1 s** |
| av38084588 | 2018-12-13 | 【试玩几分钟】疾风小侠 | 6 815 744 | `c17472f3fd1fd191` | 720×1280, 428.7 s (partial) |
| av38836370 | 2018-12-23 | 《疾风小侠：青石》：畅快淋漓！ | 27 262 976 | `eb0bc57dfb8a5d6b` | 1920×1080, 443.9 s (partial) |
| av422668606 | 2021-12-30 | Blustone-（角色故事）身分不明的双胞胎-莉兰&拉兰 | 22 020 096 | `bbc078da43959483` | 360×720, 1562.6 s (partial) |
| av46780603 | 2019-03-19 | 【懒，不想起名】疾风小侠升星日常 | 22 912 245 | `4fbcb7fdc513567c` | 640×1280, 89.4 s |
| av543711564 | 2021-01-12 | Blustone青石JJC各种防御队打法 | 2 188 873 | `0ebf7a05fc16e2f1` | 360×720, 41.1 s |
| av645709473 | 2022-09-20 | 青石（疾风小侠） | 3 064 241 | `5234af68dc981f90` | 360×800, 57.7 s |
| av759688919 | 2021-08-07 | （Blustone)第十八章：结语.第5话：新的起点 | 6 537 246 | `192511a243365108` | 360×820, 122.7 s |
| av765367044 | 2022-01-01 | Blustone-（角色故事）超快速的剑术家-拉贝斯 | 7 864 320 | `44e02520a4d0cde2` | 360×720, 1500.4 s (partial) |
| av889000216 | 2021-07-07 | （Blustone）皮肤展示 | 1 310 720 | — | 360×820, 549.4 s (partial) |
| av376524610 | 2021-07-07 | （Blustone）主线剧情第一章：突如其来的考试.第1话：队长资格测试 | 12 799 279 | `9b1adc2056bfceaf` | 360×720, 241.2 s |

¹ = **cover image**, not video. Covers were fetched separately
(`og:image`) and every one decoded to real pixels — the project's "a rewritten
URL is not evidence" rule was applied.

511 frames were extracted at 4 s granularity and reviewed as contact sheets.

---

## 3. NEGATIVE: equipment / accessory stat lines — the last recoverable gap

**Result: no Chinese source transcribes accessory values. Accessory coverage
stays 1/100.**

Why this is a real negative and not a broken instrument:

- The instrument that found the corpus (bilibili JSON search) **passed its
  control** with 78 rows, and it demonstrably filters (§0.2).
- It was queried with the **terminology the Chinese players themselves used**,
  discovered from the corpus rather than guessed — including the four candidate
  names (§1), and including the 装备/属性/饰品/武器 strings for gear.
- `Blustone 装备`, `Blustone 属性`, `Blustone 强化`, `Blustone 抽卡`,
  `Blustone 卡帕`, `Blustone 觉醒` each returned 60 rows of which **0** were
  game-relevant. On a working, filtering search engine that is a content
  statement.
- Every one of the 25 credible videos was retrieved and its frames reviewed. The
  videos that *could* have carried a gear panel are:
  - the four **角色故事** serials — sampled at 4 s, and they are **100 % dialogue**;
    the detail panel is never opened;
  - **av46780603** 升星日常 (star-up daily) — the most promising title, but its
    frames are a gacha animation and a purchase receipt, **not** a stat table;
  - **av889000216** 皮肤展示 (skin showcase) — art only.

The structural reason is visible in the corpus: **Chinese coverage of this game
is narrative and promotional, not tabular.** The CN community's own effort went
into story playthroughs and character stories, not spreadsheets. Unlike Japanese
(`capa2` guide) and Korean (namu tables), there is no Chinese equivalent of a
wiki-maintained gear table.

---

## 4. NEGATIVE: the T2 transcendence observation — still the highest-value gap

**Result: no Chinese T2 panel exists. T1 remains measured at ×1.0994 ± 0.0012
and T2/T3 remain untested.**

This is the most consequential negative in the pass, because a single T2 panel
would decide between the two scaling models (compounding → **1.2087** vs
from-base → **1.2000**).

- The corpus contains a video titled **【疾风小侠】超越极限的Speed Action！**
  (av32093561, 2018-09-20). The word **超越** ("transcend") is right there. But:
  the full description was retrieved and read — it is **promotional copy**
  ("每秒十次的快速攻击節奏" / "the pain of unprecedented release"), the cover
  was fetched and inspected and is **pure promotional art**, and it plays at
  27 minutes as a marketing reel. **A marketing use of the word 超越 is not a
  transcendence panel.** This is precisely the kind of near-miss that reads as a
  hit if the cover is not opened.
- The gameplay videos that could have shown a 卡帕超越 receipt
  (av22075032 arena, av38052023 CN-beta playthrough, av543711564 JJC) were
  reviewed frame-by-frame: **none opens the panel.**
- Chinese players appear to have used **升星** ("raise star") for the star-up
  (av46780603 升星日常) and 觉醒 for awakening — the project's native finding
  that transcendence factors are **server-side** (GUARD-19) is consistent with no
  Chinese guide transcribing them either.

---

## 5. POSITIVE: what Chinese sources *do* contain

These are real readings with provenance. All are **UI/economy numbers**, none is
a base stat tuple, and all are recorded as such. Per the task's rules they are
**not** appended to `polluted-observations.md` (parent mirrors that file).

### 5.1 Event banner — a hiring-card offer with a hard quantity

`av376524610` t≈20 s, 360×720, pre-2021 CN-locale international build.
Panel 活动 ("Events"):

- 新闻速报 banner: *新增★4觉醒猎人！甫制的杰诺比亚*
- **米德加尔特猎人节！★4猎人聘请卡 ×3拍** — "4★ hunter hiring card, ×3 shots",
  with a badge **★4 300%UP** and a timer **剩余时间 08天 04:48:43**
- **7月限定组合包！** with a bundle strip showing **×100 / ×600 / ×1** and
  **剩余时间 24天 13:07:43**
- 抽奖鼠的多多益善！ timer **剩余时间 06天 00:48:43**

*Confidence in transcription: high for the visible digits; medium for
`甫制的杰诺比亚` (low-resolution glyphs).* **Era: pre-rebalance Chinese locale.**
This corroborates the project's existing **★3 MAX → ★4** progression shape and
the 300 % bonus convention, but adds **no per-hero numbers**.

### 5.2 Village HUD — two currencies, stamina and a quest

`av376524610` t≈36 s and t≈40 s:

- **7744 / 162** with a ticket glyph (premium / free currency pair)
- **43 / 6** stamina, and a separate event counter **出乎预料奖励 ×4**
- Quest panel 目标: *请完成超给地区15次！* → **完成地区 15/15**, reward row
  showing a single item at **×10**, button **领取奖励**, header button **查看全部**
- Popup 出队进行情况 (*expedition in progress*) shows a countdown of
  **44:56:70** — a three-field H:M:S-ish display with a stray third field, which
  is itself a useful wire/display clue (the project's §16.5 captures a
  `clear_time` in seconds; a native 3-field expedition timer is new information).

### 5.3 Shop purchase receipt — a **1600 %** bonus

`av46780603` (2019-03-19) t≈88 s, cover and frame agree:

- **购买大成功** ("Great purchase success")
- **▲1600%** in cyan
- a gold-coin glyph with **×80000**

*Confidence: high for 1600 % and 80000; the displayed total is unverified* —
whether 80000 is pre- or post-bonus is not determinable from one frame. **Era:
pre-rebalance CN build.** This is a first-party purchase bonus magnitude that no
other corpus in this project has recorded. It is **not** usable as a shop price
without knowing which pack it was.

### 5.4 Arena (JJC) — the Chinese arena's own name, and its round counter

`av543711564` t≈1 s, 360×720 (read at full resolution, unambiguous):

- Header **戰鬥準備** ("battle preparation")
- **曼法琳级** — a league/tier name, *跟 Tauwind 对决*
- **1/6** with a ticket glyph → **six rounds per set**, one ticket consumed
- **我方队员 241020 VS 预想敌军 11111**
- Button **战斗开始** with a ticket glyph and **1**
- **新对手** ("new opponent")
- Frame t≈40 s ends **VICTORY / WIN! / LOSE** with 获得积分 / 获得奖励 rows

`av22075032` (2018-04-14) corroborates and adds:

- **超電壓深淵 - 8區** — the arena's proper name and a **zone number 8**
- **★★★**, **69/60+** stamina (over-cap overflow visible!), **剩余次数 1次**
- **可获得物品** with **4** item icons; **63** beside a purple currency; and
  **30** beside a coin on the 选择夥伴 button
- Twelve hero portraits each with a **戰鬥力** value:
  `20624, 17558, 17424, 16911, 16581, 16008, 15978, 15698, 15626, 15448,
  15233, 14977`
- Battle HUD damage numbers are visible (147/130, 403/148, 344/131, 172, 99…)
  and the **ULTRA!!!** rating appears, but at 360 px the digits are not reliably
  transcribable and **none is recorded**.

**Era note:** 2018-04 and 2021-01 both **pre-date** the 2019-09-05 rebalance, so
all of the above is pre-rebalance data.

### 5.5 What the 1600 % and the arena numbers are *not*

The 12 `戰鬥力` values and the 241020 / 11111 pair are **composite rating
ratios**, exactly like 戦闘力 in the Japanese corpus. `t1-measured-1.0994` §3
already proved 戦闘力 is **not linear** in HP/ATK/DEF (it moved ×1.162511 under
an operation that moved the three stats ×1.0994). Therefore **these power values
cannot be converted into base stats and must not be counted toward the 1/113
hero coverage.** They are also 12 *distinct* values with no level/grade/gear
state attached — the definition of a polluted observation.

---

## 6. The 2025-2026 batch is a content farm — established, not assumed

A batch of 8 videos appears under `疾风小侠` with titles like
《疾风小侠》2025英雄强度培养顺序攻略，疾风小侠T0级阵容搭配指南 and
疾风小侠最新角色强度榜，2026可用礼包兑换码大全. Two of them showed the
**highest engagement-looking titles** in the entire search result set, which
would otherwise have made them the most attractive targets.

They were checked and **rejected on evidence**, not taste:

1. **Different uploaders, mechanically similar names** — `uftm390`,
   `zqxm291`, `xxvk285`, `心情好运就嚎`. No one of them has a Blustone upload
   from the game's actual lifetime.
2. **The tags name a different game** — the search result carried
   `春秋玄奇` on multiple entries, a title the corpus never contains.
3. **The cover image is a different game.** `av114419086399850`'s cover was
   fetched (101 442 B, sha256 `878d801ac7595f00…`) and inspected: the screenshot
   is a **Chinese wuxia panel with a three-role meta**
   (**手体爆发 / 群体法攻 / 后排爆发** — front-line burst, group magic attack,
   back-line burst) with 手游/首领 characters. **Blustone has four roles and no
   such grid.** A large 疾风小侠 text banner is composited over it.
   Blustone's own roster is not present anywhere in the frame.
4. **Descriptions are template SEO** — "更多实用攻略教学，爆笑沙雕集锦" boilerplate,
   identical across unrelated uploaders.

**Conclusion:** these are SEO/copyright-farm videos riding the dead game's name.
They are excluded from the corpus. **They also mean the game's name is still
being harvested in 2026 — a live reputational artifact, not a stat source.**

---

## 7. Per-hero base stats — negative

Heroes stay at **1/113**. No Chinese source yields a base HP/ATK/DEF tuple with a
known level and no gear.

The nearest miss is the 12 hero portraits in the arena partner-select screen
(§5.4) with their 戰鬥力 values. Those are composite ratings, the heroes' grades
and levels are unreadable at 360 px, and gear state is entirely unknown. Under
this project's own coverage definitions (cf. the FAQ-image-8 precedent, where an
*anonymous gear-removed* tuple still did not move coverage) this is a polluted
observation, not coverage.

The one video that could in principle have opened a detail panel —
**av46780603 升星日常**, the star-up daily — was retrieved at 640×1280 and its
24 frames reviewed: it contains a gacha animation, a purchase receipt and a
cut-in, but **never a stat panel**.

---

## 8. MAX EXP by grade — Chinese sources neither corroborate nor contradict

The two-board consensus (`200/400/1200/4800/24000`) was tested with the CN
terminology: `升级`, `经验`, `升星`, `强化`, `等级`. Across 26 queries the
Chinese corpus returned **zero** level/EXP cost tables. The 2019 archive's
MAX-EXP column is therefore **uncontested rather than corroborated** — a
weaker status than agreement, and stated as such.

---

## 9. Honest summary of what Chinese sources contain

**They contain:**
- A confirmed, dated Chinese localization (疾风小侠 / 青石之战 / 青石) that the
  project had not identified, plus a **pre-rebalance CN national-server beta**
  window (2018-09 → 2018-12) with the highest machine-translatable UI.
- A **CN-server beta playthrough of 1796 s** at 1280×720 (av38052023) — the
  single best remaining Chinese artefact, currently dialogue-only in its frames
  but complete and re-analysable.
- **Arena identity and mechanics**: 超電壓深淵 (zones, zone 8 observed),
  曼法琳级 league, **6 rounds per set**, 1 ticket per battle, 1 remaining on a
  fresh set, and a 3-star tier.
- **Economy readings**: a ★4 hunter hiring card at **×3** with a **★4 300%UP**
  badge; a bundle strip of **×100 / ×600 / ×1**; a **1600%** purchase bonus on a
  **×80000** coin receipt; a **15/15** quest clearing to a **×10** item;
  currency **7744/162**, stamina **43/6** and over-cap **69/60+**.
- An **expedition countdown rendered in three fields (44:56:70)**.

**They do not contain:**
- Any accessory or equipment stat value (accessories remain 1/100).
- Any T2 (or T3) transcendence panel.
- Any per-hero base HP/ATK/DEF with level and gear separable.
- Any level/EXP cost table, gacha rate table, or drop-rate table.
- Any gear-upgrade cost table.

**The reason is structural, not accidental:** Chinese coverage of Blustone is
**narrative and promotional** — story playthroughs, character stories, beta
impressions, CN-server hype. It is a *player community*, not a *data-mining
community*. This is the opposite of namu.wiki (Korean) and `capa2`
(Japanese), which is exactly why those two hold the tables and China does not.
The negative is expected, and it is now documented rather than merely
un-searched.

---

## 10. Reproduction

`%TEMP%\opencode\zh\`

| file | role |
|---|---|
| `harness.py` | one shared `requests.Session` per thread (GUARD-15); url/status/bytes/sha256 recorded per fetch; utf-8→gb18030→big5 sniffing |
| `probe.py`, `find_search.py`, `apis.py` | instrument reachability + **control-gated** search-channel selection |
| `bilibili.py`, `bili_game.py`, `bili_full.py` | corpus enumeration; the control gate refuses to emit a zero |
| `bili_meta*.py`, `bili_deep.py` | og-tag metadata (**not** `__INITIAL_STATE__`, which is polluted by an ad component — a real trap) |
| `bili_media.py`, `dl2.py`, `dlr.py`, `finish.py` | resumable verified downloader working around the 1 MiB CDN cliff |
| `probe_vids.py`, `frames2.py`, `sheet.py`, `stills.py` | ffprobe verification, frame extraction, contact sheets, full-res stills |
| `portals.py`, `ninegame.py`, `spam_and_taptap.py` | the portal avenues, each control-gated |

**Nothing outside this file and that scratch directory was written.** No
`coverage.md`, no TSV, no `polluted-observations.md`, no `server-ts`, no fixture,
no APK, no seed, no emulator, no phone, no Ghidra.

**Coverage counters unmoved:** heroes **1/113**, accessories **1/100**,
monsters **0/22**.

**Two avenues are explicitly left OPEN, not closed:**
1. **QooApp** returned HTTP 500 to our control and is named in a video
   description as the CN distribution route. Its failure is an instrument
   fault.
2. **The 2018 CN-server beta corpus** (av38052023, 212 MB, 1796 s) is fully
   downloaded and hashed; it was sampled at 4 s and read as dialogue-only, but
   a finer pass (1 s, or a targeted look at the mid-video segment where a beta
   player would open the hunter roster) has not been done and is the obvious
   next step for this lane.
