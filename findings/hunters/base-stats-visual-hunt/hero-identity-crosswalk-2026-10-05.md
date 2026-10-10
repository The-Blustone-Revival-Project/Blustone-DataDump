# Hero identity crosswalk — the 113 catalog heroes (2026-10-05)

**Purpose.** One consolidated per-hero identity table for every real catalog hero,
with an explicit **IDENTITY CONFIDENCE** grade per hero, the sources that attest
it, and the Episode STAT rank/level context where one exists.

**Section discipline.** §1 is **PURE**: identity only (which id is which hero,
what role, what element, what rarity, who attests it). §2 is **UNPURE**: every
numeric token, quarantined and labelled. Nothing in §2 may be promoted to §1 or
to strict coverage.

**Coverage effect: NONE.** Strict coverage stays **heroes 1/113, accessories
1/100, monsters 0/22**. This file closes *identity*, not *base stats*. The
coverage rule in `coverage.md` is untouched.

**Read-only.** No fixture, server file, seed, state file, APK or emulator was
touched. No `polluted-observations.md` append was made — the parent mirrors that
lane.

**Supersedes nothing.** `hero-stat-divergence-2026-10-05.md` §3a and
`episode-stat-adjudication-2026-10-05.md` remain the sources for *magnitude*
priors; this file is the identity layer they lean on.

---

# 0. Sources, and exactly what each one can attest

| Tag | Source | Kind | What it can attest | What it cannot |
|---|---|---|---|---|
| **ARCHIVE** | `archived-hunter-database-2019.tsv` — Wayback captures of `blustone.jp/hunter/` , 63 rows, 2019-10-15 … 2019-12-16 | third-party (JP official site, archived) | JP listed name + JP title, **role**, **element**, **draw rarity**, capture timestamp; 13 numeric fields for 62 of the 63 | EN name, level, gear state, any 2.8.0.1 state |
| **EPISODE** | `analysis/recovered-reference/EPISODE_STAT_ACTORS.json` + `EPISODE_COMBAT_*.json` (exported from shipped `R_EPISODE.jet`, SHA `7f4362cd…`, manifest `EPISODE_COMBAT_STAT.manifest.json`) | **[RECOVERED] shipped game data** | `ref_id` → catalog hero id, `res_id` art pack, **native `role` enum**, **native `attr` enum**, `stat.rank`, per-occurrence thumb `{level, rank, hyper, attr}` | ordinary hunter base stats (manifest says so verbatim), gear state, draw rarity |
| **MANIFEST** | `analysis/recovered-reference/manifest.json`; `char-str.tsv` (121 TITLE rows), `skill-ref.tsv` (113 ids), `skill-tag.tsv` (113 ids × 5 slots), art-pack inventory in `split_PADResource/assets` | **[RECOVERED] shipped game data** | that the id **exists** as a card, its shipped EN `TITLE`, exactly 5 skill slots, and whether a `C0nn.jet` art pack is on disk | name, role, element, rarity (none of those are in the shipped string tables) |
| **CATALOGUE** | `analysis/catalogue/data/card-catalogue.tsv` (121 rows) / `cards.json`; `catalogue/INDEX.md` §2 | **community** (wiki InfoboxCharacter) | EN name, EN title, draw rarity, role, element, race, gender, weapon/armor/accessory names, variant owner | anything about 2.8.0.1 shipped data |
| **RELDATE** | `cards.json` `released` field, 29 of 113 populated | **community** (wiki release date) | that a dated release existed → an **era anchor**, and an independent existence attestation | role, element, rarity, stats |

### 0.1 Confidence rubric (stated once)

Identity means the binding **id → (name, title, role, element, rarity)**.

Only the three **discriminating** sources are counted, because MANIFEST attests
every one of the 113 identically and therefore never discriminates, and RELDATE
attests existence but not the binding:

| Grade | Rule |
|---|---|
| **CONFIRMED** | ≥2 of {ARCHIVE, EPISODE, CATALOGUE} supply the binding, and they do not contradict each other on role or element |
| **SINGLE-SOURCE** | exactly 1 discriminating source supplies the binding |
| **UNRESOLVED** | no discriminating source supplies role/element/rarity (catalogue blank **and** no archive row **and** no Episode row) |

### 0.2 Source-set arithmetic, reconciled

The counts that matter, all re-derived from disk this pass:

| Quantity | Count |
|---|---:|
| Catalogue rows | 121 |
| − 8 non-card rows (`901`–`904`, `912`–`914`, `x914`) | **113 real heroes** |
| ARCHIVE rows | 63 (62 numeric + `056`, whose core stats are `???`) |
| ARCHIVE numeric rows | 62 |
| EPISODE hero rows | 117 |
| EPISODE distinct hero ids | **55** |
| EPISODE distinct hero `res_id` art packs | 64 (12 are `A`/`B` costume variants + `C509`/`C510`) |
| ARCHIVE ∩ EPISODE | 44 (45 if `056` counts, which has an identity but no numbers) |
| **ARCHIVE ∪ EPISODE** | **73** |
| Real heroes in **neither** | **40** |
| MANIFEST attestations (CHAR_STR title + 5 skill slots + art) | 113 / 113 titles, 113 / 113 skill ids, 98 / 113 art packs (the 15 `_1` rows ship no art by design — `catalogue/INDEX.md` §2.3) |
| RELDATE attestations | 29 |

**Grades: CONFIRMED 71 · SINGLE-SOURCE 35 · UNRESOLVED 7.**

### 0.3 Three counts that must not be conflated

1. **ARCHIVE identity rows (63) vs ARCHIVE numeric rows (62).** `056` has an
   archive *identity* row (JP name `贖罪の「ジェノビア」`, Offense, Ice, ★4) whose
   13 stat fields are `???`. It is therefore archive-attested for **who it is**
   and archive-unattested for **what it measures**.
2. **Episode STAT `stat.rank` is not draw rarity.** 40 of the 55 Episode heroes
   sit at `stat.rank = 5`, including `059` and `060` whose archive draw rarity is
   unambiguously ★3. Episode rank is a scripted-story rank and must never be
   written into a rarity column.
3. **Catalogue `rarity` and ARCHIVE `rarity_on_draw` agree 61/61** on the 61 rows
   where the catalogue is populated. The two disagreements found are `026` and
   `034`, and in both cases the catalogue cell is **blank** and the archive fills
   it — see §1.5.

---

# 1. PURE — consolidated per-hero identity table

## 1.1 The 113 rows

`Src` = discriminating sources (`C`at-alogue, `A`rchive, `E`pisode). `Ep rows` =
Episode STAT rows for that id. `Ep context` = `res_id` @ shipped COMBAT thumb
**level** / `stat.rank`, one entry per row. `⚠` marks a row where Episode's
native enum contradicts the catalogue.

