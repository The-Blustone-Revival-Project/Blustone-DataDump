# `CSRGameMob::HasMonsterData` — what it actually consults

Written 2026-10-02 by the native-analysis lane. Answers the single open risk in
`ROOT-CAUSE-v2-showthumbnail.md` §5.

**Short answer: the parallel agent's assumption is CORRECT.**
`HasMonsterData` is a plain `std::map<std::string, CSRGameMob::INFO>::find` on the
`CSRGameMob` singleton's **first member**, which the client itself names
`m_mMonsters` in a source string compiled into the binary. `0` means "not present".
The map has **exactly one writer** in the whole binary and it is the
`/reference/GetMonster` response callback. There is no second writer, no
resource/asset registry, no loaded-flag set, no cache.

---

## Raw dumps produced by this lane

| File | Contents |
|---|---|
| `analysis/ghidra-hasmonster-01-lookup.txt` | decompile of `HasMonsterData`, `GetMonsterData`, `HasStageMonsterLinkData`, `GetStageMonsterLinkData` |
| `analysis/ghidra-hasmonster-02-emplace-callers.txt` | callers of the map's **only** insert primitive |
| `analysis/ghidra-hasmonster-03-addmonster-callers.txt` | callers of `AddMonster` |
| `analysis/ghidra-hasmonster-04-hasmonsterdata-callers.txt` | callers of `HasMonsterData` |
| `analysis/ghidra-hasmonster-05-getmonsterdata-callers.txt` | callers of `GetMonsterData` |
| `analysis/ghidra-hasmonster-06-asm-lookup.txt` | **raw instructions, whole of `HasMonsterData`** |
| `analysis/ghidra-hasmonster-07-asm-addmonster-emplace.txt` | raw instructions at the `AddMonster` emplace call site |
| `analysis/ghidra-hasmonster-08-asm-addstagemonster-emplace.txt` | `AddStageMonster` head (0xa0d194) — control for the *other* `CSRGameMob` map |
| `analysis/ghidra-hasmonster-12-asm-emplace-prologue.txt` | `__emplace_unique_key_args` prologue (0xa0df1c) |
| `analysis/ghidra-hasmonster-13-asm-assert-call.txt` | the `_RMAssert` call in `GetMonsterData` (0xa0b488-0xa0b4b4) |
| `analysis/ghidra-hasmonster-14-asm-addmonster-prologue.txt` | full `AddMonster` disassembly — the `_server` read and the emplace dataflow |
| `analysis/ghidra-hasmonster-15-asm-addmonster-serverkey.txt` | duplicate of 14 (the script's range mode fell back to whole-function); kept, not cited |
| `analysis/ghidra-hasmonster-09/10-*-callers.txt` | callers of the map's `__destroy` / `destroy` (erase/destructor path) |
| `analysis/ghidra-hasmonster-11-assert-strings.txt` | PC-relative literals in `GetMonsterData` |
| `analysis/ghidra-scripts/DumpInstructions.java` | **new** (additive) — raw instruction/range dumper; see the "Why a new script" note at the end |

---

## Q1. What does `HasMonsterData` do? — **[RECOVERED]**

It is a `find` in `std::map<std::string, CSRGameMob::INFO>`. That is the whole
function. Nine instructions, no branches other than the bool materialisation:

`analysis/ghidra-hasmonster-06-asm-lookup.txt:3-11`

```asm
===== range 0xa0b43c .. 0xa0b43c =====
00a0b428  push {r4,r6,r7,lr}
00a0b42a  add r7,sp,#0x8
00a0b42c  mov r4,r0              ; r4 = this
00a0b42e  bl  0x00a0dd98         ; r0 = map<string,CSRGameMob::INFO>::find(this /*+0*/, param_1)
00a0b432  adds r1,r4,#0x4        ; r1 = this + 4  == &_M_header._M_parent  (the end() sentinel)
00a0b434  subs r0,r1,r0          ; r0 = end - itr
00a0b436  it ne
00a0b438  mov.ne r0,#0x1
00a0b43a  pop {r4,r6,r7,pc}
```

Three things to read off it:

1. **`r0` is passed to `find` completely unmodified.** No `add rN, r0, #imm`,
   no `ldr`. The map is at **offset 0** of the `CSRGameMob` singleton — it is the
   object's first member. (This is the reason the decompiled `this` is
   trustworthy here: at instruction level there is no offset arithmetic to have
   been lost.)
