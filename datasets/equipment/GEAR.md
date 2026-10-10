# GEAR — weapons, armour, accessories and jewels

**Not per-entity, so it lives here rather than in an `NNN.md`.** This is the
highest-volume numeric recovery of the round: the equipment system is fully
quantified at level cap, and the catalogue previously listed *all* of it as
`[UNKNOWN]` ("gear stat values — only the category is known").

All values below are from the **same Beckhen (`051`) build at Lv.30**, so they are
mutually consistent by construction. The sub-stats were cross-summed against the
stat screen and 11 of 12 totals reconcile exactly — see [`051.md`](../hunters/observed-stats/051.md).

## 1. Main stat by slot, at level cap — [OCR-CONFIDENT]

`INDEX.md` §7.2 previously knew only the *category* mapping (weapon→ATK,
armor→DEF, accessory→HP). The **values** are now measured:

| slot | item (Beckhen's) | level | main stat |
|---|---|---|---|
| Weapon | Chicken Feet | 50/50 | **ATK 134** |
| Armor | Chicken Wings | 50/50 | **DEF 102** |
| Accessory | Jack | 50/50 | **Max HP 260** |

And one point off cap, from card `010`'s armour
(`found/faq-image07-card-010-vincent-equip-EN.png`):

| slot | item | level | main stat |
|---|---|---|---|
| Armor | Purple Combat Coat | 49/50 | **DEF 101** |

So an armour at Lv49 → Lv50 moves DEF **101 → 102**, i.e. **+1 per level** near the
cap. [DERIVED from two adjacent levels — a single data pair, treat as indicative.]
The same screen shows Strength `33038 → 33057` for that upgrade, i.e. **+19
Strength for +1 DEF** at level 50. [OCR-CONFIDENT]

### Level-cap note
`051`'s three panels all read `Lv.50/50` with `30359 → 30359` for Strength — i.e.
already maxed, so the "modification" preview changed nothing. Consistent.

## 2. Jewel sub-stats at Lv.15/15 — [OCR-CONFIDENT]

Jewels are 5-star ("Highest Class"). Each shows a **main** stat (white) and four
**sub** stats (bulleted). Mounted position is stated per jewel.

| panel | mount | main | sub-stats |
|---|---|---|---|
| image22 | Weapon #1 | **ATK +29** | Crit Damage +3.13 · Block Chance +0.72 · Elem Resist +1.44 · Dmg Red Blk +0.50 |
| image23 | Weapon #2 | **ATK +29** | DEF +11 · Dmg Red Blk +0.38 · Elem Enh +1.65 · ATK +11 |
| image24 | Accessory #1 | **Max HP +58** | ATK +12 · Max HP +21 · Elem Resist +1.69 · Block Chance +0.56 |
| image25 | Accessory #2 | **Max HP +58** | Max HP +18 · Crit Damage +3.87 · Block Chance +0.56 · ATK +13 |
| image26 | Armor #1 | **Block Chance +2.30** | Block Chance +0.56 · Max HP +21 · Dmg Red Blk +0.50 · DEF +11 |
| image27 | Armor #2 | **DEF +29** | Crit Chance +0.67 · Dmg Red Blk +0.38 · ATK +11 · Crit Damage +3.86 |

Every one of the 12 green total-vs-nude deltas in `faq-image18` is reproduced by
this table to the digit or to ±1 rounding — **except ATK**, which is 78 short
(239 reconstructed vs +317 observed). [UNKNOWN] — not reconciled, not guessed.

## 3. Jewel set bonuses — 12 families [TRANSCRIBED; two values have unresolved decimal placement]

From the FAQ author's own list (images 10/11), **not** from game UI. Corroboration:
the list's "Speed Jewel — Mount 4, Increase Attack Speed **1.72**" matches the
in-game set banner on `faq-image22` and the stat screen exactly, so the list is
reliable in structure.

| set | bonus |
|---|---|
| HP Jewel | Mount 2 → Increase HP **5%** |
| Offensive Jewel | Mount 2 → Increase AP **5%** [literal source wording; abbreviation not expanded here] |
| Defensive Jewel | Mount 2 → Increase DP **5%** |
| Critical Jewel | Mount 2 → Increase Critical Attack Chance **4.5%** |
| Block Jewel | Mount 2 → Increase Block Chance **4.5%** |
| Fatal Jewel | Mount 4 → Increase Critical Attack Damage **50%** |
| Super Block Jewel | Mount 4 → Damage Reduction Rate **5%** |
| Element Jewel | Mount 4 → Increase Elemental Enhancement **2** (a wrapped `3` follows) [decimal/punctuation unresolved] |
| Resistance Jewel | Mount 4 → Increase Elemental Resistance **23** [decimal placement unresolved] |
| Speed Jewel | Mount 4 → Increase Attack Speed **1.72** |
| Regeneration Jewel | Mount 4 → Increase HP Regeneration **30** [literal image digits; unit not printed] |
| Penetration Jewel | Mount 4 → Increase Armor Penetration **12** [literal image digits; unit not printed] |

The screenshot clearly renders the regeneration and penetration numerals as `30`
and `12`, with no decimal point or unit marker. Preserve those exact strings and
leave the unit unspecified; do **not** convert them to `30%`, `3.0%`, or `1.2%`.
The Element and Resistance values in the same image remain unresolved: the
Element value wraps across lines (`2` then `3`), while the Resistance suffix reads
`23`; the image does not establish decimal placement. Those two values remain
uncertain and must not be normalized to `2.3` or `23` without corroboration.

## 4. Costs observed — [OCR-CONFIDENT]

From `found/faq-image07-card-010-vincent-equip-EN.png`, upgrading a Lv.49 armour to
Lv.50: **50000** currency, plus two materials at **389/320** and **11/27**
(red = short). Held balance on that screen: **8695**.

This independently corroborates two numbers `catalogue-report.md` had already
extracted from FAQ prose — modification gates at 10/20/30/40 and +1 jewel slot at
level 20 — by showing a real level-50 upgrade screen.

## Sources

All images under [`found/`](../hunters/observed-stats/found), extracted from
`recovered-assets/community-notes-2026-09-30/Blustone Guide FAQ.md`.
Extraction is reproducible: the FAQ stores its pictures as **reference-style**
markdown (`![][imageN]` with `[imageN]: <data:image/png;base64,…>` definitions at
the end of the file) — an inline `![…](data:…)` regex matches **zero** of the 27,
which is almost certainly why round 1 concluded they were unreadable.
