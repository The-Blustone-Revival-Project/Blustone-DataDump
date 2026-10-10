# Battle scene — UI record keys and resource requirements

**Role:** static research agent, battle-scene resources.
**Date:** 2026-10-02.
**Scope:** worked ahead of the current native crash (`CSRGameBase::MakeCamp`,
`analysis/testing/report-009.md`) so that when the crash is fixed the UI/resource
layer is not the next wall.

Every claim below is tagged:

| Tag | Meaning |
|---|---|
| **[RECOVERED]** | Derived from native evidence or from a real database/file, with the address or path cited. |
| **[FIXTURE]** | Local compatibility data. Not original content. |
| **[UNKNOWN]** | Not established. Explicitly not guessed. |

Nothing here has been run on a device. Agent E owns adb/BlueStacks and the
running server; no APK was rebuilt or installed.

---

## 0. Headline

**The battle scene's UI record layer is already complete. It is not a second
blocker.**

The currently-installed seed `instrumented-seed-complete-ui-delta-v2` already
carries `EN/` aliases for **all 55** battle UI records — verified
byte-for-byte against the pristine shipped database below. There is no missing
battle UI record to seed.

The genuinely under-specified part is the **resource** side, and it is
incomplete in a way that is cheap to fix from the server side (no client rebuild
required): the replica serves 8 stage assets but the APK carries **13 more
battle-relevant packages that are neither CDN items nor folded assets**, and
three of them (`UI_INGAME`, `INGAME_ICON`, `DMGFONT`) are named directly by the
battle UI records. See §3.

A second, more subtle finding is in §5: **a third-party LevelDB library opens
these seeds read/write and silently compacts them.** That is a trap for whoever
inspects the seed next.

---

## 1. The shipped `UI_XML_RO.db` is a KO-only database

**[RECOVERED]** `recovered-assets/phone-2026-09-18/private/files/local/UI_XML_RO.db`
contains **584 keys**: 573 under `KO/`, 3 under `EN/`, 3 `JA/`, 3 `SC/`, 2 `TC/`.

The 3 pre-existing `EN/` keys are unrelated to battle:

```
EN/GUILD/G_C_GUILD
EN/SR_CHALLENGE/CH_SE_POP
EN/SR_ENHANCE/7_SR_EN_SK
```

So for the battle scene the shipped database provides **zero** `EN` records out
of the box. This is exactly the situation AGENTS.md §7 describes for the
mission map, and the same selective-delta remedy applies.

Reproduce:

```
python tools/list-ui-db-keys.py recovered-assets/phone-2026-09-18/private/files/local/UI_XML_RO.db
```

### The same shipped database, before patching

**[RECOVERED]** `recovered-assets/phone-2026-09-18/extracted/split_PADResource/assets/UI_XML.db`
survives only as an unrecovered LevelDB write-ahead log (`000003.log`, 3.5 MB)
plus a 50-byte MANIFEST. `plyvel` cannot open it, so
`tools/read-leveldb-log.py` was written to decode the physical-record framing
and then the WriteBatch operations directly.

It yields the **same 584 keys** with the same locale split — so
`UI_XML.db` and `UI_XML_RO.db` are the same content, and `UI_XML_RO.db` is the
runtime "recovered/open" variant.

**[RECOVERED]** One useful difference: the `UI_XML.db` records have **no
`file=` attributes on `<comp-motion>`**, whereas the patched `UI_XML_RO.db`
records do. So the `file="UI_BT_PRE_*"` injection is a **local patch**, applied
by a previous experiment, not shipped content. Confirmed by diffing, e.g.
`SR_INGAME/UI_HP_N`:

```
KO (pristine): <comp-motion name="DAMAGE_SHAKING" group="DAMAGE">
EN (patched) : <comp-motion name="DAMAGE_SHAKING" group="DAMAGE" file="UI_BT_PRE_S">
```

This matters for interpretation: the patched records are *not* the original EN
layout, they are the original KO layout with a motion-path override. There is no
shipped EN battle layout in this build to recover.

---

## 2. Task 1 — the battle scene UI record key table

### Method

The record namespace is derived from the database, not guessed. Records live at
`EN|/<GROUP>/<RECORD>`; the native library stores the locale-stripped
`<GROUP>/<RECORD>` string and prefixes the language at resolution time. So:

1. walk `KO/*` in the pristine database → the candidate record set;
2. match each record name against `analysis/native-all-strings.tsv` →
   **[RECOVERED]** the client genuinely names it as a literal;
