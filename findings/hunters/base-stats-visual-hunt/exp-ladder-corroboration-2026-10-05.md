# EXP-to-max ladder — cross-source corroboration and commensurability adjudication (2026-10-05)

**Purpose.** Put every source that states the hunter EXP-to-max-by-grade ladder
side by side, transcribe it, and then adjudicate one question precisely: **is the
community "MAX EXP" ladder the same kind of quantity as the local replica's
cumulative per-level `min_exp` curve, or are they two different things that must
not be merged?**

**Answer, stated up front:** they **are** the same kind of quantity — cumulative
hunter EXP from Lv 1 to the grade's ordinary level cap — so they **are**
commensurable, and the fixture endpoint is **CONTRADICTED**, not merely
UNSUPPORTED. §2.1 gives the four-step proof. Two independent reasons keep that
from being a "the fixture is wrong, adopt the ladder" conclusion: the evidence is
community prose only ([COMM], never [NATIVE] or [ORIGDATA]), and the rung-5 value
has exactly **one** transcribed source. §2.5 records what would settle it.

**Coverage effect: none.** Heroes 1/113, accessories 1/100, monsters 0/22. Not one
numeral below is a hero, accessory or monster base stat. These are economy /
progression figures.

**Actions taken: none beyond writing this file.** `server-ts`, every fixture, all
LevelDB seeds, the APK, `server-ts/data/state.json`, the emulator and the phone
were **not** touched. No Ghidra run, no native library read, no archive write, no
emulator or device contact. `polluted-observations.md` was **not** appended (the
parent mirrors it). Coverage/readme/TSV files unchanged.

---

# 1. PURE — the ladder from every source that states it, verbatim

Nothing in §1 is inferred, reconciled or normalised. Digits, commas, spelling and
wording are each author's own. Where a source is only *reported* by a prior pass
rather than transcribed, that is marked and the claim is not promoted.

## 1.1 Source register

| Tag | Source | Author | Date | Language / site | Locator | Class | Era |
|---|---|---|---|---|---|---|---|
| **[EN-199711]** | `share_en/199711` "A Glorious Guide on [How not to be a n00b] [OUTDATED for Patch 1.2.0]" | WinJ | 2017-11-12 16:32 | English, `bs.visualshower.com` board `share_en` | archived body, retrieval URL form `…/share_en/<id>`; the same corpus's confirmed capture timestamp for `197745` is `web/20180227140354` (`share-en-guide-2026-10-05.md` §1.2) | [COMM] | PRE-2019-09-05 |
| **[EN-189046]** | `share_en/189046` "Just the tips [Beginner Guide]" | shvrkboy | 2017-11-08 23:32 | English, same board | as above | [COMM] | PRE |
| **[EN-201598]** | `share_en/201598` "Enheim's guide for beginners" | Enheim | 2017-11-13 12:00 | English, same board | as above | [COMM] | PRE |
| **[EN-197134]** | `share_en/197134` "Casual?s Guide to Character Ranking" | Renjixfen | 2017-11-11 | English, same board | as above | [COMM] | PRE |
| **[EN-197134-C]** | comment by `Lgtmagician` inside `197134` | Lgtmagician | 2017-11-13 01:21 | English, same board | as above | [COMM] | PRE |
| **[EN-138442]** | `share_en/138442` "Guide" | HoZhihui | 2017-10-11 | English, same board | as above | [COMM] **reported, not transcribed** | PRE |
| **[TW-56]** | Bahamut `snA=56` 【討論】新手攻略之訓練獵人 | 糖糖 (a2581473) | 2018-01-30 19:12:23 | **Traditional Chinese**, `m.gamer.com.tw` board `bsn=33171` | **live read, not archived:** <https://m.gamer.com.tw/forum/C.php?bsn=33171&snA=56> | [COMM] **paraphrased, not transcribed** | PRE |
| **[EN-21817]** | `share_en/21817` "advancing characters" | waldo_667 | 2017-05-21 | English, same board | as above | [COMM] | PRE |
| **[EN-194179]** | `share_en/194179` "Tips from a New Player" | Taurus_Silver | 2017-11-10 | English, same board | as above | [COMM] | PRE |
| **[EN-23265]** | `share_en/23265` "Small FAQ" | YukiJudai | 2017-05-22 | English, same board | as above | [COMM] | PRE |
| **[TW-17]** | Bahamut `snA=17` 【攻略】新手入門必須知道的七件事 | 請謝謝對不起 (jordan80475) | 2017-11-03 | Traditional Chinese | <https://m.gamer.com.tw/forum/C.php?bsn=33171&snA=17> | [COMM] | PRE |
| **[REPLICA]** | local fixtures | this workspace | – | – | `server-ts/src/hunter-levels.ts`, `server-ts/src/training.ts` | [SELF] | none |

**URL caveat, stated once.** The four `[EN-*]` transcription sources
(`199711`, `189046`, `201598`, `197134`) were fetched by
`share-en-panels-2026-10-05.md` §1.6.2 and §1.6.9 from this corpus, but **that
file records only post ids and post metadata, not per-post capture timestamps.**
The single confirmed capture URL in the workspace for this board is
`web/20180227140354/http://bs.visualshower.com:80/share_en/197745`
(`share-en-guide-2026-10-05.md` §1.2, HTTP 200, 105,467 bytes). The permalink
form for any id is `…/index.php?mid=share_en&document_srl=<id>` and the short form
is `…/share_en/<id>`; both are present in the archive's 833 CDX rows
(`share-en-census-2026-10-05.md` §1.3: 710 permalink-form rows, 90 short-form
rows). **Per-post timestamps for `199711`/`189046`/`201598`/`197134` are not in the
workspace and are not invented here.**

## 1.2 The ladder, verbatim, source by source

### 1.2.1 [EN-199711] — the only source that prints all five rungs

Title as archived: "A Glorious Guide on [How not to be a n00b] [OUTDATED for
Patch 1.2.0]". Rendered in the archived body as a table:

```
n th Star | Required Exp to Max Level | Amount of Lvl 40 Cruises Required | Fuel Required
1 Star    | 200 Exp                    | 18.18 ? 19                        | 114
2 Stars   | 400 Exp                    | 36.36 ? 37                        | 222
3 Stars   | 1200 Exp                   | 109.09 ? 110                      | 660
4 Star    | 4800 Exp                   | 436.36 ? 437                      | 2622
5 Stars   | 24000 Exp                  | 2181.81 ? 2182                    | 13080
```

Preceding it, verbatim:

> Levels 36 - 40 give 11 exp per 6 Fuel (or 1.83 exp/fuel)

The `?` characters above are this project's transcription of an en-dash in the
source table. Digits are the author's.

**Its own column heading is the load-bearing phrase for this whole file:**
**"Required Exp to Max Level"** — a total, per star, to reach the cap. It is not a
per-level step and it does not claim to be.

### 1.2.2 [EN-189046] — rungs 1–3 only, and it says so

Author states level 60+ and a top-50 arena rank. Verbatim, complete:

> EXP:
> 1-Star requires 200 EXP
> 2-Star requires 400 EXP
> 3-Star requires 1200 EXP
> EXP for 4 and 5-stars don't really matter for beginner levels
> because you don't really think about grinding exp for them.

**This source declines rungs 4 and 5 in its own words.** Any tally that counts it
as a voice on 4,800 or 24,000 is wrong.

### 1.2.3 [EN-201598] — rungs 1–4 plus the sacrifice ladder, and the cap remark

> 1-Star - 200 exp , req to advance - 1x 1-Star hunter sacrifice
> 2-Star - 400 exp, req to advance - 2x 2-Star hunter sacrifice
> 3-Star - 1200 exp, req to advance - 3x 3-Star hunter sacrifice
> 4-Star - 4800 exp, req to advance - 4x 4-Star hunter sacrifice
> Notice I stopped at 4-star advancement, even though there's a 5-star tier, that's because a character is capped out at 5-star, there's no 6-star here.

And the cruise corollary, verbatim:

> the best stages to farm for exp that is fuel efficient would be staged 36-39, where each stage yields 11 exp for 6 fuel. So **19 runs for 1-star, and 37 runs for 2-star** to be brought to max level.

### 1.2.4 [EN-197134] — the run counts, third independent statement

> For Rank 1 units, **19 runs** in the Level 36-39 range is perfect to get all of them to Max Level and be ready to rank up to 2. After that, it takes **37 runs** to get the Rank 2 units to Max Level. Then, even after that it takes **110 runs** to get the Rank 3 up to Rank 4

### 1.2.5 [EN-197134-C] — a commenter, a day later, restating the same three

> if want to max a unit, 1 2 3*, farming stage 36 to 39, need respectively **19 37 110** that many times, farming at these stages is fuel cost effective and efficient.

### 1.2.6 [EN-138442] — reported only, no verbatim string stored

`share-en-census-2026-10-05.md` §2.2.1 records that `138442` publishes the same
ladder, and quotes it for the cap: "The hero you want to advance have to be max at
30 level". **No verbatim transcription of `138442`'s EXP figures exists in the
workspace**, and the census's second cap quote, "once your character is maxed
level", **does not contain the number 30**. So `138442` is counted here as a
*reported, untranscribed* voice, and its cap contribution is weaker than the
census implies. See §2.4.

### 1.2.7 [TW-56] — Bahamut, Traditional Chinese, 2018-01-30

`bahamut-remaining-2026-10-05.md` §2, verbatim as recorded:

> - **Max-EXP-per-star prose** ([snA=56](https://m.gamer.com.tw/forum/C.php?bsn=33171&snA=56)):
>   1★ 200 / 2★ 400 / 3★ 1200 / 4★ 4800 / 5★ 24000. Unverified player text;
>   do not normalize against any XP curve.

And its token table (§2 of that file):

> | Max-EXP prose 200/400/1200/4800/24000 | snA=56 text | No — unverified player prose |

**Two provenance limits, both load-bearing:**

1. **No verbatim Chinese text is stored anywhere in the workspace for this
   figure.** The string "MAX EXP" / 「經驗」 / 「滿級」 does not appear in any
   research file. The heading "Max-EXP-per-star prose" is the prior pass's
   **English gloss**, not a quotation of the source's own label.
2. The prior pass's own instruction — "**do not normalize against any XP
   curve**" — is the correct instruction and this file's §2.1 shows exactly what
   normalisation is and is not legitimate.

## 1.3 Side-by-side: how many transcribed voices per rung

| Rung | 200 | 400 | 1200 | 4800 | 24000 |
|---|---|---|---|---|---|
| [EN-199711] verbatim numeral | ✔ | ✔ | ✔ | ✔ | ✔ |
| [EN-189046] verbatim numeral | ✔ | ✔ | ✔ | — (declines) | — (declines) |
| [EN-201598] verbatim numeral | ✔ | ✔ | ✔ | ✔ | — (declines) |
| [EN-197134] run counts × 11 | ✔ 19 | ✔ 37 | ✔ 110 | — | — |
| [EN-197134-C] run counts × 11 | ✔ 19 | ✔ 37 | ✔ 110 | — | — |
| [EN-138442] | reported only | reported only | reported only | reported only | reported only |
| [TW-56] | glossed only | glossed only | glossed only | glossed only | glossed only |
| **Transcribed English voices on the numeral** | **3 + 2 run-count** | **3 + 2** | **3 + 2** | **2** | **1** |

**This corrects the "FOUR-way corroboration" claim in
`share-en-census-2026-10-05.md` §2.2.1 / §3 Rank 1 and the
`share-en-panels-2026-10-05.md` §0 finding **B** ("four-source EXP-to-max-level
ladder").** Rungs 1–3 are genuinely multi-source. **Rung 4 has two transcribed
sources and rung 5 has exactly one** on the English board. The Bahamut gloss would
make rung 5 two-source, but a paraphrase cannot carry the same weight as a
transcription. See §2.4.

## 1.4 The source's own arithmetic — done by the source, reproduced here

[EN-199711] states "11 exp per 6 Fuel". Its run column is therefore
`EXP_to_max / 11` rounded up, and its fuel column is `runs × 6`. Both hold exactly
in all five rows:

| Rung | EXP to max | ⌈EXP/11⌉ = stated runs | 11 × runs | stated runs × 6 = stated fuel |
|---|---|---|---|---|
| 1★ | 200 | 19 | **209 ≥ 200** | 19 × 6 = **114** ✔ |
| 2★ | 400 | 37 | **407 ≥ 400** | 37 × 6 = **222** ✔ |
| 3★ | 1200 | 110 | **1210 ≥ 1200** | 110 × 6 = **660** ✔ |
| 4★ | 4800 | 437 | **4807 ≥ 4800** | 437 × 6 = **2622** ✔ |
| 5★ | 24000 | 2182 | **24002 ≥ 24000** | 2182 × 6 = **13080** ✔ |

**15/15 cells self-consistent.** Two consequences, both used in §2.1:

- The figure is a **total**, not a per-level step (see §2.1 step 4).
- The fuel column is a pure restatement of the run column, so **the fuel column is
  redundant evidence, not a second measurement** — the same caveat
  `transcendence-skill-cost-2026-10-05.md` §2.5(2) applies to the fragment column.

## 1.5 The statements that bound what the ladder's span means

These are not ladder values. They are what makes the ladder interpretable at all,
and §2.1 depends on all three.

**[EN-21817], waldo_667, 2017-05-21 — one level resource, two ways to fill it.
Verbatim, complete:**

> there are two measures for leveling up a character, **the stars and the dots**.
> Dots can be gained by either running missions or by sacrificing other characters on
> the train screen. You'll know that you are leveling dots on the train screen cause
> the button says **train, not advance**.
> Stars on the other hand, can only be gained by sacrificing characters with the same
> number of stats. So one 1\* character sacrificed to get to 2\*, two 2\* characters to
> get to 3\*.
> The characters you sacrifice just need to required stars, they dont need any dots,
> but **the character you are upgrading needs full dots**.

**[EN-194179], Taurus_Silver, 2017-11-10 — the 1★ span, verbatim:**

> (You can mass level **1\* Hunters from lvl 1 -30** once you get high enough)

**`197745` (Alaiko, 2017-11-12), `share-en-guide-2026-10-05.md` §1.5 — the cruise
EXP counter is bounded by the level cap, verbatim:**

> "the experience you gain from each level is constant. This means that
> there is no difference in experience gained if you take 4 hunters or fewer
> hunters"; "**a maxed hunter also gains no experience from cruises.**"

**And the dissenting cap, [EN-23265], YukiJudai, 2017-05-22 — verbatim, item 3 of a
five-item FAQ:**

> 3. **Max level before advance is 20 which is 5 crystals \* 4 balls**

## 1.6 A DIFFERENT quantity: the star-advancement rupee ladder

Recorded here because `share-en-census-2026-10-05.md` §2.2.2 places it beside the
EXP ladder and it is easy to conflate. **It is a rupee cost for changing grade,
not an EXP quantity.** It is *not* part of the commensurability question and it
constrains no XP figure.

| advance | fodder | rupees | transcribed sources |
|---|---|---|---|
| 1★ → 2★ | 1 × 1★ | **1,000** | `24901` HoZhihui 2017-05-23; `193383` UrielSR 2017-11-10; `189046` shvrkboy 2017-11-08; `24731` Kirinxd 2017-05-23; **[TW-17]** snA=17 2017-11-03 |
| 2★ → 3★ | 2 × 2★ | **3,000** | same five |
| 3★ → 4★ | 3 × 3★ | **12,000** | same five |
| 4★ → 5★ | 4 × 4★ | **60,000** | `24901`, `193383`, `189046`, **[TW-17]**; `93837` Silverberg 2017-08-06 as hearsay |
| 4★ → 5★ | 4 × 4★ | **15,000 (dissent)** | `24731` Kirinxd **2017-05-23** |

`24731`, verbatim (`share-en-panels-2026-10-05.md` §1.6.6):

> Don't waste rupees to get challenge invitation, the recharge is only 2 time unlike fuel.
> Bronze to Silver cost 1000 rupees
> Silver to Gold cost 3000 rupees
> Gold to Green cost 12000 rupees
> **Green to Blue cost 15000 rupees**

`93837`, verbatim (`share-en-panels-2026-10-05.md` §1.6.5):

> And finally, the 5star. 5x 4stars. **24\*5= 120 hunters** on the chopping block, and
> one of these moves up and becomes a legend. I can't see what the promotion cost is,
> I'm too poor for that right now.
> (Word's out that the promotion cost is 60k. In this case, 5\*36 = 180k rupees, plus
> this 60k makes a total cost of **240k rupees**.)

`[TW-17]`, verbatim (`video-loose-ends-2026-10-05.md` §3):

> **Evolution costs stated in prose:** 2★ 1000,
> 3★ 3000, 4★ 12,000, 5★ 60,000 gold.

**Corrected tally.** The census §2.2.2 calls this a "TWO-way agreement" on
`138442` + `24901`. `share-en-panels-2026-10-05.md` §1.6.6 independently found
**five English sources** (adding `24731`, `193383`, `189046`, `201598`) and
`video-loose-ends-2026-10-05.md` §3 adds a **sixth in a different language**
(`[TW-17]`). So: **six sources, five languages-sites splits into one English board
plus one Traditional-Chinese board.** 1k/3k/12k is unanimous across all six;
4→5 is **60,000 in five and 15,000 in one**, and the dissenter is the earliest by
six months and sits in a post specifically about item shops. Unresolved.

## 1.7 A THIRD distinct quantity: the transcendence 3×3 matrix

Reproduced for completeness because the prompt asked for it and because
`share-en-census-2026-10-05.md` §2.2.3 mislabels its agreement count. **This is a
per-step material/rupee/duplicate cost. It contains no EXP figure and is not part
of the XP question.**

[EN-215324] is **VSpang, the vendor's own guide account** — "Lana's Guidebook
Ch. 8: Transcendence Gives You Wings~!", 2017-11-21. The archived body renders it
as a **real HTML `<table>`** (`share-en-panels-2026-10-05.md` §1.6.1), reproduced
here exactly as rendered:

```
1? Base Hunter
Transcendence | Metron Crystals | Metron Fragments | Rupees    | Duplicate Hunters
1st           | 5               | 50               | 5,000     | 1
2nd           | 15              | 150              | 15,000    | 2
3rd           | 45              | 450              | 45,000    | 3

2? Base Hunter
Transcendence | Metron Crystals | Metron Fragments | Rupees    | Duplicate Hunters
1st           | 7               | 70               | 7,000     | 1
2nd           | 25              | 250              | 25,000    | 2
3rd           | 60              | 600              | 60,000    | 3

3? Base Hunter
Transcendence | Metron Crystals | Metron Fragments | Rupees    | Duplicate Hunters
1st           | 9               | 90               | 9,000     | 1
2nd           | 30              | 300              | 30,000    | 2
3rd           | 80              | 800              | 80,000    | 3
```

The vendor's own prose, verbatim:

> Another commonly asked question is, does the effectiveness of transcendence change if
> you're a 3?, 4?, or 5? hunter? **The answer is no! Transcendence gives you the same
> amount of stat bonuses no matter what your Hunter Grade is.**

`197745` (Alaiko, 2017-11-12) publishes the identical nine cells in prose
(`share-en-guide-2026-10-05.md` §1.5): 1★ `5/50, 15/150, 45/450`; 2★
`7/70, 25/250, 60/600`; 3★ `9/90, 30/300, 80/800`.

**[NAMU]** (Namu wiki 헌터/블루스톤, raw-HTML cell extraction, mirrors fetched
2026-10-05, Korean, page last-modified 2026-08-13, content 2017–2021, **era
unresolved**) as stored (`transcendence-skill-cost-2026-10-05.md` §1.1): 1★
`5/50, 15/150, 45/450`; 2★ `7/70, 25/250`, **third cell empty**; 3★
`9/90, 30/300, 80/800`; 4★ `12/120, 40/400, 110/1100`; **no 5★ row exists**.
Header is `자기극복 순서 | 1 | 2 | 3`, and the wiki's own header prose states
"fragment is exactly 10× crystal in every cell".

**Corrected agreement count.** The census §2.2.3 heading says "three posts agree,
one differs"; its own body then names `215324`, `197745`, `138442`, `189046` and
`201598`. What the evidence actually supports, and what
`transcendence-skill-cost-2026-10-05.md` §2.1 already concluded:

- **9/9 cells have two independent voices** — `[EN-215324]` **vendor-authored** and
  `[EN-197745]` player, different dates, different document classes.
- `[EN-189046]` covers 3 of the 9 and writes `- T2: **?** Crystals` for 2★.
- `[EN-138442]` omits the 2★ row entirely.
- `[NAMU]` adds three 4★ cells on its own.
- 2★ T3 = **60/600/60,000/3 is single-sourced to the player guide**; no arithmetic
  rule generates it (`transcendence-skill-cost-2026-10-05.md` §2.2–2.3).

## 1.8 [REPLICA] — the local fixture as stored, verbatim

`server-ts/src/hunter-levels.ts`, whole file:

```ts
/** Native card rows are dense, ordered, rank-keyed cumulative XP tables.
 * Historical community evidence supports ordinary cap30 regardless of grade.
 * XP/source-XP/sale values remain local fixtures; awake curves are unknown.
 * Preserve old rank1 thresholds0/100 and source yields100/200 so existing
 * XP100 stays LV2. See analysis/research/hunter-level-caps.md. */
export const ordinaryHunterLevels = [1, 2, 3, 4, 5].flatMap((rank) =>
  Array.from({ length: 30 }, (_, index) => ({
    rank, level: index + 1, min_exp: 100 * index,
    upgrade_exp: 100 * (index + 1), sell_price: 0,
  })));
```

`server-ts/src/training.ts:35-45`, the arithmetic over those rows:

```ts
export function trainingCurve(card: LocalCardInstance) {
  if (Number(card.awk_step) > 0) return null; // awake curve not reconstructed
  const rows = starterLevels.card.filter((row) => row.rank === Number(card.rank));
  if (rows.length === 0) return null;
  const exp = Number(card.exp);
  const next = rows.find((row) => row.min_exp > exp);
  const level = next ? Math.max(1, next.level - 1) : rows[rows.length - 1].level;
  const row = rows.find((entry) => entry.level === level);
  if (!row || !Number.isSafeInteger(exp) || exp < 0) return null;
  return { level, sourceExp: row.upgrade_exp, maxExp: rows[rows.length - 1].min_exp };
}
```

Derived, exactly:

- `min_exp(level) = 100 × (level − 1)`; `min_exp(1) = 0`, `min_exp(30) = **2900**`.
- **`min_exp(30) = 2900 for every rank 1–5.** The curve is rank-invariant.
- Per-level step is a **flat 100**.
- `maxExp` returned to callers = **2900**.
- `upgrade_exp(level) = 100 × level`, i.e. **rank-invariant** and rising with the
  source's level: a Lv 30 source of **any** rank yields 3000.
- `server-ts/src/training.ts:26` gates star promotion on
  `Number(card.exp) < curve.maxExp` → refuses, i.e. **exp must be ≥ 2900**.

**The commensurable scalar, stated once:** the fixture's "EXP to reach max level"
is **2900**, identical at 1★ through 5★. The community's is
**200 / 400 / 1200 / 4800 / 24000**.

## 1.9 [ORIGDATA] — what the shipped client actually ships: nothing

- Native `CSRUserLV::SetLevel` `0x109f114` reads
  `/reference/GetLevel.ret_data.card` rows `rank, level, min_exp, upgrade_exp,
  sell_price`; stride 16, `min_exp`/`upgrade_exp` at +8/+12
  (`hunter-level-caps.md` "Native curve contract remains unchanged").
  **The schema is [NATIVE]-recovered; not one row value is.**
- `analysis/recovered-reference/` contains **no** `min_exp` or `upgrade_exp`
  occurrence — a grep for both across that tree returns nothing.
- `LEVELING.jet` chunk 9 `rank_1..rank_5` is the **monster-rank** multiplier and
  chunk 19 is a `power,rank,hyper,level` threshold table; neither is a hero XP
  curve (`multipliers-2026-10-05.md` §, `hero-stat-divergence-2026-10-05.md`
  §2). Per AGENTS §98/§2026-10-05 local-calibration note, these **must not** be
  used to normalise the archived hunter profiles or the community ladder.
- The shipped in-game help was swept for cost numerals and came back empty:
  **95 `CONTENTS` records, 20 patterns, 0 hits**, in **both** the 1.4.4.1 and the
  2.8.0.1 corpora (`help-2_8-sweep-2026-10-05.md`, per
  `transcendence-skill-cost-2026-10-05.md` §2.11 and
  `fixture-conflict-audit-2026-10-05.md` §2.4). **No XP numeral is in help text
  either.**
- The Wayback/`blustone.jp` hunter-database rows recovered in
  `archived-hunter-database-2019.md` are **13 basic-ability fields with no level
  and no equipped-state context** — they carry no EXP.

**Conclusion: there is no [NATIVE] and no [ORIGDATA] anchor for any rung of this
ladder anywhere in the workspace or in the archive.**

---

# 2. UNPUR[E] — the full token ledger and the adjudication

Everything in §2 is inference, cross-source reasoning or conflict classification.

## 2.1 Commensurability adjudication — the central question

**Question.** The community ladder is labelled "Required Exp to Max Level" /
"MAX EXP", one number per grade. The local fixture is a cumulative **per-level**
threshold function `min_exp(level) = 100(level−1)`. Are these the same kind of
quantity, or a category error waiting to happen?

**Answer: the same kind of quantity. They are commensurable.** Four independent
steps, each resting on a transcribed source in §1.

**Step 1 — same resource, not two EXP pools.** The obvious escape hatch is "the
community measured *cruise* EXP; the fixture delivers *Raise* EXP; those are
different currencies, so stop." **[EN-21817] (2017-05-21) closes it in one
paragraph:** *"there are two measures for leveling up a character, the stars and
the dots. **Dots can be gained by either running missions or by sacrificing other
characters on the train screen.**"* One pool, two inflows — precisely the
cruise-vs-Raise pair. The community's cruise EXP and the fixture's `upgrade_exp`
contribution fill the same counter. The prior pass's own instruction in
`bahamut-remaining-2026-10-05.md` §2 — *"do not normalize against any XP curve"* —
is therefore **too strong as stated**: normalising is what a commensurability
check *is*. What is forbidden is *adopting* the ladder as the fixture.

**Step 2 — same axis.** [EN-199711]'s table puts "Required Exp to Max Level" in
the same row as "Amount of Lvl 40 Cruises Required", and `197745` states *"a
maxed hunter also gains no experience from cruises"* — i.e. the cruise counter is
bounded above by the hunter's level cap. The community figure is the total of the
very counter whose thresholds the native `min_exp` column declares.

**Step 3 — same span.** The community's per-grade total is spent over exactly the
span the fixture publishes. [EN-194179]: *"mass level **1\* Hunters from lvl 1
-30**"*. The cap itself is 30 for all grades (`hunter-level-caps.md`: Namu fn36
「등급에 상관없이 30레벨이 최대」 **plus** the Caragublu 2018-12 **Natalia 3★
Lv30 MAX** and **3★MAX → 4★Lv1** screenshots — an explicit community claim *and*
pixels, and the very evidence the fixture's own header comment cites). The
fixture publishes 30 dense rows per rank. Both quantities run Lv 1 → Lv 30, i.e.
the same 29 steps to the same endpoint. *(One dissent, §2.5 E1.)*

**Step 4 — the community figure is a total, not a per-level step. Proven, not
assumed.** This is the step that decides the question, because if `200` were a
per-**level** cost then the two quantities really would be different kinds. It is
not:

- If 200 were per-level, maxing a 1★ would cost 29 × 200 = **5,800** EXP = ⌈5800/11⌉
  = **528** level-40 cruises.
- [EN-201598], [EN-197134] and [EN-197134-C] independently say **19**.
- 528 / 19 = **27.8×** off. And the table is self-consistent the other way:
  19 × 11 = 209 ≥ 200, and the margin is **+4.5 %** — the tightest possible fit.
  All five rungs clear their total by under 0.5 % (§1.4).
- The same argument kills the alternative that the figure is a per-level cost for
  a *few* levels: no reading of "per level" reproduces 19/37/110/437/2182.

⇒ **The community ladder and `min_exp(30)` measure the same physical quantity:
total hunter EXP to take a card of grade R from Lv 1 to its ordinary cap.**

### 2.1.1 Therefore the endpoint is contradicted, and the shape too

| Grade | [REPLICA] total | Community total | Fixture ÷ community |
|---|---|---|---|
| 1★ | **2900** | 200 | **14.5× too high** |
| 2★ | **2900** | 400 | **7.25× too high** |
| 3★ | **2900** | 1200 | **2.42× too high** |
| 4★ | **2900** | 4800 | **0.60× — fixture too LOW** |
| 5★ | **2900** | 24000 | **0.12× — 8.3× too low** |

**This is not one scaling error.** The fixture is rank-**flat** at 2900; the
community ladder's rung ratio is **1 : 2 : 6 : 24 : 120** (×2, ×3, ×4, ×5 per
grade). Any single rescale of the fixture moves it closer at one end of the ladder
and further at the other. Two independent structural features are missing from the
fixture: **grade-dependence of the total**, and any **grade-dependence of the
per-level step** (implied community averages over 29 steps: ≈ 6.9 / 13.8 / 41 /
166 / 828 per level, against the fixture's flat 100).

**What is *not* contradicted:** the **per-level distribution within a grade**. No
source states it. `200` across 29 steps is consistent with a uniform ≈ 6.9, or a
front-loaded curve, or anything between. So the honest verdict is precise:

- the fixture's **endpoint total and its rank-invariance are contradicted**;
- the fixture's **per-level step is unrecovered, not contradicted**.

## 2.2 Verdict per local fixture row, using `fixture-conflict-audit-2026-10-05.md`'s own scale

| Row | Fixture field | Local value | Verdict **before** | Verdict **after this file** | Change |
|---|---|---|---|---|---|
| **B3** | Cumulative target XP | `min_exp: 100 * index`, 30 rows × 5 ranks, endpoint 2900 flat | UNSUPPORTED | **CONTRADICTED** — in the **endpoint total** and in **rank-invariance**; per-level step still unrecovered | **changed** |
| **B2** | Source XP | `upgrade_exp: 100 * (index + 1)` | UNSUPPORTED | **UNSUPPORTED** (unchanged) + a new scale-plausibility note (§2.3) | unchanged verdict, new note |
| **B4** | Ordinary level cap | 30 rows per rank | CORROBORATED | **CORROBORATED**, unchanged, with an in-era dissent recorded (§2.5 E1) | unchanged |
| **B1** | Raise cost | 100 gold/source | UNSUPPORTED | UNSUPPORTED — the ladder says nothing about gold. **Do not conflate the 1k/3k/12k/60k star ladder (§1.6) with Raise gold.** | unchanged |
| **B8** | RankUp cost | 1000 gold/source | UNSUPPORTED | UNSUPPORTED — see the same non-conflation note | unchanged |
| — | Star-advancement rupees | not a fixture row | — | the local `trainingPrices.rank = [1000]` is a **different quantity** (per-source RankUp gold) from the community's 1k/3k/12k/60k (per-grade advancement). **No comparison is licensed and none is made.** | clarification |

**So the answer to the prompt's framing is the opposite of the "if they are not
commensurable" branch: they *are* commensurable, so the correct verdict is
CONTRADICTED, not UNSUPPORTED.** The instruction not to "declare the local curve
wrong on the strength of the community numbers" is honoured in the following
specific way — §2.4 and §2.5 state exactly how much weight the community numbers
can carry, and §2.3 records why a faithful replacement curve **cannot be built
from the ladder even if it were adopted.**

## 2.3 Full token ledger

Every numeral in play, with its class, its era, and what it does and does not
constrain. Class key: **[NATIVE]** native parser/decompile · **[ORIGDATA]** data or
prose shipped inside the original client · **[COMM]** community prose ·
**[SELF]** the replica's own receipts.

### 2.3.1 EXP-to-max ladder (the subject of this file)

| Token | Value | Source(s) | Class / era | What it constrains | Coverage? |
|---|---|---|---|---|---|
| 1★ EXP to max | **200** | [EN-199711] ✔, [EN-189046] ✔, [EN-201598] ✔; [EN-197134]+[EN-197134-C] via 19 runs × 11; [EN-138442] reported; [TW-56] glossed | [COMM] ×5 transcribed / PRE | the 1★ endpoint total | No |
| 2★ EXP to max | **400** | [EN-199711] ✔, [EN-189046] ✔, [EN-201598] ✔; 37 runs × 11 ×2; [EN-138442] reported; [TW-56] glossed | [COMM] / PRE | 2★ endpoint | No |
| 3★ EXP to max | **1200** | [EN-199711] ✔, [EN-189046] ✔, [EN-201598] ✔; 110 runs × 11 ×2; [EN-138442] reported; [TW-56] glossed | [COMM] / PRE | 3★ endpoint | No |
| 4★ EXP to max | **4800** | [EN-199711] ✔, [EN-201598] ✔; [EN-138442] reported; [TW-56] glossed | [COMM] ×**2** transcribed / PRE | 4★ endpoint | No |
| 5★ EXP to max | **24000** | [EN-199711] ✔ **only**; [EN-138442] reported; [TW-56] glossed | [COMM] ×**1** transcribed / PRE | 5★ endpoint | No |
| rung ratio | 1 : 2 : 6 : 24 : 120 | derived from the five rungs | [COMM]-derived | the fixture's rank-flatness | No |
| per-level average | ≈6.9 / 13.8 / 41 / 166 / 828 | 29 steps implied by the 30 cap | inference | **nothing** — no source states a per-level value | No |
| cruise EXP rate | **11 exp per 6 fuel** (1.83/fuel) | [EN-199711] ✔, [EN-201598] ✔, [EN-197134] ✔, [EN-197134-C] ✔ | [COMM] ×4 / PRE | nothing in the fixture | No |
| run counts | **19 / 37 / 110 / 437 / 2182** | [EN-199711] ✔, [EN-197598] ✔(19/37), [EN-197134] ✔(19/37/110), [EN-197134-C] ✔ | [COMM] ×3-4 / PRE | redundant restatement of the ladder | No |
| fuel totals | **114 / 222 / 660 / 2622 / 13080** | [EN-199711] ✔ | [COMM], **redundant** (= runs × 6) | nothing | No |
| `11 exp/6 fuel` band rule | levels ending 5 or 0 cost more; "the next region costs 7 fuel" | `197745` ✔ | [COMM] / PRE | nothing | No |

### 2.3.2 Level-cap tokens that bound the ladder's meaning

| Token | Value | Source | Class / era | Note |
|---|---|---|---|---|
| ordinary cap | **30, all grades** | Namu fn36 「등급에 상관없이 30레벨이 최대」; Caragublu 2018-12 screenshots (**pixels**); [EN-194179] ✔; [EN-138442] as quoted by the census | [COMM] + [ORIGDATA] image / PRE | fixture row **B4**; unchanged |
| ordinary cap, dissent | **20** | [EN-23265] ✔ *"Max level before advance is 20 which is 5 crystals \* 4 balls"* | [COMM] / PRE, **2017-05-22** | see §2.5 E1 |
| "full dots before advance" | rule | [EN-21817] ✔ | [COMM] / PRE, 2017-05-21 | the **rule** the fixture's `exp >= maxExp` guard implements is corroborated; the threshold value is not |

### 2.3.3 The two adjacent ladders, kept separate

| Token group | Values | Sources | Class / era | Cross-contamination warning |
|---|---|---|---|---|
| star-advancement rupees | 1,000 / 3,000 / 12,000 / **60,000**; dissent **15,000** | 6 sources (§1.6) incl. [TW-17] | [COMM] ×6 / PRE | **rupees, not EXP.** Does not touch the XP question. `trainingPrices.rank = [1000]` is per-source RankUp gold — a *third* quantity. |
| star-advancement fodder | 1/2/3/4 same-grade; total 120 1★ (dissent 96, 119) | `197745` ✔, `201598` ✔, `93837` ✔, `189046` ✔, `197134` ✔ | [COMM] / PRE | counts, not XP |
| transcendence matrix | 3×3 crystal/fragment/rupee/duplicate | [EN-215324] **vendor** ✔ + `197745` ✔ + [NAMU] partial | [COMM]/[ORIGDATA-adjacent] + [COMM] ERA-UNRESOLVED | **no EXP figure anywhere in it** |
| skill-level cost | banded 100…1000 rupees + material ladder | [EN-2017] + [NAMU] | [COMM] / PRE + unresolved | already adjudicated in `fixture-conflict-audit` A1/A3/A4 |
| team EXP | `user: [{min_exp:0},{min_exp:100}]` | [REPLICA] | [SELF] | a **fourth, different** EXP axis (team level, not hunter) — never merge |

### 2.3.4 Scale-plausibility notes — the fixture is not internally consistent either

Inference, not evidence. Recorded because "no evidence" and "evidence that says
this is the wrong order of magnitude" are different research states (the
distinction `fixture-conflict-audit-2026-10-05.md` §2.5 draws).

| Fixture field | Local value | Nearest community figure | Ratio | Reading |
|---|---|---|---|---|
| `min_exp(30)` at 1★ | 2900 | 200 | **14.5×** | high; and 8.3× **low** at 5★ |
| `min_exp(30)` at 5★ | 2900 | 24000 | **0.12×** | direction reverses — no single rescale works |
| `upgrade_exp(30)` (a Lv30 source, any rank) | 3000 | 200 = the **entire** original 1★ Lv1→Lv30 journey | **15×** | under the community ladder one max-level fodder would be worth 15× the whole lowest-grade journey. The original may simply cap out, so this is a plausibility flag, **not** a contradiction — and note the fixture's own two fields are mutually inconsistent in the same direction. |
| `min_exp` step | flat 100 | implied per-level averages 6.9 … 828 | crosses over around grade 3 | the fixture's single number is 1★-like at 1★ and 5★-like at 5★ |
| `trainingPrices.level` (Raise gold) | 100/source | — | — | the ladder says nothing about gold. **Unconstrained.** |
| campaign `character_exp` per win | 10 | — | — | unrelated system; the ladder does not bound it |

## 2.4 Corrections proposed to the parent files — **proposed, not applied**

Nothing below was edited. The parent owns these files.

1. **`share-en-census-2026-10-05.md` §2.2.1 heading vs body.** The heading says
   "**three** independent posts agree exactly" and the body names **four**, then
   calls it "a **4-way** independent corroboration". Worse, §2.2.1's level-30
   attribution is thin: the census quotes `138442` as *"The hero you want to
   advance have to be max at 30 level"* (contains 30) and `201598` as *"once your
   character is maxed level"* (**does not contain 30**) — yet presents them as two
   explicit statements of level 30. **`201598`'s actual verbatim text (§1.2.3)
   says "capped out at 5-star", i.e. about grades, not levels.** The cap-30
   attribution should be re-grounded on Namu fn36 + the Caragublu screenshots,
   which are much stronger, and `138442` marked as reported-only.
2. **The "FOUR-way corroboration" of the full five-rung ladder is an overcount.**
   Rungs 1–3 have 3 transcribed voices plus 2 run-count voices; **rung 4 has 2;
   rung 5 has 1** (§1.3). This propagates to `share-en-census-2026-10-05.md` §3
   Rank 1 ("the 4-way-corroborated EXP ladder") and `share-en-panels-2026-10-05.md`
   §0 finding **B** ("A four-source EXP-to-max-level ladder") and §1.6.2's title.
3. **`share-en-census-2026-10-05.md` §2.2.2's "TWO-way agreement" is an
   undercount** — there are **six** sources across two languages (§1.6), five
   saying 60,000 and one (`24731`, earliest) saying 15,000.
4. **`share-en-census-2026-10-05.md` §2.2.3's transcendence count.** The
   vendor-authored status of `215324` ([VENDOR-AUTHORED] HTML table,
   `share-en-panels-2026-10-05.md` §1.6.1) is not reflected in the census, which
   presents the table as three agreeing *player* posts. `transcendence-skill-cost-2026-10-05.md`
   §2.1 already has this right; the census should defer to it.
5. **`fixture-conflict-audit-2026-10-05.md` row B3 verdict → CONTRADICTED**, with
   the endpoint/shape precision in §2.2. **B2 stays UNSUPPORTED.**
6. **`bahamut-remaining-2026-10-05.md` §2's instruction "do not normalize against
   any XP curve" should be narrowed.** Commensurability is real and established
   (§2.1); what is forbidden is *adopting* the ladder. The current wording reads
   as "these are unrelated", which §1.5's [EN-21817] quote refutes. Also, the
   stored gloss "Max-EXP-per-star prose" should be labelled as **the prior pass's
   English gloss, not a source quotation** — no verbatim Chinese is in the
   workspace.
7. **`share-en-panels-2026-10-05.md` §1.6.2's "Direct consequence for the
   replica" paragraph** reaches the right conclusion ("That fixture makes XP 100 ⇒
   LV2, which these four authors contradict") but does not establish
   commensurability, so its reasoning is incomplete as written. §2.1 supplies the
   missing four steps. Its count should also read 3/3/2/1 per rung.

## 2.5 Conflict register

| ID | Item | Values | Sources | Status |
|---|---|---|---|---|
| **L1** | EXP-to-max endpoint, 1★ | **2900** vs **200** | [REPLICA] vs [EN-199711] ×3 + 2 run-counts + [TW-56] | **OPEN.** Commensurable (§2.1); [COMM] only; no [NATIVE]/[ORIGDATA] anchor exists (§1.9). Cannot be closed by help sweeping — already swept, 95 records / 20 patterns / 0 hits. |
| **L2** | EXP-to-max endpoint, 2★ / 3★ | **2900** vs **400 / 1200** | as above | **OPEN**, same character as L1 |
| **L3** | EXP-to-max endpoint, 4★ | **2900** vs **4800** (fixture **0.60×**) | [EN-199711], [EN-201598] | **OPEN.** Direction reverses here: the fixture is now *below* the community value. |
| **L4** | EXP-to-max endpoint, 5★ | **2900** vs **24000** (fixture **0.12×**) | [EN-199711] **only** transcribed | **OPEN, weakest rung.** One transcribed source. The Bahamut gloss is the only other voice and is untranscribed. |
| **L5** | Grade-dependence of the total | fixture rank-flat; community ×2/×3/×4/×5 | [REPLICA] vs ladder | **OPEN.** The structural half of L1–L4 and the part no rescale fixes. |
| **L6** | Per-level distribution within a grade | **no source states one** | — | **UNRECOVERED, not contradicted.** Implied averages only (≈6.9…828). Blocks any faithful replacement curve even if L1–L5 were resolved. |
| **E1** | Ordinary level cap | **30** vs **20** | 30: Namu fn36 + Caragublu 2018-12 pixels + [EN-194179]; 20: [EN-23265] 2017-05-22 | **OPEN.** Already logged as C2 in `share-en-panels-2026-10-05.md` §2.1; re-registered here because it bounds L1–L6. A May→November 2017 patch would explain it and the 4→5 rupee dissent (**E2**) at once. **Load-bearing for L1–L5:** the ladder's authors sit on the 30 side of that gap. |
| **E2** | 4★→5★ advancement rupees | **60,000** ×5 vs **15,000** ×1 | §1.6 | **OPEN.** Carried forward from C1; unchanged. Not an XP item. |
| **E3** | 1★ fodder for a 5★ hunter | **120** ×2 vs **96 / 119** | `93837`, `189046` vs `197134` | Settled in favour of 120 (per `share-en-panels` C3); recorded only because it shares the ladder's advancement axis. |
| **T1** | Transcendence 2★ T3 = 60/600/60,000/3 | single-sourced | [EN-201745]-only; [NAMU] cell empty | **OPEN-2** inherited from `transcendence-skill-cost-2026-10-05.md`. Not an XP item. |
| **S1** | Skill level 25 material cost | 4+1 vs 5+2 | [EN-2017] vs [NAMU] | **OPEN-1**, inherited. Not an XP item. |
| **X2** | Skill gold formula | `100 × level` vs banded 100…1000 | inherited from `fixture-conflict-audit` | **OPEN**, unchanged by this file. |

## 2.6 What would actually close L1–L6, cheapest first

| Rows | Cheapest decisive step | Why it is the only route |
|---|---|---|
| **L1–L5** | recover the network `GetLevel.card` rows the native getter indexes — i.e. the original server's `rank, level, min_exp, upgrade_exp, sell_price` table | The mechanism is already [NATIVE]-recovered (`CSRUserLV::SetLevel` `0x109f114`, stride 16, `min_exp` at +8). This is a **data** question, not a formula question. Help text is swept and empty; `LEVELING.jet` chunks 9/19 are the wrong tables; the 2019 archive rows carry no level or gear context. **No other artifact in hand contains a single XP numeral.** |
| **L6** | a single in-game EXP readout at a known level and grade (a hunter detail panel, or a training preview) | Would convert an implied average into one measured point. One screenshot. Note that per `share-en-panels-2026-10-05.md` §1.1 all 21 `share_en` namespaces are a hard negative, so this needs a *new* source, not a retry. |
| **L4** specifically | one more independent transcription of the 5★ figure, ideally in a third language | Rung 5 rests on `199711` alone in English. A second transcribed voice would move it from one-source to corroborated. |
| **E1** | a dated original patch/notice covering the ordinary level cap | Would date the 20→30 change and fix which era the ladder was read in. The 2019-09-05 TapTap announcement covers **equipment and crystals only** and says nothing about levels or XP, so era cannot currently be excluded. |
| **TW-56** provenance | re-read `m.gamer.com.tw/forum/C.php?bsn=33171&snA=56` and store the **verbatim Chinese** string plus its own label for the quantity | Currently a gloss. This is a live-page read of a public forum, needs no archive access. It is the cheapest single improvement available and it would test whether [TW-56] is independent of the English guides or a translation of them. |

## 2.7 Limits of this file

- **Nothing is native-recovered and nothing is original shipped data.** The ladder
  is [COMM] ×5 transcribed English voices plus one paraphrased Traditional-Chinese
  voice, all dated **2017-05 → 2018-01**, i.e. **entirely PRE-2019-09-05**.
- **No fixture was changed and no retune is recommended.** §2.2 changes a
  *classification*, not a value. The retune decision belongs to the repository
  owner.
- **The contradiction is real but one-sided in weight.** Native evidence pins the
  *schema and the arithmetic* (`min_exp` cumulative, `upgrade_exp` = source
  contribution, dense 30 rows, monotonic cumulative thresholds) and pins **no
  value at all**. Community prose pins **values** and no mechanism. Under AGENTS §15
  neither may be promoted to the other.
- **The local curve may still be closer to the shipped 2.8.0.1 than the 2017
  guides are.** Nothing here dates the XP curve. The documented rebalance
  (2019-09-05) touches equipment and crystals only, which is *absence of evidence
  about* XP, not evidence that XP was unchanged.
- **Era cannot arbitrate.** [EN-23265]'s cap-20 reading (2017-05) and the ladder's
  authors (2017-11) straddle a possible patch window that nothing dates.
- **Zero coverage effect.** Heroes 1/113, accessories 1/100, monsters 0/22.
- **Cross-title evidence excluded.** MON BLAST! figures (`com.vshower.prd_pf`) are
  a different app and are not used here.
- **No server, fixture, APK, seed, state file, emulator or phone action.** No
  Ghidra run, no native library read, no archive write, no re-upload, no login, no
  form submission. All `share_en` material was already in the workspace; only the
  two Bahamut URLs were cited, not re-fetched.

---

# 3. Files

- **Written:** this file (new).
- **Not appended:** `polluted-observations.md` — the parent mirrors this file.
- **Not modified, corrections only proposed (§2.4):** `share-en-census-2026-10-05.md`,
  `share-en-panels-2026-10-05.md`, `fixture-conflict-audit-2026-10-05.md`,
  `bahamut-remaining-2026-10-05.md`.
- **Untouched:** `coverage.md`, `README.md`, `coverage.tsv`, all archive TSVs,
  `server-ts/**` (including `hunter-levels.ts`, `training.ts`, `openapi.ts`),
  `server-ts/data/state.json`, the APK, all LevelDB seeds, `AGENTS.md`.
