# EXP-to-max ladder — primary sources verified, and the per-level `min_exp` attempt (2026-10-06)

**Task.** (a) find the primary source for each of the five MAX-EXP rungs; (b) recover
the per-level step function `min_exp`, which is still entirely unrecovered.

**Result, stated up front.**

| Question | Answer |
|---|---|
| Primary source for all five rungs | **`share_en/199711`, "A Glorious Guide on [How not to be a n00b] [OUTDATED for Patch 1.2.0]"** (WinJ). Now **byte-verified**: four independent Wayback captures, exact bytes, full sha256, verbatim HTML, and a **byte-identical ladder in all four**. |
| Second independent source, different language | **Bahamut `snA=56`** (Traditional Chinese, 2018-01-30). The **verbatim Chinese string now exists in this workspace** — it did not before. It is the source's own label, not a prior pass's gloss. |
| Rung 5 (`24000`) source count | **1 → 2 transcribed sources**, in two languages. `exp-ladder-corroboration-2026-10-05.md` §2.5 **L4** ("weakest rung, one transcribed source") is superseded. |
| Was `min_exp` (the per-level step function) recovered? | **NO. Not one per-level value was recovered from any source.** Status: **UNRECOVERED**. Seven independent corpora were checked; §3 records each with its control. |
| Lv20-vs-Lv30 contradiction (`E1`) | **The proposed resolution mechanism is refuted.** `exp-ladder-corroboration` §2.5 E1 proposed "a May→November 2017 patch would explain it". The 14 official patch notes covering exactly that window are transcribed in the vsfan wiki; **they raise four other caps with explicit before/after numbers and raise no hunter level cap.** New bound in §2.2. |

**Coverage effect: none.** Heroes 1/113, accessories 1/100, monsters 0/22. No numeral
below is a hero, accessory or monster base stat. These are progression/economy figures.

**Actions taken.** Read-only research. `server-ts/**`, every fixture, all LevelDB seeds,
the APK, `server-ts/data/state.json`, Ghidra, the emulator and the phone were **not**
touched. No emulator or device command was issued. `polluted-observations.md` was
**not** appended (the parent mirrors it). No parent research file was edited; corrections
are **proposed** in §2.6 only.

---

# 1. PURE

Everything in §1 is a verbatim reading of bytes I fetched myself, with a capture or
retrieval timestamp, a byte count and a sha256. Nothing is inferred.

## 1.1 Method, and the positive controls that license every negative below