2. `0xa0dd98` is the symbol
   `std::__ndk1::__tree<__value_type<std::string, CSRGameMob::INFO>, __map_value_compare<std::string, __value_type<...>>, std::less<std::string>>, true>::find<std::string>`
   (`analysis/native-evidence.tsv:12047`) — i.e. exactly
   `std::map<std::string, CSRGameMob::INFO>::find`.
3. `this + 4` is `&_Rb_tree_header::_M_parent`, which is libstdc++/ndk's
   `end()` node. So the return value is literally `itr != end()`.

### It is *named* `m_mMonsters` by the client itself — **[RECOVERED]**

`GetMonsterData` (0xa0b43c) is the same `find` plus an assert. Resolving the
assert's PC-relative literals (`tools/resolve-literals-offline.py
--function 0xa0b428:0xa0b540`):

```
ldr@0x00a0b470 r6 slot=0x00a0b52c add_pc=0x00a0b476 -> 0x01d7688d  'Cannot find MonsterData'
ldr@0x00a0b496 r7 slot=0x00a0b534 add_pc=0x00a0b49e -> 0x01d767d9  'itr != m_mMonsters.end()'
ldr@0x00a0b49e r6 slot=0x00a0b538 add_pc=0x00a0b4a4 -> 0x01d767f2  'C:/Users/hkpark/Documents/Visual Studio 2015/Projects/ramen/SR/SRGameMob.cpp'
ldr@0x00a0b4a4 r5 slot=0x00a0b53c add_pc=0x00a0b4aa -> 0x01d768a5  'GetMonsterData'
```

The literal at `0x1d767d9` is the `RM_ASSERT` *condition text*:
`itr != m_mMonsters.end()`. That is the original developer's own source text,
compiled in. So the member is `CSRGameMob::m_mMonsters`, and the container the
`find` at 0xa0b428 touches is that member, at offset 0. **No inference left.**

Corroborated at runtime by the device trace
(`analysis/r010/logcat-all.txt:9286-9289`, `analysis/r011/logcat-all.txt:136407-136410`):

```
[AST] [GetMonsterData] Cannot find MonsterData
(itr != m_mMonsters.end()) is FALSE
```

**It is not a resource registry, an asset/LevelDB lookup, a loaded-flag set, or a
cache.** There is no file/asset/CDN call anywhere in the nine instructions.

---

## Q2. Exact return convention — **[RECOVERED]**

**`1` (true) = present. `0` (false) = absent, "must fetch".**

Assembly: `subs r0, r1, r0` / `it ne` / `mov.ne r0,#0x1` — a non-zero result iff
`end - itr != 0` iff `itr != end()` iff the key was found.

Decompiled, `analysis/ghidra-hasmonster-01-lookup.txt:6-19`:

```c
bool __thiscall CSRGameMob::HasMonsterData(CSRGameMob *this,basic_string *param_1)
{
  CSRGameMob *pCVar1;
  pCVar1 = (CSRGameMob *)
           std::__ndk1::__tree<...__value_type<basic_string<...>,CSRGameMob::INFO>,...>::
           find<basic_string<...>>((__tree<...> *)this,param_1);
  return this + 4 != pCVar1;      /*  <-- the compare */
}
```

`return this + 4 != pCVar1;` is `return end != itr;`, and Ghidra types the
function `bool`.

