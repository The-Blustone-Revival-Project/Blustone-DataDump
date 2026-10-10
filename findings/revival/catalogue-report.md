# Catalogue research report — 121 card rows, 22 monsters

**Agent:** catalogue research agent
**Date:** 2026-10-03
**Owns:** `analysis/catalogue/`, `analysis/research/catalogue-report.md`
**Did not touch:** `server-ts/`, `recovered-assets/`, `analysis/recovered-data/`,
`analysis/ghidra-*`, `instrumentation/`, `tools/`. No adb, no Docker, no Ghidra, no
server, no Git.

Companion deliverables:

- `analysis/catalogue/INDEX.md` — the 143-row table, coverage matrix, and the
  real-vs-mock shipping recommendation.
- `analysis/catalogue/cards/*.md` — 121 files.
- `analysis/catalogue/monsters/*.md` — 22 files.
- `analysis/catalogue/data/` — machine-readable exports.

---

## 0. Web access: **YES, it worked**

Both search and fetch worked throughout. Sources reached:

| source | reached? | how |
|---|---|---|
| `blustone.miraheze.org` "Blustone Archiving Wiki" | **yes, fully** | MediaWiki `api.php`, all 335 pages dumped to `miraheze/*.wiki` |
| `namu.wiki` (Korean) | via search snippets only | direct fetch returns **403** (bot-blocked) |
| `en.namu.wiki`, `namu.moe`, `dark.namu.moe`, `readonly.wiki` | via search snippets | mirrors of the same namu content |
| `blustone.fandom.com` | **403** | direct fetch blocked; search snippets only |
| Google Sheets (Fight Club tier list) | **410 Gone** | the one numeric spreadsheet is **deleted** |
| Reddit `/r/Blustone` | **blocked** | `.json` API returns HTML, not JSON |
| `gamestierdb1.web.app` | via snippet | SEO tier-list spam farm, no real data |

So: the miraheze wiki was obtained **in full and offline**, which is why coverage is
high. namu was only reachable as search snippets — that is the single biggest reason
anything is `[UNKNOWN]` that is arguably knowable.

---

## 1. What I searched

**Local (exhaustive):**

- `analysis/recovered-data/leveldb-tables/all-tables.json` — all **13** tables,
  22,160 rows, every row read and pattern-scanned.
- `analysis/recovered-data/leveldb-tables/*.tsv` — all 6 pre-existing dumps.
- `analysis/recovered-data/native-key-vocabulary/*.tsv` — all 4.
- `analysis/recovered-data/environments.csv`, `cdn-manifest/`.
- `analysis/extracted/assets/LEVELING.jet` — **all 21 chunks listed and 12 fully
  extracted.** Two of these turned out to be important (§4).
- `recovered-assets/.../split_PADResource/assets/` — **all 774 `.jet` packages**
  enumerated; `M001/M002/M005/M010/M021/M100` byte-scanned for strings and run
  through `tools/jet-viewer/jet_decoder.py`.
- `recovered-assets/community-notes-2026-09-30/Blustone Guide FAQ.md` — 13,085,200
  chars, base64-stripped down to 39,081 chars / 658 lines and read **in full**.
- `recovered-assets/community-notes-2026-09-30/Account registration...txt` — skimmed.

**Web:** 6 searches + 4 fetches + 1 MediaWiki bulk dump (335 pages) + 1 dead
Sheets link + 1 blocked Reddit thread.

---

## 2. Source-quality assessment

Ordered by trust. **Local recovered data outranks all of it.**

1. **`LEVELING.jet` / `CHAR_STR_RO` / `SKILL_*_RO`** — shipped game data, binary
   truth. Highest confidence. Its limits are structural, not reliability: it simply
   does not contain stats.
2. **`blustone.miraheze.org`** — high quality, but *community*. It is visibly a
   **faithful transcription of namu.wiki** (each page cites namu in `== References ==`).
   Validated six separate ways against recovered data (§6 of `INDEX.md`):
   episode lists 18/18, stage count exact, roles 103/103, rage costs 101/103 with
   both exceptions correctly predicted by namu, `JOB_*` tags consistent, equipment
   descriptions byte-identical to `CHAR_STR_RO|*_DESC`.
   **Known defects:** the `Characters` index page has an **empty table**; both
   "Valentine" pages carry a **copy-pasted portrait filename**; 10 rows are absent
   entirely; `Release Date` and `VoiceActor` are `-` on most pages.
