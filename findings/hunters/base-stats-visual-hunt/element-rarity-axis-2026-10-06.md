# Element and rarity/grade axes for heroes — icon calibration, the shipped-table audit, and the crosswalk

**Purpose.** Recover the two identity axes that
[`job-tag-attestation-2026-10-06.md`](job-tag-attestation-2026-10-06.md) closed for
role and explicitly left open: **element** and **rarity/grade**. The method asked
for is icon calibration — find an element icon or a star badge in shipped or
original art, calibrate the glyph against heroes whose element is already known
from several independent sources, then apply the mapping. This file reports what
that calibration can and cannot support, and — more importantly — two **clean
negatives that permanently close the "some shipped table must have it" question**,
plus a measured upgrade to the standing of the community catalogue's element and
rarity columns.

**Coverage effect: NONE, by construction.** Strict coverage stays **heroes 1/113 ·
accessories 1/100 · monsters 0/22**. Element and rarity are identity attributes.
Nothing here is a base stat, a level, or a gear state. `coverage.md` is untouched
and `polluted-observations.md` was **not** appended (the parent mirrors that lane).

**Headline answers to the three questions asked.**

1. **Does any shipped LevelDB table carry element or rarity?** **No — and this is
   now a closed question, not an open search.** All thirteen shipped tables were
   enumerated and audited (§1.1), and all seven hundred seventy-four shipped JET
   resource packs were scanned for icon art (§1.2). Both scans are negative with
   positive controls. The per-card fields live only in the **HTTP-served card
   reference**, which the original server owned and which no longer exists.
2. **Does an icon→element mapping exist that can be applied?** **Measured, but not
   applicable.** Two of the four element codes have a measured disc colour, on a
   calibration set of **five observations covering two classes** (§1.3). That is
   far below the ~8-example floor set for this task, so **no hero's element is
   derived from an icon anywhere in this file.**
3. **Which of the uncovered ids can be assigned?** Four, on element and only as
   flagged inferences: `026_1` `034_1` `038_1` `086_1` (§2.2). One more, `085`,
   moves from *no source at all* to *one source* (§2.4). The remaining six stay
   unresolved, and §2.3 shows why the obvious inference for them is **falsified**.

**Section discipline.** §1 is **PURE** — measured observations with exact paths and
calibration sets. **Digits inside a `file:line` citation are pointers, not data.**
Every count, purity figure, error rate and slot index is quarantined in §2.