3. check whether an `EN/` record exists.

The four battle groups are `BATTLE/`, `SR_BATTLE/`, `SR_INGAME/`, `SR_INGAME2/`.

Reproduce:

```
python tools/map-ui-records-to-strings.py \
    --db recovered-assets/phone-2026-09-18/private/files/local/UI_XML_RO.db \
    --db2 instrumentation/assets/instrumented-seed-battle-en-delta-v1/UI_XML_RO.db \
    --strings analysis/native-all-strings.tsv
```

### Full table

**`analysis/battle-scene/ui-record-key-table.tsv`** — 55 rows, machine-readable.

| Group | Records | EN present in pristine | EN present after seeding |
|---|---|---|---|
| `BATTLE/` | 5 | 0 | **5** |
| `SR_BATTLE/` | 27 | 0 | **27** |
| `SR_INGAME/` | 14 | 0 | **14** |
| `SR_INGAME2/` | 9 | 0 | **9** |
| **Total** | **55** | **0** | **55** |

### Counts by action needed

| Action needed | Count |
|---|---|
| none (already aliased in the installed `delta-v2` seed) | **55** |
| alias required | **0** |
| unknown | **0** |
| excluded (`DEFINE_COLOR`) | 0 (it is not in a battle group) |

**Every one of the 55 battle records that exists in the shipped database now has
an `EN` alias.** There is nothing left to alias for the battle scene.

### Zero records missing outright

**[RECOVERED]** Walking the *other* direction — every battle-shaped literal in
the native string table, checked against every DB record under any locale —
returns **zero** candidates with no record:

```
python tools/find-missing-ui-records.py \
    --db recovered-assets/phone-2026-09-18/private/files/local/UI_XML_RO.db \
    --extra-db instrumentation/assets/instrumented-seed-battle-en-delta-v1/UI_XML_RO.db \
    --strings analysis/native-all-strings.tsv \
    --grep "BATTLE|INGAME|UI_BT|_BT_|BT_|IG_|SKILL_BUTTON|MODULE_"
# 0 candidate literals with no DB record
```

So the client cannot ask for a battle UI record that the database cannot supply.
**The UI key layer has no hole.**

### The records the native library actually names

**[RECOVERED]** 30 of the 55 are named as string literals in `libnative_core.so`,
with these addresses. These are the highest-confidence members of the set:

| Record | Address |
|---|---|
| `BATTLE/BT_LOBBY` | `01d80012` |
| `BATTLE/BT_RANK_T` | `01d9139e` |
| `BATTLE/BT_RANK_CELL` | `01d913af` |
| `BATTLE/BT_RWD` | `01d91426` |
| `BATTLE/BT_RWD_CELL` | `01d914cd` |
| `SR_BATTLE/3_UI_BT_DF` | `01d8012c` |
| `SR_BATTLE/5_UI_BT_MS` | `01d8017d` |
| `SR_BATTLE/6_UI_BT_MS` | `01d80658` |
| `SR_BATTLE/7_UI_BT_RK_A` | `01d8075f` |
| `SR_BATTLE/9_UI_BT_IG` | `01d73707` |
| `SR_BATTLE/11_BT_MS_ALL` | `01d84834` |
| `SR_BATTLE/BT_MN_NEW` | `01d911af` |
| `SR_BATTLE/BT_USERMATCH` | `01d80577` |
| `SR_BATTLE/LEAGUE_INFO` | `01d80448` |
| `SR_BATTLE/BT_RESULT/UI_BT_RE_WIN` | `01d803bc` |
| `SR_BATTLE/BT_RESULT/UI_BT_RE_LOS` | `01d803dd` |
| `SR_BATTLE/BT_RESULT/BT_LOS2_NEW` | `01d8051e` |
| `SR_BATTLE/BT_RESULT/BT_WIN_NEW` | `01d80797` |
| `SR_INGAME/INGAME_NM` | `01d75583` |
| `SR_INGAME/INGAME_MR` | `01d75597` |
| `SR_INGAME/SKILL_EFT` | `01d772e6` |
| `SR_INGAME/SKILL_TIP` | `01d77f6c` |
| `SR_INGAME/UI_BOSS` | `01d77b41` |
| `SR_INGAME/UI_TIMER` | `01d77d4c` |
| `SR_INGAME/UI_SKILL` | `01d77dc5` |
| `SR_INGAME/UI_SP` | `01d77e41` |
| `SR_INGAME/UI_PROG` | `01d77ede` |
| `SR_INGAME/UI_LYR_NM` | `01d7801d` |
| `SR_INGAME/UI_FEVER` | `01d7814d` |
| `SR_INGAME/UI_HP_N` | `01d778b5` |
| `SR_INGAME/9_IG_PAUSE` | `01d80e6c` |
| `SR_INGAME2/ACTOR_BASE` | `01d74826` |
| `SR_INGAME2/EFFECT_BASE` | `01d76369` |
| `SR_INGAME2/INGAME_NORMAL` | `01d80d2d` |
| `SR_INGAME2/MODULE_ACTOR_GROUP` | `01d74c53` |
| `SR_INGAME2/MODULE_SKILLVIEW` | `01d78416` |
| `SR_INGAME2/MODULE_UI` | `01d777b5` |
| `SR_INGAME2/SKILL_BUTTON` | `01d74e23` |
| `SR_INGAME2/UI_COMPONENT` | `01d777d5` |