3. **`namu.wiki`** — the authoritative Korean source (the game is Korean-first;
   `CHAR_STR_RO` has a KO column). Reachability was poor (403). Everything I have
   from it is via search snippets and should be treated as **[COMMUNITY-SOURCED,
   snippet-only]** — lower confidence than the miraheze dump.
4. **The 13 MB community guide FAQ** — genuine, player-written, long-lived (last
   edited 2026). Excellent on **systems, mechanics and meta**; contains **zero
   numeric stat tables**. Every screenshot it uses is embedded base64, so its
   stat screenshots (which do exist — "Image A — Total power of a well trained /
   invested in Beckhen") are **not machine-readable and I did not read them off the
   images.** That is a genuine gap: the Beckhen stat screenshot might contain real
   numbers. Extracting them needs OCR, which I did not attempt.
5. **`blustone.fandom.com`** — near-empty (2 items on its character category page).
   Useless, and it uses a **different role vocabulary** (Striker/Defender/
   Bombardier/Helper). Do not use.
6. **SEO tier-list sites** — content farms. Discarded.

---

## 3. Cards — what was recovered

### 3.1 The headline: `card_id == skill_id`

`CHAR_STR_RO`, `SKILL_REF_RO`, `SKILL_TAG_RO` all carry **the same 113 ids**.
Every one has exactly 5 slots. This is a structural identity, not a naming
coincidence, and it is checked in `data/cards.json`.

The 5-slot activation pattern is identical for all 103 named cards:
`Active / Follows active / Passive / Follows active / Passive`.

### 3.2 Two tables that had never been dumped

`all-tables.json` was already in the repo but only 6 of its 13 tables were
exported to TSV. Two missing ones mattered:

| table | rows | what it gave | exported to |
|---|---|---|---|
| **`SKILL_EFFECT_RO`** | 230 | the **display name of every skill slot** (e.g. card 001 slot 2 = `"Penetrate Invincible\nDefense▼"`) | `data/skill-effect.tsv` |
| `CHAR_STR_RO` extra fields | 339 | **`WEAPON_DESC` / `ARMOR_DESC` / `ACCE_DESC`** — three whole description columns the existing 7-column `char-str.tsv` silently dropped | inlined into every `cards/NNN.md`, plus `data/card-catalogue.tsv` |

**339 rows of real shipped game text were sitting in the repo, unexported.** Any
server-side card `equipment[]` or `dialog[]` payload can be filled from these.

### 3.3 Costume-variant ownership — 10 rows resolved, all confirmed

10 `CHAR_STR_RO` rows have no wiki page. I resolved each by exact-string gear
matching plus `difflib` similarity between `SUMMARY` fields:

| row | owner | evidence | strength |
|---|---|---|---|
| `034` Halloween Witch | **Riko** (`024`) | `SUMMARY` **string-identical** to Riko's, and `WEAPON` is Riko's `Wolf Knuckles` exactly | very strong |
| `088` Florist | **Harley** (`046`) | `SUMMARY` **string-identical** to Harley's | strong |
| `026` In Wonderland | **Tyltyl** (`004`) | shares Tyltyl's `ARMOR` `Combat Apron`; `SUMMARY` 0.83 similar | strong |
| `038_1` Twilight Santa Girl | **Rebecca** (`038`) | gear triple identical to `038`; `SUMMARY` is the awakened rewrite of `021_1` | strong |
| `086_1` Valentine Condemner | **Genovia** (`056`) | `SUMMARY` is the awakened rewrite of `056_1` `Condemner` | strong |
| `087` Florist Lady | **Judith** (`067`) | `SUMMARY` 0.90 similar; both are the "supportive Bomber that lowers enemy block chance + rage" template | moderate |
| `085` Lunar New Year | **Alia** (`070`) | `SUMMARY` **string-identical** to Alia's | moderate — **summary only, no shared gear** |
| `095` Knight of Swimming Pool | **Lawrence** (`079`) | fastest-Defender template shared with `Defense Knight`; knight-themed weapon | **weakest** |
| `086` / `098` Valentine | **Genovia (Valentine)** / **Selene (Valentine)** | disambiguated by elimination + template; see §3.4 | strong |
| `026_1`, `034_1` | the `_1` awakened form of `026`, `034` | gear triple identical to their base row | very strong |

**These were then independently confirmed by recovered data.** Rage cost is
*[RECOVERED]* (parsed from `SKILL_REF_RO` slot-1 EN text) and role is
*[COMMUNITY-SOURCED]* (wiki). The 10 inferred owners land on exactly the role their
rage cost implies:

| row | rage | ⇒ role | owner's role | ✓ |
|---|---|---|---|---|
| `026`, `026_1` | 4 | Support | Tyltyl Support | ✓ |
| `085` | 4 | Support | Alia Support | ✓ |
| `087` | 4 | **Bomber** | Judith Bomber | ✓ |
| `034`, `034_1` | 3 | Defense | Riko Defense | ✓ |
| `088` | 3 | Defense | Harley Defense | ✓ |
| `095` | 3 | Defense | Lawrence Defense | ✓ |
| `038_1`, `086_1` | 3 | Offense | Rebecca / Genovia Offense | ✓ |

**10/10.** Two independent recovered signals agree with an inference built from a
third source. This is as strong as the costume identifications get, and it is why
I am willing to state them despite being `[INFERRED]`.

### 3.4 The one wiki collision, and its resolution

The wiki has **two** characters whose `InfoboxCharacter |Title` is literally
`"Valentine"`: `Genovia (Valentine)` and `Selene (Valentine)`. (Both also carry the
same copy-pasted portrait filename `Portrait_Genovia_(Valentine).png` — a wiki bug.)
`CHAR_STR_RO` likewise has **two** rows titled `Valentine`: `086` and `098`, with
wholly disjoint gear.

Resolved by template:

- `086` gear `Valentine's Chocolate / Pink Dress / Flower Hairband`, `SUMMARY` is
  the Genovia template → **Genovia (Valentine)**, Offense / **Fire**.
- `098` gear `Valentine's Day Boomerang / Valentine's Day Combat Uniform / Hybrid
  Gloves`, `SUMMARY` is the Selene/Support "efficient Bomber" template →
  **Selene (Valentine)**, Bomber / **Lightning**.

Note both **swap element** relative to their base cards (Genovia is Ice → Fire,
Selene is Ice → Lightning). That is a costume quirk, not an error.

### 3.5 Non-card rows (8)

`901`–`904`, `912`–`914`, `x914` have empty `SUMMARY`, empty gear, **zero**
`SKILL_REF_RO` rows and no art. They are trainer-NPC placeholders and Transcendence
Ticket item strings; the `?` is an unreplaced localisation token.

**Candidate lead for `AGENTS.md` §16.6 item 2** (the five masked
`SRCard.cpp(731)` assertions): if `/reference/GetCard` publishes all 121 rows, five
of them are empty. **[INFERRED]**, moderate confidence — worth a controlled test.

### 3.6 Awakened cards ship no art package

All 15 `_1` rows have **no** `C<n>_1.jet`. **[RECOVERED filesystem]** Awakening is a
*skin* (`CSRSkin::FindWornSkinByCardRefId`, already recorded in `AGENTS.md` §11), not
a new package. **[INFERRED]** `res_prefix` for an awakened row should be its base id.

---

## 4. `LEVELING.jet` — two chunks nobody had catalogued

`analysis/extracted/assets/LEVELING.jet` is 18,524 bytes / 21 chunks. Chunk 5 is the
already-known `environments.csv`. I extracted the rest. Two results matter.

### 4.1 The battle timer, which `AGENTS.md` §16.6 lists as [UNKNOWN]

`AGENTS.md` §16.4: *"`*(this+0x2c)+0x22c` (the time limit) is still **[UNKNOWN]**."*

It is `play_time` in these chunks. Legal values recovered: **60, 90, 150, 180,
300, 999, 9999**, across 10 difficulty/mode configs. Plus `sp_max: 10` —
**[RECOVERED]** confirmation of the Rage capacity of 10 that namu describes. And
`elem_bonus` 20/20/25/50 by band, `elem_def_bonus` 10 everywhere.

`AGENTS.md` §16.5 records `/mission/Complete` with `clear_time: 59`, and r016 ran
the fight past 298 s. So **60 is the likely mission timer** — **[INFERRED]**,
moderate confidence, and cheap to test by flipping the served value.

**Which config maps to which scene is [UNKNOWN]** — the chunks carry only an
`unk32` discriminator, no name.

### 4.2 Role and rank multipliers, and a second stage namespace

Chunk 9's `bonus` block gives the role multipliers (bomber `hp 0.85`, support
`hp 0.80`) and the monster `rank_1..5` table (`rank_1 hp 2.6` … `rank_5` all 1.0).
Full tables in `INDEX.md` §5.

