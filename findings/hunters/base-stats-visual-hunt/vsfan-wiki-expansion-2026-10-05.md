# `vsfan.net` wiki — `Character Attributes` expansion (2026-10-05)

**Lane:** follow-up to
[`vsfan-wiki-2026-10-05.md`](vsfan-wiki-2026-10-05.md), which reported **11**
hero `Character Attributes` stat tables — 3 complete, 8 partial — and stated
that the other 8 had their Life/Attack/Defense rows *"absent from the wikitext,
not blank."*

**This lane re-retrieved the corpus from the Wayback Machine without assuming
that report's conclusions, and answers four questions:**

| # | Question | Answer |
|---|---|---|
| 1 | Do the 8 partial tables hide Life/Attack/Defense for heroes nobody has numbers for? | **No. The rows do not exist, in any surviving revision, for any of the 8.** All 11 tables were recovered and parsed field-by-field. |
| 2 | Agreement against the 2019 JP database? | **108 comparisons · 97 equal · 11 different** — an exact, independent reproduction of the prior lane's figure from retrieved bytes. |
| 3 | Which of the 51 never-covered IDs does the wiki cover? | **None of the 51 as such.** The wiki's 55 characters are *all* already in the JP archive. Its only contact with that roster is **10 awakened (`_1`) rows via their base pages** — see §2.6. |
| 4 | `List_of_Hunters` 54 rows vs 57 hero pages? | **Fully reconciled**: 57 pages − 2 duplicate pages = 55 characters; 55 − 1 (`Beckhen`) = **54 rows**. `Sylvester Schwarzenegger` is a *display* variant linking to `/wiki/Sylvester`. |

**Bottom line: this lane adds ZERO new heroes with numbers.** The prior lane's
content ceiling was real and is now proven to be a property of the only
surviving revision of each page, not an artefact of retrieval method. The
genuine new facts are the revision-census proof (§1.2), the exact per-field
blank/populated map (§1.3), the caption census (§1.4), and the closed
57→55→54 reconciliation (§2.5). Nothing here changes any coverage percentage.

---

# 1. PURE

Everything in §1 is a verbatim reading of archived bytes. Section 1 contains no
inference and no interpretation. Where a value is absent from the source, that
absence is recorded rather than filled in.

## 1.1 Retrieval method, and the two archive traps actually hit

The prior lane queried CDX with `collapse=urlkey`, which returns **one** row per
URL. This lane swept the namespace **without collapsing**, to see whether later
revisions of a page hold more than the earliest capture.

**Trap 1 — a rewritten control is not a control.** HTTPS is refused on this host:

```
https://web.archive.org/          FAIL URLError [WinError 10061] actively refused
http://web.archive.org/           OK  200 145187 bytes
https://archive.org/              OK  200   1872 bytes
```

TCP 443 and DNS both resolve (`207.241.237.3`), so this is HTTP-layer, not
name-resolution. **All fetches here use `http://`.** An agent that assumed HTTPS
and read the refusals as "the archive is down" would have produced a false
negative; §2.2 is that trap's consequence.

**Trap 2 — 200 does not mean wiki content.** The `/wiki/` burst ends in
**15 byte-identical `域名停靠` ("domain parked") pages**, all captured
2021-07-29, all 3,357 bytes, all with **zero `<table>` elements** and a single
shared SHA-256 (`bd97685e4e171255310be44c…`). They are the post-mortem domain
expiry, not revisions. They are excluded everywhere below; including them would
have made 4 hero pages falsely read as "lost the stats table in a later
capture."

**Positive controls, run before any zero was read as real:**

| # | Probe | Result |
|---|---|---|
| 1 | CDX `url=vsfan.net/wiki/List_of_Hunters&matchType=exact` | **HTTP 200, 2 rows** |
| 2 | CDX `url=vsfan.net/wiki/Akasha&matchType=exact` | **HTTP 200, 3 rows** |
| 3 | `http://web.archive.org/` | **HTTP 200, 145,187 bytes** |
| 4 | CDX `url=vsfan.net/wiki&matchType=prefix&limit=20000`, **no collapse** | **HTTP 200, 8,888 rows / 1,234 distinct URLs** |

