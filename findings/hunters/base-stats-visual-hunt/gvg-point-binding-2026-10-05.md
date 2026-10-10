# Binding the `CONTENTS15_8` 12-numeral point table to the recovered `/gvg/*` schema (2026-10-05)

**Read-only.** No `server-ts` file, fixture, test, state file, APK, seed, LevelDB,
catalogue or emulator was created, modified, opened or executed. No Ghidra project
access (parent-owned, locked). Exactly one file is written: this one.
`polluted-observations.md` is deliberately **not** appended — the parent mirrors.

**No `/gvg/*` handler was implemented**, per instruction.

**Zero coverage credit.** Strict base-stat coverage is unchanged: heroes 1/113,
accessories 1/100, monsters 0/22 (`coverage.md`). Guild Blitz scoring is not a hero,
jewel, accessory or monster stat.

**Result in one line:** the schema side is now complete enough to say *which of the
twelve numerals are point magnitudes and which are counts*, `multi` is **proved to be
a multiplier applied client-side as `val × multi`**, the documented `×2` for rearmost
areas maps onto `multi` far better than the earlier `2250 = 450 × 5`, and **450
appears in no artefact at all** — but **no numeral is bound to a specific
`POINT_INFO_TYPE` ordinal except the two attack-count ones**, and no magnitude is
recovered.

---

## 0. Sources, and three corrections that must be read before the tables

| source | what it contributes |
|---|---|
| [`gvg-reference-2026-10-05.md`](gvg-reference-2026-10-05.md) | `/gvg/GetRef` key list, `BATTLE_INFO` shape, the `point_id`/`val`/`multi` triple, the `.text`/`.rodata` spans it assumed |
| [`blitz-search-consumers-2026-10-05.md`](blitz-search-consumers-2026-10-05.md) | field dictionary, `CONTENTS15_8` row mapping, the `2250 = 450 × 5` observation |
| [`help-2_8-sweep-2026-10-05.md`](help-2_8-sweep-2026-10-05.md) | the verbatim five-locale `CONTENTS15_8` text, incl. JA/SC/TC multiplicative notation |
| [`point-info-type-2026-10-05.md`](point-info-type-2026-10-05.md) | `POINT_INFO_TYPE` = 5 values 1–5, values 2/3 named, `point_id` read as an unclamped generic number |
| `analysis/extracted/lib/armeabi-v7a/libnative_core.so` | original ARM32 library, 35 445 748 B. **Reads only** — no copy written, no patch applied |
| `analysis/recovered-data/leveldb-tables/all-tables.json` | recovered LevelDB export; `UI_TEXT_RO` GVG rows only |
| `tools/python-venv` capstone 5.0.7 | Thumb-2 disassembly |

### 0.1 CORRECTION — `.text` does **not** start at 0

`gvg-reference` §0 and `point-info-type` §"Method" both treat a single
`PT_LOAD (VA 0, offset 0)` as making `VMA == file offset` for everything they read.
That is true and the addresses they quote are correct **for `.rodata`**, but the
section table, re-parsed this pass, says:

```
.text                addr=0x00612cc0  off=0x00612cc0  size=0x015c1a38  end=0x01bd46f8
.rodata              addr=0x01d52940  off=0x01d52940  size=0x003ba754  end=0x0210d094
.data.rel.ro.local   addr=0x0210e550  off=0x0210d550  size=0x000263e0
.data.rel.ro         addr=0x02134930  off=0x02133930  size=0x00075f24
```

So **only `0x00612cc0 … 0x01bd46f8` is code.** Everything below `0x00612cc0` is
`.dynstr` / `.hash` / `.gnu.hash` / `.dynsym` — data. Any numeric sweep that treats
"VA < `.rodata`" as "in `.text`" will manufacture hits out of hash tables. This
matters for §1.5 below.

Addresses in this file are **ELF VAs**, file offset identical for `.text`/`.rodata`.
Per `AGENTS.md` §16.7 item 3, **Ghidra = ELF + `0x10000`**.

### 0.2 Method — how the `point_detail` row was re-read

Same pairing-free Thumb PIC idiom the sibling passes used, with two fixes:

1. `ldr Rt,[pc,#imm8]` slot = `Align(va+4, 4) + 4*imm8`; the slot word is a
   **pre-bias addend**; the target is `slot_word + (add_va + 4)`.
2. The `add rX,pc` was **not** required to be in the same register as the `ldr`'s
   destination. The real code interleaves unrelated work between the two
   (`0xaafb3c add r4,sp,#0x58` sits between `ldr` and `add`). Requiring register
   equality returned **zero** hits on a function known to contain eleven string
   keys; dropping it and instead requiring the resolved address to be a
   NUL-terminated, NUL-preceded printable run inside `.rodata` returned **27**
   correct keys.

Validation was run against known ground truth first: the sweep reproduces `gvg`
(`0x1d6952e`), `min_entry_cnt`, all nine `*_dtm`, `min_cp`, `max_cp`, `inf_reward`,
`reward`, `point`, `val`, `id`, `camp` — all independently confirmed by direct byte
search — plus false positives that were rejected because the resolved run is not
printable (`'ParseCompMotion'`, `'dir'`, `'type:'` at the same ldr are literal-pool
collisions, not keys).

---

# SECTION 1 — PURE: the recovered schema, and the twelve numerals side by side

Pure = verbatim bytes, verbatim disassembly, verbatim shipped strings, verified
section bounds. No balance claim, no era inference, no fixture conclusion.

## 1.1 `/gvg/GetRef` — the reference shape, re-verified

`BATTLE_INFO::parse`, ELF `0x00a93260`, keys in code order (this pass's sweep,
`0xa93260–0xa93fe8`):

