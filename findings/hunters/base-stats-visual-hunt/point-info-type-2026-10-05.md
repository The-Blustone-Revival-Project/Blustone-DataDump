# `CSRGuildBattleMgr::BATTLE_INFO::POINT_INFO_TYPE` — enumerated (2026-10-05)

**Read-only.** No Ghidra project opened (parent-owned and locked). No server,
fixture, catalogue, seed, state, APK, emulator/VM or phone action. Exactly one
file written: this one. `polluted-observations.md` is deliberately **not**
appended — the parent mirrors.

## Method actually used

`llvm-objdump -d --triple=thumbv7a-linux-gnueabihf` and `llvm-nm -D` on
`analysis/extracted/lib/armeabi-v7a/libnative_core.so` (35,445,748 bytes), plus a
small offline Thumb literal resolver written to a temp directory (not left in the
workspace). Cross-checked against `analysis/native-all-strings.tsv` and by direct
byte search in the `.so`.

The `.so` is **fully stripped**: `.dynsym`/`.dynstr` only, no `.symtab`,
`.strtab` or `.debug_*`. Segment 1 is `LOAD offset 0 / VirtAddr 0`, so
**VMA == file offset** for `.text` and `.rodata`.

> ⚠️ **That identity holds for the FIRST `PT_LOAD` only** (added 2026-10-05).
> The library has two: `VA 0x00000000 / off 0x00000000` (R-X, ends
> `0x0210d320`) and `VA 0x0210e550 / off 0x0210d550` (RW-, i.e.
> **`p_offset == p_vaddr − 0x1000`**). So `file_offset == VA` is **false** for
> `.data`, `.got`, `.data.rel.ro*` — reading at `VA − 0x10000` there lands
> `0x1000` bytes low. Every address in this file is in `.text`/`.rodata`, so this
> note does not affect any conclusion here; it is recorded because the uniform
> `− 0x10000` mapping is a documented, already-exploited trap (it produced the
> `'X'` phantom). See `address-convention-2026-10-05.md` §2 and
> `resolver-hardening-2026-10-05.md` §1.4-D2.

---

# SECTION 1 — PURE

## 1.1 Address-convention correction (this changes every address in the source note)

The addresses quoted in `blitz-search-consumers-2026-10-05.md` — and the addresses
in `analysis/native-all-strings.tsv`, which that note cites — carry a **+0x10000
bias**. Real ELF VAs are 0x10000 lower. Verified by direct byte search:

| literal | real ELF VA (byte search) | note / TSV said |
|---|---|---|
| `point_id` | `0x01d6985b` | `0x01d7985b` |
| `multi` | `0x01d69864` | `0x01d79864` |
| `TX_POINT` | `0x01d704ff` | `0x01d804ff` (TSV) |

Functions, from `llvm-nm -D` (exact defined symbols):

| symbol | real ELF VA | note said |
|---|---|---|
| `std::__ndk1::to_string<CSRGuildBattleMgr::BATTLE_INFO::POINT_INFO_TYPE>` (W) | `0x0087f9d0` | `0x0088f9d0` |
| `CSRPopUpGuildBattleWin::SetPointListData(list<pair<POINT_INFO_TYPE,int>> const&)` | `0x00c79844` | `0x00c89844` |
| `CSRPopUpGuildBattleWin::SetData(pair<POINT_INFO_TYPE,int> const&)` | `0x00c79db0` | `0x00c89db0` |
| `CSRCellGuildBattleCard::SetCombatPoint(int)` | `0x0087fd9c` | `0x0088fd9c` |

This is `AGENTS.md` §16.7 item 3 biting in the opposite direction: the note's
addresses are Ghidra-style, not ELF. Nothing below mixes the two conventions.

Also: `native-evidence.tsv` labels `0x0088f9d0` as **undefined**. That is a
defect of that file, not of the binary — `llvm-nm -D` reports the symbol as
**`W`** (weak, defined COMDAT) at `0x0087f9d0`. Every row examined in that region
carries the same bogus `undefined` tag, so the column is not usable as evidence.

