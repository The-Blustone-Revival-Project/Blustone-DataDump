# `JOB_*` as a general identity/role attestation — coverage, the Episode verdict, and where it must not be trusted

**Purpose.** Establish whether the shipped `SKILL_TAG` `JOB_*` tag can serve as a
general attestation source across the whole hero corpus, audit the Episode
disagreements, delimit the axes it covers, settle the `087` "supportive Bomber"
wording caveat, and check whether it reaches heroes no other source covers.

**Discovery being audited.** `identity-contradictions-2026-10-05.md` §0.2 found the
tag (`112` of `113` cards, slot `3`) and §1.1 used it to resolve `071` Anemone to
Defense. That file also stated the mapping was **empirical** (§2.11). **This pass
supersedes that caveat**: the mapping is written verbatim in a second shipped table,
and the tag is mechanically tied to a role ability (§1.2, §1.3).

**Coverage effect: NONE.** Strict coverage stays **heroes 1/113 · accessories
1/100 · monsters 0/22**. Nothing here is a base stat, a level, or a gear state.
`coverage.md` is untouched and `polluted-observations.md` was **not** appended (the
parent mirrors that lane).

**Section discipline.** §1 is **PURE** — identity and role only, with `file:line`
citations. **Digits inside a `file:line` citation are pointers, not data.** Every
count, enum code, slot index and tier index is quarantined in §2.

