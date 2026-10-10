# GVG numeral 3, `camp_id` / `link_camp`, and the eight-vs-five gap (2026-10-06)

**Read-only native reverse engineering.** No Ghidra project was opened. No
`server-ts` file, fixture, test, state file, APK, seed, LevelDB, JET, catalogue,
emulator, VM, physical phone or release was created, modified, opened or
executed. `analysis/extracted/lib/armeabi-v7a/libnative_core.so` was read only,
never copied, patched or moved. **`polluted-observations.md` was deliberately NOT
appended** — the parent mirrors. Exactly one file is written: this one.

**Zero coverage credit.** Strict base-stat coverage is unchanged: heroes 1/113,
accessories 1/100, monsters 0/22 (`coverage.md`). Guild Blitz scoring is not a
hero, jewel, accessory or monster stat.

**Binary integrity, verified before and after this pass:**

```
analysis/extracted/lib/armeabi-v7a/libnative_core.so
sha256 = c4646ac3817b0008b6ea387fde9c8279fd439343ccc272acdc5883fab9d00eec
size   = 35 445 748 bytes     (unchanged)
```

**Result in one line:** **numeral `3` is not bindable — proved so, not merely
unsolved**; `link_camp` is **client-inert** (exactly two consumers in the whole
22.8 MB of code, both parse/dump) and `camp_id` is an **opaque string map key with
zero comparisons**; and the "eight datetimes vs five point enumerators" gap is a
**false premise**, because there are **nine** datetimes driving **ten phase values
0–9**, and the phase clock is **never joined** to a point id.

---

## 0. Sources, method, and the conventions this pass held to

| source | identity |
|---|---|
| `analysis/extracted/lib/armeabi-v7a/libnative_core.so` | original ARM32 library, 35 445 748 B, read only |
| `tools/python-venv` capstone 5.0.7 | Thumb-2 disassembly (`CS_MODE_THUMB`) |
| `llvm-objdump` NDK 29.0.14206865, `--triple=thumbv7-linux-gnueabihf` | corroboration of decoding **only** |
| [`gvg-point-binding-2026-10-05.md`](gvg-point-binding-2026-10-05.md) | the twelve numerals, `multi` = multiplier proof, the open numeral 3 |
| [`gvg-reference-2026-10-05.md`](gvg-reference-2026-10-05.md) | `/gvg/*` key lists, `_CAMP`, the 19 routes |
| [`address-convention-2026-10-05.md`](address-convention-2026-10-05.md) | C1/C3/C8 conventions, applied throughout |

### 0.1 Every address in this file is an ELF VA

Section headers were read, not guessed (`e_shoff = 0x021cd744`, `e_shnum = 30`):

```
.text    addr=0x00612cc0  off=0x00612cc0  size=0x015c1a38  end=0x01bd46f8   (22 813 240 bytes)
.rodata  addr=0x01d52940  off=0x01d52940  size=0x003ba754  end=0x0210d094
```

Every `.text` scan in this pass is bounded to `0x00612cc0 … 0x01bd46f8`.
Ghidra image addr = ELF VA + `0x10000`; the project TSVs are in image space, so
no TSV address is used here except as a cross-check with `− 0x10000`.
`llvm-objdump`'s labels are ELF VAs with no bias and were therefore **never** used
to corroborate a TSV convention — per `address-convention-2026-10-05.md` §4b, that
is the exact trap that kept the original defect alive.

### 0.2 Relocation fact, re-measured rather than inherited

```
R_ARM_RELATIVE entries (r_info & 0xff == 23) = 128 620
targets by section: .data.rel.ro 103052 | .data.rel.ro.local 10991 | .got 7785
                    .data 6393 | .init_array 397 | .fini_array 2
```

**Zero** in `.rodata`, **zero** in `.text`. `.rodata` literal-pool slots are
therefore genuinely unrelocated and `add Rd, pc` is the only bias source. All
string resolution below is read straight out of the on-disk file.

### 0.3 The literal resolver, and the two bugs this pass had to fix first

The pairing rule is the project's: a literal is materialised by the **immediately
preceding** `ldr Rd, [pc, #imm]`, relocated by `add Rd, pc`, and the pool word is a
**pre-bias addend**:

```
slot   = ((ldr_va & ~3) + 4 + disp_bytes) & ~3
target = LE32(slot) + (add_va + 4)
```

Two defects in my own first implementation produced **zero** hits on ground truth
and are recorded because both were silent:

1. **`disp` is already in bytes.** capstone reports `mem.disp` in bytes for both
   the Thumb-1 (`0x4800`) and Thumb-2 (`0xF8D0`) encodings. Multiplying by 4 again
   sent every slot 4·N bytes wrong.
2. **`add Rd, pc` is `0x4478 | Rd` in this toolchain**, not `0x18F8 | Rd`. Verified
   by two independent decoders on 24 validated pairs (5× `0x4478`/r0, 18× `0x4479`/r1,
   1× `0x447a`/r2) and confirmed directly:
   ```
   a93280: 49ba   ldr  r1, [pc, #0x2e8]   -> slot 0xa9356c, addend 0x012d62a4
   a93286: 4479   add  r1, pc              -> 0x012d62a4 + 0xa9328a = 0x01d6952e = "gvg"  OK
   ```
   (`llvm-objdump --triple=thumbv7-linux-gnueabihf` prints `a93286: 4479  add r1, pc`,
   agreeing with capstone.)

A third defect was caught **before** any result was trusted: a backward walk that
**breaks on any 32-bit instruction** produces false negatives. Real site:
```
0xaa57f0  ldr   r1, [pc, #0x22c]     <- "min_cp"
0xaa57f2  strd  r0, r4, [sp, #0x68]   <- 32-bit, interposed
0xaa5800  add   r1, pc
```
The production census therefore walks **over** 32-bit instructions and, for every
reported site, **re-decodes the gap with capstone** and asserts that nothing between
the `ldr` and the `add` writes the destination register. A reported site is
additionally an exact 32-bit `addend + add_va + 4 == target` match, so a chance
false positive is not a practical concern.

**Self-test before use** — the validated resolver reproduces prior ground truth
exactly:

```
BATTLE_INFO::parse   18 keys: gvg, id, min_entry_cnt, teaser_begin_dtm, register_begin_dtm,
                     matching_begin_dtm, deploy_begin_dtm, combat_begin_dtm, calc_begin_dtm,
                     result_begin_dtm, finish_dtm, next_gvg_dtm, reward, min_cp, max_cp
                     (+ point / val / id / camp at 0xa93b4e, 0xa93ba6, 0xa93bac, 0xa93cbe)
_CAMP::parse          4 keys: min_cp, camp_id, name, link_camp   (+ the non-key " name" at 0xaa2e02)
_CAMP::dump           4 keys: camp_id, min_cp, name, link_camp
```