| id | Name | Title | Role | Elem | ★ | Src | Grade | Ep rows | Ep context | ⚠ |
|---|---|---|---|---|---|---|---|---:|---|---|
| `001` | Lantern | First Ever Hunter | Bomber | Fire | 3 | CAE | CONFIRMED | 2 | C001 L1/r4; C001 L30/r5 | |
| `002` | Mowgli | Forgotten Forest | Offense | Lightning | 2 | CA | CONFIRMED | 0 | — | |
| `003` | Nene | Walking Disaster | Defense | Ice | 3 | CAE | CONFIRMED | 3 | C003 L1/r4; C003 L1/r3; C003 L30/r5 | |
| `004` | Tyltyl | World's Best Cook | Support | Fire | 1 | CAE | CONFIRMED | 2 | C004 L30/r5; C004 L1/r5 | |
| `004_1` | Tyltyl (Awakened) | Legendary Chef | Support | Fire | 5 | C | SINGLE-SOURCE | 0 | — | |
| `005` | Gerard | Invincible One | Defense | Ice | 2 | CAE | CONFIRMED | 4 | C005 L1/r2; C005 L1/r2; C005 L1/r4; C005 L1/r5 | ep role≠cat |
| `005_1` | Gerard (Awakened) | Indomitable Warrior | Defense | Ice | 5 | C | SINGLE-SOURCE | 0 | — | |
| `006` | Sylvester | Undying Soldier | Offense | Fire | 1 | CAE | CONFIRMED | 1 | C006 L1/r5 | |
| `007` | Metis | Fiery Soul | Bomber | Fire | 1 | CAE | CONFIRMED | 1 | C007 L20/r4 | |
| `008` | Akasha | Maiden of Gods | Support | Lightning | 3 | CAE | CONFIRMED | 2 | C008 L1/r5; C008B L1/r5 | |
| `009` | Captain | Captain | Defense | Lightning | 1 | CAE | CONFIRMED | 9 | C009 L1/r1 ×2; C009 L15/r2; C009 L1/r5; C009 L30/r5 ×2; C509 L30/r5 ×2; C009 L1/r5 | ep elem≠cat |
| `009_1` | Captain (Awakened) | Eternal Flame | Defense | Fire | 5 | C | SINGLE-SOURCE | 0 | — | |
| `010` | Vincent | Renegade | Offense | Lightning | 4 | CAE | CONFIRMED | 9 | C010 L1/r4 ×4; C010 L30/r5; C010 L1/r5; C010 L30/r5; C510 L30/r5 ×2 | ep elem≠cat |
| `010_1` | Vincent (Awakened) | Despair of a Millennium | Offense | Ice | 5 | C | SINGLE-SOURCE | 0 | — | |
| `011` | Hecate | Protector | Defense | Fire | 1 | CAE | CONFIRMED | 3 | C011 L20/r4; C011 L30/r5; C011 L1/r5 | |
| `011_1` | Hecate (Awakened) | Counterattack Flame | Defense | Fire | 5 | C | SINGLE-SOURCE | 0 | — | |
| `012` | Karl Steiner | Immortal One | Offense | Lightning | 3 | CAE | CONFIRMED | 5 | C012 L10/r4; C012 L1/r4 ×2; C012 L20/r5; C012 L1/r5 | |
| `013` | Denali | Clean Fairy | Support | Fire | 2 | CAE | CONFIRMED | 2 | C013 L30/r3; C013 L1/r5 | |
| `014` | Locke | Locke and Cash CEO | Bomber | Ice | 1 | CAE | CONFIRMED | 2 | C014 L20/r5; C014 L30/r5 | |
| `015` | Levi | Lieutenant | Bomber | Ice | 2 | CA | CONFIRMED | 0 | — | |
| `016` | Bruce Bang | Death Metal Preacher | Support | Ice | 1 | CAE | CONFIRMED | 2 | C016 L20/r4; C016 L1/r5 | |
| `017` | Lapis | Speedy Swordsman | Offense | Ice | 1 | CAE | CONFIRMED | 3 | C017 L1/r4; C017 L1/r5 ×2 | |
| `017_1` | Lapis (Awakened) | Supersonic Swordsman | Offense | Ice | 5 | C | SINGLE-SOURCE | 0 | — | |
| `018` | Robin | King of Survival | Defense | Ice | 1 | CAE | CONFIRMED | 2 | C018 L20/r4; C018 L1/r5 | |
| `019` | Balian | Wandering Swordsman | Offense | Lightning | 1 | CAE | CONFIRMED | 2 | C019 L1/r5; C019 L1/r5 | |
| `019_1` | Balian (Awakened) | Thunderbringer | Offense | Lightning | 5 | C | SINGLE-SOURCE | 0 | — | |
| `020` | Sienna | Firepower Maniac | Bomber | Lightning | 1 | CAE | CONFIRMED | 1 | C020 L10/r5 | |
| `020_1` | Sienna (Awakened) | Railgun Shooter | Bomber | Lightning | 5 | C | SINGLE-SOURCE | 0 | — | |
| `021` | Rebecca | Twilight Bat Clan | Offense | Fire | 2 | CAE | CONFIRMED | 2 | C021 L1/r4; C021 L20/r5 | |
| `021_1` | Rebecca (Awakened) | Raging Flames of Iron | Offense | Fire | 5 | C | SINGLE-SOURCE | 0 | — | |
| `022` | Sunny | Experiment 2 | Support | Ice | 2 | CA | CONFIRMED | 0 | — | |
| `023` | Hermes | Elite Messenger | Offense | Fire | 3 | CAE | CONFIRMED | 2 | C023 L30/r5; C023 L1/r5 | |
| `024` | Riko | Hard-Knock Life | Defense | Lightning | 2 | CAE | CONFIRMED | 1 | C024 L20/r5 | |
| `024_1` | Riko (Awakened) | Sparkling Blade Claws | Defense | Lightning | 5 | C | SINGLE-SOURCE | 0 | — | |
| `025` | Teddy Bomber | Teddy Bear Terrorist | Bomber | Fire | 2 | CA | CONFIRMED | 0 | — | |
| `026` | **???** | In Wonderland | Support\* | Lightning\* | 1\* | **A** | SINGLE-SOURCE | 0 | — | |
| `026_1` | **???** | In Wonderland | ? | ? | ? | — | **UNRESOLVED** | 0 | — | |
| `027` | Athena | Flame of Battlefield | Defense | Fire | 3 | CAE | CONFIRMED | 1 | C027B L1/r5 | |
| `028` | Octavia | Frost Witch | Offense | Ice | 3 | CAE | CONFIRMED | 2 | C028 L30/r5; C028B L1/r5 | |
| `029` | Kain | Steely Bodyguard | Defense | Lightning | 3 | CAE | CONFIRMED | 2 | C029A L1/r5; C029A L30/r5 | |
| `030` | Acerola | Biologist | Support | Lightning | 2 | CAE | CONFIRMED | 1 | C030 L20/r5 | |
| `031` | Diana | Thunder Arrow | Bomber | Lightning | 3 | CA | CONFIRMED | 0 | — | |
| `032` | Scar | Wandering Fighter | Offense | Ice | 2 | CAE | CONFIRMED | 1 | C032 L1/r5 | |
| `033` | Patrone | Silent Canine | Bomber | Ice | 3 | CA | CONFIRMED | 0 | — | |
| `034` | **???** | Halloween Witch | Defense\* | Ice\* | 2\* | **AE** | **CONFIRMED** | 1 | C034 L1/r5 | |
| `034_1` | **???** | Halloween Witch | ? | ? | ? | — | **UNRESOLVED** | 0 | — | |
| `035` | Joy | Walking Infirmary | Support | Fire | 3 | CA | CONFIRMED | 0 | — | |
| `036` | Bear | Nature's Gift | Defense | Lightning | 3 | CAE | CONFIRMED | 5 | C036 L1/r3; C036 L10/r4; C036 L10/r5; C036B L1/r5; C036 L1/r5 | |
| `037` | Natalia | Noble Spear | Offense | Ice | 3 | CA | CONFIRMED | 0 | — | |
| `038` | Rebecca (Christmas) | Santa Girl | Offense | Fire | 3 | CAE | CONFIRMED | 1 | C038 L30/r5 | |
| `038_1` | **???** | Twilight Santa Girl | ? | ? | ? | — | **UNRESOLVED** | 0 | — | |
| `039` | Gullveig | Airport Officer | Bomber | Lightning | 3 | CAE | CONFIRMED | 2 | C039 L20/r5; C039 L1/r5 | |
| `040` | Bibi | Wolf Child | Offense | Lightning | 3 | CAE | CONFIRMED | 3 | C040 L10/r5 ×2; C040 L1/r5 | |
| `041` | Edward | Robot Engineer | Defense | Lightning | 3 | CAE | CONFIRMED | 2 | C041 L10/r5; C041 L30/r5 | |
| `042` | Santa Clauster | Santa Clauster | Offense | Fire | 3 | CAE | CONFIRMED | 1 | C042 L30/r5 | |
| `043` | Papillon | Notorious Jail-breaker | Defense | Ice | 3 | CAE | CONFIRMED | 1 | C043 L30/r5 | |
| `044` | Heidi | Girl with Two Faces | Offense | Fire | 3 | CA | CONFIRMED | 0 | — | |
| `045` | Yuri | Ice Skating Fairy | Offense | Ice | 3 | CA | CONFIRMED | 0 | — | |
| `046` | Harley | Man of Justice | Defense | Ice | 4 | CAE | CONFIRMED | 1 | C046 L1/r5 | |
| `047` | Lily & Lyla | Strange Twins | Offense | Fire | 4 | CA | CONFIRMED | 0 | — | |
| `048` | Dumble | Strange Old Man | Defense | Ice | 3 | CA | CONFIRMED | 0 | — | |
| `049` | Bright | Little Match Boy | Support | Fire | 3 | CAE | CONFIRMED | 3 | C049 L1/r3 ×2; C049B L1/r5 | |
| `050` | Therapy | Diabolic Physiotherapist | Support | Ice | 3 | CA | CONFIRMED | 0 | — | |
| `051` | Beckhen | Guardian of Fight Club | Offense | Ice | 3 | CAE | CONFIRMED | 2 | C051 L1/r5; C051A L1/r5 | |
| `052` | Windblade | Windy Soul | Offense | Lightning | 4 | CAE | CONFIRMED | 1 | C052 L10/r5 | |
| `053` | Calibur | Revenant | Defense | Fire | 3 | CA | CONFIRMED | 0 | — | |
| `054` | Dino | Genius Climatologist | Bomber | Ice | 3 | CAE | CONFIRMED | 4 | C054 L10/r5; C054 L1/r5 ×2; C054 L30/r5 | |
| `055` | Apollon | Singing Poet | Bomber | Fire | 3 | CAE | CONFIRMED | 1 | C055B L1/r5 | |
| `056` | Genovia | Atoner | Offense | Ice | 4 | CAE | **CONFIRMED** | 3 | C056 L10/r5; C056 L1/r5; C056 L30/r5 | |
| `056_1` | Genovia (Awakened) | Condemner | Offense | Ice | 5 | C | SINGLE-SOURCE | 0 | — | |
| `057` | Pansy | Animal Lover | Support | Ice | 3 | CAE | CONFIRMED | 2 | C057 L10/r5; C057 L1/r5 | |
| `058` | Crocus | Necromancer | Support | Lightning | 3 | CAE | CONFIRMED | 1 | C058B L1/r5 | |
| `059` | Lantern (Halloween) | Jack O' Lantern | Bomber | Fire | 3 | CAE | CONFIRMED | 1 | C059 L1/r5 | ep elem≠cat, ≠arch |
| `060` | Denali (Halloween) | Broom Witch | Support | Fire | 3 | CAE | CONFIRMED | 1 | C060 L1/r5 | |
| `061` | Chichi | Girl with Super Strength | Offense | Lightning | 3 | CA | CONFIRMED | 0 | — | |
| `062` | Juno | Aircraft Mechanic | Defense | Fire | 3 | CA | CONFIRMED | 0 | — | |
| `063` | Erise | Prestigious Tailor | Defense | Lightning | 4 | CA | CONFIRMED | 0 | — | |
| `064` | Geranium | Artifact Collector | Bomber | Lightning | 4 | **CE** | **CONFIRMED** | 2 | C064 L1/r5; C064 L30/r5 | |
| `065` | Teresa | Runaway Bride | Support | Fire | 4 | C | SINGLE-SOURCE | 0 | — | |
| `066` | Mary | Little Reaper | Offense | Fire | 4 | C | SINGLE-SOURCE | 0 | — | |
| `067` | Judith | Red Shadow | Bomber | Fire | 4 | C | SINGLE-SOURCE | 0 | — | |
| `068` | Selene | White Darkness | Bomber | Ice | 4 | **CE** | **CONFIRMED** | 3 | C068 L1/r5; C068 L30/r5; C068A L1/r5 | |
| `069` | Celine | Diva of Midgard | Support | Ice | 4 | **CE** | **CONFIRMED** | 1 | C069A L30/r5 | |
| `070` | Alia | Electrotherapist | Support | Lightning | 4 | **CE** | **CONFIRMED** | 1 | C070 L1/r5 | |
| `071` | Anemone | Great General | Defense | Fire | 4 | **CE** | CONFIRMED | 1 | C071 L1/r5 | **ep role≠cat** |
| `072` | Audrey | Dangerous Gambler | Bomber | Lightning | 4 | **CE** | **CONFIRMED** | 2 | C072A L1/r5; C072 L1/r5 | |
| `073` | Sofia | Fantastic Light | Support | Fire | 4 | C | SINGLE-SOURCE | 0 | — | |
| `074` | Leon | Veteran Army Surgeon | Support | Ice | 4 | C | SINGLE-SOURCE | 0 | — | |
| `075` | Bella | Dancing Sword | Offense | Ice | 4 | C | SINGLE-SOURCE | 0 | — | |
| `076` | Junia | Prayer | Defense | Ice | 4 | C | SINGLE-SOURCE | 0 | — | |
| `077` | Blondie | Gunslinger | Bomber | Fire | 4 | C | SINGLE-SOURCE | 0 | — | |
| `078` | Teresa (Halloween) | Ghost Bride | Support | Ice | 4 | **CE** | **CONFIRMED** | 1 | C078 L30/r5 | |
| `079` | Lawrence | Defense Knight | Defense | Fire | 4 | C | SINGLE-SOURCE | 0 | — | |
| `080` | Westfield | Legendary Coach | Support | Lightning | 4 | **CE** | **CONFIRMED** | 1 | C080 L1/r5 | |
| `081` | Monica | Master of Counterattack | Defense | Lightning | 4 | C | SINGLE-SOURCE | 0 | — | |
| `082` | Mary (Christmas) | Little Santa | Offense | Lightning | 4 | **CE** | **CONFIRMED** | 1 | C082 L30/r5 | |
| `083` | Kamala | Leader of the White Forest | Defense | Ice | 4 | C | SINGLE-SOURCE | 0 | — | |
| `084` | Lottery Mouse | Master of Recruitment | Bomber | Ice | 4 | C | SINGLE-SOURCE | 0 | — | |
| `085` | **???** | Lunar New Year | Support\* | Fire\* | ?\* | **E** | SINGLE-SOURCE | 1 | C085 L1/r5 | ⚠ see §1.7 |
| `086` | Genovia (Valentine) | Valentine | Offense | Fire | 4 | C | SINGLE-SOURCE | 0 | — | |
| `086_1` | **???** | Valentine Condemner | ? | ? | ? | — | **UNRESOLVED** | 0 | — | |
| `087` | **???** | Florist Lady | ? | ? | ? | — | **UNRESOLVED** | 0 | — | |
| `088` | **???** | Florist | ? | ? | ? | — | **UNRESOLVED** | 0 | — | |
| `089` | Clara | Post Office Supervisor | Support | Lightning | 4 | C | SINGLE-SOURCE | 0 | — | |
| `090` | Katrina | Owner of Saw Blade | Offense | Lightning | 4 | C | SINGLE-SOURCE | 0 | — | |
| `091` | Anemone (Kid) | Little General | Defense | Lightning | 4 | C | SINGLE-SOURCE | 0 | — | |
| `092` | Themis | Monster Sniper | Bomber | Fire | 4 | C | SINGLE-SOURCE | 0 | — | |
| `093` | Bella (Summer) | Midsummer Sword Dancer | Offense | Fire | 4 | C | SINGLE-SOURCE | 0 | — | |
| `094` | Leon (Summer) | Lifeguard | Support | Lightning | 4 | C | SINGLE-SOURCE | 0 | — | |
| `095` | **???** | Knight of Swimming Pool | ? | ? | ? | — | **UNRESOLVED** | 0 | — | |
| `096` | Estelle | Midgard’s Finest Sword | Offense | Fire | 4 | C | SINGLE-SOURCE | 0 | — | |
| `097` | Lily & Lyla (Christmas) | Santa Twins | Offense | Lightning | 4 | C | SINGLE-SOURCE | 0 | — | |
| `098` | Selene (Valentine) | Valentine | Bomber | Lightning | 4 | C | SINGLE-SOURCE | 0 | — | |

