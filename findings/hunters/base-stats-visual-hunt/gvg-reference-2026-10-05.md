# GVG (Guild Blitz) reference contract — offline native recovery (2026-10-05)

**Read-only.** No `server-ts` code, fixture, test, state file, APK, seed, LevelDB,
release or emulator was created, modified, opened or executed. Exactly one file is
written: this one. `polluted-observations.md` is deliberately **not** appended — the
parent mirrors.

**No `/gvg/*` handler was implemented**, per instruction. §3.1 records what the
replica does today so a future implementer knows the exact gap.

**Zero coverage credit.** Strict base-stat coverage is unchanged at heroes 1/113,
accessories 1/100, monsters 0/22 (`coverage.md`). Nothing here is a hero, jewel,
accessory or monster stat. Per `AGENTS.md` §15, recovered / fixture / unknown are
marked separately throughout.

**Result in one line: the `/gvg/GetRef` key list is fully recovered from the
original `libnative_core.so`, and `point_id` + `multi` is proven to be a single
row triple — but not one balance value is recovered.**

---

## 0. Sources, method, and two corrections that must be read first

### 0.1 Sources used

| source | identity |
|---|---|
| `analysis/extracted/lib/armeabi-v7a/libnative_core.so` | the **original** extracted ARM32 library, 35 445 748 bytes. Read only; no copy written, no patch applied |
| `llvm-nm -D --print-size --defined-only` (NDK 29.0.14206865) | 49 995 defined dynamic symbols; ELF VAs and sizes |
| Capstone 5.0.7 (`tools/python-venv`) | Thumb-2 disassembly with operand detail |
| `analysis/native-all-strings.tsv` | 515 576-entry string index, used only as a **cross-check** (see §0.3) |
| `analysis/native-evidence.tsv` | not needed; dynsym was regenerated directly from the `.so` |

Helper scripts lived in `%LOCALAPPDATA%\Temp\opencode` and were transient. They
are deliberately **not** added to the repo, because the method below has one sharp
edge (§0.4) that a future run must re-derive rather than inherit blindly.

### 0.2 CORRECTION 1 — `analysis/native-all-strings.tsv` addresses are **Ghidra**, not ELF

`blitz-search-consumers-2026-10-05.md` §"Provenance" states "addresses are ELF
VAs". **That is wrong**, and it matters. Verified byte-exactly:

```
/gvg/GetRef
  native-all-strings.tsv address : 0x01d79394
  ELF VA of the same bytes       : 0x01d69394      (d[0x01d69394] == b'/gvg/GetRef\x00')
  delta                          : 0x10000
```

Spot-checked on five independent strings (`/gvg/GetInst`, `/gvg/GetRef`,
`min_entry_cnt`, `point_id`, `multi`) — all exactly `0x10000` lower in the ELF.
This is the `AGENTS.md` §16.7 lesson-3 rule (`Ghidra = ELF + 0x10000`) applied to
the TSV. **Consequence:** any address quoted from that TSV must have `0x10000`
subtracted before it can be fed to `llvm-objdump`/`llvm-nm`. This report quotes
**both** conventions and labels every one.

### 0.3 CORRECTION 2 — `ReqGVGRefCB at 0x003600f0` is a string address, not code

`blitz-search-consumers-2026-10-05.md` line 203-206 and the task brief both place
`ReqGVGRefCB` at `0x003600f0`. Disassembly at that address is mid-instruction
garbage:

```
003600f0: 4544  add r5, r8          <- not a function entry
003600f2: 3245  cmp r2, r6
003600f4: 7600  lsls r6, r6, #1
```

`0x003600f0` is where `native-all-strings.tsv` indexes the **mangled name string**
in `.dynstr` (the TSV contains both `.rodata` literals and `.dynstr` symbol names
— that dual content is itself worth knowing). The real function:

```
ELF 0x00f7525c   Ghidra 0x00f8525c   size 0x34   Thumb
00f7525c: b0b5       push    {r4, r5, r7, lr}
00f7525e: 02af       add     r7, sp, #8
00f75260: 1068       ldr     r0, [r2]            ; res->result_code
00f75262: 1c46       mov     r4, r3              ; the json envelope
00f75264: 20b1       cbz     r0, #0xf75270
00f75266: 69f447f4   bl      #0x7deaf8           ; helper
00f7526a: 0128       cmp     r0, #1
00f7526c: 18bf       it      ne
00f7526e: b0bd       popne   {r4, r5, r7, pc}    ; EARLY RETURN if != 1
00f75270: 30f794f7   bl      #0xaa619c           ; CSRGuildBattleMgr::get()
00f75274: 0549       ldr     r1, [pc, #0x14]      <<'ret_data'>  ELF 0x1d589bb
00f75276: 0546       mov     r5, r0              ; save manager
00f75278: 2046       mov     r0, r4              ; envelope
00f7527a: 7944       add     r1, pc
00f7527c: 0df43cf7   bl      #0x7830f8           ; json::operator[](const char*)
00f75280: 0146       mov     r1, r0              ; r1 = envelope["ret_data"]
00f75282: 2846       mov     r0, r5              ; r0 = manager
00f75284: bde8b040   pop.w   {r4, r5, r7, lr}
00f75288: 1df7e6b7   b.w     #0xa93258           ; TAIL CALL CSRGuildBattleMgr::ParseRef
```

### 0.4 Method — pairing-free literal recovery, and the false positives it must reject

This build emits Thumb PIC string references in exactly one idiom:

```
ldr   r1, [pc, #0x2e8]     ; loads a SIGNED 32-bit OFFSET from a literal slot
add   r1, pc               ; r1 = offset + (address_of_add + 4)  -> .rodata VA
bl    <nlohmann::json::operator[](const char*)>   ; or another consumer
```

The literal slot does **not** contain the string address, so a naive
"literal-slot → string" reader finds nothing (that is what
`tools/resolve-literals-offline.py` style tooling gets wrong). Recovery is:
compute the slot from the encoding, read the signed offset, then require a
**same-register `add rX, pc`** to relocate it.

Two verifications make this safe against the `AGENTS.md` §16.7 lesson-1 failure
mode (a wrong **string key**, the worst possible outcome here):

1. **The pairing must be the same register**, bounded to 10 forward
   instructions, and must not cross any `b`/`cb`/`tbb`. In practice `add rX,pc`
   is 1–3 instructions after the `ldr`; instances like
   `ldr r0,[pc,#0x2f4] / mov sl,r1 / add r0,pc` are real and are why an
   "immediately preceding" rule under-reads.
2. **Every result must land on a real printable NUL-terminated string read
   directly out of the ELF.** A mis-pairing produces a garbage address that is
   almost never printable text. `.rodata` strings were read from ELF bytes, not
   from `native-all-strings.tsv`, because the TSV **omits short strings** — it has
   no entry for `"id"` anywhere, which is one of the recovered keys.

**Honest record of a rejected method.** A faster byte-level sweep of all of
`.text` (pattern-matching `ldr rX,[pc,#imm8]` + `add rX,pc` without decoding)
returned apparent hits for `my_101`, `my_110`, `enemy_101`, `enemy_110` at
addresses that, on real disassembly, are `cbz`, `str` and `movs` — **false
positives from decoding a misaligned instruction stream**. Those four results were
discarded; the real consumers were then found with the capstone method and are
reported in §1.9. The lesson generalises: *a literal-pool scan that does not
decode is a hypothesis, not evidence.* This is the same class of error as
lesson 1, reached from the opposite direction.