Row status over 8,888: `200` 5,185 · `-` 3,006 · `301` 687 · `302` 2 · `404` 8.

## 1.2 Revision census — the decisive negative

**Every single archived hero page exists in exactly ONE revision.**

| measure | value |
|---|---|
| Pages with ≥1 non-parking capture | **71** (57 hero pages + 14 index/list pages) |
| Pages with **>1 distinct `oldid`** | **0** |
| Captures-per-page histogram | 3 captures: 52 · 4 captures: 9 · 2 captures: 6 · 1 capture: 4 |

The prior lane's "the rows are absent from the wikitext" was therefore correct,
and this is now stronger than it was: the archive holds **no earlier or later
revision of these pages at all**. There is no un-retrieved revision in which the
Life/Attack/Defense rows might have existed. Repeated captures of the same
`oldid` are byte-different only in the surrounding MediaWiki chrome.

Per-hero `oldid`s are internally consistent across every capture:

| page | oldid | page | oldid | page | oldid | page | oldid |
|---|---|---|---|---|---|---|---|
| Bear | 7436 | Captain | 2323 | Diana | 7462 | Hermes | 7349 |
| Joy | 7456 | Kain | 7460 | Lantern | 7415 | Pansy | 7458 |
| Patrone | 7439 | Riko | 2615 | Scar | 7455 | | |

## 1.3 The 11 `Character Attributes` tables — every field, present vs absent

All 11 recovered. **Blank/present status is per-field and per-hero below.**
`—` means the label does not occur anywhere in that table's markup.

### 1.3.1 Complete tables (3) — caption `Transcendence Level: 3`

| field | Captain `009` | Hermes `023` | Riko `024` |
|---|---|---|---|
| caption | `Transcendence Level: 3` | `Transcendence Level: 3` | `Transcendence Level: 3` |
| **Life** | **2069** | **2275** | **2069** |
| **Attack** | **734** | **1218** | **868** |
| **Defense** | **1142** | **848** | **1047** |
| Attack Speed | 7 | 8 | 7 |
| Critical Damage Chance | 14% | 33% | 14 |
| Critical Damage | 180% | 200% | 185 |
| Armor Penetration | 1% | 0% | 0 |
| Block Chance | 33% | 14% | 33 |
| Block Resistance | 52% | 40% | 50 |
| Strengthen Elemental Attributes | 0% | 2% | 0 |
| Elemental Attack Resistance | 0% | 2% | 0 |
| Life Regeneration | 40 | 44 | 40 |

Note the **unit inconsistency inside the complete three**: Captain and Hermes
write percent signs, **Riko writes bare integers** — identical values, different
formatting. Riko is therefore *not* a percent-sign outlier of its own.

### 1.3.2 Partial tables (8) — Life/Attack/Defense absent from the markup

| field | Bear `036` | Diana `031` | Joy `035` | Kain `029` | Lantern `001` | Pansy `057` | Patrone `033` | Scar `032` |
|---|---|---|---|---|---|---|---|---|
| **caption** | *(none)* | *(none)* | *(none)* | *(none)* | *(none)* | *(none)* | *(none)* | *(none)* |
| **Life** | **—** | **—** | **—** | **—** | **—** | **—** | **—** | **—** |
| **Attack** | **—** | **—** | **—** | **—** | **—** | **—** | **—** | **—** |
| **Defense** | **—** | **—** | **—** | **—** | **—** | **—** | **—** | **—** |
| Attack Speed | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 8 |
| Critical Damage Chance | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 33 |
| Critical Damage | 180 | 180 | 180 | 185 | 180 | 185 | 185 | 200 |
| Armor Penetration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Block Chance | 33 | 14 | 14 | 36 | 14 | 14 | 14 | 14 |
| Block Resistance / Damage Reduction Block | 50 (Block Resistance) | 40 (Damage Reduction Block) | 42 (Damage Reduction Block) | 55 (Damage Reduction Block) | 42 (Block Resistance) | 40 (Damage Reduction Block) | 40 (Block Resistance) | 40 (Damage Reduction Block) |
| Strengthen Elemental Attributes | 5 | 5 | 5 | 5 | 0 | 5 | 5 | 0 |
| Elemental Attack Resistance | 5 | 5 | 5 | 5 | 0 | 5 | 5 | 0 |
| Life Regeneration | 32 | 38 | 43 | 45 | 38 | 44 | 38 | 45 |