It also contains the only recovered **card→stage binding in existence**:

```json
"stage": { "b_00_01": { "value": {"hp":1.1,"atk":1.1,"def":1.1,...},
                        "cards": ["051"] } }
```

`051` = **Beckhen**, *Guardian of Fight Club*. Two consequences:

- A **second stage namespace `b_XX_YY`** exists, distinct from the `n_XX_YY`
  expedition list. `AGENTS.md` §11 recovered `n_01_01` from CDN art and never found
  `b_*`. Now it is.
- Chunk 0 (`common.JSON`) enumerates the **full 50-stage expedition list**,
  `n_01_01`..`n_05_10`. namu independently states "50개의 던전" as of 2019.

### 4.3 Chunk 19 — the card power curve

66 rows, `power,rank,hyper,level`, rank 1–5 × hyper 0–3 × level 1–30. Full table in
`INDEX.md` §5.5.

**Trap warning:** this `rank` (higher = better, star count) and the monster `rank`
in §4.2 (rank 1 = hardest) are **different fields sharing a name and opposite
direction**. Both are reproduced in `INDEX.md` so nobody conflates them.

---

## 5. Monsters — the exhaustive negative result

**Nothing about any of the 22 monsters exists outside the art files.** I checked:

| where | result |
|---|---|
| all 13 LevelDB tables, 22,160 rows, regex `\bM\d{3}\b` on every key | **0 hits** |
| all 774 `.jet` packages | `M001/M002/M005/M010/M021/M100` byte-scanned: only compressed noise, **no readable strings** |
| `tools/jet-viewer/jet_decoder.py` on `M001.jet` | `inflate_jet_resources` returns **0 resources** |
| `analysis/native-all-strings.tsv` | the *keys* are there (`hp`, `atk`, `def`, `attr`, `role`, `rank`, `overcome`, …) but **no per-id values** |
| miraheze wiki, all 335 pages | **no monster page.** No page mentions a stage enemy by name |
| namu.wiki | no monster page found; namu documents hunters, not enemies |
| Fandom | 2 items, nothing |
| community guide | nothing |