### 0.5 Symbol → function identity used throughout

| mangled symbol | ELF VA | Ghidra VA | size | Thumb |
|---|---|---|---|---|
| `CSRSyncRef::ReqGVGRefCB(...)` | `0x00f7525c` | `0x00f8525c` | `0x34` | yes |
| `CSRGuildBattleMgr::get()` | `0x00aa619c` | `0x00ab619c` | `0x64` | yes |
| `CSRGuildBattleMgr::ParseRef(const json&)` | `0x00a93258` | `0x00aa3258` | `0x6` | yes |
| `CSRGuildBattleMgr::BATTLE_INFO::parse(const json&)` | `0x00a93260` | `0x00aa3260` | `0xd88` | yes |
| `CSRGuildBattleMgr::BATTLE_INFO::_CAMP::parse(const json&)` | `0x00aa2d7c` | `0x00ab2d7c` | `0x3e8` | yes |
| `CSRGuildBattleMgr::BATTLE_INFO::_CAMP::dump()` | `0x00aa5768` | `0x00ab5768` | `0x2c4` | yes |
| `CSRGuildBattleMgr::INFO::parse(const json&)` | `0x00aa5a2c` | `0x00ab5a2c` | `0x770` | yes |
| `CSRGuildBattleMgr::INFO::dump()` | `0x00aa6200` | `0x00ab6200` | `0x7b0` | yes |
| `CSRGuildBattleMgr::PLAY_DATA::parse(const json&)` | `0x00aa3758` | `0x00ab3758` | `0xabc` | yes |
| `CSRGuildBattleMgr::PLAY_DATA::dump()` | `0x00aa4884` | `0x00ab4884` | `0x67c` | yes |
| `CSRGuildBattleMgr::CARD::parse(const json&)` | `0x00aa4214` | `0x00ab4214` | `0x670` | yes |
| `CSRGuildBattleMgr::CARD::dump() const` | `0x00aa4f00` | `0x00ab4f00` | `0x868` | yes |
| `CSRGuildBattleMgr::CARD_SUMMARY::parse(const json&)` | `0x00aa6b80` | `0x00ab6b80` | `0x32c` | yes |
| `CSRGuildBattleMgr::CARD_SUMMARY::dump()` | `0x00aa6eac` | `0x00ab6eac` | `0x330` | yes |
| `CSRGuildBattleMgr::BATTLE_PAIR::parse(const json&)` | `0x00aa69b0` | `0x00ab69b0` | `0x98` | yes |
| `CSRGuildBattleMgr::BATTLE_PAIR::dump()` | `0x00aa6a48` | `0x00ab6a48` | `0x138` | yes |
| `CSRGuildBattleMgr::CAMP_INFO::parse(const json&)` | `0x00aa71dc` | `0x00ab71dc` | `0x7f4` | yes |
| `CSRGuildBattleMgr::CAMP_INFO::dump()` | `0x00aa79d0` | `0x00ab79d0` | `0x694` | yes |
| `CSRGuildBattleMgr::ParseReward(const json&)` | `0x00aa0818` | `0x00ab0818` | `0xd28` | yes |
| `CSRGuildBattleMgr::RequestRef(cb, bool)` | `0x00a925cc` | `0x00aa25cc` | `0xc06` | yes |
| *(unnamed)* camp-slot-name response parser, prologue | `0x00aad354` | `0x00abd354` | ≥ `0x5d4` | yes |
| *(unnamed)* point-log response parser, prologue | `0x00aaf880` | `0x00abf880` | ≥ `0x780` | yes |

Two are **not** in dynsym with usable bounds: the last two are static/local
functions. For the camp-slot parser dynsym reports a
`std::__tree<..., std::shared_ptr<...>>` template instantiation at
`0x00aaf1fc` with a bogus size `0xc2`; the real prologue was found by walking
backwards for `push {…, lr}`. Their true owning classes are **unknown** (§3.3).

Two helper targets used to type the key consumers:

| target | symbol |
|---|---|
| `0x7830f8` | `nlohmann::json::operator[](const char*) const` |
| `0x8304d8` | `std::__tree<…, std::string, nlohmann::json, …>::operator[]` (non-const form) |
| `0x718b08` | `nlohmann::detail::from_json<…, nlohmann::json::string_t>` (a string field) |
| `0x71af38` / `0x71aff0` | `nlohmann::detail::iter_impl::operator!=` / `operator*` — **array iteration** |
| `0x997d24` | `nlohmann::detail::iter_impl::operator++` |
| `0x6c5ff4` | `std::string::string(const char*)` |

---

# SECTION 1 — PURE: exact key lists and addresses

Pure = verbatim bytes, verbatim disassembly, verbatim ELF strings, verified
symbol addresses. No balance claim, no era inference, no fixture conclusion.

## 1.1 The `/gvg/GetRef` call chain — fully proven, end to end

`ParseRef` is a **6-byte thunk**, which is why it looked like it had no keys:

```
00a93258: 5030       adds  r0, #0x50      ; r0 = this + 0x50  (the BATTLE_INFO member)
00a9325a: 00f001b8   b.w   #0xa93260      ; TAIL CALL BATTLE_INFO::parse(this+0x50, json)
```

Full chain, each link read from the bytes:

```
  /gvg/GetRef                                  (literal at ELF 0x1d69394)
    -> CSRSyncRef::ReqGVGRefCB                 ELF 0x00f7525c
         if (result_code != 1) return          ; popne at 0x00f7526e
         mgr = CSRGuildBattleMgr::get()        ; bl 0x00aa619c
         j   = envelope["ret_data"]            ; ldr r1,[pc,#0x14] -> 'ret_data' ELF 0x1d589bb
                                             ; bl 0x7830f8  (json::operator[](const char*))
    -> CSRGuildBattleMgr::ParseRef             b.w 0x00a93258
         (this += 0x50)
    -> CSRGuildBattleMgr::BATTLE_INFO::parse   b.w 0x00a93260
         reads  j["gvg"]["…"]                  ; ELF 0x00a93280 loads 'gvg' (ELF 0x1d6952e)
```

**Two structural consequences, both load-bearing for any future fixture:**

- **`/gvg/GetRef` is the only GVG route with an exported reference callback.**
  A `llvm-nm -D` scan for `CSRSync.*(GuildBattle|GVG)` returns exactly one hit:
  `CSRSyncRef::ReqGVGRefCB`. The other 18 routes have **no named callback symbol**;
  their responses are consumed by local lambdas/unexported code (§3.3).
- **`BATTLE_INFO::parse` receives `ret_data`, not the envelope, and then indexes a
  `gvg` sub-object.** So the reference payload is nested one level deeper than a
  bare `ret_data` object. A `ret_data` without a `gvg` member leaves every field at
  its parse-time default (§3.1).

## 1.2 `/gvg/GetRef` — REQUEST keys (client → server)