**Read-only.** No catalogue, server, fixture, seed, state, APK, emulator or phone
file was read-modified or written. `server-ts/src/bootstrap.ts` was **read** to
establish what the local replica publishes as `attr`, and that is labelled as a
fixture read wherever it is used. Helper scripts were written only under
`%TEMP%\opencode\elrar\`. Written per `GUARD-encoding-and-archive-traps.md`: the
`write` tool plus Python `encoding='utf-8'`, never a PowerShell
`Get-Content`/`Set-Content` round-trip; U+FFFD count and CRLF count verified
zero after writing.

---

# 1. PURE — the evidence

## 1.1 The shipped LevelDB inventory is complete, and none of it carries element or rarity

This is the decisive negative, and it is complete rather than partial.

| item | value |
|---|---|
| extraction | `analysis/recovered-data/leveldb-tables/all-tables.json` |
| tables | **13** — `ADMIN_ID_RO` `BADWORD_RO` `CHAR_STR_RO` `INGAME_TALK_RO` `SKILL_DESC_RO` `SKILL_EFFECT_RO` `SKILL_REF_RO` `SKILL_TAG_RO` `TAG_REF_RO` `UI_EPISODE_RO` `UI_JSON_RO` `UI_TEXT_RO` `UI_XML_RO` |
| rows | **18 105** |
| text leaves scanned | **10 348 020 characters** (every string key and every string value, recursive) |
| on-disk source | `recovered-assets/phone-2026-09-18/game-assets/` — **28 entries**: exactly those thirteen tables (nine as `*.db` directories, four as bare directories) plus `E_NEW.jet` and `E_MIDAGE.jet` |

The `game-assets` listing is the point: **there is no thirteenth-plus table.** A
directory walk of the whole `recovered-assets/` tree found only three `.db`
filesystem objects and all three are Google Analytics databases, not game
tables. So the thirteen tables *are* the app's entire shipped LevelDB content.
The per-card reference — name, element, role, rarity — is served over HTTP by the
dead server, which is consistent with everything the project has recovered from
`/reference/GetCard` and with `catalogue/INDEX.md` §7.3.

**Per-table column shapes.** Only four tables have any column beyond the
localised-text set, and none is element or rarity:

| table | columns beyond `key`/`raw` |
|---|---|
| `SKILL_TAG_RO` | `TAG_KEY` |
| `TAG_REF_RO` | `KO` `EN` `JA` `SC` `TC` |
| `CHAR_STR_RO` | `KO` `EN` `JA` `SC` `TC` |
| `UI_JSON_RO` | `TEXT` `FONT` `SIZE` `ALIGN` `COLOR` `LSPACE` `TSPACE` `B_RECT` `B_SIZE` `B_ALIGN` |

Everything else is `key` / `raw` / `json` plus locale columns. There is not one
numeric per-card column anywhere in the shipped tables.

**Keyword audit with positive controls.** Nine regex families were run over the
full 10.3 MB of text leaves — English `fire|ice|lightning|element`, Japanese
`炎|冷気|電撃|属性`, Korean `화염|냉기|번개|속성`, key-shaped `attr|attribute` and
`elem|element`, `star|grade|rarity`, `★|☆`, and `N-star`.

| table | CTRL `JOB_ATT` | CTRL `Offense` | EN element | JA element | KO element | `attr` key | `elem` key | `star` | `★/☆` |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `SKILL_TAG_RO` | **70** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `CHAR_STR_RO` | 0 | **70** | 68 | 162 | 52 | 0 | 6 | 0 | 160 |
| `TAG_REF_RO` | **2** | **8** | 2 | 4 | 2 | 0 | 2 | 0 | 0 |
| `UI_JSON_RO` | 0 | **8** | 6 | 66 | 74 | 2 | 6 | 12 | 264 |
| `UI_TEXT_RO` | 0 | **12** | 22 | 122 | 88 | 0 | 14 | 14 | 359 |
| `UI_XML_RO` | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
| `INGAME_TALK_RO` | 0 | 0 | 18 | 2 | 0 | 0 | 0 | 0 | 0 |
| `SKILL_EFFECT_RO` | 0 | 0 | 0 | 24 | 12 | 0 | 0 | 0 | 0 |
| `SKILL_REF_RO` | 0 | 0 | 0 | 120 | 60 | 0 | 0 | 0 | 0 |
| `UI_EPISODE_RO` | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 0 |
| `SKILL_DESC_RO` | 0 | 0 | 0 | 32 | 16 | 0 | 0 | 0 | 0 |
| `BADWORD_RO` | 0 | 0 | 2 | 16 | 16 | 0 | 0 | 0 | 0 |
| `ADMIN_ID_RO` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

The two control columns are the load-bearing part: `JOB_ATT` is *known* to occur
70 times in `SKILL_TAG_RO` and is found 70 times; `Offense` is *known* to occur in
`CHAR_STR_RO` and `TAG_REF_RO` and is found in both. **The scanner works.** Every
non-zero cell in the nine audit columns is then inspectable, and inspection
shows what they actually are:

- **`CHAR_STR_RO`'s 68 English element words and 160 `★` glyphs are prose and
  pseudo-card titles.** The `★` glyphs occur on exactly eight rows, all of them
  the Trainer / Transcendence Ticket pseudo-cards: `901`…`904` and `912`, `913`,
  `914`, `x914`, whose shipped `TITLE` is literally `★1 Trainer` … `★4
  Transcendence Ticket` and whose `VICTORY` text says "use instead of ★N hunters"
  (`char-str.tsv:100-107`). **No hero row carries a `★`.**
- **`UI_JSON_RO`'s `attr`/`star` hits are Korean UI strings**, e.g. the keys
  `★1|1star|EN`, `★2|2star|EN`, `★2 이상 확정|2STAR|EN`, `★4 이상 확정|4STAR|EN`,
  `3성 헌터 섭외|TX_SE_3HT_T|KO`. These are *gacha product tiers* — the game names
  its "1-star" and "2-3-star" recruitment pools as first-class things — and they
  confirm the vocabulary exists, but they are **not per-card assignments**.
- **`UI_XML_RO`'s single element hit is the hunter detail layout**, and it is
  genuinely informative about the *field name*. `KO/SR_ENHANCE/3_SR_EN_CH/HB_DETAIL_T1`
  contains two tooltip-bearing rects:

  ```xml
  <rect name="CLASS" ...><tooltip ... param="card_role"/></rect>
  <rect name="ELEMENTAL" ...><tooltip ... param="card_attr"/></rect>
  ```

  with byte-identical siblings at `SE_DETAIL_T1` and `TR_DETAIL_T1`. Across all
  584 rows there are exactly **eight** distinct `param=` values: `card_role`
  (×3), `card_attr` (×3), `skill_1`…`skill_5` (×2 each), and one unrelated
  pair. **`card_attr` is the shipped name for the element field**, and the detail
  panel is the surface that displays it. That is a recovered field name, not a
  per-card value.

**Conclusion for §1.1.** No shipped structured field carries element or rarity for
any card. This permanently closes that question in the negative, with control
evidence. It also **agrees with and upgrades** the existing statement in
`job-tag-attestation-2026-10-06.md` §1.10, which reached the same conclusion for
the five tables it examined; the scope there is now the whole shipped set.

## 1.2 The shipped art inventory contains no element icon and no draw-rarity badge

The obvious hope was that a per-hero art pack carries a badge. Tested and
negative, twice, with controls.

**Test A — the per-hero `_Q` packs.** `analysis/extracted/assets/` holds 787
files; 160 are `*_Q.jet`, and they exist for **every** hero and costume variant
(`C001_Q` … `C098_Q` plus `C003A_Q`, `C028B_Q`, …). Using the read-only JET
decoder (`tools/jet-viewer/jet_decoder.py`), every embedded PNG was extracted
and SHA-256'd: **2 251 PNG payloads**, **1 758 distinct hashes**, every pack
parsed successfully (positive control: the PNG count per pack is 14 on 112 packs,
15 on 35, with the balance being smaller variant packs).

The decisive statistic is **element purity**: for each image hash, take the set of
distinct base heroes whose pack contains it, restrict to heroes with a known
element, and measure the fraction in the modal element class. The background rate
is the largest single class among known base heroes.

| image hash (prefix) | dims | base heroes | heroes with known element | element purity |
|---|---|---:|---:|---:|
| `23b70d30fb4b7c8b` | 96×97 | 5 | 3 | 0.667 |
| `27617f91076caab7` | 84×29 | 5 | 3 | 0.667 |
| `be22d14e47e3768d` | 84×29 | 4 | 4 | 0.500 |
| `e1a4cde063aecb4a` | 84×29 | 27 | 27 | 0.407 |
| `74881a0642246a1e` | 175×210 | 41 | 38 | 0.395 |
| `2957629a388e39be` | 110×110 | 44 | 40 | 0.375 |
| `2d92b35487e3e3c5` | 96×97 | 34 | 32 | 0.344 |

**Background rate: 0.349.** Every large-sample image sits at or below it; the only
values above it are on three- and four-hero samples, where 0.667 on n=3 is what
you get from noise. Rarity purity peaks at 0.750 on an n=4 sample. **No image in
any per-hero art pack predicts element or rarity.** The four heavily-shared images
are frames and plates — a 110×110 portrait base, a 175×210 portrait plate, a
96×97 plate, an 84×29 name plate — and their membership lists are visibly
alphabetical stretches of hero ids, not classes.

**Test B — every shipped pack.** The same decode was run over **all 774 JET
packs**: **9 873 PNG payloads, 9 110 distinct hashes**, all 774 packs inspected
without error (positive control: the Test-A hash `2957629a…` is re-found in 58
distinct packs). Results:

- exactly **four** hashes are shared by ≥30 distinct packs, and all four are the
  `_Q` frames already shown to be element-neutral;
- **zero** icons of ≤64 px on a side are shared by ≥6 packs — in fact no small
  shared icon set exists anywhere in the recovered resource corpus.

So the element disc that the game demonstrably renders (§1.3) is **not present in
any recovered art pack**. Its source is the HTTP-served UI package that the
original server owned, or engine-generated geometry. Either way it is gone, and
**no shipped art can calibrate it.**

## 1.3 The element icon is rendered in-game — two of four codes measured

The icon *is* on screen, in the same panel `UI_XML_RO` names. Five observations,
each with an exact path. Disc colour is reported as the modal quantised RGB of the
disc region after removing near-white pixels, which is a reproducible measurement
rather than an impression; glyphs are described by eye at 4× nearest-neighbour.

| # | hero | source of the element value | element | disc colour (modal) | class disc | glyph | frame provenance |
|---|---|---|---|---|---|---|---|
| 1 | `001` Lantern | archive `火炎` + wiki + Episode `attr` 1 | **Fire** | **`#B82810`** | `#807050` (olive) | white two-tongued **flame** | **original game**, VisualShower press kit, with the word "Fire" printed beside the icon |
| 2 | `004` Tyltyl | archive `火炎` + wiki (fixture `attr: 1`) | **Fire** | **`#B82810`** | `#686868` (grey) | white two-pronged mark | local replica run |
| 3 | `003` Nene | archive `冷気` + wiki + Episode `attr` 2 | **Ice** | **`#00D8E8`** | `#686868` (grey, **shield** glyph) | white soft crystal | local replica run |
| 4 | `051` Beckhen | archive `冷気` + wiki + Episode `attr` 2 | **Ice** | **`#00D8E8`** | grey/brown | white soft crystal | **original game** (community FAQ capture) |
| 5 | `010_1` Vincent Awakened | wiki (Ice) + original frame | **Ice** | cyan by eye; the automated colour crop missed the disc | `#686868` (grey, crossed swords) | white soft crystal | **original game** (community FAQ capture) |