**All 8 partial tables are otherwise fully populated — 9 of 9 sub-stat fields
plus Attack Speed.** None is blank in any cell. The absence is confined
*exactly* to the three core rows.

**`Scar 032` is newly retrieved by this lane** (the prior lane reported it but
its bytes were not re-verified here until now). It behaves exactly as predicted:
9 fields, all equal to the JP database, no caption.

### 1.3.3 Verbatim raw markup — proof the values are real text

Bear (partial). Note the table jumps **straight** from the header to a single
`colspan="3"` Attack Speed row. There is no Life/Attack/Defense row and no
`<caption>` element anywhere:

```
<tbody><tr>
<th colspan="4">Character Attributes
</th></tr>
<tr>
<td colspan="3">Attack Speed
</td>
<td style="text-align:right;">7
</td></tr>
<tr>
<th colspan="4">Stat Details: Attack
</th></tr>
<tr>
<td colspan="3">Critical Damage Chance
</td>
<td style="text-align:right;">14
</td></tr>
…
<tr>
<td colspan="3">Life Regeneration
</td>
<td style="text-align:right;">32
</td></tr></tbody></table>
```

Captain (complete) — the two-row `Life|Attack` / `Defense|Attack Speed` layout
and the caption, verbatim:

```
<caption>Transcendence Level: 3
</caption>
<tbody><tr>
<th colspan="4">Character Attributes
</th></tr>
<tr>
<td>Life</td>
<td style="text-align:right;">2069</td>
<td>Attack</td>
<td style="text-align:right;">734
</td></tr>
<tr>
<td>Defense</td>
<td style="text-align:right;">1142</td>
<td>Attack Speed</td>
<td style="text-align:right;">7
</td></tr>
```

## 1.4 Caption census — and why "no caption" is not "base"

| tables | count | caption | what the caption establishes |
|---|---|---|---|
| Captain `009`, Hermes `023`, Riko `024` | 3 | `Transcendence Level: 3` | **Transcendence level only.** Not level, not rank, not gear. |
| Bear, Diana, Joy, Kain, Lantern, Pansy, Patrone, Scar | 8 | **none — no `<caption>` element at all** | **Nothing whatsoever.** |

**Stated explicitly, per the standing rule:** for **each** of the 8 partial
heroes — Bear `036`, Diana `031`, Joy `035`, Kain `029`, Lantern `001`,
Pansy `057`, Patrone `033`, Scar `032` — **the table carries no caption, and no
other text on the page states a level, rank, transcendence state or equipment
state for the stat table.** Their 9 populated fields therefore have **zero
declared state context**. The page's `Fan Art` / equipment / skill sections do
not qualify the table.

## 1.5 Corpus-wide proof that only 3 heroes ever carry core stats

An exhaustive, cell-aware sweep of **every** table row in **every** non-parking
capture — pairing any cell labelled `Life` / `Attack` / `Defense` (plus
synonyms `hp`, `health`, `vitality`, `stamina`, `atk`, `def`, `defence`) with
any numeral following it in that row:

| page | Life | Attack | Defense |
|---|---|---|---|
| Captain | 2069 | 734 | 1142 |
| Hermes | 2275 | 1218 | 848 |
| Riko | 2069 | 868 | 1047 |

**3 of 71** archived pages carry any Life/Attack/Defense numeral at all. There
is no other hero stat table anywhere in the corpus, and no alternative-labelled
column hiding the same data.

## 1.6 Cross-source agreement against the 2019 Japanese database

