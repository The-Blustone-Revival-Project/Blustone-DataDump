# T2 panel hunt — controlled negatives, plus one prize-2 candidate (2026-10-08)

**Lane goal.** One T2 panel settles the compounding-vs-from-base question:
**(A)** predicts 1.2087, **(B)** predicts 1.2000. Second prize: any
same-grade different-level `戦闘力` pair, or the blonde-child ★4/Lv.MAX rating.

**Answer in three lines.**

1. **No T2 panel exists in any avenue I could reach.** The complete
   `blustone.jp` image corpus (344 unique archived URLs, all fetched and
   **pixel-decoded**) was opened and read; the official site carries exactly
   **one** transcendance receipt (`capa2`), which is the already-measured T1.
2. **A same-frame, same-hero, different-level `戦闘力` pair was recovered** —
   Lv.1 `1999` → Lv.14 `2283` in one Hunter List, implying per-level
   **g = 1.010271** and **g²⁹ = 1.344931**. It is **not** a clean prize-2
   result, because the two instances' ★ grade is **not resolvable** at this
   resolution (§4). It is a **candidate with the confound named**, not a
   measurement of `g`.
3. **The T1 = 1.0994 measurement is untouched and unchallenged.** Nothing here
   contradicts it, and nothing here separates model (A) from model (B).

**Coverage does not move: heroes 1/113, accessories 1/100, monsters 0/22.**
Nothing outside this folder was written. `coverage.md`, `README.md`,
`polluted-observations.md`, every TSV, `server-ts`, fixtures, seeds, the APK,
the emulator, the physical phone and Ghidra were **not** touched.

---

## 1. Positive controls, run before any zero was recorded

GUARD requires this, and on this host it was not optional — archive.org
refused connections on most requests.

| # | control | result |
|---|---|---|
| C1 | `capa2-1024x911.jpg` @ `20190403161635id_` | **200, 69 340 B, decoded JPEG 1024×911 — PASS** |
| C2 | CDX `url=blustone.jp/wp-content/uploads&matchType=prefix`, paged | **345 rows / 344 unique** URLs |
| C3 | `blustone.jp/wp-content/uploads/2018/11/capa2-1024x911.jpg` present in the C2 census | **yes, exactly 1 row** — the C2 instrument sees the known-good artifact |
| C4 | archive.org availability API, `vsfan.net/wiki/Guide_to_Blustone` | **HIT, ts 20200805020132** — API is functional on this host |
| C5 | same API, `bs.visualshower.com` | **HIT, ts 20190401005534** |
| C6 | same API, `blustone.jp` | **MISS** — but C3 proves the host *is* captured, so this is the documented availability-API false negative (GUARD 2), **not** a content negative |
| C7 | namu mirrors `m`/`d`/`dark.namu.moe` | **200, ~110 KB each — transport PASS** (content empty; see §5) |

**Transport failure was never recorded as a content result.** `WinError 10061`
occurred repeatedly on `web.archive.org/web/...id_/` and is treated as a
transport event throughout; the fetcher retries with jitter and the positive
control runs before every fetch batch.

---

## 2. The complete `blustone.jp` image corpus — read

The prior lane opened ~12 of 344 URLs. **This lane fetched and pixel-decoded all
of them** (`t2-hunt-2026-10-08/img/`, 344 files, manifest `work/cdx-uploads.tsv`).
Every candidate game-screen frame — all 45 images at ≥1000 px wide, the family
that can physically carry a stat panel — was opened and read.

**343 of the 344 decoded.** The single exception is `IMG_9762.jpg`, which returns
a hard **HTTP 404** from `id_` at three separate capture timestamps
(`20190403200153`, `20190403212230`, `20191216051555`) after the nearest-capture
resolver confirmed `20190403200153`. Seven further PNGs decode but are **50×50 /
70×70 site icons** and cannot carry a stat panel. So **every image in the corpus
capable of carrying a stat panel has been opened.**

**Result: the corpus contains exactly one per-stat transcendance receipt, and it
is `capa2`, the already-measured T1.** Confirmed against the images the prior
lane had *not* opened:

| newly examined image | decoded | content | stat block |
|---|---|---|---|
| `0d40a5e4…-2-1024x904` | 1024×904 | Abyss excavation + airship map | no |
| `0d40a5e4…-3-1024x904` | 1024×904 | mission list + idle screen | no |
| `0d40a5e4…-4-1024x904` | 1024×904 | story cutscene + story list | no |
| **`0d40a5e4…-1024x911`** | 1024×911 | **Haiden detail + equipment panel** | **戦闘力 only** (see §3) |
| **`0d40a5e4…-5-1024x879`** | 1024×879 | **Kain ★5 detail + skill training** | **戦闘力 only** |
| `0d40a5e4…-11-1024x882` | 1024×882 | Caliber / Terabi detail pages | no |
| `0d40a5e4…-7-1024x415` | 1024×415 | skill-training before/after, Lv.21 & Lv.19 | skill effect only |
| `1547530477`, `-10839`, `-1314`, `-13163`, `-1476` | 1024×911 | missions, captcha, rewards, stage-clear | no |
| `1548235686/5710/5742/5768` | 1024×911 | market (roupi / fight-chip / secret) | no |
| `1550200979`, `-1353-2`, `-1669` | 1024×910 | supply / recruit / missions | no |
| `1550473238`, `-1550474475` | 1024×911 | Fight Club detail / battle prep | no |
| `1550733537`, `-1550735696` | 1024×911 | rewards / hero detail pair | no |
| `1551089100`, `-1551089150` | 1024×911 | news+events / excavation result | **戦闘力 per party member** |
| `1551427143-1`, `1551430697`, `1551433025` | 1024×911 | excavation rewards / **equipment panel** / market | 戦闘力 only |
| `1552976108`, `1553741645`, `1553741962`, `1553742530` | 1024×911 | excavation results | **戦闘力 per party member** |
| `1547531476`, `1543461051`, `TOP`, `biginner1`, `rank1`, `rank3`, `rank4`, `equip1`, `capa1` | 1024×9xx | see §3, §4 | mixed |
| `IMG_0407` (750×421), `IMG_1024` (748×388), `IMG_1030` (749×677), `IMG_0448` (749×533) | 2019/02 | `IMG_0407` is a **Hunter-List fragment with `戦闘力` per hero**; others are an excavation map, a battle HUD, and a **rotating "featured hunter" list** — **no stat panel** |
| `IMG_0410`, `5161f8b8…`, `IMG_5970…`, `IMG_6429`, `de31b93…` | 750×400 – 580×370 | promotional chibi art, hero splash art | no |
| `ac318ec…` (1280×720), `b6f1ecc…` (480×360) | 2019/03 | YouTube-thumbnail banners | no |
| `IMG_9764`, `IMG_9767`, `jigoku2`, `jigoku…`, `IMG_9825`, `IMG_9828` | 576–750 px | guide illustrations, fishing-rod diagram, area map, item/currency detail popups | no |

`IMG_0407-1024x911`-class fragments matter slightly: they are cropped
Hunter-List pieces, but every one read carries **Lv.1 rows only** and no grade
is legible, so they add no pair beyond §4.

**This closes the `capa2`-only claim on a much stronger footing than "verified by
opening the candidates":** it is now exhaustive over the entire archived image
namespace, on decoded pixels, with the numeric control in §1.

### 2.1 `blustone.jp` is itself now closed as a future source

Two independent structural facts, both new:

- The CDX prefix census on `wp-content/uploads` returns **344 unique URLs** and
  is **not truncated** (paged, no `collapse`, `limit` respected). This is the
  *complete* archived image namespace — unlike `matchType=domain`, which the
  prior lane measured truncating at 170–207 rows.