> **Measured across the whole column 2026-10-05** (later pass): this is not a
> regional artefact. `native-evidence.tsv` line 2 declares `IMAGE_BASE 00010000`,
> and **all 40 290** `[FUNCTIONS]` rows carry the literal tag `undefined`, of which
> **36 755 (91.2 %)** are in fact defined dynamic symbols per `llvm-nm -D`
> (20 445 `T` + 16 310 `W`). Of the remaining 3 535, 2 363 are IDA synthetic names
> (`FUN_*`, `SUB_*`, `loc_*`, `switch*` — no dynsym counterpart at all) and 397 are
> `_INIT_*` pseudo-symbols. Only **775** rows — the genuine libc/libc++ imports
> (`strlen`, `pthread_create`, `__cxa_atexit`, …) — deserve the tag. See
> `address-convention-2026-10-05.md` §4.

The `+0x10000` correction above is itself now confirmed exhaustively: **all 36 467**
`[FUNCTIONS]` rows that `llvm-nm -D` can resolve match it at `addr − 0x10000`, and
**none** matches at `addr` as printed. `native-all-strings.tsv` uses the *same*
Ghidra convention (515 576/515 576 rows verified).

## 1.2 The enumerator list: cardinality and value range — **5 values, 1…5**

This is the decisive result, and it comes from a **jump table**, not from the
`to_string` body.

`CSRPopUpGuildBattleWin::SetData(std::pair<POINT_INFO_TYPE,int> const&)`,
`0x00c79db0` (the only `SetData(pair<POINT_INFO_TYPE,int>)` in the dynamic symbol
table, so the enum has exactly one per-row consumer). Exact listing:

```asm
c79dd8: a80d   add  r0, sp, #0x34
c79dda: 4629   mov  r1, r5
c79ddc: 4632   mov  r2, r6
c79dde: f6f6 ff55  bl  0x0b70c8c   ; FindCastByName<...>(this, row)
c79de2..c79dec  (spill / basic_string dtor)
c79df0: 6820   ldr  r0, [r4]        ; r4 = &pair ; r0 = pair.first = POINT_INFO_TYPE
c79df2: 1e41   subs r1, r0, #0x1    ; r1 = value - 1
c79df4: 2904   cmp  r1, #0x4        ; unsigned: r1 <= 4
c79df6: f200 80a1 bhi.w 0x00c79f3c  ; default -> skip
c79dfa: 2000   movs r0, #0x0
c79dfc: e8df f001  tbb  [pc, r1]
c79e00: 84 03 42 81 83 00           ; table bytes
c79e06: 499c   ldr  r1, [pc, #0x270] @ 0x00c7a078   ; case-1 block
...
c79e80: 2001   movs r0, #0x1
c79e82: e002   b    0x00c79f08
c79e84: 497e   ldr  r1, [pc, #0x1f8] @ 0x00c7a080   ; case-2 block
...
c79efe: 2001   movs r0, #0x1
c79f00: e002   b    0x00c79f08
c79f02: 2002   movs r0, #0x2
c79f04: e000   b    0x00c79f08
c79f06: 2003   movs r0, #0x3
c79f08: eb00 0040  add.w r0, r0, r0, lsl #1       ; r0 = 3 * r0
c79f0c: a154      adr  r1, #336
c79f0e: f961 0aef  vld1.64 {d16,d17}, [r1:128]
c79f12: eb05 1500  add.w r5, r5, r0, lsl #4        ; r5 = this + 48 * k
c79f26: 6860      ldr  r0, [r4, #0x4]              ; pair.second (int)
c79f2c: f8c5 0680  str.w r0, [r5, #0x680]          ; store the magnitude
```

**Table base** is `Align(tbb_va + 4, 4)` = `0x00c79e00`; entries are bytes,
`target = base + 2 * byte`. Decoded, with `index = value - 1`:

| value | table byte | target | lands on |
|---|---|---|---|
| **1** | `0x84` | `0x00c79f08` | merge point directly; `r0 = 0` |
| **2** | `0x03` | `0x00c79e06` | localized-label block A; `r0 = 1` |
| **3** | `0x42` | `0x00c79e84` | localized-label block B; `r0 = 1` |
| **4** | `0x81` | `0x00c79f02` | `movs r0, #2` |
| **5** | `0x83` | `0x00c79f06` | `movs r0, #3` |

The sixth byte at `0x00c79e05` (`0x00`) is never indexed: `cmp r1,#4` bounds
`r1` to 0…4.