From `CSRGuildBattleMgr::RequestRef` (ELF `0x00a925cc`, Ghidra `0x00aa25cc`), in
code order:

| # | Ghidra `.rodata` | ELF `.rodata` | key |
|---|---|---|---|
| 1 | `0x01d689d0` | `0x01d589d0` | `app_code` |
| 2 | `0x01d689d9` | `0x01d589d9` | `app_ver` |
| 3 | `0x01d689ee` | `0x01d589ee` | `market` |
| 4 | `0x01d686aa` | `0x01d586aa` | `pvid` |
| 5 | `0x01d689ea` | `0x01d589ea` | `otp` |
| — | `0x01d79394` | `0x01d69394` | route `/gvg/GetRef` |

**There is no gameplay parameter.** `/gvg/GetRef` carries the standard five-field
auth envelope only — no gvg id, no guild id, no season. That is a genuinely
useful negative: the reference table is global, not per-instance.

## 1.3 `/gvg/GetRef` — RESPONSE keys (server → client)

Envelope: `result_code` (must be `1`, else early return), then
`ret_data.gvg`.

From `BATTLE_INFO::parse` (ELF `0x00a93260`), keys in **code order** with the
exact load sites:

| # | Ghidra | ELF | key | note |
|---|---|---|---|---|
| 0 | `0x01d7952e` | `0x01d6952e` | `gvg` | the sub-object, `r6` |
| 1 | `0x01d676c3` | `0x01d576c3` | `id` | `j["gvg"]["id"]`, via `from_json<json::string_t>` |
| 2 | `0x01d79532` | `0x01d69532` | `min_entry_cnt` | |
| 3 | `0x01d79540` | `0x01d69540` | `teaser_begin_dtm` | |
| 4 | `0x01d79551` | `0x01d69551` | `register_begin_dtm` | |
| 5 | `0x01d79564` | `0x01d69564` | `matching_begin_dtm` | |
| 6 | `0x01d79577` | `0x01d69577` | `deploy_begin_dtm` | |
| 7 | `0x01d79588` | `0x01d69588` | `combat_begin_dtm` | |
| 8 | `0x01d79599` | `0x01d69599` | `calc_begin_dtm` | |
| 9 | `0x01d795a8` | `0x01d695a8` | `result_begin_dtm` | |
| 10 | `0x01d795b9` | `0x01d695b9` | `finish_dtm` | |
| 11 | `0x01d795c4` | `0x01d695c4` | `next_gvg_dtm` | |
| 12 | `0x01d6edc1` | `0x01d5edc1` | `reward` | consumed as a whole; sub-structure **not** resolved this pass |
| 13 | `0x01d795d1` | `0x01d695d1` | `min_cp` | |
| 14 | `0x01d795d8` | `0x01d695d8` | `max_cp` | |
| 15 | `0x01d795df` | `0x01d695df` | `inf_reward` | |
| 16 | `0x01d65900` | `0x01d55900` | `point` | |
| 17 | `0x01d643ff` | `0x01d543ff` | `val` | `j["gvg"]["point"][…]["val"]` |
| 18 | `0x01d676c3` | `0x01d576c3` | `id` | `j["gvg"]["point"][…]["id"]`, into `r6` |
| 19 | `0x01d74aa7` | `0x01d64aa7` | `camp` | rows handed to `_CAMP::parse`, §1.4 |

So the reference shape recovered is exactly:

```jsonc
{ "result_code": 1,
  "ret_data": {
    "gvg": {
      "id":              <string>,
      "min_entry_cnt":   <number>,
      "teaser_begin_dtm":  "register_begin_dtm": "matching_begin_dtm":
      "deploy_begin_dtm":   "combat_begin_dtm": "calc_begin_dtm":
      "result_begin_dtm":   "finish_dtm": "next_gvg_dtm":      <server datetimes>,
      "reward":          <?>,
      "min_cp": "max_cp": <?>,
      "inf_reward":      <?>,
      "point": [ { "val": <n>, "id": <n> }, … ],
      "camp":  [ { "min_cp": …, "camp_id": …, "name": …, "link_camp": … }, … ]
    }
  } }
```

**Types are deliberately left as `<?>`/`?`.** For every numeric field the parse
site contains a `tbb` type-dispatch on the nlohmann value type (null / boolean /
number-float / number-uint / number-int / string / object / array) followed by a
conversion — the same tolerant pattern used elsewhere in this codebase
(`search-effect-root-contract.md`, `arena-*`). The **widest safe** shape is
therefore a JSON number; whether each field is `uint32` or `double` was not
pinned and must not be guessed.

## 1.4 `BATTLE_INFO::_CAMP::parse` — the `camp[]` row

ELF `0x00aa2d7c`, Ghidra `0x00ab2d7c`:

| # | Ghidra | ELF | key |
|---|---|---|---|
| 1 | `0x01d795d1` | `0x01d695d1` | `min_cp` |
| 2 | `0x01d7943e` | `0x01d6943e` | `camp_id` |
| 3 | `0x01d63176` | `0x01d53176` | `name` |
| 4 | `0x01d79683` | `0x01d69683` | `link_camp` |

**`name` is NOT the same thing as the literal `" name"`.** Both appear in this
function and the distinction matters:

```
00aa2e46: <'name'>  r1  ; consumed by json::operator[]  -> a real key
00aa2e02: 2d6f7361 <' name'> r2
00aa2e04: 7a44       add  r2, pc
00aa2e12: 0bf40bfe   bl   #0x6caa2c      ; std::string helper, r0 = dest, r1 = json["camp_id"]
```

`" name"` (leading space, ELF `0x01d6967d`) is a **concatenation suffix** used to
build a display/lookup name from `camp_id`. It is **not** a JSON key and must
never be sent as one. `_CAMP::dump` confirms the field set:
`camp_id`, `min_cp`, `name`, `link_camp`.

## 1.5 `point_id` + `multi` — the decisive pair, now a proven triple

The task brief and `blitz-search-consumers` §1.3 record `point_id` (`0x01d7985b`)
and `multi` (`0x01d79864`) as *adjacent `.rodata` literals* and explicitly flag
that "the `point_id`/`multi` adjacency is `.rodata` adjacency, not a proven parse
pair" (`§4` of that file). **This pass closes that gap.**

A capstone decode of the surrounding region shows each of the four literals
resolved from **exactly one** load site, and all four inside **one function**, the
three row keys 8 and 6 bytes apart and all feeding the same receiver:

| key | Ghidra | ELF | sole consumer (Ghidra) |
|---|---|---|---|
| `point_detail` | `0x01d7984e` | `0x01d6984e` | `0x00abfa6a` |
| `point_id` | `0x01d7985b` | `0x01d6985b` | `0x00abfb3a` |
| `val` | `0x01d643ff` | `0x01d543ff` | `0x00abfb42` |
| `multi` | `0x01d79864` | `0x01d69864` | `0x00abfb48` |

Verbatim, at ELF `0x00aafb34`:

```
00aafb34: add.w r0, fp, #0x198
00aafb38: str   r0, [sp, #0x34]
00aafb3a: ldr   r0, [pc, #0xb4]   <<'point_id'>>   ; add r0,pc ; mov sb, r0
00aafb42: ldr   r0, [pc, #0xb0]   <<'val'>>        ; add r0,pc ; mov sl, r0
00aafb48: ldr   r0, [pc, #0xac]   <<'multi'>>      ; add r0,pc ; mov r8, r0
00aafb4e: b     #0xaafb66
  …
00aafb66: mov   r0, r4                     ; r4 = the CURRENT ROW
00aafb68: bl    #0x71aff0                  ; iter_impl::operator*  -> the row
00aafb6c: mov   r1, sb                     ; r1 = "point_id"
00aafb6e: mov   r5, r0
```

**Conclusion (pure): a `point_detail` row is exactly `{ point_id, val, multi }`,
all three read from the same object.** `point_id` is an enumerated kind and
`multi` the multiplier, matching
`CSRPopUpGuildBattleWin::SetPointListData(const std::list<std::pair<POINT_INFO_TYPE,int>>&)`
(`.dynsym` **ELF `0x00c79844` / Ghidra `0x00c89844`**, `T`, size `0x56c`) and
`CSRCellGuildBattleCard::SetCombatPoint(int)` (ELF `0x0087fd9c`). The
`std::to_string` specialisation for `POINT_INFO_TYPE` also exists but its
enumerator table is unreadable from disk — see §1.11.

`point_detail` is a **JSON array**: the loop uses
`iter_impl::operator!=` (`0x71af38`) at `0x00aafb5c` and
`iter_impl::operator*` (`0x71aff0`) at `0x00aafb68`.

## 1.6 The full point-log response shape

Same function (prologue ELF `0x00aaf880` / Ghidra `0x00abf880`), all keys:

| # | Ghidra | ELF | key | consumer |
|---|---|---|---|---|
| 1 | `0x01d689bb` | `0x01d589bb` | `ret_data` | `std::__tree<…>::operator[]` |
| 2 | `0x01d6ef58` | `0x01d5ef58` | `user` | nested object |
| 3 | `0x01d79635` | `0x01d69635` | `offense_point` | under `user` |
| 4 | `0x01d79643` | `0x01d69643` | `defense_point` | under `user` |
| 5 | `0x01d7984e` | `0x01d6984e` | `point_detail` | array |
| 6 | `0x01d7985b` | `0x01d6985b` | `point_id` | per row |
| 7 | `0x01d643ff` | `0x01d543ff` | `val` | per row |
| 8 | `0x01d79864` | `0x01d69864` | `multi` | per row |
| 9 | `0x01d74aa7` | `0x01d64aa7` | `camp` | |
| 10 | `0x01d7146f` | `0x01d6146f` | `order` | |
| 11 | `0x01d7970b` | `0x01d6970b` | `card_%d` | **format string**, see §1.7 |
| 12 | `0x01d6edf2` | `0x01d5edf2` | `ref_id` | per card |

This is the shape of a **per-camp clear-point log** (`user` wrapper +
`offense_point`/`defense_point` totals + an itemised `point_detail` array), i.e.
the response family behind `GetCampClearPointLog` and/or `GetResult`. Rows 9–12
are read **later in the same function** than rows 1–8; their nesting (under
`point_detail`, under a per-camp object, or a sibling list) was **not**
established in this pass and must not be assumed. `card_%d` is a **format
string**, not a key (§1.7). Its presence here shows the point-log parser *builds*
its card-row names by formatting (`card_%d`), whereas `CAMP_INFO::parse` builds
the same names by `std::string("card_")` plus an index (§1.7) — two routes, one
naming convention, `card_<1..4>`.

Which specific route wires to this function is **[UNKNOWN]** (§3.3) — the owning
class is not in dynsym and there are no `bl` callers of `0x00aaf880` (verified by
a full `.text` branch-target scan), so it is reached through a function pointer.
The pointer **is** locatable: the 4-byte value `0x00aaf881` (Thumb bit set) sits
at VA `0x021507dc`, inside a vtable whose neighbours are
`0x00aaf749`, `0x00aaf7d9`, `0x00aaf82d`, `0x00aaf881`, `0x00ab0159`,
`0x00ab0171` — i.e. a small class with six virtuals in that region.

## 1.7 `camp`, `order` and the four `card_` slots

`CAMP_INFO::parse` (ELF `0x00aa71dc`) is the one GVG parser that indexes
**`ret_data` then `camp`**, i.e. it takes the **full envelope**:

| # | Ghidra | ELF | key | reg |
|---|---|---|---|---|
| 1 | `0x01d689bb` | `0x01d589bb` | `ret_data` | r1 |
| 2 | `0x01d74aa7` | `0x01d64aa7` | `camp` | r1 |
| 3 | `0x01d7146f` | `0x01d6146f` | `order` | r0 |
| 4 | `0x01d686aa` | `0x01d586aa` | `pvid` | r1 |
| 5 | `0x01d796d5` | `0x01d696d5` | `defense_cnt` | r2 |
| 6 | `0x01d796e1` | `0x01d696e1` | `challenger` | r1 |
| 7 | `0x01d79669` | `0x01d69669` | `card_` | r1 |
| 8 | `0x01d70531` | `0x01d60531` | `occupied` | r1 |
| 9 | `0x01d704df` | `0x01d604df` | `empty` | r1 |
| 10 | `0x01d704f2` | `0x01d604f2` | `deploying` | r1 |
| 11 | `0x01d796ec` | `0x01d696ec` | `point_list` | r1 |
| 12 | `0x01d686aa` | `0x01d586aa` | `pvid` | r0 |
| 13 | `0x01d796f7` | `0x01d696f7` | `total_point` | r0 |
| 14 | `0x01d79703` | `0x01d69703` | `reg_dtm` | r0 |
| 15 | `0x01d69740` | `0x01d59740` | `nickname` | r1 |

`CAMP_INFO::dump` corroborates: `order`, `pvid`, `defense_cnt`, `challenger`,
`card_%d`, `camp`, `pvid`, `total_point`, `reg_dtm`, `nickname`, `point_list`.

**The `card_` key is a prefix, and the loop bound is four slots.** Read from the
bytes at ELF `0x00aa74ae`:

```
00aa74ae: blx    #0xdfb634
00aa74b2: add.w  r4, sl, #0x20
00aa74b6: movs   r6, #1            <- slot index starts at 1
00aa74b8: strd   r0, r1, [sl, #8]
00aa74bc: b      #0xaa74d4         <- loop head
  …
00aa74cc: adds   r6, #1
00aa74ce: adds   r4, #0x34         <- stride 0x34 per card slot
00aa74d0: cmp    r6, #5
00aa74d2: beq    #0xaa7558         <- EXIT when index == 5
00aa74d4: ldr    r1, [pc, #0x7c]   <<'card_'>  ELF 0x01d69669
00aa74d6: add    r1, pc
00aa74d8: mov    r0, r5
00aa74da: bl     #0x6c5ff4         ; std::string::string(const char*) -> "card_"
```

The index takes values **1, 2, 3, 4** before the `#5` exit, so **four** card
slots per camp row; `CAMP_INFO::dump` renders the same slots through the
`card_%d` format literal (ELF `0x01d6970b`). `PLAY_DATA::parse`/`dump` carry the
same `camp_id` / `order` / `card_` triple (dump adds `thumb_prefix` and
`skin_ref_id` for `CARD`), so `card_<1..4>` is a shared GVG convention.

