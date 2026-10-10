# Miraheze + VSFan equipment stat mining — 2026-10-07

**Lane:** accessory/equipment stat lines. **Trigger:** `blustone.miraheze.org` is live
and its 309 equipment entries had never been mined past rendered prose.

## 0. Result, stated plainly

**Equipment stat lines recovered: 0. Accessory coverage stays 1/100. Not inflated.**

Two independent, well-maintained Blustone communities were taken to exhaustion:

| source | extent read | equipment stat lines | control |
|---|---:|---:|---|
| `blustone.miraheze.org` | **all 1,567 revisions** of the whole wiki | **0** | detector fires on 5 synthetic stat lines, silent on 6 real flavour lines |
| `vsfan.net` (Wayback) | **911 pages**, 144 equipment effect cells | **0** | `TAILNUM` fires on `Increases HP 260`, matched 0/144 real cells |

An equipment stat line needs item + stat + value + level basis. Neither source ever
supplies the **value**. Both supply item, slot, stat *type* and level basis. That is
§2 UNPURIFIED and it stays there.

**The finding is structural, not a sampling gap:** both wikis have the *slot* for the
number and left it empty on every single row, while the *same pages* carry filled
numbers for skills. The communities had the data, transcribed it for skills, and
never for equipment. `blustone.miraheze.org` additionally has **no capability at all**
to display an equipment stat — see §2.2.

---

## 1. Method note — three of my own instruments were broken, and the controls caught them

Recording these because they are the reusable lesson, and because three separate
"zero results" in this lane were initially artefacts.

1. **`list=allpages` without `apnamespace` silently returned only ns=0.** The prior
   lane's "335 pages / 8 categories" was namespace-0 only. Per-namespace enumeration
   gives **1,254 pages, 1,393 revision rows, 1,254 distinct titles**, and only
   **3** categories (not 8). Namespaces 1/2/3/5/7/9/11/13/15/461/711/829 and the
   custom **460 Campaign** are all **empty** — the Campaign namespace is registered
   but has never held a page.
2. **CirrusSearch is only partially indexed on this wiki and every `insource:` zero
   is worthless.** `srsearch=accessory` → **0** although "(Accessory)" appears in 103
   pages; `srsearch=Weapon` → 0; `srsearch="Rage Gauge"` → 0 although it is in every
   hero's Skills table. `intitle:Bella` → 0. Meanwhile `Beckhen` → 2, `a` → 16,
   `the` → 46. A 1,254-page wiki cannot legitimately have 46 hits for "the".
   **Do not use this wiki's search as an oracle.** It is the `GUARD`-file trap in
   exactly the shape the guard warns about: a zero that reads like content absence.
   I discarded every `insource:` result for this reason.
3. **`allpages` paging and a `resumeKey` CDX page-2 both failed**, silently returning
   page 1 only. Any Wayback prefix dump must be checked against a known control row.

---

## 2. `blustone.miraheze.org` — complete, and empty

### 2.1 Completeness control (the one that matters)

`list=allrevisions` was walked wiki-wide and every revision's content fetched by
revid:

```
revisions enumerated      1,393 rows / 1,254 titles / 1,567 distinct revids
revisions content fetched 1,567
site statistics "edits"   1,568      <- matches (delta 1 = the statistic's own rounding)
numeric tokens scanned    4,662
equipment-context stat hits 0
```

A first per-title history sweep returned only **631** revisions and had silently
missed **936** (almost all ns6 File pages). The `allrevisions` walk fixed that. The
result above is exhaustive, not sampled.

### 2.2 The wiki has no equipment-stat capability at all

Read the templates, not the prose:

- `Template:InfoboxCharacter` accepts `Name, Title, Rarity, Role, Element, Gender,
  Race, VoiceActor, ReleaseDate, Image*`. **No HP/ATK/DEF/level parameter exists.**
- `Template:CharacterTable` / `CharacterRow` columns are
  `Name, Rarity, Role, Element, Gender, Race, ReleaseDate`. **No stat column.**