**The bound is hard.** `subs r1, r0, #1` + `cmp r1, #4` + unsigned `bhi` means
exactly values **1, 2, 3, 4, 5** reach the table; **0 and every value ≥ 6 take the
default path** (`0x00c79f3c`), which stores nothing and returns. So:

> `POINT_INFO_TYPE` has **exactly five enumerators with numeric values 1–5**.
> There is no enumerator 0 and no sixth enumerator.

**Base-ambiguity check (so the decode is not a guess).** Five candidate bases
were tested. `0x00c79e00` is the only one whose five targets are all 2-byte-aligned
instruction starts inside the function body. Bases `0x00c79e02`, `…e04`, `…e06`,
`…e08` yield targets that land inside the table itself or mid-instruction
(`0x00c79e02`, `0x00c79e04`, `0x00c79e07`, …). `0x00c79e00` is therefore unique.

## 1.3 What each value *does* — the enumerator list proper

After the table, `r0` (0…3) selects one of **four** display slots: `r0 *= 3` then
`this + r0*16`, i.e. a **48-byte stride**, and `pair.second` is stored at
`this + 0x680 + 48*k`. Values 1, 4 and 5 perform **no** label lookup; values 2 and
3 each perform a `CMHashID` → `FindCastByName<CSRUITextbox>` →
`CGMDataMgr::GetLocalizedText` → `CSRUITextbox::SetText` sequence.

Literal resolution (all five pinned; see §1.8 for the rules):

| value | slot `k` | node name | `GetLocalizedText` key | key VA |
|---|---|---|---|---|
| **1** | 0 | — (none) | — (none) | — |
| **2** | 1 | `TX_POINT` | **`GVG_한번의 공격으로 격퇴`** | `0x01d721e9` |
| **3** | 1 | `TX_POINT` | **`GVG_두번의 공격으로 격퇴`** | `0x01d7220b` |
| **4** | 2 | — (none) | — (none) | — |
| **5** | 3 | — (none) | — (none) | — |

The containing row/label container is resolved once in the prologue:
`basic_string(char const*)` on `0x01d721df` = **`RE_POINT1`**, then
`FindCastByName(this, "RE_POINT1")`.

Related node names shipped in the same block, for context:
`RE_MOTION` (`0x01d721d5`, used by `SetPointListData` `0x00c79844` with the tween
literal `"begin"`), `RE_POINT` (`0x01d7222d`) and `RE_TOTAL` (`0x01d72236`), the
latter two used by a different popup at `0x00c7844c`/`0x00c784c6`.

**Observed, not interpreted:** values **2 and 3 select the same display slot
`k = 1`** *and* write to the same node name `TX_POINT`, differing only in the
localized key. Whether that is a developer slip or an intentional grouping is
**not determined here** — each list row receives one `SetData` call, so no runtime
collision is implied, but the code as emitted does map two enumerators onto one
slot. Do not read this as evidence of a scoring rule.

## 1.4 The two named point kinds

- **`POINT_INFO_TYPE = 2` → `GVG_한번의 공격으로 격퇴`** — "defeated in one attack",
  first-attempt.
- **`POINT_INFO_TYPE = 3` → `GVG_두번의 공격으로 격퇴`** — "defeated in two attacks",
  second-attempt.

These are the **only two point-kind labels in the binary**. A whole-file scan for
`GVG_*` literals returned **158 distinct** strings; the two above sit alone in the
`CSRPopUpGuildBattleWin` string block between `GVG_BT_WIN` (`0x01d721c0`) and
`GVG_REAL/GVG_BT_LOSE` (`0x01d7223f`). The other point-flavoured GVG keys —
`GVG_총 승점 획득` (`0x01d817b9`), `GVG_공격 승점` (`0x01d817cf`), `GVG_방어 승점`
(`0x01d817e1`) — live in the `GVG_RANK_CELL` block and are **not** referenced by
this switch.

The English renderings ("First Attempt" / "Second Attempt") are cited from
`blitz-search-consumers-2026-10-05.md` §1.6's recovered `UI_TEXT_RO` rows; **I did
not re-read the LevelDB this pass**, so treat the EN strings as cited, not
independently re-verified. The KO keys themselves are read straight out of the
`.so`.