| load site | key | ELF `.rodata` |
|---|---|---|
| `0xa93280` | `gvg` | `0x1d6952e` |
| `0xa93280` | `min_entry_cnt` | `0x1d69532` |
| `0xa9328c` | `id` | `0x1d576c3` |
| `0xa93280` | `teaser_begin_dtm` | `0x1d69540` |
| `0xa9337a` | `register_begin_dtm` | `0x1d69551` |
| `0xa933c2` | `matching_begin_dtm` | `0x1d69564` |
| `0xa9340a` | `deploy_begin_dtm` | `0x1d69577` |
| `0xa93452` | `combat_begin_dtm` | `0x1d69588` |
| `0xa9349a` | `calc_begin_dtm` | `0x1d69599` |
| `0xa934e2` | `result_begin_dtm` | `0x1d695a8` |
| `0xa9352a` | `finish_dtm` | `0x1d695b9` |
| `0xa935a4` | `next_gvg_dtm` | `0x1d695c4` |
| `0xa93636` | `reward` | `0x1d5edc1` |
| `0xa936c4` | `min_cp` | `0x1d695d1` |
| `0xa936d6` | `max_cp` | `0x1d695d8` |
| `0xa936c4` | `inf_reward` | `0x1d695df` |
| `0xa93b4e` | `point` | `0x1d55900` |
| `0xa93ba6` | `val` | `0x1d543ff` |
| `0xa93bac` | `id` | `0x1d576c3` |
| `0xa93cbe` | `camp` | `0x1d64aa7` |

Corroborates `gvg-reference` §1.3 field for field. Two additions:

- **`min_cp` occurs TWICE — once at the `gvg` level and once per camp row — while
  `max_cp` occurs only once.** Re-scanned `_CAMP::parse` (ELF `0x00aa2d7c`, size
  `0x3e8`) this pass: its keys resolve to `min_cp`, `camp_id`, `name`, `link_camp`
  and **`max_cp` does not appear**. Byte-search confirms exactly one `max_cp`
  literal in the whole library, at `0x1d695d8`, consumed only by
  `BATTLE_INFO::parse`.

  **So the two are NOT a symmetric pair.** There is a gvg-level Strength band
  `[min_cp, max_cp]`, and a separate per-camp Strength floor `min_cp` with no
  ceiling. This asymmetry is directly relevant to §2.7: a per-camp `min_cp` with no
  `max_cp` sibling is a much better structural fit for a **per-hunter deployment
  floor** than the gvg-level band is, because a band implies a global limit and the
  shipped 4000 sentence states no upper bound. Still not proven (§2.7).
- **`'max_cp'` is loaded into a different register than `'min_cp'`/`'inf_reward'`**
  (`r0` vs `r1`) and `'%s Defence Card Duplication'` resolves from the same pool
  region — i.e. the assertion sits in the same translation unit, not in a distant
  one. No semantic conclusion drawn.

## 1.2 THE reference `point[]` row has **no `multi` and no `point_id`**

This is the single most load-bearing negative in this file, and it is new.

```
BATTLE_INFO::parse  (0x00a93260 … 0x00a93fe8)
  'point'  0x1d55900  loaded at 0xa93b4e
  'val'    0x1d543ff  loaded at 0xa93ba6   (into r0)
  'id'     0x1d576c3  loaded at 0xa93bac   (into r6)
```

A targeted re-scan of the whole `BATTLE_INFO::parse` body for `multi`, `point_id`
and `point_detail` returns **zero hits**. The reference table is therefore a flat
**two-field** row:

```jsonc
"point": [ { "id": <n>, "val": <n> }, … ]      // reference magnitudes
"camp":  [ { "min_cp": …, "camp_id": …, "name": …, "link_camp": … }, … ]
```

**Consequence:** the multiplier exists **only in the per-camp point log**, never in
the reference table. The two shapes are different tables with different jobs:

| | shape | role |
|---|---|---|
| `/gvg/GetRef` → `gvg.point[]` | `{id, val}` | **per-event magnitude table**, one row per scoring event |
| point-log → `point_detail[]` | `{point_id, val, multi}` | **per-camp itemisation**, one row per contribution |

## 1.3 The `point_detail` row — `multi` is a multiplier, PROVED

`point-info-type` §2.2 left this explicitly open: *"`val`'s role relative to `multi`
(base amount × multiplier?) is not established — that is an inference, and it is
withheld."* **It is now established.** Verbatim, at ELF `0x00aafb66`–`0x00aafc9e`:

```asm
00aafb66  mov   r0, r4                  ; the array iterator
00aafb68  bl    #0x71aff0               ; nlohmann::detail::iter_impl::operator*
00aafb6c  mov   r1, sb                  ; sb  == "point_id"
00aafb6e  mov   r5, r0                  ; r5 == the row
00aafb70  bl    #0x7830f8               ; nlohmann::json::operator[](const char*)
00aafb74  ldrb  r1, [r0]
00aafb76  subs  r1, #3
00aafb78  cmp   r1, #4
00aafb7a  bhi   #0xaafbb4
00aafb7c  tbb   [pc, r1]                ; <-- type-tag dispatch, 5 cases
   …  (5 targets, all converge at 0xaafbb6) …
00aafbb4  movs  r4, #0                  ; DEFAULT -> r4 = 0

00aafbb6  mov   r0, r5                  ; the row again
00aafbb8  mov   r1, sl                  ; sl  == "val"
00aafbba  bl    #0x7830f8
00aafbbe  ldrb  r1, [r0]
00aafbc0  subs  r1, #3
00aafbc2  cmp   r1, #4
00aafbc4  bhi   #0xaafc2a
00aafbc6  addw  r2, pc, #0xc
00aafbca  tbb   [r2, r1]
   …  (5 targets, all converge at 0xaafc2c) …
00aafc2a  movs  r6, #0                  ; DEFAULT -> r6 = 0

00aafc2c  mov   r0, r5                  ; the row again
00aafc2e  mov   r1, r8                  ; r8  == "multi"
00aafc30  bl    #0x7830f8
00aafc34  ldrb  r1, [r0]
00aafc36  subs  r1, #3
00aafc38  cmp   r1, #4
00aafc3a  bhi   #0xaafc74
00aafc3c  tbb   [pc, r1]
   …  (5 targets, all converge at 0xaafc76) …
00aafc74  movs  r0, #0                  ; DEFAULT -> r0 = 0

00aafc76  mul   r5, r0, r6              ; <<<< r5 = multi x val
00aafc7a  movs  r0, #0x10
00aafc7c  blx   #0xdfb280               ; operator new(16)
00aafc80  ldr   r1, [sp, #0x34]
00aafc82  str   r4, [r0, #8]            ; node+0x08 = point_id
00aafc84  str   r1, [r0, #4]            ; node+0x04 = prev
00aafc86  str   r5, [r0, #0xc]          ; node+0x0c = val * multi   <<<<
00aafc88  ldr.w r1, [fp, #0x198]
00aafc8c  str   r1, [r0]                ; node+0x00 = next
00aafc8e  str   r0, [r1, #4]            ; prev->next = node
00aafc90  ldr.w r1, [fp, #0x1a0]
00aafc94  str.w r0, [fp, #0x198]
00aafc98  adds  r0, r1, #1
00aafc9a  str.w r0, [fp, #0x1a0]        ; ++size
```