`\*` = value supplied **only** by the source named in `Src`, filling a catalogue
cell that is blank upstream. See §1.5.

Grade distribution by source combination:

| Combination | n | Grade |
|---|---:|---|
| ARCHIVE + CATALOGUE + EPISODE | 44 | CONFIRMED |
| ARCHIVE + CATALOGUE | 17 | CONFIRMED |
| CATALOGUE + EPISODE | 9 | CONFIRMED |
| ARCHIVE + EPISODE (`034` only) | 1 | CONFIRMED |
| CATALOGUE only | 33 | SINGLE-SOURCE |
| ARCHIVE only (`026`) | 1 | SINGLE-SOURCE |
| EPISODE only (`085`) | 1 | SINGLE-SOURCE |
| none | 7 | UNRESOLVED |

## 1.2 Archive-side identity ledger (63 rows)

JP listed name, role, element, draw rarity, and whether the row carries the 13
numeric fields. Capture timestamps cluster at 2019-10-15 (31 rows) and
2019-11-13 … 2019-12-16 (32 rows).

| id | JP listed name | Role | Elem | Draw ★ | Numeric? | Capture |
|---|---|---|---|---:|---|---|
| `001` | 世界初のハンター「ランターン」 | Bomber | Fire | 3 | yes | 2019-12-09 |
| `002` | 消えた森の「モーグリ」 | Offense | Lightning | 2 | yes | 2019-12-08 |
| `003` | 伝説の厄介者「ネネ」 | Defense | Ice | 3 | yes | 2019-12-10 |
| `004` | 最高のシェフ「チルチル」 | Support | Fire | 1 | yes | 2019-12-09 |
| `005` | 不屈の「ジェラード」 | Defense | Ice | 2 | yes | 2019-12-10 |
| `006` | 消えぬ老兵「シルベスター」 | Offense | Fire | 1 | yes | 2019-10-15 |
| `007` | 今日もホットな「メティス」 | Bomber | Fire | 1 | yes | 2019-10-15 |
| `008` | 神木の巫女「アーカーシャ」 | Support | Lightning | 3 | yes | 2019-10-15 |
| `009` | キャプテン「主人公」 | Defense | Lightning | 1 | yes | 2019-10-15 |
| `010` | 裏切り者「ビンセント」 | Offense | Lightning | 4 | yes | 2019-10-15 |
| `011` | 守護神「ヘカテ」 | Defense | Fire | 1 | yes | 2019-10-15 |
| `012` | 不滅の「カルシュタイナー」 | Offense | Lightning | 3 | yes | 2019-10-15 |
| `013` | 清潔フェアリー「テナリ」 | Support | Fire | 2 | yes | 2019-12-11 |
| `014` | ロック＆キャッシュCEO「ロック」 | Bomber | Ice | 1 | yes | 2019-10-15 |
| `015` | 中尉「レヴィ」 | Bomber | Ice | 2 | yes | 2019-12-08 |
| `016` | デスメタルの伝道師「ブルース・バン」 | Support | Ice | 1 | yes | 2019-12-16 |
| `017` | 快速の剣術士「ラピス」 | Offense | Ice | 1 | yes | 2019-10-15 |
| `018` | 生存術の覇者「ロビン」 | Defense | Ice | 1 | yes | 2019-12-11 |
| `019` | さすらいの剣客「バリアン」 | Offense | Lightning | 1 | yes | 2019-10-15 |
| `020` | 火力オタク「シエナ」 | Bomber | Lightning | 1 | yes | 2019-12-08 |
| `021` | 黄昏のバット団「レベッカ」 | Offense | Fire | 2 | yes | 2019-10-15 |
| `022` | 実験体 2号「ヘソン」 | Support | Ice | 2 | yes | 2019-10-15 |
| `023` | 特級伝令使「ヘルメス」 | Offense | Fire | 3 | yes | 2019-12-10 |
| `024` | 波乱万丈「リコ」 | Defense | Lightning | 2 | yes | 2019-10-15 |
| `025` | テディベアテロリスト「テディボマー」 | Bomber | Fire | 2 | yes | 2019-12-11 |
| `026` | 不思議の国の「チルチル」 | Support | Lightning | 1 | yes | 2019-12-10 |
| `027` | 戦場の火花「アテナ」 | Defense | Fire | 3 | yes | 2019-12-09 |
| `028` | 極寒の魔女「オクタピア」 | Offense | Ice | 3 | yes | 2019-10-15 |
| `029` | 鋼のボディガード「カイン」 | Defense | Lightning | 3 | yes | 2019-10-15 |
| `030` | 植物学者「アセロラ」 | Support | Lightning | 2 | yes | 2019-12-08 |
| `031` | 雷矢少女「ディアナ」 | Bomber | Lightning | 3 | yes | 2019-12-09 |
| `032` | 放浪の格闘家「スカー」 | Offense | Ice | 2 | yes | 2019-12-16 |
| `033` | 静寂な牙「パトローネ」 | Bomber | Ice | 3 | yes | 2019-12-08 |
| `034` | ハロウィン魔女「ハロウィンリコ」 | Defense | Ice | 2 | yes | 2019-10-15 |
| `035` | 往診治療室「ジョイ」 | Support | Fire | 3 | yes | 2019-11-15 |
| `036` | 大自然の贈り物「クマ」 | Defense | Lightning | 3 | yes | 2019-10-15 |
| `037` | 高貴な槍「ナタリア」 | Offense | Ice | 3 | yes | 2019-10-15 |
| `038` | サンタガール「サンタギャルレベッカ」 | Offense | Fire | 3 | yes | 2019-12-11 |
| `039` | 飛行場管理人「グルヴェイグ」 | Bomber | Lightning | 3 | yes | 2019-10-15 |
| `040` | オオカミ少女「ビビ」 | Offense | Lightning | 3 | yes | 2019-12-11 |
| `041` | ロボット工学者「エドワード」 | Defense | Lightning | 3 | yes | 2019-10-15 |
| `042` | 悪ガキ狩り「サンタクロースター」 | Offense | Fire | 3 | yes | 2019-12-16 |
| `043` | 稀少な脱獄囚「パピヨン」 | Defense | Ice | 3 | yes | 2019-10-15 |
| `044` | 2つの顔を持つ少女「ハイディ」 | Offense | Fire | 3 | yes | 2019-12-11 |
| `045` | 銀盤の妖精「ユリ」 | Offense | Ice | 3 | yes | 2019-10-15 |
| `046` | 正義のヒーロー「ハリー」 | Defense | Ice | 4 | yes | 2019-10-15 |
| `047` | 正体不明のツインズ「リリー＆ララー」 | Offense | Fire | 4 | yes | 2019-10-15 |
| `048` | 奇妙な老人「ダンブル」 | Defense | Ice | 3 | yes | 2019-12-16 |
| `049` | マッチ売りの少年「ブライト」 | Support | Fire | 3 | yes | 2019-10-15 |
| `050` | 魔性の理学療法士「テラピー」 | Support | Ice | 3 | yes | 2019-10-15 |
| `051` | ファイトクラブの守護者「ベッケン」 | Offense | Ice | 3 | yes | 2019-12-16 |
| `052` | 風のような魂「ストーム」 | Offense | Lightning | 4 | yes | 2019-10-15 |
| `053` | 鋼鉄のレヴェナント「カリバー」 | Defense | Fire | 3 | yes | 2019-12-08 |
| `054` | 天才気象学者「ディノ」 | Bomber | Ice | 3 | yes | 2019-10-15 |
| `055` | 吟遊詩人兼音楽家「アポロン」 | Bomber | Fire | 3 | yes | 2019-12-09 |
| `056` | 贖罪の「ジェノビア」 | Offense | Ice | 4 | **no (`???`)** | 2019-10-15 |
| `057` | 動物愛好家「パンジー」 | Support | Ice | 3 | yes | 2019-12-09 |
| `058` | ネクロマンサー「クロッカス」 | Support | Lightning | 3 | yes | 2019-11-15 |
| `059` | ジャック・オ・ランタン「ハロウィンランターン」 | Bomber | Fire | 3 | yes | 2019-12-16 |
| `060` | ほうき魔女「ハロウィンテナリ」 | Support | Fire | 3 | yes | 2019-12-08 |
| `061` | 怪力の少女「チチ」 | Offense | Lightning | 3 | yes | 2019-12-11 |
| `062` | 航空整備士「ジュノ」 | Defense | Fire | 3 | yes | 2019-10-15 |
| `063` | 一流仕立て屋「エリーズ」 | Defense | Lightning | 4 | yes | 2019-10-15 |

