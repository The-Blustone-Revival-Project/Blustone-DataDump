# Identity contradictions in the hero catalogue — resolved and still open

**Purpose.** Close, or honestly decline to close, the four contradictions that
`hero-identity-crosswalk-2026-10-05.md` carried forward as UNRESOLVED, using the
newly available `vsfan` community-wiki corpus plus two shipped sources the earlier
pass did not exploit.

**Coverage effect: NONE.** Strict coverage stays **heroes 1/113 · accessories
1/100 · monsters 0/22**. Nothing here is a base stat. `coverage.md` is untouched.

**Section discipline.** §1 is **PURE**: identity only — role, element, costume
lineage — with `file:line` citations. **Digits inside a `file:line` citation are
pointers, not data.** Every numeric value that could be mistaken for a
measurement — enum codes, counts, HP/ATK/DEF, tier indices, hash prefixes — is
quarantined in §2 and must not be promoted out of it.

**Read-only.** No catalogue, server, seed, state, APK or emulator file was
modified and no change to any data file is proposed. `polluted-observations.md`
was **not** appended (the parent mirrors that lane). Helper scripts were written
only under the approved temp directory, outside the workspace.

---

## 0. Provenance, and what changed in this pass

### 0.1 This file pre-existed

An earlier version of this file was already on disk (untracked, last written
2026-10-05 22:41 local) carrying four resolutions. **Every one of its
`file:line` citations was re-derived from source this pass and all of them
verified byte-exact** — 16 window citations in `EPISODE_STAT_ACTORS.json`, 5 in
the `EPISODE_COMBAT_*.json` thumbs, and 28 row citations in `char-str.tsv` and
`card-catalogue.tsv`. Its conclusions on `071`, `085`, the tier rule and `038_1`
all reproduce. This version therefore keeps those conclusions, **adds two new
sources**, **splits `059` into a closed gameplay question and an open identity
question**, and **corrects several arithmetic statements** (§2.10).

### 0.2 NEW SOURCE 1 — the shipped `skill-tag` `JOB_*` role tag

`analysis/recovered-data/leveldb-tables/skill-tag.tsv` gives each card five
slot → `TAG_KEY` rows. Slot 3 carries a **`JOB_*` job tag** on 112 of the 113
cards (`051` Beckhen is the sole card with none; `036` and `043` carry theirs in
slot 5 instead of slot 3). Cross-tabulated against the community catalogue:

| shipped `JOB_*` | catalogue role | rows | exceptions |
|---|---|---:|---:|
| `JOB_ATT` | Offense | 33 | **0** |
| `JOB_DEF` | Defense | 26 | **0** |
| `JOB_GUN` | Bomber | 21 | **0** |
| `JOB_SUP` | Support | 22 | **0** |
| *(none)* | Offense | 1 | `051` |

This is a **perfect, zero-exception, game-authored role attestation** that is
independent of the community wiki, of the Episode actor table and of the
in-game description prose. It is a second shipped role source, and it is what
upgrades `071` from "resolved by outvote" to "resolved by two independent
shipped sources" (§1.1). It also fills the catalogue's ten blank `role` cells a
second time, agreeing with the prose on all ten (§1.6).

`skill-tag.tsv` says **nothing** about element. There is no shipped element tag
anywhere in the five LevelDB tables.

### 0.3 NEW SOURCE 2 — the `vsfan` community wiki, and what it does *not* cover

`vsfan-wiki-2026-10-05.md` recovered 57 hero pages carrying rarity / role /
element infoboxes (55 distinct characters). Its Identity Metadata cross-check
agreed with the 2019 JP database on 55 of 57. **Which of the six heroes in
question does it actually cover?**

| hero | in the wiki's hero infobox set? | reading if present |
|---|---|---|
| `071` Anemone | **NO** | — |
| `085` Lunar New Year | **NO** | — |
| `059` Lantern (Halloween) | **NO** (the wiki has `Lantern` = `001` only) | — |
| `038` Rebecca (Christmas) | **NO** (the wiki has `Rebecca` = `021` only) | — |
| `038_1` Twilight Santa Girl | **NO** | — |
| `009` Captain | **YES** | `vsfan-wiki-2026-10-05.md:474` — ★, Defense, Electric, oldid 2323 |
| `010` Vincent | **YES** | `vsfan-wiki-2026-10-05.md:515` — ★★★★, Offense, Electric, oldid 7372 |
| `005` Gerard (control) | **YES** | `vsfan-wiki-2026-10-05.md:481` — ★★, Defense, Ice, oldid 2403 |

The 55 covered catalogue ids parsed straight out of that file's §1.5 table are
the contiguous early roster plus a few later entries; `059`, `038`, `071`, `085`,
`091`, `070`, `026` and `034` are **all absent**, and the strings `Anemone`,
`Lunar`, `Jack O`, `Santa Girl`, `Florist` and `Rebecca (Christmas)` occur
**zero times** in the whole harvest note.

**So the new source decides nothing outright.** What it does do is supply a
**third and fourth independent attestation of the `009` / `010` base forms**
(Lightning, matching archive + catalogue + the Episode base-tier rows), and it
confirms `005` = Defense, which is the crosswalk's only Episode *role* mismatch
besides `071`.

**One bounded negative, control-backed.** The wiki is the only community corpus
that names a transcendence/awakening state, so it was the one place that could have
documented whether element changes with tier. It does not. A CDX sweep of the
whole archived `/wiki/` URL space (**1,224 rows returned, `url=vsfan.net/wiki*`,
`collapse=urlkey`**) contains exactly **two** pages matching
`transcend|awaken|awak|element`: `Awake` and `Element_Type`. `Awake` was fetched
(HTTP 200, 42,751 bytes) and is a **story-dialogue page** — Captain dialogue from
the opening, plus the site navbox — with no mechanics content at all.
`Element_Type` is a redirect to the stale 2017 `Hunter` page, already recorded
as such at `vsfan-wiki-2026-10-05.md:906`. A live control
(`https://example.com/`, HTTP 200, 577 bytes) succeeded in the same run, so the
two-hit result is a real absence rather than a failed query.

### 0.4 The shipped source is exhausted for `059`

`analysis/extracted/assets/R_EPISODE.jet` (SHA-256
`7f4362cdf80545a6da937444094837f334c8aae4f9f791d6ff4161948d98a01e`, byte-identical
to the phone-snapshot copy) was re-decoded with `tools/jet-viewer/jet_decoder.py`.
It holds **66 logical resources**: one event, a season list containing **only
`season1`**, one season, one tutorial block, and the COMBAT/STAT records. The
string `C059` occurs **exactly once in the entire pack**. So there is precisely
one shipped `attr` for `059`, there is no second episode season, and the Episode
STAT table is the **only** shipped file in the whole workspace that assigns an
element to any hero at all — and it is a **scripted-story actor table, not a card
reference table** (`EPISODE_COMBAT_STAT.manifest.json` says so verbatim). No
further shipped vote on `059` can be recovered from local data.

---

# 1. PURE — the evidence per contradiction

## 0. The shipped description prose

`analysis/recovered-data/leveldb-tables/char-str.tsv` (derived from the shipped
`CHAR_STR_RO` LevelDB row; see `analysis/recovered-reference/manifest.json`) has a
column the crosswalk never used: **`SUMMARY`**, the in-game hunter description.
It names the role archetype in English prose.