So the caller guard in `FUN_00b4a7a8` reads exactly as the root-cause note
claimed — **the note's inference here was right**
(`analysis/ghidra-enemycamp-decomp-04.txt:56-73`):

```c
for (pbVar18 = local_78; ...; pbVar18 = pbVar18 + 0xc) {   /* STAGE_MONSTER_LINK::ids, stride 0xc */
    iVar7 = CSRGameMob::HasMonsterData(pCVar6,pbVar18);
    if (iVar7 == 0) {          /* 0 == "do NOT already have it" -> push and request */
      ... operator_new(0x14) ...
      local_64 = local_64 + 1;
    }
}
```

and then `if (local_64 == 0) { ...fire the completion callback... } else { ... CSRSyncMStage::GetMonster(this,&list,cb) ... }`
(`analysis/ghidra-enemycamp-decomp-04.txt:93-149`).

**Both `HasMonsterData` call sites in the entire binary are inside
`FUN_00b4a7a8`** — `analysis/ghidra-hasmonster-04-hasmonsterdata-callers.txt`:

```
target 0xa0b428  function=HasMonsterData
  from 0x0  <no function>          <- Ghidra artifact: the pre-relocation / Thumb-lowbit placeholder
  from 0xb4a804  FUN_00b4a7a8
  from 0xb4a870  FUN_00b4a7a8
```

`HasMonsterData` is called **nowhere else** in the game. It is not used by the
battle scene, the actor builder, or the UI. It exists solely to decide the
`GET /reference/GetMonster` `list`. This matters: it means the fix has exactly
one narrow lever, and no other code path silently depends on the result.

---

## Q3. What keys `m_mMonsters`, and does it match the response key? — **[RECOVERED] container + key origin; [INFERRED-strong] key = `_server`**

### The two operations use the same tree — **[RECOVERED]**

- `HasMonsterData` / `GetMonsterData` `find` pass `r0 = this` unmodified → **offset 0**.
- `AddMonster`'s emplace at `0xa0cd08` has `r1` reloaded from `[sp,#0x14]`
  (`analysis/ghidra-hasmonster-14-asm-addmonster-prologue.txt:2066,2107-2111`),
  and `[sp+#0x14]` was written once at `0xa0bbc4` as `str.w r8,[sp,#0x14]` with
  `r8 = this` captured at function entry (`0xa0b552  mov r8,r0`):

```asm
00a0cc84  ldrd r6,r8,[sp,#0x14]        ; r6 = this
00a0ccfe  add r4,sp,#0xa0
00a0cd00  add r0,sp,#0x240
00a0cd02  mov r1,r6                    ; r1 = this
00a0cd04  mov r2,r4                    ; r2 = sp+0xa0
00a0cd06  mov r3,r4
00a0cd08  bl 0x00a0df1c                ; __emplace_unique_key_args<string,pair<const string,INFO>>
```

Ghidra's decompiler agrees at the same site
(`analysis/ghidra-enemycamp-decomp-03.txt:9392-9396`): the emplace's tree argument
is printed as `this`. The target `0xa0df1c` is the **only**
`__tree<__value_type<string, CSRGameMob::INFO>,...>` insert instantiation in the
binary (`analysis/native-evidence.tsv:12049`; the only other `CSRGameMob` map
insert is `0xa0e618` for `STAGE_MONSTER_LINK`, a different value type).

So `HasMonsterData` and `AddMonster` provably operate on the **same**
`std::map<std::string, CSRGameMob::INFO>`.

### The key is **not** the `ret_data` object key — **[RECOVERED]**

`CSRSyncMStage::ReqMonsterCB` (0xb4514c), the `/reference/GetMonster` callback,
iterates `ret_data` and passes only the **dereferenced value**
(`analysis/ghidra-enemycamp-decomp-04.txt:299-311`):