Note `occupied` / `empty` / `deploying`: these are **wire strings**, not just UI
vocabulary. They are `r1` arguments to the key accessor, i.e. a camp row carries
a status **string**, and `CAMP_STATUS` is a named enum
(`_CCellGBPoint::SetPoint(const std::string&, CSRGuildBattleMgr::INFO::CAMP_STATUS&)`,
dynsym ELF `0x00c60fc4`).

## 1.8 `PLAY_DATA`, `CARD`, `CARD_SUMMARY`, `BATTLE_PAIR`, `INFO`

**`PLAY_DATA::parse`** (ELF `0x00aa3758`) — no `ret_data`, so it takes an
already-unwrapped object:

| Ghidra | ELF | key |
|---|---|---|
| `0x01d79615` | `0x01d69615` | `enemy_guild_id` |
| `0x01d79624` | `0x01d69624` | `inf_gvg` |
| `0x01d6ef58` | `0x01d5ef58` | `user` |
| `0x01d78c2d` | `0x01d68c2d` | `guild_id` |
| `0x01d7962c` | `0x01d6962c` | `total_cp` |
| `0x01d79635` | `0x01d69635` | `offense_point` |
| `0x01d79643` | `0x01d69643` | `defense_point` |
| `0x01d79651` | `0x01d69651` | `commander` |
| `0x01d6edfd` | `0x01d5edfd` | `card_list` |
| `0x01d7965b` | `0x01d6965b` | `deployed_list` |
| `0x01d7943e` | `0x01d6943e` | `camp_id` |
| `0x01d7146f` | `0x01d6146f` | `order` |
| `0x01d79669` | `0x01d69669` | `card_` |

`PLAY_DATA::dump` emits the **same thirteen names**, only reordered
(`inf_gvg`, `guild_id`, `total_cp`, `offense_point`, `defense_point`,
`commander`, `user`, `card_list`, `camp_id`, `order`, `card_`, `enemy_guild_id`,
`deployed_list`), so the parse and dump field sets agree exactly.

**`CARD::parse`** (ELF `0x00aa4214`): `ref_id`, `level`, `overcome_cnt`, `cp`,
`awk_step`, `awk_overcome`, `enemy_camp_id`, `remain_hp`, `skin_id`,
`skill_level`. `CARD::dump` adds `skin_ref_id` and `thumb_prefix` (client-side
rendering fields, not necessarily wire fields).

**`CARD_SUMMARY::parse`** (ELF `0x00aa6b80`): `ref_id`, `rank`, `level`,
`overcome_cnt`, `remain_hp`, `cp`, `awk_step`, `awk_overcome`, `skin_id`. So
`CARD_SUMMARY` = `CARD` minus `enemy_camp_id`/`skill_level`, plus `rank`.
`CARD_SUMMARY::dump` matches.

**`BATTLE_PAIR::parse`** (ELF `0x00aa69b0`) and `dump` (ELF `0x00aa6a48`) both
yield exactly three keys: `max_deck_cnt`, `my`, `enemy`. So the per-camp pairing
is `{ my: <row>, enemy: <row> }` with a shared `max_deck_cnt`. `my` is ELF
`0x01d693e2`, `enemy` is ELF `0x01d67246`.

**`INFO::parse`** (ELF `0x00aa5a2c`) — 16 keys, corroborated field-for-field by
`INFO::dump` (ELF `0x00aa6200`): `guild_id`, `guild_name`, `total_cp`, `point`,
`icon_url`, `message`, `type`, `msg`, `camp_status`, `mvp`, `pvid`, `nickname`,
`profile`, `deploy_cnt`, `survive_cnt`, `remain_hp`. `INFO` is the per-guild
summary record; `message`/`type`/`msg` are the guild-message triple.

**`ParseReward`** (ELF `0x00aa0818`) — the reward/wallet receipt, 16 keys:
`update`, `contribution`, `rupee`, `ap`, `ap_charge_time`, `bp`,
`bp_charge_time`, `honor`, `vip_exp`, `iap`, `free_iap`, `add`, `item`,
`ref_id`, `inst_id`, `qty`. Note the shape: **`ap_charge_time` / `bp_charge_time`
are siblings of `ap` / `bp`, not nested inside them** — this is the opposite of
the mission `Complete` contract, where `ap_charge_time` sits *inside* `ap`
(`AGENTS.md` §16.5 / `arena-battle-contract.md`). Recorded because it is exactly
the kind of nesting a fixture author would get wrong. `rupee` and `contribution`
are flat scalars here.

## 1.9 The twenty camp-slot keys, all in one function

The task brief and `blitz-search-consumers` §1.3 list
`my_101…my_110` / `enemy_101…enemy_110` as literals. Confirmed as **genuine
wire keys**, all read by a **single function** (prologue ELF `0x00aad354`, Ghidra
`0x00abd354`), each looked up exactly twice:

```
ELF 0x00aad562 / 0x00aad57c  my_101      ELF 0x00aade88 / 0x00aadea2  enemy_101
ELF 0x00aad642 / 0x00aad65c  my_102      ELF 0x00aadf68 / 0x00aadf82  enemy_102
ELF 0x00aad748 / 0x00aad762  my_103      ELF 0x00aae048 / 0x00aae062  enemy_103
ELF 0x00aad828 / 0x00aad842  my_104      ELF 0x00aae128 / 0x00aae142  enemy_104
ELF 0x00aad908 / 0x00aad922  my_105      ELF 0x00aae228 / 0x00aae242  enemy_105
ELF 0x00aad9e8 / 0x00aada02  my_106      ELF 0x00aae308 / 0x00aae322  enemy_106
ELF 0x00aadae8 / 0x00aadb02  my_107      ELF 0x00aae3e8 / 0x00aae402  enemy_107
ELF 0x00aadbc8 / 0x00aadbe2  my_108      ELF 0x00aae4c8 / 0x00aae4e2  enemy_108
ELF 0x00aadca8 / 0x00aadcc2  my_109      ELF 0x00aae5c8 / 0x00aae5e2  enemy_109
ELF 0x00aadd88 / 0x00aadda2  my_110      ELF 0x00aae6a8 / 0x00aae6c2  enemy_110
```

Same function also reads, in order: **`ret_data`** (ELF `0x01d589bb`),
**`message`** (ELF `0x01d59749`), **`main`** (ELF `0x01d6875f`) — then the
twenty slots. The leading keys sit at ELF `0x00aad3b0` / `0x00aad428` /
`0x00aad480`, and `ret_data` there is reached through
`std::__tree<…,std::string,nlohmann::json,…>::operator[]` (`0x008304d8`) rather
than the const `json::operator[]` used by the reference path — i.e. this parser
inserts/mutates rather than reads, which fits a handler that also *writes* the
camp map. `ret_data` is then iterated with `iter_impl::operator!=`
(`0x0071af38` at `0x00aad3f8`) and `iter_impl::operator++` (`0x00997d24` at
`0x00aad404`), so **each `ret_data` element is an object with one or more of the
twenty slot keys**.