**Why this source is admissible.** Re-derived this pass:

- It names exactly one archetype word on 110 of 121 rows; 1 row (`011_1`)
  names a second, non-archetype word; 10 name none.
- Against `analysis/catalogue/data/card-catalogue.tsv`, on every row where both
  exist: **101 compared, 101 agree, 0 disagree** (100/100 if `011_1` is excluded
  for that second word).
- Against the shipped `skill-tag` `JOB_*` tag (§0.2): **110 compared, 110 agree,
  0 disagree.**
- Against the Episode native enum it dissents on `071`, and on `005` only
  because `005` carries both values in Episode (§2.3).

So `SUMMARY` is shipped, game-authored, and independent of the community wiki
and of the Episode actor table. It speaks to **role only** — never element.

## 1.1 `071` Anemone — role conflict — **RESOLVED: Defense**

Two independent shipped sources and the catalogue say Defense; one scripted
Episode row says Offense.

| source | file:line | reads |
|---|---|---|
| shipped prose | `char-str.tsv:72` | "The powerful **Defense** who doesn't have block chance but instead has a high defense, and can overturn the battle with forcing the enemy to change" |
| shipped job tag | `skill-tag.tsv`, `071` slot 3 | **`JOB_DEF`** |
| catalogue | `card-catalogue.tsv:86` | Defense |
| Episode STAT (only row) | `EPISODE_STAT_ACTORS.json:4283` | `role 1` = Offense |

Three further shipped facts, all re-verified:

- **The whole Anemone line is a Defense.** `char-str.tsv:92` (`091` "Anemone
  (Kid)" / "Little General") carries a **byte-identical** `SUMMARY`;
  `skill-tag.tsv` `091` slot 3 is also `JOB_DEF`; `skill-ref` and `skill-tag` for
  `071` and `091` are byte-identical. Adult and child form, same class.
- **`091`'s own weapon is `Lightning Sword`** (`card-catalogue.tsv:107`) where
  `071`'s is `Fiery Sword` (`card-catalogue.tsv:86`), and the catalogue gives
  `091` Lightning against `071` Fire. So the two Anemone cards differ on
  **element** while agreeing on **role** — which is precisely why the element
  rule of §1.3 is needed and the role question is separate.
- **Per-encounter role overrides demonstrably exist in this very table.** `005`
  has four Episode rows; `EPISODE_STAT_ACTORS.json:6538` (`CB0102_005_1`) says
  Offense while `:6616`, `:11912` and `:515` all say Defense, on the same art
  pack and the same tier index. `071` is the same failure mode with only one row
  to hide it — and `071`'s single row sits on the **tier-3** row, the tier where
  the two known *element* overrides also sit (§1.3), which is the shape of
  scripted-encounter authoring rather than identity.

**Verdict.** `071` Anemone is a **Defense**. `CB1502_071.role = 1` must not be
used as identity evidence. `071`'s element (**Fire**, `EPISODE_STAT_ACTORS.json:4282`
`attr 1`) was never in conflict and is unaffected; its grade rises from
SINGLE-SOURCE to **CONFIRMED**, now resting on shipped data.

## 1.2 `085` Lunar New Year — element conflict inside the shipped source — **RESOLVED: the STAT row is the gameplay element; the three COMBAT thumbs are copy-propagated dead data**

The disagreement: `EPISODE_STAT_ACTORS.json:1850` gives the STAT row for
`EVCB0301_C085` an `attr` of Fire, while all three COMBAT records that place
that actor give its encounter thumb Lightning — `EPISODE_COMBAT_EVCB0302.json:52-57`,
`EPISODE_COMBAT_EVCB0303.json:36-41`, `EPISODE_COMBAT_EVCB0304.json:36-41`.

**Which one reaches the game — traced on the original dumps:**

1. `analysis/ghidra-episode-combat-actors-keys.txt:21-22` — `ParseActor`
   (`0x00b1bd5c`) reads `attr` and `role` out of the **STAT** row.
   `analysis/research/episode-first-combat-contract.md:13` records that
   `FindActorRef` returns that same `CSRCardInfo` and that `LoadCombat` installs
   it on the episode actor.
2. `analysis/ghidra-episode-first-combat.txt:929-1075` — for a non-empty
   `actor_id`, `CSRSceneMEpisode::MakeStageInst` copies that shared `CSRCardInfo`
   pointer into the fresh `ACTOR_INFO` and then reads the thumb fields `rank`
   (`:976`), `awake_step` (`:977`), `hyper` / `awake_hyper` (`:978`),
   `init_hpratio` (`:979`) and `skill` (`:988`, `:994`). **It never reads the
   thumb's `attr`** at actor offset `+0x24`. The complete offset set is in §2.6.
3. `analysis/ghidra-enemycamp-decomp-02.txt:374-384` — the element the in-battle
   actor actually carries is taken from `CSRCardInfo::GetRefAttr` on the
   fixed-actor branch and stored at actor `+0x7c`.
4. `analysis/research/card-enums.md:96-100` — `GetRefAttr` returns reference
   member `+0x6c`, and the instance getter resolves the normal **or awakened**
   reference. So the STAT row's `attr` is the element the client uses, and the
   reference is tier-resolved.

**New this pass — the thumbs are demonstrably copied, not authored.** All four
Episode rows of the `EVCB03xx` family that involve Alia and her Lunar New Year
costume carry a **byte-identical thumb**:

| row | file | `res_id` | thumb |
|---|---|---|---|
| `EVCB0301_070` | `EPISODE_COMBAT_EVCB0301.json` | `C070` | level 1 / rank 5 / hyper 0 / **attr 3** |
| `EVCB0301_C085` | `EPISODE_COMBAT_EVCB0302.json` | `C085` | level 1 / rank 5 / hyper 0 / **attr 3** |
| `EVCB0301_C085` | `EPISODE_COMBAT_EVCB0303.json` | `C085` | level 1 / rank 5 / hyper 0 / **attr 3** |
| `EVCB0301_C085` | `EPISODE_COMBAT_EVCB0304.json` | `C085` | level 1 / rank 5 / hyper 0 / **attr 3** |

All four also share the actor-id prefix `EVCB0301_`, and `085`'s single STAT
entry is *defined* in the `EVCB0301` record while being *placed* by three later
records — one STAT entry, three placements, one thumb, copied. By contrast the
`070` and `085` **STAT** rows are independently authored: they differ in `attr`,
`hp`, `def` (`EPISODE_STAT_ACTORS.json:1715-1735` vs `:1847-1867`). The thumb
carries no information the STAT row does not already contradict.

**Therefore `085`'s gameplay element is Fire**, from
`EPISODE_STAT_ACTORS.json:1850`.

**The crosswalk's tie-break is retracted.** It argued that because the catalogue
infers `085`'s owner as `070` Alia, who is Lightning, "the thumb agrees with the
owner, so the thumb is right". That reasoning fails twice: the thumb is not a
consumer of the element, and **element is not inherited from the costume owner**
(§1.3; `026` and `034` already show a variant carrying a different element from
its base).