Literal resolution re-verified independently (§0.2): `sb` = `0x1d6985b`
`point_id`, `sl` = `0x1d543ff` `val`, `r8` = `0x1d69864` `multi`, resolved from pool
slots `0xaafbf0`, `0xaafbf4`, `0xaafbf8` read straight out of `.rodata`.

### 1.3.1 Four consequences, each of them PURE

**(a) `multi` is a multiplier on `val`, not an independent field.**
`MULS r5, r0, r6` with `r0` = the `multi` conversion and `r6` = the `val`
conversion. The value the client keeps is the **product**.

**(b) The stored element is a 16-byte `std::list` node whose payload at `+8/+0xc`
is `(point_id, val × multi)`.** `push_back` + size counter are visible. That layout
is `std::list<std::pair<A,int>>` and the only consumer with that exact signature in
`.dynsym` is
`CSRPopUpGuildBattleWin::SetPointListData(const std::list<std::pair<POINT_INFO_TYPE,int>>&)`
(ELF `0x00c79844`). **Not claimed as a proven link** — the caller edge was not traced
(this pass used no decompiler, per `AGENTS.md` §16.7 lesson 7) — but no other
`std::pair` candidate has this layout, and it closes the *shape* half of what
`point-info-type` §3 left open.

**(c) A missing or non-numeric `multi` silently zeroes the row.** All three
conversions have a `movs rX, #0` default. `multi` absent ⇒ `r0 = 0` ⇒
`0 × val = 0`. **`multi` is not optional in a fixture, and there is no default-1
path.** This is the single most dangerous item for anyone implementing
`/gvg/GetCampClearPointLog`: a row that looks correct renders as **0 points** with no
assertion, no log and no visible error.

**(d) The type tolerance is wider than "number".** Each of the three reads is a
nlohmann **type-tag** dispatch (`subs r1,#3 / cmp r1,#4 / tbb`), i.e. types 3–7 =
string, boolean, integer, unsigned, float. Each has a real conversion (a
`blx`-based string→number path, `ldrb` for boolean, `ldr` for the integer types,
`vldr`+`vcvt` for float). A string `"5"` is accepted. Types outside 3–7
(null/object/array) hit the `= 0` default.

## 1.4 The reference table and the log are **different id spaces**

| | id field | range known? |
|---|---|---|
| `/gvg/GetRef` → `point[].id` | `id` | **no clamp located**, generic number read |
| point log → `point_detail[].point_id` | `point_id` | read as a generic number, **no client-side clamp** (`point-info-type` §1.6); the 1–5 bound is a *rendering* bound in `CSRPopUpGuildBattleWin::SetData`'s `tbb`, not a parse contract |

Both are read tolerantly, neither is validated. The reference table may therefore
carry **more than five** rows without any client complaint. `CONTENTS15_8` describes
**eight** scoring events. **Eight magnitudes cannot be distributed one-to-one over
five enumerators** — so either the reference id space is wider than
`POINT_INFO_TYPE`, or several events share an ordinal and are separated by
`multi`. Both remain open; §2.2 argues for the second.

## 1.5 Numeral-constant sweep, now correctly bounded

Restricting literal-pool loads to real code (`0x00612cc0 … 0x01bd46f8`) and requiring
the loaded word to equal the numeral:

| numeral | `ldr`-loaded constant sites in `.text` |
|---|---|
| 5 | **0** |
| 25 | 1 — `0x1bc6f66`, and its pool word resolves to non-printable bytes in `.text`; **not** a scoring constant |
| 50 | **0** |
| 150 | **0** |
| 450 | **0** |
| 2250 | **0** |
| 3000 | **0** |
| 4000 | **0** |
| 100000 | **0** |

The `2250`, `3000`, `4000`, `100000` and `450` hits reported by an unbounded sweep
earlier in this session were all below `0x00612cc0`, i.e. inside `.dynstr`/`.hash`
(§0.1). **The negative in `gvg-reference` §1.11 and `blitz-search-consumers` §1.8
stands, and is now bounded to code rather than asserted over the whole file.**

A separate `MOVW/MOVT` immediate-pair sweep for the same set also returns zero
pairs, and Thumb-1 `CMP #imm8` is only usable for 5/25/50 (whose counts are 343 / 43
/ 111 across all of `.text` — i.e. meaningless without context). **No balance
constant for any of the twelve numerals exists client-side.**

## 1.6 `cp` is Strength; points are a different dimension

`CARD::parse` (ELF `0x00aa4214`) and `CARD_SUMMARY::parse` read `cp`;
`CSRPopUpGuildBattleCard::SetCombatPoint(int)` (ELF `0x0087fd9c`) takes it;
`PLAY_DATA::parse` reads `total_cp`; `INFO::parse` reads `total_cp` and `point`.

The shipped strings pin the vocabulary: `GVG_회원별 전투력` = "Total Strength",
`GVG_팀 전투력` = "Team Strength", `GVG_필요 참가인원` = "Least Needed Members".
**`cp` ≡ 전투력 ≡ "Strength"**, and it is a **different dimension** from
`승점` ≡ points (`offense_point`, `defense_point`, `total_point`, `point_list`,
`point`, `point_detail`). Any binding that reads a Strength numeral as a point, or
vice versa, is dimensionally wrong.

**A live confusion hazard, flagged:** `/lobby/GetGuildInfo`'s guild INFO cluster
contains **`fc_point_limit`**, and `analysis/systems/guild.md` §6.3 proposes
`fc_point_limit: 4000` as a fixture (guide-derived). That `4000` is a **Fight Club**
point limit. It is numerically identical to the GVG **Strength** floor and belongs to
a different system with a different dimension. Do not let the two meet.