**[RECOVERED]** `UI_BATTLE` at `01d736b4` — the string the task brief cites — is
**not** a UI record key. It is a **resource/package name**, and it is the only
battle-ish literal in the table that has no `SR_.../` path shape. The record
`SR_BATTLE/9_UI_BT_IG` at `01d73707` sits 0x353 bytes later, which is why the
two are easy to conflate.

The remaining 25 records are **[RECOVERED]** present in the database under `KO/`
and reachable by the same naming scheme but not individually named in the string
table (e.g. `SR_BATTLE/0_UI_BT_MN`, `SR_BATTLE/BT_DECKSET`,
`SR_BATTLE/BT_RESULT/UI_BT_RESULT`, `SR_INGAME/UI_PROG`, `SR_INGAME2/UI_FEVER`).
They are included in the seed because they ship in the same group and the client
can request any of them; excluding them would be a guess in the unsafe direction.

### The records are XML, and they name sprites

**[RECOVERED]** The 55 records are XML fragments. A real excerpt from
`EN/SR_INGAME2/MODULE_UI`:

```xml
<layer name="LY_UI_BASE" size="screen, screen" ...>
  <layer name="LY_INGAME_LAYER" pos="0, 60" ...>
    <button name="BTN_PAUSE" size="80, 80" align="right, top" event="pressed, release" ...>
      <res-sprite res-name="UI_IG_EXIT" .../>
    </button>
    <video name="VD_SKILL_BG" res-name="BG_LIGHT" ...>
    <button name="BT_AUTO" size="100, 100" align="left, bottom">
      <layer name="LY_AUTO_ALL" size="100, 100" align="center, center">
        <res-sprite res-name="AUTO2_T" align="center, center">
          <comp-motion group="init" loop="t" file="UI_BT_PRE_S">
            <trans rot="0, 0, -360" time="1.5"/>
          </comp-motion>
        </res-sprite>
        <textbox name="AUTO_AUTO" text-ko="AUTO"/>
      </layer>
    </button>
```

Reproduce with:

```
python tools/dump-ui-record.py \
    --db instrumentation/assets/instrumented-seed-battle-en-delta-v1/UI_XML_RO.db \
    --key EN/SR_INGAME2/MODULE_UI
```

This is the key structural fact: **the battle UI record layer is not a set of
missing keys, it is a set of present keys that name 236 sprites.** §3 is about
those sprites.

---

## 3. Task 2 — the battle scene's resource requirements

### 3a. What the records reference

**[RECOVERED]** The 55 battle records name **236 distinct resources** via
`res-name=` / `file=` attributes. Reproduce:

```
python tools/collect-ui-resource-refs.py \
    --db instrumentation/assets/instrumented-seed-battle-en-delta-v1/UI_XML_RO.db \
    --group SR_INGAME --group SR_INGAME2 --group SR_BATTLE --group BATTLE
```