**Read-only.** No catalogue, server, fixture, seed, state, APK, emulator or phone
file was read-modified or written. Helper scripts were written only under
`%TEMP%\opencode\jobtag\`, outside the workspace. `SKILL_TAG`, `TAG_REF`,
`CHAR_STR`, `SKILL_REF`, `EPISODE_STAT_ACTORS.json` and the two archive TSVs were
read only. Written per `GUARD-encoding-and-archive-traps.md`: `write` tool plus
Python `encoding='utf-8'`, never a PowerShell `Get-Content`/`Set-Content`
round-trip.

---

# 1. PURE — the evidence

## 1.1 Provenance of the tag — which shipped table, which column

| Item | Value |
|---|---|
| Table | `SKILL_TAG` |
| Export | `analysis/recovered-data/leveldb-tables/skill-tag.tsv` |
| Columns | `skill_id`, `slot`, `TAG_KEY` — `skill-tag.tsv:1` |
| Rows | 565 (`skill-tag.tsv:2-566`) |
| Distinct `skill_id` | **113** |
| Original source | `recovered-assets\phone-2026-09-18\game-assets\SKILL_TAG_RO.db\000005.ldb` — `analysis/recovered-reference/manifest.json:34` |
| Source SHA-256 | `b448f236…c6fd` — `manifest.json:35` |
| Manifest key | `manifest.json:32` |

`TAG_KEY` is a comma-separated list of tag keys. The `JOB_*` family is four keys
plus a parent, and it appears **once per row, never co-listed with another tag**
(0 rows mix them).

## 1.2 **The mapping is shipped text, not an inference** — `TAG_REF` documents all four roles

This is the single largest upgrade over the discovery note. `TAG_REF` is a second
shipped LevelDB table
(`manifest.json:38-41`, source `TAG_REF_RO.db\000005.ldb`, SHA-256 `84b7ce8f…cfc`)
whose columns are `tag`, `TITLE`, `DESC` (`tag-ref.tsv:1`) — the in-game tag
reference. It carries the whole tag vocabulary (71 tags) and names the role
**verbatim** in `TITLE`:

| file:line | `tag` | `TITLE` | `DESC` |
|---|---|---|---|
| `tag-ref.tsv:55` | `JOB` | Role | "The common effect that is granted\naccording to the hunter's role." |
| `tag-ref.tsv:56` | `JOB_ATT` | **Offense** | "Offense's role ability.\nOffense's attack increases when the battle starts." |
| `tag-ref.tsv:57` | `JOB_DEF` | **Defense** | "Defense's role ability.\nDefense's defense increases when the battle starts." |
| `tag-ref.tsv:58` | `JOB_GUN` | **Bomber** | "Bomber's role ability.\nThe whole team's attack increases when the battle starts." |
| `tag-ref.tsv:59` | `JOB_SUP` | **Support** | "Support's role ability.\nThe whole team's HP increases when the battle starts." |

So `JOB_ATT → Offense`, `JOB_DEF → Defense`, `JOB_GUN → Bomber`, `JOB_SUP →
Support` is a **dictionary lookup in a shipped reference table**, not a
zero-exception empirical fit. `identity-contradictions-2026-10-05.md` §2.11's
"established empirically … not asserted from the native enum" is **retracted**; the
§0.2 wording is unchanged but is now unnecessary as a caveat. The `TITLE` strings
are also byte-equal to the community catalogue's `role` vocabulary.

Note also `JOB_GUN`'s own shipped description: the Bomber role ability is a
**whole-team attack buff**, and `JOB_SUP`'s is a **whole-team HP buff**. That
matters for §1.11.

## 1.3 **The tag is mechanically tied to the role ability** — 112/112, and one text per role

The `JOB_*` tag marks the skill slot that carries the role-ability passive. Joining
`SKILL_TAG` to `SKILL_REF` (same provenance class; `skill-ref.tsv:1` columns
`skill_id`, `row`, `col`, `FORMULAR`, `IS_FLOAT`, `SUB_SERIAL`, `EN`) on
(`skill_id`, row = the tagged slot, col 0) yields:

- **112 of 112** tagged cards: the tagged slot's shipped text is that role's
  canonical role ability. **Zero** exceptions.
- For each role there is **exactly one distinct string** across every card that
  carries it:

| `JOB_*` | distinct role-ability strings | the one string |
|---|---:|---|
| `JOB_ATT` | **1** | "Increases the attack of self by [value]% when the battle starts." |
| `JOB_DEF` | **1** | "Increases the defense of self by [value]% when the battle starts." |
| `JOB_GUN` | **1** | "Increases all teammates’ attack by [value]% when the battle starts." |
| `JOB_SUP` | **1** | "Increases all teammates’ maximum HP by [value]% when the battle starts." |

Worked citations: `001`/`skill-ref.tsv:5`, `002`/`skill-ref.tsv:13`,
`003`/`skill-ref.tsv:21`, `004`/`skill-ref.tsv:30`. Both slot-`5` cards carry the
same role ability as the slot-`3` population: `036`/`skill-ref.tsv:291`,
`043`/`skill-ref.tsv:348`.

**Why this matters for trust.** Exactly one `JOB_*` per card, on a slot whose text
is the role's role ability, means the tag is not a loose label — it is the marker
the game itself puts on the passive that *defines* the class. A card cannot be
tagged `JOB_GUN` without shipping a Bomber role ability.

## 1.4 Coverage denominator — stated honestly, with the placeholder split

`SKILL_TAG`'s 113 `skill_id`s are **exactly** the 113 hunter cards. Verified by set
identity against `analysis/catalogue/data/card-catalogue.tsv` (121 rows): the
difference is **8 pseudo-card rows**, and nothing else.

| set | n |
|---|---:|
| `card-catalogue.tsv` rows | 121 |
| — pseudo-card rows (`901` `902` `903` `904` `912` `913` `914` `x914`) | 8 |
| — **hunter cards** | **113** |
| `SKILL_TAG` distinct `skill_id` | **113** — set-equal to the hunter cards |
| **cards carrying a `JOB_*` tag** | **112** |
| cards with none | **1** (`051`) |

The 8 excluded rows are **Trainer / Transcendence Ticket pseudo-cards**, not
heroes: their only populated columns are `title` ("★1 Trainer" … "★4 Transcendence
Ticket"), `owner_card_id` and `n_skill_slots = 0`; `name`, `role`, `element`,
`gender`, `race` are all empty. In `char-str` their `SUMMARY` is empty too — the
help text exists but sits in the `VICTORY` column instead ("[Training and Advancing
Helper]… use instead of ★N hunters when training or advancing",
`char-str.tsv:100-103`; "[Transcendence Material]… transcend a ★N hunter",
`char-str.tsv:104-107`). None of the eight appears in the Episode table or the
2019 archive.

**This corrects a denominator that was previously ambiguous.** The discovery note's
"112 of the 113 cards" is right, but its companion figures quoted against a
`121`-row `char-str` table blur 113 heroes with 8 pseudo-cards. The honest
denominators are: **113 heroes, 112 tagged, 1 untagged.**

Row completeness: every one of the 113 heroes has **exactly five** `SKILL_TAG` rows,
one per slot `1`-`5`. No card has a missing or duplicated slot.

Role distribution over the tagged 113-card corpus and over the comparable subsets:

| `JOB_*` | role | over all 112 tagged cards | vs catalogue role (comparable subset) | vs prose (comparable subset) |
|---|---|---:|---:|---:|
| `JOB_ATT` | Offense | 35 | 33 | — |
| `JOB_DEF` | Defense | 30 | 26 | — |
| `JOB_GUN` | Bomber | 22 | 21 | — |
| `JOB_SUP` | Support | 25 | 22 | — |
| *(no tag)* | — | 1 (`051`) | 1 (`051`) | — |

The `33 / 26 / 21 / 22` column is the discovery note's figure and is correct **as a
comparable-subset count**, not as the tag distribution. §2.1 keeps both apart.

## 1.5 The `_1` awakened variant rows — 15, and they never disagree with their base

`SKILL_TAG` carries the fifteen awakened rows
`004_1 005_1 009_1 010_1 011_1 017_1 019_1 020_1 021_1 024_1 026_1 034_1 038_1
056_1 086_1`.

- **15 of 15** carry a `JOB_*` tag.
- **15 of 15** carry the **same** `JOB_*` as their base card. Zero role changes
  across awakening anywhere in the corpus.
- Every `_1` row sits on slot `3` like the base population; none is one of the two
  slot-`5` cases.
- **No `_1` card appears in the Episode STAT table at all** (0 of 55 Episode hero
  `ref_id`s end `_1`), so the two sources are simply disjoint on that axis — the
  awakening rows are attested by `SKILL_TAG` + `char-str` + catalogue + (for the
  11 that have it) `uncovered-archive-roster-2019.tsv`, and never by Episode.

**Consequence.** `SKILL_TAG` is the **only shipped source that speaks to the
awakened `_1` rows as a set**. `identity-contradictions-2026-10-05.md` §1.8 notes
"the fifteen awakened `_1` rows are still single-source for everything except the
four whose role is now shipped-attested twice" — that is now understated for the
role axis: the `_1` role axis is attested by `SKILL_TAG` for **all fifteen**, and by
`char-str` prose for the thirteen that name an archetype.

Worked citations: `skill-tag.tsv:424` (`071 3 JOB_DEF`), `:529` (`091 3 JOB_DEF`),
`:404` (`067 3 JOB_GUN`), `:509` (`087 3 JOB_GUN`), `:494` (`085 3 JOB_SUP`),
`:99` (`015 3 JOB_GUN`), `:59` (`009 3 JOB_DEF`), `:54` (`009_1 3 JOB_DEF`).

## 1.6 Four independent attestations now agree on every hero where all exist

Re-derived this pass, all against the same 113-card set:

| comparison | comparable | agree | disagree |
|---|---:|---:|---:|
| `JOB_*` vs shipped prose (`char-str` `SUMMARY`) | **110** | **110** | **0** |
| `JOB_*` vs community catalogue `role` | **102** | **102** | **0** |
| `JOB_*` vs **2019 JP archive** `role_ja` (mapped) | **62** | **62** | **0** |
| `JOB_*` vs Episode STAT `role`, ≥1 tier must match | 53 of 55 | 53 | 2 (see §2.2) |

The prose row reproduces `identity-contradictions-2026-10-05.md` §2.4 exactly
(110/110, re-derived independently).

**The 2019 archive row is new in this pass.** `archived-hunter-database-2019.tsv`
carries a Japanese `role_ja` column. Its four values are the original game's own
role names, and each is unambiguous:

| `role_ja` | maps to | rows |
|---|---|---:|
| 攻撃手 | Offense | 20 |
| 守備手 | Defense | 17 |
| 爆撃手 | Bomber | 12 |
| ヘルパー | Support | 13 |

**62 of 62 agree with `JOB_*`, zero mismatches.** The archive's 63rd row is the
`056` placeholder (numbers `???`), which has a role value but is counted in the 62.
The JP→EN mapping is a four-item lookup, not a judgement call, and the four counts
partition the set exactly.

This makes `JOB_*` the **only** source in the project that agrees with the
2019 Japanese database on **every** hero both cover, including the cases where the
English catalogue and the Episode table disagree (§2.2). It also means the role
vocabulary is not an English-locale artifact: `JOB_GUN → 爆撃手` and
`JOB_SUP → ヘルパー` is a tag-to-original-JP-name confirmation, not a translation.

**Systematic negative check.** Over the 52 Episode heroes where `JOB_*`, catalogue
role and prose **all three** exist, the count of heroes where `JOB_* ≠ catalogue`
**or** `JOB_* ≠ prose` is **zero**. `JOB_*` is never the odd one out.

## 1.7 The 51-ID uncovered-archive roster — `JOB_*` covers **51 of 51**

`uncovered-archive-roster-2019.tsv` (51 ids) is the set with no numeric 2019
archive row. `JOB_*` is present on **all 51**.

- **43** of the 51 have a non-blank `role` column in that roster file; `JOB_*`
  **agrees with all 43**, zero disagreements.
- The remaining **8** have a **blank** `role` column — `026_1 034_1 038_1 085
  086_1 087 088 095` — so there is nothing to disagree with. `JOB_*` supplies
  their role (Support, Defense, Offense, Support, Offense, Bomber, Defense,
  Defense) and it agrees with `char-str` prose on **8 of 8**.

All fifteen awakened rows in that roster (`004_1 005_1 009_1 010_1 011_1 017_1
019_1 020_1 021_1 024_1 026_1 034_1 038_1 056_1 086_1`) carry a tag and all
fifteen match their base card.

**Net effect.** `JOB_*` moves the roster's role axis from "43 community values,
8 blanks" to **51 shipped values with zero dissenters**. It does not move name,
element, rarity, or any stat.

## 1.8 The 11 Episode-only heroes — `JOB_*` covers **11 of 11**

"Episode-only" is the crosswalk's §1.3 definition: in the Episode STAT table with
no numeric 2019 archive row — `056 064 068 069 070 071 072 078 080 082 085` (of
those, ten have no archive row at all; `056` is listed with `???` numbers).

`JOB_*` is present on **11 of 11**, and each is corroborated by shipped prose:

| id | `SKILL_TAG` | role | `char-str` prose | archive |
|---|---|---|---|---|
| `056` | `JOB_ATT` | Offense | Offense (`char-str.tsv:57`) | 攻撃手 (listed) |
| `064` | `JOB_GUN` | Bomber | Bomber | none |
| `068` | `JOB_GUN` | Bomber | Bomber | none |
| `069` | `JOB_SUP` | Support | Support | none |
| `070` | `JOB_SUP` | Support | Support (`char-str.tsv:71`) | none |
| `071` | `JOB_DEF` | **Defense** | **Defense** (`char-str.tsv:72`) | none |
| `072` | `JOB_GUN` | Bomber | Bomber | none |
| `078` | `JOB_SUP` | Support | Support | none |
| `080` | `JOB_SUP` | Support | Support | none |
| `082` | `JOB_ATT` | Offense | Offense | none |
| `085` | `JOB_SUP` | Support | Support (`char-str.tsv:86`) | none |

**`071` Anemone is the headline.** The crosswalk's §1.3 table marked her Episode
`role` as **1 Offense** in bold with no archive row and no wiki page — the one case
where she was genuinely contested. `SKILL_TAG` resolves it with two independent
shipped sources: `skill-tag.tsv:424` = `071 3 JOB_DEF` and `char-str.tsv:72` =
"The powerful **Defense** who doesn't have block chance…". Her costume sibling
`091` agrees on both (`skill-tag.tsv:529` = `JOB_DEF`, and a byte-identical
`SUMMARY`). `JOB_*` **sides with the shipped description and the catalogue, against
Episode** — exactly as the discovery note reported.

**`085` Lunar New Year is the other one worth naming.** The crosswalk §1.3 records
that Episode was "the only source in the entire project that states a role or
element at all" for `085`. That is **no longer true for the role axis**:
`skill-tag.tsv:494` = `085 3 JOB_SUP` and `char-str.tsv:86` names Support. Episode's
own row also reads Support, so all three agree. `085`'s **element** remains
unresolved and untouched by this pass (`JOB_*` is silent on element — §1.10).

## 1.9 `051` Beckhen — the one card with no `JOB_*`, and it is a genuine shipped gap

`051` is the sole untagged hero. **The absence is real data, not an extraction
failure**, and the reason is visible:

| `skill-tag` line | slot | `TAG_KEY` | matching `skill-ref` text |
|---|---:|---|---|
| `skill-tag.tsv:317` | 1 | `HARD_HIT` | "Uses 3 Rage Gauge when using a skill." (`skill-ref.tsv:410`) |
| `skill-tag.tsv:318` | 2 | `BUFF` | "Strengthens the frontline teammate's Attack Speed…" (`skill-ref.tsv:412`) |
| `skill-tag.tsv:319` | 3 | `INVIN_REPEAT` | "Becomes immune for [duration] second(s) every 3 seconds." (`skill-ref.tsv:413`) |
| `skill-tag.tsv:320` | 4 | `DEBUFF,STUN` | "This effect has a 30% chance to activate…" (`skill-ref.tsv:414`) |
| `skill-tag.tsv:321` | 5 | `ENERMY_WEAKEN,FIGHTCLUB_BOUNS` | "Increases the basic ability of self by 10% during a Fight Club battle." (`skill-ref.tsv:417`) |

None of the five is a role ability. `FIGHTCLUB_BOUNS` appears on **exactly one row
in the entire 565-row table** — `051`'s — so `051` ships a Fight-Club-specific
passive in the slot where every other card ships its role ability. **`051`
genuinely has no role-ability passive, therefore no `JOB_*` tag.**

**`051` is therefore not a gap in the evidence — it is a gap in the game data.**
Its role is attested by four other sources that all say Offense: `char-str.tsv:52`
("The **Offense** who sometimes gets in an immunity state and becomes especially
stronger in Fight Club"), `card-catalogue.tsv:65`, the 2019 archive (攻撃手), and
both of its Episode rows (`EPISODE_STAT_ACTORS.json:823` and `:951`, both
`"role": 1`). **No source dissents.** `JOB_*` is silent on `051`, not wrong.

## 1.10 Axes covered, and axes not covered

| axis | covered by `JOB_*`? | evidence |
|---|---|---|
| **role / class** | **YES, completely** | `tag-ref.tsv:55-59` names all four; §1.3 ties the tag to the role ability 112/112 |
| **slot position of the role ability** | yes (incidental) | slot `3` on 110 cards, slot `5` on `036` and `043` |
| element | **NO** | none of the 67 distinct `TAG_KEY` values in `SKILL_TAG` matches `ATTR|ELEM|FIRE|ICE|LIGHT*`; `TAG_REF`'s 71 tags contain no element tag |
| draw rarity | **NO** | no rarity/grade tag anywhere in the 71-tag vocabulary; the only rarity-adjacent tags are `MAXIM` (Maximization) and `OWN_PASSIVE` (Special), neither of which is a star rating |
| gender | **NO** | no gender tag; `card-catalogue`'s `gender` column has no shipped counterpart in any of the five tables |
| race / species | **NO** | no race tag; `race` likewise has no shipped counterpart |
| name, title, gear | **NO** | those live in `CHAR_STR`, a different table |
| any base stat | **NO** | `SKILL_TAG` has no numeric field at all; its `FORMULAR`/`IS_FLOAT` companions are in `SKILL_REF` and are display formulas, not recovered values |

The keyword audit was run over **all five** shipped string tables. `char-str` and
`skill-ref` contain element/rarity/gender words, but as **prose and as formula
variables** (`stat`, `rank`, `value`) — never as a structured per-card tag. The
claim is precise: **no shipped structured tag carries element, rarity, gender or
race for any card.**

## 1.11 `087` — the "supportive Bomber" caveat. `JOB_*` encodes the ROLE, not a subtype

**Answer: purely the role. There is no subtype axis in the tag at all.** Four
reasons, each sufficient:

1. **Closed vocabulary.** `TAG_REF` defines five `JOB`-family keys total — one
   parent `JOB` plus exactly four leaves (`tag-ref.tsv:55-59`). There is no fifth
   role, no qualifier, and no `JOB_*` variant key anywhere in the 71-tag
   reference. A subtype could not be expressed.
2. **Closed cardinality.** Every tagged card has **exactly one** `JOB_*`
   (112/112; no card carries two, no row carries two).
3. **`JOB_GUN`'s own shipped text is a team buff.** `tag-ref.tsv:58` says the
   Bomber role ability is "The **whole team's attack** increases when the battle
   starts", and `skill-ref.tsv:5` gives that same string for `001`. So a Bomber is
   *already* team-facing by design; `supportive` is not outside the role.
4. **`087`'s tagged slot carries the standard Bomber role ability, unchanged.**
   `skill-tag.tsv:509` = `087 3 JOB_GUN`; the matching text is `skill-ref.tsv:779`
   = "Increases all teammates’ attack by [value]% when the battle starts" —
   byte-identical to `067` (`skill-ref.tsv:556`), `015` (`skill-ref.tsv:123`) and
   `001` (`skill-ref.tsv:5`).

**`087`'s "supportive" describes its active skill, not its class.**
`char-str.tsv:88`: "The supportive Bomber who decreases the whole enemies' block
chance and greatly increases the team's rage **when using a skill**" — an on-use
skill, structurally distinct from the always-on role ability in slot 3. Nothing
about the wording touches the tag.

**Is `087` unique? No — and that is the finding.** Four other heroes carry a
support-adjective on a Bomber description, and **all five agree with their tag**:

| id | `char-str` line | wording | `JOB_*` | role |
|---|---|---|---|---|
| `001` | `:2` | "The Bomber who … provides powerful **supporting** fire" | `JOB_GUN` | Bomber |
| `015` | `:16` | "The **assistive** Bomber who can deal damage to the whole enemy team" | `JOB_GUN` | Bomber |
| `059` | `:60` | "The Bomber who … provides powerful **supporting** fire" | `JOB_GUN` | Bomber |
| `067` | `:68` | "The **supportive** Bomber who decreases the whole enemies' block chance and the enemy's rage" | `JOB_GUN` | Bomber |
| `087` | `:88` | "The **supportive** Bomber who …" | `JOB_GUN` | Bomber |

A **systematic** scan over all 121 `char-str` rows for a support-flavoured modifier
finds these five Bombers plus the twenty-five genuine Supports — and no Offense or
Defense hero described as supportive anywhere. `087`'s description is
near-identical to `067`'s, and the catalogue already anchors `087` to owner `067`
(`card-catalogue.tsv:103`). **The wording is a house prose formula for a Bomber
whose kit is debuff-plus-team-rage, not a role signal.**

**The genuine mismatch class runs the other way, and it is not a `JOB_*` problem.**
Ten non-Support heroes describe team effects in their prose: nine Bombers (above
plus `014 020 033 039 055 084 098 020_1` — expected, Bomber's role ability is a
team buff) and exactly **one** outlier, `009_1` Captain (Awakened),
`char-str.tsv:110` — "A true Captain with high armor penetration and strong
resilience, who **increases the team's Rage continuously**" — tagged
`JOB_DEF` (`skill-tag.tsv:54`). That is a Defense whose kit touches team rage. Its
base `009` is also `JOB_DEF`, its catalogue role is Defense, its prose
(`char-str.tsv:10`) is Defense, and Episode reads Defense. **`JOB_*` is not in
conflict there; the *prose* is the outlier, and it is one of the ten rows that name
no capitalised archetype at all.**

---

# 2. UNPURIFIED — every numeral, quarantined

**Rule for this section.** Nothing below is a base stat, a coverage credit, or a
rebalance input. It is recorded so derivations can be re-checked without being
re-done. Per `coverage.md`, none of it changes **heroes 1/113 · accessories
1/100 ·
monsters 0/22**.

## 2.1 Arithmetic of the audit

| Quantity | Value |
|---|---:|
| `SKILL_TAG` rows / distinct `skill_id` | 565 / **113** |
| rows per card | exactly 5 on all 113 |
| cards with exactly one `JOB_*` | **112** |
| cards with none | **1** (`051`) |
| rows where `JOB_*` shares its row with another tag | **0** |
| rows carrying more than one `JOB_*` | **0** |
| slot carrying `JOB_*` | 3 on 110 cards, 5 on `036` and `043` |
| tag distribution over 112 tagged cards | `JOB_ATT` 35 · `JOB_DEF` 30 · `JOB_GUN` 22 · `JOB_SUP` 25 |
| tag distribution over the 102 catalogue-comparable cards | `ATT` 33 · `DEF` 26 · `GUN` 21 · `SUP` 22 |
| `TAG_REF` tags total / `JOB`-family | 71 / **5** |
| tagged cards whose tagged slot text is the role ability | **112 / 112** |
| distinct role-ability strings per role | **1 each** |
| awakened `_1` ids / tagged / agreeing with base | 15 / 15 / **15** |
| `_1` ids present in the Episode table | **0** |
| `char-str` rows naming 1 / 0 archetype words | 111 / 10 |
| the 10 naming none | `097 009_1` + the 8 pseudo-cards |
| prose vs `JOB_*`, both present | **110 / 110 agree** |
| catalogue vs `JOB_*`, both present | **102 / 102 agree** |
| 2019 JP archive vs `JOB_*`, both present | **62 / 62 agree** |
| Episode hero `ref_id`s / hero STAT rows | 55 / 117 |
| Episode rows where `role` conflicts inside a (`ref_id`, tier) cell | 1 (`005`) |
| Episode heroes whose `role` varies across tiers | **0** |
| `JOB_*` vs Episode, ≥1 tier must match | **53 / 55**; exceptions `051` (no tag), `071` |
| heroes with `JOB_*` + catalogue + prose all present | 52 |
| …of which `JOB_*` ≠ catalogue **or** `JOB_*` ≠ prose | **0** |
| …of which `JOB_*` = catalogue = prose but Episode never agrees | **1** (`071`) |
| `SKILL_TAG` ids not in the catalogue | **0** |
| catalogue ids not in `SKILL_TAG` | 8 (all pseudo-cards) |
| 51-id uncovered roster: tagged / agreeing with a non-blank role | **51** / 43 of 43 |
| 11 Episode-only heroes tagged | **11 / 11** |

## 2.2 The Episode disagreements, one by one

### 2.2.1 The `53 / 55` figure is two different things — do not merge them

`identity-contradictions-2026-10-05.md` §2.4 reports "**53 / 55** agree; exceptions
`051` (no tag) and `071`". That is a **hero-level, ≥1-tier-must-match** reading, and
it reproduces exactly. It is **not** a count of disagreements:

- **only one** hero has an actual `JOB_*`-vs-Episode conflict (`071`);
- **one** hero has no `JOB_*` to conflict with (`051`);
- a third hero, `005`, has a conflicting Episode **row** but an agreeing hero-level
  reading, because three of its four rows say Defense.

### 2.2.2 `071` Anemone — **Episode is the sole dissenter; `JOB_*` sides with the shipped sources**

| source | file:line | reads |
|---|---|---|
| Episode STAT (only row) | `EPISODE_STAT_ACTORS.json:4279-4284` — `"id": "CB1502_071"`, `"role": 1` at `:4283` | **Offense** |
| `SKILL_TAG` | `skill-tag.tsv:424` — `071 3 JOB_DEF` | **Defense** |
| `TAG_REF` | `tag-ref.tsv:57` — `JOB_DEF` → `TITLE` `Defense` | **Defense** |
| role ability text | `skill-ref.tsv` row 3 of `071` = "Increases the defense of self…" | **Defense** |
| shipped prose | `char-str.tsv:72` | **Defense** |
| catalogue | `card-catalogue.tsv:86` | **Defense** |
| costume sibling `091` | `skill-tag.tsv:529` (`JOB_DEF`) + `char-str.tsv:92` (byte-identical `SUMMARY`) | **Defense** |
| 2019 archive | no row | — |

**`JOB_*` sides with the shipped description and the catalogue. Episode is wrong as
identity evidence.** This is not an outvote: it is a shipped tag, a shipped tag
reference naming the role in `TITLE`, the shipped role-ability text, shipped prose,
a costume sibling, and a community catalogue — against one scripted-story row, on
the **top-tier** row where the two known element overrides also sit.

### 2.2.3 `005` Gerard — **Episode is right *for that scene*, wrong for identity**

| actor id | file:line | `role` | `res_id` | thumb tier |
|---|---|---:|---|---:|
| `CB0102_005_1` | `EPISODE_STAT_ACTORS.json:6534-6539`, `"role": 1` at `:6538` | **1 Offense** | `C005` | 0 |
| `CB0103_005_1` | `:6616-6621`, `"role": 2` at `:6620` | 2 Defense | `C005` | 0 |
| `CB0401_005_1` | `:11912-11917`, `"role": 2` at `:11916` | 2 Defense | `C005` | 0 |
| `EVCB0201_005` | `:515-520`, `"role": 2` at `:519` | 2 Defense | `C005` | 0 |

Same art pack, same element, same tier index; only `CB0102_005_1` dissents.
`SKILL_TAG` `skill-tag.tsv:34` = `005 3 JOB_DEF`, `char-str.tsv:6` = Defense,
catalogue (`card-catalogue.tsv:7`) = Defense, 2019 archive = 守備手.

**`JOB_*` sides with the shipped sources and the catalogue on identity. Episode's
row is *locally* correct for that one scripted encounter and *globally* wrong as a
character class.** This is a per-encounter override, and it is the mechanism that
makes `071`'s lone row interpretable.

### 2.2.4 `051` Beckhen — **no `JOB_*` exists; no dissent anywhere**

`skill-tag.tsv:317-321` — five rows, no `JOB_*`. Episode reads Offense on both rows
(`EPISODE_STAT_ACTORS.json:823`, `:951`), and prose (`char-str.tsv:52`),
catalogue (`card-catalogue.tsv:65`) and archive (攻撃手) agree. See §1.9 for why
the tag is legitimately absent.

### 2.2.5 Two more Episode rows that dissent — **on monster packs, and they are not identity rows**

Auditing all 152 Episode STAT entries rather than only the 117 hero-pack rows turns
up two further divergences that the hero-pack filter hides:

| entry | file:line | `res_id` | `ref_id` | Episode `role` | `JOB_*` |
|---|---|---|---|---:|---|
| `CB0002_M01` | `EPISODE_STAT_ACTORS.json:5887-5892` | `M034` | `034` | 1 Offense | Defense |
| `CB0001_M01` | `:5935-…` | `M001` | `001` | 1 Offense | Bomber |
| `CB0001_BOSS` | `:5911-…` | `M040` | `040` | 1 Offense | Offense (agrees) |

These are **monster** actors whose `ref_id` field happens to collide with a hero
id. `JOB_*` says nothing about monsters, and there is no hero identity claim to
make. Recorded because it is a further reason **not** to treat the Episode
`ref_id` field as a reliable card identity key: across all 34 monster-pack STAT
entries, 31 carry `ref_id: null` and 3 carry a colliding hero id. A naive
"Episode says `034` is Offense" would be a false identity claim.

Full Episode-entry audit by pack type and verdict:

| pack type | verdict | entries |
|---|---|---:|
| hero pack | agrees with `JOB_*` | 113 |
| hero pack | **diverges** | **2** (`CB1502_071`, `CB0102_005_1`) |
| monster pack | agrees | 1 |
| monster pack | **diverges** | **2** (`CB0002_M01`, `CB0001_M01`) |

## 2.3 **Verdict on the critical question: is Episode ever RIGHT where `JOB_*` disagrees?**

**No. Not once, on the identity axis.** Stated plainly, because the task makes this
the load-bearing question:

1. **Direct test.** Over the 52 heroes where `JOB_*`, catalogue role and shipped
   prose all exist, the number where `JOB_*` ≠ catalogue or `JOB_*` ≠ prose is
   **zero**. `JOB_*` never dissents from any other source.
2. **Reverse test.** The number of heroes where `JOB_*` = catalogue = prose **and**
   Episode never agrees is exactly **one** — `071`. There Episode is the lone
   dissenter against five sources.
3. **The one row where Episode outvotes (`CB0102_005_1`) is a per-encounter
   override, not an identity claim.** Its own file contradicts it three rows later
   on the same art pack and tier. `JOB_*` still sides with identity there.
4. **No counter-example exists in the corpus.** There is no hero for which Episode
   supplies a role, `JOB_*` supplies a different one, and Episode is right.

**Therefore Episode per-encounter roles do NOT override the card role, and `JOB_*`
is safe as a general role attestation.** Episode *does* contain per-encounter role
overrides — demonstrably at `005` — but those are authored script values on
story-actor rows, they never produce a hero for whom Episode's reading beats the
card role, and the one hero where Episode is unanimous (`071`) is a case where
Episode is wrong.

Two independent reasons Episode cannot serve as the role oracle, both now measured:
its role is **not** single-valued per (`ref_id`, tier) cell — one cell conflicts —
and its `ref_id` field **collides with monster ids** on three monster rows (§2.2.5).
`JOB_*` has neither defect: one tag per card, no collisions, and 112/112 mechanical
agreement with the role ability it names.

## 2.4 Where `JOB_*` must NOT be trusted — the complete list

1. **Not a card-existence oracle.** 113 ids, and it says nothing about the 8
   pseudo-card rows or about any non-hero content.
2. **Not a rarity, element, gender, race, name, title or gear source.** §1.10.
3. **Silent, not authoritative, on `051`.** Do not read the missing tag as "unknown
   role" — four other sources say Offense and none dissents.
4. **Not a subtype.** Four leaves, one per card. Any question of the form "which kind
   of Bomber" is unanswerable from the tag by construction (§1.11).
5. **Not an awakens-changes-role source.** It never changes; do not expect it to
   carry awakening-specific role information.
6. **Not a base-stat source and not a coverage source.** No numeric field; heroes
   stay at 1/113.
7. **Slot position is not a role.** Two cards carry the role ability on slot `5`
   (`036`, `043`). Any parser hard-coded to slot 3 will silently miss two heroes —
   which is exactly the failure mode `identity-contradictions-2026-10-05.md` §0.2
   already warned about in passing.
8. **It is not the arbiter of `059`'s element.** `059`'s tag is `JOB_GUN`
   (`skill-tag.tsv:…`, `char-str.tsv:60` Bomber, catalogue Bomber, archive 爆撃手 —
   four sources, unanimous). Its **element** conflict (`archive`/catalogue Fire vs
   Episode Lightning) is untouched by `JOB_*`, which is silent on element, and
   `059` therefore stays **UNRESOLVED on element**. Do not let a clean role column
   be read as a clean identity column.

## 2.5 Retained conventions, unchanged

- Role enum `1 Offense / 2 Defense / 3 Bomber / 4 Support`
  (`analysis/research/card-enums.md:10-27`) was used to read the Episode `role`
  field. That mapping was **not** re-derived and is independent of this file's
  conclusion — §1.2 and §1.3 do not use the enum at all; they use `TAG_REF`'s
  `TITLE` strings and the role-ability text.
- Episode `stat.rank` is a **scripted-story rank**, not draw rarity
  (`hero-identity-crosswalk-2026-10-05.md` §0.3 item 2). It appears in §2.2 tables
  only to show that the dissenting rows share an art pack and tier.
- None of the HP/ATK/DEF values anywhere in the Episode table is a base stat.
  `analysis/recovered-reference/EPISODE_COMBAT_STAT.manifest.json` says so
  verbatim ("Episode-only actor STAT table; not ordinary hunter card-base stats").
  **No such value is cited in §1 of this file at all.**

---

## Limits of this file

- **Identity and role only.** It promotes nothing to strict coverage. Heroes stay
  **1/113**, accessories **1/100**, monsters **0/22**.
- **One axis.** `JOB_*` is a role attestation and nothing more. It cannot and does
  not settle element, rarity, gender, race, name or stats.
- **Two sources, one game.** `SKILL_TAG` and `TAG_REF` both come from the shipped
  client, so §1.2 and §1.3 are *consistent*, not *independent*. The genuinely
  independent confirmations are the shipped **prose** (`char-str`, a third table),
  the community **catalogue**, and the **2019 Japanese archive** (62/62) — those are
  what make the role column safe rather than merely internally tidy.
- **Episode is treated as a weak source throughout**, and §2.5 item 8 is the
  standing reminder that a clean role column is not a clean identity column.
- **Read-only.** No catalogue, server, fixture, seed, state, APK, emulator or phone
  file was modified and no change to any of them is proposed.
  `polluted-observations.md` was **not** appended.
- **`059`'s element remains deliberately unresolved**, and `085`'s element is
  untouched. Neither is affected by this pass.