**Values 1, 4 and 5 are not named by anything in the binary.** Their only recovered
identity is positional: they are the 1st, 4th and 5th enumerators and they fill
display slots 0, 2 and 3 respectively.

## 1.5 `std::to_string<POINT_INFO_TYPE>` is a NUMBER formatter — no name table

This is the source note's stated "cheapest next decompilation", and it is a dead
end. That hypothesis is **falsified**.

`0x0087f9d0`, weak COMDAT, full body `0x0087f9d0`–`0x0087faec`:

```asm
0087f9d0: push  {r4,r5,r6,r7,lr}
0087f9d2: add   r7, sp, #0xc
0087f9da: strd  r0, r1, [sp, #12]        ; save sret ptr + the enum value
0087fa06: blx   0x0a06950
0087fa3e: blx   0x0a06960
0087fa70: bl    0x006d4c10   ; EXACT SYMBOL: std::__ndk1::basic_ostream<char>::operator<<(int)
0087fa78: bl    0x006d55bc   ; EXACT SYMBOL: std::__ndk1::basic_stringbuf<char>::str() const
0087fa8a: itt   ne
0087fa8e: blxne 0x0a06540
0087fa98: blx   0x0a06970
0087faa2: blx   0x0a06980
0087faea: nop
```

Both call targets were confirmed by **exact** `llvm-nm -D` match, not by
nearest-preceding-symbol inference. There is **no jump table, no `tbb`/`tbh`, and
not one string literal** in the body. It streams the value as an `int` and returns
the stream buffer as a decimal string.

So `to_string` contributes **nothing** to enumerator naming. It does prove the enum
is an integral type passed by value into the libc++ template — but it does **not**
distinguish `enum class` from an unscoped enum, because for an unscoped enum the
`to_string(_Tp)` template is still an exact match that beats the `to_string(int)`
conversion. **Do not claim the enum is scoped.**

## 1.6 Wire provenance — the values are server-supplied

The `point_detail` row parser sits at ≈`0x00aafa60`–`0x00aafc30` inside
`CSRGuildBattleMgr`. Resolved keys, in request order:

| key | VA | pool slot | load site |
|---|---|---|---|
| `point_detail` | `0x01d6984e` | `0x00aafbec` | `0x00aafa6a` |
| `point_id` | `0x01d6985b` | `0x00aafbf0` | `0x00aafb3a` → `r9` |
| `val` | `0x01d543ff` | `0x00aafbf4` | `0x00aafb42` → `r10` |
| `multi` | `0x01d69864` | `0x00aafbf8` | `0x00aafb48` → `r8` |

So a `point_detail` row is `{point_id, val, multi}` — note `val`, which the source
note's field dictionary does **not** list.

`point_id` is consumed at `0x00aafb70` as a **generic JSON number**:

```asm
00aafb70: bl    0x07830f8   ; nlohmann basic_json::operator[](char const*)
00aafb74: ldrb  r1, [r0]     ; json value type tag
00aafb76: subs  r1, #0x3
00aafb78: cmp   r1, #0x4     ; nlohmann type 3..7 = the numeric types
00aafb7a: bhi   0x00aafbb4   ; default -> r4 = 0
00aafb7c: tbb   [pc, r1]
```

**This second `subs #3 / cmp #4 / tbb` is a `nlohmann::json` type-tag dispatch, not
an enum switch** — it is easily mistaken for one, so it is flagged here explicitly.
There is **no client-side validation, clamping or remapping of `point_id` into
1…5 at parse time**; the default path merely substitutes 0. The enum values
therefore arrive from the server, and the TBB bound of §1.2 is a *rendering* bound,
not a parse-time contract.

Adjacent confirmed parser facts, for the record:

- `CSRGuildBattleMgr::BATTLE_INFO::parse` (`0x00a93260`) reads `gvg`→`id`,
  `min_entry_cnt`, `max_cp`, `inf_reward`, `point`, `camp`.
- `CSRGuildBattleMgr::BATTLE_INFO::_CAMP::parse` (`0x00aa2d7c`) reads `min_cp`,
  `camp_id`, `name`, `link_camp`, `enemy_guild_id`, `inf_gvg`, `user`, `guild_id`,
  `total_cp`, `offense_point`, `defense_point`, `commander`, `card_list`,
  `deployed_list`, `card_%d`, `ref_id`, `level`, `overcome_cnt`, `cp`, `awk_step`,
  `awk_overcome`, `enemy_camp_id`, `remain_hp`, `skin_id`, `order`, `skill_level`.
