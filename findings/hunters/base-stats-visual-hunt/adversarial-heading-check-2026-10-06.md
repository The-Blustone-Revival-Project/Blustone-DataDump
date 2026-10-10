# ADVERSARIAL CHECK — "base-ness is client-attested" (2026-10-06)

**Target:** `base-stat-heading-client-attested-2026-10-06.md`
**Source of truth:** `analysis/recovered-data/leveldb-tables/all-tables.json`
**Method:** read-only Python only. No PowerShell Get-Content/Set-Content. No edits to
`coverage.md`, any TSV, `server-ts`, APK, seeds, emulator, phone or Ghidra.
`polluted-observations.md` **not appended**.

---

# VERDICT: **SURVIVES-WITH-CAVEAT**

**What survives, and it is more than the claim asserted.** The client genuinely
ships the archive's two headings, byte-identically, in all five locales, inside a
dedicated 3-block stat widget family. That part is now genuinely
`[RECOVERED]` and is **stronger than the original claim** — the original argued
from `UI_TEXT_RO` + one widget; I additionally recovered the *whole* panel
structure from `UI_XML_RO`, which the original note never opened.

**What does not survive.** The load-bearing inference — *heading says "Base Stat"
⇒ values are gear-free* — is **not supported by anything in the client**, and I
found three independent pieces of counter-evidence. `기본 능력치` in this game is
**"basic/primary", not "base/unmodified"**. The gear-exclusion sense of "base"
is **[UNKNOWN]** and the claim's own §3.2 correctly named it as the residual
risk; my finding is that §3.2 is not merely "risk", it is the **unproven link
the argument silently depends on**, and it has active counter-evidence against it.

So: the coverage upgrade 1/113 → 62/113 **is not licensed by this note**. The
"client-attested" framing overstates what was established. Base-ness remains
**source-labelled, not client-attested.**

---

# 1. HARNESS VALIDATION (run before any zero was believed)

Same loader, same matcher, on `tables.*`:

| control | expected | got | verdict |
|---|---|---|---|
| `UI_TEXT_RO` contains `Base Stat` | >0 | **4** | PASS |
| `UI_TEXT_RO` contains `캐릭터` | >0 | **8** | PASS |
| `UI_JSON_RO` contains `TEXT` | >0 | 25 317 | PASS |
| `UI_JSON_RO` contains `SIZE` | >0 | 49 409 | PASS |
| `UI_TEXT_RO` contains `ZZZ_NOT_A_REAL_STRING` | 0 | **0** | PASS |

Also structural: `UI_TEXT_RO`/`UI_JSON_RO`/`CHAR_STR_RO`/`UI_EPISODE_RO`/
`SKILL_REF_RO` all have entry shape `{key, json, raw}`; `UI_JSON_RO` has
12 351 entries, **all** of which split into exactly 3 `|`-separated fields
(`label|widget|locale`) — **0 exceptions** (`all-tables.json` `summary`).

**Two of my own zeros were false negatives; both are retracted in this file** —
see §2.3 and §5.2. Recording them because the note under review got exactly this
wrong in its §4 and the same discipline is owed here.

---

# 2. AXIS 1 — Is `TX_ST_TL1` really a stat-block title? **YES. Strongly.**

## 2.1 Exhaustive enumeration, as demanded

`UI_JSON_RO` widget census over **all 12 351** entries → **1 494** distinct
widget names. Exactly **5** entries carry widget `TX_ST_TL1`, and they carry
**exactly one** 1st-field label:

| file:index | key | EN | JA | SIZE | ALIGN |
|---|---|---|---|---|---|
| `UI_JSON_RO[10756]` | `캐릭터 기본 능력치\|TX_ST_TL1\|EN` | `Base Stat` | `基本能力値` | 28 | left\|center |
| `UI_JSON_RO[10757]` | `…\|JA` | `基本能力値` | — | 28 | left\|center |
| `UI_JSON_RO[10758]` | `…\|KO` | `기본 능력치` | — | 28 | left\|center |
| `UI_JSON_RO[10759]` | `…\|SC` | `基本能力值` | — | 28 | left\|center |
| `UI_JSON_RO[10760]` | `…\|TC` | `基本能力值` | — | 28 | left\|center |

**The "other screens use `TX_ST_TL1` with different headings" attack fails
cleanly: there are no other headings.** One label, one widget, five locales.

## 2.2 The decisive thing the original note missed: `TX_ST_*` is a *panel family*

`TX_ST_*` is not a loose prefix. It is **one coherent 3-block stat panel** with
a strict number/value pairing (`TX_ST_SB<n>` = label, `TX_ST_NM<n>` = value):