Same label→JP-column mapping and same unit convention as the prior lane
(`14%` → `14`). Compared hero-by-hero on
[`archived-hunter-database-2019.tsv`](archived-hunter-database-2019.tsv).

> **108 field comparisons · 97 equal · 11 different.**

The 97 equal fields are **all** Attack Speed, Critical Damage Chance, Critical
Damage, Armor Penetration, Block Chance, Block/Damage-Reduction,
Strengthen Elemental Attributes, Elemental Attack Resistance and Life
Regeneration, for all 11 heroes. Every difference is listed:

| hero | field | wiki | JP 2019 | ratio |
|---|---|---|---|---|
| Captain `009` | hp | 2069 | 1624 | 1.2740 |
| Captain `009` | atk | 734 | 628 | **1.1688** ← outlier |
| Captain `009` | def | 1142 | 893 | 1.2788 |
| Captain `009` | hp_regen | 40 | 41 | — (off-by-one) |
| Hermes `023` | hp | 2275 | 1750 | 1.3000 |
| Hermes `023` | atk | 1218 | 937 | 1.2999 |
| Hermes `023` | def | 848 | 653 | 1.2986 |
| Riko `024` | hp | 2069 | 1624 | 1.2740 |
| Riko `024` | atk | 868 | 682 | 1.2727 |
| Riko `024` | def | 1047 | 821 | 1.2753 |
| Riko `024` | hp_regen | 40 | 41 | — (off-by-one) |

**Reproduction check.** Before retrieving `Scar`, this lane held 10 heroes and
measured **99 / 88 / 11**. That implied `Scar` contributes exactly 9 further
all-equal fields. On retrieval, `Scar` did exactly that — **108 / 97 / 11**. The
prior lane's arithmetic is independently confirmed.

## 1.7 `List_of_Hunters` — the 54 rows, extracted

Capture `20191114021317`, `oldid 7480`. The sortable table has **55 `<tr>` = 1
header + 54 data rows**, 54 distinct names, **zero duplicate names**.

Every row carries the name as a link plus per-hero skill names. Rarity/role/
element are icons, recovered from `alt` attributes:

```
  Captain        rar=1  role=Defense  elem=Electric  | Attack skill / Block chance up / Defense up / Speed up / Armour Pen
  Vincent        rar=4  role=Offense  elem=Electric  | Attack skill + Disables immunity / Immunity / Attack up / Speed up
  Lantern        rar=3  role=Bomber   elem=Fire      | Attack skill / Enemy def down / Team attack up / + Skill damage /
  …
  Sylvester Schwarzenegger rar=1 role=Offense elem=Fire | Attack skill / Dmg up / Attack up / + Skill damage / Crit chance u
  …
  Juno           rar=3  role=Defense  elem=Fire      | Dmg over time60px / Reduce enemy defence60px / Defense up / Damage
```

Distribution over the 54 rows: rarity 1★ 11, 2★ 10, 3★ 29, 4★ 4 · role Offense
17, Defense 15, Bomber 11, Support 11 · element Fire 18, Ice 19, Electric 17.

## 1.8 Identity metadata agreement — sortable table vs hero-page infobox

Per character, all three fields:

> **52 of 54 agree on all three fields (rarity, role, element); 2 disagree.**

| character | sortable table | hero-page infobox | field |
|---|---|---|---|
| Pansy `057` | 3 / Support / **Ice** | 3 / Support / **Electric** | element |
| Robin `018` | **1**★ / Defense / Ice | **2**★ / Defense / Ice | rarity |

These reproduce the two disagreements the prior lane flagged, now located in a
**second, independently structured source** (a sortable table rather than an
infobox). Nothing here resolves *which* value is correct.

---

# 2. UNPUR

Everything in §2 is a numeral or a claim with unresolved identity, level, gear,
unit, or era. **None of it counts toward base-stat coverage.** Per §15 of the
project's reporting rules and the supplementary-deliverable rule, a partial
field is never presented as a base stat.