## 1.3 The 11 Episode-only heroes — and what their STAT rows actually say

**Definition used here.** "Episode-only" = present in the Episode STAT table but
with **no numeric row in the 2019 archive**. That set is 11 ids. Note the
distinction from §0.3 item 1: of those 11, **`056` does have an archive identity
row** (its numbers are `???`), so only **10** are absent from the archive
altogether. `hero-stat-divergence-2026-10-05.md` §3a's "11 absent from S1" is
counting S1 as the 62 *numeric* rows and is right to do so; this file states both
numbers so the two cannot be confused.

Every one of the 11 is a member of the **51-id `uncovered-archive-roster-2019.tsv`**
— see §1.4. Their Episode STAT rows, in full:

| id | Name | Episode `res_id` | Ep `role` | Ep `attr` | Ep `stat.rank` | COMBAT thumb level / rank / hyper | Archive status |
|---|---|---|---|---:|---|---|---|
| `056` | Genovia — Atoner | `C056` ×3 | 1 Offense | 2 Ice | 5 | L10/r5/h1 · L1/r5/h3 · L30/r5/h2 | listed, `???` numbers |
| `064` | Geranium — Artifact Collector | `C064` ×2 | 3 Bomber | 3 Lightning | 5 | L1/r5/h3 · L30/r5/h2 | **no row at all** |
| `068` | Selene — White Darkness | `C068` ×2, `C068A` ×1 | 3 Bomber | 2 Ice | 5 | L1/r5/h3 · L30/r5/h2 · L1/r5/h0 | **no row at all** |
| `069` | Celine — Diva of Midgard | `C069A` | 4 Support | 2 Ice | 5 | L30/r5/h1 | **no row at all** |
| `070` | Alia — Electrotherapist | `C070` | 4 Support | 3 Lightning | 5 | L1/r5/h0 | **no row at all** |
| `071` | Anemone — Great General | `C071` | **1 Offense** | 1 Fire | 5 | L1/r5/h3 | **no row at all** |
| `072` | Audrey — Dangerous Gambler | `C072`, `C072A` | 3 Bomber | 3 Lightning | 5 | L1/r5/h0 · L1/r5/h0 | **no row at all** |
| `078` | Teresa (Halloween) — Ghost Bride | `C078` | 4 Support | 2 Ice | 5 | L30/r5/h0 | **no row at all** |
| `080` | Westfield — Legendary Coach | `C080` | 4 Support | 3 Lightning | 5 | L1/r5/h0 | **no row at all** |
| `082` | Mary (Christmas) — Little Santa | `C082` | 1 Offense | 3 Lightning | 5 | L30/r5/h1 | **no row at all** |
| `085` | **???** — Lunar New Year | `C085` | 4 Support | 1 Fire ⚠ | 5 | L1/r5/h0 | **no row at all** |