```c
pbVar4 = (basic_json *) nlohmann::detail::iter_impl<...>::operator*((iter_impl *)&local_2c);
this_00 = (CSRGameMob *)CSRGameMob::get();
CSRGameMob::AddMonster(this_00, pbVar4);
```

There is no `iteration_proxy_value::key()` call — contrast
`ReqTargetStageMonsterCB` (0xb4606c), which *does* call
`iteration_proxy_value::key()` and passes it to `AddStageMonster`
(`analysis/ghidra-enemycamp-decomp-04.txt:1157-1168`). **The iteration key is
never handed to `AddMonster`, so it cannot be the map key.** Whatever
`/reference/GetMonster` uses as its top-level JSON key is irrelevant to
`m_mMonsters`. The root object must still be an object/array the client can
iterate, but the *id* comes from the record itself.

### The key is the record's `_server` field — **[INFERRED, strong]**

`AddMonster`'s **first** JSON read is `_server`, and it is read as a string into
the 3-word `basic_string` slot at `sp+0x1b8`
(`analysis/ghidra-mob-keys.txt:2`, and
`analysis/ghidra-hasmonster-14-asm-addmonster-prologue.txt:12-33`):

```asm
00a0b552  mov r8,r0                  ; this
00a0b556  mov r6,r1                  ; the json
00a0b558  ldr r1,[0x00a0b874]        ; literal slot
00a0b55a  add r0,pc
00a0b562  add r1,pc
00a0b590  mov r0,r6
00a0b592  bl 0x007930f8              ; nlohmann::basic_json::operator[](const char*)
```

and the decompile names the value
(`analysis/native-monster-stage.txt:463-471`):

```c
uVar15 = ...operator[]<char const>(param_2, _DAT_00a0b874 + 0xa0b566);   /* slot 0xa0b874 = "_server" */
_ZN8nlohmann6detail9from_jsonI...string_tE (uVar15,&uStack_2b8);
```

Following that string to the emplace, the same 3-word string is copied into
**`sp+0xa0..0xab`, which is the `const std::string` key slot of the
`pair<const std::string, CSRGameMob::INFO>` that is forwarded to
`__emplace_unique_key_args`** (`sp+0xa0` is also the `_server` field inside
`INFO`, at `+0xc` — the pair and the INFO both start with the server id, which
is why the string lands twice):

`analysis/ghidra-hasmonster-14-asm-addmonster-prologue.txt:2025-2035, 2066-2111`

```asm
00a0cc14  ldrb.w r0,[sp,#0x1b8]       ; the "_server" std::string, SSO flag byte
00a0cc20  lsls r0,r0,#0x1f
00a0cc24  vldr.64 d16,[sp,#0x1b8]
00a0cc28  ldr   r0,[sp,#0x1c0]
00a0cc2a  str   r0,[sp,#0xa8]         ; -> pair key, word 2
00a0cc2c  vstr.64 d16,[sp,#0xa0]       ; -> pair key, words 0..1
...
00a0cc88  add r0,sp,#0x1b8
00a0cc8a  vldr.64 d16,[sp,#0x1b8]
00a0cc96  ldr   r0,[sp,#0x1c0]
00a0cc9e  str   r0,[sp,#0xb4]         ; -> INFO+0x0, word 2
00a0cca0  vstr.64 d16,[sp,#0xac]       ; -> INFO+0x0, words 0..1
...
00a0cd02  mov r1,r6                    ; this
00a0cd04  mov r2,r4                    ; &pair  (r4 = sp+0xa0)
00a0cd08  bl 0x00a0df1c
```

**[UNKNOWN], and deliberately not asserted:** the exact physical
register↔parameter mapping at `0xa0cd08`. Ghidra's demangled prototype for
`__emplace_unique_key_args` on this instantiation ends in `E_&&` (an rvalue
reference to the `pair`), and the printed parameter order does not line up with
what the register trace shows. I am relying on the *type* identity of
`0xa0df1c` plus the `this`-as-`r1` dataflow, not on Ghidra's argument order.
This does not affect any conclusion above.