## 2.1 The 8 partial heroes gain no base stat, and no new identity

The 8 partial heroes are Bear `036`, Diana `031`, Joy `035`, Kain `029`,
Lantern `001`, Pansy `057`, Patrone `033`, Scar `032`. For **each**, the
Life/Attack/Defense value does not exist in the only surviving revision, so:

- **no Life/Attack/Defense reading is recorded for any of them from this source**;
- their 9 populated fields are **already held, identically, from the 2019 JP
  archive** (§1.6 — 97/97 equal), so they add **no new field for any hero**;
- and because **all 55** wiki characters already have numeric rows in the JP
  archive (**0 missing**, verified), the wiki **introduces no hero the project
  did not already have numbers for.**

The premise that these partials "may hold Life/Attack/Defense for heroes nobody
has numbers for" is **falsified**. The rows are absent, not withheld, and the
heroes are all already covered.

## 2.2 The three complete tuples are Transcendence-Level-3, and remain UNPUR

Captain `009`, Hermes `023`, Riko `024` do carry Life/Attack/Defense, captioned
**`Transcendence Level: 3`**. These are therefore **boosted, advanced-state
values**. The caption supplies the transcendence state and nothing else: **not
level, not rank, not equipment, not jewels, not skills.**

The prior lane's candidate multiplier **≈1.27–1.30** is reproduced here
(Hermes 1.2999/1.3000/1.2986; Riko 1.2740/1.2727/1.2753; Captain
1.2740/**1.1688**/1.2788). Two cautions stand:

- **Captain's Attack ratio 1.1688 is an outlier** against its own hp 1.2740 and
  def 1.2788. A single uniform multiplier does not fit all three heroes. The
  multiplier is **not pinned** and must not be used to de-boost anything.
- The two `hp_regen` off-by-ones (wiki 40 vs JP 41, both Captain and Riko) are
  **unexplained**; they are *not* covered by the ratio.

## 2.3 Era tag — applies to every numeral in this report

These are **community wiki edits of unknown authorship and unknown date**. The
archived captures span 2017-08-25 → 2021-07-29, but the **game-content burst is
2019-08-21 → 2019-09-23**, and each page carries a single frozen `oldid`
(§1.2). Consequences:

- **The edit date is unknown.** A page captured in 2019 may hold numbers
  transcribed from any earlier version of the game.
- **No page states its own version.** Nothing here is tied to 2.8.0.1, and
  nothing is tied to any patch.
- **Relative to the 2019-09-05 rebalance** documented in
  [`stat-version-context.md`](stat-version-context.md) — equipment +50%,
  1–3★ crystal main +30%, 4–5★ +50%, all substats +50% — the wiki's **2019-08**
  captures are **pre-rebalance**. This is a reason for extra caution in reading
  any of these numbers as balance evidence; it is **not** a licence to adjust
  them by the stated percentages, which are per-item and not per-hero.
- The three complete tables are T3-boosted, which is a **2019-era endgame
  state** for characters that are ★1–★★3 on draw.

## 2.4 What the 9 sub-stats legitimately add

Nothing under coverage, but two real observations:

1. **They are not contaminated by the T3 boost.** Every sub-stat matches the
   unboosted JP row exactly, all 11 heroes, 97 fields. So the boost applies to
   Life/Attack/Defense and leaves the sub-stat block untouched — consistent with
   the sub-stats being equipment-slot-derived and the core rows being
   card-base-derived. This is an **inference from the pattern**, not a recovered
   rule.
2. **Label drift is real and split.** `Block Resistance` vs `Damage Reduction
   Block` is used inconsistently across heroes for the same JP column
   (`block_damage_reduction`). Any future parser must accept both, and must not
   treat them as two different stats.

## 2.5 The 57 → 55 → 54 reconciliation, closed