```
UI_XML_RO[275]  KO/SR_COMMON/1_UI_CM_CH/2_UI_CM_C_ME
  rect RE_CH_DI1: TX_ST_TL1 '캐릭터 기본 능력치'   <- "Base Stat"
                  TX_ST_SB1 '생명력'      TX_ST_NM1  = HP           @UI_JSON_RO[6971]
                  TX_ST_SB2 '방어력'      TX_ST_NM2  = DEF          @UI_JSON_RO[5766]
                  TX_ST_SB3 '공격력'      TX_ST_NM3  = ATK          @UI_JSON_RO[3021]
                  TX_ST_SB4 '공격 속도'   TX_ST_NM4  = AttackingSpeed @UI_JSON_RO[2966]
  rect RE_CH_DI2: TX_ST_TL2 '세부 능력치 : 공격력'  <- "Attack Stat Details"  @UI_JSON_RO[7156]
                  TX_ST_SB5 치명타 확률 / SB6 치명타 피해량 / SB7 관통력
  rect RE_CH_DI3: TX_ST_TL3 '세부 능력치 : 방어력'  <- "Defense Stat Details" @UI_JSON_RO[7161]
                  TX_ST_SB8 막기 확률 / SB9 피해 감소량 / SB10 속성 강화
                  / SB11 속성 저항 / SB12 생명력 재생량
```

This is **stronger than the original claim**: `TX_ST_TL1` is not "a title
widget that happens to say Base Stat"; it is the title of a **specific
rect-delimited block containing exactly HP/DEF/ATK/Attack-Speed** — the same
4-stat set the archive prints under `基本能力値` (`level-factor-test-2026-10-05.md:174`).

## 2.3 RETRACTION of one of my own probes

I initially read `TR_STAT_POP`'s `text-global="공격력[개행x]"` as a
**delta/gear-suffix placeholder**, which would have been direct axis-2 evidence
of a gear-delta presentation. **That reading was wrong.** `[개행x]` is
`개행` = *line break*; `[약식]` = *abbreviation*. My control that reported
`0` layouts containing `[개행` was itself a **false negative**: I searched the
**raw** XML, which is HTML-entity-encoded (`&#44060;&#54665;` = 개행). Re-run on
decoded text: `[개행` → **2** layouts, `[약식` → **2**. `[값` → 0 (control
passes: the token genuinely does not exist). I withdraw the delta reading.

---

# 3. AXIS 2 — THE CRUX. Does "Base Stat" mean **gear-free**?

## 3.1 What the client actually contrasts

`기본` contrasts with `세부` (**detail**), never with any gear term:

| heading | block content | EN |
|---|---|---|
| `TX_ST_TL1` `기본 능력치` | HP, DEF, ATK, Attack Speed | **Base Stat** |
| `TX_ST_TL2` `세부 능력치 : 공격력` | crit, crit-dmg, pen | Attack Stat Details |
| `TX_ST_TL3` `세부 능력치 : 방어력` | block, blockred, elem-enh, elem-res, regen | Defense Stat Details |

So the axis is **primary-vs-secondary**, exactly as in D&D-style stat sheets.
`기본` = "the primary/basic ones". **There is no second heading of the same
noun meaning "with gear".**

## 3.2 Positive-controlled search for gear-exclusion semantics — all ZERO

Controls first: KO `기본` → **8**; KO `방어력` → **7**; `UI_JSON_RO` KO
`기본 능력치` → **1**. Matcher proven live.

| probe | hits |
|---|---|
| KO `장비 제외` / `장비미착용` / `장비 없이` / `기본 능력치 제외` / `순수 능력치` | 0, 0, 0, 0, 0 |
| EN `excluding` / `without equipment` / `base only` / `naked` / `unequipped` | 0,0,0,0,0 |
| JA `装備なし` / `装備を含` / `除外` / `素の` | 0,0,0,0 |
| EN pairs of (gear-term × stat-term) — `Gear`×`stat`, `Equip`×`stat`, `Item`×`stat`, `Jewel`×`stat`, `Total`×`stat`, `Current`×`stat`, `Adjusted`, `Effective` | **all 0** |

**The client never says "base" in this game means "excluding gear".** The
property is unattested, not attested.

## 3.3 Counter-evidence 1 — EN "Base" is a *generic adjective*, elsewhere

`UI_TEXT_RO[68]` key `1스킬_태그`: KO `기본` → EN **`Base`**, JA `基本`.
Same EN word, completely unrelated context (a skill tag). So EN `Base` is the
dictionary rendering of the ordinary Korean adjective, not a stat-system term of
art. **This materially weakens reading EN "Base Stat" as a gear-exclusion
claim.**

