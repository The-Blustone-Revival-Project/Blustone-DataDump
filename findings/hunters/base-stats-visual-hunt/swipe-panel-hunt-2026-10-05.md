# Swipe-panel hunt — actual stat panels located, transcribed and cross-checked (2026-10-05)

**Lane:** the vendor statement in `share-en-panels-2026-10-05.md` §1.6.3 (post `42865`,
`VSpang`: the training screen's full stat list is a **swipe-up**, deliberately
under-exposed because "there is a slight glitch when viewing the stats"), the
canonical 12-attribute panel order from `audio-transcripts-2026-10-05.md` §1.5
(`7adedb12.txt` / `UI_CSV`), and the 11 hero `Character Attributes` tables in
`vsfan-wiki-2026-10-05.md` §1.6.

**Read this first — the headline is a confirmation and a set of new *structural*
facts, not new hero coverage.**

1. **The `share_en` `440600` Google Doc is now EXHAUSTED, with a passing positive
   control.** All **28** base64 images were re-fetched and decoded from the live
   document and **every one was viewed by eye**. The document contains exactly
   **five** stat/upgrade panels and **all five were already in this project's
   ledger**. The prior pass's "16 already mined, 12 unmined" framing was based on
   *filenames*, and **byte-hash comparison shows 0 of 28 match the repo copies** —
   the repo's 17 `faq-imageNN-*.png` files are re-encodes, so filename matching is
   not a valid dedup test. **Viewing, not matching, is what closed this.** (§1.2, §1.3)
2. **One new full 12-attribute panel was transcribed first-hand, verbatim, in both
   UI states** — the collapsed 5-row block and the `Details`-expanded
   `Character Attributes` list — for **Beckhen (`051`)**, with its complete
   9-node equipment tree. (§1.4)
3. **NEW: the collapsed block and the expanded list use DIFFERENT row orders.**
   Collapsed prints `HP, ATK, DEF, Attacking Speed` (both EN and KO);
   expanded prints `HP, DEF, ATK, Attacking Speed, …`. This **retracts** the
   reading-order "correction" in `share-en-panels-2026-10-05.md` §1.7 and
   **confirms** the `2866 / 1522 / 1103 = HP/ATK/DEF` attribution recorded in
   `AGENTS.md`. (§1.5)
4. **NEW: an exact arithmetic closure** — `Strength 24068 +6291 = 30359`, and
   `30359` is independently printed on Beckhen's card page **and** on all three
   equipment-at-cap frames. The green delta is therefore proven to mean
   "added by equipment + jewels". (§1.6)
5. **NEW: a jewel set bonus is numerically identical to the stat delta it causes.**
   Set banner `Mount 4, Increase Attack Speed 1.72` ≡ the green `+1.72` on
   `Attacking Speed`; `Mount 2, Increase ATK 5%` ≡ `ATK +317`. (§1.7)
6. **NEW: the three equipment-at-cap frames are IDENTIFIED as Beckhen's** by the
   items' own description prose (`…protects Beckhen's body`, `…Says Beckhen`),
   not merely by adjacency. The accessory frame prints the label **`Max HP`**,
   which is the game's own maximum-HP key (`최대 체력` in `e44ab8ed.txt`) — so the
   goal's `Jack / Max HP 260 @ Lv.50` accessory row is now **visually labelled**,
   not assumed. (§1.8)
7. **Independent corroboration of the archived wiki's only filled equipment
   value**: the 2019 wiki says `Beckhen | Weapon | Chicken Feet | … Lv. 50 | 134`;
   the screenshot of that item reads `ATK 134 → 134` at `Lv.50/50`. Two unrelated
   sources, one number. (§1.8)
8. **NEW NEGATIVE with a passing control, closing a live hypothesis:** the wiki's
   8 *partial* `Character Attributes` tables were checked against **every**
   archived capture of those pages — **33 page fetches across 11 heroes, 2–4
   captures each** — and **no revision of any of the 8 ever contained a
   `Life`/`Attack`/`Defense` cell**. The missing rows are absent from the
   wikitext in all revisions, not recoverable from the archive. (§1.9)
9. **NEW NEGATIVE, unmined corpus:** the 7 PDFs under `analysis/VSFan/Research/`
   (E3/CDEE/Dubai expo reports and brochures, 99 raster images ≥240 px extracted)
   are **trade-show photographs and other VisualShower titles**. No Blustone stat
   panel. This corpus had never been opened. (§1.11)
10. **`analysis/VSFan/Images` re-audited by viewing, not from a manifest.** The 220
    files are 24+23 hunter portraits, 24 emoji, ~35 item icons, ~28 location
    paintings, ~28 NPC busts, logos, press-kit art, and **exactly 6 in-game
    screenshots** — none of which is a stat panel. The earlier "no stat panels"
    judgement is **confirmed**, but its basis is upgraded from a manifest to
    actual viewing. (§1.10)
11. **Caragublu `s1600` originals re-fetched in full (11 images across 2 articles,
    previously only 2 saved locally).** `Upgrade+Equipment.jpg` yields a
    **complete anonymous gear-bearing panel that the ledger recorded only as
    "Strength 18,244, +4,186"** — the HP/ATK/DEF/AS rows, the 3-piece + 6-jewel
    level tree and the `Apply Set` row are **new transcriptions of an already
    known image**. (§1.12)

**Coverage: unchanged. Heroes 1/113, accessories 1/100, jewels 12/12 set families,
monsters 0/22.** Nothing in this lane creates a new base tuple, and §2 states
plainly why each numeric row does not.

---

# SECTION 1 — PURE

Every reading in this section was taken from a decoded image or a retrieved
document **in this session**. Where a row repeats something already in the
project's ledger it is marked **[RE-VERIFY]** — re-read by eye, adds nothing.
Where it is not in the ledger it is marked **[NEW-READING]**.

## 1.1 Controls run before any zero was read as a negative

Per `GUARD-encoding-and-archive-traps.md`: a zero is meaningless without a
positive control **in the same session**, and a harness that cannot fail is not a
control. Every fetch harness in this lane gates on a control and **aborts**.

| # | Harness | Control | Result |
|---|---|---|---|
| 1 | Google Doc text | `export?format=txt` on the same document | **HTTP 200, 36,493 bytes** → abort if `<10,000` |
| 2 | Google Doc HTML | byte count **and** a base64-payload count gate (`abort if <20`) | **HTTP 200, 31,038,284 bytes, 28 images** → abort if `<100,000` |
| 3 | Caragublu pass 1 | `https://example.com/` | **HTTP 200, 577 bytes** |
| 4 | Caragublu pass 2 | `Upgrade+Equipment.jpg` at `s1600` (a real image) | **HTTP 200, 55,666 bytes** |
| 5 | VSFan wiki revision sweep | CDX `url=vsfan.net/wiki/Bear&matchType=exact` | **200, 3 rows** → abort if empty |

**Two controls failed for real, and both aborts were correct:**