| step | count | basis |
|---|---|---|
| Archived hero **pages** | **57** | `Card_stat_divergence` §1.5 hero-page set, re-derived from the sweep |
| − duplicate pages | **−2** | `Karl` / `Karl_Steiner` are both `012`; `Teddy_Bomber` / `TeddyBomber` are both `025` (each pair shares one `oldid`) |
| = distinct **characters** | **55** | also = 55 distinct catalogue IDs |
| − `Beckhen` | **−1** | present as a hero page, **absent from the 54-row sortable table** |
| = `List_of_Hunters` rows | **54** | 55 `<tr>` minus 1 header; 54 distinct names, no duplicates |

**The `Sylvester` false discrepancy, resolved by markup not by name.** Row 9
displays the text **`Sylvester Schwarzenegger`**, which has no hero page. Its
`href` is `/wiki/Sylvester`:

```
Sylvester   displayed as: ['', 'Sylvester Schwarzenegger']
```

So the sortable table contains **all 54 of its 54 names as real article links**
and has no name without a page. `List_of_Hunters` is therefore **missing
exactly one character — `Beckhen` `051`** — and is *incomplete*, not
over-complete. This is the only roster gap in the corpus, and it is a **missing
row, not a missing hero**: `Beckhen` has its own page and its own JP numeric row.

Two supporting checks:

- **Element balance over 55 characters is 18/18/19** (Electric/Fire/Ice), not
  19/19/19. The prior lane's "exactly 19/19/19 — a deliberate balance" is true
  **only over the 57 pages**, where the duplicate pages happen to split one to
  Electric and one to Fire. Over distinct characters it is **18/18/19**. The
  "deliberate balance" reading does not survive deduplication and should not be
  cited.
- **Role balance over 55 characters**: Offense 18, Defense 15, Bomber 11,
  Support 11 (the 57-page figures of 19/15/12/11 each fold one duplicate in).

## 2.6 Cross-reference against the 51-ID never-covered roster

`uncovered-archive-roster-2019.tsv` lists 51 catalogue IDs the JP 2019 archive
never gave a numeric row. **The wiki covers none of them as such.**

Exact base-ID intersection of the wiki's 55 characters with the 51:

```
EXACT base-ID overlap: ['004','005','009','010','011','017','019','020','021','024']
name-based matches   : []
```

**These 10 are the *base* forms; the roster's entries are the *awakened* `_1`
forms.** Reading the roster precisely:

| roster ID | roster name | base ID | base has a wiki page? |
|---|---|---|---|
| `004_1` | Tyltyl (Awakened) | 004 | yes — Tyltyl |
| `005_1` | Gerard (Awakened) | 005 | yes — Gerard |
| `009_1` | Captain (Awakened) | 009 | yes — **Captain** |
| `010_1` | Vincent (Awakened) | 010 | yes — Vincent |
| `011_1` | Hecate (Awakened) | 011 | yes — Hecate |
| `017_1` | Lapis (Awakened) | 017 | yes — Lapis |
| `019_1` | Balian (Awakened) | 019 | yes — Balian |
| `020_1` | Sienna (Awakened) | 020 | yes — Sienna |
| `021_1` | Rebecca (Awakened) | 021 | yes — Rebecca |
| `024_1` | Riko (Awakened) | 024 | yes — **Riko** |

So **10 of the 51 awakened rows have a base-form wiki page — and 2 of those 10
(`009_1` Captain, `024_1` Riko) are the two pages whose stat tables are
complete.** That is the single most interesting structural fact this lane
found, and it is **still not a base tuple**:

- The values are captioned `Transcendence Level: 3`, so they are a **boosted
  state**, not the awakened *base*.
- The wiki page is titled `Captain` / `Riko`, and its infobox rarity is **★1 /
  ★★2 — the base form's rarity**, not the roster's 5★.