### The `show_thumbnail` strings are the query, and they must match `_server` verbatim

`FUN_00b4a7a8` walks `STAGE_MONSTER_LINK::ids` with **stride `0xc`** (a 3-word
`std::string`), and for each element allocates a 0x14-byte list node whose
`basic_string` is **copy-constructed from that element verbatim**
(`analysis/ghidra-enemycamp-decomp-04.txt:60-70`). No normalisation, no
prefixing, no case folding. Whatever the client puts in
`ret_data[<stage>]["show_thumbnail"]` is sent back verbatim as the
`list` form field of `GET /reference/GetMonster` (the `list` literal is resolved
at `0xb44686`; the URL at `0xb447ce`):

```
$ python tools/resolve-literals-offline.py --function 0xb444c4:0xb45260
ldr@0x00b44686 r7 -> 0x01d6a8ff  'list'
ldr@0x00b447ce r6 -> 0x01d7b3d5  '/reference/GetMonster'
ldr@0x00b45170 r2 -> 0x01d689bb  'ret_data'
```

Therefore, for the lookup to hit, the ids in `show_thumbnail` must equal the
`_server` values of the records you publish from `/reference/GetMonster`.
`"M001"` in one place and `"001"` in the other is a miss.

---

## Q4. What populates `m_mMonsters`? — **[RECOVERED] — one writer, one route**

The complete set of `std::map<std::string, CSRGameMob::INFO>` helper symbols in
the binary (`analysis/native-evidence.tsv:12047-12051, 12077`):

| Address | Symbol | Role |
|---|---|---|
| `0xa0dd98` | `__tree<...INFO...>::find` | read (`HasMonsterData`) |
| `0xa0de5a` | `__tree<...INFO...>::find const` | read (`GetMonsterData`) |
| `0xa0e030` | `__tree<...INFO...>::__find_equal` | read helper |
| **`0xa0df1c`** | **`__tree<...INFO...>::__emplace_unique_key_args<string, pair<const string,INFO>>`** | **the only insert** |
| `0xa0e106` | `allocator_traits::__destroy<pair<const string,INFO>>` | node teardown |
| `0xa0eebe` | `__tree<...INFO...>::destroy(__tree_node*)` | node teardown / erase |

There is **no** `map::operator[]` and **no** `__insert_unique_key_args`
instantiation for `INFO`. The single insert primitive has exactly one caller:

`analysis/ghidra-hasmonster-02-emplace-callers.txt`
```
target 0xa0df1c  function=__emplace_unique_key_args<...CSRGameMob::INFO...>
  from 0x0  <no function>     <- Ghidra placeholder artifact, not a real call site
  from 0xa0cd08  AddMonster
callers: 2
```

and `AddMonster` has exactly one caller:

`analysis/ghidra-hasmonster-03-addmonster-callers.txt`
```
target 0xa0b540  function=AddMonster
  from 0x0  <no function>     <- Ghidra placeholder artifact
  from 0xb45206  ReqMonsterCB
callers: 2
```

`0xb45206` is inside `CSRSyncMStage::ReqMonsterCB`, whose URL is
`/reference/GetMonster` (see Q3).

**Writer chain: `/reference/GetMonster` response → `ret_data` → `ReqMonsterCB` →
`AddMonster` → `m_mMonsters.emplace(<record>["_server"], INFO{...})`. Nothing else.**

The teardown side confirms there is no `Clear`/`Reset` that could be a hidden
second writer — `destroy` is only reachable from the map's own destruction
(`analysis/ghidra-hasmonster-09/10-*-callers.txt`):

```
0xa0e106 __destroy<pair<const string,INFO>>  <- from 0xa0eee0 destroy
0xa0eebe destroy                            <- from 0xa0ee52 __on_zero_shared,
                                                0xa0eece destroy, 0xa0eed6 destroy
```