What the Episode source actually contributes for these 11, and what it does not:

- **Contributes (identity):** a shipped-game `ref_id` → art-pack binding
  (`C056`, `C064`, `C068`/`C068A`, `C069A`, `C070`, `C071`, `C072`/`C072A`,
  `C078`, `C080`, `C082`, `C085`), plus a native `role` and `attr` per
  occurrence.
- **Contributes (identity, newly):** for `085` it is the **only** source in the
  entire project that states a role or element at all. The catalogue leaves
  `085`'s name, rarity, role and element blank.
- **Does not contribute:** draw rarity, level as a stat input, gear state, or any
  base stat. `stat.rank = 5` on all 11 rows is a scripted-story rank and is
  **not** evidence of a ★5 draw (§0.3 item 2).
- **⚠ `085` internal contradiction.** `EVCB0301_C085` carries `attr = 1` (Fire)
  in the STAT table while the very same actor's COMBAT thumb carries
  `attr = 3` (Lightning). This is the **only** hero row of 117 where
  `STAT.attr ≠ thumb.attr`, so it is a genuine within-source disagreement, not a
  mapping error. The catalogue infers `085`'s owner as `070` Alia, who is
  Support/**Lightning** ★4 — which agrees with the thumb, not the STAT row.
  `085`'s element is therefore **unresolved**, and Support is agreed by both.

## 1.4 The 51-id uncovered-archive roster — which of them Episode now attests

`uncovered-archive-roster-2019.tsv` = the 113 heroes with **no numeric archive
row** (51 ids: 15 awakened `_1` rows plus 36 base rows — `056`, which the archive
listed without numbers, and `064`–`098`, which post-date every capture).

**All 11 Episode-only heroes are members of that roster.** That is the genuine
identity recovery, stated plainly:

> 10 heroes the 2019 archive never covered at all (`064, 068, 069, 070, 071,
> 072, 078, 080, 082, 085`) plus 1 the archive listed but never measured
> (`056`) now have a **shipped-game** identity attestation — a native `role`
> and `attr` enum bound to a real art pack — that no community source was
> needed to produce.

What that does and does not buy:

- **9 of the 11 agree exactly** with the community catalogue on both role and
  element — `056, 064, 068, 069, 070, 072, 078, 080, 082`. Each of those 9 is
  thereby upgraded from SINGLE-SOURCE to **CONFIRMED** on independent shipped
  evidence.
- `071` **disagrees on role** — shipped says Offense (1), catalogue and the
  uncovered roster both say Defense. Element (Fire) agrees. Unresolved; §1.7.
- `085` has no catalogue role/element to disagree with, and its own two shipped
  fields disagree with each other. Support is agreed; element is not. §1.7.
- **No base stat is recovered for any of the 11.** Coverage stays 1/113.

Remaining after this recovery: **40 of 113** heroes are in neither ARCHIVE nor
EPISODE (15 awakened `_1` rows, plus `065, 066, 067, 073, 074, 075, 076, 077,
079, 081, 083, 084, 086, 087, 088, 089, 090, 091, 092, 093, 094, 095, 096, 097,
098`).

## 1.5 The 10 catalogue rows the project left blank — and what fills them

The catalogue (`catalogue/INDEX.md` §2) marks 10 of 113 rows `**?**` for name and
rarity because no community Infobox existed for them. Three of them now have an
independent identity source:

| id | Catalogue title | Variant owner (inferred) | Filled by | Role | Elem | Draw ★ |
|---|---|---|---|---|---|---:|
| `026` | In Wonderland | `004` Tyltyl [i] | **ARCHIVE** `不思議の国の「チルチル」` | Support | Lightning | 1 |
| `034` | Halloween Witch | `024` Riko [i] | **ARCHIVE + EPISODE** | Defense | Ice | 2 |
| `085` | Lunar New Year | `070` Alia [i] | **EPISODE** (only) | Support | Fire ⚠ | — |

`026` and `034` are also **independent confirmations of the inferred owner**:

- `026`'s archive name is literally `チルチル` (Tyltyl) — the catalogue's
  inferred owner `004` is therefore name-confirmed. Role Support agrees; the
  element differs (Lightning vs base `004`'s Fire), i.e. `026` is a
  **re-skinned / re-elemented** Tyltyl, not a duplicate row.
- `034`'s archive name is literally `リコ` (Riko) — the inferred owner `024` is
  name-confirmed. Archive says Defense/Ice/★2, base `024` is Defense/**Lightning**/★2,
  so again the variant swaps element. The Episode STAT row independently gives
  `role 2 / attr 2` = Defense/Ice, matching the archive exactly. **`034` is the
  single strongest identity match in the file**: two independent sources, one of
  them shipped, agreeing on role *and* element *and* a name-confirmed owner.

The remaining 7 blank rows stay UNRESOLVED: `026_1`, `034_1`, `038_1`, `086_1`,
`087`, `088`, `095`.

**One flag worth carrying forward, not a fix:** `038_1`'s shipped title is
`Twilight Santa Girl`, and the catalogue infers its owner as `038`
Rebecca (Christmas) *Santa Girl*. But `Twilight` is `021` Rebecca's own epithet
(`黄昏のバット団` / *Twilight Bat Clan*). The `_1` owner inference for `038_1` may
be wrong; no source resolves it. Do not "correct" it without evidence.

## 1.6 The hard cross-validation: shipped native enums versus the archive

This is what makes the Episode crosswalk trustworthy rather than a name match.
Over the ~~103~~ **100** Episode hero rows whose `ref_id` also has a usable archive row:

> **CORRECTION 2026-10-06 — the "103 hero rows" pool contained 3 MONSTER rows.**
> `103` is reproducible only as *100 `C*`-namespace rows + 3 rows whose `res_id` is an
> `M*` monster token but which carry a 3-digit hero `ref_id`*: `CB0002_M01`
> (`M034`, `ref_id 034`), `CB0001_BOSS` (`M040`, `ref_id 040`), `CB0001_M01`
> (`M001`, `ref_id 001`). This file's §2 filter is `res_id` starts `C`, which excludes
> those 3 — so §1.6 and §2.1 were computing over **different pools in the same
> document**. **Missing filter:** `res_id` namespace was not applied to §1.6.
> Corrected figures: **`res_id`-namespace pool = 100 rows, role agreement
> 99/100**; **strict `hunter`-typed pool = 92 rows, role agreement 91/92**. The
> `role` **mismatch identity is unchanged** — `CB0102_005_1` (`005` Gerard,
> Episode `role 1` Offense vs archive `守備手` Defense) is a hunter row either way.
> **[UNRESOLVED]** the two **element** cells below (`97/103` and its 6 named
> mismatches) could **not** be reproduced under any pool; they appear to compare
> `STAT.attr` against the archive `element_ja` column via a Japanese-token
> translation step that this pass could not replicate (the archive tokens are
> `冷気`/`火炎`/`電撃`, not `氷`/`火`/`雷`). **Not edited — the values are left as
> written and flagged rather than guessed at.**

| Axis | Result |
|---|---|
| **role** | **~~102 / 103~~ 99 / 100** agree (`res_id`-namespace pool). Sole mismatch: `CB0102_005_1` (`005` Gerard), Episode `role 1` Offense vs archive `守備手` Defense. |
| **attr (element)** | **97 / 103.** The 6 mismatches are `CB1701_C510`, `CB1702_C510`, `CB1702_C509`, `CB1706_C509`, `EVCB0105_059`, `CB1604_C009`. **[UNRESOLVED 2026-10-06 — not reproduced; see the correction above. Left verbatim.]** |
| `stat.rank` vs COMBAT thumb `rank` | 116 / 117 identical; one row at thumb r4 / stat r5. **[2026-10-06: `117` is the `res_id`-namespace pool; strict `hunter` pool is 108/109, same single mismatch `CB0602_040_1`.]** |
| `STAT.attr` vs COMBAT thumb `attr` | 116 / 117 identical; sole mismatch `EVCB0301_C085`. **[2026-10-06: strict `hunter` pool is 108/109, same single mismatch.]** |
| Episode `res_id` present in the catalogue art list | 113 / 117; the 4 exceptions are `C509`/`C510`, which `catalogue/INDEX.md` §2.2 records as the 12 art packages with no `CHAR_STR_RO` row. **[2026-10-06: could not be reproduced by an independent token scan of `catalogue/INDEX.md`; left verbatim, flagged.]** |
| Episode `res_id` pack present on disk | **117 / 117.** **[2026-10-06: strict `hunter` pool is 109/109.]** |

Reading of the six element mismatches — this is a *variant-art* signature, not
noise:

- `C509` / `C510` are the only two `C5xx` packs the Episode table ever names, and
  they appear **only** on `CB17xx` rows at `L30 / r5 / hyper 3` — the awakened
  costume tier. `catalogue/INDEX.md` §2.2 lists `C509`/`C510` as art with no
  string-table row, i.e. story/costume-only. Their element disagreement with the
  archive is consistent with a costume swap, not with a wrong `ref_id`.
- `EVCB0105_059` (`059` Lantern Halloween) reads Lightning where both archive and
  catalogue say Fire. `059` is a variant of `001` and the only non-`C5xx`
  mismatch, so this one is **unexplained**.
- `CB1604_C009` reads Fire where both say Lightning — an intra-source variant
  flip on the same hero in the same episode family (`009` also appears as
  `C009` Lightning elsewhere). Unresolved.

**`attr_resist: 99`** appears on exactly 10 rows, and the set is itself
diagnostic: `CB1701_C510`, `CB1702_C510`, `CB1702_C509`, `CB1706_C509`,
`CB1402_C056`, `EVCB0201_082`, `CB0002_BOSS`, `CB0003_BOSS`, `CB0004_BOSS`,
`CB0302_010_1`. Every one is either a `C5xx` costume pack, the `082`/`056`
`hyper ≥ 1` tier, or a Vincent boss row — never an ordinary low-hyper hunter
row. It is an apparent sentinel, not a resistance value, which is why `009`/`010`
are flagged rather than trusted.

## 1.7 Contradictions and open items, kept explicit

1. **`071` Anemone — role conflict (unresolved).** Shipped Episode enum says
   **Offense**; catalogue and the uncovered roster both say **Defense**. Element
   (Fire) agrees. No archive row exists, so nothing breaks the tie. Do not pick
   one silently.
2. **`085` — element conflict inside the shipped source (unresolved).** STAT
   `attr 1` Fire vs COMBAT thumb `attr 3` Lightning; the inferred owner `070` is
   Lightning. Support is agreed by both.
3. **`059` — element conflict against two sources (unresolved).** Episode
   Lightning; archive Fire; catalogue Fire.
4. **`009`/`010` — element varies by costume pack within the Episode source.**
   `009` reads Lightning on `C009` and Fire on `C509`; `010` reads Lightning on
   `C010` and Ice on `C510`. Base identity (Lightning) is the majority reading.
5. **`005` — role conflict on one row only.** `005` has **four** Episode rows:
   `EVCB0201_005` role 2, `CB0102_005_1` role 1, `CB0103_005_1` role 2,
   `CB0401_005_1` role 2. Three of four agree with the archive (Defense);
   `CB0102_005_1` alone says Offense. Treated as a per-encounter scripted
   override, not an identity failure.
6. **The 7 UNRESOLVED rows** (`026_1`, `034_1`, `038_1`, `086_1`, `087`, `088`,
   `095`) have a shipped `TITLE` and 5 shipped skill slots, and nothing else. No
   name, role, element or rarity is recoverable from any local source.
7. **The 15 awakened `_1` rows** are single-source (catalogue) for their entire
   binding, ship no art of their own, and appear in **no** Episode row. Their
   `rarity 5` is a community claim, consistent with `INDEX.md` §2.3's restyle
   mechanism but not independently attested.
8. **`038_1` owner inference** may be wrong (§1.5).

---

# 2. UNPURE — every numeric token, quarantined

**Rule for this whole section.** Nothing below is a base stat, a coverage credit,
or a rebalance input. It is recorded so a future rebalance has the raw material
and so nothing has to be re-derived. Per `coverage.md`, none of it changes
**heroes 1/113 · accessories 1/100 · monsters 0/22**.

## 2.1 Episode STAT numeric ledger — 117 rows / 55 heroes

> **CORRECTION 2026-10-06 — the whole §2.1 ledger is `res_id`-namespace filtered, not
> `hunter` filtered.** 8 of its 117 rows are `type: "monster"` placements
> (`CB0002/0003/0004_BOSS` = `C010`; `CB1102_006/_008/_011/_018/_019` =
> `C006`/`C008`/`C011`/`C018`/`C019`). Consequences measured on the strict pool:
> **109 rows / 54 distinct `ref_id` / 62 distinct `res_id`**; heroes carrying more
> than one distinct tuple **31 → 28**, exactly-one **24 → 26**; thumb level
> distribution (`last placement` rule) **L1 ×67, L10 ×11, L15 ×1, L20 ×10, L30 ×28
> → L1 ×59, L10 ×11, L15 ×1, L20 ×10, L30 ×28**. Rows attributable to `006`, `008`,
> `011`, `018`, `019` and the three enemy-`C010` rows in the tables below are
> **monster-encounter tuning, not hunter evidence** — though like the rest of this
> file they remain **IMPURE** (scripted per-combat tuning) and earn zero coverage
> either way. **Coverage effect: none.**

`res_id HP/ATK/DEF @stat.rank`. **IMPURE** — scripted per-combat tuning. 31 of the
55 heroes carry **more than one** distinct tuple; 24 carry exactly one. The
shipped COMBAT thumb level does **not** determine these numbers
(`episode-stat-adjudication-2026-10-05.md` §1.1 already proved this for monsters
and it holds identically for heroes). Level distribution across the 117 hero rows
is `L1 ×67, L10 ×11, L15 ×1, L20 ×10, L30 ×28`.