## 1.7 The twelve numerals, verbatim, in five locales

`CONTENTS15_8` `desc1`, markup stripped. **Verbatim shipped bytes.**

```text
KO   승점 획득 세부사항
     - 방어팀 배치 시 : 150점
     - 방어팀 격파 시 : 25점
     - 첫번째 공격으로 방어팀 격파 시 : 50점 추가
     - 두번째 공격으로 방어팀 격파 시 : 25점 추가
     - 방어팀 격파 후 살아있는 팀원 수 만큼 : 5점 추가
     - 공격 시작 시 비워둔 팀원 수 만큼 : 5점 추가
     - 지역 1개 점령 시 : 2250점(최후방의 3개 지역은 2배)
     - 점령한 지역에 배치되어있던 방어팀 수 만큼 : 50점 추가

EN   Winning Point Details
     - Defense Team Deployment Points : 150 Points
     - Victory over Defense Team Points : 25 Points
     - Points for Victory over Defense Team on the 1st Attack : Plus 50 Points
     - Points for Victory over Defense Team on the 2nd Attack : Plus 25 Points
     - Points for Each Surviving Hunter after Victory over Defense Team : Plus 5 Points
     - Points for Each Undeployed Unit during the Attack : Plus 5 Points
     - Points for 1 Occupied Area: 2250 Points (Double Points for 3 Final Defense Line Areas)
     - Points for Each Deployed Defense Team in the Occupied Area : Plus 50 Points

JA   防衛チーム配置 : 150点
     防衛チーム撃破 : 25点
     1回目の攻撃で防衛チーム撃破：50点追加
     2回目の攻撃で防衛チーム撃破：25点追加
     防衛チーム撃破後の生存ハンター数 : x5点追加
     攻撃開始時の空席ハンター数 : x5点追加
     1エリア占領 : 2250点 (最後方の3ヶ所は2倍)
     占領したエリアに配置されていた防衛チーム数 : x50点追加

SC   配置防御队伍时：150分
     击溃防御队伍时：25分
     首次出击击溃防御队伍时：追加50分
     二次出击击溃防御队伍时：追加25分
     击溃防御队伍后：5分x幸存猎人数
     开始出击时：5分x空余猎人数
     占领一个地区时：2250分（最终3个地区2倍积分）
     占领地区原有防御队伍数：追加x50分

TC   (same numerals as SC)
```

**Two locale facts, both load-bearing, both shipped bytes:**

- **Exactly three rows are written multiplicatively in JA/SC/TC and flat in EN:**
  per-surviving-hunter (`x5点`), per-undeployed (`x5点` / `5分x…`), and
  per-deployed-defense-team (`x50点` / `x50分`). EN renders all three as
  "Plus N Points".
- **The area row is written flat in all five locales** — `2250点`,
  `1エリア占領 : 2250点` — with the ×2 as a **parenthetical**, not as a
  multiplicative prefix.

## 1.8 The twelve numerals, decomposed by *role* (not yet by field)

Reading §1.7 as a table rather than a number list gives a structure that the raw
numeral sequence `150, 25, 1, 50, 2, 25, 5, 5, 1, 2250, 3, 50` hides:

| # | numeral | appears in | grammatical role | is it a point magnitude? |
|---|---|---|---|---|
| 1 | **150** | `방어팀 배치 시 : 150점` | flat amount for one event | **yes** |
| 2 | **25** | `방어팀 격파 시 : 25점` | flat amount for one event | **yes** |
| 3 | **1** | `첫번째 공격으로 …` | **ordinal: which attack** | **no — a discriminator** |
| 4 | **50** | `… 1st Attack : Plus 50` | amount, gated by #3 | **yes** |
| 5 | **2** | `두번째 공격으로 …` | **ordinal: which attack** | **no — a discriminator** |
| 6 | **25** | `… 2nd Attack : Plus 25` | amount, gated by #5 | **yes** |
| 7 | **5** | `… 만큼 : 5점 추가` (per surviving hunter) | **rate × count** | **yes, as a rate** |
| 8 | **5** | `… 만큼 : 5점 추가` (per undeployed unit) | **rate × count** | **yes, as a rate** |
| 9 | **1** | `지역 1개 점령 시` | **count: how many areas** | **no — a multiplier slot** |
| 10 | **2250** | `: 2250점` | rate per area × count #9 | **yes, as a rate** |
| 11 | **3** | `최후방의 3개 지역은 2배` | **count: how many areas are special** | **no — a spatial set size** |
| 12 | **50** | `… 만큼 : 50점 추가` (per deployed team) | **rate × count** | **yes, as a rate** |

**Result: 8 point magnitudes (150, 25, 50, 25, 5, 5, 2250, 50) and 4 non-magnitudes
(1, 2, 1, 3).** §2 binds each of the eight, and §2.6 addresses the four.

---

# SECTION 2 — UNPURE: each binding as an explicit hypothesis

Every row below is inference. Each carries what supports it and what would falsify
it. **None may become a fixture without a local-policy label.**

Support legend: **S** = shipped-text evidence, **B** = native-binary evidence
(this pass or a cited sibling pass), **L** = logic/arithmetic only.

## 2.1 The two attack-count ordinals — the only ordinals that are *named*

| numeral | bound to | support | status |
|---|---|---|---|
| **1** (1st attack) | `POINT_INFO_TYPE = 2` | **B** the value-2 branch of `CSRPopUpGuildBattleWin::SetData` (ELF `0x00c79e06`) fetches `GVG_한번의 공격으로 격퇴` = "defeated in **one** attack" (ELF `0x01d721e9`, byte-verified this pass). **S** the help row is literally "1st Attack". **S** EN renders it "First Attempt" (`UI_TEXT_RO`) | **SUPPORTED** |
| **2** (2nd attack) | `POINT_INFO_TYPE = 3` | **B** value-3 branch (`0x00c79e84`) fetches `GVG_두번의 공격으로 격퇴` = "defeated in **two** attacks" (ELF `0x01d7220b`, byte-verified this pass). **S** "2nd Attack" / "Second Attempt" | **SUPPORTED** |