`resolve-literals-segment-aware.py` was **not** used as a key-list generator; the
`operator[]` call and the containing parser were followed at every site quoted.

### 0.4 Census stability

Every count in §1.4 is **identical** at backward depths 14, 30 and 60 halfwords,
so the counts are not artefacts of the walk limit:

```
back=14/30/60 -> name 58 | camp_id 11 | link_camp 2 | min_cp 3 | max_cp 1 | gvg 1
                 point_detail 1 | point_id 1 | multi 1 | "101" 1 | "103" 1
                 fc_point_limit 5 | fc_point 2 | gvg_win_cnt 2 | gvg_inf_win_cnt 2
```

---

# SECTION 1 — PURE: field bindings, with ELF addresses and instruction evidence

Pure = verbatim bytes, verbatim disassembly, verbatim shipped strings, section
bounds read from the section table, census method self-tested. No balance claim,
no era inference, no fixture conclusion.

## 1.1 CORRECTION that closes a route: `to_string<POINT_INFO_TYPE>` is a **numeric** formatter, not an enumerator table

`gvg-reference-2026-10-05.md` §1.11 and `gvg-point-binding-2026-10-05.md` §4.2
both propose reading `POINT_INFO_TYPE`'s enumerator names out of
`_ZSt9to_string<CSRGuildBattleMgr::BATTLE_INFO::POINT_INFO_TYPE>`
(**ELF `0x0087f9d0`**, size `0x130`). **That route is now permanently closed.**

The body's five pool words are at `0x0087faec … 0x0087fafc`; the `add Rd, pc` sites
are `0x0087f9e6/0x0087f9e8/0x0087fa14/0x0087fa18/0x0087fa4c`. The first resolves to
`__stack_chk_guard` (ELF `0x021aafe4`; `.rel.dyn` type 21 = `R_ARM_GLOB_DAT`,
symbol 21 = `__stack_chk_guard` — verified this pass, not assumed). The remaining
four resolve into `.got` and then into `.data.rel.ro` RTTI objects:

```
GOT 0x021ab0f8 -> relocated 0x021450e4 -> points at type_info name "CActorStateHandler"
GOT 0x021ab0fc -> relocated 0x021450bc -> object with vtable [0x008ea08d,0x008ea0b1,0x008ea0dd,0x008ea1cd]
GOT 0x021ab100 -> relocated 0x02145190 -> vtable [0x008ea1d9,0x008ea1fd,0x008ea229,0x008ea309]
GOT 0x021ab104 -> relocated 0x0214513c -> vtable [0x008ea349,0x008ea34d,0x008ea36d,...]
```

Neighbouring RTTI name strings in `.data.rel.ro` are `CActorStateHandler`,
`CMImageNode`, `CMoveTo`, `_CCatch`, `CMPool<...>` — **nothing GVG-related**. What
the function actually calls is libc++'s arithmetic `to_string`:

```
0x0087fa70  bl  #0x006d4c10   std::__ndk1::basic_ostream<char>::operator<<(int)
0x0087fa78  bl  #0x006d55bc   std::__ndk1::basic_stringbuf<char>::str()
```

i.e. `ostringstream << value`, which prints a **decimal number**. There is no
enumerator-name table anywhere in this function.

**Consequence (PURE):** `POINT_INFO_TYPE`'s *names* are not recoverable from this
binary by that route. Only the `1..5` **range** is recoverable, and that comes from
the renderer's `tbb` (§1.9), not from this symbol.

## 1.2 `_CAMP` — the complete four-field layout, from `dump` with `parse` as cross-check

`CSRGuildBattleMgr::BATTLE_INFO::_CAMP::dump` (ELF `0x00aa5768`, size `0x2c4`) is
the clean side: one key load per field, each reading `this` directly (`sb = this`,
`r8 = this`):

```
00aa5794  movs r0, #3                ; build a 12-byte JSON value
00aa57a8  add.w r1, r8, #0x10       ; <-- source of the FIRST key emitted
00aa57ac  bl  #0x006c7efc           ;   string copy-construct
00aa57b0  ldr  r1, [pc, #0x268]     ; <-- "camp_id"   (ELF 0x01d6943e)
00aa57ec  ldr.w r0, [r8]           ; <-- source of the SECOND key: this+0x00
00aa57f0  ldr  r1, [pc, #0x22c]     ; <-- "min_cp"   (ELF 0x01d695d1)
00aa5840  add.w r1, r8, #4         ; <-- source of the THIRD key: this+0x04
00aa584e  ldr  r1, [pc, #0x1d4]     ; <-- "name"     (ELF 0x01d53176)
00aa5890  ldrd r5, sl, [r8, #0x28]  ; <-- source of the FOURTH key: this+0x28 (begin/end)
00aa58d2  adds r5, #0xc             ; <-- stride 0x0C per element
00aa5906  ldr  r1, [pc, #0x19e]     ; <-- "link_camp"(ELF 0x01d69683)
```

| `_CAMP` offset | key | C++ type | evidence for the type |
|---|---|---|---|
| `+0x00` | `min_cp` | `uint32_t` | parse `0x00aa2d96` → nlohmann type-tag `tbb` dispatch (`subs r1,#3 / cmp r1,#4 / tbb` at `0xaa2dac`), default `mov.w sl,#0` at `0xaa2dbc`, then `str.w sl,[r4]` at `0xaa2f70` |
| `+0x04` | `name` | `std::string` (**derived**, not sent) | parse builds it at `sp+0x58` by `bl 0x006caa2c` (`0xaa2e12`) with `r2` = the literal `" name"` (ELF `0x01d6967d`, loaded `0xaa2e02`); the raw `camp_id` is what gets concatenated |
| `+0x10` | `camp_id` | `std::string` | parse `0x00aa2dec` → `from_json<nlohmann::json::string_t>` (ELF `0x00718b08`) at `0xaa2dfe`, then `std::string::assign` (`0x006c82f4`) into `this+0x10` |
| `+0x28` | `link_camp` | `std::vector<T>`, **stride 0x0C** | parse `0x00aa2ede` → `from_json<string_t>` then an assign at `sp+0x38`; parse's own element loop `0x00aa3000 ldrd r0,r1,[r4,#0x2c]` / `0x00aa3014 adds r0,#0xc` / `0x00aa301e str r0,[r4,#0x2c]` |

**Exactly four JSON keys. No fifth field, no boolean, no ordinal, no row count.**
`gvg-reference-2026-10-05.md` §1.4 and `gvg-point-binding-2026-10-05.md` §1.1 are
confirmed field-for-field from a second, independent function.

**This meets the falsifier that `gvg-point-binding-2026-10-05.md` §2.6 wrote for
itself** ("a decompiled `_CAMP::parse` showing no boolean/ordinal rear-area field")
— with the stronger negative that the dump agrees, so it is not a parser
oversight.