### Why, structurally

Monster data is **server-authoritative**. `CSRGameMob::AddMonster` reads
`_server, title, attr, role, res_prefix, rank, level, overcome, hp, atk, def,
crt_chance, crt_dmg, penetration, block_chance, block_dec_dmg, attr_enhance,
attr_resist, hp_page, skill_start_time, skill_list, name, desc, type, effect,
effect_type` off the JSON the server sends. That JSON lived on the dead server. The
APK never had it. **The original values are therefore unrecoverable in principle** —
only a captured original-server response would yield them, and we have none.

This is not a research failure, it is a fact about the architecture. `analysis/
recovered-data/native-key-vocabulary/deck-and-arity.tsv` already recorded the
stage→wave arity as "the one real gap"; I confirm that verdict and extend it to the
entire monster record.

### The one non-recovered observation

`M001` was seen **on screen as a penguin** in the r016 battle capture
(`analysis/r016-02-BATTLE-SCENE-RENDERED.png`, per
`analysis/MILESTONE-2026-10-03-battle-renders.md`). That is a single visual
observation from a working project screenshot. It is **[INFERRED]**, low confidence,
uncorroborated, and it is recorded as such in `monsters/M001.md`. It is **not**
evidence for any of the other 21.

### What *is* recovered for monsters