Per `GUARD-encoding-and-archive-traps.md` ("A rewritten URL is not evidence that content
exists… Always run a positive control against a namespace known to be downloadable before
reading a zero-row CDX result as a real negative"), every control was run **in the same
session and, where the archive was queried, in the same request batch**.

| # | Control | Result |
|---|---|---|
| C1 | `GET https://web.archive.org/` | **HTTP 200, 145,187 bytes** (byte-identical to the figure already recorded in `vsfan-wiki-2026-10-05.md` §1.1 probe 1) |
| C2 | `GET https://example.com/` | **HTTP 200, 577 bytes** |
| C3 | CDX **exact** `bs.visualshower.com/share_en/197745` | **HTTP 200, 1,412 bytes, 7 rows** — including one `200` at `20180227140354`, the corpus capture already cited in `share-en-guide-2026-10-05.md` §1.2 |
| C4 | CDX **exact** `namu.wiki/w/블루스톤` (the parent page) | **HTTP 200, 6 rows, 5 × `200`** — licenses the namu zero in §3.6 |
| C5 | CDX **prefix** `bs.visualshower.com/files/attach/images/` | **HTTP 200, 50,721 bytes, 178 rows, 177 × `200`** — licenses the "2017 board screenshots are not archived" zero in §3.5 |

C3 and C5 are decisive for the two CDX negatives in this file; C4 is decisive for the
namu one. No zero in §3 rests on an untested query.

**Retrieval tooling note.** Python `urllib` **timed out** against `web.archive.org`
(`TimeoutError(10060)`) in this environment while `curl.exe` returned 200. All fetches
below used `curl.exe 8.21.0`; all hashing used Python over the downloaded bytes.

## 1.2 The primary source, now byte-verified

**`[EN-199711]`** · `share_en/199711` · title, verbatim from the archived
`<title>`: **"A Glorious Guide on [How not to be a n00b] [OUTDATED for Patch 1.2.0] -
Blustone"** · author **WinJ** · board `share_en` on `bs.visualshower.com` · language
**English** · [COMM] · era **PRE-2019-09-05** (post dates present in the body:
`2017-11-12`, `2017-11-13`).

**CDX exact-URL result** (`https://web.archive.org/cdx/search/cdx?url=bs.visualshower.com%2Fshare_en%2F199711&output=json`,
1,414 bytes, 8 rows):

| capture (UTC) | status | CDX `length` | note |
|---|---|---:|---|
| 20180131140608 | 302 | 862 | redirect capture |
| **20180331221549** | **200** | 17975 | |
| **20180505210407** | **200** | 18434 | |
| 20180606062634 | 302 | 860 | |
| **20180709140841** | **200** | 18411 | |
| 20180814080157 | 302 | 862 | |
| **20180914213120** | **200** | 18604 | latest `200` |
| 20190913213212 | 302 | 598 | |

All four `200` captures were retrieved in `id_` (raw, un-rewritten) form and hashed:

| capture | retrieval URL | HTTP | fetched bytes | sha256 |
|---|---|---:|---:|---|
| 20180331221549 | `https://web.archive.org/web/20180331221549id_/http://bs.visualshower.com:80/share_en/199711` | 200 | 83,055 | `eb4c7f484e1a8194c7976bd341c9d9d814c9242a59f30c5e83b31b78e1cf98fb` |
| 20180505210407 | `https://web.archive.org/web/20180505210407id_/http://bs.visualshower.com:80/share_en/199711` | 200 | 88,837 | `6ae4392f39249dfc2a8d6e046eea50d8d6f406f46dc5b73e77d690366805ca65` |
| 20180709140841 | `https://web.archive.org/web/20180709140841id_/http://bs.visualshower.com:80/share_en/199711` | 200 | 89,110 | `d0c789d15ad339df073e68714b7bd3e1d78e0616b1f1d7f26539b49e45c878fb` |
| 20180914213120 | `https://web.archive.org/web/20180914213120id_/http://bs.visualshower.com:80/share_en/199711` | 200 | 89,576 | `3e7976534e2173718cb22603a810d7411303e25afb3af518f108070d8b82a6b0` |

Retrieval window 2026-10-06 07:38–07:41 UTC.

**This closes the provenance gap `exp-ladder-corroboration-2026-10-05.md` §1.1 declared
open and refused to fill**: *"Per-post timestamps for `199711` … are not in the
workspace and are not invented here."* They are now established, with hashes.

### 1.2.1 The ladder, verbatim (text extraction of the rendered table)

Column header, verbatim: **`Required Exp to Max Level`**. Row labels verbatim:
`1 Star`, `2 Stars`, `3 Stars`, `4 Star`, `5 Stars` (the inconsistent singular/plural
is the author's).

```
nth Star | Required Exp to Max Level | Amount of Lvl 40 Cruises Required | Fuel Required
1 Star    | 200 Exp                   | 18.18 = 19                      | 114
2 Stars   | 400 Exp                   | 36.36 = 37                      | 222
3 Stars   | 1200 Exp                  | 109.09 = 110                    | 660
4 Star    | 4800 Exp                  | 436.36 = 437                    | 2622
5 Stars   | 24000 Exp                 | 2181.81 = 2182                  | 13080
```

(`=` stands for the `≈` glyph as rendered in the source.)

### 1.2.2 The source's own statement of the span — the load-bearing sentence

Verbatim, in the source's own words, three lines above the table:

> **Every star you character gains, the exp required to go from lvl 1 to max lvl
> increases:**

This is the strongest provenance statement in the whole ladder file and it was not
previously transcribed. It does three things at once:

1. it fixes the span as **lvl 1 → max lvl**;
2. it states the grade-dependence as the author's own explanation, not an inference from
   the numerals;
3. it labels the quantity as **the total over that span**, not a per-level step.

### 1.2.3 The source contradicts itself two bullets earlier — preserved, not tidied

Verbatim, the three bullets, in order:

> 1. It is not shared between characters. (Solo/Group runs give the same amount to EACH character)
> 2. **EXP is independent of Character Stars/Type/Element/etc.**
> 3. **Every star you character gains, the exp required to go from lvl 1 to max lvl increases:** [table]

Bullet 2 (EXP *gained* is star-independent) and bullet 3 (EXP *required* is
star-dependent) are both about EXP and are both consistent only if "independent" in
bullet 2 is read as being about the **inflow**. The author does not disambiguate. **This
is a real ambiguity in the primary source** and any future reading of the ladder must
preserve it, because bullet 2 read literally would contradict bullet 3.

### 1.2.4 The proof bullet is unfinished

The ordered list ends, verbatim: **`(Placeholder Text)`**. The "Proof Below" promised by
the section heading *"Things to note about EXP (Proof Below):"* was never supplied in
text. The 13 attached screenshots are named in `alt` text but the captions that exist
are `Level 40 Clear`, `Higher rate for Rupee Lottery Tickets`, and date-stamped filenames
— **none is captioned as an EXP readout**, and none is archived (§3.5).

### 1.2.5 Cross-capture stability — the ladder did not drift

Extracted from all four captures and compared: the star labels, the five EXP cells, the
five `(≈)` run pairs and the five fuel cells are **byte-identical across 2018-03-31,
2018-05-05, 2018-07-09 and 2018-09-14**. Signature (sha256 of the extracted tuple, first
16 hex): `9e8b6eae37b36f92`. The numerals were not edited between March and September
2018. (Page *byte* length does grow 83,055 → 89,576 — unrelated boilerplate grew; the
ladder did not.)

### 1.2.6 The EXP-per-run denominator, verbatim

> Levels 36 - 40 give 11 exp per 6 Fuel (or 1.83 exp/fuel)

Independently confirmed by the 2019 vsfan wiki — see §1.6.

## 1.3 The second-language primary: Bahamut, verbatim Traditional Chinese

`[TW-56]` · Bahamut `bsn=33171`, `snA=56` · title **【討論】新手攻略之訓練獵人** · author
**糖糖 (a2581473)** · **2018-01-30 19:12:23** · Traditional Chinese ·
<https://m.gamer.com.tw/forum/C.php?bsn=33171&snA=56> (desktop form
`https://forum.gamer.com.tw/C.php?bsn=33171&snA=56`) · [COMM] · PRE-2019-09-05.

**Live page retrieval 2026-10-06 08:18 UTC: HTTP 200, 46,839 bytes decoded, sha256
`292f1fc556f561afbac33d6535fda355ae31c87a800db57c7efb3f8866452678`.**
(`curl --compressed`; the wire body was larger, the decoded figure is the one hashed.)

**The verbatim string, which did not previously exist in this workspace:**

```
練好一張卡需要看的面向有三:
1.星等與等級
這個就是農肥料刷經驗，十分的枯燥。
…
各星等獵人滿等所需經驗:
 一星:200
 二星:400
 三星:1200
 四星:4800
 五星:24000
```

Translation of only the two lines that carry the semantics: *"各星等獵人滿等所需經驗" =
"the experience required for a hunter of each star grade to reach **max level** (滿等)"*;
the five values are `1★:200 2★:400 3★:1200 4★:4800 5★:24000`.

**Why this is more than a paraphrase.** `exp-ladder-corroboration-2026-10-05.md`
§1.2.7 and §2.6 recorded two limits on this source, both of which are now removed:

1. *"No verbatim Chinese text is stored anywhere in the workspace for this figure"* —
   **removed**. The string above is stored here.
2. *"the heading 'Max-EXP-per-star prose' is the prior pass's **English gloss**, not a
   quotation of the source's own label"* — **removed**. The source's own label is
   **滿等所需經驗** = "EXP required to reach max level". It is an **endpoint total**, in
   the author's own words, in a second language, six weeks after the English guide.

**Effect on the rung tally** (`exp-ladder-corroboration` §1.3): rung 5 moves from
**1 transcribed English voice to 2 transcribed voices in 2 languages**; rung 4 from 2 to
3. Rungs 1–3 are unchanged. Its §1.3 tally row `[TW-56] glossed only` becomes
`[TW-56] verbatim`.

**Corroborating context in the same thread, verbatim (different quantity, not merged):**

> 超越一次大約加10%的三圍(攻、防、血，不是B/W/H)

"one transcendence adds about 10% to the three stats (atk, def, hp)". This is a *third*
independent reading of the transcendence stat bonus, alongside the vsfan
`Transcendence Level: 3` ratio of ≈1.27–1.30 (`vsfan-wiki` §2.2) — and 1.10³ = 1.331, so
the two are **consistent**. It does not bear on EXP; recorded because it is new and it
cross-checks an existing open item.

## 1.4 The three attached images in `[TW-56]` — retrieved and inspected

All three fetched HTTP 200 with a Referer of the thread, 2026-10-06 08:19 UTC:

| # | URL | bytes | sha256 | what it is |
|---|---|---:|---|---|
| 1 | `https://truth.bahamut.com.tw/s01/201801/1757762f38744a4a59f16bcf8d7f15e6.JPG` | 266,001 | `5390a450f740cd9b245b9f2ecedd6822439506779b675331c5dde6278c708ecd` | **全獵人技能** — the all-hunters *skill* table (5 skill slots × role columns). Captioned 「這是全獵人技能」 |
| 2 | `https://truth.bahamut.com.tw/s01/201801/d5fdf502a6dc22982fbc776e2cd2b8ee.JPG` | 108,282 | `37918229ed608377c29288d24ede1b194362dba7738da3cfa39d7fe1ae0bd69b` | **T000H00's skill-level cost table**, credited 「來源於…T000H00大大的升技需求表格」 |
| 3 | `https://truth.bahamut.com.tw/s01/201801/4ef71b962fb6e0acab8dd81ac00ccd3c.JPG` | 74,374 | `f4ea4a4db14e948d6cec77e1913ab8eeefb6b3ca9e788280dce3b3b756d2c29a` | **T000H00's transcendence requirement table** |

**Image 2 is the only genuinely new numeric table in this pass, and it is on the SKILL
axis, not the hunter-level axis.** Read by eye, verbatim, header
`等级/次数 | 所需卢比（总计） | 所需材料（总计）`:

| 等级/次数 | 所需卢比（总计） | 所需材料（总计） |
|---|---|---|
| 1-5 / 4次 | 100（400） | 迈特伦碎片1（4）， |
| 5-10 / 5次 | 200（1000） | 迈特伦碎片1（5）；低级素材1（5） |
| 10-15 / 5次 | 300（1500） | 迈特伦碎片2（10）；低级素材2（10） |
| 15-20 / 5次 | 400（2000） | 迈特伦碎片3（15）；低级素材3（15） |
| 20-25 / 5次 | 500（2500） | 低级素材4（20）；中级素材1（5） |
| 25-30 / 5次 | 600（3000） | 低级素材5（25）；中级素材2（10） |
| 30-35 / 5次 | 700（3500） | 中级素材3（15）；高级素材1（5） |
| 35-40 / 5次 | 800（4000） | 中级素材4（20）；高级素材2（10） |
| 40-45 / 5次 | 900（4500） | 中级素材5（25）；高级素材3（15） |
| 45-50 / 5次 | 1000（5000） | 中级素材6（30）；高级素材4（20） |
| **总计** | **27400** | 迈特伦碎片34；低级素材75；中级素材105；高级素材50 |

**This is a SKILL-level table and must not be merged with the hunter-level ladder.** It
is recorded here for one reason only: its last band is `45-50`, independently confirming
the **skill cap of 50** in a third language, consistent with vsfan
`Guide_to_Blustone` (`45 - 49`) and the project's 10-per-grade × 5-grade = 50 convention.
It also gives a **cumulative** material/rupee total (`总计 27400`, fragments 34) that no
English source publishes. The 5-grade × 10-level skill-cap axis and the ordinary 30-level
hunter-cap axis stay separate (§2.3).

**`T000H00` is a named Chinese table-compiler** credited twice in this thread. It is the
single most concrete lead to a fuller Chinese dataset. I did not locate their other
tables (§3.7).

## 1.5 Per-stage EXP yield by region — a NEW table, and a different axis

Extracted from the already-harvested local vsfan corpus
(`analysis/research/base-stats-visual-hunt/vsfan-wiki-2026-10-05.md` §1.4's 299 pages,
stored locally by the 2026-10-05 pass). **19 area pages carry an `EXP per stage`
infobox field.** This table is new to the project.

| Areas | Region | fuel/stage | **EXP/stage** | rupees/stage | page | oldid | capture |
|---|---|---:|---:|---:|---|---:|---|
| 1-10 | Midgard Snowfields | 6 | **7** | ? | `Midgard_Snowfields` | 3248 | 2019-08-21 |
| 11-20 | Midgard Ice Zone | 6 | **7** | ? | `Midgard_Ice_Zone` | 3342 | 2019-08-26 |
| 21-30 | North Highlands | 6 | ? | ? | `North_Highlands` | 3351 | 2019-08-21 |
| **31-40** | **Blood Red Canyon** | **6** | **11** | 65 +/- 5 | `Blood_Red_Canyon` | 3365 | 2019-08-26 |
| 41-50 | Giant's Shelter | 7 | **13** | 70 +/- 5 | `Giant's_Shelter` | 3375 | 2019-08-26 |
| 51-60 | Wolf's Mouth | 7 | **14** | 72 +/- 5 | `Wolf's_Mouth` | 3390 | 2019-08-26 |
| 61-70 | Silent Forest | 7 | **15** | 75 +/- 5 | `Silent_Forest` | 3401 | 2019-08-21 |
| 71-80 | Mt. Black Rock | 8 | **17** | 77 +/- 5 | `Mt._Black_Rock` | 3413 | 2019-08-21 |
| 81-90 | Emerald Canyon | 8 | **19** | 80 +/- 5 | `Emerald_Canyon` | 3424 | 2019-08-21 |
| 91-100 | Crimson Chasm | 8 | **20** | 130 +/- 5 | `Crimson_Chasm` | 3259 | 2019-08-26 |
| 101-110 | Flamestone Basin | 9 | **21** | 135 +/- 5 | `Flamestone_Basin` | 3270 | 2019-08-21 |
| 111-120 | Non-melting Forest | 9 | ? | ? | `Non-melting_Forest` | 3279 | 2019-08-21 |
| 121-130 | Crescent Hill | 9 | **23** | 140 +/- 5 | `Crescent_Hill` | 5832 | 2019-08-21 |
| 131-140 | Burned Forest / Blue Wing Valley | 10 | ? | ? | `Burned_Forest` / `Blue_Wing_Valley` | 5868 / 5873 | 2019-08-21 |
| 141-150 | Forest of the Wanderers | 10 | ? | ? | `Forest_of_the_Wanderers` | 6142 | 2019-08-21 |
| 151-160 | Hawk Turn Highlands | 10 | ? | ? | `Hawk_Turn_Highlands` | 6145 | 2019-08-21 |
| 171-180 | West Forest Outskirts | 12 | **32** | ? | `West_Forest_Outskirts` | 7450 | 2019-08-21 |
| 181-190 | Gray Valley | 12 | **32** | ? | `Gray_Valley` | 7451 | 2019-08-26 |

**Why this matters, precisely.** The ladder's entire arithmetic rests on one number:
**11 EXP per 6 fuel at levels 36–40**. `[EN-199711]` states it. The vsfan wiki, in a
**different language, a different author, and ~21 months later**, states that region
**31-40 yields 11 EXP per stage at 6 fuel per stage**. The ladder's `⌈200/11⌉ = 19`
conversions therefore rest on a denominator confirmed by a source that is **independent
of the ladder's own author**. That is new corroboration for the *basis*, not for the
ladder.

**This is an INFLOW axis, not the `min_exp` threshold axis.** Both
`[EN-199711]` ("the experience you gain from each level is constant… a maxed hunter also
gains no experience from cruises") and vsfan `Guide_to_Blustone` ("the experience you
gain from each level is constant") state the per-stage yield does not vary with the
hunter. So this table **cannot** be divided into the ladder to produce a per-level curve,
and no such division is performed anywhere in this file.

## 1.6 What the vsfan wiki does **not** contain (whole-corpus negative)

A whole-corpus scan of all **299** locally-stored pages (not a targeted probe):

| pattern | hits in 299 pages |
|---|---:|
| `max level` / `maximum level` | 1 |
| `level cap` | **0** |
| `level 30` / `30 level` | 1 / 0 |
| `level 20` / `20 level` | 1 / 0 |
| `Lv. 30` / `Lv. 20` | **0** / **0** |
| `level up` | 1 |

The single `maximum level` hit is `Guide_to_Blustone`: *"If your hunter is already maxed
out, instead of the training option, you will see the advance option"* — **it never
states what "maxed out" is.** The two `level 30` / `level 20` hits are both inside the
**skill** cost band list (`30 - 34: 700 Rupees…`, `20 - 25: 500 Rupees…`), not the
hunter-level cap. **The vsfan wiki contains no hunter level cap and no per-level EXP
value anywhere.**

---

# 2. UNPURIFIED

Inference, cross-source reasoning, and conflict classification. None of §2 is evidence
of a number.

## 2.1 The one arithmetic identity the ladder does have

Derived from the five rungs, and stated here because it is **checkable and
curve-agnostic**:

```
total(R) = 200 · R!      for R = 1..5
200·1! = 200     200·2! = 400     200·3! = 1200
200·4! = 4800    200·5! = 24000
```

Equivalently, each grade multiplies the previous grade's total by its own ordinal
(×2, ×3, ×4, ×5). This is **consistent with but not proof of** a separable per-level
form `min_exp(L, R) = g(R) · h(L)` with `Σ_{L=1..29} h(L) = 100`. **No per-level value
follows from it and none is asserted.** It is recorded because it is a constraint any
future candidate curve must satisfy, and because it makes the local fixture's failure
precise: `server-ts/src/hunter-levels.ts` is **rank-flat** (`min_exp: 100 * index`, 30
rows × 5 ranks, endpoint **2,900** at every grade), i.e. `g(R) ≡ 1`.

## 2.2 E1 (Lv20 vs Lv30) — the proposed mechanism is refuted, and a new bound

**The standing contradiction.** `exp-ladder-corroboration-2026-10-05.md` §2.5 **E1**:
ordinary cap **30** (Namu fn36 + the Caragublu 2018-12 pixels + `[EN-194179]`) versus
**20** from `[EN-23265]`, "Small FAQ", YukiJudai, **2017-05-22**, verbatim:

> 3. Max level before advance is 20 which is 5 crystals * 4 balls

**What that file proposed.** §2.5 E1: *"A May→November 2017 patch would explain it and the
4→5 rupee dissent (E2) at once."* §2.6: the cheapest decisive step for E1 is *"a dated
original patch/notice covering the ordinary level cap."*

**That step has now been taken, and it refutes the hypothesis.**

The vsfan wiki transcribes the **official patch-note series as a first-class corpus**:
29 `Patch_*` pages with parsed dates. Their date coverage:

| version | date | version | date | version | date |
|---|---|---|---|---|---|
| 0.9.3 | 2017-02-27 | 0.9.8 | 2017-04-07 | 0.9.8.1 | 2017-04-13 |
| 0.9.9 | 2017-04-19 | 1.0.0 | 2017-05-14 | 1.0.0.3 | 2017-05-16 |
| 1.0.1.0 | 2017-05-18 | 1.0.1.1 | 2017-05-20 | 1.0.2.0 | 2017-05-25 |
| 1.0.3.0 | 2017-05-31 | 1.0.4.0 | 2017-06-05 | 1.0.5.0 | 2017-06-15 |
| 1.0.6.1 | 2017-06-27 | 1.0.7.0 | 2017-07-12 | 1.0.7.2 | 2017-07-19 |
| 1.0.7.3 | 2017-07-26 | 1.0.8.0 | 2017-08-03 | 1.1.0.0 | 2017-08-17 |
| 1.1.1.0 | 2017-08-23 | 1.1.2.0 | 2017-08-31 | 1.1.3.0 | 2017-09-08 |
| 1.1.4.0 | 2017-09-20 | 1.1.5.0 / 1.1.6.0 / 1.1.7.0 | undated (later 2017) | | |

**The E1 window is 2017-05-22 → 2017-11-12, and it is fully inside this corpus.** The
notes in it are 1.0.2.0 (May 25), 1.0.3.0, 1.0.4.0, 1.0.5.0, 1.0.6.1, 1.0.7.0, 1.0.7.2,
1.0.7.3, 1.0.8.0, 1.1.0.0, 1.1.1.0, 1.1.2.0, 1.1.3.0, 1.1.4.0 — plus the undated
1.1.5–1.1.7, which post-date the English guide.

**These notes are specific about caps, and give explicit before/after numbers — for four
other limits, and never for a hunter level:**

| patch | date | cap/limit change, verbatim |
|---|---|---|
| 0.9.6 | 2017-03-30 | *"EXP gain has been balanced out"* (no numeral) |
| 1.0.7.0 | 2017-07-12 | *"Daily fuel supply has been increased from **30 to 45**"* · *"**Hunter dormitory cap has been raised from 57 to 72**"* |
| 1.0.8.0 | 2017-08-03 | 2★/3★ recruitment requests added as a rare event item |
| 1.1.0.0 | 2017-08-17 | *"Hunter Dormitory increased from **72 to 84**"* |
| 1.1.1.0 | 2017-08-23 | *"The **Fever mode** levels have been changed from white to green"* |
| 1.1.3.0 | 2017-09-08 | *"The **transcendence system has been added** to the game"* (dates transcendence) |
| 1.0.2.0 | 2017-05-25 | *"Hunters **at their maximum levels** will now display a badge over their icon"* |

**Verdict on E1.** The corpus raises a *fuel* cap (30→45) and a *dormitory* cap
(57→72→84) with exact before/after values, and adds the transcendence system — and states
nothing about any hunter level cap. Therefore:

- **(a) REFUTED:** the mechanism E1 relied on. There is no patch note in the entire
  transcribed 2017 series raising a hunter level cap, and the E1 window is covered.
- **(b) What survives.** Three readings remain open, none of which is "a patch did it":
  1. the cap was already 30 on 2017-05-22 and `[EN-23265]`'s *"20 which is 5 crystals \*
     4 balls"* is a transcription or comprehension error — note the parenthetical is a
     **currency-flavoured gloss** ("5 crystals × 4 balls"), not a level statement, which
     is weak evidence that the author was reading a different quantity;
  2. `[EN-23265]` is reporting an **in-game display limit** (e.g. what the level bar or
     the training UI showed) rather than the cap;
  3. the change predates 2017-02-27 and `[EN-23265]` was simply wrong.
- **(c) A hard bound that now holds:** **the five ladder totals are independent of the
  cap.** Every cell of `[EN-199711]`'s own arithmetic is `⌈EXP / 11⌉` and `runs × 6` and
  **none of it references a level count**. So E1 cannot be used to weaken the five rungs;
  what a cap of 20 versus 30 changes is only the **implied per-level average**
  (≈10.5 over 19 steps versus ≈6.9 over 29 steps at 1★). E1 stays open **only** as a
  question about the cap, and it is now bounded to "no in-window patch did it".

**Not verified in this pass.** I did **not** re-fetch and re-verify `[EN-23265]`'s own
bytes. Its capture is needed and `web.archive.org` became unreachable from this host
after 08:20 UTC (sibling agents in this workspace were saturating it — see §3.8). The
`20 which is 5 crystals * 4 balls` string is cited from the existing transcription in
`exp-ladder-corroboration-2026-10-05.md` §1.5, which is itself marked as transcribed from
`share-en-panels-2026-10-05.md`. Treat the *word* "20" as transcribed-but-not-this-pass
byte-verified.

## 2.3 Axes that must stay separate (a false-merge warning)

The search for `min_exp` surfaced several per-grade ladders that are **not** hunter XP.
Merging any of them would be the same class of error the project has already made once
(`trace-rarity-vote-2026-10-05.md` §1.4, on the vsfan trace `Value` column):

| ladder | values | axis | source |
|---|---|---|---|
| **hunter EXP to max** | 200/400/1200/4800/24000 | **cumulative EXP, Lv1→cap** | this file §1.2, §1.3 |
| vsfan trace `Value` | ★20 / ★★100 / ★★★300 | a per-trace rarity VALUE | `vsfan-wiki` §1.10 |
| namu recruitment traces | 1★20 / 2★40 / 3★80 / 4★160 | a **recruitment** threshold | namu 헌터 page, via search index |
| project `collect_qty` | LOCAL 10 / 20 | LOCAL fixture | `server-ts/src/hunter-traces.ts` |
| star-advancement rupees | 1k/3k/12k/60k | per-grade rupee cost | `exp-ladder` §1.6 |
| **skill-level costs** | bands 100…1000 rupees; `总计 27400`; cap 50 | **skill** level | this file §1.4 image 2; `vsfan-wiki` §1.14 |
| transcendence | 3×3 crystal/fragment/rupee/duplicate | per-step cost | `exp-ladder` §1.7 |
| **EXP per stage** | 7…32 by region | **EXP INFLOW**, grade-independent | this file §1.5 |

The namu recruitment ladder (`20/40/80/160`, ×2 per grade) is the most dangerous of these
because it is *also* a ×2-per-grade per-grade table. It is a **trace** threshold and has
no arithmetic relationship to XP.

## 2.4 Era labelling of everything new here

| item | era | note |
|---|---|---|
| `[EN-199711]` ladder | **PRE-2019-09-05**, post 2017-11-12/13 | four captures, all 2018; the page's own title says it is already outdated for Patch 1.2.0 |
| `[TW-56]` ladder | **PRE-2019-09-05**, 2018-01-30 | |
| vsfan EXP-per-stage table | **POST-2019-09-05** territory — wiki content burst 2019-08-21 → 2019-09-23 | **the only source here on the far side of the 2019-09-05 rebalance** |
| vsfan patch series | 2017-02-27 → 2017-09-20 (+3 undated later-2017) | PRE |
| `[EN-23265]` cap-20 | 2017-05-22, PRE | not byte-verified this pass (§2.2) |

**This matters and cuts a way the project should note.** The **only** source in this file
dated on the far side of the documented 2019-09-05 rebalance (equipment +50%, 1–3★ crystal
main +30%, 4–5★ main +50%, all crystal substats +50%, larger upgrade gains after
equipment Lv.20 — see `stat-version-context-2026-10-05.md`) is the vsfan **EXP-per-stage
inflow** table, and it does not restate the EXP-to-max ladder at all. **So no source
here dates the EXP-to-max ladder, and the 2019 rebalance remains silent about it.**
Silence is not evidence of continuity.

---

# 3. NEGATIVES — every one with the control that licenses it

## 3.1 The `min_exp` step function — UNRECOVERED

**Not one per-level EXP value was found in any source.** The seven corpora checked:

| # | corpus | method | result |
|---|---|---|---|
| N1 | **vsfan wiki, all 299 pages** | whole-corpus regex scan over tag-stripped text | **no hunter level cap, no per-level EXP** (§1.6) |
| N2 | **vsfan `Guide_to_Blustone`** (oldid 7465) + `Hunter_Gym` (3172) + `List_of_Blustone_Items` (5115) | full text read | skill costs, transcendence, 12-rank ladder, gacha rates, traces, shop — **no hunter EXP** |
| N3 | **VSFan `Hunter Stats [BROKEN IGNORE].xlsx`** | both worksheets fully parsed (162 shared strings, all cells) | **NO EXP column, no level column, no grade column.** `Details` = Name/Title/Role/Type/Skill1-5 for 30 rows. `Stats` = Strength/Life/Attack/Defense/9 sub-stats × 10 tier rows (Base/Max Bronze→Blue) for 19 heroes. The tier axis Bronze/Silver/Gold/Green/Blue is a **rank-name** axis, not a grade axis. 67 numeric rows, 9 all-N/A heroes. |
| N4 | **`Blustone Guide FAQ.md`** (13,085,200 chars, the official EN help export) | full regex sweep for `4,800` / `24,000` / `1,200` / `\bEXP\b` / `경험치` | `24,000`: **0**. `1,200`: 1, inside base64 image noise. `4,800`: 1, in *"guaranteed to be recruited on their banners after 16 pulls (4,800 manda)"* — a **Manda** cost. `\bEXP\b`: 2, both prose. `경험치`/`경험`: **0**. Q11 (the level/transcendence question) read in full: **no numeral.** |
| N5 | **local recovered assets** (`recovered-assets/`, 6,832 files scanned for `min_exp`, `upgrade_exp`, `sell_price`, `GetLevel`) | raw byte scan | `min_exp`/`upgrade_exp`/`sell_price`: **only** `libnative_core.so` (the JSON key strings) in 3 files. `GetLevel`: only the same library plus this project's own replica logs. **No cached reference response exists on disk.** |
| N6 | **`LEVELING.jet` recovered chunks** | read | `leveling-chunk001.csv` = level→value rate table, a decaying ~1/L hyperbola, **an upgrade/rate cost axis — not XP**; `leveling-chunk019.csv` = `power,rank,hyper,level` thresholds on the **rank** axis; `leveling-chunk09.json` = role modifiers + `rank_1..rank_5` (monster-rank multiplier). **None is a hero XP curve.** Confirms the established negatives; **no fourth chunk was ever extracted.** |
| N7 | **`Hunter Stats` sibling data + 5 packet captures** | inventory only | `analysis/VSFan/Packet Captures/` holds 5 pcaps; the 2017 note already records the Blustone bodies as encrypted. Not re-analysed (no new tooling justified). |

**Conclusion for the parent: `min_exp` remains UNRECOVERED, and this pass did not change
its status.** `exp-ladder-corroboration-2026-10-05.md` §2.5 **L6** stands unchanged.
**No curve was invented from the five totals**, and §2.1 is labelled derived.

## 3.2 The `share_en` corpus — the ladder's own board

The whole corpus was inventoried to check whether the primary source has siblings this
project has not read. CDX **prefix** `bs.visualshower.com/share_en/`, collapsed by urlkey:
**91 rows, 75 × `200`, 74 distinct post ids** — `619, 954, 974, 4921, 12043, 12420,
12654, 16494, 17502, 18069, 18237, 19196, 20858, 21506, 21817, 22732, 23201, 23265,
24731, 30997, 30999, 42865, 55607, 55613, 55618, 55626, 55641, 55672, 55691, 62649,
69900, 83188, 83282, 96417, 97147, 98323, 100785, 138442, 172181, 173620, 174414,
175648, 176367, 178267, 178832, 192223, 192930, 193383, 194024, 194179, 195719, 196827,
197134, 197642, 197745, 197885, 198374, 199332, 201598, 201800, 203849, 215324, 319492,
330982, 395828, 401574, 440600, 507556, 570606, 588855, 601569, 611579, 613470, 630834`.

This is the **short-form** namespace only and matches the 90 short-form rows already
censused in `share-en-census-2026-10-05.md` §1.3. **I did not content-scan the
un-transcribed members** (see §4.1 — a sibling agent was already paging the sibling
board when archive.org became unreachable).

## 3.3 The 13 screenshots attached to the primary source — not archived

All 13 attachment URLs were extracted from the 199711 body (paths
`bs.visualshower.com/files/attach/images/565/{711/199,362/200}/…`, `alt` texts
`Screenshot_2017-11-13-17-16-40.png`, `Screenshot_20171113-123555.png`, etc.). CDX
**prefix** on the whole attachment namespace returned **178 rows, 177 × `200`** (control
C5) — and **not one** of them is under `565/…`. The earliest archived attachment is from
**2019-05-23**. **The two 2017 screenshots the author presents as his "Proof Below" of the
EXP ladder are not in the Wayback Machine.** Even if they were, their captions
(`Level 40 Clear`, `Screenshot_20171113-123555.png`) do not identify them as EXP readouts.

## 3.4 namu.wiki — the `헌터` page is not in the archive

`namu.wiki` returns **HTTP 403** to a browser-shaped request from this host
(5,806 bytes of block page), so a live read was impossible. Archive fallback, with
control C4: CDX **exact** `namu.wiki/w/블루스톤` → **6 rows, 5 × `200`**
(`20200723025215`, `20201203042755`, `20220323055453`, `20220418223152`), and CDX
**prefix** `namu.wiki/w/블루스톤/` → **21 rows** of which the only `200`s are the root
plus unrelated titles (`블루스톤 Dod`, `블루스톤经费`, `블루스톤卡牌100/4000`, `블루스톤桌游`,
`블루스톤技能`, `블루스톤街`, `블루스톤接头`).

**`namu.wiki/w/블루스톤/헌터` — the hunter page that the project's transcendence and trace
figures came from — has ZERO CDX rows.** Not even a `403` row. It is absent from the
archive under that exact URL.

Retrieval of the root page failed twice (`id_` and rewritten forms both returned the
4,611-byte "not archived" page despite the CDX `200` rows), and archive.org became
unreachable at ~08:20 UTC. **I therefore did not read the namu root page and make no claim
about its contents.** The namu facts quoted in this file (skill cap 10 per grade, trace
thresholds 20/40/80/160, 「등급에 상관없이 30레벨이 최대」) come from the **search-engine
index of that page as rendered on 2026-10-06**, not from bytes I fetched, and are used
only in §2.3 as a false-merge warning and in §2.2 as the standing 30-cap citation already
in the project.

## 3.5 Bahamut — the board index is not reachable

`https://forum.gamer.com.tw/index.php?bsn=33171` and
`https://m.gamer.com.tw/forum/index.php?bsn=33171` both return **HTTP 403**
(73,574 / 73,537 bytes). Only a direct `C.php?bsn=…&snA=…` thread URL resolved (§1.3).
**I could not enumerate the Blustone board**, so the other threads advertised in the
thread's own elevator (`【攻略】新手攻略之陣容篇`, `【問題】新手求方向`,
`【問題】求方向`, `【討論】新手想請教高手一些問題!!!求方向指導`) were not opened.

## 3.6 `T000H00` — not located

The Chinese table-compiler credited twice in `[TW-56]` for a skill-cost table and a
transcendence table was not located elsewhere. Searches for
`T000H00` + Blustone/藍色石頭/블루스톤 returned no attributable table host.

## 3.7 Search engines — no per-level table exists in the indexed web

Four targeted searches were run (Korean: `블루스톤 헌터 레벨업 필요 경험치 표 1성 200 2성 400
3성 1200`; Korean: `블루스톤 헌터 레벨업 경험치 필요 경험치 30레벨 최대 등급별`; Chinese:
`Blustone 獵人 等級 經驗值 滿等 200 400 1200 4800 24000 升等 表格`; English: `"Blustone"
hunter exp per level table level 1 to 30 min exp cumulative`).

The only Blustone hits returned were the two already-known pages (namu 헌터 and the
Bahamut thread now transcribed in §1.3). Every other result was a **different game**
(Neverness to Evernness `헌터 레벨`, MapleStory/MapleLand EXP tables, Monster Hunter,
OSRS, Hunt: Showdown, hearthstone.wiki) — i.e. **"hunter level EXP" is a phrase collision
and no Blustone per-level table is indexed.**

## 3.8 Network contention — a limitation of this pass, recorded

From ~08:20 UTC `web.archive.org` refused connections from this host
(`curl (7) Failed to connect … after 3003 ms`, repeated, after C1/C2/C3 had all succeeded
at 07:38–07:41). At that moment **three sibling processes in this workspace were paging the
same archive** (`vsx-fetch.py`, `vsx-retry.py`,
`tools/forum-en-cdx-one-page.py --dir recovered-assets/forum-en-2026-10-05/census
--page 28`). I did not touch them. Consequences, all disclosed:

- `[EN-23265]`'s own bytes were **not** re-verified (§2.2).
- The `share_en` **permalink-form** CDX sweep was not completed, so the census in §3.2 is
  short-form only.
- The namu root page was not read (§3.4).

Nothing in §1 depends on any of these.

---

# 4. What would actually close `min_exp`, cheapest first

`exp-ladder-corroboration-2026-10-05.md` §2.6 remains correct that this is a **data**
question, not a formula question. Ranked by cost now:

| # | route | why it is the only one that works | state |
|---|---|---|---|
| **1** | **`forum_en` — a 3,193-post English board inventory that has never been content-scanned** | The census at `recovered-assets/forum-en-2026-10-05/census/en-post-ids.json` lists **3,193 ids** with `shapes` (BODY/BODYPAGE/COMMENT), `statuses`, `captures`, `canonical_ts` and canonical URLs. **`forum_en` is a different board from `share_en`** — all six ladder ids (`23265, 199711, 138442, 189046, 201598, 197134`) are **ABSENT** from it, so it is genuinely unmined ground, and it is the main English forum where a per-level table or an EXP-bar screenshot discussion would live. **It is 24× the size of the `share_en` short-form corpus.** | **highest-value open item; a sibling agent was paging it as I finished** — do not run concurrently |
| **2** | one in-game screenshot showing `Lv.N` next to an EXP fraction or bar | One frame converts an implied average into one measured point. Best candidates: an **in-app screenshot from the archive-free 2017 board** (unavailable, §3.3), the Reddit/Discord archives already mined by earlier passes, or a **live capture on the replica's own client** — which the project can generate freely, since the `GetLevel.card` rows are fixture-sourced. **A replica screenshot proves the fixture, not the original**, so it can only bound the fixture, never recover the curve. | needs a source with real pixels |
| **3** | the un-transcribed ~55 `share_en` posts in §3.2 | Same board, same era, same authors as the ladder. A 2017 guide by a different author is the single most likely place for a per-level table. | blocked by archive.org availability (§3.8) |
| **4** | the original server's `GetLevel.card` rows | Mechanism is [NATIVE]-recovered (`CSRUserLV::SetLevel` `0x109f114`, stride 16, `min_exp` at +8). Help text swept and empty; `LEVELING.jet` chunks are the wrong tables; `recovered-assets/` holds no cached reference (§3.1 N5). | unchanged |
| **5** | a **pre-2019-09-05** reading of the per-stage EXP inflow | §1.5 is POST-rebalance. If the 2019 rebalance touched XP, the ladder and the inflow table may now describe different games. Nothing here dates either. | open |

## 4.1 Corrections proposed to the parent files — **proposed, not applied**

Nothing below was edited. The parent owns these files.

1. **`exp-ladder-corroboration-2026-10-05.md` §1.1** — the "per-post timestamps … are not
   in the workspace and are not invented here" caveat is now **obsolete** for `199711`.
   Add §1.2's capture table, byte counts and sha256; add the verbatim span sentence
   (§1.2.2); add the bullet-2/bullet-3 self-contradiction (§1.2.3); add the
   `(Placeholder Text)` note (§1.2.4).
2. **§1.2.7 / §2.6, `[TW-56]`** — both stated limits are removed. Store the verbatim
   Traditional Chinese and the source's own label **滿等所需經驗**; change `[TW-56]` from
   "glossed only" to "verbatim" in the §1.3 tally; update §1.3's rung counts from
   **3/3/2/1** to **3/3/3/2** (transcribed voices per rung) and change **L4** from
   "OPEN, weakest rung — one transcribed source" to corroborated.
3. **§2.5 `E1`** — the "a May→November 2017 patch would explain it" mechanism is
   **REFUTED** (§2.2). Replace with the three surviving readings and the new bound that
   the five totals are cap-independent. Record that `[EN-23265]`'s own bytes were not
   re-verified in this pass.
4. **§2.5 `L6`** — unchanged: `min_exp` is **UNRECOVERED**. Add §3.1's seven-corpus
   negative table so the next pass does not repeat it, in particular N3 (the xlsx has **no
   EXP column** — this was an open question in my brief and is now settled) and N5 (no
   cached reference response exists anywhere in `recovered-assets/`).
5. **`share-en-census-2026-10-05.md` §2.2.1 / §3 Rank 1** — the "4-way corroboration"
   overcount is now **3/3/3/2**, with `[TW-56]` promoted from gloss to transcription.
   `share-en-panels-2026-10-05.md` §0 finding **B** and §1.6.2's title need the same
   correction (already proposed as item 2 in `exp-ladder` §2.4; this is the corroborating
   half).
6. **`fixture-conflict-audit-2026-10-05.md` row B3** — verdict **CONTRADICTED** stands
   (endpoint + rank-invariance), and §2.1's `total(R) = 200·R!` identity is the crispest
   statement of the rank-flatness failure yet. **B3's per-level step remains UNRECOVERED.**
7. **New ledger entry: the vsfan EXP-per-stage region table (§1.5).** It is a real,
   citable, third-language-axis-adjacent table that the project's §1.10/§1.11 tables
   never extracted, and it is **the only source in this file on the far side of the
   2019-09-05 rebalance**. It should go into the base-stat hunt's economy annexe as an
   **inflow** quantity, never as a `min_exp` input.
8. **New ledger entry: the Bahamut skill-level cost table with `总计` (§1.4 image 2).** It
   is the only cumulative skill-cost total in the project and independently confirms the
   **skill cap of 50** in a third language. Skill axis only.

## 4.2 Limits of this file

- **Nothing is [NATIVE]-recovered and nothing is [ORIGDATA].** The five rungs remain
  [COMM] — now **2 transcribed languages** (English `share_en/199711` byte-verified;
  Traditional Chinese Bahamut `snA=56` byte-verified), both **PRE-2019-09-05**, plus two
  further English voices (`189046`, `201598`) already transcribed by an earlier pass and
  **not re-verified here**.
- **`min_exp` was not recovered and no curve was invented.** §2.1 is arithmetic on the
  five totals and is labelled derived; it yields **no** per-level value.
- **The local fixture was not changed and no retune is recommended.** Nothing here is
  licensed to replace `100 * (level - 1)`.
- **Era still cannot arbitrate the ladder.** The 2019-09-05 rebalance notice covers
  equipment and crystals and is **silent** on XP; the one POST-rebalance source here
  (§1.5) does not restate the ladder.
- **Zero coverage effect.** Heroes 1/113, accessories 1/100, monsters 0/22.
- **Cross-title evidence excluded.** `Neverness to Everness`, MapleStory/MapleLand,
  Monster Hunter and MON BLAST! figures surfaced repeatedly in search and are **not** used.
- **No contention.** I issued no emulator, adb, Ghidra or `server-ts` command, killed no
  sibling process, and made no network request after archive.org stopped answering on
  purpose.

---

# 5. Files

- **Written:** this file (new).
- **Local working artefacts** (outside the repo, in the approved temp dir
  `C:\Users\shaha\AppData\Local\Temp\opencode\`): `se199711_20180331221549.html`,
  `se199711_20180505210407.html`, `se199711_20180709140841.html`,
  `se199711_20180914213120.html`, `se199711.txt`, `bahamut_sn56.html`, `bh1.JPG`,
  `bh2.JPG`, `bh3.JPG`, `cdx_199711.json`, `cdx_attach.json`, `cdx_ctl.json`,
  `cdx_namu_root.json`, `cdx_namu_sub.json`, `area_exp.json`, plus the fetch/verify
  scripts. Hashes for the archived artefacts are in §1.2 and §1.4.
- **Read-only reuse of an existing local corpus:** `…\Temp\opencode\vsfan\pages\` (the 299
  pages harvested 2026-10-05) — §1.5, §1.6 and §2.2 are computed from it. Nothing in it
  was modified.
- **Not appended:** `polluted-observations.md` — the parent mirrors it.
- **Not modified, corrections only proposed (§4.1):** `exp-ladder-corroboration-2026-10-05.md`,
  `share-en-census-2026-10-05.md`, `share-en-panels-2026-10-05.md`,
  `fixture-conflict-audit-2026-10-05.md`, `vsfan-wiki-2026-10-05.md`.
- **Untouched:** `coverage.md`, `README.md`, `coverage.tsv`, all archive TSVs,
  `server-ts/**` (including `hunter-levels.ts`, `training.ts`, `hunter-traces.ts`),
  `server-ts/data/state.json`, the APK, all LevelDB seeds, `AGENTS.md`, Ghidra.