## 1.3 What `_CAMP::parse` does with `camp_id` and `" name"` — verbatim

```
00aa2dec  ldr  r1, [pc, #0x364]   ; "camp_id"  -> 0x01d6943e
00aa2df2  bl   #0x007830f8         ; nlohmann::json::operator[](const char*) const
00aa2df6  strd r6, r6, [sp, #0x68] ; zero a 12-byte string at sp+0x68
00aa2dfe  bl   #0x00718b08         ; from_json<json::string_t>(sp+0x68)   <- RAW camp_id
00aa2e02  ldr  r2, [pc, #0x354]   ; " name"    -> 0x01d6967d   (r2 = 3rd argument)
00aa2e06  add.w r8, sp, #0x58
00aa2e0a  add.w fp, sp, #0x68
00aa2e0e  mov  r0, r8              ; dest   = sp+0x58
00aa2e10  mov  r1, fp              ; source = sp+0x68 (the raw camp_id)
00aa2e12  bl   #0x006caa2c         ; dest = f(camp_id, " name")  <- DERIVED name
```

`0x006caa2c` has no covering defined symbol, but it is called as a 3-argument
`(char* dest, const char* src, const char* suffix)` helper here and in
`QueryCampStatus` (§1.5), where the same shape is unambiguously
`a + b`. **Confirmed reading:** `name` is a client-side derived display/lookup
label built from `camp_id` plus a literal space. It is a `dump()` output, not a
wire input — `gvg-reference` §1.4's warning that `" name"` must never be sent as a
key is reinforced.

## 1.4 **`camp_id` and `link_camp` consumer census over all of `.text` — the load-bearing result**

| literal | ELF `.rodata` | **sites in 22 813 240 bytes of `.text`** | sites |
|---|---|---|---|
| **`link_camp`** | `0x01d69683` | `0x00aa2ede` `_CAMP::parse`, `0x00aa5906` `_CAMP::dump` | **2** |
| **`camp_id`** | `0x01d6943e` | 6 request builders + 2 parsers + 2 dumps + 1 unnamed parser | **11** |
| `min_cp` | `0x01d695d1` | `0x00a936c4` gvg-level, `0x00aa2d96` per-camp, `0x00aa57f0` dump | **3** |
| `max_cp` | `0x01d695d8` | `0x00a936d6` gvg-level only | **1** |
| `point_id` | `0x01d6985b` | `0x00aafb3a` point-log parser | **1** |
| `multi` | `0x01d69864` | `0x00aafb48` point-log parser | **1** |
| `point_detail` | `0x01d6984e` | `0x00aafa6a` point-log parser | **1** |

### `link_camp` — **client-inert.** This is the answer to Task 2.

Its only two consumers are the parse that stores it and the dump that re-emits it.
**Zero** other sites in the entire binary read the literal, and (per §1.2) nothing
else reads `_CAMP+0x28`. A field that is written once, re-serialised once, and
**never consulted** cannot drive any client behaviour. `link_camp` therefore
**cannot** be the home for numeral `3` or any other numeral, and it cannot be the
rear-area marker the prior pass left open.

Its type is a `std::vector` of 0x0C-stride elements populated from a JSON **string**
(`from_json<json::string_t>` at `0x00aa2dfe`… applied to `link_camp` at
`0x00aa2ede`), i.e. a **list of strings**, not an index, not a rank, not a flag.
The natural reading is "camps linked to this one" — useful to a **server** drawing
attack adjacency, invisible to the client. Recorded as reading, not as meaning.

### `camp_id` — an **opaque string map key**, never compared

All 11 sites, with the owning function read from `.dynsym` directly:

| site | owner |
|---|---|
| `0x00a99a3a` | `CSRGuildBattleMgr::RequestCombatReady` `@0x00a99894` +0x1a6 — **request** |
| `0x00a9abdc` | `RequestGetCombatLog` `@0x00a9aa38` +0x1a4 — **request** |
| `0x00a9bbc4` | `RequestEnemyCampDetail` `@0x00a9ba70` +0x154 — **request** |
| `0x00a9c9ca` | `RequestDefenderList` `@0x00a9c868` +0x162 — **request** |
| `0x00a9d834` | `RequestDefenderReserve` `@0x00a9d6d0` +0x164 — **request** |
| `0x00a9e948` | `RequestDeployDefender` `@0x00a9e754` +0x1f4 — **request** |
| `0x00aa2dec` | `_CAMP::parse` — read into a `std::string` |
| `0x00aa3f5c` | `PLAY_DATA::parse` — read into a `std::string` |
| `0x00aa4b88` | `PLAY_DATA::dump` — re-emit |
| `0x00aa57b0` | `_CAMP::dump` — re-emit |
| `0x00ab307e` | unnamed GVG response parser (also reads `point_list` `0x01d696ec`, `total_point` `0x01d696f7`, `pvid`, `reg_dtm`, `nickname`) — re-emit |

**Every consumer treats it as an opaque `std::string`.** The two decision functions
that a positional rule would live in are pure tree lookups with **no arithmetic on
the id**:

- `CSRGuildBattleMgr::GetCampActionStatus(const std::string&)` (ELF `0x00aa1540`,
  668 B): no string literal at all; returns a status in `{0,1,2,3}` chosen purely by
  **presence/absence** in two maps at `[this+0xf0]+0x88` and `+0x8c`
  (`cmp sb,#3 / movne sb,#2` at `0x00aa16f2`).
- `CSRGuildBattleMgr::CanAttackCamp(const std::string&, unsigned char)` (ELF
  `0x00aa1dd8`, 484 B): no string literal; walks the same map, `strcmp`-compares the
  key against the argument string (`0x00aa1e72 lsreq / 0x00aa1e7c cmp r5,r3`), and
  returns a bool. **No numeric parse of the id anywhere.**

**So `camp_id` is not a client-side field in any meaningful sense: it is a lookup
key the client echoes back.** It cannot be numeral 3's home either.

### 1.5 The only hard-coded camp ids in the library are `"101"` and `"103"` — and they are not a rear-set rule

`CSRPopUpGuildBattleField::QueryCampStatus(const std::string&)` (ELF `0x00c60b14`,
756 B) is the **only** function in the binary that compares a camp id against a
literal:

```
00c60b7e  cmp  r1, #3              ; camp_id STRING LENGTH == 3
00c60b80  bne.w #0xc60b40         ; else return 0
00c60c88  ldr  r1, [pc, #0x16c]    ; -> 0x01d71b88  "101"
00c60c92  add  r1, pc
00c60c94  blx  #0x00611b18         ; memcmp(camp_id, "101", 3)
00c60c98  cbz  r0, #0xc60cac      ; equal -> skip the next test
00c60c9a  ldr  r1, [pc, #0x160]    ; -> 0x01d71b8c  "103"
00c60ca0  add  r1, pc
00c60ca2  blx  #0x00611b18         ; memcmp(camp_id, "103", 3)
00c60ca6  cmp  r0, #0
00c60ca8  bne.w #0xc60b40         ; neither -> return 0
```