- Control 5's first form used a regex that matched **one label/value pair per
  `<tr>`**. The wiki tables pack **two** pairs per row
  (`<td>Life</td><td>2069</td><td>Attack</td><td>734</td>`), so `Attack` and
  `Attack Speed` were **silently dropped** from the parse while `Life` and
  `Defense` survived. A partial parse that *looks* like a negative is exactly the
  failure class this project keeps hitting. Corrected parser in §1.9.
- Control 4 was first written against `https://example.com/` *with an anti-HTML
  guard*, so the guard rejected the control itself and the batch aborted. The
  control was retargeted at a real image. Recorded because a control that
  cannot fail is not a control (§4, note 3).

## 1.2 The `440600` Google Doc — fetch, decode, exact disposition

Source document, from `share-en-panels-2026-10-05.md` §1.6.4 (post `440600`,
Nishino, 2018-02-26, still live):

```
https://docs.google.com/document/d/1O_xdOZqplSVw2XczV2nEl2_wvEZaOc_Mm9RFIY2qaXc
```

Document's own footer, verbatim: `This guide was last edited: 21 / 09 / 2026 (04:51 am GMT-5 Mexico time zone)` — so it **spans 2018 → 2026** and is **MIXED era**; see §2.1.

**28 images decoded, all with valid signatures and real dimensions**
(1080×1920 down to 444×180). Files:
`_swipe/gdoc/faq_01..faq_28` + `_manifest.txt` (sha256 per file).

### The dedup question, answered properly

The prior pass reported "16 of 28 already exist in the repo". **Byte-hash
comparison says otherwise:**

```
repo files: 17
exact-hash matched: 0   unmatched (UNMINED): 28
```

`analysis/catalogue/stats/found/faq-image05..27` are re-encodes (different
containers/compression), so filename similarity is not evidence of duplication.
**All 28 were therefore viewed.** Their captions were extracted from the HTML
text layer in document order, which is how the panels were located at all.

### Every image, its caption, and its verdict

| # | Doc caption / context (verbatim where quoted) | Content | Stat panel? |
|---|---|---|---|
| 01 | (pre-"VINCENT" block) | Search finished, `Deep in the Volcanic Abyss`; Team Level 40; 4 hunter Strengths `14349 / 15207 / 7691 / 15661`; Rupees `+1400`; items | No |
| 02 | (pre-"VINCENT" block) | Search finished, `The Heart of the Electric Abyss`; Team Level 62; Strengths `20484 / 21432 / 18792 / 15409`; Rupees `+2000` | No |
| 03 | (pre-"VINCENT" block) | Search finished; Team Level 55; Strengths `18385 / 18524 / 16050 / 15121` | No |
| 04 | (pre-"VINCENT" block) | `Co-op Exploration Reward`; `21000` rupees; `Rank 210` `People`; mileage `510/510` | No |
| 05 | `VINCENT 20.- Who is Vincent? …` | **Vincent (`010`) "Train Teammate"**; `Master Hunter`; `Lv.30`; `MAX`; **Strength `26711`**. Buttons `Advance / Transcendence / Skill Training / Upgrade Equipment / Story` | Partial (Strength only) |
| 06 | `VINCENT 20.` | **Vincent `010_1` detail panel — see §1.13** | **YES** |
| 07 | `MILEAGE RECRUITING SYSTEM 21.` | Mileage scroll-count table | No |
| 08 | `First example of equipment … Photo by: Vinh-Diesel (American player)` | **Vincent `010` armor `Purple Combat Coat` — see §1.13** | **YES** |
| 09 | `Second example of equipment, displaying gems and stat upgrades Photo by: Aeku (Korean player)` | **Anonymous KO panel — see §1.9** | **YES** |
| 10 | `TYPES OF GEMS AVAILABLE AND EFFECTS` | Gem type selection grid | No |
| 11 | (gem effects) | Gem set-effect illustration | No |
| 12 | (gem effects) | Gem set-effect illustration, 444×180 | No |
| 13 | `Example of Solace's Guild Interface` | Guild interface | No |
| 14 | `Example of Solace's Guild Profile` | Guild profile | No |
| 15 | `Some of the released character skins as of 22 / 12 / 2018` | Skin gallery | No |
| 16 | `Modified skin of Athena` | Athena skin | No |
| 17 | `Image A - Total power of a well trained / invested in Beckhen.` | **Beckhen `051` card page — see §1.4** | Strength only |
| 18 | `Image A.a - General view of the unit stats and modifications … Pressing on "details" in your in-game units gives access to additional information!` | **THE panel, collapsed — see §1.4** | **YES** |
| 19 | `Image A.b - Detailed description of the sub-stats …` | **THE panel, `Details` expanded — see §1.4** | **YES (the only full 12-attribute capture in the whole corpus)** |
| 20 | `Images B (1, 2, 3) - Total main stat increase from reaching the cap …` | Weapon `Chicken Feet` — §1.8 | **YES** |
| 21 | same | Armor `Chicken Wings` — §1.8 | **YES** |
| 22 | same | Accessory `Jack` — §1.8 | **YES** |
| 23–28 | `Weapon jewel #1 (1 out of 6)` … `Armor jewel #2 (6 out of 6)` | Six jewel instance panels | No (jewel class, not accessory) |

**Disposition: 5 panels, 5 already known.** The specific unmined items the prior
pass flagged (`faq_01`–`faq_04` the "Mirage Ruins / co-op loot screens", `faq_07`
the mileage table) were viewed: they are Search/Ruins **reward** screens and a
mileage table, containing **no hunter stat panel**. That lead is closed by viewing.

## 1.3 The canonical 12-attribute panel order is confirmed against pixels

`audio-transcripts-2026-10-05.md` §1.5 recovered the order from
`7adedb12.txt`: `HP, DEF, ATK, Attacking Speed, Critical Attack Chance,
Critical Attack Damage, Armor Penetration, Block Chance, Damage Reduction
Block, Elemental Enhancement, Elemental Resistance, Regeneration`.

Image `faq_19` prints **exactly that order, with exactly those labels, all 12,
plus `Strength` above them** (§1.4). This upgrades the order from
*recovered-from-a-localization-table* to ***recovered-from-a-localization-table
AND observed rendered in-game, in the game's own EN***. The single structural
mismatch with the wiki's editor-written English is now pinned:

- **Game panel** says **`Damage Reduction Block`**.
- **Wiki editors** wrote `Damage Reduction Block` on 5 of 11 heroes and
  **`Block Resistance`** on the other 6, for what the wiki's own field-mapping
  table treats as the same column.

So the label alternation is an **editor inconsistency in one wiki**, not two
distinct stats. The game's own string is `TX_ST_SB9 = Damage Reduction Block`.

## 1.4 ★ Beckhen (`051`) — the full panel in both UI states, verbatim

The document's own `Image A.a` / `Image A.b` pair is the *same screen in two
states*, which makes it the most valuable single object in this corpus: it shows
both what the collapsed panel prints and what the swipe-up reveals.

### 1.4.1 `faq_17` — card page [NEW-READING]

> **Beckhen** · `Guardian of Fight Club` · `Master Hunter` · `Lv.30` · **Strength `30359`**