- `== Equipment ==` is a flat bullet list: `* <Name> (<Slot>) - <flavour prose>`.

So there is no hidden, collapsed, or template-generated stat anywhere — the schema
itself has no place to put a number. Section headings found in the corpus are only:
`(preamble)`, `Introduction`, `Quotes`, `Story`, `Skills`, `Equipment`, `Gallery`,
`References`, `Premise`, `Season 1: Metron Hunter`. There is no "Stats",
"Statistics", "Enhance", "Upgrade", "Accessory" or equipment page of any kind.

### 2.3 Equipment-section numeric census, every revision ever

```
revisions containing '== Equipment =='   214
distinct pages ever carrying one          103
distinct (name, slot) entries ever seen  282
distinct accessory names ever seen        94
distinct Equipment prose lines            283
```

Exactly **10** of those lines contain any digit, and all ten are flavour prose. This
reproduces the prior lane's count exactly, now from complete history:

- `Bear's Feet` — Captain hospitalised for **3** weeks
- `Young Gentleman Blouse` — sales up **50**%
- `Matchboy Hood` — recreates the look **200**%!, sales +**100**%
- `Great Sword` — used to block **100** bandits
- `Halloween Pumpkin` — a **4**kg pumpkin at **5**m/s
- `M67 Grenade` — an **M67** grenade
- `Bear Leather` — when she was **10** years old
- `Thermal Jumper` — best selling jumper **30** years ago
- `Black Suit 2XL` — a custom made **2XL** size
- `Gambling Dice` — probability to roll **1** and **6**

Skill tables on this wiki use unfilled `[value]` / `[duration]` placeholders.

### 2.4 The 74 namu references this wiki cites per hero — blocked, with a control

Every hero page cites its equipment source as a namu page, and the four cited pages
are literally *per-role gear* pages:

- 공격수 (weapon) · 수비수 (armour) · 폭격수 (bomber gear) · 도우미 (support gear)

This was the single most promising lead in the lane, because it means the wiki's
authors had a namu source that plausibly contains the numbers they did not copy.

- Live fetch of `namu.wiki` / `en.namu.wiki` → **HTTP 403** (crawler-blocked), matching
  the prior note.
- Wayback `url=namu.wiki&matchType=domain` → rows exist but are all `403`/`404`
  block pages and assets; the four gear paths → **0 rows** each, both hosts.
- **Positive control in the same run:** `vsfan.net/wiki/Beckhen` → 1 row, status 200,
  15,698 bytes. The CDX path works; namu gear pages are genuinely unarchived.

So the one external source this wiki names for equipment is unavailable to both the
crawler and the archive. Recorded as a real blocker, not a content absence.

### 2.5 Everything else on this wiki, inspected and empty

| what | extent | result |
|---|---|---|
| All namespaces (21 registered) | 1,254 pages | no equipment/stat page outside ns0 |
| Talk namespaces (1,3,5,7,…) | 0 pages | never used |
| Custom `Campaign` ns 460 | 0 pages | registered, never populated |
| Templates | 11 read in full | no stat parameter anywhere |
| Categories | 3 | no equipment category |
| File-description pages | 904 titles, only **17** with any text | no gear screenshots |
| `Special:Log` deletions | exactly **1** delete ever (`Template:Extension DPL`), 0 imports, 0 undeletes, 0 revisiondeletes | no deleted stats page |
| `Special:Log` moves | 28, all typo fixes / icon uploads | no moved equipment page |
| Uploaded files (881) | filenames enumerated | portraits, role icons, emotes, CGs, one gym image |
| CirrusSearch `insource:` | 26 queries | **all zero — index broken, results discarded (§1.2)** |

### 2.6 Main Page's Drive image archive — recursed, no gear panels