The literals it concatenates around that test are `_Camp_Defeat_` (`0x01d71ad7`),
`_first` (`0x01d71b5e`) and `_second` (`0x01d71ae5`), and the results are handed to

- `CSRUserDB::PutFirstAction(const std::string&)` — ELF `0x0108cd90`
- `CSRUserDB::IsFirstAction(const std::string&)` — ELF `0x0108ce44`

i.e. **a local-DB "has this camp's defeat animation already played" flag**.
`"101"` / `"103"` gate that flag. They are **not** a rear-area rule, they are not a
count of three, and they involve no point magnitude. Recorded because it is the
closest thing in the binary to a positional special case, and it is disqualifiable.

### 1.6 Byte search: the client embeds **no** rear/front-area concept at all

Searched every section-backed, non-comment region of the file:

| needle | occurrences |
|---|---|
| `최후방` (rearmost), `후방` (rear), `2배` (×2) — UTF-8 | **0** |
| `Rear`, `Final Defense Line`, `Double Points` | **0** |
| `double_point`, `bonus_rate`, `point_limit`-standalone | **0** |
| `double` | 12 — 9 in `.dynstr` (spine/float mangled names), 3 unrelated `.rodata` |

The "3 final areas are doubled" statement exists **only** in the shipped help data
(`UI_CSV.jet` `CONTENTS15_8`), never in the executable.

The field builder was read directly and carries no count either:
`CSRPopUpGuildBattleField::SetEnemyArea(CSRGuildBattleMgr::STATE)` (ELF
`0x00c5a6f4`, **5 128 bytes**) resolves 20 literals, and **every one is a UI-name
prefix or a `BATTLE_PAIR` key**:

```
PA_REGION 0x01d71a32 | PA_CAMP 0x01d71ac8 | PA_CLOUD 0x01d71a81 | CLOUD_ 0x01d71ad0
CELL_CLOUD_ 0x01d71aed | CELL_CAMP_ 0x01d71af9 | CELL_POINT_ 0x01d71b04 | CELL_FIRE_ 0x01d71b35
CELL_MVP_ 0x01d71b10 | BT_ENEMY_ 0x01d71a62 | RE_ENEMY_ 0x01d71b2b | RE_CAMP_MVP 0x01d71b1a
PA_CAMP    | _Camp_Defeat_ | _second | team 0x01d71b26 | enemy 0x01d67246 | camp 0x01d64aa7
gvg_enter_first 0x01d71b40
```

No loop bound of 3, no rear test, no doubled anything. **The rearmost set is a
server-side notion.**

## 1.7 Nine datetimes, ten phase values — and the premise's "eight" is off by one

`CSRGuildBattleMgr::GetCurGVGPhase(std::pair<int,int>*, CSRGuildBattleMgr*)`,
ELF `0x00a9b938`, size 312. Verbatim:

```
00a9b92e  bl   #0x0072e298        ; CMSingleton<CGMTime>::get()
00a9b936  bl   #0x007877fc        ; CGMTime::GetCurServerTimeStamp()
00a9b98e  ldr.w r1, [r5, #0x80]   ; dtm
00a9b992  cmp   r1, #1            ; 0 == "unset"
00a9b994  blt   #0xa9b9a6
00a9b996  ldr.w r2, [r5, #0xe0]   ; time bias member
00a9b99a  add   r2, r0            ; T = bias + server timestamp
00a9b99c  cmp   r1, r2
00a9b99e  bge   #0xa9b9a6
00a9b9a0  movs  r0, #9            ; dtm[0x80] elapsed -> phase 9
...
00a9b9a6  ldr   r2, [r5, #0x7c]   ; -> phase 8
00a9b9ba  ldr   r2, [r5, #0x78]   ; -> phase 7
00a9b9ce  ldr   r2, [r5, #0x74]   ; -> phase 6
00a9b9e2  ldr   r2, [r5, #0x70]   ; -> phase 5
00a9b9f6  ldr   r2, [r5, #0x6c]   ; -> phase 4
00a9ba0a  ldr   r2, [r5, #0x68]   ; -> phase 3
00a9ba1e  ldr   r2, [r5, #0x64]   ; -> phase 2
00a9ba32  ldr   r2, [r5, #0x60]   ; -> phase 1
00a9ba66  movs  r0, #0 ; movs r1, #0   ; default phase 0
00a9ba44  add.w r2, r5, r0, lsl #2
00a9ba48  ldr   r2, [r2, #0x60]
00a9ba4a  subs  r1, r2, r1        ; remaining = dtm[phase] - T
00a9ba4c  strd  r0, r1, [r8]      ; out = (phase, remaining)
```

### The offset→field mapping is confirmed from **two independent sides**

**Side A — the parse stores.** `BATTLE_INFO::parse` (ELF `0x00a93260`) reads the
nine dtm keys in order and stores each conversion into consecutive ints. The store
for key *n* is emitted just after the `ldr` for key *n+1*, at:

| key | store site | `this+` |
|---|---|---|
| `min_entry_cnt` | `0x00a93332` `str.w r4, [sb,#0xc]` | `+0x0c` |
| `teaser_begin_dtm` | `0x00a9337e` `str.w r4, [sb,#0x10]` | `+0x10` |
| `register_begin_dtm` | `0x00a933c4` `str.w r0, [sb,#0x14]` | `+0x14` |
| `matching_begin_dtm` | `0x00a9340c` `str.w r0, [sb,#0x18]` | `+0x18` |
| `deploy_begin_dtm` | `0x00a93454` `str.w r0, [sb,#0x1c]` | `+0x1c` |
| `combat_begin_dtm` | `0x00a9349c` `str.w r0, [sb,#0x20]` | `+0x20` |
| `calc_begin_dtm` | `0x00a934e4` `str.w r0, [sb,#0x24]` | `+0x24` |
| `result_begin_dtm` | `0x00a9352c` `str.w r0, [sb,#0x28]` | `+0x28` |
| `finish_dtm` | `0x00a935a6` `str.w r0, [sb,#0x2c]` | `+0x2c` |
| `next_gvg_dtm` | (store at `+0x30`, past the dump window) | `+0x30` |

**Side B — the base offset.** `ParseRef` (ELF `0x00a93258`) is a 6-byte thunk:
```
00a93258  adds  r0, #0x50         ; BATTLE_INFO == this(CSRGuildBattleMgr) + 0x50
00a9325a  b.w   #0xa93260
```
So `mgr + 0x60 == BATTLE_INFO + 0x10 == teaser_begin_dtm`, `mgr + 0x64 == register`,
… `mgr + 0x80 == BATTLE_INFO + 0x30 == next_gvg_dtm`. **That is byte-exactly the
offset ladder `GetCurGVGPhase` tests.** Two independent code paths, zero residual.