Paths:

1. `analysis/VSFan/Images/Blustone/Screenshots/Original/recruitment_screen_full.png`
   — the official VisualShower recruitment **share card**. Bottom-left: a gold ring
   enclosing **three gold stars**. Bottom-right: role icon labelled "Bomber" and
   element icon labelled **"Fire"**.
2. `analysis/testing/revival-007/05-tyltyl-details.png` — in-game `See Details`
   panel; rects `Class` and `Elemental`, `LV.1`, "Amateur Hunter".
3. `analysis/testing/revival-006/19-nene-details.png` — in-game `Hunter Details`
   popup; shield class icon, cyan element disc on the portrait.
4. `analysis/catalogue/stats/found/faq-image16-card-051-beckhen-cardpage.png`
   — `Lv. 30`, "Master Hunter", cyan element disc.
5. `analysis/catalogue/stats/found/faq-image05-card-010_1-vincent-awakened.png`
   — `Lv.30/30`, "AWAKENED", cyan element disc.

**The mapping that was measured, and why it is not used.**

| element code | disc colour | observations | sources |
|---|---|---:|---|
| Fire | `#B82810` | 2 | 1 original frame with a printed text label, 1 local run |
| Ice | `#00D8E8` | 3 | 2 original frames, 1 local run |
| Lightning | — | **0** | — |
| None | — | **0** | — |

Three reasons this stops here, in order of force:

1. **The calibration set is too small by an order of magnitude.** Five
   observations, two classes, and no Lightning observation at all. The task set
   ~8 calibrated examples as the floor; this is well under it, and a
   two-class mapping cannot discriminate a third.
2. **Glyph shape is not stable across UI generations, so it cannot be the
   mapping key.** Observation 1 (2017-era share card) uses a filled white flame;
   observation 2 (2.8.0.1 detail panel) uses a two-pronged mark. **Disc colour
   is stable; glyph is not.** Any future calibration must key on colour, and must
   say so.
3. **Two of the five observations are local-replica readings.** They are not
   circular *for the mapping* — the attr code they display was independently
   attested by the archive and the wiki before the screenshot existed, and the
   fixture read confirms the replica publishes that same code — but the frame is
   only as trustworthy as the fixture, so they carry less weight than the two
   original-game frames.

**Error rate on the calibration set: 0 disagreements in 5** against the
archive-plus-wiki element. That is the *calibration* error rate and it is
meaningless at this sample size; it is not a claim about any hero's element.

## 1.4 There are two different star axes, and both were measured

This is the single most useful thing the visual pass produced, because
"rarity/grade" is ambiguous and the two things it can mean are different axes.

| axis | where it appears | what the stars count | evidence |
|---|---|---|---|
| **draw rarity** | the recruitment / share card | the hunter's rarity **when drawn** from the pool | `recruitment_screen_full.png`: gold ring, three stars, for `001` Lantern — matching archive `rarity_on_draw` **3** and wiki **3** |
| **current rank / grade** | the in-game detail panel portrait badge | the hunter's **present** rank | `05-tyltyl-details.png`: bronze ring, one star, "Amateur Hunter"; `faq-image16`: cyan ring, one large centre star plus four small, "Master Hunter"; `faq-image05`: pink ring, "AWAKENED", `Lv.MAX` |