- `_CAMP` is keyed by **string** in a `std::map<std::string, shared_ptr<_CAMP>>`
  (`__tree::__map_value_compare<const string, shared_ptr<_CAMP>>`), not by the enum.
- `point_list` / `total_point` are parsed at `0x00aa761c`/`0x00aa76e6` and
  `0x00aa7d96`/`0x00aa7ec2` (two sites).

## 1.7 Consumer inventory

| role | real ELF VA | symbol |
|---|---|---|
| enum → display switch (**the only one**) | `0x00c79db0` | `CSRPopUpGuildBattleWin::SetData(pair<POINT_INFO_TYPE,int> const&)` |
| row list driver | `0x00c79844` | `CSRPopUpGuildBattleWin::SetPointListData(list<pair<POINT_INFO_TYPE,int>> const&)` |
| numeric stringifier (no names) | `0x0087f9d0` | `std::__ndk1::to_string<…POINT_INFO_TYPE>` |
| single-int cell point (**not** enum-typed) | `0x0087fd9c` | `CSRCellGuildBattleCard::SetCombatPoint(int)` |
| `BATTLE_INFO` parse | `0x00a93260` | `…BATTLE_INFO::parse(json const&)` |
| `_CAMP` parse | `0x00aa2d7c` | `…BATTLE_INFO::_CAMP::parse(json const&)` |
| `_CAMP` dump (struct→json) | `0x00aa5768` | `…BATTLE_INFO::_CAMP::dump()` |

`SetCombatPoint(int)` takes a plain `int`, so it carries **no** enum and gives no
naming evidence — worth stating because the source note lists it beside the
enum-typed call.

## 1.8 Explicit negative — the C++ enumerator identifiers are unrecoverable

Stated plainly rather than guessed:

- The library is **fully stripped**. No `.symtab`, no `.strtab`, no `.debug_info`,
  no `.debug_str`. There is no DWARF enumeration of any kind.
- Itanium C++ mangling encodes the enum's **type** name only. Every mangled
  occurrence in the binary is
  `…17CSRGuildBattleMgr11BATTLE_INFO15POINT_INFO_TYPEE…` — the enumerator
  identifiers (`POINT_INFO_TYPE::<something>`) **never appear anywhere**.
- RTTI cannot help either: `_ZTI`/`_ZTS` records carry class names, and there is no
  `type_info for enum` emission that enumerates members.

Therefore the honest enumerator list is **ordinals with two display names**:

```
POINT_INFO_TYPE = 1   slot 0   (no shipped label)   -- unidentified
POINT_INFO_TYPE = 2   slot 1   GVG_한번의 공격으로 격퇴   -- first-attack defeat
POINT_INFO_TYPE = 3   slot 1   GVG_두번의 공격으로 격퇴   -- second-attack defeat
POINT_INFO_TYPE = 4   slot 2   (no shipped label)   -- unidentified
POINT_INFO_TYPE = 5   slot 3   (no shipped label)   -- unidentified
```

No enumerator *name* is guessed for 1, 4 or 5, and none should be.

## 1.9 Method notes — three resolver defects hit, so the next pass does not repeat them

The offline Thumb PIC-literal pattern here is
`ldr rX,[pc,#imm]` … (usually **one** intervening instruction) … `add rX,pc`.
Three separate real bugs were made and caught, each of which produced
plausible-but-wrong *strings* rather than a clean miss — the most dangerous failure
mode per `AGENTS.md` §16.7 item 1:

1. **Thumb-1 `ldr`'s Rd is bits 10–8, not bits 2–0.** Reading `op & 7` gave the
   wrong register and silently killed every pairing.
2. **Two different bases.** The literal *slot* is at
   `Align(ldr_va+4,4) + 4*imm`, while the *value* is
   `u32(slot) + (add_va + 4)`. Conflating them shifts every string by 4 bytes.
3. **For the 16-bit `add rX,pc` form, PC == `add_va + 4` with NO 4-byte
   alignment.** Using `Align(add_va+4,4)` is correct for some slots and wrong for
   others, which is what produced a clean-looking `"TX_POINT"` from one slot and
   mid-Korean garbage from another.