### Resulting phase table

| phase | elapsed marker | meaning |
|---|---|---|
| 0 | none elapsed | before `teaser_begin_dtm` |
| 1 | `teaser_begin_dtm` | teaser → register |
| 2 | `register_begin_dtm` | registration |
| 3 | `matching_begin_dtm` | matching |
| 4 | `deploy_begin_dtm` | **defender deployment** |
| 5 | `combat_begin_dtm` | **combat** |
| 6 | `calc_begin_dtm` | calculation |
| 7 | `result_begin_dtm` | **result** |
| 8 | `finish_dtm` | finish |
| 9 | `next_gvg_dtm` | after the season |

`remaining` is `dtm[phase] - T`, i.e. time until the **next** phase's marker.
Note: for phase 9 it computes `mgr + 0x60 + 9*4 = mgr + 0x84`, which is
`BATTLE_INFO + 0x34` — **one `int` past the end of the dtm array.** A real
one-past-the-array read; flagged, not exploited. It is not a tenth datetime.

**Correction to the task premise:** `/gvg/GetRef` returns **nine** absolute
datetimes, not eight. `next_gvg_dtm` is the ninth, and `GetCurGVGPhase` has **ten**
phase values (0–9). `gvg-reference-2026-10-05.md` §2.1 already recorded the ninth
("eight phase markers … plus `next_gvg_dtm`"); the task brief's "eight" dropped it.

## 1.8 The two id spaces are **never joined** — the falsifier test from `gvg-reference` §3.2, run and negative

`gvg-reference-2026-10-05.md` §3.2 item 3 offered a falsifier for the "reference id
space is wider than the display enum" reading: *decompile
`RefreshPoint` and show the display id indexing the reference table*. **Run, and
negative.**

`CSRPopUpGuildBattleWin::RefreshPoint(unsigned)` (ELF `0x00c7838c`, 1012 B) resolves
**exactly seven** literals, and **none** of them is `point`, `val` or `id`:

```
'+'          0x01d69924 @ 0xc7840c
RE_POINT     0x01d7222d @ 0xc7844c
RE_TOTAL     0x01d72236 @ 0xc784c6
IT_WINPOINT  0x01d60525 @ 0xc784ec
TX_WINPOINT  0x01d60469 @ 0xc78512  and  @ 0xc7857e
(+ the GOT / __stack_chk_guard slot @ 0xc7839c)
```

It is pure UI assembly (`RE_POINT` rows + `RE_TOTAL` total, formatted with `+`).
It never touches the reference magnitude table.

The reference `point[]` (`{id, val}`) has exactly **two** consumers:

| site | function | what it does with it |
|---|---|---|
| `0x00a93b4e` / `0x00a93bac` / `0x00a93ba6` | `CSRGuildBattleMgr::BATTLE_INFO::parse` | stores the `{id,val}` pairs |
| `0x00a8d4ec` (unnamed, prologue `0x00a8d4b8`) | `CSRGuildBattleDeckHandler::SaveEntry`'s `$_5` lambda | reads `gvg_get_deploy_point` (`0x01d6925e`) → `point` and writes the **local-DB key** `GVG_진입한_지역` (`0x01d690d8`) |

Supporting identification: the `.rodata` string at `0x01dfe741` is
`ZN25CSRGuildBattleDeckHandler9SaveEntryENSt6__ndk18functionIFvvEEEE3$_5`, the
exact mangled name of that lambda. `CSRTableGuildBattleDefense::OnInit`
(ELF `0x00ff3804`) also reads `gvg_get_deploy_point` → `point` at `0x00ff39e4` /
`0x00ff3a10` for the **deploy-point popup**, and
`ProcessDeployPointPopup` (ELF `0x00ff3b28`) shows `GV_WINPOINT`
(`0x01d69918`) with the notice key at `0x01d815e9`.

**No display path reads `/gvg/GetRef`'s `point[]`.** The two id spaces — the
server-side magnitude table keyed by `point[].id`, and the client-side
`POINT_INFO_TYPE` — are structurally independent in this client.

## 1.9 `POINT_INFO_TYPE` display mapping — four rows, and values 2 and 3 collide

`CSRPopUpGuildBattleWin::SetData(const std::pair<POINT_INFO_TYPE,int>&)`,
ELF `0x00c79db0`, size 728:

```
00c79df0  ldr  r0, [r4]          ; pair.first == POINT_INFO_TYPE
00c79df2  subs r1, r0, #1
00c79df4  cmp  r1, #4
00c79df6  bhi.w #0xc79f3c       ; id > 5  ->  STORE NOTHING, silent return
00c79dfa  movs r0, #0
00c79dfc  tbb  [pc, r1]         ; table at 0x00c79e00 = 84 03 42 81 83
```

| `POINT_INFO_TYPE` | tbb byte | target | text resolved | slot `r0` | record at |
|---|---|---|---|---|---|
| **1** | `0x84` | `0x00c79f08` | **none** | 0 | `this+0x000` |
| **2** | `0x03` | `0x00c79e06` | `TX_POINT` + `GVG_한번의 공격으로 격퇴` (`0x01d721e9`) | **1** | `this+0x030` |
| **3** | `0x42` | `0x00c79e84` | `TX_POINT` + `GVG_두번의 공격으로 격퇴` (`0x01d7220b`) | **1** | `this+0x030` |
| **4** | `0x81` | `0x00c79f02` | none (`movs r0,#2`) | 2 | `this+0x060` |
| **5** | `0x83` | `0x00c79f06` | none (`movs r0,#3`) | 3 | `this+0x090` |
| ≥ 6 | — | `0x00c79f3c` | — | — | **nothing stored** |

Slot arithmetic: `00c79f08 add.w r0, r0, r0, lsl #1` then
`00c79f12 add.w r5, r5, r0, lsl #4` ⇒ **stride 48 = `0x30`**, four records at
`this+0x658, +0x688, +0x6b8, +0x6e8`. Each record receives
`[+0x658]=2`, `[+0x660/+0x664]` from `bl 0x010ef8e8`, `[+0x668..+0x677]` a 16-byte
constant (`0xbf00bf00, 0x000001f4, 0, 0` from `0x00c7a05c`), `[+0x67c]=0`, and
**`[+0x680] = [r4+4]` = the pair's `.second`, i.e. the scored amount**
(`00c79f26 ldr r0, [r4, #4]` / `00c79f2c str.w r0, [r5, #0x680]`).

The two text branches are structurally identical and differ only in the
localization key. Their chain is fully identified:

```
CMHashID("TX_POINT")                     0x006ce260   @ 0xc79e0e
CMNode<CMUpdatable>::FindCast<CSRUITextbox> 0x00774b4c  @ 0xc79e18
CGMDataMgr::get()                        0x00783aa0   @ 0xc79e1e
CGMDataMgr::GetLocalizedText(const char*) 0x00782ca4   @ 0xc79e2a
CSRUITextbox::SetText(const std::string&, uchar) 0x007a5bfc @ 0xc79e34
```

**Two consequences, both new and both PURE:**

1. **The win popup has 4 point rows, not 5**, and `POINT_INFO_TYPE` 2 and 3 both
   write row 1 — so if both are present in one `point_detail` list, the **later one
   wins and the other is invisible**. Whether that is a shipped bug or intended
   merging is **not** determined here.
2. The `1..5` bound is a **rendering** filter with a **silent** `bhi`, exactly as
   `gvg-point-binding-2026-10-05.md` §2.2 said. Confirmed.

## 1.10 `/gvw/GetResult` — an **aggregate**, not an itemisation. One new key.

`CSRPopUpGuildBattleResult::RESULT_INFO::Parse` (ELF `0x00c72600`, 1808 B):

| site | ELF `.rodata` | key |
|---|---|---|
| `0x00c72618` | `0x01d71ff0` | `summary` |
| `0x00c7262e` | `0x01d693e2` | `my` |
| `0x00c72642` | `0x01d55900` | `point` (under `my`) |
| `0x00c7268e` | **`0x01d71ff8`** | **`contribution_multi`** ← NEW |
| `0x00c726de` | `0x01d63482` | `is_win` |
| `0x00c7272a` | `0x01d5ede5` | `free_iap` |
| `0x00c7277a` | `0x01d5edd0` | `ap` |
| `0x00c727ca` | `0x01d5edd3` | `bp` |
| `0x00c7281a` | `0x01d5edd6` | `gold` |
| `0x00c7286c` | `0x01d5a8a1` | `item_list` |

**There is no `point_detail[]` and no per-event breakdown on the result route.**
One scalar `point` per side, plus a `contribution_multi` multiplier. `dump`
(`0x00c72d10`) re-emits `point` three times (`0x00c72d3a`, `0x00c72e02`,
`0x00c72eba`), i.e. the result side has **three** point-shaped rows in its JSON
(my / enemy / contribution), each a scalar.

## 1.11 The `point_limit` falsifier test from `gvg-reference` §2.7 — run, and **negative**

The prior pass asked for "any recovered key whose name pairs `point` with
`limit`/`min`/`floor`". Result of a whole-file byte search:

```
point_limit   occurs ONCE, at .rodata ELF 0x01d68c62
fc_point_limit occurs at               ELF 0x01d68c5f
```

`0x01d68c62 == 0x01d68c5f + 3`. **`point_limit` is the tail of `fc_point_limit`,
not a separate key.** There is no standalone `point_limit`-shaped GVG key.

Consumer census for the neighbours:

| literal | sites | owners |
|---|---|---|
| `fc_point_limit` | 5 | `CSRGuild::ParseGuild` `@0x00a5a384` +0x340/+0x350, `CSRGuild::ParseUserGuild` `@0x00a5ba78` +0x21c, `RequestBuild` +0x1c8, `RequestModify` +0x1c8 |
| `fc_point` | 2 | `CSRGuild::ParseMember` `@0x00a5b4b0` +0x156, `CSRGuild::ParseApplicants` `@0x00a5b680` +0xcc |
| `gvg_win_cnt` | 2 | `CSRGuild::ParseGuild` +0x600/+0x60e |
| `gvg_inf_win_cnt` | 2 | `CSRGuild::ParseGuild` +0x65e/+0x66e |

All in **guild INFO**, none in a GVG scoring parser. The adjacent `.rodata`
neighbourhood is confirmed as guild vocabulary (`guild_id`, `newbie`,
`contribution`, `region`, `emblem_id`, `member_cnt`, `members`, `banished`).

**Consequence (PURE): there is no client-side GVG winning-points floor.** `gvg_win_cnt`
/ `gvg_inf_win_cnt` are guild counters; the 3000-point threshold would have to be
server-side or hidden inside `reward`/`inf_reward`, whose sub-shapes remain
**[UNKNOWN-1]** (unchanged).

## 1.12 `_first` / `_second` — help numerals 1 and 2 as **UI state names**, not ids

`_first` (`0x01d71b5e`) has exactly **2** consumers, `_second` (`0x01d71ae5`)
exactly **4**, all in two functions:

```
0x00c60bc0 / 0x00c60bee / 0x00c60c4a / 0x00c60d00 / 0x00c60d42   in QueryCampStatus @0x00c60b14
0x00c61c66 ('_first')                                              in DefeatAnimControl @0x00c61c30
```

Both are string fragments concatenated onto a camp id and consumed by
`CSRUserDB::IsFirstAction` / `PutFirstAction`. **This independently corroborates
that the shipped first/second-attack distinction is a real client concept — as an
animation/DB state — and simultaneously shows the numbering is a *suffix*, not the
`point_id` enum.** They do not close the `point_id` → wire-numbering gap that
`gvg-point-binding-2026-10-05.md` §2.1 already flagged.

---

# SECTION 2 — UNPURIFIED: inference, support, falsifiers

Everything here is interpretation. Nothing here may become a fixture without an
explicit local-policy label.

## 2.1 Numeral `3`: **NOT BOUND, and proved unbindable in the recovered client schema**

**Verdict: numeral `3` has no client-side home.** This is stronger than
`gvg-point-binding-2026-10-05.md`'s "UNBOUND — no candidate found", because the
candidate space is now closed rather than unsearched.

| candidate | verdict | evidence |
|---|---|---|
| `multi` on the area `point_detail` row | **rejected** | §1.4: `multi` is 1:1 with a row and is consumed as `val × multi` at `0x00aafc76`. It cannot express "3 of 10 camps differ"; it also has no referent for "3" on a ten-camp map. Consistent with the prior pass's §2.5. |
| `camp_id` | **rejected** | §1.4: 11 consumers, all opaque-string; `GetCampActionStatus` / `CanAttackCamp` do no arithmetic on it. |
| `link_camp` | **rejected** | §1.4: **2** consumers, parse and dump only. Client-inert by construction. |
| a fifth `_CAMP` field | **rejected** | §1.2: exactly four keys, in parse **and** dump. |
| a positional rule over `my_101..my_110` | **rejected** | §1.6: the 5 128-byte field builder resolves only UI-name prefixes; no count constant, no rear test. |
| a localization key naming the rear set | **rejected** | §1.6: zero occurrences of `최후방`, `후방`, `2배`, `Rear`, `Final Defense Line`, `Double Points` anywhere in the file. |
| `"101"` / `"103"` | **rejected** | §1.5: one consumer, a local-DB "first action" flag for the defeat animation. |

**Therefore:** the rearmost set, its size (3), and the ×2 factor are **server-side
only**. The client cannot know which areas are rearmost, therefore the doubling
**must arrive inside the row the server sends** — as `val`, or as `multi`.