`drive.google.com/drive/folders/1XitkPbYPGgMdHUaiD3_oxs9eBze5TQ6k` ("Blustone
Image Archive") resolves via `embeddedfolderview`:

```
[BLUSTONE]
├── [CHARACTERS]  → [1MALE] [FEMALE1] [FEMALE2] [NPCS] + 13 loose images
├── [FISH!]       → 3 images
└── [MUSIC]       → 19 mp3 + [UNNAMED]
```

42 entries at depth 2. **No equipment, gear, item or stat folder.** The only
gameplay-looking images are `battle_ranking.png` and three `[CHARACTERS]` subfolders,
which are character art.

---

## 3. `vsfan.net` (the *other* Blustone wiki, via Wayback) — the schema, but no values

This is the genuinely new source, and it is where the lane nearly paid.

`accessory-stat-hunt-2026-10-06.md` §3.4 recorded `Template:Equipment` as "HTTP 404s
on `id_` replay even though a CDX row exists." **That 404 was a retrieval artefact.**
Re-fetched successfully (18,392 bytes), it yields the canonical equipment schema:

```
Type        | Description          | Effect
Weapon      | {{{weapname}}}       | Increases attack {{{weapmax}}}
Armor       | {{{armorname}}}      | Increases defense {{{armormax}}}
Accessory   | {{{accname}}}        | Increases HP {{{accmax}}}
```

Three things fall out of this:

1. **`{{{accmax}}}` is the game's own accessory field and its stat is HP** — an
   independent confirmation of the `Max HP 260 @ Lv.50` reading on `faq-image21`.
2. The parameters are named **`weapmax` / `armormax` / `accmax`**, i.e. the value is
   the **max at Lv.50**, which matches the `Lv. 50` rendered next to it.
3. `Jack` is not special-cased anywhere; it is an ordinary `accname`.

### 3.1 The values were never filled in — controlled negative

Every `/wiki/` page in the archive was enumerated (**1,221 distinct titles**) and
**911** pages fetched with `id_` replay plus `''`/`if_`/`im_` fallbacks.

```
equipment effect cells scanned              144
cells whose value slot begins with a NUMBER   0
CONTROL: TAILNUM.match(" 260")               True   <- detector verified live
```

Rendered form of a real row, verbatim from the Acerola capture:

```
Accessory | Red Glasses | Increases HP Lv.50 | Glasses with thick lens that make ...
```

The `{{{accmax}}}` slot renders to nothing, so the table reads `Increases HP Lv.50`
with the number missing. 37 accessory rows are published this way in total: **36 real accessory entries**
(one of which is Juno's `???` placeholder) plus `Template:Equipment`'s own
`{{{accname}}}` demo row.

**The decisive contrast:** the *same pages* carry **140 filled skill rows** at
Lv.50 — Captain `Crying Sword` **7.54%**, Captain `Increase defense` **15.00%**,
Hermes `Reduction of Enemy Defense` **30%** / `Decrease Enemy Block Chance` **35%**,
Nene `Ground Strike` **4609**, Levi `Loan Shot`-style absolutes like **1143**,
Crocus `Necromancer's Might` **12.5%**, Papillon `Dancing Butterfly` **93.06%**. The
editors were transcribing max-level numbers all over these pages and left every
single equipment value blank. That is a deliberate editorial gap, not a lost capture.

---

## 4. Two cross-lane finds — flagged for parent, NOT counted here

Both are real recovered data. Neither is an accessory stat line and neither changes
the 1/100 figure.

### 4.1 33 vsfan accessory names crosswalk exactly onto the shipped `CHAR_STR` table

Read from the vsfan Equipment tables and matched against
`charstr-items-2026-10-06.tsv` column **`accessory_en`** (note: column 4, *not*
column 2 — an earlier attempt used the wrong column and spuriously reported 0/19
matches):

| vsfan hero | vsfan accessory name | shipped row |
|---|---|---|
| Lantern | Judecca's Gift | **001** |
| Tyltyl | Leather Crossbody Bag | **004** |
| Spirit Bracelet → Akasha | Spirit Bracelet | **008** |
| Denali | Pressure Hair Tie | 013 |
| Rebecca | Skull Necklace | 021 |
| Sunny | Chocolate Bar | 022 |
| Rebecca | Angel Wings | 038 |
| Gullveig | Glory of the Past | 039 |
| Bibi | Wolf Ear Decorations | 040 |
| Edward | Magnifying Glass | 041 |
| Santa Clauster | Santa Sunglasses | 042 |
| Papillon | Prisoner Number | 043 |
| Heidi | Pompom Headband | 044 |
| Yuri | Chocolate Syrup | 045 |
| Harley | Hero's Mark | 046 |
| Dumble | Eye of Truth | 048 |
| Bright | Matchboy Hood | 049 |
| Therapy | Ice Cube Character bracelet | 050 |
| **Beckhen** | **Jack** | **051** |
| Calibur | Emergency Belt Bag | 053 |
| Dino | Anemometer Backpack | 054 |
| Apollon | **Case** | **055** |
| Pansy | **Mia** | **057** |
| Crocus | Straw Doll | 058 |
| Diana | Ribbon Hair Tie | 031 |
| Scar | Ancient Necklace | 032 |
| Patrone | Blue Checkered Shemagh | 033 |
| Joy | First Aid Kit Bag | 035 |
| Bear | Bear's Feet | 036 |
| Natalia | Last Goodbye | 037 |
| Kain | Last Gift | 029 |
| Sienna | Heatproof Cannon Gloves | 020 |
| Acerola | Red Glasses | 030 |

**33 of 36 resolve exactly.** Three do not: Juno's `???` (a placeholder, not an
item), `Lyla's Cheer Cure` (Lily & Lyla), `Unknown Shemagh` (Windblade — probably
`Blue Checkered Shemagh` 033 under a different name).

Why this is worth a line: it is a **second, independent name source confirming the
shipped table**, and it independently pins three rows that the first extraction pass
appeared to lose — `Case`=055, `Mia`=057, `Jack`=051 — matching
`accessory-stat-hunt` §2.1's suffix-whitelist recovery exactly. `Lantern`→`001` and
`Tyltyl`→`004` also agree with the hero↔accessory rows already in the catalogue.

### 4.2 Five vsfan hero stat blocks — post-Transcendence, so NOT base coverage

Five hunter pages carry a `Stats[edit]` block. **Captain and Hermes explicitly state
`Transcendence Level: 3`.** Per this project's own evidence, advancement is
3★MAX→4★LV1, so these are post-Transcendence values and **must not be counted as
base stats** — the exact contamination the coverage rules forbid.

| hero | Transc. | Life | Attack | Defense | Atk Spd | Crit% | CritDmg% | ArmorPen% | Block% | BlockRes% | StrElem% | ElemRes% | LifeRegen |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Captain | 3 | 2069 | 734 | 1142 | 7 | 14 | 180 | 1 | 33 | 52 | 0 | 0 | 40 |
| Hermes | 3 | 2275 | 1218 | 848 | 8 | 33 | 200 | 0 | 14 | 40 | 2 | 2 | 44 |
| Kain | not stated | — | — | — | 7 | 14 | 185 | 0 | 36 | 55 | 5 | 5 | 45 |
| Lantern | not stated | — | — | — | 7 | 14 | 180 | 0 | 14 | 42 | 0 | 0 | 38 |
| Patrone | not stated | — | — | — | 7 | 14 | 185 | 0 | 14 | 40 | 5 | 5 | 38 |

Kain/Lantern/Patrone are missing Life/Attack/Defense outright, and Kain's
"Block Resistance" is labelled "Damage Reduction Block", so the three rows are not
even internally consistent. Useful as a fixture-shape reference for the stat-line
structure (`Character Attributes` → `Stat Details: Attack` → `Stat Details: Defense`)
and for the fact that these are *derived* panels, not a base table. Nothing more.

### 4.3 140 original skill effect values at Lv.50

The vsfan skill tables are filled (§3.1). Full list is in the working data; the
headline is that `server-ts/src/skills.ts` magnitudes are still local fixtures while
these are transcribed originals, e.g. Captain `Crying Sword` 7.54% armor penetration
(a non-round number that no fixture would produce), Nene `Ground Strike` 4609,
Octavia `Persistent Damage` 926, Nene `Continuous Physical Recovery` 163.92. Relevant
to whoever owns skill balance; out of scope for this lane and **not** applied.

---

## 5. Map for a later lane — what is exhausted, do not redo

**Proven empty, with controls:**

1. `blustone.miraheze.org` current wikitext, all 365 text-bearing pages, all
   namespaces. No stat anywhere, including history.
2. `blustone.miraheze.org` **complete** revision history, 1,567 revisions, verified
   against the site's own edit count. No stat, ever.
3. Miraheze `Special:Log` — one delete ever, no imports. No lost page.
4. Miraheze custom `Campaign` ns 460, and all Talk namespaces — empty.
5. Miraheze's 74 namu gear references — 403 live, unarchived in Wayback
   (control: vsfan CDX returns 200). **This is the only real blocker in the lane**
   and it is external.
6. Miraheze Main Page Drive image archive, depth 2, 42 entries — no gear panels.
7. `vsfan.net` `Template:Equipment` — schema recovered, values never filled.
8. `vsfan.net` 911 pages / 144 equipment cells — zero values.
9. `vsfan.net/wiki/Items` and `/wiki/Jewels` — **no 200 capture exists** (checked
   directly; not a fetch failure). The `Jewels` negative in
   `jewel-instance-2026-10-05.md` is confirmed at the archive level.
10. `namu.wiki` / `en.namu.wiki` gear pages — blocked and unarchived.

**Instrument traps, so nobody re-derives them:**

- Miraheze CirrusSearch is **unreliable** — never trust its zeros here (§1.2).
- Miraheze `list=allpages` without `apnamespace` returns ns0 only (§1.1).
- Wayback `resumeKey` paging and `matchType=domain` both truncate silently; always
  run a known-good control row (§1.3, and the `GUARD` archive trap).
- `Template:Equipment` on vsfan is **not** a 404 — it fetches fine with `id_`
  replay. The prior note's negative was wrong.
- `charstr-items-2026-10-06.tsv` accessory column is index **3** (`accessory_en`),
  not index 1 (`weapon_en`).

**Not yet tried, in rough value order:**

1. Other namu mirrors/proxies, or a namu dump — the only unblocked path to
   per-role gear tables.
2. Crawler-spoofed namu fetch (the 403 is a UA/bot gate, not an absence).
3. `vsfan.net` non-`/wiki/` paths: the `/sc/` Korean-community section (565 archived
   URLs, never read by this project) may carry gear posts.
4. Wayback `vsfan.net` **older** revisions: `Template:Equipment` was last edited
   2018-07-28, but per-hero *equipment rows* may predate that and were never checked
   at older `oldid`s.
5. The 9 vsfan hero pages still unfetched (Bella, Celine, Erise, Katrina, Lawrence,
   Leon, Monica, Selene, Sofia) — low value: all 36 rows already found were blank.

---

## 6. Honesty statement

- **Recovered equipment stat lines: 0.** Coverage stays **1/100**
  (`Jack`, `Max HP 260 @ Lv.50`, from the FAQ panel, per the prior lane).
- Nothing in this note is an accessory stat. `Template:Equipment` is a **schema**
  recovery (which field, which stat, which level basis) and is labelled as such.
- The two cross-lane finds in §4 are genuine recovered data but are deliberately
  **not** counted toward accessory coverage; §4.2 is explicitly excluded as
  post-Transcendence.
- Every zero in this note is a *controlled* zero: the fetch path was verified with a
  known-good row in the same run, and the detector was verified with synthetic input
  in the same run. Three instruments that initially produced false zeros
  (`insource:`, `allpages`, Wayback paging) were found and corrected rather than
  reported.
- The one asymmetry a future lane should not over-read: an equipment stat value was
  never published by *these* communities. That is evidence about these communities,
  not proof the original game lacked the display — `faq-image21` proves the game
  itself showed `Max HP 260`. The original table lived on the dead server, consistent
  with the recovered protocol (`/reference/GetItem` → `CSRItemInfo::SetItem`).