Rules that made the resolver trustworthy here, and should be kept:

- Pool slots hold **pre-bias addends**. Reading the `.so` directly and treating
  the word as a pointer yields garbage — exactly the `AGENTS.md` §11 warning.
  > ⚠️ **CORRECTED 2026-10-05 (address-convention pass).** This bullet previously
  > read "there are **no `R_ARM_RELATIVE` entries at all** … **128,620
  > `R_ARM_NONE`** … `R_ARM_RELATIVE` count = 0". **Both the type name and the
  > conclusion were wrong.** The *count* was right and the *label* was wrong: the
  > histogram of the 128,665 `DT_REL` records (`DT_REL` @ `0x515a10`,
  > `DT_RELSZ` = `0xfb4c8`, `DT_RELENT` = 8) is **128,620 `R_ARM_RELATIVE`
  > (`r_info & 0xff == 23`)** + 32 `R_ARM_GLOB_DAT` + 13 `R_ARM_ABS32`; **zero**
  > `R_ARM_NONE`. (`.rel.plt` adds 379 `R_ARM_JUMP_SLOT`.) So the binary carries a
  > **very large** relocation table — the largest in this project.
  >
  > **The operative conclusion nevertheless survives, on stronger evidence:** a
  > section-level classification of all 128,620 `R_ARM_RELATIVE` targets shows
  > **0 in `.rodata` and 0 in `.text`**. Every one lands in a writable segment —
  > `.data.rel.ro` 103,052, `.data.rel.ro.local` 10,991, `.got` 7,785, `.data`
  > 6,393, `.init_array` 397, `.fini_array` 2. `.rodata` literal-pool slots are
  > therefore genuinely **unrelocated**, so a pool word *is* a pre-bias addend and
  > the bias must come from the `add rX,pc` register. The old text reached the
  > right rule by counting the wrong relocation type; do not repeat that
  > inference. **Never infer "no relocations" from a total count** — read
  > `r_info & 0xff` and then map each `r_offset` to a section.
  >
  > This same 128,620-entry table is also what makes `native-all-strings.tsv`
  > differ from the on-disk file in its writable-data rows; see
  > [`address-convention-2026-10-05.md`](address-convention-2026-10-05.md) §3,
  > where applying these relocations with bias `0x10000` takes the string-index
  > byte-verification from 99.78 % to **515,576 / 515,576 = 100.0000 %**.
- Require the resolved target to be a NUL-terminated printable run **preceded by a
  NUL byte**. That single check is what exposed bugs 2 and 3.
- **Validate the resolver against known ground truth before trusting a sweep.**
  Done: the sweep reproduces all five `SetData` strings (`RE_POINT1`, `TX_POINT`
  ×2, and both GVG keys) exactly, before being used anywhere else.
- Bounds: `max_gap = 3` instructions, same-register required, no branch or
  clobber in between. Per `AGENTS.md` §41, only register-proven pairings were
  accepted.

An earlier whole-`.text` byte scan for `cmp rX,#4` + `tbb` was also run and
**discarded as useless** (the `0x04 0x29` byte pair matched ~2000 unrelated
sites). No claim in this document rests on it. There is exactly one
`SetData(pair<POINT_INFO_TYPE,int>)` in the dynamic symbol table, so "one switch
site" is established from the symbol table, not from that scan.

---

# SECTION 2 — UNPURE

**Every numeral in this section is impure.** Era tags per
`stat-version-context.md` (threshold **2019-09-05**), following
`blitz-search-consumers-2026-10-05.md`:

- **[BINARY]** — a native literal/field/address from this build. The binary is the
  build under study and carries no independent date, but GVG is absent from
  1.4.4.1, so it is by construction 2.8-era.
- **[DB-2.8.0.1]** — recovered `UI_TEXT_RO` rows. Same client lineage,
  post-threshold.

## 2.1 The attempt-count numerals are now bound to enumerators — and that is display copy

This is the **one** new impure binding this pass produces.