## 3.4 Counter-evidence 2 — "기본 능력치" is the LIVE, gear-adjacent stat pool

The client attributes **runtime percentage buffs** and **Awakening** to this
exact quantity:

| file:index | EN |
|---|---|
| `SKILL_REF_RO[554]` `051\|5\|0` | "Increases the basic ability of self by 10% during a Fight Club battle." |
| `SKILL_REF_RO[784]` `074\|5\|1` | "Increases all teammates' basic ability by 10% during the Guild Blitz battle." |
| `TAG_REF_RO[14]` `BLITZ_TEAM_BONUS\|DESC` | "Increases the basic stat of all dispatched members of the team by 10%…" |
| `TAG_REF_RO[54]` `FIGHTCLUB_BOUNS\|DESC` | "Increases the basic stat of self by 10%…" |
| `UI_TEXT_RO[418]` `각성_설명` | "You'll gain new power through Awakening. **Your basic stats will increase**…" |

A **frozen reference column** cannot be "increased by 10% during a battle".
`기본 능력치` is therefore the **live stat pool the stat panel displays**. A
heading over the live pool does **not** by itself certify gear-exclusion — and
JA `TAG_REF_RO[14]` even drops 基本: `出撃チームの全体能力値を10%増加` (plain
`能力値`), i.e. the client is loose about which modifier it attaches.

## 3.5 Counter-evidence 3 — the panel lives ON THE GEAR SCREEN, next to the level gauge

`TX_ST_TL1` is instantiated in exactly **3** layouts (exhaustive):

| file:index | layout | gear controls on same layout | level on same card |
|---|---|---|---|
| `UI_XML_RO[275]` | `KO/SR_COMMON/1_UI_CM_CH/2_UI_CM_C_ME` | no `TX_UP` | no `EN_LEVEL` |
| `UI_XML_RO[367]` | `KO/SR_ENHANCE/3_SR_EN_CH/1_UI_EN_C_TI` | **`TX_UP` = `장비강화`** (Equipment Upgrade) | — |
| `UI_XML_RO[376]` | `KO/SR_ENHANCE/3_SR_EN_CH/TR_TEAMMATE` | **`TX_UP`/`TX_UP_OFF` = `장비강화` / `장비 관리`** (Equipment Management) | **yes, `EN_LEVEL_NUM` = `0/30`** |

`SR_ENHANCE` is the **gear screen**: `UI_XML_RO[367]`'s own labels resolve to EN
`Power` / `Train` / `Story` / `HP` / `DEF` / `ATK` / `Attacking Speed`, plus
`장비강화`. **2 of the 3 hosts of the "Base Stat" heading are the gear
management screen.** A block whose entire purpose is "your stats as they are
now, next to your gear" is precisely where a *live* pool is displayed.

**The level co-location is the sharpest finding.** In `UI_XML_RO[376]` the level
gauge `RE_LEVEL_GAUGE@19250 / RE_LEVEL_INFO@19350 / RE_LEVEL_THUMB@19537`
sits within 3000 chars of **both** `RE_CH_DI1` panels (`@16735`, `@21522`) —
i.e. **the "Base Stat" panel and `Lv. n/30` are in the same card block.**
(Two of the seven `RE_LEVEL*` nodes — `@5457`, `@25156` — are far away; those are
the list-header rows, not this card.)

> **A "Base Stat" block in this client is LEVEL-BEARING.** It is not an
> as-drawn Lv.1 row. Therefore a heading reading "Base Stat" **cannot** by
> itself certify that a value is level-independent.

## 3.6 Verdict on axis 2

`기본 능력치` = **"basic/primary stats"**, the display heading for the
HP/DEF/ATK/Speed block. The gear-free reading is **[UNKNOWN]**, with three
pieces of active counter-evidence (§3.3 generic adjective, §3.4 live
buffable pool, §3.5 co-located with gear UI and a level gauge).

**The chain breaks here:** `heading says "Base Stat"` does **not** entail
`values are gear-free`, and the claim's §1→§5 inference runs straight through
that gap.

---

# 4. AXIS 3 — Is the JA match load-bearing, or coincidence?

**It is load-bearing but not decisive.** Census of `基本能力値` across **all 13
tables** (control: `能力値` → **30** rows, so the matcher works):