**`051` Beckhen demonstrates the separation in a single hero.** Its draw rarity
is **3** (archive `rarity_on_draw` 3, wiki 3) while the badge on its own detail
page shows the **five-star maximum-rank** cluster. The two numbers are about
different things and both are correct.

**Independent corroboration that both axes are first-class in the shipped game:**

- `analysis/VSFan/Images/Blustone/Items/Recruitment/` contains `3star.png` and
  `2-3star.png` as official product art — the gacha pools are literally named
  after star tiers.
- The 2017 APK asset package `UI_CHA_RANK_NEW`, unpacked under
  `analysis/VSFan/Extracted Assets (2026)/1441 (APK)/UI_CHA_RANK_NEW/`, holds
  **218 PNGs in fourteen distinct size classes**. Two of those classes are the
  rank badge family and were inspected visually:
  - **160×140, ten sprites**: five ring colourways (bronze, silver, cyan, amber,
    green) as empty rings, and five carrying star clusters of **1, 2, 3, 4** and
    **one large centre star plus four small** — the five rank steps. The bronze
    one-star matches Tyltyl; the cyan large-plus-four matches Beckhen.
  - **98×98, fifteen sprites**: the same star clusters in three colourways
    (white, cyan, gold) — the small-badge variant of the same five steps.
  - The other twelve classes are not identity badges: 56×20 is a family of
    sixty-three generic gradient pills, and 132×86 / 130×64 / 130×66 / 122×41 /
    122×43 / 122×45 are rank-up crystal-shard effect sprites.
- `UI_JSON_RO` names the gacha tiers in shipped UI strings (`★1|1star`,
  `2STAR`, `4STAR`, `3성 헌터 섭외`), as tabulated in §1.1.

**Limit of this sub-result.** The 160×140 and 98×98 sets come from a 2017 build
with hashed filenames; the ring colourway that corresponds to each rank step is
**not** recoverable from the montage alone, and one observed badge (Vincent
Awakened) uses a pink ring that is not among the five 2017 colourways. Star
**counts** are matched; ring-colour-to-rank is **not** claimed.

## 1.5 The 2019 Japanese developer's database carries both axes, and it agrees with the wiki 61/61 on both

`archived-hunter-database-2019.tsv` was harvested for base stats. It also carries
two identity columns this project had not been reading as identity evidence:
`element_ja` and `rarity_on_draw`. `archived-hunter-database-2019.md` documents
that the pages "give the hunter's rarity **when drawn**" — so `rarity_on_draw` is
the **draw-rarity** axis of §1.4, not the rank axis.

Its element vocabulary is closed and complete:

| `element_ja` | reading | rows |
|---|---|---:|
| `冷気` | Ice | 22 |
| `火炎` | Fire | 21 |
| `電撃` | Lightning | 20 |

**No fourth value appears on any of the 63 rows.** The native enum has four
values (0 None, 1 Fire, 2 Ice, 3 Lightning), and **no source in the project
assigns 0 to a hero.** The Episode histogram over its hero-pack rows is 1×17,
2×19, 3×21 — again no 0. "None" is a legal enum member that no hero uses, as far
as any recovered source shows.

Its draw-rarity distribution: `1`×12, `2`×11, `3`×34, `4`×6.

**The agreement measurement that matters.** Comparing against the community
catalogue (`analysis/catalogue/data/card-catalogue.tsv`, itself
`[COMMUNITY-SOURCED]` per `catalogue/INDEX.md:503-505`) wherever both have a
value:

| axis | comparable | agree | disagree |
|---|---:|---:|---:|
| element (`element_ja` vs wiki `element`) | **61** | **61** | **0** |
| draw rarity (`rarity_on_draw` vs wiki `rarity`) | **61** | **61** | **0** |

The only two archive rows that do not "match" are `026` and `034`, and in both
cases the **catalogue is blank** and the archive supplies the value. The archive
therefore fills two catalogue gaps and contradicts the catalogue **zero** times.