- The full `AddMonster` key vocabulary (26 core + 13 effect-detail keys).
- The legal `role` enum: `offense` / `deffense` (sic) / `bomber` / `support`, plus
  `atk_camp` / `def_camp`. Hard cap of four roles.
- The legal `rank` enum 1–5 and its multipliers.
- The `attr` enum: `Fire` / `Ice` / `Lightning`, with the rock-paper-scissors order.
- `res_prefix` = the monster id (the only art prefix in the pack).
- **No monster in the game has a named special.** No monster key appears in any of
  the 13 tables, and `SKILL_EFFECT_RO` is keyed exclusively by the 113 **card** ids.
  **[INFERRED]** from absence — so an empty `skill_list` cannot mismatch anything.

---

## 6. Korean text — unrecoverable from this LevelDB extract

`CHAR_STR_RO`, `SKILL_REF_RO` etc. carry `KO`/`JA`/`SC`/`TC` columns, but the KO
values in this extract are **mojibake** (raw high bytes, not valid UTF-8 Korean —
e.g. `"����?��1'�?~ �,����"`). The EN columns are intact.

So Korean display names are **[UNKNOWN]** from local data. This is a dump/encoding
defect, not an absence of data — the bytes are there. **[UNKNOWN]** whether another
extraction path would recover them; I did not attempt one. Flagged because it is
cheap for someone with the right tooling and would be a real win for the project.

---

## 7. Explicit `[UNKNOWN]` list

**Per card (all 113):**

1. **base HP / ATK / DEF** — published nowhere, recovered nowhere.
2. **skill numeric magnitudes** — `[value]`, `[value_up]`, `[duration]`. Only the
   formula ships.
3. **gear stat values** — only the category is known (weapon→ATK, armor→DEF,
   accessory→HP).
4. **Korean name / any non-English string.**
5. **stage placement** — except card `051` (`b_00_01`) and card `009`
   (`n_00_01..03`).
6. **rarity / star count** for the 10 costume rows.
7. **role / element / race / gender** for the 10 costume rows (inferable from the
   owner, but not independently sourced for the row itself).
8. **release date** for 84 of 113; **voice actor** for 106 of 113.

**Per monster (all 22):**

9. display name (any language)
10. `attr`, `role`, `rank`, `level`, `overcome` per-id
11. `hp`, `atk`, `def`
12. `crt_chance`, `crt_dmg`, `penetration`, `block_chance`, `block_dec_dmg`,
    `attr_enhance`, `attr_resist`, `hp_page`
13. `skill_list`, `skill_start_time`, `type`, `effect`, `effect_type`
14. **stage / area membership** — i.e. the whole stage→wave→monster mapping
15. which `LEVELING.jet` config maps to which scene

**Global:**

16. Korean strings from the LevelDB (mojibake in this extract).
17. The 12 orphaned `C5xx` art packages' identities.
18. Rank ordering of monster `rank` (1 vs 5 direction) — inferred, not proven.

---

## 8. Contradictions between local and web

**Three, and all three are resolved in favour of local.**

1. **Role vocabulary.** Fandom says *Striker / Defender / Bombardier / Helper*.
   Everything else — `CHAR_STR_RO|SUMMARY` ("The Bomber who…"), namu
   (공격수/수비수/폭격수/도우미, machine-translated to attacker/defender/bombardier/
   helper), and the miraheze wiki (**Bomber / Offense / Defense / Support**) — uses
   a different set. `LEVELING.jet` settles it: the shipped `bonus` block has exactly
   `offense` / `deffense` / `bomber` / `support` and no fifth key.
   **Verdict: Fandom is wrong.** Its four English names do not correspond
   one-to-one — note it has *Defender* where the game has *Defense*, and it lacks
   the Offense/Defense/Bomber/Support distinction entirely. Discard Fandom.