**Support for this conclusion:** §1.2 (four fields), §1.4 (two consumers, eleven
opaque-string consumers), §1.5 (one disqualified positional special case), §1.6
(zero occurrences of the concept), all measured over all of `.text`.

**What this does and does not do to the prior pass's reading.**
`gvg-point-binding-2026-10-05.md` §2.5 preferred "`val = 2250`, `multi = 1`
normally and `multi = 2` on a rearmost area". **That hypothesis survives and is
now the *only* surviving reading** — it was always a server decision, and §1.6
proves the client has no alternative. What is newly excluded is any variant in
which the client applies the doubling, or in which the rearmost membership is
published in `/gvg/GetRef`.

**Falsifiers (in order of cost):**

1. **A consumer of `_CAMP+0x28`** (the `link_camp` vector) that this census missed.
   Any such consumer would reopen the question immediately. The census found two
   sites over 22.8 MB with a decode-verified pairing rule and a per-site clobber
   check, but it only covers the Thumb PIC `ldr`+`add` idiom — see §3.
2. **A captured `/gvg/GetRef` in which `link_camp` is a scalar rank or index whose
   values correlate with the doubled areas.** That would make `link_camp` a
   server-published rear marker that a *later* client build consumes. The client
   here would then be ignoring it, which is a legitimate (if unhelpful) outcome,
   not a contradiction.
3. **A captured `/gvg/GetCampClearPointLog` `point_detail` row for a rearmost
   area carrying `val = 4500, multi = 1`.** That would refute §2.5 and show the
   doubling is pre-baked into `val`. One capture resolves six of the eight
   magnitudes at the same time (prior pass §4.4 item 2) — still the highest-value
   single artefact in this system.

## 2.2 The eight-vs-five gap: **the premise is false**, and here is the replacement count

The question as posed was: *eight datetimes, five point enumerators — real gap, or
do some datetimes award nothing?* The honest answer is that the correspondence
**does not exist**, so neither branch is the right frame. Three measured facts:

1. **There are nine datetimes and ten phase values (0–9)** (§1.7), not eight and
   five. The counts do not line up under any reading.
2. **The phase clock and the point ids are never joined.** §1.8: the reference
   `point[]` is read by the parser and by one local-DB writer, never by a display
   path. §1.9: the renderer's `tbb` bounds the *display* id and does not index
   anything. No code maps a datetime, or a phase, to a `point_id`.
3. **A datetime is a phase boundary, and a boundary awards nothing by itself.** The
   client only ever derives `(phase, remaining)` from it (§1.7). All awarding is
   server-side, delivered as `point_detail` rows with their own `point_id`.

So the real structural facts about how many point rows exist are:

| table | shape | row count |
|---|---|---|
| `/gvg/GetRef` → `point[]` | `{id, val}` | one row per scoring event; **`id` is read with no clamp**, so it *may* carry eight (or more) rows with no client complaint (§1.8, and `gvg-point-binding` §1.4) |
| `/gvg/GetCampClearPointLog` → `point_detail[]` | `{point_id, val, multi}`, stored as `val × multi` | one row per contribution; arbitrary count |
| `/gvg/GetResult` → `summary.my.point` | **scalar** + `contribution_multi` | **one aggregate per side, no itemisation** (§1.10) |
| win popup UI | 4 records, stride `0x30`, ids 1–5 with 2 and 3 colliding | **4 rows render** (§1.9) |

**What a future `/gvg/*` implementation needs, answered directly:**

- **`/gvg/GetRef` should publish up to eight `point[]` rows** (one per
  `CONTENTS15_8` scoring event) with `id` values the server chooses and the client
  never validates. Sending five is safe; sending eight is safe. **Sending fewer than
  the events you want scored is the only real failure**, and it fails silently.
- **`/gvw/GetCampClearPointLog` must send one `point_detail` row per contribution**,
  and **every row must carry `multi`** — an omitted `multi` is a hard zero
  (prior pass §1.3(c), confirmed by the 1-site census for `multi` in §1.4).
- **`/gvg/GetResult` needs no per-event rows at all** — one scalar plus
  `contribution_multi` (§1.10). A fixture that itemises the result screen will be
  ignored by this client.
- **No route needs more fields for numeral `3`** (§2.1). The gap is not a schema
  gap; it is an absent server-side rule.

**Support:** §1.7 (counts), §1.8 (no join), §1.9 (4 rows), §1.10 (aggregate).
**Falsifier:** a decompiled or live-observed path in which a `point_id` is computed
from a phase value or a `*_dtm`. None exists in the paths read here; the census
covers the literal-idiom population only, so a join built from a *non*-string
constant (e.g. `phase + 1` passed straight to `SetData`) would not be caught by a
literal census — I checked the one caller chain I could name,
`CSRPopUpGuildBattleMgr::GetCombatEndPointList` (ELF `0x00a97e2c`, size **6**), and it
is a 6-byte accessor thunk, so the caller edge is still untraced.

## 2.3 `POINT_INFO_TYPE` 2-and-3 collision: reading, not conclusion

§1.9 shows both branches writing row index 1 (`movs r0,#1` at `0x00c79e80` and
`0x00c79efe`). Two readings fit:

- **(i) shipped bug** — the two attack-count bonuses overwrite each other and only
  the last is visible.
- **(ii) intended merge** — the popup is *designed* to show one "attack bonus" row
  and the two `GVG_*` keys are legacy leftovers, with `SetPointListData`'s iteration
  order deciding which.

`SetPointListData` (ELF `0x00c79844`, 1388 B) resolves only `RE_MOTION`, `begin`,
`begin` plus non-printable GOT slots — it drives the reveal animation and hands
each pair to `SetData`. Its iteration order over the `std::list` is therefore the
decider under (ii), and that is **not** traced here.

**Support for the observation itself:** the two `movs r0,#1` sites, read verbatim.
**Falsifier:** a live `point_detail` containing both `point_id` 2 and 3 with a
result screenshot — one capture distinguishes (i) from (ii) and also reveals which
of the two labels the user sees.

## 2.4 One genuine anomaly, reported rather than exploited

`GetCurGVGPhase`'s `remaining` for **phase 9** reads
`mgr + 0x60 + 9*4 = mgr + 0x84 = BATTLE_INFO + 0x34`, one `int` past the dtm array
(§1.7). Consequences that are *not* established: whether it aliases a real member
(the next field, or the `camp` map's first word), and whether the subtraction can go
negative in normal operation. Recorded because a future implementation must not
assume phase 9 has a defined countdown.

---

## 3. Limits, retractions, and what this pass did NOT do

### 3.1 Retractions and corrections this pass forces on prior files

1. **"The `POINT_INFO_TYPE` enumerator table is behind pre-relocation pointers"**
   (`gvg-reference` §1.11; `gvg-point-binding` §4.2; `blitz-search-consumers` §4.1
   item 4) — **RETIRED, for a different and stronger reason.** §1.1: the function is
   libc++'s **numeric** `to_string` (`basic_ostream<char>::operator<<(int)` +
   `basic_stringbuf<char>::str()`). There is no name table, relocated or not. The
   "needs relocated data, not just the symbol" framing is wrong: it needs a
   **different** symbol, and there may not be one.