This is a real upgrade, and it should be recorded as such: the wiki's element and
rarity columns were previously supported only by internal consistency and by a
loose plausibility argument in `catalogue/INDEX.md` §7.3 ("extremely likely
correct… but it is not recovered"). They are now corroborated, on **61 of 103**
named rows, by an **official, non-wiki, non-English source published by the
original developer** — the Japanese `blustone.jp/hunter` database, captured by the
Wayback Machine in October–December 2019. The remaining 42 named rows remain
wiki-only, and the ten unnamed costume rows remain blank.

## 1.6 The catalogue's gap is exactly the unnamed costume and awakened rows

The catalogue has blank `element` on 18 rows and blank `rarity` on 18 rows. Of
those, eight are the pseudo-cards. The remaining ten are the **same ten rows**:

`026` `026_1` `034` `034_1` `038_1` `085` `086_1` `087` `088` `095`.

Every one of them has `inferred_owner = yes` in the catalogue, and every one of
them has an **empty `name`**. They are the costume variants the wiki never named.
So the shape of the gap is not random: **the community catalogue has no element
and no rarity for precisely the costume rows it also has no name for.** Those ten
rows are the whole of what §2 has to work with.

Their titles are shipped-ish catalogue metadata and are suggestive but not
evidence: `In Wonderland` (×2), `Halloween Witch` (×2), `Twilight Santa Girl`,
`Lunar New Year`, `Valentine Condemner`, `Florist Lady`, `Florist`, `Knight of
Swimming Pool`.

---

# 2. UNPURIFIED — every numeral, quarantined

**Rule for this section.** Nothing below is a base stat, a coverage credit, or a
rebalance input. It is recorded so derivations can be re-checked without being
re-done. Per `coverage.md`, none of it changes **heroes 1/113 · accessories
1/100 · monsters 0/22**.

## 2.1 The crosswalk arithmetic

Corpus: `card-catalogue.tsv` 121 rows − 8 pseudo-cards (`901` `902` `903` `904`
`912` `913` `914` `x914`) = **113 heroes**. The archive has 63 rows of which 62
returned numeric stats (`056` is a `???` placeholder); 50 heroes have no archive
row at all, and `uncovered-archive-roster-2019.tsv`'s 51 rows are exactly those
50 plus `056`.

### Source-presence patterns, element

`#values` = number of distinct element readings across the three sources; `C`/`A`/`E` = catalogue / 2019 archive / Episode `attr` present.

| pattern | heroes |
|---|---:|
| 0 values, no source | **7** |
| 1 value, Episode only | 1 |
| 1 value, archive only | 1 |
| 1 value, archive + Episode | 1 |
| 1 value, catalogue only | 33 |
| 1 value, catalogue + Episode | 9 |
| 1 value, catalogue + archive | 17 |
| 1 value, all three | 41 |
| **2 values, all three present** | **3** |

Total 113. **106 heroes have at least one element source; 7 have none.**

### Source-presence patterns, draw rarity

| pattern | heroes |
|---|---:|
| 0 values, no source | **8** |
| 1 value, archive only | 2 |
| 1 value, catalogue only | 42 |
| 1 value, both, agreeing | 61 |

Total 113. **105 have at least one rarity source; 8 have none.**

### The unresolved lists

| axis | ids with no source at all |
|---|---|
| element (7) | `026_1` `034_1` `038_1` `086_1` `087` `088` `095` |
| rarity (8) | `026_1` `034_1` `038_1` `085` `086_1` `087` `088` `095` |

### Conflicts

| axis | conflicting heroes | detail |
|---|---:|---|
| rarity | **0** | none. No hero has two different rarity readings anywhere. |
| element | **3** | `009` Fire/Lightning · `010` Ice/Lightning · `059` Fire/Lightning |

**The rarity axis has zero conflicts across 113 heroes and two independent
sources.** That is a materially stronger position than role (which has two
Episode dissenters) or element (three). It is the cleanest identity column in the
corpus.

**The two of the three element conflicts are the known tier-changing heroes and
should not be counted as contradictions.** `009` Captain and `010` Vincent are
precisely the pair `AGENTS.md` and the prior notes identify as changing element at
the top tier, and the Episode table confirms it mechanically: over its hero-pack
rows the only two heroes with more than one distinct `attr` are `009`
{1, 3} and `010` {2, 3}. For both, the catalogue and archive give the **base**
element and Episode supplies the **top-tier** element, and the catalogue's
awakened rows (`009_1` Fire, `010_1` Ice) match Episode's other value. **The
tier-change finding is independently reproduced here from a different pairing of
sources.**

**`059` Lantern (Halloween) is a genuine, unresolved, one-sided conflict.** The
2019 archive says `火炎` (Fire) and the wiki says Fire; the Episode table says
`attr` 3 (Lightning). This is exactly the case `job-tag-attestation-2026-10-06.md`
§2.4 item 8 flagged and deliberately left open. **It is still open.** Two sources
against one, and Episode is the weakest of the three for identity — but two
against one is not a resolution either, and `059` should not be recorded as
Lightning on the strength of one scripted-story row.

### The full crosswalk

Role is shown for orientation only; it is `job-tag-attestation-2026-10-06.md`'s
result, not this pass's. `—` means the source has no value for that row.

| id | name | role (`JOB_*`) | elem: wiki | elem: JP-2019 | elem: Episode | rarity: wiki | rarity: JP-2019 | skill slots |
|---|---|---|---|---|---|---|---|---:|
| `001` | Lantern | Bomber | Fire | Fire | Fire | 3 | 3 | 8 |
| `002` | Mowgli | Offense | Lightning | Lightning | — | 2 | 2 | 7 |
| `003` | Nene | Defense | Ice | Ice | Ice | 3 | 3 | 10 |
| `004` | Tyltyl | Support | Fire | Fire | Fire | 1 | 1 | 8 |
| `004_1` | Tyltyl (Awakened) | Support | Fire | — | — | 5 | — | 9 |
| `005` | Gerard | Defense | Ice | Ice | Ice | 2 | 2 | 9 |
| `005_1` | Gerard (Awakened) | Defense | Ice | — | — | 5 | — | 13 |
| `006` | Sylvester | Offense | Fire | Fire | Fire | 1 | 1 | 8 |
| `007` | Metis | Bomber | Fire | Fire | Fire | 1 | 1 | 7 |
| `008` | Akasha | Support | Lightning | Lightning | Lightning | 3 | 3 | 7 |
| `009` | Captain | Defense | Lightning | Lightning | Fire/Lightning | 1 | 1 | 9 |
| `009_1` | Captain (Awakened) | Defense | Fire | — | — | 5 | — | 13 |
| `010` | Vincent | Offense | Lightning | Lightning | Ice/Lightning | 4 | 4 | 10 |
| `010_1` | Vincent (Awakened) | Offense | Ice | — | — | 5 | — | 13 |
| `011` | Hecate | Defense | Fire | Fire | Fire | 1 | 1 | 8 |
| `011_1` | Hecate (Awakened) | Defense | Fire | — | — | 5 | — | 12 |
| `012` | Karl Steiner | Offense | Lightning | Lightning | Lightning | 3 | 3 | 10 |
| `013` | Denali | Support | Fire | Fire | Fire | 2 | 2 | 9 |
| `014` | Locke | Bomber | Ice | Ice | Ice | 1 | 1 | 8 |
| `015` | Levi | Bomber | Ice | Ice | — | 2 | 2 | 7 |
| `016` | Bruce Bang | Support | Ice | Ice | Ice | 1 | 1 | 7 |
| `017` | Lapis | Offense | Ice | Ice | Ice | 1 | 1 | 8 |
| `017_1` | Lapis (Awakened) | Offense | Ice | — | — | 5 | — | 10 |
| `018` | Robin | Defense | Ice | Ice | Ice | 1 | 1 | 8 |
| `019` | Balian | Offense | Lightning | Lightning | Lightning | 1 | 1 | 7 |
| `019_1` | Balian (Awakened) | Offense | Lightning | — | — | 5 | — | 10 |
| `020` | Sienna | Bomber | Lightning | Lightning | Lightning | 1 | 1 | 7 |
| `020_1` | Sienna (Awakened) | Bomber | Lightning | — | — | 5 | — | 10 |
| `021` | Rebecca | Offense | Fire | Fire | Fire | 2 | 2 | 7 |
| `021_1` | Rebecca (Awakened) | Offense | Fire | — | — | 5 | — | 9 |
| `022` | Sunny | Support | Ice | Ice | — | 2 | 2 | 7 |
| `023` | Hermes | Offense | Fire | Fire | Fire | 3 | 3 | 9 |
| `024` | Riko | Defense | Lightning | Lightning | Lightning | 2 | 2 | 9 |
| `024_1` | Riko (Awakened) | Defense | Lightning | — | — | 5 | — | 11 |
| `025` | Teddy Bomber | Bomber | Fire | Fire | — | 2 | 2 | 7 |
| `026` | In Wonderland | Support | — | **Lightning** | — | — | **1** | 8 |
| `026_1` | In Wonderland | Support | — | — | — | — | — | 9 |
| `027` | Athena | Defense | Fire | Fire | Fire | 3 | 3 | 10 |
| `028` | Octavia | Offense | Ice | Ice | Ice | 3 | 3 | 9 |
| `029` | Kain | Defense | Lightning | Lightning | Lightning | 3 | 3 | 9 |
| `030` | Acerola | Support | Lightning | Lightning | Lightning | 2 | 2 | 7 |
| `031` | Diana | Bomber | Lightning | Lightning | — | 3 | 3 | 7 |
| `032` | Scar | Offense | Ice | Ice | Ice | 2 | 2 | 7 |
| `033` | Patrone | Bomber | Ice | Ice | — | 3 | 3 | 8 |
| `034` | Halloween Witch | Defense | — | **Ice** | Ice | — | **2** | 9 |
| `034_1` | Halloween Witch | Defense | — | — | — | — | — | 11 |
| `035` | Joy | Support | Fire | Fire | — | 3 | 3 | 7 |
| `036` | Bear | Defense | Lightning | Lightning | Lightning | 3 | 3 | 8 |
| `037` | Natalia | Offense | Ice | Ice | — | 3 | 3 | 8 |
| `038` | Rebecca (Christmas) | Offense | Fire | Fire | Fire | 3 | 3 | 7 |
| `038_1` | Twilight Santa Girl | Offense | — | — | — | — | — | 9 |
| `039` | Gullveig | Bomber | Lightning | Lightning | Lightning | 3 | 3 | 8 |
| `040` | Bibi | Offense | Lightning | Lightning | Lightning | 3 | 3 | 8 |
| `041` | Edward | Defense | Lightning | Lightning | Lightning | 3 | 3 | 8 |
| `042` | Santa Clauster | Offense | Fire | Fire | Fire | 3 | 3 | 8 |
| `043` | Papillon | Defense | Ice | Ice | Ice | 3 | 3 | 10 |
| `044` | Heidi | Offense | Fire | Fire | — | 3 | 3 | 8 |
| `045` | Yuri | Offense | Ice | Ice | — | 3 | 3 | 8 |
| `046` | Harley | Defense | Ice | Ice | Ice | 4 | 4 | 11 |
| `047` | Lily & Lyla | Offense | Fire | Fire | — | 4 | 4 | 9 |
| `048` | Dumble | Defense | Ice | Ice | — | 3 | 3 | 9 |
| `049` | Bright | Support | Fire | Fire | Fire | 3 | 3 | 8 |
| `050` | Therapy | Support | Ice | Ice | — | 3 | 3 | 8 |
| `051` | Beckhen | — | Ice | Ice | Ice | 3 | 3 | 9 |
| `052` | Windblade | Offense | Lightning | Lightning | Lightning | 4 | 4 | 8 |
| `053` | Calibur | Defense | Fire | Fire | — | 3 | 3 | 9 |
| `054` | Dino | Bomber | Ice | Ice | Ice | 3 | 3 | 7 |
| `055` | Apollon | Bomber | Fire | Fire | Fire | 3 | 3 | 9 |
| `056` | Genovia | Offense | Ice | Ice | Ice | 4 | 4 | 10 |
| `056_1` | Genovia (Awakened) | Offense | Ice | — | — | 5 | — | 14 |
| `057` | Pansy | Support | Ice | Ice | Ice | 3 | 3 | 7 |
| `058` | Crocus | Support | Lightning | Lightning | Lightning | 3 | 3 | 8 |
| `059` | Lantern (Halloween) | Bomber | Fire | Fire | **Lightning**⚠ | 3 | 3 | 8 |
| `060` | Denali (Halloween) | Support | Fire | Fire | Fire | 3 | 3 | 9 |
| `061` | Chichi | Offense | Lightning | Lightning | — | 3 | 3 | 8 |
| `062` | Juno | Defense | Fire | Fire | — | 3 | 3 | 10 |
| `063` | Erise | Defense | Lightning | Lightning | — | 4 | 4 | 10 |
| `064` | Geranium | Bomber | Lightning | — | Lightning | 4 | — | 10 |
| `065` | Teresa | Support | Fire | — | — | 4 | — | 8 |
| `066` | Mary | Offense | Fire | — | — | 4 | — | 12 |
| `067` | Judith | Bomber | Fire | — | — | 4 | — | 9 |
| `068` | Selene | Bomber | Ice | — | Ice | 4 | — | 9 |
| `069` | Celine | Support | Ice | — | Ice | 4 | — | 10 |
| `070` | Alia | Support | Lightning | — | Lightning | 4 | — | 11 |
| `071` | Anemone | Defense | Fire | — | Fire | 4 | — | 11 |
| `072` | Audrey | Bomber | Lightning | — | Lightning | 4 | — | 10 |
| `073` | Sofia | Support | Fire | — | — | 4 | — | 10 |
| `074` | Leon | Support | Ice | — | — | 4 | — | 12 |
| `075` | Bella | Offense | Ice | — | — | 4 | — | 12 |
| `076` | Junia | Defense | Ice | — | — | 4 | — | 13 |
| `077` | Blondie | Bomber | Fire | — | — | 4 | — | 10 |
| `078` | Teresa (Halloween) | Support | Ice | — | Ice | 4 | — | 8 |
| `079` | Lawrence | Defense | Fire | — | — | 4 | — | 14 |
| `080` | Westfield | Support | Lightning | — | Lightning | 4 | — | 12 |
| `081` | Monica | Defense | Lightning | — | — | 4 | — | 14 |
| `082` | Mary (Christmas) | Offense | Lightning | — | Lightning | 4 | — | 12 |
| `083` | Kamala | Defense | Ice | — | — | 4 | — | 11 |
| `084` | Lottery Mouse | Bomber | Ice | — | — | 4 | — | 13 |
| `085` | Lunar New Year | Support | — | — | **Fire** | — | — | 12 |
| `086` | Genovia (Valentine) | Offense | Fire | — | — | 4 | — | 10 |
| `086_1` | Valentine Condemner | Offense | — | — | — | — | — | 14 |
| `087` | Florist Lady | Bomber | — | — | — | — | — | 9 |
| `088` | Florist | Defense | — | — | — | — | — | 11 |
| `089` | Clara | Support | Lightning | — | — | 4 | — | 11 |
| `090` | Katrina | Offense | Lightning | — | — | 4 | — | 11 |
| `091` | Anemone (Kid) | Defense | Lightning | — | — | 4 | — | 11 |
| `092` | Themis | Bomber | Fire | — | — | 4 | — | 10 |
| `093` | Bella (Summer) | Offense | Fire | — | — | 4 | — | 12 |
| `094` | Leon (Summer) | Support | Lightning | — | — | 4 | — | 11 |
| `095` | Knight of Swimming Pool | Defense | — | — | — | — | — | 14 |
| `096` | Estelle | Offense | Fire | — | — | 4 | — | 12 |
| `097` | Lily & Lyla (Christmas) | Offense | Lightning | — | — | 4 | — | 9 |
| `098` | Selene (Valentine) | Bomber | Lightning | — | — | 4 | — | 9 |

## 2.2 The awakened-element rule — quantified, then applied to four rows

**The rule.** Does awakening change a hunter's element? Fifteen `_1` rows exist
and the catalogue names the base and the awakened variant of eleven of them.

| outcome | pairs | ids |
|---|---:|---|
| element preserved | **9** | `004_1` `005_1` `011_1` `017_1` `019_1` `020_1` `021_1` `024_1` `056_1` |
| element changed | **2** | `009_1` Lightning→Fire · `010_1` Lightning→Ice |
| awakened side unnamed | **4** | `026_1` `034_1` `038_1` `086_1` |

**Observed preserve rate: 9 of 11 = 82%.** Both changes are out of the same base
element (Lightning), which is a 35-of-106 coincidence if independent, but cannot
be distinguished from a systematic rule with n=2.

**Applied to the four unnamed awakened rows, each tagged as an inference:**

| id | base card | base element | base element sources | inferred `_1` element | confidence |
|---|---|---|---|---|---|
| `026_1` | `026` In Wonderland | Lightning | 2019 archive only | **Lightning** | archive base + 9/11 rule |
| `034_1` | `034` Halloween Witch | Ice | 2019 archive + Episode `attr` 2 | **Ice** | **strongest**: two independent sources on the base |
| `038_1` | `038` Rebecca (Christmas) | Fire | archive + wiki + Episode `attr` 1 | **Fire** | **strongest**: two independent sources on the base |
| `086_1` | `086` Genovia (Valentine) | Fire | wiki only | **Fire** | wiki-only base + 9/11 rule — **weakest** |

**Stated error rate: 2 in 11 ≈ 18% per row.** For `086_1` the two uncertainties
compound (weak base source *and* the 18% rule), so `086_1` should not be treated
as better than a coin-flip-weighted guess. `034_1` and `038_1` are the only two
this file would defend.

**This is an inference, not a measurement, and none of these four values is used
anywhere else.** They are listed so a future pass can check them, not so they can
be quoted.

## 2.3 The costume-element rule is **falsified** — so `087`, `088`, `095` stay empty

The tempting inference for the three unnamed costume heroes is "a costume variant
inherits its owner's element." Two named costume rows exist and **both falsify
it**:

| costume | owner | costume element | owner element | changed? |
|---|---|---|---|---|
| `086` Genovia (Valentine) | `056` Genovia | Fire | Ice | **yes** |
| `098` Selene (Valentine) | `068` Selene | Lightning | Ice | **yes** |

**Preserve rate 0 of 2.** The other costume rows the catalogue *does* name by
appending the owner's name in parentheses — `038` Rebecca (Christmas), `059`
Lantern (Halloween), `060` Denali (Halloween), `078` Teresa (Halloween), `082`
Mary (Christmas), `091` Anemone (Kid), `093` Bella (Summer), `094` Leon (Summer),
`097` Lily & Lyla (Christmas) — keep their owner's element in the catalogue, which
is consistent with a mix rather than a rule. `098` is the counter-example that
breaks the pattern, and `091` is a second kind of surprise: Anemone `071` is Fire
and Anemone (Kid) `091` is Lightning.

**Therefore no element is assigned to `087`, `088` or `095`.** Their owners are
`067` Judith (Fire), `046` Harley (Ice) and `079` Lawrence (Fire), and the
inheritance rule that would license copying those values has a measured 0-for-2
record. Copying them would be a fabricated claim.

**Rarity is the same story, and weaker.** Both named costume pairs preserve draw
rarity (`056` 4 → `086` 4; `068` 4 → `098` 4): 2 of 2. But `067`, `046` and `079`
are all 4, and every named card in the `064`–`098` block is 4, so "inherit 4" is
what the base rate says anyway. **The inference carries no information and is not
applied.**

## 2.4 `085` moves from *no source* to *one source* — and that is all

`085` Lunar New Year (a costume of `070` Alia) had **no** element reading
anywhere. `job-tag-attestation-2026-10-06.md` §1.8 noted that Episode was "the
only source in the entire project that states a role or element at all" for it,
and §2.4 item 8 said its element was untouched. Reading `attr` explicitly: the
Episode STAT table has exactly **one** hero-pack row for `085`, and it reads
`attr` **1 = Fire**.

So `085` goes from zero sources to one. **That is not a resolution.** It is a
single scripted-story row, it is the same class of source that is wrong about
`071`'s role and locally wrong about `005`'s role, and it is contradicted by
nothing because there is nothing to contradict it. `085` is recorded as
**Fire, single-source (Episode), unconfirmed.**

Its rarity remains at zero sources and is not assigned.

## 2.5 A semantic hazard in the rarity column itself

The catalogue's `rarity` column mixes the two axes of §1.4:

- for **base** cards it is the **draw rarity**, corroborated 61/61 by
  `rarity_on_draw` (§1.5);
- for the **eleven named awakened** `_1` rows it is **5**, which is the **maximum
  rank**, not a draw rarity. Awakened forms are evolutions; they are not drawn.

The original-game frames agree with the rank reading for the awakened rows:
`010_1` Vincent Awakened shows "AWAKENED" and a `Lv.MAX` maximum-rank badge.

**Consequence.** `rarity` must not be published as one undifferentiated number
per card. For the 113-row table the honest column set is *draw rarity on draw*
(105 heroes have one) and *maximum rank* separately. The four unnamed awakened
rows (`026_1` `034_1` `038_1` `086_1`) have no value in the catalogue because they
are unnamed costume rows, not because awakened forms lack a rank — every named
awakened row is 5.

## 2.6 `element_enhance` / `element_resistance` were checked as an element signal and rejected

The archive's two element-affinity columns looked like a plausible independent
element detector. They are not:

| (`element_enhance`, `element_resistance`) | rows |
|---|---:|
| (`5`, `5`) | 29 |
| (`0`, `0`) | 28 |
| (`2`, `2`) | 3 |
| (`0`, `10`) | 2 |
| (`???`, `???`) | 1 |

The pairs are **symmetric** and cluster by **card era**, not by element: the `5/5`
group spans Fire, Ice and Lightning alike (`027` Athena Fire, `028` Octavia Ice,
`029` Kain Lightning, `031` Diana Lightning, `033` Patrone Ice, `035` Joy Fire,
`036` Bear Lightning, `037` Natalia Ice, and 22 more), and the `0/0` group spans
all three (`001` Fire, `003` Ice, `008` Lightning, and 25 more). The two `0/10`
rows are `062` Juno and `063` Erise.

**Rejected as an element signal.** Recorded here so a future pass does not retry
it.

## 2.7 The icon mapping is measured and **not applied** — restated as a rule

| element code | disc colour | n observations | originals | applied to any hero? |
|---|---|---:|---:|---|
| Fire (attr 1) | `#B82810` | 2 | 1 | **no** |
| Ice (attr 2) | `#00D8E8` | 3 | 2 | **no** |
| Lightning (attr 3) | — | **0** | 0 | **no** |
| None (attr 0) | — | **0** | 0 | **no** |

Two classes, five observations, zero disagreements on the calibration set, and no
observation of the third class. **Every element value in §2.1 comes from a table,
not from a pixel.** The pixels are here so that a later pass with more original
frames — or with a recovered UI art pack — can extend the mapping instead of
starting over, and so the glyph-vs-colour instability (§1.3) is not rediscovered
the hard way.

---

## Limits of this file

- **Identity axes only.** It promotes nothing to strict coverage. Heroes stay
  **1/113**, accessories **1/100**, monsters **0/22**. No base stat, level or gear
  state is asserted anywhere.
- **Both negatives are negatives about *shipped* data only.** The per-card fields
  demonstrably exist in the game — `UI_XML_RO` names `card_attr`, the detail panel
  renders it, `/reference/GetCard` serves it — they simply lived on the HTTP
  reference that no longer exists. Do not read §1.1 as "the game has no element
  column".
- **The 2019 archive is a strong but dated and partial source.** It is
  official and non-wiki, which is why it carries weight, but it is a 2019 capture
  of one server's render, it covers 62 of 113 heroes, and the project already
  records that Blustone 2 was a substantial rebalance (`stat-version-context.md`).
  It settles disagreements in the catalogue's favour here; it does not prove the
  catalogue correct for the 42 rows it does not cover.
- **The icon mapping is two classes wide.** §1.3's five observations support a
  colour key for Fire and Ice and nothing else. `Lightning` and `None` are
  unmeasured.
- **The `UI_CHA_RANK_NEW` sprite family is from a 2017 build** with hashed
  filenames. Star **counts** match observed badges; **ring colourway per rank does
  not**, and one observed badge uses a colourway absent from that build. Do not
  build a rank table from it.
- **Everything in §2.2–§2.4 is inference.** The four awakened element values, the
  `085` element, and the *refusal* to assign `087`/`088`/`095` are all derived
  from small-n rules with stated error rates. None is a measurement, none is
  promoted, and `059`'s element conflict is deliberately left open.
- **Read-only.** No catalogue, server, fixture, seed, state, APK, emulator or
  phone file was modified and no change to any of them is proposed.
  `server-ts/src/bootstrap.ts` was read only to establish the local replica's
  `attr` for two calibration frames. `polluted-observations.md` was **not**
  appended.