| numeral | bound to | evidence | era |
|---|---|---|---|
| **1** | `POINT_INFO_TYPE = 2` | localized key `GVG_한번의 공격으로 격퇴` ("…in **one** attack") fetched by the value-2 branch at `0x00c79e06`; EN "First Attempt" per the sibling note §1.6 | [BINARY] key + [DB-2.8.0.1] EN |
| **2** | `POINT_INFO_TYPE = 3` | localized key `GVG_두번의 공격으로 격퇴` ("…in **two** attacks") fetched by the value-3 branch at `0x00c79e84`; EN "Second Attempt" per the sibling note §1.6 | [BINARY] key + [DB-2.8.0.1] EN |

Why impure, and why it still does not license a fixture:

- The ordinal is **hard native evidence**; the *meaning* attached to it is a
  **localized display string**, i.e. shipped copy. A display key is a weak binding
  — the same class of evidence as §16's `CONTENTS15_8` prose.
- The numerals are the **attack counts 1 and 2**, which is *not* the same quantity
  as the sibling note's §2.1 rows 3–6. Those rows pair "1st-attack bonus" with
  **50** and "2nd-attack bonus" with **25**. This pass confirms *which enumerator*
  is the 1st-attempt kind and which is the 2nd-attempt kind; it recovers **no
  magnitude**.
- A `point_id` arriving as `2` from the server is consistent with, but does **not
  prove**, "1st-attempt points = 50".

## 2.2 What is still NOT recovered — explicitly

- **No point magnitude anywhere.** None of `150`, `25`, `50`, `5`, `2250`, `450`
  is bound to any enumerator by this pass, and none appears in the binary as a GVG
  constant. `2250` still has no data source of any kind.
- **`multi` is a multiplier, still valueless.** §1.6 confirms the field and its
  wire position; no value is known.
- **`val` is newly named but unvalued** (§1.6). Its role relative to `multi`
  (base amount × multiplier?) is **not established** — that is an inference, and
  it is withheld.
- **Values 1, 4 and 5 have no shipped name at all.** Any assignment of
  "surviving hunter", "undeployed unit", "occupied camp", "deployed defense team"
  or "2250-double rear area" to those three would be **invented**. The sibling
  note's §2.1 mapping of the 12-numeral help table onto point kinds remains
  **unproven**, and this pass neither confirms nor refutes it — it only shows the
  enum has room for exactly five kinds, and that two of them are the
  attack-count kinds.

## 2.3 Unchanged from the sibling note — restated so nothing is silently carried

- The **10-camp roster** and the **4000 Strength deployment floor** remain the only
  two numerals a `/gvg/GetRef` fixture may legitimately take from shipped
  evidence. This pass found no new numeral that changes that.
- `min_entry_cnt` must stay a **field**, not a literal 10.
- The source note's §2.1 twelve numerals **must not** be imported into a fixture.

## 2.4 Coverage

**Zero coverage credit. Nothing changes.** Strict coverage remains
**heroes 1/113, accessories 1/100, monsters 0/22** (`coverage.md`). Guild Blitz
scoring is not a hero, jewel, accessory or monster stat. The broader 70% goal is
untouched by this pass.

---

# SECTION 3 — Limits

- **No Ghidra run.** Ghidra was parent-owned and locked. Everything here is
  instruction-level reading from `llvm-objdump` plus `.rel.dyn`/symbol-table
  cross-checks. The `tbb` decode was validated by uniqueness of the base, not by
  a decompiler.
- **`point_id` → enum is not a proven assignment instruction.** I established that
  `point_id` is read as a generic JSON number and that the win popup switches over
  a 5-value type, and that the two share the `BATTLE_INFO` object. I did **not**
  trace the exact store that copies `point_id` into the `POINT_INFO_TYPE` field, so
  "value 2 on the wire ⇒ label 'first attack'" is a **strong but unproven** link.
  A Ghidra pass on the `point_detail` row store would close it.
- **No enumerator names.** §1.8. Not recoverable from this artefact set at all.
- **The `k = 1` collision between values 2 and 3 is reported as observed machine
  behaviour only.** No interpretation is offered.
- **`val` vs `multi` semantics unproven.** See §2.2.
- **LevelDB not re-read.** The EN "First Attempt"/"Second Attempt" renderings are
  cited from the sibling note, not independently re-verified here. The KO keys
  were read directly from the `.so`.
- **No server, fixture, catalogue, seed, state, APK, LevelDB, emulator or phone
  action. No `polluted-observations.md` append.**