2. **Rage cost vs role.** namu says Bear costs 4 Rage despite being a Defense, and
   that Lily & Lyla (an Offense) also costs 4. My `role × rage` cross-tab found
   exactly **two** exceptions out of 103 — and they are cards `036` (Bear) and
   `047` (Lily & Lyla). **The web was right and my role set was complete.**
   No contradiction; recorded because it is a positive result.

3. **Awakened card art.** The intuitive assumption is `004_1` → `C004_1.jet`.
   **[RECOVERED]** there is no such package for any of the 15 awakened rows, and
   `SKIN.jet` + `CSRSkin::FindWornSkinByCardRefId` (already in `AGENTS.md` §11)
   explain why. **Verdict: local wins**; do not invent `C<n>_1` prefixes. An
   `AGENTS.md` §16.2-style miss would produce an empty resource layer set.

No unresolved contradictions found.

---

## 9. Confidence summary

| claim class | n | confidence |
|---|---|---|
| `CHAR_STR_RO` text (titles, summaries, gear, gear descs, victory) | 113 | **certain** — shipped data |
| 5-slot skill tables + formulas + tags + effect names | 113 | **certain** — shipped data |
| Rage costs | 113 | **certain** — parsed from shipped text |
| `LEVELING.jet` balance data (role/rank/play_time/sp_max/power curve) | — | **certain** — shipped data |
| Stage list `n_01_01`..`n_05_10`, namespace `b_XX_YY` | 50 + ? | **certain** — shipped data |
| Wiki role / element / race / gender / name | 103 | **high** — 6 independent cross-validations |
| Wiki rarity | 103 | **high** — corroborated by chunk 19's 5 rank bands and awakening costs |
| Costume-variant ownership | 10 | **high** — double-confirmed by recovered rage cost |
| Korean strings | 0 | **none** — mojibake |
| Base stats (cards) | 0 | **none** |
| Everything about monsters except art + key vocabulary | 0 | **none** |
| `M001` is a penguin | 1 | **low** — single screenshot |
| Monster `rank` direction (1 = hardest) | — | **moderate** — argued in `INDEX.md` §5.2 |

---

## 10. Recommended next steps, cheapest first

1. **Serve `play_time` from `LEVELING.jet`** (60/90/150/180/300/999/9999) and see
   whether the battle timer moves. Resolves an `AGENTS.md` §16.6 `[UNKNOWN]` in one
   experiment.
2. **Publish the 339 recovered `*_DESC` strings** in `/reference/GetCard`'s
   `equipment[]`. Free real content, zero invention.
3. **Test whether the 8 non-card `CHAR_STR_RO` rows are what cause the five masked
   `SRCard.cpp(731)` assertions** (`AGENTS.md` §16.6 item 2). One-line change.
4. **Set awakened `res_prefix` to the base card id.** Prevents an empty-layer crash.
5. **Add the `b_XX_YY` stage list** and the `b_00_01 → card 051` whitelist.
6. **Re-run the whole catalogue against a Korean-language extraction** of the
   LevelDB if someone can fix the mojibake — that is where the remaining
   [COMMUNITY-SOURCED] fields could become [RECOVERED].
7. **OCR the FAQ's stat screenshots.** `Image A` is a fully-invested Beckhen stat
   page and `Image A.b` is the sub-stat breakdown. Those are the only real numbers
   in the entire offline corpus and I did not read them off the images.

---

## 11. Stats hunt round 2 — follow-up agent, 2026-10-03

**Agent:** stat-hunting agent. **Full write-up: `analysis/catalogue/stats/README.md`.**
This section corrects §7 of the above: step 7 was the right call and it **paid off**.

### The reason round 1 got zero from the FAQ

Not an absence of data — **a parsing bug**. The FAQ stores its 27 screenshots as
*reference-style* markdown: `![][imageN]` with the data URIs in
`[imageN]: <data:image/png;base64,…>` definitions at the **end** of the file. An
inline `!\[…\]\(data:image/…\)` regex matches **0 of 27**. With the correct pattern,
**6 of the 27 are stat screens.** Round 1's judgement ("not machine-readable") was
right about the obstacle and wrong about the conclusion.

### What was recovered