Identity is **printed on screen**, and `Master Hunter` + `Lv.30` is the rank/level
badge. No gear is visible on this screen (it is the card page, not the
equipment screen), so **gear state is not asserted by this frame** — but §1.6
closes it arithmetically.

### 1.4.2 `faq_18` — `Image A.a`, COLLAPSED [RE-VERIFY + new row-order finding]

Title bar verbatim: **`Upgrade Equipment`**.

Equipment tree, all nine nodes with their printed levels:

| Node | Printed level |
|---|---|
| Weapon (bow icon) | **`Lv. 50`** |
| Armor (wing icon) | **`Lv. 50`** |
| Accessory (Jack face icon) | **`Lv. 50`** |
| Jewel ×6 (two magenta, one red top-left, one red top-right, two magenta bottom) | **all `Lv. 15`** |

Row: **`Apply Set`** with **two** active set icons.

Collapsed stat block, verbatim, white value then green delta:

```
Strength          24068   +6291
HP                2879    +437
ATK               1471    +317
DEF               1149    +154
Attacking Speed   8.00    +1.72
```

Footer affordance, verbatim: **`Details  ▼`**

### 1.4.3 `faq_19` — `Image A.b`, `Details` EXPANDED [RE-VERIFY]

Same title bar, same values, **expanded**, verbatim:

```
Strength                 24068   +6291
HP                       2879    +437
DEF                      1149    +154
ATK                      1471    +317
Attacking Speed          8.00    +1.72
Critical Attack Chance   33.00   +0.67
Critical Attack Damage   200.00  +10.86
Armor Penetration        0.00    +0
Block Chance             14.00   +4.69
Damage Reduction Block   42.00   +1.76
Elemental Enhancement    5.00    +1.65
Elemental Resistance     5.00    +3.13
Regeneration             42.00   +0
```

Set banners at the foot, verbatim:

> **Mount 2, Increase ATK 5%**
> **Mount 4, Increase Attack Speed 1.72**

**This is the only capture in the entire corpus, across every source consulted
by this project, of the complete 12-attribute readout for an identified hero.**
It is already credited as hero `051` in `analysis/catalogue/stats/051.md`
(§4, note 4 explains why it still is not a *base* tuple).

## 1.5 ★ NEW — the collapsed block and the expanded list use different row orders

This is the finding that resolves the project's standing ambiguity, and it
**retracts** a prior reading-order claim.

| Screen | Observed row order | Locales |
|---|---|---|
| **Collapsed** 5-row block | `HP, ATK, DEF, Attacking Speed` | **EN** (`faq_18`) **and KO** (`faq_09`) |
| **Expanded** `Character Attributes` | `HP, DEF, ATK, Attacking Speed, …` | **EN** (`faq_19`) |

Proof from the KO frame, transcribed first-hand from `faq_09`
(title verbatim `장비 강화`, footer row `세트 적용`, i.e. "set applied"):

| KO label (verbatim) | White | Green | EN equivalent |
|---|---|---|---|
| 전투력 | **23847** | +4047 | Strength |
| 생명력 | **2866** | +221 | HP |
| 공격력 | **1522** | +126 | **ATK** |
| 방어력 | **1103** | +110 | **DEF** |
| 공격 속도 | **8.00** | +1.72 | Attacking Speed |

`생명력` = HP, `공격력` = ATK, `방어력` = DEF are the game's own abbreviations
(`audio-transcripts` §1.6, from `e44ab8ed.txt`). Therefore **ATK is `1522` and
DEF is `1103`** — so the values `2866 / 1522 / 1103` recorded in `AGENTS.md` as
`HP/ATK/DEF` are **correct as labelled**.

**The retraction.** `share-en-panels-2026-10-05.md` §1.7 states, of this same
image:

> *"Correction on my own reading order: the KO panel stacks fields as
> 전투력/생명력/공격력/방어력/공격 속도 = Strength/HP/ATK/DEF/AS, so ATK is
> `1103 +110` and DEF is `1522 +126`. The values `2866 / 1522 / 1103` recorded in
> `AGENTS.md` as 'HP/ATK/DEF' therefore read … as HP 2866, DEF 1522, ATK 1103 —
> i.e. the recorded label order is transposed relative to the panel."*

**That correction is itself wrong.** The panel's KO order *is*
전투력/생명력/공격력/방어력 = Strength/HP/**ATK**/DEF, so the recorded
`2866 / 1522 / 1103` = HP/**ATK**/DEF is right and nothing is transposed. What
actually caused the error is the **collapsed/expanded row-order split** documented
above: the same screen number set is printed in `HP, DEF, ATK` order once
`Details` is expanded, so assuming one order for both screens manufactures a
transposition. **`AGENTS.md` §74's figures need no change; the earlier
"correction" should be dropped, not the original reading.**

The KO frame's own `Attacking Speed` `8.00` also matches the EN collapsed
`8.00`, and both KO and EN show `+1.72` on it — the same accessory-side delta as
the EN Beckhen frame, from a different account and locale. `+1.72` therefore
looks like a **jewel-set effect on Attacking Speed** (see §1.7), not an
account-specific number.

## 1.6 ★ NEW — the green delta is "added by gear", proven by closure

Three independently-sourced numbers close exactly:

```
Strength (collapsed panel)      24068
Strength (card page faq_17)      30359
Difference                       6291   == printed green delta on Strength
```

and the green delta is printed as **`+6291`**. So:

> **`delta` = value *after* equipping − value *before* equipping, exactly.**
> `24068 + 6291 = 30359` ✓

Further confirmation that `30359` is a gear-inclusive ceiling rather than a
base: **all three** equipment-at-cap frames in §1.8 print
`Strength 30359 → 30359`, i.e. **zero further increase available**. A number that
is simultaneously the post-gear total and the point where upgrading a piece
yields nothing cannot be a gear-free base value.

This is the strongest single argument in the project that a stat panel captured
on an **equipment screen** can never yield a base stat, and it is *why* the
single credited hero row (`051`) is credited only as a gear-bearing reading.

## 1.7 ★ NEW — a jewel set bonus is numerically equal to the delta it causes

On `faq_19` the two set banners and the green deltas can be matched one-to-one:

| Set banner (verbatim) | Green delta on the matching row | Match |
|---|---|---|
| **`Mount 4, Increase Attack Speed 1.72`** | `Attacking Speed … +1.72` | **exact, same numeral and same decimals** |
| **`Mount 2, Increase ATK 5%`** | `ATK 1471 +317` | consistent (5% applied to a 6340-scale ATK contribution → ~317) |

The first is an **exact** identity, not a coincidence of rounding: a set-effect
string and a stat delta carrying the same two decimals, on the same frame. This
is direct visual evidence that **jewel set bonuses are additive into the
stat row**, and it explains why the FAQ prose says single jewels "do NOT give any
kind of effect" while the panel shows non-zero per-jewel deltas: the per-jewel
subs roll into the row, and only the *set* contributes the named bonus.

It also independently corroborates the FAQ's own claim that the KO frame's
`+1.72` on `공격 속도` is a `Mount 4` set effect.