- `bs.visualshower.com` (the developer/publisher host, **live-UNREACHABLE** on
  this host per the project's own record) was enumerated in the archive:
  **1 230 unique URLs**, of which **1 106 are HTML** and only **13 are PNG, 2
  GIF, 0 JPEG**. The image namespace is essentially empty, and **no URL in the
  1 230 contains any transcendence-related path segment**
  (`capa`, `chou`, `cha`, `trans`, `rankup`, `grow`, `育成`, `stat`, `hunt` all
  return zero). The site is a redirect/marketing shell, not a strategy site.

So the official Japanese guide had exactly one receipt and still does. **A
future lane should not re-crawl `blustone.jp` or `bs.visualshower.com`.**

---

## 3. New `戦闘力` readings (not a base stat, not a scaling law)

These are recorded because they are genuine new observations of the quantity the
project needs. **None is a base stat** — all sit at non-zero levels, and two
sit at grades that *can* hold equipment.

| hero | state | `戦闘力` | source image (decoded) |
|---|---|---:|---|
| **Kain `029`** | **★5, Lv.1, マスターハンター** | **13 148** | `0d40a5e4…-5-1024x879` |
| **Haiden `044`** | **★4, Lv.7, アドバンスハンター** | **6 228** | `0d40a5e4…-1024x911` |
| Haiden `044` | ★4, Lv.7, same frame, equipment panel delta | 6 237 → 6 246 | same |
| unidentified | equipment `護衛剣` Lv.14→20 panel, left | 6 704 → 6 714 | `1551430697-1024x911` |
| unidentified | equipment `護衛剣` Lv.14→20 panel, right | 6 762 → 6 792 | same |
| unidentified | equipment `若いタオル` Lv.10 panel, left | 6 607 → 6 634 | `equip1-1024x911` |
| unidentified | equipment `若いタオル` Lv.10 panel, right | 6 634 → 6 643 | same |

**Kain ★5 / Lv.1 = 13 148 is a first** for this corpus. It is *not* usable for
the ★4/Lv.MAX question (§6), for two independent reasons: it is at **Lv.1**,
not Lv.MAX, and a ★5 hero **can hold equipment**, so gear state is unknown.
Reported as an observation only.

**A structural observation worth keeping:** the two `equip1` panels give
`6607 → 6634` and `6634 → 6643`. The two readings **share the endpoint 6634**,
so they are the same hero at the same state photographed across two consecutive
equipment operations — a small internal consistency check that the panel's
"before" value is a state readout and not a projection.

---

## 4. The prize-2 candidate — and precisely why it is not yet a result

### 4.1 The observation

`capa1-1024x911.jpg` (**decoded 1024×911**) left pane is a Hunter List of the
same account, sorted by `戦闘力` (戦闘力順). Among its rows:

| row | hero | level | `戦闘力` |
|---|---|---:|---:|
| row 2, col 3 | red-haired girl, red eye, green collar, gold ring | **Lv. 14** | **2 283** |
| row 4, col 3 | **same portrait** | **Lv. 1** | **1 999** |

Portrait identity was checked at 8× (`zoom/z-red-lv14.png`,
`zoom/z-red-lv1.png`, `zoom/z-red1999.png`): identical hair sweep, identical red
iris, identical green collar, identical gold ring. The frame also contains a
**third** red-haired girl at Lv.1 / `2156` who is **demonstrably a different
hero** — white headband and teal eye (`zoom/z-red2156.png`). So the list does
resolve visually distinct redheads, which strengthens the pairing.

Both `2283` and `1999` are also independently corroborated by the game's own
panel: `capa2`'s receipt reads Bear `036` `2326` in this same list, and `2326`
is the exact pre-transcendence rating in the T1 receipt. The list is
self-consistent with the already-measured T1 frame.

### 4.2 What it implies, if the confound were resolved

Over 13 levels:

| quantity | value |
|---|---:|
| ratio | **1.142071** |
| per-level `g` | **1.010271** |
| implied `g²⁹` | **1.344931** |
| prior per-level cap (`g²⁹ ≤ 1.498434`) | 1.014043 |
| **within the prior bound?** | **yes** |

If this `g²⁹ = 1.344931` were correct, the two rank-up transitions would give

```
f = 1.482030 / 1.344931 = 1.101938      (blonde child, 3311 → 4907)
f = 1.498434 / 1.344931 = 1.114134      (ponytail girl, 2554 → 3827)
```

which would compress the 1.1 % spread between the two transitions to **1.1 %** as
well — i.e. it would *not* by itself explain the project's recorded
hero-dependence. **That is a reason for caution, not a reason to accept it.**

### 4.3 The confound, named

**The two instances' ★ grade is not resolvable.** At the badge resolution of a
1024-wide source the grade pips are ~8 px and decode to a coloured blob
(`zoom/z-pip-lv14.png`, `zoom/z-pip-lv1.png` — both illegible, reported as
illegible rather than guessed, per the project's standing instruction). This is
the same limitation already recorded as U5 in `transcendence-t1t2-hunt-2026-10-06.md`
§2.

Because the list contains many Lv.1 entries, a natural reading is that `1999` is
a freshly-recruited ★1 and `2283` an older, higher-grade one. If they are not
the same grade, the pair measures `f · g¹³` and **not** `g¹³`, and the implied
`g` is meaningless.

**Therefore this is recorded as a candidate, explicitly not as a measurement.**
It is worth one dedicated attempt to resolve the grade at higher resolution —
and that attempt has a defined target: an uncropped, higher-DPI frame showing
this account's red-haired hunter list, or the same hero in a panel that states
its grade in text (e.g. a rank-up result, which prints the grade ring large).

### 4.4 A second, independent same-frame candidate — also grade-limited

`1547531476-1024x911.jpg` (decoded 1024×911) right pane is an expedition result
listing the party with `戦闘力` and level. The red-haired girl appears again:

| image | level | `戦闘力` | decoded |
|---|---:|---:|---|
| `capa1` | Lv.14 | 2 283 | 1024×911 |
| `1547531476` | Lv.16 | 2 416 | 1024×911 |

Portrait matched at 4× (`zoom/z-1547-lv16b.png`). Ratio over 2 levels
**1.058257**, per-level **1.028716** — which **violates** the prior per-level
bound of 1.014043 by a wide margin, and is also inconsistent with the 1.010271
from §4.1.

**These are two different accounts at two different dates**, so this is *not*
evidence that either reading is wrong; it is a demonstration that
**cross-frame, cross-account `戦闘力` comparisons are worthless here**. The
project's own record already found `戦闘力` is not a linear function of
HP/ATK/DEF (the +5.744 % excess); these two frames add that it is also not
comparable across accounts. Recorded so no future lane attempts it.

Within one frame the picture is cleaner: `capa1` shows Bear `036` three times at
**Lv.1 / 2326, 2326, 2326** — byte-identical ratings for three instances of the
same hero at the same level, which is a small but real confirmation that
`戦闘力` is deterministic given (hero, level, grade, state).

---

## 5. Instrument limits reached (recorded, not worked around)

**namu mirrors: transport PASS, content unavailable.** `m`, `d` and
`dark.namu.moe` all return **HTTP 200 with ~110 KB** (C7) — the mirrors are
reachable, which no prior lane had established, since `namu.wiki` 403s. But the
returned HTML is a client-rendered shell: the extracted document text collapses
to 1 link and the game-specific pages all 404
(`블루스톤/자기극복`, `/육성`, `/전투력`, `/능력치`, and the `(게임)` variant).
**This is an instrument limit — the mirror serves no server-side article text to
a plain HTTP client — not a claim that namu lacks transcendence documentation.**
A browser-rendered fetch would be required, which is outside this lane.

**Archive CDX paging artefact.** `matchType=prefix` on `bs.visualshower.com/`
returned 2 000 rows / 1 230 unique and then **HTTP 400 on the first resumeKey
page**. The paging was stopped and the partial census reported as partial.
Per GUARD, a resumeKey failure is never treated as "that is all there is".

**`Hunter Stats [BROKEN IGNORE].xlsx` re-read and excluded, with a reason.** The
sheet has 19 named heroes × `Base/Max` × `Bronze/Silver/Gold/Green/Blue` rows
(67 numeric rows). The `Base`/`Max` pair **cannot be a level pair**: for every
hero the nine sub-stat columns **F–N are byte-identical between `Base` and
`Max`** (e.g. Lapis rows 3/4: Att Spd 8, CD 25, CDmg 205, Pen 0, Block 10,
BlockRes 50, Elem 0, Res 0, Regen 5 — unchanged). A level change that left all
nine sub-stats untouched while moving Life 151→180 and Attack 186→215 is not a
level progression; it is a grade template. **No coverage credit, no `g`.**

---

## 6. Why the ★4/Lv.MAX rating was not obtained

The target is the blonde child's `戦闘力` at ★4 / Lv.MAX — the left-hand value
of the ★4→★5 transition. It is the value the surviving `IMG_5729` crops cut off
at the badge row.

**This lane does not overturn the prior lane's finding that the un-cropped
★4→★5 result does not exist.** All three uploads are crops of one user-edited
phone photo. The complete 344-image census (§2) adds no fourth upload: the
whole `IMG_5729*` family in the namespace is three PNGs, 650×365 / 690×388 /
750×389, plus the `-e15…` duplicates.

A **new** observation, though: `rank1-1024x911.jpg` (decoded 1024×911) shows
**Kain `029` at ★3 / Lv.MAX / `戦闘力 3311`** in a list, on the same account as
`capa1`. That independently reproduces the prior lane's correction that the
`3311` reading belongs to Kain's own ★3/Lv.MAX state. It does **not** give the
blonde child's ★4/Lv.MAX, and Kain and the blonde child are different heroes.

### 6.1 A ★5/Lv.MAX-adjacent datum that does **not** answer it

Kain ★5/Lv.1 = 13 148 (§3) plus Kain ★3/Lv.MAX = 3 311 give
**13 148 / 3 311 = 3.971**, over two grade steps with a level reset each time.
That is **not** usable as a `f` or `g` measurement, for three independent
reasons, each sufficient on its own:

1. the two grade steps are **★3→★4→★5**, whereas every `f` in the project is
   defined at **★3→★4**; a two-step product conflates `f₁·f₂` with anything else;
2. Kain at ★5 **can hold equipment**, and no gear state is shown, so the
   numerator is gear-contaminated while the ★3 denominator is determinately
   gear-free (§2.3 of `grade-vs-level-factor-2026-10-06.md`);
3. transcendance state is unshown on the detail panel, so a T1/T2/T3 multiplier
   could apply to the ★5 reading alone.

Recorded so a future lane does not treat the `3.971` as a clean two-step factor.
It is also **not** evidence against the T1 = 1.0994 measurement, which is
internal to a single frame.

---

## 7. What I searched, exhaustively

| avenue | result |
|---|---|
| `blustone.jp` CDX image census, paged, no collapse | **344 unique, complete; 343 decoded** |
| all 45 large game-screen images + every cropped Hunter-List fragment, pixel-decoded | **one transcendance receipt = `capa2` = T1** |
| `bs.visualshower.com` archive census | 1 230 URLs, 13 PNG, 0 JPEG, **0 transcendence paths** |
| archive availability API (8 hosts) | functional; `blustone.jp` MISS = documented false negative |
| `Hunter Stats [BROKEN IGNORE].xlsx` | grade template, sub-stats invariant ⇒ **not** a level pair |
| shipped client help text `UI_CSV/7adedb12.txt`, all `TRC*` keys | **complete UI string set for the transcendance panel recovered** (§8) |
| namu mirrors `m`/`d`/`dark` | transport PASS, server-side content absent |
| web search (4 queries, EN + KR) | nothing Blustone-specific; results were other games |

---

## 8. By-product: the complete shipped UI string set for Transcendence

No lane had read the client's own transcendance UI keys. Recovered from
`analysis/VSFan/Extracted Assets (2026)/1441 (APK)/UI_CSV/7adedb12.txt`, lines
7122–7250. This is the **full** key space for the panel that renders a
transcendance result, across all five shipped locales:

| key | meaning | en string |
|---|---|---|
| `TRC_TXT` | success banner | `Successfully transcended.` / ja `キャパ超越に成功しました!` |
| `ENH_TRC_INFO1` | picker prompt | `Select a hunter.` |
| `ENH_TRC_INFO2` | cost heading | `Items Required` |
| `ENH_TRC_INFO3` | fodder rule | `To transcend the hunter above\| only identical hunters who are 3★ or above can be used as fodder. The used hunter will disappear.` |
| `EN_TRC_NUM1` | material count | `1/1` |
| `EN_TRC_NUM2` | item count | `10/10` |
| **`TRC_POWER1` / `TRC_POWER2`** | **rating, before / after** | **`Strength`** |
| **`TRC_STAT1` / `TRC_STAT1_1` / `TRC_STAT1_2`** | **ATK, before / after** | **`ATK`** |
| **`TRC_STAT2` / `TRC_STAT2_1` / `TRC_STAT2_2`** | **DEF, before / after** | **`Defense`** |
| **`TRC_STAT3` / `TRC_STAT3_1` / `TRC_STAT3_2`** | **HP, before / after** | **`HP`** |
| `TRC_POWERNUM1` / `TRC_POWERNUM2` | rating numerals | `10000` (placeholder) |

**Three consequences.**

1. **This structurally confirms the `capa2` reading.** The panel is defined with
   exactly **four** numeric rows — ATK, DEF, HP, Strength — in
   before/after pairs. That is precisely the shape read in `capa2`, and it means
   the receipt has **no room** for a sub-stat row: the project's U2 ("does a
   sub-stat row exist on this panel?") is now answered **no, by the client's own
   string table**.
2. **`ENH_TRC_INFO3` independently confirms the ★3 floor** in the shipped build,
   matching the frame's own on-screen rule text quoted in §1.3 of
   `transcendence-t1t2-hunt-2026-10-06.md`.
3. **All numerals are the literal placeholder `10000`.** The client ships **no
   multiplier text at all** — there is no "10 %" / "20 %" string anywhere in the
   `TRC*` key space. **The step factors are server-side numbers, not client
   copy.** This is why no amount of string archaeology will ever yield 1.20 or
   1.30, and it is worth recording so no future lane spends a pass on it.

It also explains something about `capa2`: the panel has a dedicated `戦闘力`
before/after pair (`TRC_POWER1`/`TRC_POWER2`), which is where the
`2326 → 2704` / `2704` readings in that frame live — consistent with
`t1-measured-1.0994-2026-10-08.md` §3.

---

## 9. Reproduction

- CDX paging: `t2-hunt-2026-10-08/cdx.py` (paged, no `collapse`, `resumeKey` 400
  handled as a paging artefact, never as a content negative).
- Wayback fetch with jittered retry: `t2-hunt-2026-10-08/wb.py`.
- Bulk image fetch + decode: `t2-hunt-2026-10-08/fetchimgs.py`
  (positive control first; every file decoded; real dimensions recorded).
- Targeted priority fetch: `t2-hunt-2026-10-08/priority.py` (59 large frames).
- Zoom crop helper: `t2-hunt-2026-10-08/zoom.py`.
- namu mirror fetch: `t2-hunt-2026-10-08/namu.py`, `namuprobe.py`.
- xlsx reader: `t2-hunt-2026-10-08/readxlsx.py`.

Artefacts under `t2-hunt-2026-10-08/`: `img/` (decoded images), `zoom/`
(verification crops), `work/cdx-uploads.tsv` (344 rows), `work/cdx-vs.tsv`
(1 230 rows), `work/priority.log`. Retained for auditability.

## 10. Recommendation for the next lane

**Do not** re-crawl `blustone.jp` or `bs.visualshower.com` (§2.1 — closed).
**Do not** attempt cross-account `戦闘力` comparisons (§4.4).
**Do not** mine `TRC*` client strings for a multiplier (§8.3 — provably absent).

The only two things that would move this forward, in order of value:

1. **A T2 receipt from any non-Japanese source.** Korean and Chinese player
   communities are far larger than the Japanese one for this title and the
   prior lanes exhausted neither. A browser-rendered namu fetch is the concrete
   untried instrument.
2. **Resolve the grade of the `capa1` red-haired pair (§4.3).** One
   higher-DPI frame showing that account's list, or the same hero in a panel
   that prints its grade in text, converts the strongest `g` candidate in the
   project into a real measurement — or kills it.