**The costume lineage is independently confirmed.** `char-str.tsv:86` (`085`
"Lunar New Year") carries a `SUMMARY` **byte-identical** to `char-str.tsv:71`
(`070` "Electrotherapist"); `skill-tag.tsv` gives `085` slot 3 `JOB_SUP`, the
same as `070`; and `skill-ref` for `085` is `070`'s slot-1-to-3 text verbatim,
rebalanced in slot 4. Role is **Support** on three sources (prose, `JOB_SUP`,
Episode `role 4`); the catalogue leaves it blank. So `085` is a Lunar New Year
costume of Alia — and its **element is its own**, Fire.

## 1.3 The element rule for `059`, `009`, `010` — **RESOLVED as a RULE; `009`/`010` closed**

**The rule, stated once:**

> **Element belongs to the (card, tier) pair — i.e. to the specific card *form* —
> not to the card id and not to the costume art pack. The tier key is the COMBAT
> record's `hyper`, which the client copies into the actor's card via
> `CSRCard::SetOvercome`. A base card and its awakened/costume tier can carry
> different elements, and the `C5xx` art packs track the costume tier rather than
> causing it.**

Evidence, in the order that matters:

1. **Tier is the selector, not the pack.** Across every hero row of every one of
   the 61 COMBAT records, `attr` is a **single-valued function of
   (`ref_id`, `hyper`)** over **85 distinct cells with zero conflicts** (§2.5).
   It is **not** single-valued per art pack: the plain `C009` pack alone carries
   both Lightning and Fire.
2. **Role never varies with tier, element does — for exactly two heroes.** Over
   the same 85 cells `role` is single-valued everywhere except one cell
   (`005` at the base tier, §2.3). That asymmetry is itself evidence that
   element is a designed per-tier property rather than authoring noise.
3. **The decisive control is `CB1604_C009`.** `EPISODE_COMBAT_CB1604.json:16-21`
   places Captain on the **plain `C009`** art pack — no `C5xx` anywhere — at
   hyper 3, and still flips the element; `EPISODE_STAT_ACTORS.json:6227-6231` is
   that row's STAT entry. A tier flip on the base pack proves the pack is not
   the cause.
4. **Exactly two heroes change element with tier, both at the top tier, and both
   land on the value the community catalogue independently records for their
   awakened row.** `009` goes Lightning → **Fire**, and
   `card-catalogue.tsv:13` has `009_1` Captain (Awakened) = **Fire**. `010` goes
   Lightning → **Ice**, and `card-catalogue.tsv:15` has `010_1` Vincent
   (Awakened) = **Ice**. Two independent sources, one shipped and one community,
   arriving at the same per-tier split from opposite directions.
5. **The `C5xx` packs are the costume tier, not the cause.** `C509` and `C510`
   occur *only* on the `CB17xx` records and *only* at hyper 3; they are the only
   two `C5xx` packs the Episode table ever names. Their thumbs additionally
   carry `awake_step` / `awake_hyper`, and their STAT rows are the only four in
   the whole table carrying an `awk_step` marker — every one `"1"` (§2.5).
   `analysis/catalogue/INDEX.md:231-233` records twelve `C5xx` packs that no
   `CHAR_STR_RO` row references: the same costume-tier signature as the
   `C0nnA`/`C0nnB` alternates.
6. **Native shape agrees.** `analysis/research/card-enums.md:96-100` states the
   instance element getter resolves the normal **or awakened** reference. "Element
   follows the tier" is how the engine is built, not an artefact of the data.
7. **A fourth source agrees on the base forms.** The `vsfan` wiki reads `009` =
   Defense/Electric (`vsfan-wiki-2026-10-05.md:474`) and `010` =
   Offense/Electric (`:515`). Combined with the archive, the catalogue and the
   Episode base-tier rows, the base element of both is **Lightning on four
   independent sources**. The wiki's own corpus documents no element change with
   transcendence (§0.3).

**Consequence for `009` / `010` — closed.** Their base-form identity element is
Lightning; their costume/awakened tier is Fire and Ice respectively. There is no
contradiction left. The crosswalk's "element varies by costume pack" was a true
observation of the wrong mechanism.

**Consequence for `059` — §1.4. Still open on the identity axis.**

## 1.4 `059` Jack O' Lantern — **the gameplay question is CLOSED; the identity question is NOT**

Applying the §1.3 rule reduces `059` to **one** remaining element conflict in the
entire table. It has to be split into two questions that the previous version of
this file ran together.

### (a) What element does the client put on the actor in encounter `EVCB0105`? — **Lightning, closed**

- `EPISODE_STAT_ACTORS.json:3894` — the sole Episode row for `059` reads
  `attr 3` (Lightning), at the **base** tier, in **both** the STAT row and its
  own COMBAT thumb (`EPISODE_COMBAT_EVCB0105.json:92-97`, hyper 0, `attr 3`).
- Per §1.2 step 2, the STAT `attr` is the only element the fixed-actor path
  consumes; the thumb is not read.
- Therefore the encounter actor is Lightning **as a matter of recovered
  mechanics**, and this is not open.

### (b) What element is the recruitable card `059`? — **not proven. Fire is strongly indicated.**

The conflict:

- `archived-hunter-database-2019.tsv` row `catalog_id 059`
  (`element_ja` 火炎, capture `20191216043248`) reads **Fire**.
- `card-catalogue.tsv:74` reads **Fire**.
- The single shipped Episode row reads **Lightning**.

The balance of evidence, stated with its arithmetic:

- **The Episode table's base-tier element is otherwise a reliable proxy for the
  card's element.** Of the **45** Episode heroes that also have a usable archive
  element, **44 have at least one Episode tier whose `attr` equals the archive
  element. `059` is the only hero that never agrees, at any tier** (§2.1). At
  row level the same fact reads **69 of 72** rows agreeing, with the only three
  disagreements in the whole table being `009` at the top tier, `010` at the
  top tier, and `059` at the base tier — the first two already explained by the
  §1.3 rule.
- **`059` is a pure re-skin of `001` in every shipped *string* table.**
  `SUMMARY` byte-identical to `001` (`char-str.tsv:60` vs `:2`), `VICTORY`
  byte-identical, `skill-ref` byte-identical, `skill-tag` byte-identical, and the
  2019 archive stat triple byte-identical. Only the accessory differs
  (`Halloween Pumpkin` vs `Judecca's Gift`). `001`'s own Episode rows read
  `attr 1` (Fire) at **both** tiers it appears (§2.5), and `001`'s archive
  element is also 火炎.
- **Correction to the previous version of this file:** it described `059` as "a
  pure re-skin of `001`" in a way that implied its STAT row was a copy too. It
  is **not**: the `001` and `059` STAT stat-blocks differ in **12 of 14** fields,
  including a different `stat.rank` (§2.9). The STAT row is *independently
  authored*, which cuts both ways — it means the lone `attr 3` is a deliberate
  authored value for this encounter, and it equally means the row is not a
  copy-propagation artefact that could be dismissed as mechanically inherited.
  This is stated because the previous wording overstated the re-skin case.
- The `vsfan` wiki has **no `059` page** (§0.3), so it adds nothing either way.