This is the **only** numeral→ordinal binding in the table that is supported rather
than hypothesised, and it is supported by *two independent shipped corpora agreeing
with the native switch*.

**Remaining gap, stated plainly:** the ordinal is bound to the **enum**, not to the
**wire**. `point_id` is read with no clamp (`point-info-type` §1.6), so "a `point_id`
of `2` on the wire means first-attempt" rests on the server and the original data
using the same numbering as the display enum. The *shape* link (payload pair at
node `+8/+0xc`) is strong (§1.3.1b); the *numbering* link is untraced.

**Falsifier:** a captured `/gvg/GetCampClearPointLog` response in which a
first-attempt clear carries a `point_id` other than `2`. Or a decompiled trace of the
store into the `BATTLE_INFO` `POINT_INFO_TYPE` field showing a remap.

## 2.2 The eight magnitudes — one ordinal per event, five ordinals available

| # | event | numeral | `point_id` hypothesis | `val` | `multi` hypothesis | support | status |
|---|---|---|---|---|---|---|---|
| 1 | Defense-team deployment | 150 | 1 or 4 or 5 | 150 | 1 per deployment | **B** `gvg_get_deploy_point` field exists (ELF `0x1d6925e`); **S** flat in all 5 locales ⇒ no count multiplier | **HYPOTHESIS** (ordinal unassigned) |
| 2 | Defense-team clear | 25 | 1 or 4 or 5 | 25 | 1 per clear | **S** flat in all 5 locales | **HYPOTHESIS** (ordinal unassigned) |
| 3 | + bonus, cleared on 1st attack | 50 | **2** | 50 | 1 | **B**+**S** §2.1 | **ordinal SUPPORTED**, magnitude **HYPOTHESIS** |
| 4 | + bonus, cleared on 2nd attack | 25 | **3** | 25 | 1 | **B**+**S** §2.1 | **ordinal SUPPORTED**, magnitude **HYPOTHESIS** |
| 5 | per surviving hunter | 5 | 1 / 4 / 5 | 5 | **survivor count** | **B** `multi` is a multiplier (§1.3); **S** JA `生存ハンター数 : x5点` is multiplicative ⇒ a count is present; **B** `survive_cnt` (`0x01d796bc`) models the count | **HYPOTHESIS**, but the **rate × count shape is SUPPORTED** |
| 6 | per undeployed unit | 5 | 1 / 4 / 5 | 5 | **undeployed count** | **S** `空席ハンター数 : x5点`; **B** `deploy_cnt` (`0x01d796b1`) / `max_deck_cnt` (`0x01d796c8`) | **HYPOTHESIS**, shape **SUPPORTED** |
| 7 | per occupied area | 2250 | 1 / 4 / 5 | 2250 | **occupied-area count** (1 in the example, #9) | **S** flat in all 5 locales ⇒ `multi` = 1 in the common case; **B** `multi` exists as the only multiplier mechanism | **HYPOTHESIS**, shape **SUPPORTED** |
| 8 | per deployed defense team in the occupied area | 50 | 1 / 4 / 5 | 50 | **deployed-team count** | **S** `占領したエリアに配置されていた防衛チーム数 : x50点` multiplicative; **B** `max_deck_cnt`, `point_list` | **HYPOTHESIS**, shape **SUPPORTED** |

**The counting problem, stated honestly.** Eight events, five enumerators. Rows 3
and 4 consume ordinals 2 and 3. Rows 1, 2, 5, 6, 7, 8 must fit ordinals **1, 4, 5**
— three slots for six events. So **either**:

- **(i)** several events share an ordinal and are distinguished only by `multi`
  (which would need six different `multi` semantics under three ids — no
  discriminator left), **or**
- **(ii)** the reference `point[].id` space is **wider than `POINT_INFO_TYPE`**, and
  the 1–5 enum is a *result-popup display grouping* rather than the reference key.

**(ii) is strongly preferred** and is a correction to `blitz-search-consumers` §3.1's
framing. Three independent reasons:

1. The reference row is `{id, val}` with **no `multi`** (§1.2). If one `id` had to
   carry two events, the reference row could not express the difference at all — the
   magnitude table would be self-contradictory.
2. `point_id` is read with **no clamp** (§1.4), so a wider reference id space is
   perfectly legal on the wire.
3. `CSRPopUpGuildBattleWin::SetData`'s `tbb` bounds **rendering** only, and values
   ≥ 6 silently store nothing (`0x00c79f3c`) rather than asserting — a display
   filter, not a schema limit.

**Falsifier for (ii):** a decompiled `CSRPopUpGuildBattleWin::RefreshPoint` (ELF
`0x00c7838c`) showing the display id used to **index** the reference table, which
would force the two id spaces together.

**Falsifier for every row in this table:** any captured real
`/gvg/GetCampClearPointLog` payload. One capture resolves rows 1, 2, 5, 6, 7, 8
simultaneously, because it contains both `point_id` and the `val × multi` product
that was actually scored.

## 2.3 `multi` semantics, restated as an implementation contract

Pure fact (§1.3): stored magnitude = `val × multi`. Impure consequences:

1. **A server that pre-multiplies and sends `multi: 1` renders correctly.**
   **A server that pre-multiplies and omits `multi` renders 0.** There is no
   default-1.
2. **`multi` is the natural home for the three per-count rows**, and the JA/SC/TC
   `x5点` / `x50分` notation is (on this reading) a faithful rendering of a `multi`
   field that EN drops — which **upgrades** `blitz-search-consumers` §3.4 item 3 from
   "should be upgraded" to "is now structurally supported".
3. **`multi` is also the only candidate for the rearmost-area ×2** (§2.5).
4. **A `multi` of `0` is indistinguishable from an absent `multi`.** A server that
   wants "no bonus this event" must omit the whole row, not send `multi: 0`.

**Falsifier:** a payload where `val` and `multi` are both non-trivial, the rendered
point equals `val` alone, and `multi ≠ 1`. That would mean `multi` is a *display*
factor applied elsewhere, not the row multiplier.

## 2.4 Is `multi` a multiplier *on `val`* or an independent field?

**Answer: a multiplier, proved at `0x00aafc76`.** §1.3(a) is not an interpretation —
`MULS r5, r0, r6` with register provenance verified from the three literal loads.

The practical implication is that **the two fields are not independent choices**: a
fixture author choosing `val` has already chosen `multi = total / val`, and must
choose `val` and `multi` such that the product is an integer if the original point
values are integers. `val = 5, multi = 3` and `val = 15, multi = 1` are the *same*
row as far as the client is concerned, and nothing on the wire distinguishes them.

**Open:** whether the server sends the raw rate + count (so `val` is a rate) or the
pre-multiplied total with `multi: 1`. The help text's multiplicative notation in
three locales suggests **rate + count**, but that is display copy, not protocol.

## 2.5 The `2250` numeral — is `450 × 5` real, and does `×5` mean `multi`?

This is where the earlier lane's arithmetic is corrected.

**Is 450 present anywhere? No.**

| location | result |
|---|---|
| `CONTENTS15_8`, all five locales | absent — the only numerals are the twelve listed in §1.8 |
| the other 94 `CONTENTS` records, both help corpora | absent — `help-2_8-sweep` §2.1 tested `'450'` → **0 records** |
| `libnative_core.so` as a GVG scoring constant | absent — **0** literal-pool loads in `.text` (§1.5) |
| `LEVELING.jet`, the 774 JET packages, the LevelDB tables | absent (`blitz-search-consumers` §3.3) |

**450 has no source in any artefact this project holds.**

**Does the ×5 correspond to `multi`? Almost certainly not.** Three reasons:

1. **`multi` is a *count* of the event, and the documented multiplier on the area row
   is 2, not 5.** `2250 × 2 = 4500` for rearmost areas; the help text says so in all
   five locales.
2. **The area row is written flat in every locale** (§1.7). The three rows that *are*
   multiplicative are exactly the three per-count rows. If the area row carried
   `multi = 5`, JA/SC/TC would have written `2250点 x5` or `5箇所…2250点`. They wrote
   a bare `2250点`.
3. **`multi` needs an integer count with a referent.** "5" has no referent on the
   area row: the camp roster is **ten** camps (`my_101..110`, ten `GVG_N호 캠프`
   rows), and the help says the rearmost set is **three**. Neither is 5.

**Where 5 *does* occur is telling.** `5` is the rate for two other events
(rows 5 and 6). The coincidence `2250 = 450 × 5` therefore reuses a numeral that
belongs to two *different* events. That is arithmetic coincidence dressed as a rule.

**The better reading, and the one this file supports:**

> **Area row: `val = 2250`, `multi = 1` for a normal area, `multi = 2` for one of
> the three rearmost areas.** The client then stores `2250` and `4500`
> respectively, matching the shipped "Double Points for 3 Final Defense Line Areas".

This is **HYPOTHESIS**, and it is the single most consequential one in the file,
because it turns the rearmost bonus from an unexplained server-side rule into a
field the schema can express. It also predicts something checkable: **a rearmost
camp's `point_detail` row carries `multi = 2`, not a doubled `val`.**

**Falsifier:** a captured rearmost-camp `point_detail` row with `val = 4500, multi = 1`
(or `val = 2250` and no `multi`). That would mean the doubling is applied server-side
to `val` and `multi` is reserved for unit counts.

**Falsifier for `450 × 5` specifically:** any artefact anywhere containing `450` as a
GVG point value. The KO help sweep already tested the string and found none.

## 2.6 The four non-magnitude numerals

| numeral | role | bound to | status |
|---|---|---|---|
| **1** (row 3) | 1st-attack ordinal | `POINT_INFO_TYPE = 2` | **SUPPORTED** (§2.1) |
| **2** (row 5) | 2nd-attack ordinal | `POINT_INFO_TYPE = 3` | **SUPPORTED** (§2.1) |
| **1** (row 9) | the count slot of the area row | `multi` = number of occupied areas | **HYPOTHESIS**, well supported by §1.7's flat notation + §1.3's proven multiplier |
| **3** (row 11) | size of the rearmost set | **no candidate found** | **UNBOUND** |

**Numeral `3` is the table's genuine loose end.** It is a count of *areas*, i.e. a
property of the **camp list**, not of any single `point_detail` row. Candidates
examined and rejected:

- `multi` — rejected: §2.5; the documented factor is 2, and `multi` cannot express
  "3 of my 10 rows behave differently".
- `camp_id` / `link_camp` — **unrejected, unresolved.** `_CAMP` carries exactly
  `{min_cp, camp_id, name, link_camp}`; a rear-area flag would plausibly live in
  `camp_id` ordering or `link_camp`. **Not established.** `_CAMP::parse` was not
  re-disassembled this pass.
- `inf_gvg` / `enemy_camp_id` — not examined.

**Falsifier:** a decompiled `_CAMP::parse` showing no boolean/ordinal rear-area
field, plus a server that nonetheless doubles some areas ⇒ the rearmost set is
server-only and unrepresentable in the recovered schema. That would be a genuine
schema gap worth recording.

## 2.7 Could the 4000 Strength floor and the 3000 point floor be `min_cp`?

Both questions collapse into one distinction, which §1.6 settles: **`cp` is
Strength (전투력); points are 승점. They are different dimensions, and the two
numerals are in different dimensions.**

| numeral | dimension | is `min_cp` a candidate? | reasoning |
|---|---|---|---|
| **4000** | **Strength** (per hunter) | **dimensionally YES; the per-camp slot is now the structurally better candidate — still UNRESOLVED** | `min_cp` is a CP/Strength field, so the *dimension* matches. §1.1 newly establishes the asymmetry: `min_cp` exists at the gvg level **and** per camp row, while `max_cp` exists **only** at the gvg level. So the per-camp `min_cp` is a **floor with no ceiling**, which fits a deployment eligibility rule ("4000 or more", no stated maximum) far better than a band would. Against that: the shipped sentence is **per hunter** at deployment (`GVG_4000이하_헌터`, EN byte-verified from `UI_TEXT_RO`), and a camp is occupied by **four** defenders (`card_1..card_4`), so a per-camp floor is plausibly 4 × 4000 = 16000, not 4000 — and **16000 was searched and is absent** from the binary's code (§1.5). A per-hunter floor has **no recovered field**: `CARD::parse` reads `cp` but no per-card minimum exists. Finally the `.rodata` key is literally named **`GVG_4000…`** — a *localization key* — and a value baked into a key name is evidence the client hard-codes 4000 with no server field involved. **Status: better-motivated than before, still not established; the "baked into the key name" reading remains the strongest single argument against any `min_cp` home.** |
| **3000** | **points** (guild total) | **NO — dimensionally excluded** | 3000 gates a *winning-points* total. Every `min_cp`/`max_cp` in the recovered vocabulary is a Strength field (§1.6). Reading 3000 into `min_cp` would put a points threshold in a Strength field. **Rejected outright.** |

**Where could 3000 live instead?** No candidate in the recovered key set. `reward`
is consumed as an opaque whole value with **no child keys looked up** in
`BATTLE_INFO::parse` (`gvg-reference` §1.11) — so `reward` or `inf_reward` is the only
structural hiding place, and their sub-shapes are **[UNKNOWN-1]**. A `point_limit`
field may exist inside `reward` and simply never be read by this parser (the parser
stores the object; a consumer elsewhere may index into it).

**Falsifier for the 4000-as-`min_cp` reading:** a captured `/gvg/GetRef` whose
`min_cp` is **not** 4000, or whose `min_cp` is 4 × 4000 = 16000 (a *team* floor)
rather than 4000. Both would show the field models a different granularity than the
per-hunter sentence. Note that 16000 has no client-side constant (§1.5), so a
server-supplied 16000 remains possible — but it would be *invisible* to the binary,
which is exactly why this cannot be settled from the client alone.

**Falsifier for the 3000 reading:** any recovered key whose name pairs `point` with
`limit`/`min`/`floor` — e.g. a `point_limit` sibling of the Fight Club
`fc_point_limit` (§1.6). That would be a decisive, cheap finding.

## 2.8 Net binding ledger

| # | numeral | role | ordinal | magnitude | status |
|---|---|---|---|---|---|
| 1 | 150 | magnitude | — | 150 | hypothesis (ordinal unassigned) |
| 2 | 25 | magnitude | — | 25 | hypothesis (ordinal unassigned) |
| 3 | **1** | **ordinal** | **`POINT_INFO_TYPE = 2`** | — | **SUPPORTED** |
| 4 | 50 | magnitude | **`2`** | 50 | ordinal supported; magnitude hypothesis |
| 5 | **2** | **ordinal** | **`POINT_INFO_TYPE = 3`** | — | **SUPPORTED** |
| 6 | 25 | magnitude | **`3`** | 25 | ordinal supported; magnitude hypothesis |
| 7 | 5 | rate × count | — | 5 | rate/count shape **SUPPORTED**, ordinal hypothesis |
| 8 | 5 | rate × count | — | 5 | rate/count shape **SUPPORTED**, ordinal hypothesis |
| 9 | **1** | **count slot** | — | — | hypothesis (`multi` = area count) |
| 10 | 2250 | rate × count | — | 2250 | rate/count shape **SUPPORTED**, ordinal hypothesis |
| 11 | **3** | **spatial set size** | — | — | **UNBOUND — the loose end** |
| 12 | 50 | rate × count | — | 50 | rate/count shape **SUPPORTED**, ordinal hypothesis |

**Two ordinals supported. Eight magnitudes shaped but unassigned. Four numerals
correctly reclassified as non-magnitudes. One (3) unbound. Zero values recovered.**

---

# SECTION 3 — Direct answers to the four questions

**1. The 2250 numeral; is 450 present, and does ×5 correspond to `multi`?**
**450 is present in nothing** — not the five help locales, not the other 94
`CONTENTS` records of either corpus, not the binary as a scoring constant (0
literal-pool loads in `.text`), not any JET package, not LevelDB. The `×5` is **not**
`multi`: the documented multiplier on that row is **2**, the row is written **flat**
in all five locales while the three genuinely multiplicative rows are written
`x5点`/`x50分`, and `multi` must be a count of a single event — for which "5" has no
referent on a ten-camp map whose rearmost set is three. The supported alternative:
**`val = 2250`, `multi = 1` normally and `multi = 2` on a rearmost area**, giving
2250 / 4500 as the client computes them (§2.5). `450 × 5` survives as an arithmetic
coincidence that reuses a numeral belonging to two other events.

**2. The two named enum values; do any numerals describe an attack-count reward,
and which?**
**Yes — exactly two: numeral 50 (paired with the ordinal "1st Attack") and numeral
25 (paired with "2nd Attack").** Those are the two attack-count bonuses. The numerals
**1** and **2** themselves are **not** point values; they are the attack-count
**discriminators**, and they are the only part of the twelve numerals bound to a
native ordinal: `POINT_INFO_TYPE = 2` → `GVG_한번의 공격으로 격퇴` ("defeated in
one attack") and `= 3` → `GVG_두번의 공격으로 격퇴` ("defeated in two attacks"), both
byte-verified in `.rodata` and both cross-attested by the help table and the
`UI_TEXT_RO` English "First Attempt" / "Second Attempt". Note that 25 and 50 each
appear **twice** in the twelve (rows 2/6 and rows 4/12), so the numeral alone does not
identify an event — `point_id` does.

**3. Is `multi` a multiplier on `val` or an independent field?**
**A multiplier, and this is now proved rather than inferred.** ELF `0x00aafc76` is
`mul r5, r0, r6`, where `r0` is the conversion of the row's `multi` and `r6` is the
conversion of the row's `val`; the product is stored at node `+0xc` alongside
`point_id` at node `+8` in a 16-byte `std::list` node. This closes
`point-info-type` §2.2, which explicitly withheld this. **Implication for reading
the table:** a `point_detail` row is *not* two independent quantities — it is a
`(kind, rate × count)` product, and `multi` has **no default of 1** (all three
conversions default to `0`), so an omitted `multi` silently zeroes the row with no
assertion and no log. `val = 5, multi = 3` and `val = 15, multi = 1` are
indistinguishable on the wire.

**4. Could the 4000 Strength floor and the 3000 point floor be `min_cp` values?**
**4000: dimensionally yes, and the newly-found per-camp `min_cp` is a structurally
better candidate than before — but still UNRESOLVED, with the strongest single
argument still pointing away.**
**3000: no — dimensionally excluded.** `cp` is Strength (전투력); 3000 gates a
*points* total and cannot be a CP field. For 4000, §1.1 newly establishes that
`min_cp` appears at the `gvg` level **and** per camp row while `max_cp` appears
**only** at the `gvg` level — so the per-camp `min_cp` is an unbounded floor, which
matches "4000 **or more**, no stated maximum" better than a band would. Against it:
the sentence is **per hunter**, a camp holds **four** defenders so a per-camp floor
would be 16000 rather than 4000 (and 16000 has no client constant, §1.5), and —
strongest of all — the `.rodata` key is literally named **`GVG_4000이하_헌터`**, so
the numeral is baked into a **localization key name**, which is what a client-side
hard-coded check looks like. Separately: `/lobby/GetGuildInfo` carries
**`fc_point_limit`** and `analysis/systems/guild.md` §6.3 proposes
`fc_point_limit: 4000` as a fixture. That is a **Fight Club** value, numerically
identical to the GVG Strength floor and semantically unrelated. Flagged as a live
confusion hazard (§1.6).

---

# SECTION 4 — Limits, retractions, and what was NOT done

## 4.1 What this pass changes

1. **`multi` semantics: CLOSED.** `mul r5, r0, r6` at `0x00aafc76` proves
   `multiplier`, superseding `point-info-type` §2.2's explicit withholding.
2. **`val × multi` with no default-1: NEW, and fixture-critical.** Three new
   implementation requirements.
3. **`/gvg/GetRef`'s `point[]` row is `{id, val}` with no `multi` and no
   `point_id`: NEW.** The reference is a flat magnitude table; the multiplier lives
   only in the per-camp log. This is what forces the eight-events-vs-five-enumerators
   reading.
4. **`2250 = 450 × 5` downgraded** from an arithmetic observation to an explicitly
   unsupported rule, with a better-supported `multi = 1 / 2` alternative (§2.5).
5. **The twelve numerals reclassified:** 8 magnitudes + 4 non-magnitudes (§1.8).
6. **The ordinal count problem named**, with the preferred resolution (reference id
   space wider than the display enum) and its falsifier (§2.2).
7. **The constant-absence negative re-established over code**, not over the whole
   file, after finding that `.text` begins at `0x00612cc0` (§0.1, §1.5).
8. **`min_cp` is not symmetric with `max_cp`: NEW.** `min_cp` is read twice (gvg
   level **and** per camp row); `max_cp` exists once, at the gvg level only. So the
   gvg-level pair is a Strength **band** and the camp-level `min_cp` is an
   **unbounded floor**. This revises the §2.7 assessment of the 4000 Strength floor
   in the *favour* of a `min_cp` home while leaving it unproven (§1.1, §2.7).
9. **Own-draft error caught and fixed:** §2.2 originally cited
   `gvg_get_deploy_point` at "ELF `0x01d7925e`" — a **Ghidra** address carried over
   from `blitz-search-consumers` §1.3 without the §0.2 subtraction. Byte search puts
   the literal at **ELF `0x1d6925e`**. Corrected in place. Recorded because it is
   exactly the `AGENTS.md` §16.7 lesson-3 trap this project keeps re-earning, and
   this time it survived into a *new* file rather than a correction section.

## 4.2 Explicit unknowns after this pass

- **Ordinals for six of eight events.** No evidence assigns rows 1, 2, 5, 6, 7, 8 to
  `POINT_INFO_TYPE` 1, 4 or 5 — or confirms that they must be.
- **All eight magnitudes remain server-side.** Nothing here may become a fixture.
- **Numeral `3` (rearmost set size) is unbound** (§2.6). `_CAMP::parse` was not
  re-disassembled this pass; `camp_id` / `link_camp` were not tested as a flag.
- **`reward` / `inf_reward` sub-shapes**, and therefore any home for the 3000-point
  floor, remain **[UNKNOWN-1]**.
- **Whether the server sends rate+count or pre-multiplied total+`multi:1`** is not
  determined. The JA/SC/TC multiplicative notation favours rate+count; that is
  display copy.
- **The caller edge from the parsed `point_detail` list to
  `SetPointListData` was not traced.** No decompiler was used. The node layout is
  consistent with the mangled type and with no competing candidate, but "consistent
  with" is not "traced".
- **`point_id` on the wire vs the display enum numbering** remains an untraced
  assumption, as in `point-info-type` §3.

## 4.3 What this pass did NOT do

- **No Ghidra run, no Ghidra project access.** Parent-owned and locked. Every
  function-level claim is from capstone on the original `.so`, or from verified
  section bounds and literal resolution. Per `AGENTS.md` §16.7 lesson 7, raw
  instructions were used throughout, not the decompiler.
- **No decompiler was used at all**, so the two remaining callers named in §4.2
  (`CSRPopUpGuildBattleWin::RefreshPoint` at ELF `0x00c7838c`, `_CAMP::parse` at ELF
  `0x00aa2d7c`) were not attempted.
- **No `/gvg/*` handler implemented.** No `server-ts` file read, written or executed;
  no test run; no build; no server start; no state file opened.
- **No APK, seed, LevelDB or JET opened or modified.** No emulator, VM, physical
  phone or release operation.
- **No catalogue edit, no fixture edit.**
- **`polluted-observations.md` NOT appended** — the parent mirrors.
- **Zero coverage credit.** Heroes 1/113, accessories 1/100, monsters 0/22.

## 4.4 Cheapest next steps, in order

1. **Re-read `_CAMP::parse` (`0x00aa2d7c`)** looking for a rear-area flag among
   `camp_id` / `link_camp` / `inf_gvg`. This is the only route to numeral `3`, the
   one unbound numeral. A capstone sweep of that function with the §0.2 resolver is
   cheap and does not need Ghidra.
2. **Any real `/gvg/GetCampClearPointLog` capture** resolves six of the eight
   magnitudes at once, because the payload carries both `point_id` and the scored
   `val × multi`.
3. **`CSRPopUpGuildBattleWin::RefreshPoint` (`0x00c7838c`)** settles whether the
   display id indexes the reference table — i.e. §2.2's (ii) vs (i).
4. **A search for a `point_limit`-shaped key** beside `fc_point_limit` would settle
   where 3000 lives (§2.7).