| file:index | JA |
|---|---|
| `UI_TEXT_RO[329]`, `UI_TEXT_RO[567]`, `UI_JSON_RO[10757]` | the heading |
| `UI_TEXT_RO[418]` | Awakening raises `基本能力値` |
| `SKILL_REF_RO[554]`, `SKILL_REF_RO[784]`, `TAG_REF_RO[54]` | buffs raise `基本能力値` by 10% |

**The match is not an independent coinage** — the portal is transcribing the
game's own term, and `詳細能力値` likewise (`UI_TEXT_RO[324]`, plus
`[323]`/`[325]` `攻撃詳細能力値` / `防御詳細能力値`). So the original note's
§1.3 "byte-identical in both locales" holds, and the *provenance* argument is
real.

**But it proves a shared vocabulary, not a shared semantics.** Note the
portal re-renders the sub-headings with **different word order**
(`詳細能力値：攻撃力` vs client `攻撃詳細能力値`), so it is a *faithful
re-rendering of the same 3-block scheme*, not a verbatim copy — consistent with
transcription-from-game, and equally consistent with two parties independently
adopting the same natural JA phrasing for "basic stats". The byte-identity
argument proves **the portal used the game's terms**; it cannot prove **the
game intended gear-exclusion by them**, because §3.2–3.5 show the client never
says that.

---

# 5. AXIS 4 — Two-block structure, or over-read adjacent `TR_` keys?

**Real, and the original note got the citation slightly wrong.**

- `UI_TEXT_RO[323]` `TR_공격 세부 능력치` → EN `Attack Stat Details` / JA `攻撃詳細能力値` → **`TX_ST_TL2`**
- `UI_TEXT_RO[325]` `TR_방어 세부 능력치` → EN `Defense Stat Details` / JA `防御詳細能力値` → **`TX_ST_TL3`**

Both are genuine stat-block headings (SIZE 28, same B_RECT `25|25`,
`400|40`, same left|center), and each governs a **rect-delimited** block.

**Correction to the claim's §1.3:** it cites `UI_TEXT_RO[324]`
`TR_능력치 상세 정보` (EN `Stat Details` / JA `詳細能力値`) as the client's
"separate sub-stat heading". `TR_STAT_POP` (`UI_XML_RO[375]`) binds it to
`name=TOP_TEXT` at **font size 30** — it is the **popup title**, *above* the
`TR_캐릭터 기본 능력치` line at size 26. `324` is a dialog caption, not a block
heading. The claim's *"the game has exactly two stat headings"* is therefore
**three block headings + one popup caption**. The archive's second heading is
`詳細能力値` which matches the popup title; the archive's sub-blocks
(`詳細能力値：攻撃力` / `：防御力`) match `[323]`/`[325]`. Net: the structural
analogy survives; the exact index citation does not.

---

# 6. AXIS 5 — Anything that CONTRADICTS "these are base stats"?

**Yes — one strong partial contradiction, plus one that favours the claim.**

## 6.1 CONTRADICTS: the client's "Base Stat" is level-bearing (§3.5)

`UI_XML_RO[376]` puts `Lv. n/30` and the `基本能力값` panel in **the same card
block**. If the client's own "Base Stat" block renders whatever the card's
stats currently are, then "Base Stat" is orthogonal to level, and a value
labelled "Base Stat" carries **no level guarantee**. The archive's
`level: not shown` (`not shown` on **63/63** rows) therefore remains a real gap,
exactly as §3.1 of the claim itself conceded — but the claim's §1 evidence does
not close it, and §3.5 shows why it **cannot** be closed by the heading.

## 6.2 FAVOURS: sub-stat identity for `051`

`051` archive row: `speed 8, crit 33, crit_damage 200, pen 0, block 14,
blockred 42, elem_enh 5, elem_res 5, hp_regen 42` — byte-identical on all nine
sub-stats to the FAQ Lv.30 **no-equip** panel (`level-factor-test-2026-10-05.md:278-280`).
Jewels move `elem_enh/elem_res/regen/crit`, so identical sub-stat vectors are
real evidence of a gear-free reading. **But n=1, and it constrains only
sub-stats, not HP/ATK/DEF** — which is where the gear question actually bites.

## 6.3 Internal consistency of the 62 rows — no contradiction found

`archived-hunter-database-2019.tsv`: **63** rows, **62** numeric; `level`
`{not shown}` ×63; `gear_state` `{not established}` ×63; `fetch_status`
`{ok: 62, non-numeric-core-stats: 1}` (`056` Genovia, `hp='???'`).