The literal `"my_"` (ELF `0x01d69713`) and `"enemy_"` (ELF `0x01d69717`) also
exist; `my_` has one consumer (Ghidra `0x00ab808c`), `enemy_` has **no**
`ldr`/`add pc` consumer at all — it is probably reached by a different (non-PIC)
form. Do not assume `my_`/`enemy_` are keys without checking.

**Caveat on `main`.** `main` is a heavily duplicated literal in this build — **9**
occurrences exist in the scanned `.rodata` window (ELF `0x01d5fde5`, `0x01d61af0`,
`0x01d6875f`, `0x01d6f0f7`, `0x01d7e008`, `0x01d90286`, `0x01d9028d`,
`0x01d90711`, `0x01d908d5`). The **only** `main` consumed by a GVG parser in this
pass is ELF `0x01d6875f` / Ghidra `0x01d7875f`, read by this function. It is
*not* in `INFO::parse`'s key list (§1.8), and `INFO::parse` reads a `type`/`msg`
pair from ELF `0x01d569f5` / `0x01d5b4a3` while `/gvg/UpdateStrategy` *sends* the
same two names (§1.10). So the presence of a `main` string proves nothing on its
own; only the load site above is evidence.

## 1.10 All 19 `/gvg/*` routes: builder, request keys, verified

Every route literal was located in the request builder that emits it, so route ↔
function is proven rather than adjacent. All share the same five auth fields;
only the **extra** fields are listed.

| route (ELF literal) | builder (ELF VA) | extra request keys beyond `app_code`/`app_ver`/`market`/`pvid`/`otp` |
|---|---|---|
| `/gvg/GetInst` `0x01d69345` | `RequestInst` `0x00a8f63c` | *(none)* |
| `/gvg/RegisterPending` `0x01d69352` | `RequestRegisterPending` `0x00a901c8` | `guild_id` |
| `/gvg/ToggleAutoRegister` `0x01d69367` | `RequestAutoRegister` `0x00a90df4` | *(none)* |
| `/gvg/RegisterConfirm` `0x01d6937f` | `RequestEntryJoin` `0x00a919a0` | `guild_id` |
| **`/gvg/GetRef`** `0x01d69394` | **`RequestRef` `0x00a925cc`** | ***(none)* — §1.2** |
| `/gvg/GetRegisteredMemberList` `0x01d693a0` | `RequestEntryList` `0x00a93fe8` | `guild_id` |
| `/gvg/GetStrategy` `0x01d693bd` | `RequestGetStrategy` `0x00a94be4` | *(none)* |
| `/gvg/UpdateStrategy` `0x01d693ce` | `RequestUpdateStrategy` `0x00a95758` | `type`, `msg` |
| `/gvg/CombatEnd` `0x01d693fd` | `RequestCombatEnd` `0x00a963c4` | `my`, `enemy`, `ref_id`, `dmg`, `heal`, `tank`, `remain_hp` |
| `/gvg/GetResult` `0x01d6940c` | `RequestResult` `0x00a972bc` | *(none)* |
| `/gvg/CombatBegin` `0x01d6941b` | `RequestCombatBegin` `0x00a97e34` | `card_list` |
| `/gvg/CombatCancel` `0x01d6942c` | `RequestCombatCancel` `0x00a98d20` | *(none)* |
| `/gvg/CombatReady` `0x01d69446` | `RequestCombatReady` `0x00a99894` | `camp_id`, `order` |
| `/gvg/GetCampClearPointLog` `0x01d69461` | `RequestGetCombatLog` `0x00a9aa38` | `camp_id`, `is_myteam` (+ literal `"0"`/`"1"`) |
| `/gvg/GetCampDetail` `0x01d6947b` | `RequestEnemyCampDetail` `0x00a9ba70` | `camp_id` |
| `/gvg/GetDefenderList` `0x01d69499` | `RequestDefenderList` `0x00a9c868` | `camp_id`, `is_myguild` (+ literal `"0"`/`"1"`) |
| `/gvg/OccupyDefender` `0x01d694ae` | `RequestDefenderReserve` `0x00a9d6d0` | `camp_id`, `order` |
| `/gvg/DeployDefender` `0x01d694c2` | `RequestDeployDefender` `0x00a9e754` | `camp_id`, `order`, `card_list` |
| `/gvg/GetSummaryInfo` `0x01d694d6` | `RequestSummaryInfo` `0x00a9fa74` | *(none)* |

**CORRECTION to `blitz-search-consumers` §1.3:** `dmg`, `heal`, `tank`,
`remain_hp` are recorded there as "the four values of the combat-log row
consumed by `/gvg/CombatEnd`". They are in fact **request** keys that the client
**sends** in `/gvg/CombatEnd` (all four are `r1` literals feeding the request
builder at ELF `0x00aa66aa`–`0x00aa6752`), alongside `my`, `enemy` and
`ref_id`. They are not established as response fields of any route.

`is_myteam` / `is_myguild` take the **string** literals `"0"` and `"1"`
(ELF `0x01d52b2e`, `0x01d5b5ea`), i.e. boolean-as-string, like the mail
`target_list` comma form (`AGENTS.md` §88). Do not send them as JSON booleans.

## 1.11 Explicit negatives for `/gvg/GetRef`

Stated so a future pass does not spend a round re-deriving them:

- **No value is recovered for any field.** No point magnitude, no `min_cp`/
  `max_cp` value, no `min_entry_cnt` value, no `reward`/`inf_reward` content.
- **No native literal equals any `CONTENTS15_8` numeral.** `150`, `25`, `50`,
  `2250`, `450` appear nowhere in the GVG `.rodata` block (ELF `0x01d69000`–
  `0x01d69900`) as scoring constants. Re-confirms `blitz-search-consumers` §1.8.