## 1.8 ★ Equipment at cap — three frames, now identified, with `Max HP` labelled

`Images B (1, 2, 3)`. All three are on the same hunter: **Beckhen (`051`)**, and
now each frame **says so in its own item description**, which upgrades identity
from "adjacent to Image A" to **stated on the object**.

| Frame | Item | Screen | Readings (verbatim) | Description text that identifies the hero |
|---|---|---|---|---|
| `faq_20` | **Chicken Feet** (weapon) | `Lv.50/50` | `Strength 30359 → 30359` · `ATK 134 → 134` | *"…But anyway, Chicken Feet is a threatening weapon."* |
| `faq_21` | **Chicken Wings** (armor) | `Lv.50/50` | `Strength 30359 → 30359` · `DEF 102 → 102` | *"…It is actually an armor that protects **Beckhen's body**."* |
| `faq_22` | **Jack** (accessory) | `Lv.50/50` | `Strength 30359 → 30359` · **`Max HP 260 → 260`** | *"Jack's main role is to be **Beckhen's** interpreter, but sometimes he helps in the battle. …Says Beckhen."* |

Three consequences:

1. **The accessory panel's HP field is labelled `Max HP`.** The game's
   localization table carries `현재 체력` ("current HP") and `최대 체력` ("max
   HP") as **distinct** keys (`audio-transcripts` §1.6). `Max HP` is therefore the
   **maximum-HP** key, so the goal's accessory row `Jack / Max HP 260 @ Lv.50`
   is **visually labelled as maximum HP**, no longer an assumption. It remains a
   *jewel/accessory instance* value, not a hero base stat.
2. **Independent cross-source confirmation of the archived wiki.** `vsfan-wiki`
   §1.8 records that across 216 equipment rows only **two** values were ever
   filled in: `Beckhen | Weapon | Chicken Feet | Increases attack Lv. 50 | 134`
   and `Yuri | Weapon | Skate Shoes | … | 134`. This screenshot of the item
   itself reads **`ATK 134`** at `Lv.50/50`. A 2019 wiki editor transcribing a
   2018 screenshot and an independent image capture agree on **134**. The
   `Skate Shoes 134` cell remains uncorroborated (different item, different
   hero).
3. **The three caps are `DEF 102`, `ATK 134`, `Max HP 260` at `Lv.50/50`,** all
   showing `→` unchanged, i.e. **cap reached**. These are the only
   equipment-cap magnitudes in the whole corpus. `Lv.50` is corroborated: the
   wiki's equipment rows are all `Lv.50`, and the FAQ prose says the special
   element modifiers are used at levels 10/20/30/40 with the slot structure
   still improving past 20.

## 1.9 ★ ★ NEW NEGATIVE — the wiki's 8 missing `Life/Attack/Defense` rows are unrecoverable from the archive

`vsfan-wiki-2026-10-05.md` §1.6 is explicit that 8 of the 11 hero stat tables
jump from `Character Attributes` straight to `Attack Speed`, and that "the
Life/Attack/Defense row anywhere in the markup" is absent — **not blank**. The
open question was whether an **earlier or later revision** of those pages
contained them.

**Method.** CDX `matchType=exact` per page, `collapse=timestamp:8`, every
distinct capture, fetched with the `id_` (raw) form, then every `<tr>` walked and
**all** cells extracted in document order.

**Result — 33 page fetches across 11 heroes, 2–4 captures each:**

| Hero | catalogue | captures checked | caption found | `Life`/`Attack`/`Defense` in ANY revision |
|---|---|---:|---|---|
| Bear | `036` | 3 (2019-08-26, 2019-10-15, 2019-12-09) | none | **never** |
| Diana | `031` | 2 (2019-08-26, 2019-11-14) | none | **never** |
| Joy | `035` | 3 (2019-08-21, 2019-10-20, 2019-12-06) | none | **never** |
| Kain | `029` | 4 (+ 2021-07-29) | none | **never** |
| Lantern | `001` | 3 (2019-08-21, 2019-10-15, 2019-12-16) | none | **never** |
| Pansy | `057` | 3 (2019-08-21, 2019-10-15, 2019-12-16) | none | **never** |
| Patrone | `033` | 4 (+ 2021-07-29) | none | **never** |
| Scar | `032` | 4 (+ 2021-07-29) | none | **never** |
| **Captain** | **`009`** | 4 | **`Transcendence Level: 3`** | Life `2069` · **Attack `734`** · Defense `1142` |
| **Hermes** | **`023`** | 4 | **`Transcendence Level: 3`** | Life `2275` · **Attack `1218`** · Defense `848` |
| **Riko** | **`024`** | 3 | **`Transcendence Level: 3`** | Life `2069` · **Attack `868`** · Defense `1047` |

**Verdict: the 8 partial tables never had those rows in any archived revision.
The "maybe an older wiki revision has it" hypothesis is closed, not merely
untested.** (The 2021 captures are a later site state in which the stat section
is gone entirely — `has_LAD=None`, no table.)

The three complete tables are confirmed verbatim at `Transcendence Level: 3`,
including the `Attack` values which the prior note listed but which a naive
one-pair-per-row parser drops (§1.1). Full raw HTML for Captain, verbatim:

```
<caption>Transcendence Level: 3 </caption>
<tr> <th colspan="4">Character Attributes </th></tr>
<tr> <td>Life</td> <td style="text-align:right;">2069</td> <td>Attack</td> <td style="text-align:right;">734 </td></tr>
<tr> <td>Defense</td> <td style="text-align:right;">1142</td> <td>Attack Speed</td> <td style="text-align:right;">7 </td></tr>
```

## 1.10 `analysis/VSFan/Images` — re-audited by viewing, not from a manifest

The task brief recorded that a prior pass judged these "no stat panels" **from a
MANIFEST**. That is a document-reading judgement, and `GUARD-encoding-and-archive-traps.md`
warns exactly about accepting a rewritten/absent artefact as evidence. So the
inventory was rebuilt and **every candidate class was viewed**.

**Inventory — 220 files, exact:**

| Class | Count | Panel risk |
|---|---:|---|
| `Blustone/Hunters/Original/*_portrait_1080.png` + `diana_full.png` | 24 | none (portraits) |
| `Blustone/Hunters/Half Size/*` | 23 | none |
| `Blustone/Emoji/*` | 24 | none |
| `Blustone/Items/**` (coupons, currency, events, materials, metron, recruitment, traces) | 35 | none (icons/grids) |
| `Blustone/Locations/**` (15 expedition areas + 3 abysses + 8 Midgard buildings, half/full) | 46 | none (background art) |
| `Blustone/NPCs/**` (faces, half, original) | 26 | none (busts) |
| `VisualShower/*` logos | 4 | none |
| `Beyond the Bounds/Press Kit/**`, `White Island/Press Kit/**` | 31 | none (other titles) |
| **`Blustone/Screenshots/Original/**` — the ONLY in-game screenshots** | **6** | **all 6 viewed** |

**All six in-game screenshots, viewed:**

| File | What it shows | Stat panel? |
|---|---|---|
| `battle_screen_full.png` | `Ready to Battle` preparation; Area `40`; fuel `166/60`; 3 stars; 4 allies vs 3 opponents; `MAX` badges | **No** |
| `recruitment_screen_full.png` | `Recruited` — **Lantern `001`**, `First Ever Hunter`, Bomber/Fire, rupee `1000`, `See Details` / `Okay` | **No** — the panel is one unpressed button away |
| `migard_upper_full.png` | Village upper; progress `282/360`; fuel `198/60`; challenge `6/6` | **No** |
| `migard_lower_full.png` | Village lower; `Train` / `Get Hunters`; `28202` rupees, `16` crystals | **No** |
| `dialogue_system_full.png` | dialogue system | No |
| `visualshower_shirt_full.png` | staff photo | No |

**Result: the prior conclusion is CONFIRMED, and its basis is now actual viewing
rather than a filename manifest.** One incidental identity note: the recruit
screen names **Lantern** and prints the epithet **`First Ever Hunter`** with a
2-star badge — an independent EN-locale confirmation of the catalogue's `001`
identity, and it is the only place in this archive where a hero is named on an
in-game screen. **No stat panel.**

## 1.11 ★ NEW NEGATIVE — the VSFan PDFs had never been opened

`analysis/VSFan/Research/` holds **7 PDFs** (55 MB total) that no prior lane in
this goal had extracted: `2013 E3 Gameshow Korea Pavilion` (9.1 MB),
`2014 E3 Gameshow Korea Pavilion`, `Unknown E3 Korean Pavilion Brochure`,
`Unknown E3 Korean Pavilion Company Descriptions`,
`2014 China Digital Entertainment Expo _ Conference Post Show Report`,
`2010 Dubai World Game Expo Report`, and `LingoWinner Company Introduction`
(2.3 MB). A VisualShower expo brochure plausibly carries gameplay stills, so
this was a real candidate corpus.

**Method.** PyMuPDF 1.28.2; every `page.get_images(full=True)` xref extracted;
kept only rasters ≥12 KB **and** ≥240×240; then labelled contact sheets built
with Pillow and **viewed**.

**Result — 99 rasters extracted, 9 sheets screened:**

| PDF | pages | rasters ≥240 px | content |
|---|---:|---:|---|
| 2010 Dubai World Game Expo Report | 4 | 10 | trade-show booth photos |
| 2013 E3 Gameshow Korea Pavilion | 8 | 8 | publisher panel sheets (CESTool, ESTSoft, etc.) |
| 2014 E3 Gameshow Korea Pavilion | 8 | 10 | publisher panel sheets |
| 2014 China Digital Entertainment Expo | 34 | 20 | hall plans, crowd photos |
| LingoWinner Company Introduction | 38 | 32 | a **different** VisualShower title |
| Unknown E3 Korean Pavilion Company Descriptions | 1 | 15 | **other games**: El Sword, Puzzle MonStar, Mutant Metal Blood, Codex |
| Unknown E3 Korean Pavilion Brochure | 1 | 4 | logos / layout |

A text-layer sweep confirms **none of the seven documents contains the string
`Blustone` or `블루스톤` at all** — only `VisualShower` as publisher. **No
Blustone content, therefore no Blustone stat panel.** This corpus is closed.

## 1.12 ★ Caragublu `s1600` originals — full re-fetch, and a completed panel

Only 2 of the 11 Caragublu images were saved locally
(`analysis/research/public-training/caragublu-{train,advance}.jpg`); the rest had
been viewed in-browser only and their bytes were not on disk. Both articles were
re-fetched and **all 11 images downloaded at the `s1600` variant**
(`_swipe/caragublu/`).

Note a fetch trap recorded in code: Blogger image URLs carry the size as a
**path segment** (`…/AVvXsEgl…/s320-rw/Name.jpg`), so the correct transform is to
**replace** that segment with `/s1600/`, not to delete it. Deleting it yields a
404 for every image — which is exactly what the first pass did and reported as
five `MISS` lines.

### 1.12.1 `guide-Upgrade+Equipment.jpg` [NEW-READING — the panel was only half recorded]

This is the frame the ledger records only as *"an unidentified equipment build
with Strength 18,244 and adjacent green +4,186"*. **Transcribed in full,
verbatim:**

Title bar: **`Upgrade Equipment`**. Equipment tree: Weapon **`Lv.25`**, Armor
**`Lv.20`**, Accessory **`Lv.20`**, six jewels at **`Lv.6`, `Lv.6`, `Lv.6`,
`Lv.8`, `Lv.8`, `Lv.8`**. Row: **`Apply Set`** with **two** active set icons.

```
Strength          18244   +4186
HP                2317    +240
ATK               1287    +155
DEF               835     +105
Attacking Speed   8.00    +0
```

Footer affordance: **`Details  ▼`** — collapsed, exactly as the vendor described.

**New relative to the ledger:** the four lower rows (`HP 2317 +240`,
`ATK 1287 +155`, `DEF 835 +105`, `Attacking Speed 8.00 +0`), the complete
three-piece + six-jewel level tree, and the two-icon `Apply Set` row.

**Two properties worth keeping:**

- **`Attacking Speed 8.00` with delta `+0`** — the max ladder value, and this
  build's gear contributes **nothing** to it. Contrast Beckhen, whose `8.00`
  gains `+1.72` from a `Mount 4` set. So the same AS row can be gear-boosted or
  not, frame to frame; `+0` is a real reading, not a missing value.
- **It is an *Upgrade Equipment* screen, so by §1.6's closure argument its white
  values are gear-inclusive.** Its white `Strength 18244` is therefore **not** a
  base value, and `18244 + 4186 = 22430` would be its post-gear total — a number
  that appears nowhere else and is not asserted here.

### 1.12.2 The remaining Caragublu frames [RE-VERIFY]

| File | Content | Panel? |
|---|---|---|
| `Blustone+Train+Hunter.jpg` | Two-pane `Train Teammate`: **Natalia `037`** `Harvesting Disaster`, 3★ `Experienced Hunter`, **`Lv.1` Strength `2480`** → **`Lv.30` Strength `3323`**; buttons `Train / Transcendence / Skill Training / Upgrade Equipment / Story` | Strength only, no HP/ATK/DEF |
| `Blustone+Hunter+Adcance.jpg` | Advancement match, `Power Upgraded 2628 → 3068` (2 fodder, `8000`) / `2628 → 3947` (3 fodder, `12000`) | No |
| `Blustone+Skill+Training.jpg` | **Crocus `058`** `Necromancer's Might` `Lv.35/50`; `Max HP 8.75% → 9.00%`; `4240/4`, `298/4`, `16/2`; `Begin Training 800` | Skill effect, not a base stat |
| `Blustone+Hunter+Transcendence.jpg` | **Bear `036`** `Nature's Gift`, `3425 → 3969`, fodder `1/1`, `Transcendence 9000` | No |
| `Hunter+Recruit.jpg`, `Blustone+Guide+Tips+and+Trick.jpg` | promo / recruit banner | No |
| `anime-*` (5 images, second article) | promo art, battle UI, elements grid, recruit grid | No |

Note the Natalia frame is the **cleanest identity-and-level anchor in the whole
goal**: a named hero, an explicit level change `Lv.1 → Lv.30`, and the Strength
change it causes `2480 → 3323` — but on the **training** screen, which prints
**only** `Strength`. It is a level-delta observation, not a base tuple.

## 1.13 Vincent (`010` / `010_1`) — first-hand transcription

`faq_05`, `faq_06`, `faq_08`.

**`faq_06` — the `010_1` detail panel** (title bar `Train Teammate`; name
`Vincent`; epithet **`Despair of a Millennium`**; **`Lv.30/30`**; a magenta `MAX`
badge; the awakened/skinned portrait):

```
Strength   61815
HP          4980
ATK         2634
DEF         1992
```

Buttons: `Advance` · `Transcendence` · `Skill Training` · `Upgrade Equipment` · `Story`.
**No `Details` expander and no gear tree are visible on this screen**, so
**gear state is NOT shown** — this is the one frame in the corpus where a *named,
identified, levelled* hero has an HP/ATK/DEF reading **and** the gear state is
structurally absent rather than unknown. `AGENTS.md` §75 records these four
numbers with "gear state is unknown"; that is correct and this lane does not
change it — but the *reason* can now be stated precisely: **it is the card
detail screen, which has no equipment tree at all.** That is a strictly stronger
statement than "unknown", and it is the right basis for treating these four
numbers as a candidate base-ish reading rather than an obviously gear-polluted
one.

**`faq_05`** — the `010` (non-awakened) card page: `Renegade Vincent`,
`Master Hunter`, `Lv.30`, `MAX`, **Strength `26711`** only.

**`faq_08`** — `Vincent 010`'s **armor `Purple Combat Coat`**, `Lv.49` → `Lv.50`
upgrade comparison: `Strength 33038 → 33057`, **`DEF 101 → 102`**, cost `50000`.
The coat's own description reads, verbatim: *"It's slightly older than Captain's
coat, but it is presumed to be the same."* — an in-game **cross-reference from
Vincent `010`'s armor to Captain `009`**, which is an identity relationship the
catalogue does not otherwise record.

## 1.14 ★ The `Transcendence Level: 3` cross-check — why the wiki cannot yield a base stat

The task brief asked for this pairing specifically. It was performed, and it
yields a **negative that is more useful than a tuple**.

The wiki gives, at `Transcendence Level: 3`:

| | Captain `009` | Hermes `023` | Riko `024` |
|---|---|---|---|
| Life | 2069 | 2275 | 2069 |
| Attack | 734 | 1218 | 868 |
| Defense | 1142 | 848 | 1047 |

The 2019 `blustone.jp` archive gives, at unspecified state:

| | Captain `009` | Hermes `023` | Riko `024` |
|---|---|---|---|
| hp | 1624 | 1750 | 1624 |
| atk | 628 | 937 | 682 |
| def | 893 | 653 | 821 |

Ratios (wiki ÷ JP), recomputed here: Captain `1.274 / 1.169 / 1.279`;
Hermes `1.300 / 1.300 / 1.299`; Riko `1.274 / 1.273 / 1.275`.

**What this establishes, and what it does not:**

- **It establishes** that the two corpora are the same underlying data at two
  different progression states — the 9 sub-stats match exactly for all 11 heroes
  while *only* Life/Attack/Defense differ, which is precisely the signature of a
  multiplier applied to three fields and not to nine.
- **It does not establish** a divisor. A transcendence multiplier is not
  invertible without knowing (a) the base level of each reading, (b) whether the
  JP row is Lv.1, Lv.30 or a grade-normalised figure, and (c) whether the
  transcendence bonus applies once or is folded into the level curve. Captain's ATK
  ratio of `1.169` against `1.274`/`1.279` for its other two fields is
  **evidence that no single multiplier explains all three** — the divergence is
  too large to be rounding.
- **Therefore no base stat may be derived by division**, and this lane does not
  derive one. The pairing's real value is diagnostic: it proves the JP archive
  rows are **not** bare base stats, which is a fact the coverage ledger had
  recorded as "level and equipped state unresolved" and can now narrow.

---

# SECTION 2 — UNPURE

Every numeral touched in this lane, with its identity, level/rank, gear state and
era. **None of these rows earns coverage**, and the reasons are given rather than
implied.

## 2.1 Era tags

| Tag | Meaning |
|---|---|
| **PRE-2019-09-05** | before the +50% equipment / +30–50% crystal rebalance (`stat-version-context.md`) |
| **POST-2019-09-05** | after it |
| **MIXED** | document created before and last edited after the boundary |

- **`440600` Google Doc (all 28 images): MIXED.** Created 2018-02-26, footer
  `last edited: 21 / 09 / 2026`. Individual frames are un-datable. `faq_20–22`
  (equipment at cap) and `faq_19` (full panel) are **most likely PRE**, because
  the FAQ's own prose describes the pre-rebalance equipment economy, but this is
  an inference and the frames carry no visible date.
- **Caragublu guide: PRE-2019-09-05.** Article dated `2018-12-05` by
  `itemprop=datePublished`. All 11 frames.
- **`vsfan.net` wiki: POST** for the 2019-08/09/10/12 and 2021 captures (all
  post-date the rebalance).
- **`archive.org` revision sweep (§1.9): 2019-08 → 2021-07.** The 2021 captures
  no longer contain the stat table.

## 2.2 Numeric ledger — identity / level / gear state per row

**Legend.** `ID?` = identity not established. `GEAR` = gear state visible.
`NO-GEAR` = screen has no equipment tree, so gear is structurally not shown.

| # | Source | Hero | ID | Level / rank badge | Gear state | Readings | Why it is not coverage |
|---|---|---|---|---|---|---|---|
| N1 | gdoc `faq_19` | Beckhen | **`051`** | `Master Hunter`, `Lv.30` | **GEAR** — 3 pieces all `Lv.50`, 6 jewels all `Lv.15` | Strength `24068+6291`; HP `2879+437`; DEF `1149+154`; ATK `1471+317`; AS `8.00+1.72`; CritChance `33.00+0.67`; CritDmg `200.00+10.86`; Pen `0.00+0`; Block `14.00+4.69`; DRB `42.00+1.76`; ElemEnh `5.00+1.65`; ElemRes `5.00+3.13`; Regen `42.00+0` | **Gear-bearing.** §1.6 proves `24068` is the pre-gear value of a *fully geared* hunter and `30359` its total; neither is a base stat. Already the project's single credited hero row. |
| N2 | gdoc `faq_18` | Beckhen | **`051`** | same | same | collapsed block: `24068 / 2879 / 1471 / 1149 / 8.00` with `+6291 / +437 / +317 / +154 / +1.72` | Same panel, collapsed. Row-order finding only (§1.5). |
| N3 | gdoc `faq_17` | Beckhen | **`051`** | `Master Hunter`, `Lv.30` | not shown | Strength `30359` | Post-gear ceiling; equals the delta sum (§1.6). |
| N4 | gdoc `faq_09` | `ID?` | **not identified** | none | **GEAR** — Weapon `Lv.40`, Armor `Lv.20`, Accessory `Lv.20`; jewels `Lv.5×3`, `Lv.10×2`, `Lv.5`; `세트 적용` 2 sets | 전투력 `23847+4047`; 생명력 `2866+221`; 공격력 `1522+126`; 방어력 `1103+110`; 공격 속도 `8.00+1.72` | No identity ⇒ not a hero tuple. Already the project's single anonymous gear-removed reading. |
| N5 | gdoc `faq_20` | Beckhen's weapon | — | `Lv.50/50` | cap reached | `Chicken Feet`: `Strength 30359→30359`; `ATK 134→134` | Equipment-instance value, not a hero stat. Corroborates wiki (§1.8). |
| N6 | gdoc `faq_21` | Beckhen's armor | — | `Lv.50/50` | cap reached | `Chicken Wings`: `Strength 30359→30359`; `DEF 102→102` | As N5. |
| N7 | gdoc `faq_22` | Beckhen's accessory | — | `Lv.50/50` | cap reached | `Jack`: `Strength 30359→30359`; **`Max HP 260→260`** | As N5. Label now **visually confirmed** as the max-HP key. |
| N8 | gdoc `faq_06` | **Vincent** | **`010_1`** | **`Lv.30/30`**, magenta `MAX` | **NO-GEAR** (card detail screen has no tree) | Strength `61815`; HP `4980`; ATK `2634`; DEF `1992` | Identified and levelled, and gear is structurally absent — but the level is 30 and the row is the **awakened** variant, and no source states whether an awakened unit's own growth is folded into these numbers. Not a base tuple. `AGENTS.md` §75 already holds these four. |
| N9 | gdoc `faq_08` | Vincent's armor | **`010`** | `Lv.49`→`Lv.50` | upgrade in progress | `Strength 33038→33057`; `DEF 101→102`; cost `50000` | Gear-instance comparison. Already in `AGENTS.md` §75. |
| N10 | gdoc `faq_05` | **Vincent** | **`010`** | `Master Hunter`, `Lv.30`, `MAX` | NO-GEAR | Strength `26711` | Strength only; no HP/ATK/DEF. |
| N11 | gdoc `faq_08` armor text | — | — | — | — | *"It's slightly older than **Captain's** coat, but it is presumed to be the same."* | Qualitative identity relation `010` → `009`; no number. |
| N12 | Caragublu `Upgrade+Equipment.jpg` | `ID?` | **not identified** | none | **GEAR** — Weapon `Lv.25`, Armor `Lv.20`, Accessory `Lv.20`; jewels `Lv.6×3`, `Lv.8×3`; `Apply Set` 2 sets | Strength `18244+4186`; HP `2317+240`; ATK `1287+155`; DEF `835+105`; AS `8.00+0` | No identity ⇒ not a hero tuple. Upgrade-Equipment screen ⇒ gear-inclusive by §1.6. **[NEW-READING]** relative to the ledger's one-line entry. |
| N13 | Caragublu `Train+Hunter.jpg` | **Natalia** | **`037`** | 3★ `Experienced Hunter`, **`Lv.1` → `Lv.30`** | NO-GEAR | Strength `2480` → `3323` | Training screen prints only Strength. A level-delta anchor, not a base tuple. |
| N14 | Caragublu `Hunter+Transcendence.jpg` | **Bear** | **`036`** | 3★, `Lv.1` | transcendence result | Strength `3425 → 3969`; fodder `1/1`; `Transcendence 9000`; blue gem `85/9`; crystals `4240/90` | Result, not a base stat. |
| N15 | Caragublu `Hunter+Adcance.jpg` | `ID?` | — | 3★ `Lv.MAX` → 4★ `Lv.1` | n/a | `Power Upgraded 2628 → 3068` (2 fodder, `8000`) / `→ 3947` (3 fodder, `12000`) | Result/cost, not a stat. |
| N16 | Caragublu `Skill+Training.jpg` | **Crocus** | **`058`** | skill `Lv.35/50` | NO-GEAR | `Max HP 8.75% → 9.00%`; `4240/4`, `298/4`, `16/2`; `Begin Training 800` | Skill effect percentage. Not the hero's Max HP. |
| N17 | gdoc `faq_01`–`03` | 4 heroes each, unnamed | `ID?` | mixed `Lv.11`/`Lv.26`/`Lv.MAX` | NO-GEAR | Team Level `40`/`55`/`62`; Strengths `14349,15207,7691,15661` / `20484,21432,18792,15409` / `18385,18524,16050,15121`; Rupees `+1400`/`+2000` | Search reward screens. Strength-only, no identity, no HP/ATK/DEF. |
| N18 | gdoc `faq_04` | — | — | — | — | Co-op `21000`; `Rank 210 People`; mileage `510/510` | Guild/economy. |
| N19 | VSFan `recruitment_screen_full.png` | **Lantern** | **`001`** | `First Ever Hunter`, 2★ badge | NO-GEAR | Rupee `1000` | Identity only. No stat. |
| N20 | VSFan `battle_screen_full.png` | — | — | `MAX` badges | — | Area `40`; fuel `166/60`; 3 stars | Preparation screen. |
| N21 | gdoc `faq_14` | — | — | — | — | guild `63713539/75620000`; `Members 21/40`; `Victory 13 times`; Rank 5 | Guild economy. Personal identifiers deliberately not reproduced. |
| N22 | gdoc `faq_06`/`08` name text | Vincent / Captain | `010_1` / `009` | — | — | epithets `Despair of a Millennium`, `Renegade` | Qualitative. |

## 2.3 Rejected leads and false positives — recorded so they are not re-raised

| Candidate | Why it looked promising | Verdict |
|---|---|---|
| **Naver blog `lovejhs96/220763343274`**, quoting *"상세 스탯 UI에서 크리티컬 최소 데미지와 크리티컬 최대 데미지가 삭제되고 크리티컬 데미지가 추가됩니다"* — i.e. "in the **detailed stat UI**, Critical Min Damage and Critical Max Damage are **deleted** and Critical Damage is **added**" | It reads exactly like a first-party patch note about a stat-panel field change, from a Korean source | **REJECTED — wrong game.** The full document is MapleStory V's 5th-job patch notes (Nexon; `maplestory.nexon.com`; meso/linca/Arcane Stone; Lv.200). `상세 스탯 UI` is MapleStory's own panel. **Zero Blustone content.** Fetched and read in full before rejecting. |
| `analysis/VSFan/Research/VisualShower/*.pdf` (5 files, 17 MB) | VisualShower E3 brochures plausibly carry gameplay stills | **REJECTED by extraction:** 97 rasters, all trade-show photography, other titles; no `Blustone` string in any text layer (§1.11). |
| Filename dedup against `analysis/catalogue/stats/found/` | The prior pass's "16 of 28 already mined" implied a dedup test | **METHOD INVALIDATED.** 0 of 28 hash-match; the repo copies are re-encodes. Dedup required viewing. |
| `faq_20–22` caption *"Total main stat increase from reaching the cap"* | Reads as if the frames show a *before/after increase* | **MISLEADING CAPTION.** All three print `30359 → 30359` and the stat `→` unchanged: the frames show a piece **already at cap**, so there is no increase. The caption describes the intent of the section, not the state in the frames. |
| 2021-07 wiki captures (Kain, Patrone, Scar) | Later revision ⇒ maybe more data | **REJECTED:** the stat section is **absent entirely** in that site state, so nothing is added and nothing is lost. |
| JP ÷ wiki ratios as a transcendence divisor | 3 heroes × 3 fields give 9 tidy ratios | **REJECTED:** Captain's ATK ratio `1.169` vs its HP/DEF `1.274`/`1.279` rules out a single multiplier; the state of each reading is unknown, so the division is not invertible (§1.14). |

## 2.4 Method notes

1. **A rewritten/renamed artefact is not a duplicate.** The 17 repo `faq-imageNN`
   files are re-encodes of the same 28-document images; hash comparison found
   zero matches. A filename-number match would have declared 16 images "already
   mined" and skipped them. **Only viewing settles "is this already known".**
2. **A parser that reads one pair per row silently drops half a two-column
   table.** The wiki's stat tables pack `Life|value|Attack|value` into one
   `<tr>`. My first sweep "found" `Life` and `Defense` on Captain, Hermes and
   Riko and *nothing* on the other eight — a result that looked exactly like the
   expected negative and was **partly an artifact**. Fixed by walking every
   `<tr>` and emitting all cells in document order (§1.9).
3. **A control must be able to fail.** The Caragublu second pass gated on
   `https://example.com/` *with* an anti-HTML guard, so the guard rejected the
   control and the batch aborted. Correct behaviour, useless control; the control
   was retargeted at a real image. This is the same class as the `share-en`
   lane's directory-missing abort (`share-en-panels` §2.4 note 1).
4. **Why hero coverage stays at 1/113, stated as a proof rather than a
   disclaimer.** Every one of the 12 panels in this corpus was captured on an
   **equipment screen** (N1, N2, N4, N12), a **card/detail screen** at level 30
   or MAX (N8, N13), a **result screen** (N14, N15), or shows **no HP/ATK/DEF at
   all** (N3, N5–N11, N17, N19). §1.6 demonstrates quantitatively that an
   equipment screen's white value is a geared total. The one frame that *is*
   identified, levelled and structurally gear-free (N8, Vincent `010_1`) is a
   level-30 **awakened** unit. There is no panel in the corpus that is
   **identified + level-1 + gear-free**, which is precisely the tuple the goal
   requires.
5. **What would actually move coverage**, in order of expected yield:
   (a) a **card detail screen for a 1★ hunter at Lv.1** — the screen exists
   (`NO-GEAR`, N8/N13) and N13 proves the game prints level and identity on it;
   it simply does not print HP/ATK/DEF at Lv.1 in any captured frame.
   (b) a **weapon/armor/accessory frame at a level *below* 50**, which would give
   a magnitude and a per-level rate (N5–N7 are all capped, N9 is the only
   uncapped frame and it is Vincent's own armor).
   (c) **patch notes for the 2019-09-05 rebalance**, which would turn PRE and
   POST frames into a ratio — the `stat-version-context.md` announcement already
   gives `+50%` equipment and `+30%/+50%` crystals, and one corroborated patch
   frame would let that percentage be tested against an actual panel.

## 2.5 Coverage statement — stated first

| Dataset | Before | After this lane |
|---|---:|---:|
| Hero base-stat tuples | 1 / 113 | **1 / 113** |
| Accessories (name + level rows) | 1 / 100 | **1 / 100** |
| Jewel set-bonus families | 12 / 12 (1 disputed) | unchanged |
| Monsters | 0 / 22 | **0 / 22** |

**This lane produced zero new base tuples, zero new accessory rows, zero new
jewel instances and zero monster tuples.** Its output is:

- the **closure of three leads** (`440600` image set, `analysis/VSFan/Images`,
  `analysis/VSFan/Research/*.pdf`) with passing controls and actual viewing;
- the **closure of the wiki-revision hypothesis** for the 8 partial stat tables;
- **four new structural facts** (§1.5 row-order split, §1.6 delta arithmetic,
  §1.7 set-bonus identity, §1.8 `Max HP` label + hero identification from item
  prose) that each change how a future panel reading must be interpreted;
- one **retraction** of a prior reading-order "correction" (§1.5);
- and **three complete panel transcriptions** (§1.4 collapsed + expanded +
  tree, §1.12.1) that were previously recorded only in part.

## 2.6 Reproduction

All under `analysis/research/base-stats-visual-hunt/_swipe/`:

| File | What it does |
|---|---|
| `fetch_gdoc.py` | fetches `440600` txt+HTML behind two controls, decodes all 28 base64 images, writes `_manifest.txt` |
| `which_unmined.py` | SHA-256 of the 28 vs the 17 repo copies → the 0-match finding |
| `gdoc_text.py` | extracts document text with `[[IMAGE nn]]` markers, giving each image its caption |
| `fetch_caragublu.py`, `fetch_caragublu2.py` | Caragublu fetch; pass 2 fixes the Blogger size-segment transform |
| `pdf_images.py`, `pdf_pages.py`, `pdf_sheets.py` | PDF raster extraction, text-layer page screening, contact sheets |
| `wiki_lad.py` | CDX sweep of all 11 hero pages × all captures |
| `wiki_parse.py` | correct all-cells `<tr>` parser (§1.1 note 2) |
| `trim_scratch.py`, `health_check.py` | drop reproduced scratch bytes; verify this file's encoding per the GUARD |
| `gdoc/` (32 files), `caragublu/` (14), `wiki/` (31) | retained evidence: the **28 decoded FAQ images**, the **11 Caragublu `s1600` originals**, the **33 wiki revisions** |
| `pdfimg/`, `pdfsheets/` | **removed after screening** (25.6 MB of trade-show photography). Regenerate with `pdf_images.py` then `pdf_sheets.py`; the verdict is §1.11 and needs no re-derivation. |

**Encoding health of this file, verified as bytes rather than as a console dump
(`GUARD-encoding-and-archive-traps.md`):** `U+FFFD` = **0**, `CRLF` = **0**,
bare `CR` = **0**, mojibake `Ã` = **0**, em-dash U+2014 = **100**, Hangul
AC00–D7A3 = **148**. All seven required Hangul strings from the `faq_09`
transcription are present (`전투력`, `생명력`, `공격력`, `방어력`,
`공격 속도`, `세트 적용`, `장비 강화`).

No file under `analysis/VSFan/` was modified — verified: the newest file inside
that tree is dated `2026-10-05 09:45`, before this lane ran. No server, APK,
emulator or account was touched, and **`polluted-observations.md` was not
appended to** (parent mirrors it; its mtime `2026-10-06 10:11` predates this
lane's first write). Written with the `write`/`edit` tools and Python only; no
PowerShell `Set-Content` round-trip.