Breakdown by role, sampled from the full list (the authoritative list is the
tool's stdout; only representative names are quoted here):

| Role | Sample names |
|---|---|
| In-battle HUD | `UI_IG_EXIT`, `UI_IG_TIME`, `UI_IG_TM`, `UI_IG_TM_BG`, `UI_IG_TM_LI`, `UI_IG_NAV`, `UI_IG_NAV_BG`, `UI_IG_S_L`, `UI_IG_L_L`, `UI_IG_P_L`, `UI_IG_I_L` |
| Character frames | `UI_IG_CH`, `UI_IG_CH_BG`, `UI_IG_CH_R`, `IG_CH_S`, `IG_CH_BG_S`, `IG_FR_ICON`, `IG_SD_IMG`, `IG_SD_SK` |
| Gauges | `IG_GAGE`, `IG_GAGE_BG`, `BT_GAGE`, `BT_GAGE_BG`, `BT_GAGE_BOX` |
| Skill slots (9) | `IG_SK_P1` … `IG_SK_P9`, `IG_SK_BG1`, `UI_IG_SKILL`, `UI_IG_SK_EF`, `UI_IG_SK_T`, `UI_IG_SK_BG` |
| Fever | `IG_FI_GA0`, `IG_FI_GA1`, `IG_FI_GA_G`, `IG_FI_GA_ON`, `IG_FI_GA_T`, `IG_FI_GA_T_G`, `IG_FI_BG0` |
| Auto/TAP | `AUTO2_T`, `AUTO2_F`, `AUTO_K_ON`, `AUTO_K_OFF` |
| Turn-order list | `IG_LS_BG`, `IG_SD_AT`, `UI_IG_TR_IC0`, `UI_LS_TITLE` |
| Battle result | `VICTORY`, `FL_VS`, `MS_VS`, `ICON_VS`, `VS_LINE`, `BT_WIN`, `BT_LOSE`, `FX_WIN`/`FX_LOSE`-family (`FX_LOSE`, `FX_OK_N`, `FX_BACK_N`), `FIREWORK`, `FIREWORK_N`, `STAREXPLODE`, `PARTICLE` |
| Rewards / rank | `BA_REWARD`, `BA_REWARDS`, `BT_REWARD_BG`, `BT_RANK1_BG`, `BT_RANK2_BG`, `BT_RANK3_BG`, `BT_RU_STAR`, `LEAGUE4`, `LEGUEUP` |
| Stage-specific | **`N003_BG`**, `N003_B01` |
| Fonts | `DEFAULT_FONT`, `EN_BBI`, `EN_EBI`, `NOTOSANS` (via `font=` attributes, 95 occurrences) |
| Motion | `UI_BT_PRE_S`, `UI_BT_PRE_M`, `UI_BT_PRE_L`, `UI_BT_REL_S`, `UI_BT_REL_M`, `UI_BT_REL_L` |

Two entries deserve attention:

- **`N003_BG`** **[RECOVERED]** is named by the battle records. That is the
  *current stage's* background, and it ties the UI layer to the replica's stage
  fixture: the stage is `N003` (`report-009`), and `N003_BG.jet` exists in the
  APK but is **not** served (§3c). **[UNKNOWN]** whether the scene hard-codes it
  or substitutes by `res_prefix`; `res_prefix` on the stage fixture is `ST001`,
  so a mismatch is plausible. This is worth a device trace.
- **`EN_BBI`, `EN_EBI`, `NOTOSANS`** **[RECOVERED]** are the font names in
  `font=` attributes. **[UNKNOWN]** no font file (`.ttf`/`.otf`/`.ttc`) exists
  anywhere in the recovered workspace; fonts ship inside `Font.jet` /
  `DMGFONT.jet` as opaque binary, and the sprite-name search below found no
  literal occurrence. If the font resolver needs a named font it will warn
  (`[AST] The font '%s' was not found.`, `01d67b02`) but that is a warning, not
  an assertion.

### 3b. The sprite names are NOT in the served tree

**[RECOVERED]** The 236 names are sprite identifiers *inside* the resource
packages, not filenames. The `.jet` container here is the `I2` texture-atlas
format — an indexed resource list with no name table:

```
UI_BATTLE.jet  1032471 bytes
  00 00 00 00 00 00 00 00 | 49 1d 9a fd 00 00 00 00 | 00 00 49 32 78 9c ...
                                                        ^^^^^^ "I2" then zlib
```

So a literal grep is the right test for *"is this sprite name knowable at all"*:

```
# no .jet in analysis/extracted/assets or the phone snapshot contains:
UI_IG_CH_BG, IG_GAGE, UI_IG_TIME, AUTO2_T, BT_GAGE, UI_IG_EXIT, IG_SK_P1
```

**[UNKNOWN]** How the client maps `res-name` → atlas entry. It must build a
name→index map at load time from somewhere not yet located (possibly the
`[RSM]` resource-manager state, possibly an index inside the I2 header). Until
that is understood, **it is not possible to statically prove a given sprite is
present in a package.** I am explicitly not claiming the sprites are missing.

This is the main gap and it is where the other agent's device work lands: the
60 `Cannot find the resource` lines are the only reliable existence oracle, and
those must be reconciled with this list. Concretely: cross-check whether any of
the 60 names are in the 236-name list here, and whether the count changes when
the battle scene is actually reached.

### 3c. Packages present in the APK but not served

**[RECOVERED]** The replica currently serves 11 CDN packages plus 8 stage
assets folded into the `E_NEW` tree (AGENTS.md §9). Cross-referencing the 774
`.jet` files in `analysis/extracted/assets`:

| Package | In APK | Served? | Battle relevance |
|---|---|---|---|
| `UI_BATTLE` | yes | folded asset | **battle HUD** |
| `UI_BATTLE2` | yes | folded asset | **battle HUD** |
| `ST001` | yes | folded asset | stage art |
| `M001` | yes | folded asset | monster art |
| `UI_INGAME` | yes | **NO** | **in-battle scene assets** |
| `INGAME_ICON` | yes | **NO** | in-battle icons |
| `INGAME_EFT` | yes | **NO** | in-battle effects |
| `BATTLE_NEW` | yes | **NO** | battle scene |
| `DMGFONT` | yes | **NO** | **damage numbers** |
| `DMGFONT_PREF` | yes | **NO** | damage font preferences |
| `Font` / `FONT_OLD` | yes | **NO** | fonts (`EN_BBI`/`EN_EBI`/`NOTOSANS`) |
| `MOTION` | yes | **NO** | motion clips (`UI_BT_PRE_*`) |
| `GLSL` | yes | **NO** | shaders |
| `ST002`–`ST007`, `ST099`, `ST100` | yes | **NO** | stage art |
| `N003`, `N003_BG` | yes | **NO** | **the live stage's background** |
| `M002`, `M003` | yes | **NO** | monster art |
| `SKILL_EFT` | yes | **NO** | skill effects |
| `N_M_ICON` | yes | **NO** | stage node icons |

**Caveat, stated plainly:** these are APK-bundled assets. The client reads them
from its own package, not from the replica's CDN. So "not served" means *not
deliberately exposed by the replica* — **not** automatically "absent at
runtime". The correct reading is: if the battle scene needs a package that the
original build shipped in the APK base and the replica has replaced/trimmed the
APK base, that is a real gap. Whether the instrumented build ships the full
`assets/` tree is **[UNKNOWN]** from here and is a one-line question for agent E
(`adb shell ls <apk>/assets | wc -l`).

The `E_NEW` / `E_MIDAGE` trees do **not** contain the sprite names either
(`UI_IG_CH_BG`, `IG_GAGE`, `UI_IG_TIME`, `BT_GAGE`, `AUTO2_T` all absent from
`analysis/reconstructed-resources/E_NEW.jet`), consistent with §3b: names are
resolved through an index, not stored as text.

---

## 4. Task 3 — the pre-built seed

### Location

```
instrumentation/assets/instrumented-seed-battle-en-delta-v1/UI_XML_RO.db/
    000005.ldb   3525039   <- base, byte-identical to pristine
    000054.ldb     82831   <- the 55 EN aliases (new SSTable)
    000057.ldb       135   <- empty tombstone flush
    000060.ldb       134   <- empty tombstone flush
    000061.log         0
    CURRENT, LOCK, LOG, LOG.old, MANIFEST-000059
    stamp.json          90
```

### Honest framing: this is a **reproduction**, not a new capability

The installed seed `instrumented-seed-complete-ui-delta-v2` already contained all
55 battle aliases before this work started. So this seed adds **no new key** to
the project. Its value is:

1. **Re-derivable from the pristine source**, not inherited from another
   experiment, so it can be audited.
2. **Independently verified byte-identical** to the working seed (55/55), which
   is a real result: it proves the current battle aliases are a faithful
   mechanical derivation and not an accident of an earlier experiment's ordering.
3. A **battle-only** artifact, so a future battle experiment does not have to
   carry the 45 unrelated `delta-v2` aliases.

**It is not a superset of `delta-v2`.** If agent E installs this *instead of*
`delta-v2`, the mission-map, lobby and dialog aliases go away and the game will
regress to the pre-mission-map state. **This seed is a verification and staging
artifact only.** Say so in the run notes.

### Build

```
python tools/build-battle-en-delta.py --flush \
    --source recovered-assets/phone-2026-09-18/private/files/local/UI_XML_RO.db \
    --dest   instrumentation/assets/instrumented-seed-battle-en-delta-v1/UI_XML_RO.db
```

Safe selective-delta method throughout, per AGENTS.md §7:

- `shutil.copytree` of the pristine directory, then `plyvel` writes **only** the
  55 new `EN/` keys. The source directory is never opened read/write.
- **No compaction.** `compact_range()` is never called.
- **`DEFINE_COLOR` is excluded** by an explicit denylist, and asserted absent
  after the build.
- The base table is **hard-verified byte-identical** at the end of the build; the
  script exits non-zero if it is not.

### Verification (all passing)

```
python tools/verify-ui-delta-seed.py \
    --seed      instrumentation/assets/instrumented-seed-battle-en-delta-v1/UI_XML_RO.db \
    --pristine  recovered-assets/phone-2026-09-18/private/files/local/UI_XML_RO.db \
    --reference instrumentation/assets/instrumented-seed-complete-ui-delta-v2/UI_XML_RO.db
```

```
1. BASE TABLE INTEGRITY
   000005.ldb seed=ebb5f31c282fab94 pristine=ebb5f31c282fab94  OK
   stamp.json preserved: True
2. KEY SET
   pristine=584  seed=639 ;  pristine keys lost: 0 OK ;  keys added: 55
3. SAFETY RULES (AGENTS.md section 7)
   EN/DEFINE_COLOR present: 0  OK (must be 0)
   build sentinels left: 0  OK
4. BATTLE GROUP COVERAGE
   KO battle records 55 / with an EN alias 55 / missing 0
5. PRE-EXISTING RECORDS UNCHANGED
   pre-existing keys whose bytes changed: 0  OK
6. BYTE-IDENTITY vs REFERENCE SEED
   identical=55  differs=0  not-in-reference=0

RESULT: PASS
```

### Two bugs I made and fixed, because they are easy to repeat

Recorded in the tool's docstrings so they are not re-made:

1. **Attribute injected outside the start tag.** The first version inserted
   `file="..."` *after* the closing `>`, producing
   `<comp-motion group="init" loop="t"> file="UI_BT_PRE_S"`. The byte length is
   **identical** to the correct form, so a length comparison against the working
   seed did not catch it — it needed a content diff. `--verify-xml` now
   re-derives the `<comp-motion>` tag statistics and fails the build if any tag
   lacks an in-tag `file=`.
2. **`>` inside an attribute value.** A plain `text.find('>', start)` truncates
   the tag; these records contain vector-style attributes whose values contain
   `>`. The tag scanner is now quote-aware.

Also: the `file=` injection is a **local patch**, not shipped content (§1).
Reproduce the pristine comparison with:

```
python tools/read-leveldb-log.py \
    recovered-assets/phone-2026-09-18/extracted/split_PADResource/assets/UI_XML.db \
    --grep SR_INGAME/UI_HP_N
```

---

## 5. Trap for the next person: opening these seeds rewrites them

**[RECOVERED]** `plyvel.DB()` opens LevelDB read/write. **Iterating the
database is enough** to trigger a background compaction that deletes the base
table:

```
Compacting 2@0 + 0@1 files
Generated table #64@0: 639 keys, 983254 bytes
Compacted 2@0 + 0@1 files => 983254 bytes
Delete type=2 #5                    <- 000005.ldb is gone
```

I hit this twice, and it silently destroyed the base table both times. After it
happens the database is still *functionally* correct (all 639 keys read back
fine), which makes it easy to miss — the damage is only visible by comparing
file names and hashes against the pristine source.

### 5a. Incident: I damaged an existing seed, and restored it

**This must be reported rather than quietly fixed.** I was explicitly told not
to modify existing seed directories. I did, twice, by opening
`instrumentation/assets/instrumented-seed-complete-ui-delta-v2` with `plyvel`
while comparing it against my own build.

What happened:

1. The compaction above ran against the **reference seed**, and silently
   **dropped two keys**:
   - `EN/SR_FLOW/7_UI_FL7`
   - `EN/SR_GLOBAL/0_GL_PROGRESS/0_PROGRESS`

   682 keys read back instead of 684. The data was still *usable* — which is
   exactly why it nearly went unnoticed. It was only caught because I had taken
   a key dump (`684 keys`) before starting and diffed against it afterwards.
   **Lesson: take a key-count/hash manifest before touching anything.**

2. My first repair attempt made it worse: I rewrote `CURRENT` with a CRLF
   (`b'MANIFEST-000047\r\n'`), which made the database **unopenable** —
   `IO error: ... The filename, directory name or volume label syntax is
   incorrect`. LevelDB requires a bare LF in `CURRENT`.

**Repair, verified.** `tools/restore-ui-seed-keys.py` was written to do this
properly:

```
python tools/restore-ui-seed-keys.py \
    --seed  instrumentation/assets/instrumented-seed-complete-ui-delta-v2/UI_XML_RO.db \
    --donor instrumentation/assets/instrumented-seed-complete-ui/UI_XML_RO.db \
    --key   EN/SR_FLOW/7_UI_FL7 \
    --key   EN/SR_GLOBAL/0_GL_PROGRESS/0_PROGRESS
```

- `CURRENT` normalised back to `b'MANIFEST-000047\n'`.
- The two keys restored from
  `instrumentation/assets/instrumented-seed-complete-ui`, after confirming that
  **five independent backups agree byte-for-byte** on both records
  (`7_UI_FL7` = 1392 bytes, sha256 `366f8a1e43abcbb2…`;
  `0_PROGRESS` = 1881 bytes, sha256 `24fe313e6c5c1ae6…`). Neither contains a
  `file="UI_BT_PRE_*"` injection, so they were verbatim aliases — consistent
  with the pristine-vs-patched comparison in §1.
- Post-repair diff against the pre-incident dump: **684 keys, 0 lost, 0 gained.**

**Residual risk, stated plainly.** The seed's *table layout* is not the original
(its SSTables were compacted and two new ones appended), so it is not
byte-identical to what it was at session start. The *content* is verified
identical key-for-key and byte-for-byte. I judged restoring content to be
correct and re-deriving the layout to be riskier; if the parent agent prefers
pristine history, this seed can be rebuilt from
`instrumentation/assets/instrumented-seed-complete-ui` (which still has the full
1154-key content) or from the build scripts.

Consequences for the next person:

- **Never open a seed with `plyvel` in place.** Copy first, or use
  `tools/verify-ui-delta-seed.py`, which works on a throwaway copy.
- **`CURRENT` must end in a bare LF.** Any tool rewriting it should write bytes,
  not text-mode lines.
- This is a **tooling** artefact, not necessarily a client problem: the native
  engine opens LevelDB through its own GMLevelDB, and the AGENTS.md §7 concern
  is about the *native downloader* replacing the open base table. Whether the
  native path would compact the same way is **[UNKNOWN]** and untested here.
- It does explain why the prior-art seeds in `analysis/instrumented-ui-seed-*`
  have differing table layouts for what should be equivalent content.

---

## 6. Task 4 — is UI/resources a second blocker?

### Verdict: **the UI key layer is not a blocker. The resource layer is a moderate, server-only risk.**

**UI records: not a blocker. [RECOVERED]**
All 55 battle records have `EN` aliases, byte-identical between the installed
seed and an independent rebuild. Zero battle records are missing from the
database entirely. The mission-map blocker from AGENTS.md §7 has **no analogue**
here, because someone already fixed it. The battle scene should get past record
lookup.

**Resources: cannot rule out. Moderate likelihood. [UNKNOWN]**
Concretely:

- What is *known*: the battle records name 236 sprites; the replica serves 8
  stage assets; the APK carries at least 13 further battle-relevant packages
  that the replica does not expose, including `UI_INGAME`, `INGAME_ICON` and
  `DMGFONT`.
- What is *not* known: whether `res-name` resolution even needs the replica to
  serve anything for those sprites (§3b), and whether the instrumented build
  ships the full APK `assets/` tree.
- The asymmetry that keeps me from calling it safe: the battle scene has **never
  opened** on this replica, so there is zero empirical evidence either way. The
  village and mission map both worked once their UI records were seeded, which
  is weak positive evidence that record presence was the binding constraint
  there — but the battle scene additionally loads *sprites*, and the mission map
  largely did not.

**Expected failure mode, if it does fail:** non-fatal. A missing sprite produces
`Cannot Read Atlas File %s` / `Sprite '%s' loading was failed`
(`01d93890`), not an assertion. So a resource gap would most likely produce a
**visually broken but running** battle scene — which is a good outcome, and
distinguishable in a screenshot. A resource gap is therefore unlikely to be the
thing that re-kills the client.

**The more likely thing to kill the client remains the `MakeCamp` crash itself**
— an empty `ref_id` in `ACTOR_INFO` (report-009 §0: `list` is five empty
strings), which is a data problem in the card/mirage fixtures, not a resource
one.

### Cheapest next probes, in order

1. **One screenshot at the moment `MakeCamp` is entered.** If the scene opens
   with missing art, the UI layer is fine and the resource question is
   cosmetic. This single observation resolves most of §3.
2. **Reconcile the 60 `Cannot find the resource` names against the 236-name
   list** in §3a. If they are disjoint, they are not battle-related at all and
   the battle resource layer is clean.
3. **Check the instrumented APK's `assets/` count.** One `adb shell ls`, tells
   you whether the APK-bundled battle packages are present at runtime.
4. If and only if 1–3 show a real gap, add the missing packages to
   `BLUSTONE_RESOURCE_ASSET_NAMES`. That is a **server-only** change — no client
   rebuild, no APK release.

---

## 7. What remains unknown

| # | Question | Why it is open | Who can close it |
|---|---|---|---|
| 1 | How does `res-name` map to an atlas entry? | `I2` containers have no name table; no literal sprite name appears in any `.jet` | Needs native decompile (`CRMResourceMgr4::LoadResourceFromFile`, `0x003ab8e8`) or a device trace |
| 2 | Are the 236 sprites present at runtime? | Follows from 1. No static oracle exists | The agent enumerating the 60 `Cannot find the resource` lines |
| 3 | Does the instrumented APK ship the full `assets/` tree? | Cannot check without adb | agent E, one command |
| 4 | Does the battle scene need `N003_BG` or a `res_prefix`-derived name? | `N003_BG` is hard-named in the records but the stage fixture says `res_prefix: ST001` | Device trace, or the stage-scene loader |
| 5 | Where do `EN_BBI` / `EN_EBI` / `NOTOSANS` resolve? | No font file recovered; fonts are opaque inside `Font.jet` | Follows from 1 |
| 6 | Is there a shipped EN battle layout at all? | Evidence says **no** — only a KO layout plus local patches (§1) | Probably closed: treat as unrecoverable |
| 7 | Would the *native* LevelDB open compact the seed like plyvel does? | plyvel behaviour is not the native behaviour | Requires a device test |
| 8 | Are the 25 non-literal battle records actually requested? | They ship in the group; individual request sites unknown | Only a device trace can confirm |

Items 1–3 are the ones that matter for the battle opening. None of them needs a
client rebuild.

---

## 8. Files added

New, none overwriting existing work:

| Path | Purpose |
|---|---|
| `analysis/battle-scene/ui-record-key-table.tsv` | The 55-row key table, machine-readable |
| `analysis/research/battle-scene-ui-resources.md` | This document |
| `instrumentation/assets/instrumented-seed-battle-en-delta-v1/` | The verified battle-only EN delta seed |
| `tools/build-battle-en-delta.py` | Builds the seed (safe selective delta) |
| `tools/verify-ui-delta-seed.py` | Verifies a seed **without** modifying it |
| `tools/list-ui-db-keys.py` | Lists every key in a UI_XML_RO database |
| `tools/map-ui-records-to-strings.py` | DB record → native string table cross-reference |
| `tools/find-missing-ui-records.py` | Native string → DB record (the reverse direction) |
| `tools/dump-ui-record.py` | Dumps one record's XML and referenced tokens |
| `tools/collect-ui-resource-refs.py` | Collects the `res-name` / `file` tokens of a record set |
| `tools/resolve-ui-record-deps.py` | Battle record dependency closure |
| `tools/check-text-global-coverage.py` | `text-global` id coverage against `UI_JSON.db` |
| `tools/read-leveldb-log.py` | Decodes an unrecovered LevelDB `.log` / WriteBatch |
| `tools/scan-leveldb-log-keys.py` | Key-only scan of the same |
| `tools/list-jet-entries.py` | Lists entries in a `.jet` package |
| `tools/restore-ui-seed-keys.py` | Restores keys lost from a seed; normalises `CURRENT` |

`server-ts/`, `analysis/ghidra-project/`, `analysis/ghidra-scripts/`, existing
`analysis/*.txt`, `analysis/testing/`, other `analysis/research/` files and
`instrumentation/src/` were not modified. Ghidra, adb, Docker and the server
were not run. No git operations. No APK rebuild or install.