- **`POINT_INFO_TYPE`'s enumerator names and values are not recovered**, and the
  reason is specific. `_ZSt9to_string<CSRGuildBattleMgr::BATTLE_INFO::POINT_INFO_TYPE>`
  is **weak *defined*** (`W` in `.dynsym`) at **ELF `0x0087f9d0` / Ghidra
  `0x0088f9d0`, size `0x130`** — so it **does** have a body in this build. (Note
  that `blitz-search-consumers` §1.2 quotes it as `0x0088f9d0`, i.e. the Ghidra
  address, which is independently consistent with the §0.2 correction.)

  The body was disassembled. It contains **no inline string literals**; it reaches
  its strings through four GOT-relative pointer slots loaded at ELF
  `0x0087f9e4`, `0x0087fa0a`, `0x0087fa10`, `0x0087fa42`, which resolve to
  `.data.rel.ro` at VA `0x021bb0f8`, `0x021bb0fc`, `0x021bb100`, `0x021bb104`.
  **On disk those words are pre-relocation placeholders** — `0x021bb0f8` holds
  `0x01ff85a0` and the other three hold `0x00000000`. They are therefore
  unreadable from the file, exactly the trap recorded in `AGENTS.md` §11
  ("the on-disk value is a pre-relocation placeholder … Do not trust the
  `DAT_xxxx` labels").

  **Net:** the enumerator table is reachable only from relocated memory (a live
  process) or from a relocated Ghidra image. `movs r1, #0x10` near ELF
  `0x0087fa5c` is a **candidate** table stride/count but is **not** proven to be
  the enumerator count and must not be quoted as one. A decompilation of
  `CSRPopUpGuildBattleWin::RefreshPoint(int)` (**ELF `0x00c7838c`**, size
  `0x3f4`) or of `_CCellGBPoint::SetPoint(const std::string&, …INFO::CAMP_STATUS&)`
  (**ELF `0x00c60fc4`**, size `0x19c`) is the remaining route. This **corrects**
  the follow-up suggestion in `blitz-search-consumers` §4.1 item 4: the
  `to_string` shortcut needs relocated data, not just the symbol.
- **The exact numeric type of each `/gvg/GetRef` field is not pinned.** Each site
  is a `tbb` type-dispatch with a conversion; send numbers, do not assume
  `uint32` vs `double`.
- **The `reward` and `inf_reward` sub-structures are not resolved.** They are read
  as whole values with no further key lookups in `BATTLE_INFO::parse`.
- **`" name"` is not a key** (§1.4). `"card_"` is a prefix, `"card_%d"` a format
  string (§1.7).
- **`enemy_` has no located consumer**; `my_` has exactly one (§1.9).
- **Only `ReqGVGRefCB` is a named GVG callback.** The other 18 response parsers are
  in unexported code; no dynsym name exists for them (§3.3).
- **No GVG reference row exists in any local data artefact.** Not in
  `LEVELING.jet`, not in the 774 recovered JET packages, not in the LevelDB
  tables. Re-confirms `blitz-search-consumers` §4.

---

# SECTION 2 — UNPURE: every numeral, with source and era

**Every numeral in this section is impure.** None is a recovered stat, none
changes a fixture, none counts toward any coverage denominator. Era tags follow
`analysis/research/base-stats-visual-hunt/stat-version-context.md` (balance-epoch
threshold **2019-09-05**), as used by the two source passes:

- **[BINARY]** — a native literal, field name, loop bound or wire key in the
  2.8.0.1 `libnative_core.so`. **Era-neutral**: the binary carries no independent
  date, but GVG is absent from 1.4.4.1, so it is by construction the 2.8-era
  feature.
- **[DB-2.8.0.1]** — recovered LevelDB `UI_TEXT_RO` / `UI_JSON_RO`. Shipped client
  lineage. POST-threshold.
- **[HELP-2.8.0.1]** — `UI_CSV.jet` from the shipped build. POST-threshold.
- **[REPLICA-LOCAL]** — a value in `server-ts`. Local policy, not original data,
  and **not** era-classified.

## 2.1 Numerals this pass newly established (all [BINARY], all structural)

| numeral | where | what it is | is it a balance value? |
|---|---|---|---|
| **19** | §1.10, one literal per request builder | number of `/gvg/*` routes | no — route count |
| **20** | §1.9, ELF `0x00aad562`–`0x00aae6c2` | `my_101..110` + `enemy_101..110` slot keys | no — key names |
| **101 … 110** | §1.9 | the numeric suffix of the twenty slot keys | no — key names. **Do not read as a level or stage number** |
| **4** | §1.7, `cmp r6,#5` at ELF `0x00aa74d0` | card slots per camp row (`card_1..card_4`) | no — a loop bound. Consistent with `GVG_방어팀엔 만드시 4명의 헌터…` but **independently read from the instruction stream, not inferred from that string** |
| **5** | §1.7, `cmp r6,#5` | the *exit sentinel*, one past the four live slots | no |
| **0x34** | §1.7, `adds r4,#0x34` | in-memory stride per card slot (52 bytes) | no — struct layout |
| **0x50** | §1.1, `adds r0,#0x50` | offset of the `BATTLE_INFO` member inside `CSRGuildBattleMgr` | no — struct layout |
| **9** | §1.3 rows 3–11 | nine absolute datetimes: the eight phase markers `teaser_begin_dtm` … `finish_dtm`, plus `next_gvg_dtm` | no — field count. Confirms `blitz-search-consumers` §2.4's "eight absolute server datetimes" **plus** `next_gvg_dtm` |
| **0 / 1** | §1.10 | the `"0"`/`"1"` string literals for `is_myteam`/`is_myguild` | no |
| **1** | §1.1, `cmp r0,#1` | the accepted `result_code` | no — transport |
| **6** | §0.5 | `ParseRef` thunk size in bytes | no |
| **0x10000** | §0.2 | ELF↔Ghidra address delta | no — this pass's main tooling correction |
| **0x10 (16)** | §1.11, `movs r1,#0x10` at ELF `0x0087fa5c` | inside `std::to_string<POINT_INFO_TYPE>`; **candidate** table stride/count | no — and **NOT PROVEN** to be the enumerator count. Recorded so it is not mistaken for one |
| **9** | §1.9, vtable neighbours at VA `0x021507dc` | number of adjacent pointers found around the point-log parser's entry | no — this is only a pointer-scan observation, **not** a class size, virtual count or layout claim |

## 2.2 Carried-forward numerals from the source passes — still impure

Reproduced so this file is self-contained. **No new information; do not
re-derive.**

| numeral | source | claim | native status | era |
|---|---|---|---|---|
| **4000** | `GVG_4000이하_헌터` "You can only select a hunter with 4000 or more Strength." + `.rodata` `GVG_4000` Ghidra `0x01d791c9` | minimum hunter Strength to deploy as a Defense Team | **key `GVG_4000` is native; the numeral is NOT in the binary** | [DB-2.8.0.1] / [BINARY] |
| **10** | ten `GVG_N호 캠프` rows (Excavator / Carrier / Supply Station / Command Post / Landing Station × 1/2) | ten camps | **corroborated** by this pass: `my_101..my_110` is a ten-slot enumeration, and `card_1..card_4` shows each camp carries four defenders | [DB-2.8.0.1] / [BINARY] |
| **10** | `CONTENTS15_2` "at least 10 Guild Members" | `min_entry_cnt` | `min_entry_cnt` is a **field** (Ghidra `0x01d79532`, read at ELF `0x00a932d8`). **The value is not in the binary** | [HELP-2.8.0.1] / [BINARY] field only |
| **3000** | `CONTENTS15_6` + `UI_TEXT_RO` `GVG_참가기록이 있는 유저만…` | guild point floor for rewards | display copy only; **no native code reads 3000** | [HELP-2.8.0.1] / [DB-2.8.0.1] |
| **150 / 25 / 50 / 2250** | `CONTENTS15_8` 12-numeral point table | per-event point magnitudes | **fields exist; no value is native.** `point_id`+`multi`+`val` (§1.5) is the shape that would carry them | [HELP-2.8.0.1] / [BINARY] structure |
| **4** | `GVG_최상위 4개 협회 중` | guilds in the Infinite Blitz bracket | display copy only | [DB-2.8.0.1] |
| **7 × 2** | `GVG_TUTO_방어_치르치르_1..7`, `GVG_TUTO_공격_치르치르_1..7` | tutorial chain lengths | display copy only | [DB-2.8.0.1] |
| **Wednesday** | `TIP_8` "Guild Blitz participation requests can be made every Wednesday." | weekly registration | **no weekday logic exists client-side**; the phase clock is the nine `*_dtm` fields | [DB-2.8.0.1] / [BINARY] negative |

## 2.3 Replica-side numerals, for completeness

None of these is original data and none is era-classified.

| numeral | location | meaning |
|---|---|---|
| **0** | `game-routes.ts:570`, `Object.assign(data, { list: [], users: [] })` | the only GVG content the replica emits today (§3.1) |
| **1** | `state.ts` `envelope()`, `result_code: 1` | the accepted application code; matches §1.1's `cmp r0,#1` |
| **0** | `state.ts` `envelope()`, `protocol_code` / `code` | transport zeros |

---

# SECTION 3 — Current replica state, gaps, and what was NOT done

## 3.1 What `/gvg/*` returns today, and why that is inert

`server-ts/src/game-routes.ts:570`, verbatim:

```ts
if (/^\/(guild|gvg|arena|relation)\//.test(route)) Object.assign(data, { list: [], users: [] });
```

with `state.ts` `envelope()` placing that object under `ret_data` **and**
`data`. So `/gvg/GetRef` currently answers:

```jsonc
{ "result_code": 1, "ret_data": { "list": [], "users": [] }, "data": { "list": [], "users": [] } }
```

Traced against §1.1: `ReqGVGRefCB` sees `result_code == 1`, calls
`json["ret_data"]` successfully, and `BATTLE_INFO::parse` then evaluates
`ret_data["gvg"]` on an object with no `gvg` member. nlohmann's
`operator[](const char*) const` on a missing key yields **null**, and every
subsequent access takes the null/type-miss branch, leaving `BATTLE_INFO` at its
parse-time defaults. **No assertion fires** — this is the silent-failure class
that §16.2 of `AGENTS.md` was written about. `list`/`users` are also not read by
any recovered GVG key, so they contribute nothing.

This is recorded as a diagnosis only. **No handler was implemented.**

## 3.2 Ranked gaps for whoever implements this next

1. **`reward` and `inf_reward` sub-shapes** — read as whole values in
   `BATTLE_INFO::parse`; no child keys are looked up there. A fixture must guess,
   or the consumer must be decompiled.
2. **Numeric widths** for every `/gvg/GetRef` field (see §1.11).
3. **`point_id` enum values** — `POINT_INFO_TYPE`'s enumerator table is behind
   **pre-relocation pointers**, so it cannot be read from the `.so` (§1.11). The
   `to_string` shortcut proposed in `blitz-search-consumers` §4.1 item 4 needs
   **relocated** data (a live process, or a relocated Ghidra image) — merely
   finding the symbol is not enough. Otherwise decompile
   `RefreshPoint`/`SetPoint` (§1.11 addresses).
4. **Route→parser attribution for the other 18 routes.** Known parsers:
   `BATTLE_INFO`(+`_CAMP`) → `/gvg/GetRef`; `PLAY_DATA`, `CAMP_INFO`, `CARD`,
   `CARD_SUMMARY`, `BATTLE_PAIR`, `INFO` → unattributed. `CAMP_INFO::parse` is the
   one that indexes the full envelope (`ret_data` → `camp`, §1.7), so it belongs
   to a route whose response is a camp array; `PLAY_DATA::parse` does **not** index
   `ret_data`, so its caller unwraps first. Both facts are pure and useful for
   narrowing the search.
5. **Owning classes of the two unnamed parsers** (§1.5, §1.9). The point-log
   parser's vtable is at VA `0x021507dc`; `dladdr`/RTTI would name it, but that
   needs the Ghidra project, which is parent-owned and locked.
6. **Request field types** for `is_myteam` / `is_myguild` — the code uses the
   strings `"0"`/`"1"`; whether `0`/`1` are also accepted is untested.

## 3.3 Retractions and corrections this pass forces

1. **"addresses are ELF VAs" for `analysis/native-all-strings.tsv` — RETRACTED.**
   They are **Ghidra** addresses, `ELF + 0x10000` (§0.2). Every TSV address in
   `blitz-search-consumers-2026-10-05.md` and in the task brief needs `0x10000`
   subtracted before use. Its §1.3 route table (e.g. `/gvg/GetRef` at
   `0x01d79394`) is a **string** address and is correct as such.
2. **"`ReqGVGRefCB` at `0x003600f0`" — RETRACTED.** That is the `.dynstr` address
   of the mangled name. Real: ELF `0x00f7525c` / Ghidra `0x00f8525c` (§0.3).
3. **"`point_id`/`multi` adjacency is `.rodata` adjacency, not a proven parse
   pair" — CLOSED.** Both are read from one object in one function, together with
   `val`, on an array element, and `point_detail` is array-iterated with nlohmann
   iterators (§1.5). The triple is `{point_id, val, multi}`.
4. **"`dmg`/`heal`/`tank`/`remain_hp` … consumed by `/gvg/CombatEnd`" — CORRECTED.**
   They are **request** keys the client sends in `/gvg/CombatEnd` (§1.10). No
   recovered code reads them from a response.
5. **"The point kinds come from the `POINT_INFO_TYPE` → `std::to_string` table" —
   NOT AVAILABLE FROM DISK.** The `to_string` specialisation **is** weak-defined
   with a body (ELF `0x0087f9d0`, size `0x130`), but its string table sits behind
   **pre-relocation pointers** in `.data.rel.ro` (`0x021bb0f8`…`0x021bb104`), so
   the enumerator names cannot be read out of the file (§1.11).
6. **`"my_"/"enemy_"` as key prefixes — PARTLY RETRACTED.** The twenty
   `my_1NN`/`enemy_1NN` keys are real and all in one function (§1.9), but the bare
   `"my_"` prefix has exactly one consumer and `"enemy_"` has **no** located
   consumer.
7. **`ParseReward` nesting — new, and easy to get wrong.** `ap_charge_time` /
   `bp_charge_time` are **siblings** of `ap` / `bp` in the GVG reward receipt
   (§1.8), unlike the mission `Complete` contract where `ap_charge_time` nests
   **inside** `ap`.

## 3.4 What this pass did NOT do

- **No Ghidra run and no Ghidra project access.** The project is parent-owned and
  locked. Every function-level claim here comes from `llvm-nm -D` plus capstone
  on the original `.so`, or from verbatim bytes quoted inline.
- **No decompiler was used**, only raw instructions. Per `AGENTS.md` §16.7
  lesson 7, that is the correct choice for iterators and `std::map` — and it is
  what resolved `card_1..card_4` and the `point_id`/`val`/`multi` triple, both of
  which a flattened decompile would have hidden.
- **No `.so` was written, copied, patched or moved.** Only reads.
- **No value was recovered.** All twelve `CONTENTS15_8` point numerals, the
  `3000` floor, the `4000` Strength floor and the `min_entry_cnt` value remain
  server-side. Nothing here may be turned into a fixture without an explicit
  local-policy label.
- **No `/gvg/*` handler implemented**, no `server-ts` file touched, no test run,
  no build, no server start, no state file read or written.
- **No LevelDB opened**, no JET decoded, no catalogue edited, no emulator / VM /
  physical-phone / release operation.
- **`polluted-observations.md` NOT appended.** The parent mirrors.
- **Zero coverage credit.** Heroes 1/113, accessories 1/100, monsters 0/22
  unchanged; the broader base-stat goal remains far from its 70% thresholds.