| id | hero | rows | `res_id HP/ATK/DEF @rank` |
|---|---|---:|---|
| `001` | Lantern | 2 | C001 390/200/180 r4 ; C001 3700/3800/240 r5 |
| `003` | Nene | 3 | C003 525/160/250 r4 ; C003 514/333/394 r3 ; C003 4500/3300/280 r5 |
| `004` | Tyltyl | 2 | C004 2700/1200/1100 r5 ; C004 2000/1000/900 r5 |
| `005` | Gerard | 4 | C005 1000/280/260 r2 ; C005 310/210/290 r2 ; C005 2000/240/200 r4 ; C005 2600/1200/1400 r5 |
| `006` | Sylvester | 1 | C006 3600/3200/240 r5 |
| `007` | Metis | 1 | C007 2300/1400/200 r4 |
| `008` | Akasha | 2 | C008 3600/2800/240 r5 ; C008B 2400/1000/1100 r5 |
| `009` | Captain | 9 | C009 170/140/205 r1 ; C009 170/140/205 r1 ; C009 323/229/320 r2 ; C009 2747/1062/1553 r5 ; C009 3230/1240/1787 r5 ; C009 4000/1300/1900 r5 ; C509 4000/1300/2000 r5 ; C509 5000/1400/2100 r5 ; C009 2400/1000/1100 r5 |
| `010` | Vincent | 9 | C010 1000/100/250 r4 ; C010 2000/140/200 r4 ; C010 2000/120/160 r4 ; C010 3000/310/210 r4 ; C010 3700/1800/260 r5 ; C010 3200/1601/1149 r5 ; C010 4000/1900/1400 r5 ; C510 5000/2200/1800 r5 ; C510 5000/2200/1800 r5 |
| `011` | Hecate | 3 | C011 3300/900/250 r4 ; C011 2400/1000/1250 r5 ; C011 4500/2800/250 r5 |
| `012` | Karl Steiner | 5 | C012 2500/850/220 r4 ; C012 1150/750/550 r4 ; C012 1150/750/533 r4 ; C012 8000/3500/280 r5 ; C012 2800/2000/1100 r5 |
| `013` | Denali | 2 | C013 1300/500/160 r3 ; C013 3000/1200/1300 r5 |
| `014` | Locke | 2 | C014 3200/2800/220 r5 ; C014 3700/4200/240 r5 |
| `016` | Bruce Bang | 2 | C016 2400/1000/220 r4 ; C016 8600/2200/250 r5 |
| `017` | Lapis | 3 | C017 1500/280/180 r4 ; C017 9000/2400/240 r5 ; C017 2100/1200/950 r5 |
| `018` | Robin | 2 | C018 3100/1000/240 r4 ; C018 4500/2900/230 r5 |
| `019` | Balian | 2 | C019 3800/3200/240 r5 ; C019 2200/1200/950 r5 |
| `020` | Sienna | 1 | C020 4500/3300/260 r5 |
| `021` | Rebecca | 2 | C021 450/180/200 r4 ; C021 4100/2600/260 r5 |
| `023` | Hermes | 2 | C023 2800/1600/1100 r5 ; C023 5000/1400/1300 r5 |
| `024` | Riko | 1 | C024 5000/2400/280 r5 |
| `027` | Athena | 1 | C027B 2500/1100/1200 r5 |
| `028` | Octavia | 2 | C028 4300/3800/240 r5 ; C028B 2000/1200/900 r5 |
| `029` | Kain | 2 | C029A 2200/800/1000 r5 ; C029A 5000/1050/850 r5 |
| `030` | Acerola | 1 | C030 5500/3600/270 r5 |
| `032` | Scar | 1 | C032 2300/1300/1100 r5 |
| `034` | **???** | 1 | C034 2000/850/1000 r5 |
| `036` | Bear | 5 | C036 1700/330/220 r3 ; C036 2800/850/200 r4 ; C036 7500/4100/250 r5 ; C036B 2700/1000/1000 r5 ; C036 2500/1000/1000 r5 |
| `038` | Rebecca (Christmas) | 1 | C038 2700/1400/1100 r5 |
| `039` | Gullveig | 2 | C039 3200/2800/230 r5 ; C039 2200/1200/1000 r5 |
| `040` | Bibi | 3 | C040 4000/900/240 r5 ; C040 6500/4300/230 r5 ; C040 2400/1100/1000 r5 |
| `041` | Edward | 2 | C041 6500/3100/280 r5 ; C041 20000/1900/280 r5 |
| `042` | Santa Clauster | 1 | C042 2800/1500/1200 r5 |
| `043` | Papillon | 1 | C043 4600/3300/270 r5 |
| `046` | Harley | 1 | C046 3600/1400/1100 r5 |
| `049` | Bright | 3 | C049 900/300/140 r3 ; C049 600/356/333 r3 ; C049B 1800/900/800 r5 |
| `051` | Beckhen | 2 | C051 2400/1100/1000 r5 ; C051A 2400/1100/1000 r5 |
| `052` | Windblade | 1 | C052 6000/2100/240 r5 |
| `054` | Dino | 4 | C054 2400/1600/1200 r5 ; C054 7500/2700/210 r5 ; C054 7500/2700/210 r5 ; C054 2700/1800/1100 r5 |
| `055` | Apollon | 1 | C055B 2000/1200/900 r5 |
| `056` | Genovia | 3 | C056 7000/2800/260 r5 ; C056 3000/1600/1000 r5 ; C056 3400/1800/1450 r5 |
| `057` | Pansy | 2 | C057 4500/3800/240 r5 ; C057 2400/1000/900 r5 |
| `058` | Crocus | 1 | C058B 2300/1100/1100 r5 |
| `059` | Lantern (Halloween) | 1 | C059 1700/1300/600 r5 |
| `060` | Denali (Halloween) | 1 | C060 1800/800/700 r5 |
| `064` | Geranium | 2 | C064 2700/1600/850 r5 ; C064 2800/1900/1400 r5 |
| `068` | Selene | 3 | C068 2600/1700/850 r5 ; C068 2800/2500/1200 r5 ; C068A 2000/1300/800 r5 |
| `069` | Celine | 1 | C069A 2600/1100/1200 r5 |
| `070` | Alia | 1 | C070 2000/1000/900 r5 |
| `071` | Anemone | 1 | C071 14000/2300/280 r5 |
| `072` | Audrey | 2 | C072A 1800/1200/700 r5 ; C072 2300/1200/1000 r5 |
| `078` | Teresa (Halloween) | 1 | C078 2200/1000/1000 r5 |
| `080` | Westfield | 1 | C080 2300/1000/1200 r5 |
| `082` | Mary (Christmas) | 1 | C082 2700/1450/1150 r5 |
| `085` | **???** | 1 | C085 2200/1000/1000 r5 |

## 2.2 Archive numeric ledger — 62 rows

`HP/ATK/DEF` and `combat_power` as printed. **IMPURE** — unknown level, unknown
gear state, POST-2019-09-05 era. Full 13-field rows stay in
`archived-hunter-database-2019.tsv`; the tuple is repeated here only so this file
is self-contained.