That is `__tree::~__tree` / `_M_destroy`, i.e. singleton teardown at exit. There
is no `CSRGameMob::Clear`/`Reset`/`Init` in the retained symbol set at all.

### What this means for the failed device run

`analysis/testing/report-011.md` observed that with the monster-id map key the
`GetMonster` route **was never issued**. That is fully consistent with the
recovered control flow and needs no further explanation:

- `AddStageMonster` filed the link under the *stage* key, so
  `STAGE_MONSTER_LINK::ids` was populated from
  `show_thumbnail` — which the replica sent as the **integer `1`**, not an array,
  so iteration yielded nothing and `show_thumbnail` contributed no ids at all;
- and whatever ids *were* present resolved as already-known, making the
  `local_64 == 0` branch fire and the `GetMonster` request be skipped.

`m_mMonsters` was therefore never populated in that run, which is precisely why
`CSRMStage::MakeStageInst()` then dereferenced a null `INFO` at `+0x4c`.

---

## VERDICT

> **The `show_thumbnail` fix is sufficient in the sense that matters, and there
> is NO other writer of `m_mMonsters` — its only writer in the entire binary is
> the `/reference/GetMonster` response callback, so if the `list` the client
> builds from `show_thumbnail` is non-empty the route *will* fire and *will*
> populate the map. The one thing that can still miss is the id *string*: the map
> is keyed on the record's `_server` field (not the `ret_data` object key), so
> `show_thumbnail` entries and the published `/reference/GetMonster` records must
> carry byte-identical `_server` values.**

The risk the root-cause note flagged is retired. What is left is a value
match, not a mechanism: if the next run shows `GetMonster` fired and
`SRGameMob.cpp(38)` still asserts, the cause is an id mismatch between
`show_thumbnail` and `_server` — not a missing writer, and not a second
container.

### [INFERRED] residual risk worth one cheap check on the wire

`ReqMonsterCB` iterates `ret_data` and calls `AddMonster` per element, so a
`ret_data` that is an **array** works, and so does an object. But an element that
is **not** an object (e.g. a bare string) would make `AddMonster`'s first
`operator[]("_server")` return a null and `from_json<std::string>` yield `""`,
filing a useless `""` entry. Given `HasMonsterData` is only ever asked about
`show_thumbnail` ids, a `""` entry is harmless — but it is worth publishing each
record as a full object with a non-empty `_server`.

---

## Honesty notes

- Everything tagged **[RECOVERED]** is quoted from raw instructions or from the
  offline literal resolver reading the on-disk `.so`; both agree, and the
  `m_mMonsters` name additionally appears in a device logcat. No `DAT_xxxx`
  label from an older dump was trusted — the `DAT_` addresses in
  `analysis/native-mob.txt` / `analysis/ghidra-enemycamp-decomp-04.txt` are
  decompiler artifacts and were ignored in favour of the `slot=` addresses the
  resolvers print.
- The single **[UNKNOWN]** is the physical register↔parameter mapping of the
  `__emplace_unique_key_args` call (see Q3). Stated with its reason rather than
  guessed. It is not load-bearing.
- The `_server`-is-the-key claim is **[INFERRED]**, not [RECOVERED]: the dataflow
  is unambiguous but I did not disassemble `0xa0df1c` to its completion to see
  it perform `__find_equal(key)`. The reasoning does not depend on it: the
  `ret_data` key is provably unavailable to `AddMonster`, so the key must come
  from the record, and `_server` is the only string field it reads before it has
  built anything.
- **Why a new Ghidra script was added.** `DecompileAtAddress` gives C, and C
  cannot distinguish "the decompiler lost the member offset" from "the offset is
  0". `analysis/ghidra-scripts/DumpInstructions.java` dumps raw instructions so
  the offset claim in Q1/Q3 rests on `mov r4,r0` / `bl find` with no intervening
  arithmetic, and so the `_server` dataflow in Q3 is traceable. Additive only.
