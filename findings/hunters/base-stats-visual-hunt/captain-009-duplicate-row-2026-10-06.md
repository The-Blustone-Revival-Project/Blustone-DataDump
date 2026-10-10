# Correction — the Captain `009` ATK outlier is a duplicated row, not a refutation

> ## RETRACTED 2026-10-06 — the premise is FALSE and this file's conclusion is WRONG
>
> **Do not act on anything below.** I claimed Captain `009`'s archive row was a
> **copy-paste defect** and that its `atk 628` was therefore not its own value.
> A lane re-fetched the primary `blustone.jp` pages and refuted all of it:
> `settle-005-009-2026-10-06.md`.
>
> | | `005` Gerard | `009` Captain |
> |---|---|---|
> | `基本能力値` block | HP 1624 / **ATK 628** / DEF 893 | HP 1624 / **ATK 628** / DEF 893 |
> | `排出時の★` | **★2** | **★1** |
> | capture | `20191210181801` | `20191211113041` |
>
> All 13 TSV fields match both pages. **`009`'s ATK is 628 and that is correct.**
> The `628 → 576` substitution floated in §1 here is **withdrawn** (`576` is
> simply `011`'s ATK; the fit was numerology on a correct cell).
>
> **They are distinct cards, not variants** — different names, epithets,
> elements, rarities, all five skills, all three items. The method
> discriminates: `024`/`034` share a hero name *and all five skills verbatim*
> while `005`/`009` share neither. The site simply publishes **one shared base
> row for two different cards**.
>
> **Three consequences:**
>
> 1. **Rarity does NOT determine the row.** The site gives a ★1 and a ★2 hero
>    the identical block, which falsifies the "keyed on `(hero, rarity)`" reading
>    outright and matches the separate finding that `(rarity, role)` leaves all
>    14 cells ambiguous.
> 2. **The vsfan T3 non-uniformity is a REAL, UNEXPLAINED anomaly** — `009`'s ATK
>    ratio `1.1688` against its own HP/DEF `1.2740` / `1.2788` — **not** an
>    artefact of a bad cell. This file "corrected" that anomaly away; that
>    correction is itself retracted. n = 3 heroes.
> 3. **The real defect is in a different column.** `capture_timestamp` /
>    `source_url` are wrong for **31 rows** — `20191015065805` is the October
>    *index* capture copied into rows that resolve elsewhere.
>
> **What survives here:** only §3's arithmetic, which is correct and is now the
> thing that needs explaining. **Hermes** `023` is internally consistent to
> **0.11 %** and **Riko** `024` to **0.20 %** across HP/ATK/DEF, while `009` sits
> at **8.87 %** — with every cell verified correct at the primary source.
>
> **Lesson, added to SYNTHESIS §5.5:** I twice built a data-defect story on a
> *pattern* (a shared triple, an outlier ratio) without checking the primary
> source, and was wrong both times. A pattern in a derived table is a **hypothesis
> about provenance**, never evidence about the cells. Fetch the page.


**Written:** 2026-10-06. **Responds to:** `swipe-panel-hunt-2026-10-05.md`, which
concluded that dividing the three vsfan `Transcendence Level: 3` tables by the
2019 JP archive is "not invertible", that Captain's `1.169` ATK ratio "rules out
a single multiplier", and that this therefore "proves the JP rows are **not**
bare base stats."

**That conclusion is overreach, and the arithmetic that undermines it is visible
in the archive itself.** The Captain ATK cell is bad data. The multiplier model
was not refuted by a non-uniform ratio; it was refuted by **one bad cell**, which
is a different claim with a different fix.

Nothing in any data file has been altered. This file flags, it does not correct.

---

## 1. The ratio arithmetic, recomputed

Base = `archived-hunter-database-2019.tsv`. T3 = the three complete vsfan tables
as reported by the swipe lane.

| hero | rarity | base hp/atk/def | T3 hp/atk/def | ×HP | ×ATK | ×DEF | 3-ratio spread |
|---|---|---|---|---:|---:|---:|---:|
| `023` Hermes | 3★ | 1750/937/653 | 2275/1218/848 | 1.3000 | **1.2999** | 1.2986 | **0.11 %** |
| `024` Riko | 2★ | 1624/682/821 | 2069/868/1047 | 1.2740 | **1.2727** | 1.2753 | **0.20 %** |
| `009` Captain | 1★ | 1624/**628**/893 | 2069/734/1142 | 1.2740 | **1.1688** | 1.2788 | **8.87 %** |

Two of three heroes are internally consistent to **better than 0.25 %** across
all three stats — that is a single per-hero multiplier, cleanly. Only Captain
departs, and only in one cell.

Substituting `628 → 576` makes Captain's ATK ratio `1.2743`, sitting between its
own HP `1.2740` and Riko's cluster. **576 is not a guess**: it is the `atk` of
archive row `011`.

---

## 2. Why `628` is wrong — the duplicate-row audit

Grouping all 62 numeric archive rows by core triple finds **12 duplicated
triples**. Crucially, **3 pairs are identical across all 12 stat fields
*including* `combat_power`**:

| ids | shared triple | rarity | role | `combat_power` |
|---|---|---|---|---|
| `059` / `001` | 1521/1058/653 | 3★ / 3★ | Bomber / Bomber | 8359 / 8359 |
| `024` / `034` | 1624/682/821 | 2★ / 2★ | Defense / Defense | 8552 / 8552 |
| `026` / `004` | 1467/679/679 | 1★ / 1★ | Support / Support | 6664 / 6664 |

**Ten of the twelve duplicates are legitimate.** Their Japanese names identify
them as costume variants of the same base card — `001` 世界初のハンター「ランターン」
and `059` ジャック・オ・ランタン「ハロ…」(Jack O'Lantern); `024` 波乱万丈「リコ」
and `034` ハロウィン魔女「ハロウィンリ…」; `026` 不思議の国の「チルチル」 and
`004` 最高のシェフ「チルチル」. Same rarity, same role, same base card ⇒ identical
row is **expected**, and it independently corroborates the established rule that
identity is a function of `(card, tier)`.

**The twelfth is not legitimate:**

| ids | shared triple | rarity | role |
|---|---|---|---|
| **`005` / `009`** | 1624/**628**/893 | **2★ / 1★** | Defense / Defense |

`005` and `009` share every core stat **and** the role, yet carry **different
rarities** — which contradicts the monotone, near-disjoint rarity banding the
archive otherwise obeys (§2.1 of
`base-stat-heading-client-attested-2026-10-06.md`): 1★ HP tops out at 1624 and
2★ starts at 1395, so 1624 sits on both edges, but two heroes of *different*
rarities sharing an identical `atk` **and** `def` **and** `combat_power`-scale row
is the signature of a **copied row**, not a lookup-table hit.

**Therefore `009`'s archive row is a duplicate of `005`'s, and its ATK is not
that hero's own value.** That is a far better explanation of a lone 1.169 outlier
than "transcendence scales ATK differently from HP and DEF" — which would also
have to explain why Hermes and Riko show no such effect at all.

---

## 3. Corrected position

| claim | status |
|---|---|
| A single per-hero multiplier fits Hermes and Riko to <0.25 % | **SUPPORTED** (n=2) |
| Captain's `009` ATK is reliable | **REFUTED** — probable copied row |
| "Non-uniform ratios prove the JP rows are not base stats" | **RETRACTED** — inference ran backwards from one bad cell |
| The archive's `基本能力値` block is the client's "Base Stat" | **unchanged, and reinforced** — a copied row is a transcription defect, not evidence that the block means something else |
| Two unexplained clusters: Hermes ×1.300, Riko ×1.274 | **still open** — Captain now *drops out* as unreliable rather than joining Riko |

Note what did **not** change: the swipe lane's four structural findings are
independent of this and stand — collapsed block prints `HP, ATK, DEF` while
expanded prints `HP, DEF, ATK`; `24068 + 6291 = 30359` closes arithmetically and
proves the green delta means *added by gear*, so **no equipment screen can ever
yield a base stat**; a set-bonus banner equals its own green delta; and the
accessory frame prints the game's own `Max HP` key. Its `share_en` closure
(28 images viewed, 5 panels, all already known) is also sound.

**The lane's real negative survives and is important:** all 12 panels were captured
on an equipment screen, at Lv.30/MAX, or as result screens. The tuple this project
still lacks is **identified + Lv.1 + gear-free** — and per §2 no equipment screen
can ever supply it.

---

## 4. What would settle `009`

1. Re-fetch the `blustone.jp` profile for Captain `009` and read its `基本能力値`
   block directly, against `005`'s. If they are genuinely identical, the archive's
   `rarity_on_draw` for one of them is wrong instead — either way **one cell is
   bad** and the row pair cannot both be right.
2. Check whether the vsfan wiki carries a **separate** Captain page (it covers
   `009`, `010`, `005` only) with its own base row.
3. Do **not** "correct" `628` to `576` in the TSV on the strength of the ratio
   argument alone. The ratio is consistent with `576`; it does not establish it.

## 5. Reproduction

`%TEMP%\opencode\captain_atk.py` (ratio table + the `576` substitution),
`dup_check.py` (duplicate grouping on core triple, on all 12 fields, and the
rarity-consistency check). Both read-only; no file outside temp was written.
Coverage counts untouched: heroes 1/113, accessories 1/100, monsters 0/22.