**Verdict: (b) UNRESOLVED.** Fire is the better-supported reading — a 44-of-45
reliable field, two independent external sources, and an exact character identity
with `001` whose own element is Fire — but the shipped Episode row is a
*deliberate* authored value for a specific scripted encounter, and nothing in the
workspace adjudicates between a story-actor element and a card element. The
Episode table is explicitly **not** a card reference table. Do not silently pick
Fire (the crosswalk's implicit lean) or Lightning.

## 1.5 `038_1` "Twilight Santa Girl" — owner inference — **RESOLVED: the inference is CORRECT**

The crosswalk flagged that `038_1`'s title contains "Twilight", which is `021`
Rebecca's epithet, and suspected the catalogue's owner (`038`) was wrong.

**It is not wrong.** `038_1` is the awakened form of `038`, and `038` is a Rebecca
costume. Every shipped field says so:

- `char-str.tsv:120` — `038_1`'s `SUMMARY` is **byte-identical** to
  `char-str.tsv:116` (`021_1` "Raging Flames of Iron"). The description is
  copied from the *awakened Rebecca* text, which is what a costume-of-a-costume
  does.
- `char-str.tsv` `VICTORY` column — `021`, `021_1`, `038` and `038_1` all carry
  one byte-identical voice line. They are one character; the next-largest such
  group anywhere is size 2.
- Gear: `038_1`'s weapon/armor/accessory triple is byte-identical to `038`'s
  (`Surprise Bat` / `Santa Dress` / `Angel Wings`) and **different** from
  `021_1`'s (`Flames of Iron Bat` / `Gangster Hoodie` / `Skull Necklace`). Gear
  follows the costume, so `038_1` is the awakening *of that costume*.
- `skill-tag.tsv` slot 3: `021`, `038`, `021_1` and `038_1` all read `JOB_ATT`.
- `skill-ref.tsv`: `038_1`'s rows are byte-identical to `021_1`'s and `038`'s to
  `021`'s — the same two-step lineage, base → costume → awakened costume.
- `card-catalogue.tsv:52` already records `owner_card_id = 038`. Correct.

**Why "Twilight" is not counter-evidence.** It is `021`'s epithet, and the entire
Rebecca costume line already inherits `021`'s voice text verbatim — `038`
included. The epithet propagates down the whole line by exactly the same copy
mechanism that propagates the `SUMMARY`. Its appearance in `038_1`'s title is
expected.

**The same rule independently clears the other two costume-of-a-costume rows**,
so this is a rule and not a special pleading:

- `char-str.tsv:119` — `034_1` `SUMMARY` byte-identical to `char-str.tsv:117`
  (`024_1` "Sparkling Blade Claws"); gear identical to `034`'s; `JOB_DEF` on both.
- `char-str.tsv:122` — `086_1` "Valentine Condemner" `SUMMARY` byte-identical to
  `char-str.tsv:121` `056_1` "Condemner"; gear identical to `086`'s; `JOB_ATT` on
  both.

**Retract the flag.** `038_1`'s owner is `038`. Do not "correct" it.

## 1.6 Side finding — role for the ten blank catalogue rows, on two shipped sources

Not one of the four questions, but it falls out of the same sources and removes
the role axis from the crosswalk's seven UNRESOLVED rows. All ten catalogue rows
left blank for **role** are named by both the shipped prose and the shipped
`JOB_*` tag, and the two agree on all ten:

| id | catalogue line | shipped prose | shipped `JOB_*` | id | catalogue line | shipped prose | shipped `JOB_*` |
|---|---|---|---|---|---|---|---|
| `026` | `:37` | Support | `JOB_SUP` | `034_1` | `:47` | Defense | `JOB_DEF` |
| `026_1` | `:38` | Support | `JOB_SUP` | `038_1` | `:52` | Offense | `JOB_ATT` |
| `034` | `:46` | Defense | `JOB_DEF` | `085` | `:100` | Support | `JOB_SUP` |
| `086_1` | `:102` | Offense | `JOB_ATT` | `087` | `:103` | Bomber | `JOB_GUN` |
| `088` | `:104` | Defense | `JOB_DEF` | `095` | `:111` | Defense | `JOB_DEF` |

One wording caveat, reported rather than smoothed: `087` "Florist Lady" reads
"The **supportive** Bomber who decreases the whole enemies' block chance…". The
only capitalised archetype word is `Bomber`, and `JOB_GUN` agrees, but the
lowercase "supportive" is a counter-signal in the same sentence. `087`'s role is
Bomber on the weight of the tag and the capitalisation; the prose wording is
not clean.

This does **not** resolve their name, element or draw rarity — both sources speak
only to role. `026_1`, `034_1`, `038_1`, `086_1`, `087`, `088` and `095` therefore
remain **UNRESOLVED as complete identities**; only their role axis is now
shipped-attested twice.

## 1.7 Side finding — the catalogue's costume anchoring is inconsistent (reported, not fixed)

The catalogue marks **12** rows `inferred_owner = yes`, anchoring them to the
*original* character (`034`→`024`, `026`→`004`, `085`→`070`, `086`→`056`,
`088`→`046`, `095`→`079`, `087`→`067`, `098`→`068`) and their awakened forms to
the costume (`034_1`→`034`, `038_1`→`038`, `086_1`→`086`, `026_1`→`026`).

Five further rows are marked **self-owned** although the shipped string tables
give them an unambiguous parent character:

| id | catalogue line | shipped parent | evidence |
|---|---|---|---|
| `038` | `:51` | `021` Rebecca | `SUMMARY` byte-identical; `skill-ref` byte-identical |
| `059` | `:74` | `001` Lantern | `SUMMARY` + `VICTORY` + `skill-ref` + `skill-tag` byte-identical |
| `060` | `:75` | `013` Denali | `SUMMARY` + `skill-ref` byte-identical |
| `042` | `:56` | `006` Sylvester | `SUMMARY` + `skill-ref` byte-identical |
| `082` | `:97` | `066` | `SUMMARY` byte-identical |

So the file anchors `034` to its original character but `038` to itself. That is
an **inconsistent anchoring convention in the catalogue**, not a `038_1` defect —
and note that *either* convention leaves `038_1`'s parent as `038`, never `021`,
so §1.5 is unaffected. **No data file was changed.**

## 1.8 Scoreboard

| # | Contradiction | Verdict | Deciding evidence |
|---|---|---|---|
| 1 | `071` role Offense vs Defense | **RESOLVED → Defense** | two independent shipped sources (`char-str.tsv:72` prose; `skill-tag.tsv` `JOB_DEF`) + catalogue, 3-to-1 over one Episode row; `005` proves per-encounter role overrides exist |
| 2 | `085` STAT Fire vs thumb Lightning | **RESOLVED → Fire (STAT)**; crosswalk tie-break **retracted** | `MakeStageInst` never reads thumb `attr`; element comes from `GetRefAttr`; the three `085` thumbs are byte-identical copies of `070`'s own thumb |
| 3 | `009` / `010` element by costume pack | **RULE ESTABLISHED**; both **closed** | `attr` is a single-valued function of (card, tier) over 85 cells; `CB1604_C009` flips on the *plain* pack; tier-3 values match the catalogue's awakened rows; wiki gives a 4th base-form attestation |
| 3b | `059` — encounter element | **CLOSED → Lightning** | single shipped STAT row; the only element the fixed-actor path consumes |
| 3c | `059` — card element | **UNRESOLVED**; Fire strongly indicated | 44 of 45 Episode heroes agree with the archive at ≥1 tier and `059` never does; archive + catalogue say Fire; but the Episode row is deliberately authored and no shipped card table exists |
| 4 | `038_1` owner inference | **RESOLVED → inference correct**, flag retracted | `SUMMARY`/`VICTORY`/gear/`JOB_*`/`skill-ref` lineage 021 → 038 → 038_1; same rule clears `034_1`, `086_1` |

**What remains open after this pass: `059`'s card element, and nothing else from
the original list.** The seven blank catalogue rows keep their unresolved name /
element / rarity; the fifteen awakened `_1` rows are still single-source for
everything except the four whose role is now shipped-attested twice.

---

# 2. UNPURE — every numeral, quarantined

**Rule for this section.** Nothing below is a base stat, a coverage credit, or a
rebalance input. It is recorded so the derivations can be re-checked without being
re-done. Per `coverage.md`, none of it changes **heroes 1/113 · accessories
1/100 · monsters 0/22**.

## 2.1 Arithmetic of the sources used

| Quantity | Value |
|---|---:|
| `char-str.tsv` rows | 121 |
| `card-catalogue.tsv` rows | 121 (112 card rows + 9 non-card) |
| `skill-tag.tsv` rows / distinct cards | 565 / 113 |
| `skill-ref.tsv` rows / distinct cards | 1070 / 113 |
| Episode COMBAT records (excluding `*.manifest.json`) | 61 |
| Episode COMBAT actor slots, total | 408 |
| — of which empty placeholder `{}` slots | 168 |
| — non-empty actor rows | **240** |
| — of which `type: hunter` / `type: monster` | 160 / 80 |
| — rows whose STAT `res_id` is a hero pack (`M*` excluded) | **168** (160 hunter-typed + 8 monster-typed that reuse a card `res_id`) |
| Episode STAT entries, total | 152 |
| — empty (`{}`) entries | 1 |
| — non-empty entries | **151** |
| — `res_id` begins with `M` | 34 |
| — hero STAT rows | **117** |
| — hero STAT rows lacking `ref_id` | 0 (all 31 `ref_id`-less non-empty entries are monsters) |
| distinct `(ref_id, hyper)` cells over hero combat rows | **85** |
| cells where `attr` conflicts inside a cell | **0** |
| cells where `role` conflicts inside a cell | **1** (`005` at hyper 0) |
| heroes whose `attr` changes across tiers | **2** (`009`, `010`) |
| heroes whose `role` changes across tiers | **0** |
| `res_id` carrying more than one `attr` | **1** (`C009`) |
| STAT rows never referenced by any COMBAT actor | 1 (`CB0002_M01`, a monster) |
| distinct hero `ref_id`s in Episode | **55** |
| Episode hero rows whose `ref_id` ends `_1` | **0** |
| `R_EPISODE.jet` logical resources / occurrences of `C059` | 66 / **1** |

### Episode ↔ archive cross-validation, re-derived

| Axis | Result |
|---|---|
| **role**, STAT entry vs archive | **102 / 103** agree; sole mismatch `CB0102_005_1` |
| **element**, per hero (≥1 tier must match) | **44 / 45** agree; sole failure `059` |
| **element**, per `(ref_id, tier)` cell | **69 / 72** agree; failures `009`@3, `010`@3, `059`@0 |
| **element**, per STAT entry (crosswalk's unit) | 97 / 103 agree; 6 mismatching entries, all `C509`/`C510`/tier-3 except `EVCB0105_059` |
| Episode heroes with no archive element | 10 (`064 068 069 070 071 072 078 080 082 085`) |

The three "element" rows above are the same fact at three units of aggregation;
they are listed separately so they cannot be conflated.

## 2.2 `071` — the numbers behind the resolution

| Source | File:line | Reads |
|---|---|---|
| Episode STAT (only row) | `EPISODE_STAT_ACTORS.json:4279-4283` | `attr 1`, `role 1`, `cool_time 7000` |
| — its stat block | `:4284-4299` | `rank 5`, `hp 14000`, `atk 2300`, `def 280`, `spd 7.00`, `crt_chance 30.00`, `crt_dmg 250`, `penetration 0`, `attr_enhance 20`, `block_chance 0.00`, `block_dec_dmg 60`, `attr_resist 20`, `hp_regen 180` |
| — its encounter thumb | `EPISODE_COMBAT_CB1502.json:26-31` | `level 1`, `rank 5`, **`hyper 3`**, `attr 1` |
| Catalogue | `card-catalogue.tsv:86` | rarity 4, role Defense, element Fire, weapon "Fiery Sword" |
| Shipped prose | `char-str.tsv:72` | Defense |
| Shipped job tag | `skill-tag.tsv` slot 3 | `JOB_DEF` |
| `091` prose / tag / catalogue | `char-str.tsv:92` / slot 3 / `card-catalogue.tsv:107` | Defense / `JOB_DEF` / rarity 4, role Defense, element **Lightning**, weapon "Lightning Sword" |

The glass-cannon shape of the `CB1502_071` row, and its placement on the
**top-tier** row, are consistent with an encounter-level script — which is what
the `005` precedent says a divergent role there means. Neither is evidence of
Anemone's own class. `071`'s own element (`attr 1` = Fire) matches
`card-catalogue.tsv:86` exactly.

## 2.3 The `005` per-encounter role override — the precedent, in full

| Actor id | File:line | `role` | `rank` | thumb `hyper` | thumb `attr` | `res_id` |
|---|---|---:|---:|---:|---:|---|
| `CB0102_005_1` | `:6534-6538` | **1** | 2 | 0 | 2 | `C005` |
| `CB0103_005_1` | `:6616-6620` | 2 | 2 | 0 | 2 | `C005` |
| `CB0401_005_1` | `:11912-11916` | 2 | 4 | 0 | 2 | `C005` |
| `EVCB0201_005` | `:515-519` | 2 | 5 | 0 | 2 | `C005` |

Same art pack, same `attr`, same tier index; only `CB0102_005_1` dissents. This
is the sole cell in the 85-cell table where `role` is not single-valued. Its
precedent is what stops a lone dissenting Episode row from outvoting two
agreeing shipped sources — and it is why `071`'s single dissenting row cannot
either.

## 2.4 `SUMMARY` prose and `JOB_*` tag — validation arithmetic

| Measurement | Value |
|---|---:|
| `char-str.tsv` rows | 121 |
| rows naming exactly one archetype word | 110 |
| rows naming an archetype word plus a second non-archetype word | 1 (`011_1` — "A **Defense** who overwhelms the **Attacker**"; intended archetype Defense) |
| rows naming no archetype word | 10 (`009_1`, `097`, `901`, `902`, `903`, `904`, `912`, `913`, `914`, `x914`) |
| prose vs catalogue, both present | **101 compared, 101 agree, 0 disagree** (100/100 excluding `011_1`) |
| prose vs `JOB_*`, both present | **110 compared, 110 agree, 0 disagree** |
| `JOB_*` vs catalogue role, both present | **102 compared, 102 agree, 0 disagree** |
| `JOB_*` coverage | 112 of 113 cards (`051` has none); slot 3 on 110 cards, slot 5 on `036` and `043` |
| `JOB_*` vs Episode role, ≥1 tier must match | **53 / 55** agree; exceptions `051` (no tag) and `071` (`JOB_DEF` vs Episode Offense) |

Prose says nothing about element. No shipped table carries an element tag.

## 2.5 The element rule — the full `(ref_id, hyper) → attr` matrix

Element names via `card-enums.md:24-27` (`0 NONE`, `1 Fire`, `2 Ice`,
`3 Lightning`). **Every cell below is single-valued; there are no conflicts.**

```
001 h0=Fire h1=Fire              033 (no rows)
003 h0=Ice  h1=Ice               034 h0=Ice
004 h0=Fire h2=Fire              036 h0=Lightning h2=Lightning
005 h0=Ice                       038 h1=Fire
006 h2=Fire                      039 h0=Lightning h1=Lightning
007 h0=Fire                      040 h0=Lightning h2=Lightning
008 h0=Lightning h2=Lightning    041 h1=Lightning h2=Lightning
009 h0=Lightning h2=Lightning h3=Fire    <-- TIER FLIP
010 h0=Lightning h2=Lightning h3=Ice     <-- TIER FLIP
011 h0=Fire h1=Fire h2=Fire      042 h1=Fire
012 h0=Lightning h1=Lightning h2=Lightning   043 h1=Ice
013 h0=Fire                      046 h3=Ice
014 h1=Ice                       049 h0=Fire
016 h0=Ice  h3=Ice               051 h0=Ice
017 h0=Ice  h3=Ice               052 h1=Lightning
018 h0=Ice  h2=Ice               054 h2=Ice h3=Ice
019 h0=Lightning h2=Lightning     055 h0=Fire
020 h1=Lightning                 056 h1=Ice h2=Ice h3=Ice
021 h0=Fire  h1=Fire             057 h0=Ice h2=Ice
023 h0=Fire  h2=Fire             058 h0=Lightning
024 h1=Lightning                 059 h0=Lightning   <-- UNRESOLVED vs archive/wiki Fire
027 h0=Fire                      060 h0=Fire
028 h0=Ice  h1=Ice               064 h2=Lightning h3=Lightning
029 h0=Lightning                 068 h0=Ice h2=Ice h3=Ice
030 h1=Lightning                 069 h1=Ice
032 h0=Ice                       070 h0=Lightning
                                 071 h3=Fire
                                 072 h0=Lightning
                                 078 h0=Ice
                                 080 h0=Lightning
                                 082 h1=Lightning
                                 085 h0=Fire
```

`role` over the same 85 cells: single-valued everywhere **except**
`(005, hyper 0)` = {1, 2} — the §2.3 override. **Role never varies with tier;
element does, for exactly two heroes.**

### The two tier flips, against the community catalogue

| hero | tier `hyper` | Episode `attr` | catalogue base element | catalogue `_1` element | catalogue `_1` line |
|---|---:|---|---|---|---|
| `009` | 0 | Lightning | Lightning | **Fire** | `card-catalogue.tsv:13` |
| `009` | 2 | Lightning | | | |
| `009` | 3 | **Fire** | | | |
| `010` | 0 | Lightning | Lightning | **Ice** | `card-catalogue.tsv:15` |
| `010` | 2 | Lightning | | | |
| `010` | 3 | **Ice** | | | |

Catalogue base vs `_1` element across the Episode table, recomputed: of the 13
base heroes present in Episode that have a comparable `_1` row, **9 have an
identical element, 2 differ, 2 are not comparable** (`034`/`034_1` both blank,
`038_1` blank). **The only two that differ are exactly the two that flip.** No
`_1` card appears in the Episode table at all, so this is a comparison against
the community catalogue's awakened rows, not a shipped tier comparison.

### The top-tier rows, complete

```
CB1402  046 C046 stat 2 thumb 2      CB1502  071 C071 stat 1 thumb 1
CB1402  056 C056 stat 2 thumb 2      CB1502  017 C017 stat 2 thumb 2
CB1402  064 C064 stat 3 thumb 3      CB1502  016 C016 stat 2 thumb 2
CB1402  068 C068 stat 2 thumb 2      CB1502  054 C054 stat 2 thumb 2  (x2)
CB1604  009 C009 stat 1 thumb 1      CB1701  010 C510 stat 2 thumb 2
CB1702  009 C509 stat 1 thumb 1      CB1702  010 C510 stat 2 thumb 2
CB1703  010 C510 stat 2 thumb 2      CB1704  010 C510 stat 2 thumb 2
CB1705  010 C510 stat 2 thumb 2      CB1706  009 C509 stat 1 thumb 1
                                     CB1706  010 C510 stat 2 thumb 2
```

`CB1604` is the control: top tier, **plain `C009` pack**, Fire.
`C509`/`C510` appear **only** in the `CB17xx` records and **only** at the top
tier, and are the only thumbs carrying `awake_step 1` / `awake_hyper 3`.

`attr_resist 99` (the apparent sentinel) sits on exactly 10 STAT rows:
`EPISODE_STAT_ACTORS.json` lines for `CB1701_C510`, `CB1702_C510`, `CB1702_C509`,
`CB1706_C509`, `CB1402_C056`, `EVCB0201_082`, `CB0002_BOSS`, `CB0003_BOSS`,
`CB0004_BOSS`, `CB0302_010_1`. Every one is either a `C5xx` costume pack, the
`082`/`056` top-tier row, or a Vincent boss row — never an ordinary base-tier
hunter row. Note `CB0302_010_1` is a **hunter**-typed row on the **plain `C010`**
pack, so the sentinel is not exclusive to costume art either.

`awk_step` appears in the STAT stat block on exactly 4 of the 117 hero rows, all
on `C509`/`C510`, all `"1"` (`CB1701_C510`, `CB1702_C510`, `CB1702_C509`,
`CB1706_C509`). It is the only stat-block tier marker shipped.

`state.init_hpratio` appears on exactly 10 actor rows across 8 different COMBAT
records — it is an ordinary per-encounter HP tuning knob, present on base-tier
rows too, and is **not** a marker of anything unusual about `CB1604`.

## 2.6 `thumb.attr` — the bounded negative

`CSRMEpisode::ACTOR::ACTOR` (`analysis/ghidra-episode-fixed-actor.txt`) parses,
in order, the keys resolved at `analysis/ghidra-episode-fixed-actor-keys.txt:2-11`:
`thumb / level / rank / hyper / awake_step / awake_hyper / attr / state /
init_hpratio`. `thumb.attr` is genuinely parsed and written to the episode actor
record at `+0x24`. Note that `ParseActor`'s STAT `attr` and the ACTOR thumb
`attr` resolve to the **same literal address** (`0x1d6f9d9`,
`ghidra-episode-combat-actors-keys.txt:21` and
`ghidra-episode-fixed-actor-keys.txt:8`), which is exactly why the two are easy to
conflate.

`CSRSceneMEpisode::MakeStageInst` fixed-actor branch
(`analysis/ghidra-episode-first-combat.txt:929-1075`) reads these actor offsets
and no others:

| Actor offset | Field | Consumer | line |
|---:|---|---|---|
| `+0x00` | `type` string | compared against `"monster"` | `:931-941` |
| `+0x10` | `rank` | written to `ACTOR_INFO + 0x24` | `:976` |
| `+0x14` | `hyper` | `CSRCard::SetOvercome` arg 1 | `:978` |
| `+0x18` | `awake_step` | `CSRCard::SetAwake` | `:977` |
| `+0x1c` | `awake_hyper` | `CSRCard::SetOvercome` arg 2 | `:978` |
| `+0x20` | `init_hpratio` | local | `:979` |
| `+0x24` | **`attr`** | **not read** | — |
| `+0x34` / `+0x38` | shared `CSRCardInfo` | copied into the new `ACTOR_INFO` | `:947-948`, `:1054` |
| `+0x3c` / `+0x40` | `skill` tree | `__assign_multi` | `:988`, `:994` |

This is a negative bounded to this one function on the fixed-actor path. A
UI-only consumer of `thumb.attr` elsewhere in the binary is **not excluded**, and
is not needed: the gameplay element is already accounted for at
`ghidra-enemycamp-decomp-02.txt:383`.

## 2.7 `085` versus its owner `070` — the raw numbers

| Field | `070` (`:1715-1735`) | `085` (`:1847-1867`) |
|---|---|---|
| `attr` | 3 | **1** |
| `role` | 4 | 4 |
| `cool_time` | 5000 | 5000 |
| `hp` | 2000 | 2200 |
| `atk` | 1000 | 1000 |
| `def` | 900 | 1000 |
| `spd` / `crt_chance` / `crt_dmg` | 7.00 / 14.00 / 200 | 7.00 / 14.00 / 200 |
| `penetration` | 0.00 | 0.00 |
| `attr_enhance` / `attr_resist` | 5 / 5 | 5 / 5 |
| `block_chance` / `block_dec_dmg` | 14.00 / 40 | 14.00 / 40 |
| `hp_regen` | 45 | 45 |
| `rank` | 5 | 5 |
| `skill-ref` rows | 11 | 12 |
| thumb, all occurrences | level 1 / rank 5 / hyper 0 / **attr 3** | level 1 / rank 5 / hyper 0 / **attr 3** |

`skill-ref.tsv` diff, `070` → `085`: slots 1–3 are identical in `EN`, `FORMULAR`,
`IS_FLOAT` and `SUB_SERIAL` (only `skill_id` differs), then `085` adds one extra
row and rebalances the rage effects — `070` row 9 is `IS_FLOAT 1`, "Increases 2
Rage Gauge of the team"; `085` splits that into `IS_FLOAT 0`, "Increases 1 Rage
Gauge of the team" plus a new `IS_FLOAT 0`, "Decreases 1 Rage Gauge of the
enemy.", and its `SUB_SERIAL` on the bleed row shifts from 2 to 3.

That is a **rebalanced variant of Alia's kit, not a copy** — which is why the
catalogue's `owner` column is an inference about the *character*, not a statement
that every field is inherited. Element is one of the fields that is **not**
inherited (§1.3).

## 2.8 `038_1` — lineage fingerprints

Gear triples (`char-str.tsv`, weapon / armor / accessory):

| Row | Triple |
|---|---|
| `038` (`:39`) | Surprise Bat / Santa Dress / Angel Wings |
| `038_1` (`:120`) | Surprise Bat / Santa Dress / Angel Wings |
| `021` (`:22`) | Fire Bat / Gangster Hoodie / Skull Necklace |
| `021_1` (`:116`) | Flames of Iron Bat / Gangster Hoodie / Skull Necklace |

`VICTORY` byte-identical groups of size ≥ 2 (all of them):

```
4x ['021','021_1','038','038_1']   4x ['024','024_1','034','034_1']
2x ['001','059']  2x ['004','004_1']  2x ['005','005_1']  2x ['013','060']
2x ['019','019_1']  2x ['026','026_1']  2x ['056','056_1']  2x ['086','086_1']
2x ['914','x914']
```

`SUMMARY` byte-identical groups of size ≥ 2 (all of them):

```
['001','059']              ['006','042']              ['013','060']
['020','020_1']            ['021','038']              ['024','034']
['046','088']              ['056','086']              ['066','082']
['070','085']              ['071','091']              ['075','093']
['004_1','026_1']          ['021_1','038_1']          ['024_1','034_1']
['056_1','086_1']
```

`skill-tag.tsv` byte-identical groups of size ≥ 2 (all of them):

```
['001','059']              ['004','026']             ['006','042']
['013','060']              ['016','030','035']       ['021','038']
['024','034']              ['056','086']             ['079','095']
['004_1','026_1']          ['021_1','038_1']         ['024_1','034_1']
['056_1','086_1']          ['071','091']
```

`skill-ref.tsv` byte-identical groups of size ≥ 2 (all of them):

```
['001','059']  ['004','026']  ['006','042']  ['013','060']  ['021','038']
['024','034']  ['071','091']  ['004_1','026_1']  ['021_1','038_1']
['024_1','034_1']  ['056_1','086_1']
```

Note `056`≡`086` in `skill-tag` but **not** in `skill-ref` — the Valentine
Genovia variant's tag profile matches while its skill text was rebalanced. The
pair is still same-character on three other tables, but the combined
"identical in both tables" shorthand is wrong for that one pair.

Row counts: `skill-ref` `021`/`038` = 7 each; `021_1`/`038_1` = 9 each;
`skill-tag` = 5 slots for every card checked, including all four Rebecca rows.

Note the recurrence of the `X` → `X_1` → `X_variant_1` shape across
`021`/`038`, `024`/`034`, `056`/`086`, `004`/`026`. `038_1` is the fourth instance,
not an anomaly.

## 2.9 `059` — the unresolved numbers

| Source | File:line | Reads |
|---|---|---|
| Episode STAT (only row) | `EPISODE_STAT_ACTORS.json:3891-3895` | `attr 3`, `role 3`, `cool_time 5000` |
| — stat block | `:3897-3910` | `rank 5`, `hp 1700`, `atk 1300`, `def 600`, `spd 7`, `crt_chance 14.00`, `crt_dmg 203`, `penetration 0.00`, `attr_enhance 10`, `block_chance 14.00`, `block_dec_dmg 42`, `attr_resist 0`, `hp_regen 40` |
| — encounter thumb | `EPISODE_COMBAT_EVCB0105.json:92-97` | `level 1`, `rank 5`, `hyper 0`, `attr 3` |
| Archive | `archived-hunter-database-2019.tsv` (`element_ja` 火炎) | Fire; capture `20191216043248` |
| Catalogue | `card-catalogue.tsv:74` | rarity 3, role Bomber, element Fire |
| Shipped prose | `char-str.tsv:60` | Bomber |
| Shipped job tag | `skill-tag.tsv` slot 3 | `JOB_GUN` |
| Wiki | — | **no page** (§0.3) |

Comparison baseline, `001`: archive triple `1521/1058/653`, capture `20191209130238`,
element 火炎; `059` archive triple `1521/1058/653`, capture `20191216043248`,
element 火炎 — byte-identical.

`001` vs `059` STAT stat-blocks, field by field — **12 of 14 differ**:

| Field | `001` | `059` | | Field | `001` | `059` |
|---|---:|---:|---|---|---:|---:|
| `rank` | 4 | 5 | | `crt_dmg` | 180 | 203 |
| `hp` | 390 | 1700 | | `attr_enhance` | 0 | 10 |
| `atk` | 200 | 1300 | | `attr_resist` | 0 | 0 (same) |
| `def` | 180 | 600 | | `block_chance` | 20.00 | 14.00 |
| `spd` | 7.00 | 7 | | `block_dec_dmg` | 40 | 42 |
| `crt_chance` | 20.00 | 14.00 | | `hp_regen` | 26 | 40 |
| `penetration` | 0 | 0.00 | | `attr` | 1 (Fire) | **3 (Lightning)** |

So the character is a byte-identical re-skin across four shipped string tables
and one stat table, while the **Episode STAT row is independently authored** —
and its one non-matching field against the archive is `attr`. That is the whole
of the `059` problem in one table.

## 2.10 Corrections to the previous version of this file

Every one of these was re-derived this pass; all are arithmetic, none changes a
conclusion.

| # | Previous statement | Corrected | Why it matters |
|---|---|---|---|
| 1 | "Episode COMBAT actor rows (non-empty) 240 … hero rows 173 (168 after dropping the two monster rows that reuse a card `ref_id`)" | 408 slots → 168 empty `{}` placeholders → **240 non-empty** → **168 rows whose STAT `res_id` is a hero pack** (160 hunter-typed + **8** monster-typed reusing a card `res_id`) | The "2 monster rows" was wrong; there are **8**, and they include `CB1102_006/008/011/018/019` plus `CB0002/0003/0004_BOSS`. The endpoint 168 was right |
| 2 | "prose vs catalogue, both present: 100 compared, 100 agree" | **101 compared, 101 agree** | The previous pass excluded `011_1` for naming a second non-archetype word; including it (its intended archetype is Defense, matching the catalogue) gives 101 |
| 3 | "prose vs Episode enum … disagreeing: 1 (`071`)" | **2 cards carry a dissenting Episode row** — `005` and `071`. It is 1 only on an "is there any agreeing Episode row" reading, which is also true | The reading must be stated, not assumed; `071` is still the only hero with **no** agreeing Episode row |
| 4 | "For the other **ten** `_1` heroes that appear in the Episode table (`004`, `011`, `017`, `019`, `020`, `021`, `024`, `056`) …" | **No `_1` card appears in the Episode table at all** (0 of 55 hero `ref_id`s end `_1`; the list was also 8 long, not 10). Of 13 base heroes in Episode with a comparable `_1` catalogue element: **9 identical, 2 differ, 2 not comparable** | The comparison is against the *catalogue's* awakened rows, not shipped tiers |
| 5 | "`059` is a *pure re-skin* of `001`" used as evidence its lone divergent `attr` is an authoring slip | The **string tables** are byte-identical re-skins; the **STAT stat-block is independently authored** and differs in 12 of 14 fields | It removes the mechanical-inheritance argument in both directions and is the honest reason `059` stays open |
| 6 | "`059` … one shipped row against one archived third-party page plus the wiki" | There is **no `059` page in the wiki**. The two external sources are the 2019 JP archive and the community InfoboxCharacter catalogue | Naming the wiki as a third source for `059` was unsupported |
| 7 | §1.3 quoted `MakeStageInst` as `:929-1074` | The branch runs to `:1075`; all offset reads are unchanged | Line-boundary precision only |
| 8 | "the three COMBAT records that place that actor" for `085` | Correct, but the pass did not note that those three thumbs are **byte-identical to `070`'s own thumb** in the same `EVCB03xx` family | This is the strongest single piece of evidence for the `085` verdict |
| 9 | §2.5 header said "the other ten `_1` heroes"; `attr_resist 99` described as "on all four `C509`/`C510` STAT rows … and nowhere else among the tier-flip rows" | Accurate for the tier-flip rows, but `CB0302_010_1` is a **plain-`C010`, base-tier** sentinel row, so the sentinel is not costume-exclusive | Matters for anyone tempted to read `99` as a costume marker |

## 2.11 Retained numeric conventions, unchanged

- Role enum `1 Offense / 2 Defense / 3 Bomber / 4 Support` and element enum
  `0 NONE / 1 Fire / 2 Ice / 3 Lightning` (`analysis/research/card-enums.md:10-27`).
  Both mappings were used here and neither was re-derived. The `JOB_*` mapping
  `JOB_ATT`/`JOB_DEF`/`JOB_GUN`/`JOB_SUP` → Offense/Defense/Bomber/Support is
  established **empirically** in §0.2 (zero exceptions over 102 catalogue rows),
  not asserted from the native enum.
- `stat.rank` in the Episode table is a **scripted-story rank**, not draw rarity
  (`hero-identity-crosswalk-2026-10-05.md` §0.3 item 2). The tier flips in §2.5
  are keyed on the COMBAT thumb's `hyper`, a different field.
- None of the HP/ATK/DEF values above are base stats. They are per-encounter
  scripted tuning; `analysis/recovered-reference/EPISODE_COMBAT_STAT.manifest.json`
  says so verbatim ("Episode-only actor STAT table; not ordinary hunter card-base
  stats").

---

## Limits of this file

- **Identity only.** Role, element and costume lineage. It promotes nothing to
  strict coverage. Heroes stay **1/113**, accessories **1/100**, monsters
  **0/22**.
- **Read-only.** No catalogue, server, seed, state, APK or emulator file was
  touched, and no change is proposed to any of them. The only network access was
  GET-only reads of `web.archive.org` (the `Awake` page plus one CDX query), with
  a live HTTP control in the same run, matching the discipline of
  `vsfan-wiki-2026-10-05.md` §2.15.
- **`059`'s card element is deliberately left unresolved.** One deliberately
  authored shipped story-actor row against two external sources and a 44-of-45
  base-tier reliability rate. §1.3's rule is about tiers and supplies no
  tie-break for a base-tier disagreement. Reporting a firm answer would repeat the
  error this file exists to correct. Its **encounter** element *is* closed.
- **The `thumb.attr` negative is bounded** to `CSRSceneMEpisode::MakeStageInst`'s
  fixed-actor branch on the dumps on disk. It is a strong, reproducible negative,
  not a proof that no code anywhere reads that field.
- **The `005` precedent is a precedent, not a mechanism.** It proves per-encounter
  role overrides occur in this table. It does not prove that `CB1502_071` is one;
  that conclusion rests on `071` being outvoted by **two independent shipped
  sources** plus the catalogue.
- **`SUMMARY` and `JOB_*` attest role only.** Neither speaks to element, name or
  draw rarity, so §1.6 must not be read as resolving the seven blank rows.
- **`JOB_*` is an inferred semantic mapping.** The tag *names* are read as roles
  because the mapping is exception-free over 102 rows and agrees with prose on
  110. No native evidence pins the tag vocabulary to `CHAR_ROLE`; if that
  inference is ever wrong it is wrong uniformly, which is why `071` still had two
  further agreeing sources.
- The catalogue-side anchoring inconsistency (§1.7) is **reported, not fixed**.
  Changing a data file is out of scope here.