| id | hero | HP/ATK/DEF | cp | id | hero | HP/ATK/DEF | cp |
|---|---|---|---:|---|---|---|---:|
| `001` | Lantern | 1521/1058/653 | 8359 | `033` | Patrone | 1521/1003/726 | 8580 |
| `002` | Mowgli | 1624/839/682 | 8587 | `034` | **Halloween Riko** | 1624/682/821 | 8552 |
| `003` | Nene | 1750/726/864 | 9371 | `035` | Joy | 1710/828/726 | 8236 |
| `004` | Tyltyl | 1467/679/679 | 6664 | `036` | Bear | 1923/755/864 | 10011 |
| `005` | Gerard | 1624/628/893 | 8567 | `037` | Natalia | 1750/883/755 | 9909 |
| `006` | Sylvester | 1537/817/576 | 7558 | `038` | Rebecca (Christmas) | 1790/992/668 | 9666 |
| `007` | Metis | 1277/908/576 | 6624 | `039` | Gullveig | 1521/1021/689 | 8437 |
| `008` | Akasha | 1710/762/762 | 8081 | `040` | Bibi | 1750/883/755 | 9888 |
| `009` | Captain | 1624/628/893 | 8567 | `041` | Edward | 1821/718/901 | 9495 |
| `010` | Vincent | 1923/1032/718 | 11252 | `042` | Santa Clauster | 1821/937/689 | 9659 |
| `011` | Hecate | 1537/576/817 | 7620 | `043` | Papillon | 1606/726/792 | 8261 |
| `012` | Karl Steiner | 1750/1007/689 | 9851 | `044` | Heidi | 1750/952/689 | 9764 |
| `013` | Denali | 1584/755/682 | 7293 | `045` | Yuri | 1750/937/718 | 9635 |
| `014` | Locke | 1277/908/576 | 6653 | `046` | Harley | 2033/755/1036 | 11534 |
| `015` | Levi | 1395/1014/580 | 7370 | `047` | Lily & Lyla | 1923/996/755 | 10679 |
| `016` | Bruce Bang | 1467/660/715 | 6716 | `048` | Dumble | 1750/689/901 | 9322 |
| `017` | Lapis | 1537/854/540 | 7495 | `049` | Bright | 1710/828/755 | 8403 |
| `018` | Robin | 1537/642/751 | 7716 | `050` | Therapy | 1710/825/762 | 8428 |
| `019` | Balian | 1537/817/576 | 7574 | `051` | Beckhen | 1678/864/660 | 8709 |
| `020` | Sienna | 1277/944/540 | 6565 | `052` | Windblade | 1955/992/835 | 11504 |
| `021` | Rebecca | 1624/893/580 | 8122 | `053` | Calibur | 1750/846/1284 | 10162 |
| `022` | Sunny | 1584/718/718 | 7329 | `054` | Dino | 1560/1029/744 | 8921 |
| `023` | Hermes | 1750/937/653 | 9177 | `055` | Apollon | 1560/1054/708 | 8767 |
| `024` | Riko | 1624/682/821 | 8552 | `057` | Pansy | 1742/762/806 | 8394 |
| `025` | Teddy Bomber | 1395/978/646 | 7656 | `058` | Crocus | 1710/806/806 | 8535 |
| `026` | **In Wonderland Tyltyl** | 1467/679/679 | 6664 | `059` | Lantern (Halloween) | 1521/1058/653 | 8359 |
| `027` | Athena | 1750/689/901 | 9322 | `060` | Denali (Halloween) | 1710/828/726 | 8200 |
| `028` | Octavia | 1750/901/689 | 9304 | `061` | Chichi | 1821/937/798 | 10148 |
| `029` | Kain | 1790/689/1007 | 10229 | `062` | Juno | 1968/743/1125 | 11556 |
| `030` | Acerola | 1584/718/718 | 7321 | `063` | Erise | 2019/933/1070 | 12725 |
| `031` | Diana | 1521/1021/689 | 8401 | | | | |
| `032` | Scar | 1624/839/682 | 8550 | | | | |

`056` Genovia is absent from this ledger: its archive row exists but every one of
its 13 numeric fields is the literal `???` (`fetch_status =
non-numeric-core-stats`). **No number for `056` exists in the archive.**

Note `026` (`1467/679/679`) and `004` (`1467/679/679`) are byte-identical, and
`034` (`1624/682/821`) and `024` (`1624/682/821`) are byte-identical. This is
**expected**: the variants keep the base card's numbers, and only the identity
fields (name/element) change. It is also the reason those variant rows must never
be counted as independent stat observations.

## 2.3 The 11 Episode-only heroes' numbers, in full — still IMPURE

These are the only numeric tokens the project holds for heroes the 2019 archive
never measured. They are **not** base stats: `056` for instance reads
`7000/2800/260` in `CB0802` and `3000/1600/1000` in `CB1402` — the same hero, the
same rank, two different tuples. Recorded so the 11 are not mistaken for
data-free rows.

| id | hero | Episode tuples | archive numbers? |
|---|---|---|---|
| `056` | Genovia | C056 7000/2800/260 r5 ; C056 3000/1600/1000 r5 ; C056 3400/1800/1450 r5 | none (`???`) |
| `064` | Geranium | C064 2700/1600/850 r5 ; C064 2800/1900/1400 r5 | no row |
| `068` | Selene | C068 2600/1700/850 r5 ; C068 2800/2500/1200 r5 ; C068A 2000/1300/800 r5 | no row |
| `069` | Celine | C069A 2600/1100/1200 r5 | no row |
| `070` | Alia | C070 2000/1000/900 r5 | no row |
| `071` | Anemone | C071 14000/2300/280 r5 | no row |
| `072` | Audrey | C072A 1800/1200/700 r5 ; C072 2300/1200/1000 r5 | no row |
| `078` | Teresa (Halloween) | C078 2200/1000/1000 r5 | no row |
| `080` | Westfield | C080 2300/1000/1200 r5 | no row |
| `082` | Mary (Christmas) | C082 2700/1450/1150 r5 | no row |
| `085` | **???** Lunar New Year | C085 2200/1000/1000 r5 | no row |

## 2.4 Numbers the 7 UNRESOLVED rows do **not** have

| id | shipped title | archive | Episode | any HP/ATK/DEF anywhere? |
|---|---|---|---|---|
| `026_1` | In Wonderland | — | — | none (base `026` shares `004`'s row, which is a variant duplicate, not an observation of `_1`) |
| `034_1` | Halloween Witch | — | — | none |
| `038_1` | Twilight Santa Girl | — | — | none |
| `086_1` | Valentine Condemner | — | — | none |
| `087` | Florist Lady | — | — | none |
| `088` | Florist | — | — | none |
| `095` | Knight of Swimming Pool | — | — | none |

The 15 awakened `_1` rows are in the same position numerically: **no** archive
row, **no** Episode row, **no** base number of any kind.

## 2.5 Other numeric tokens deliberately excluded from this file

- `LEVELING.jet` chunk 9 `bonus.*` role/rank multipliers and chunk 19
  `power,rank,hyper,level` — shared tuning, not per-hero. Already carried in
  `multipliers-2026-10-05.md` and `hero-stat-divergence-2026-10-05.md` §1.A S4.
- VSFan `Hunter Stats [BROKEN IGNORE].xlsx` — PRE-era and contaminated (4 tuples
  shared across two hero names). Already quarantined in
  `vsfan-hunter-stats-raw.tsv` as polluted rebalance candidates.
- Monster rows, cross-title MON BLAST! cards, monster HUD tokens and every
  polluted hero reading — all already in `polluted-observations.md` /
  `monster-hud-observations.md`. **Not duplicated here**, by instruction.

---

## Limits of this file

- **Identity only.** It promotes nothing to strict coverage. Heroes stay
  **1/113**, accessories **1/100**, monsters **0/22**.
- **Read-only.** No fixture, server file, seed, state file, APK or emulator was
  touched, and no change is proposed.
- Every count, grade, flag and tuple above was re-derived from
  `archived-hunter-database-2019.tsv`,
  `uncovered-archive-roster-2019.tsv`,
  `analysis/recovered-reference/EPISODE_STAT_ACTORS.json`, the 61
  `EPISODE_COMBAT_*.json` records,
  `analysis/catalogue/data/card-catalogue.tsv`,
  `analysis/catalogue/data/cards.json`,
  `analysis/recovered-data/leveldb-tables/{char-str,skill-ref,skill-tag}.tsv`,
  `analysis/recovered-reference/manifest.json` and the
  `split_PADResource/assets` listing. None of those files was modified.

**Machine-verified before delivery.** Three independent re-reads of the finished
file against the sources: §1.1 — all **113** rows present, zero missing, zero
extra, and every `name`/`title`/`role`/`element`/`rarity` cell byte-equal to
`card-catalogue.tsv` (the only intentional deltas are the 6 cells explicitly
marked `\*` in §1.1, which fill a blank catalogue cell from the source named in
`Src`). §1.2 — all **63** archive rows parsed and every JP listed name, role,
element, draw rarity, numeric-presence flag and capture date byte-equal to
`archived-hunter-database-2019.tsv`. §2.1 — all **55** Episode heroes with row
counts and every `res_id HP/ATK/DEF @rank` tuple byte-equal to
`EPISODE_STAT_ACTORS.json`. §2.2 — all **62** archive numeric rows with
`HP/ATK/DEF` and `combat_power` byte-equal to the TSV. Zero replacement
characters, zero stray placeholders.
- **MANIFEST never discriminates.** All 113 heroes have a shipped `TITLE` and
  exactly 5 shipped skill slots, so MANIFEST is a floor, not evidence of a
  binding. It is reported per-row in the arithmetic but excluded from grading.
- **The single hard new fact** is the shipped-enum ↔ archive crosswalk in §1.6
  (role 102/103, element 97/103, art pack on disk 117/117) and, from it, the
  confirmation that the archive's 63-id crosswalk is sound and that the Episode
  source can be trusted to name an identity the archive never listed.