- **That `Transcendence Level: 3` is the same state as the catalogue's `_1`
  "Awakened" row is NOT proven.** Transcendence and star-advancement are
  different mechanics in this game's own documentation
  (`Guide_to_Blustone`: transcendence needs a 4★/5★ base for T2/T3, whereas the
  roster's `_1` rows are 5★). Equating them would be exactly the kind of
  inference this project's rules forbid. **Recorded as an open question, not a
  result.**

The remaining 41 roster IDs (`056`, `056_1`, `064`–`098`, `026_1`, `034_1`,
`038_1`, `086`, `086_1`, `087`, `088`, `095`) have **no wiki page of any kind**.
The wiki's 57 pages are all pre-`056`; it has nothing on the 4★ 2019-era roster
or on `Genovia`.

## 2.7 Heritage: this lane adds nothing to `coverage.md`

| metric | before | after this lane |
|---|---|---|
| Hero base HP/ATK/DEF tuples | 1/113 | **1/113 — unchanged** |
| Monsters | 0/22 | **0/22 — unchanged** |
| Jewelry / accessories | unchanged | **unchanged** |
| Heroes newly given a base tuple | — | **0** |

The one hero with an identified, gear-separated base line remains Beckhen
`051` (`analysis/catalogue/stats/010.md` calibration), and the three complete
wiki tables stay in the UNPUR register because they are T3-boosted.

## 2.8 Limits of this lane

1. **Edit dates are unknown.** Capture date ≠ edit date (§2.3).
2. **No level, rank or gear context** for any of the 11 tables; for the 8
   partials, **no context whatsoever** (§1.4).
3. **The ≈1.27–1.30 multiplier is not pinned** — Captain's Attack is a 1.1688
   outlier and the two `hp_regen` off-by-ones are unexplained (§2.2).
4. **`Transcendence Level 3` ↔ catalogue `_1` "Awakened" is an open
   hypothesis**, not a finding (§2.6).
5. **Identity metadata disagrees in 2 of 54** between the sortable table and
   the infoboxes (Pansy element, Robin rarity), unresolved in either direction
   (§1.8).
6. **The "19/19/19 deliberate element balance" does not survive
   deduplication** (18/18/19 over 55 characters) and should not be cited
   (§2.5).
7. **`Beckhen` is missing from the roster table**, so the roster's completeness
   is itself unverified against any other source.
8. **One page, `Riko`, has only a single capture.** Its bytes are internally
   consistent, but it has no cross-capture check available.
9. No hero-page numerals were found in any *other* table type (equipment,
   skill, story) beyond what §1.5 and the prior lane already logged.

---

# 3. Reproduction

Scripts and the retrieved cache live in this directory. All are read-only with
respect to the game, the workspace, and any account.

| script | purpose |
|---|---|
| `vsx-fetch.py`, `vsx-retry.py` | CDX sweep (no collapse) + revision retrieval over **`http://`** |
| `vsx-parse.py` | per-revision `Character Attributes` extraction → `_wf1_cache/stats-tables.json` |
| `vsx-revcensus.py` | distinct-`oldid` census → `_wf1_cache/rev-census.json` |
| `vsx-sweep.py` | corpus-wide Life/Attack/Defense sweep, parking pages excluded |
| `vsx-agree.py` | field-by-field JP comparison → `_wf1_cache/agreement.json` |
| `vsx-list.py`, `vsx-listcheck.py` | `List_of_Hunters` rows + link-target proof |
| `vsx-reconcile.py`, `vsx-crossref.py` | 57/55/54 arithmetic and roster cross-reference |
| `vsx-final.py` | single consolidated pass → `_wf1_cache/final.txt`, `final.json` |
| `_wf1_cache/raw/` | the retrieved archived HTML, one file per capture |
| `_wf1_cache/cdx-wiki-all.json` | the 8,888-row uncollapsed CDX result |

Encoding: all scripts force UTF-8 stdout (`sys.stdout.reconfigure`) because the
host console is cp1252 and renders CJK as mojibake — per
[`GUARD-encoding-and-archive-traps.md`](GUARD-encoding-and-archive-traps.md)
rule 2, that is a console artefact, not file corruption. No file was written
through PowerShell.

**Provenance note.** `vsfan.net` is NXDOMAIN and its Miraheze successor
(`vsfanwiki.miraheze.org`) returns `Wiki not found`; the Wayback Machine is the
only surviving copy found. Re-verified this session over `http://`.