| rarity | n | HP | ATK | DEF |
|---|---:|---|---|---|
| 1★ | 12 | 1277–1624 | 576–944 | 540–893 |
| 2★ | 11 | 1395–1624 | 628–1014 | 580–893 |
| 3★ | 34 | 1521–1968 | 689–1058 | 653–1284 |
| 4★ | 5 | 1923–2033 | 755–1032 | 718–1070 |

20 distinct HP over 62 rows; 50 distinct `(hp,atk,def)` triples; top repeated
values `1750`×11, `1624`×7, `1710`×6. Duplicate triples carry differing
`combat_power` (e.g. `1710/828/726` → `8200` vs `8236`), consistent with the
claim's §2.1 "designed lookup table" reading. **Speed takes only `6,7,8`** —
matching the client's 4th base-block stat `TX_ST_SB4` "Attacking Speed"
(`UI_JSON_RO[2966]`) and the archive page's `攻撃スピード 8`. The archive's
column set maps **4 + 9 = 13 stats onto the client's `SB1..SB12` + speed
structure**, a good independent corroboration that the portal transcribed the
game's stat panel.

**Nothing internal contradicts base-ness** — but nothing internal establishes it
either, because `level` and `gear_state` are unset on every row.

---

# 7. What exactly breaks, stated precisely

The claim's chain:

```
L1  client ships 基本能力値 / "Base Stat" as a stat-block title   -> PROVEN (§2.1, §2.2)
L2  archive uses both headings byte-identically                  -> PROVEN (§4)
L3  therefore the archive rows are gear-free  "base" values      -> NOT SUPPORTED
```

**L3 is the break.** It has no positive support and three pieces of negative
support (§3.3, §3.4, §3.5). The inference is an unlicensed semantic jump from
*label* to *statistical property*.

Secondary defects, non-fatal:
- §1.3's "exactly two stat headings" — actually 3 block headings + 1 popup
  caption; `UI_TEXT_RO[324]` is the caption (`TOP_TEXT`, size 30).
- The note's own §5 correctly flagged this as "the parent's call" and
  **recommended the upgrade anyway**. The recommendation is not supportable on
  this evidence, and §3.5 makes the `level` caveat worse, not better.

**Additional finding the original note missed, in its favour:** the panel is
rect-delimited and 1:1 with `TX_ST_SB1..SB12` + `TX_ST_NM1..NM12`, hosted in 3
layouts under `SR_COMMON`/`SR_ENHANCE`, with an exact 4-stat + 2×sub-block
shape that the archive's 13 columns reproduce. **Provenance of the archive's
transcription is now much better established** — that is a real gain.

---

# 8. Recommendation to the owner of `coverage.md`

**Do not apply the 1/113 → 62/113 upgrade on the strength of this note.**
The upgrade's stated ground ("base-ness is client-attested") is not established:
`gear_state` is `not established` on **63/63** rows, and the client provides
neither gear-exclusion vocabulary nor a gear-free reading of `기본 능력치`.

What **is** now established, and is worth recording separately:

1. `[RECOVERED]` the client ships `기본 능력치` / `Base Stat` / `基本能力値` as
   the title of a rect-delimited stat block (`UI_TEXT_RO[329]`,`[567]`;
   `UI_JSON_RO[10756..10760]`; `UI_XML_RO[275]`,`[367]`,`[376]`).
2. `[RECOVERED]` that block contains exactly **HP, DEF, ATK, Attack Speed** —
   matching the archive's `基本能力値` block 4-for-4.
3. `[RECOVERED]` the archive's 13 columns map 1:1 onto the client's
   `TX_ST_SB1..SB12` family.
4. `[UNKNOWN]` whether `기본 능력치` is gear-exclusive — **never stated** by the
   client, with 3 counter-indications (§3.3/3.4/3.5).
5. `[RECOVERED]` the client's "Base Stat" block is **level-bearing**
   (`EN_LEVEL_NUM` co-located, `UI_XML_RO[376]`), so the heading certifies
   nothing about level.

If the coverage definition requires a **gear-free base tuple**, item 4 blocks
the upgrade and the count correctly stays **1/113**. Items 1–3 are still worth
banking: they establish that the portal transcribed the game's own stat panel,
which is the *provenance* half of the argument — a real and durable gain that
survives this refutation intact.

---

# 9. Files touched / not touched

**Created:** this file only. Scripts in `%TEMP%\opencode\adv\` (read-only; write
only to their own `.txt`).
**Not touched:** `coverage.md`, `README.md`, `polluted-observations.md`, every
TSV, `analysis/catalogue/**`, `server-ts`, fixtures, seeds, APK, emulator,
physical phone, Ghidra project, native library. No account or game state was
read or written.