2. **"The `multiplier` on the area row is the only place the rearmost ×2 can live"**
   (`gvg-point-binding` §2.5) — **NARROWED.** It can also be pre-baked into `val`; the
   client cannot distinguish, and §1.6 now proves the client cannot be the one to
   apply it. §2.5's own falsifier (`val=4500, multi=1`) stands.
3. **`camp_id` / `link_camp` are "client-side fields"** (the task brief's framing) —
   **CORRECTED.** `camp_id` is a wire key the client echoes back and never
   interprets; `link_camp` is parsed, stored and re-emitted and read by nothing.
   Neither is a client-side field in the sense of driving behaviour.
4. **"`/gvg/GetRef` returns eight absolute datetimes"** (task brief) — **CORRECTED to
   nine** (`gvg-reference` §2.1 already said so).
5. **`_CAMP` field order** — `gvg-reference` §1.4 lists `min_cp, camp_id, name,
   link_camp`; the **memory** order is `min_cp(+0x00), name(+0x04), camp_id(+0x10),
   link_camp(+0x28)`, and `name` is a **derived** field that is never a wire input.
   Load-bearing for anyone writing a fixture or a reader.

### 3.2 What this pass did NOT do

- **No Ghidra run, no Ghidra project access.** Parent-owned and locked. Every
  function-level claim is capstone + verbatim bytes on the original `.so`, plus
  `.dynsym` read directly with `struct`.
- **No decompiler was used at all**, only raw instructions and the `tbb` tables —
  per `AGENTS.md` §16.7 lesson 7, that is what made the four-row stride and the
  phase ladder legible; a flattened decompile would have hidden both.
- **No `/gvg/*` handler implemented**, no `server-ts` file read/written/executed, no
  test, no build, no server start, no state file touched.
- **No `.so` written, copied, patched or moved.** Reads only; SHA-256 identical
  before and after (§ header).
- **No APK, seed, LevelDB or JET opened or modified.** No emulator, VM, physical
  phone or release operation.
- **No catalogue edit, no fixture edit.**
- **`polluted-observations.md` NOT appended.** The parent mirrors.
- **Encoding guard:** the file was written with the `write` tool as UTF-8/LF and
  then verified by a Python pass — **U+FFFD = 0, CRLF = 0**. Hangul and Hangul-free
  line contents were not round-tripped through PowerShell at any point; no
  `Get-Content`/`Set-Content`/`WriteAllLines` touched any workspace file. Console
  echoes of Hangul in this session are PowerShell rendering only and are not file
  evidence (`GUARD-encoding-and-archive-traps.md` §Rule 2).

### 3.3 Residual limits of the census method (important — this is the whole evidential base of §1.4 and §2.1)

1. **The census only sees the Thumb PIC idiom** (`ldr Rd,[pc,#imm]` + `add Rd,pc`).
   A consumer that obtains `"link_camp"` some other way — a different relocation
   form, a jump table, an address computed from a base register, or a pointer
   stashed in `.data.rel.ro` — would not appear. The census is a **strong** negative
   over the dominant idiom, not a proof over the whole address space.
2. **The 32-bit-interleave walk is permissive.** It relies on the exact 32-bit
   addend match plus a capstone check that nothing in the gap writes the
   destination register. It is not a proof that no intervening `add Rd, Rn` could
   have refilled the register from elsewhere — that case is covered by the gap
   clobber check, which does inspect every decoded instruction.
3. **`back = 14/30/60` stability shows the walk limit is not binding**; it does not
   show that a `ldr` more than 60 halfwords before its `add` does not exist. That is
   implausible for this compiler's idiom (measured maximum in the validated
   resolvers was 2) but is a limit, not a proof.
4. **`tbb` tables were read by hand from raw bytes** at `0x00c79e00` and from the
   `cmp`/`movs` ladder at `0x00a9b938 … 0x00a9ba66`. The table byte values
   (`84 03 42 81 83`) were decoded as `target = table_base + 2*byte` and each
   resulting target was then read as a **decoded instruction** to confirm what it
   does (`movs r0,#1` vs `movs r0,#2`). Both readings agree.
5. **Untraced caller edges**, unchanged from prior passes: the owner of the point-log
   parser (prologue `0x00aaf880`) and of the unnamed GVG parser at `0x00ab307e`;
   the route→parser attribution for 18 of 19 `/gvg/*` routes; and the caller of
   `CSRGuildBattleMgr::GetCombatEndPointList` (a 6-byte thunk, so the edge itself is
   the open question).
6. **`_CCellGBPoint::SetPoint`** (ELF `0x00c60fc4`) resolves `TX_CAMPPOINT` and `+`
   only, and **`_CCellGBPoint::Play`** resolves `PA_CAMP_POINT`, `MotionCtrl`,
   `appear_camppoint` — these are the per-camp point popups and were read but their
   **displayed value's provenance** (i.e. whether it comes from `INFO::point` or from
   a `point_detail` aggregate) is **not** traced.
7. **`INFO::parse` / `INFO::dump`** carry a `point` key (`0x00aa5b68`, `0x00aa6268`)
   and are the per-guild summary record. That `point` is the **guild total**, not a
   per-event magnitude — consistent with `gvg-reference` §1.8, but the value's
   provenance inside `INFO` was not re-verified here.
8. **Zero coverage credit** and zero fixture content. The broader base-stat goal
   remains far from its 70% thresholds.

---

## 4. Cheapest next steps, in order

1. **Any real `/gvg/GetCampClearPointLog` capture.** One payload resolves the
   `multi`-vs-`val` question (§2.1 falsifier 3), whether `point_id` is ever ≥ 6, and
   whether ids 2 and 3 both appear in one list (§2.3) — three open questions at once.
2. **Any real `/gvg/GetRef` capture.** Settles whether the reference `point[]` really
   carries eight rows (the only remaining count question), and whether `link_camp`
   ships as anything other than an array of strings.
3. **Close the census's residual limit (§3.3.1)** with one additional sweep that
   does not rely on the `ldr`+`add` pairing — e.g. resolve every `.rodata` address
   that appears as a `.data.rel.ro` pointer target, then find code that dereferences
   it. This is the only way to convert §1.4's "client-inert" from *strong* to
   *complete*.
4. **`CSRPopUpGuildBattleWin::SetPointListData` iteration order** (§2.3), which is a
   few instructions and decides whether the 2/3 collision is a bug or a merge.