| | cards | monsters |
|---|---|---|
| with any numeric stat | **3 / 121** | **0 / 22** |
| with a complete stat line | **1** (`051`, 13 stats, Lv.30) | **0** |

- **`051` Beckhen** — full 13-stat line at **Lv.30**, plus the exact equipment
  delta. Identity proven by an exact 4-way string match against `CHAR_STR_RO|051`
  (`Guardian of Fight Club` / `Chicken Feet` / `Chicken Wings` / `Jack`, all four
  visible on the screenshots). White column = nude card, green = gear, proven by
  `24068 + 6291 = 30359` matching the card page exactly, and by 11 of 12 jewel
  sub-stats summing to their green totals. [`stats/051.md`]
- **`010_1` Vincent (Awakened)** — Strength 61815, HP 4980, ATK 2634, DEF 1992 at
  Lv.30. [`stats/010_1.md`]
- **`010` Vincent** — armour "Purple Combat Coat" DEF 101 @Lv49 → 102 @Lv50, and
  the Strength delta +19. [`stats/010.md`]
- **The equipment system** — previously listed as wholly `[UNKNOWN]` in §7 item 3.
  Weapon ATK **134**, armour DEF **102**, accessory Max HP **260** at Lv.50; six
  jewel main+sub stat sets at Lv.15; 12 jewel set bonuses (including Offensive Jewel); upgrade cost 50000.
  [`stats/GEAR.md`]

### Corrections to §7 and §9 of this report

- §7 item 1 ("base HP/ATK/DEF — published nowhere, recovered nowhere") is now
  **wrong for 2 cards**. It was right that nothing *publishes* them; it was wrong
  that nothing *recovers* them — they were in a local file all along, as pixels.
- §7 item 3 ("gear stat values — only the category is known") is now **wrong**.
  Values are recovered at level cap. §7.2's `[INFERRED-FIXTURE]` per-piece growth
  guess can be replaced with a real anchor at Lv.50.
- §9's "Base stats (cards) | 0 | none" → **2 cards, high confidence**.

### Two traps the follow-up hit, worth recording

1. **OCR produced a wrong number that a human read would not.** Tesseract read
   card `010_1`'s Strength as `671815`; the screen says **61815**. Every figure in
   `stats/` was therefore also read by eye at 2–5x zoom, and OCR was used only to
   triage. The same happened on `051`: `33.00` → `"e .00"`. **An OCR'd number
   without visual confirmation is worse than no number**, exactly as suspected.
2. **Batched image reads render out of order.** Two `read` calls in one block came
   back with the second image's content attached to the first filename. That
   produced one real misattribution mid-run (`image7`/`image8` were swapped) before
   it was caught. **Read images one per call, or the filenames lie.**

### Why monsters are still zero — now a fact, not a gap

The one unchecked vector was monster HP on the combat screen. It exists, but it is
a **transient mid-fight value with no monster id, no level and no maximum**, so it
cannot populate `/reference/GetMonster`. No screen in this game shows a monster's
base stats, which is consistent with §5: monster data was server-authoritative and
never shipped in the APK.

**Monsters are unrecoverable in principle from any public source.** Only a captured
original-server response would yield them and there is none. §5's verdict stands and
is now stronger: do not re-run this sweep expecting a different answer.

### Also exhausted, confirmed this round

- **miraheze wiki images: zero.** All 881 images enumerated; 96 `Portrait_*`,
  96 `Icon_*`, 689 emotion sprites. A regex for
  `stat|table|tier|chart|graph|power|level|balance|screen|data` over every filename
  returns **0 hits**. The wiki publishes no stat graphics.
- **YouTube: zero, 4 videos, ~1,400 frames OCR'd.** `qtXrVbFQ9fA` (434),
  `pXWN5m0yqOo` (322), `i1YTS0KL8Ps` (121), `cnMBlXFd5W4` (537). All gameplay,
  recruiting or combat; none shows a card detail page. Note the search-space
  problem: "blustone" is swamped by *Bluestone* (LoL item, Minecraft, Dokkan,
  Smite) and `블루스톤 능력치` returns Solo Leveling and Bloodborne.
- **§5's per-monster `[UNKNOWN]` list stands in full.**
