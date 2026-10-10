# Gem popup display bindings — 2026-10-05

**Lane:** BLUSTONE gem (jewel) polish UI — `CSRPopUpGemLevelUp` **display
bindings** and call sites. This is the pass that closes
[`gem-levelup-action-2026-10-05.md`](gem-levelup-action-2026-10-05.md) §1.3's
third bullet ("`UpgradeCB` display bindings: unproved. Popup helpers
`SetBaseInfo`/`UpgradeEvent`/`StatusUpdate`/`SetUpgradeComment` exist as symbols
… but their call sites/operands were not traced").

**Status:** research only. Read-only native evidence. **No server/APK change, no
implementation, no Ghidra project access, no emulator input, no strict coverage
credit** (heroes 1/113, accessories 1/100, monsters 0/22 unchanged). This lane
also recovered the `/gem/LevelUp` **request** form keys as a side effect — see
§1.6, which supersedes §1.3 bullets 1–2 of the parent report.

**Impure ledger:** [`polluted-observations.md`](polluted-observations.md)
("Gem popup bindings pass") — §2 here is duplicated there.

**Output rule for this file:** §1 is **PURE** — call sites, operand
derivations, resolved UI keys, structural types. No price, possibility,
compensation or rate AMOUNT is asserted in §1. §2 is **UNPURE** — every numeral
encountered is marked impure and counts toward no 70% threshold.

## Address conventions (read before using any address below)

Three different conventions appear in this workspace. Mixing them is the single
most common source of wrong results here (AGENTS.md §16.7 lesson 3).

| Kind | Convention | Example |
|---|---|---|
| **This file, all code addresses** | **ELF VA** (file offset == vaddr for `.text`) | `SetBaseInfo` @ `0x0bc0454` |
| Ghidra (`analysis/native-evidence.tsv`, `ghidra-*.txt`) | ELF VA **+ 0x10000** | `SetBaseInfo` @ `0x0bd0454` |
| `analysis/native-all-strings.tsv` 8-hex keys | **GHIDRA image addresses** (= ELF VA + `0x10000`) — ⚠️ corrected, see below | `002a6244` is `_ZN18CSRPopUpGemLevelUp11SetBaseInfoE…` at ELF VA `0x00296244` |
| `.rodata` string addresses | ELF VA; `.rodata` vaddr == file offset too | `'GEM_NAME1'` @ `0x1d6e9dd` |

**⚠️ Row 3 correction (2026-10-05, later pass).** This table previously read
"`analysis/native-all-strings.tsv` 8-hex keys | **file-order tokens, NOT
addresses** | `002a6244` is not an address". **Both claims were wrong.** Measured
over the whole file: all **515 576** 8-hex rows are **Ghidra image addresses**,
proven by byte lookup — for every row, `data[(token − 0x10000) : …]` reproduces the
printed string, and for the 1 763 rows that land in the *second* `PT_LOAD` the file
offset is `(token − 0x10000) − 0x1000` while `token − 0x10000` **never** works
(0/1763). `002a6244` specifically is a real row (**line 25258** — corrected
2026-10-05; this note previously said 25257, which is `002a621d
_ZN18CSRPopUpGemLevelUp11AnvilheatedEi`) and
`d[0x00296244] == b'_ZN18CSRPopUpGemLevelUp11SetBaseInfoERKNSt6__n'`. Definitive
table and proof: [`address-convention-2026-10-05.md`](address-convention-2026-10-05.md).

The file's **own** addresses are unaffected: every code address and every `.rodata`
literal here was independently re-verified as **ELF VA** (16/16 literal↔address
pairs match byte-exactly at the address as printed), so only row 3 — a claim about a
*foreign* table — was wrong.

All figures below were produced with `llvm-objdump` from the NDK at
`tools/android-sdk/ndk/29.0.14206865/.../llvm-objdump.exe` against
`analysis/extracted/lib/armeabi-v7a/libnative_core.so`, and cross-checked
against `llvm-nm -D` (dynamic symbol table). **No Ghidra lock was taken.**

---

## 1. PURE — call sites, operands, resolved bindings (no amounts)

### 1.0 Method and its self-validation (read this before trusting §1)

Two tools were written for this pass and **both are self-validating**. Both
caught real bugs during the pass; the corrections are recorded because they are
the reason the results can be trusted.

**(a) Literal resolver, self-test 13/13.** The PC-relative resolver
(`ldr rX,[pc,#imm]` immediately followed by `add rX,pc`) reproduces **13 of 13**
independent resolutions already present in
`analysis/ghidra-gem-inventory-keys.txt` — `ret_data`, `ref_id`, `inst_id`,
`rank`, `level`, `position`, `target_inst_id`, `ability`, `abilities`,
`level_up_failed`, `main`, `sub`, and the single-space `" "`. It aborts and
prints nothing if any case fails.

Three defects were found and fixed **because the self-test failed**, not by
inspection:

1. **Ghidra/ELF convention mix.** The first run reported 0/13 with nonsense
   targets like `0xffa8b5d6`. Cause: the self-test table was pasted in Ghidra
   coordinates but applied to ELF bytes. This is AGENTS.md §16.7 lesson 3
   recurring inside a *new* tool.
2. **Wrong pool address.** I initially read the literal word from the *slot
   address* Ghidra printed, rather than from
   `((ldr_addr + 4) & ~3) + imm`. Ghidra's "slot=" column is the address a
   human can look up, not the displacement.
3. **Single-character string rejected.** The 13th self-test (`" "`, a
   deliberate 1-byte literal at `0x1d650c1`) failed on a `len >= 2` guard even
   though the resolved address was byte-exact.

A fourth defect was a *false negative in the first working version*: the regex
for the `ldr` operand was **end-anchored**, while `objdump` appends
`@ 0x…<symbol>` decoration, so **every** literal silently failed to match and
the pass initially reported "0 literals in every function". Likewise
`add rX,pc` was matched against a field that contained only operands. Both were
caught only because `OnInit` demonstrably calls `GetLocalizedText` and
`FindCastByName` — a "0 literals" result contradicted already-visible branch
targets, so the measurement, not the code, was wrong (AGENTS.md §16.7 lesson 5).
**A clean zero is a claim about the measurement until it is cross-checked.**

**(b) Branch-target decoder.** A standalone Thumb `BL` decoder was written,
then **cross-validated against `llvm-objdump` over the whole popup region**
(`0xbbd85c–0xbc4400`): **0 false negatives** (every objdump `bl` site was found)
and 91 decoder-only hits, which were confirmed to be **literal-pool data**, not
code — exactly the failure mode a raw byte scan has and a boundary-accurate
disassembler does not. Its first version also had a real bug: it treated
`J1`/`J2` in `hw1 = 11 J1 1 J2 imm11` as a BL/BLX flag. They are **offset bits**;
bit 12 is the discriminator.

**Final branch enumeration used `objdump`'s own linear disassembly of the entire
executable PT_LOAD** (`0x00000000–0x0210d320`, 34,657,056 bytes), so every
"no caller" negative below is a *whole-library* result, not a local-range one.

### 1.1 The full `CSRPopUpGemLevelUp` vtable — which members are virtual

Dumping `_ZTV18CSRPopUpGemLevelUp` @ `0x02158290` (32 slots read; the table
**ends** at `+0x7c`, where `0xfffff9ac` = `_end`) settles the virtual/non-virtual
question that §1.3 needed:

| Slot | Word | Target |
|---|---|---|
| `+0x00` | `0x00000000` | offset-to-top = 0 |
| `+0x04` | `0x02158334` | typeinfo `_ZTI18CSRPopUpGemLevelUp` |
| `+0x08` | `0x00bc2501` | `D2Ev` |
| `+0x0c` | `0x00bc2809` | `D0Ev` |
| `+0x10` | `0x00f0befd` | `CSRFramedScene::Init(void*)` |
| `+0x18` | `0x00f0c8cd` | `CSRFramedScene::Refresh()` |
| `+0x44` | `0x00bc126b` | **`OnProcessKeyInput(float,int,unsigned char)`** |
| **`+0x5c`** | `0x00bbd85d` | **`OnInit()`** |
| `+0x70` | `0x00bc13a5` | **`OnRefresh()`** |
| `+0x78` | `0x00bc0979` | **`OnButtonClick(CMUIView*, CMUIBase*)`** |

Only **three** of the helpers in question are virtual. **`SetBaseInfo`,
`StatusUpdate`, `UpgradeEvent`, `SetUpgradeComment`, `SetState`,
`RequestGemLevelUp`, `SetThumb`, `Anvilheated`, `SeekingPlayer` are NON-virtual**,
so for those a whole-library `bl`/`blx` scan is a complete answer.

### 1.2 Call sites — complete, with negative results

Direct `bl`/`blx` callers found in the **entire executable segment**. Where a
function is non-virtual and has no direct caller, a 4-byte function-pointer
reference was also searched across `.rodata`, `.data.rel.ro`,
`.data.rel.ro.local`, `.data`, `.got`, `.init_array`, `.fini_array`, `.text`
(both even and Thumb-bit-set forms) — so "no caller" is not merely "no direct
call".

| Target (ELF) | Symbol | Call sites | Kind |
|---|---|---|---|
| `0x0bbd85c` | `OnInit` | **NONE direct** — vtable `+0x5c` | virtual |
| `0x0bbe700` | `CreateView` | `0x0bbe45c` (in `OnInit`), `0x0bbef68` (`blx`, in `SeekingPlayer`) | non-virtual |
| `0x0bbed0c` | `SeekingPlayer` | `0x0bbe464` (`OnInit`), `0x0bc130c` (`OnProcessKeyInput`), `0x0bc183a` (`OnRefresh`, **r1=1**), `0x0bc2408` (`UpgradeCB`, **r1=0**), `0x0bc13a0` (`blx`, tail of `UpgradeEvent`) | non-virtual |
| `0x0bbfef8` | `StatusUpdate` | `0x0bbe88c` (in `CreateView`), **r1 = 1** at `0x0bbff0c` | non-virtual |
| `0x0bc023c` | `SetThumb` | `0x0bbe8b2` (in `CreateView`) | non-virtual |
| `0x0bc0454` | **`SetBaseInfo`** | **`0x0bbe8ec` (in `CreateView`)** | non-virtual |
| `0x0bc0720` | `Anvilheated` | `0x0bbeb0a` (`CreateView`), `0x0bc320e`, `0x0bc338e` (both inside `__tree::__emplace_unique_key_args…` `STAT`→`STAT_BOX` map helpers) | non-virtual |
| `0x0bc0978` | `OnButtonClick` | **NONE direct** — vtable `+0x78` | virtual |
| `0x0bc0bf4` | `RequestGemLevelUp` | `0x0bc09f8` (`blx`, in `OnButtonClick`) | non-virtual |
| `0x0bc1326` | **`UpgradeEvent`** | **NONE — not in vtable, no pointer reference anywhere** | non-virtual, **uncalled** |
| `0x0bc13a4` | `OnRefresh` | **NONE direct** — vtable `+0x70` | virtual |
| `0x0bc1e8a` | `SetState` | **NONE — not in vtable, no pointer reference** | non-virtual, **uncalled** |
| `0x0bc1e90` | **`SetUpgradeComment`** | **`0x0bbf032` (in `SeekingPlayer`)** | non-virtual |
| `0x0bc2368` | **`UpgradeCB`** | **NONE `bl`/`blx`** — a **`.got` function pointer** @ `0x021ada74` | std::bind target |

Two negatives are load-bearing and **differ from each other**:

- **`UpgradeEvent` (0x0bc1326) is dead code in this build.** It is not virtual,
  has no `bl`/`blx` caller anywhere, and its address appears in **no**
  pointer-bearing section.
- **`UpgradeCB` (0x0bc2368) IS reachable, but only indirectly.** There is no
  direct call. It is the bound callback of the `std::bind` machinery
  (`__bind<CSRPopUpGemLevelUp::UpgradeCB, …placeholders 1,2,3…>`, dynsym
  `0x00bc42d2`–`0x00bc435c`); its address is referenced from **`.got` @ `0x021ada74`**.
  This matches the mangling (§1.1 of the parent report) and means
  "no `bl` caller" here is expected, **not** evidence of dead code.
- `SetState` (0x0bc1e8a) is likewise uncalled; its body is 6 bytes
  (`0x0bc1e8a`–`0x0bc1e8f`).

**Do not generalise**: `UpgradeEvent` being uncalled says nothing about
`SetState`'s or `StatusUpdate`'s intent, and none of these negatives says the
*original* 2.8.0.1 server never exercised them.

### 1.3 `UpgradeCB` — the `pair<int,int>` is the display discriminator

`UpgradeCB` @ `0x0bc2368` (151 instructions, `0x0bc2368`–`0x0bc24fe`) resolves
§1.3's central question. Its third parameter is `pair<int,int> const&`
(confirmed by mangling) and it is read as a **reference on the stack**, i.e. via
`r3`:

```
0x0bc2382  ldr  r5, [r3]        ; pair.first
0x0bc2384  cmp  r5, #1
0x0bc2386  bne  0x0bc243a      ; pair.first != 1  -> FAILURE path
0x0bc2388  ldr  r6, [r3, #0x4]  ; pair.second
```

**`pair.first == 1` is the success test.** `pair.second` is then used as a
**repeat count** for a node-append loop (`0x0bc23d4`–`0x0bc2402`, entered when
`r6 >= 1`, `subs r6,#1` / `bne`), each iteration allocating a 12-byte node via
`_Znwj` (0x01bc23c4) and writing `2` or `3` at node offset `+8`:

```
0x0bc23da  eor  r1, r6, #1
0x0bc23de  orrs.w r1, r1, r9     ; r9 = [gem_inst + 0x28]
0x0bc23e2  mov.w r1, #3
0x0bc23e6  it   eq
0x0bc23e8  moveq r1, #2
```

So the stored value is **`3` normally, `2` when `(repeat == 1) && (r9 == 0)`**.
`r9` is loaded from `[FindGemInst-result + 0x28]` at `0x0bc23a0`. This is the
**same `2`/`3` encoding** as the owned-instance `main`/`sub` split seen in
`gem-polish-parsers-2026-10-05.md`, but *which* field it denotes here is
**NOT proved** — do not label it "main"/"sub" from this alone.

**Success path** (`0x0bc238a`–`0x0bc2408`): `CSRGem::get()` (0x0a4c988) →
`CSRGem::FindGemInst(unsigned long)` (0x0a4d32c), whose two operands come from
the popup's own fields `[this+0x6a8]` and `[this+0x6ac]`
(`ldr.w r2,[r11,#0x6a8]` / `ldr.w r3,[r11,#0x6ac]`), then finally
`SeekingPlayer(0)` at `0x0bc2408` (`movs r1, #0x0`).

**Failure path** (`0x0bc243a`–`0x0bc2484`) is the display binding for errors:

```
0x0bc243a  movs r0, #0x0
0x0bc243c  str.w r0, [r11, #0x65c]     ; clear the in-flight/busy flag
0x0bc2440  bl   0x08a3390              ; CSRDataMgr::get()
0x0bc245a  bl   0x08a3260              ; CSRDataMgr::GetErrorStr(int, string&)
0x0bc2464  bl   0x0109c434             ; Toast(string, unsigned char, float)
```

`GetErrorStr` is called with **`r2 = r5 = pair.first`** — i.e. the **same value
that failed the `== 1` test** is used as the **error-code argument**. So the
`pair<int,int>` is `(error_code, repeat_count)`, and success is `error_code == 1`.

⚠️ **Correction to an easy inference:** the failure path's Toast string literal
resolves to the **empty string** `""` @ `0x1d52ab4` (slot `0x0bc24fc`). The
*user-visible* text therefore comes from `GetErrorStr`'s own table, **not** from
a key in `UpgradeCB`. Do not claim a per-code message string in this function.

**`UpgradeCB` also reads NO JSON.** It has **zero** `.rodata` string literals
(other than a `.got` reference). All response interpretation already happened
in `CSRGem::ParseGemLevelUp`. This is why §1.3 could not find display fields
here.

### 1.4 `UpgradeEvent` is the inlined twin of the `UpgradeCB` loop

`UpgradeEvent(int,int,int)` @ `0x0bc1326` has **no string literals** and **no UI
calls at all** — it is *not* a display function despite its name. Its body is:

- `0x0bc1336`, `0x0bc1366`: two 12-byte node allocations (`blx 0x0dfb280`,
  `movs r0,#0xc`);
- `0x0bc136a`–`0x0bc1378`: the identical `eor/orrs/mov #3/it eq/moveq #2`
  sequence;
- `0x0bc1394`–`0x0bc13a0`: `SeekingPlayer(0)` as a **tail call**
  (`b.w 0x0bbed0c`).

A blob comparison against the loop inlined in `UpgradeCB` (`0x0bc23d4`–`0x0bc2402`)
**normalising only the `this` register (r10 vs r11) and treating the backward
branch by PC-relative displacement** reports:

```
UpgradeEvent loop (0xbc1364-0xbc1392), this=r10, count = 8
UpgradeCB inlined loop (0xbc23d4-0xbc2402), this=r11, count = 8
text-level differences: 0
MNEMONIC+OPERAND SEQUENCE IDENTICAL
```

So the 8-instruction sequence is **the same code, emitted twice**. `UpgradeCB`
inlined it and also carries the `r9` operand; `UpgradeEvent` is the
never-called out-of-line copy. **This is why §1.3 could not find a call site for
it** — and it is a compiler artefact, not a gameplay fact. Do not report
`UpgradeEvent` as a live display path.

Two further identical-node-loop copies exist and were located for completeness:
`OnProcessKeyInput` (`0x0bc12d8`–`0x0bc1306`, guarded by
`cmp r2,#0x55 / cmpeq r3,#0x1` at `0x0bc1274`/`0x0bc127c`) and `Anvilheated`'s
two map-helper callers. All four share the `2`/`3` encoding, so the popup has a
**single** 12-byte "STAT_BOX" append idiom, keyed through the
`[this+0x750]` / `[this+0x758]` vector pair.

### 1.5 `StatusUpdate` — the only other animation driver, also not a UI-key binder

`StatusUpdate(unsigned char)` @ `0x0bbfef8` (343 instructions). Two real
literals: **`'upgrade_event'`** @ `0x1d6ea03` (ldr@`0x0bbfff6`) and **`'init'`**
@ `0x1d56d26` (ldr@`0x0bc0044`). Its only caller passes **r1 = 1**
(`mov r4, r1` at `0x0bbff0c`).

Its actual effect is an **animation sequence**, and the bindings are
`CMComponentPlayable` methods:

| Address | Call | Meaning |
|---|---|---|
| `0x0bc0056` | `CMComponentPlayable::SetGroup(CMHashID)` @ 0x006e1ec2 | group ← `"init"` |
| `0x0bc006a` | `CMComponentPlayable::Stop()` @ 0x006e18a0 | stop |
| `0x0bc0070` | `CMComponentPlayable::Rewind()` @ 0x006e197c | rewind |
| `0x0bc0076` | `CMComponentPlayable::Play()` @ 0x006e1846 | play |
| `0x0bbfff0` | `CMUIView::GetRoot()` @ 0x00773628 | view root |
| `0x0bc0006` | `CMUpdatable::FindComponent<CMComponentAnim>` @ 0x0087e55c | via `"upgrade_event"` |

`'upgrade_event'` is therefore a **CMComponentPlayable/CMComponentAnim
identifier**, not a server field and not a JSON key. It builds a string from
`"upgrade_event"` + 8 (`adds r1,#0x8` at `0x0bc0086`) before lookup
(`0x0bc2834` = `CMEventPool<…>::operator=`), i.e. the name is
**prefix + 8 characters**.

### 1.6 `/gem/LevelUp` request form keys — RECOVERED (supersedes parent §1.3 bullets 1–2)

Traced through `CSRPopUpGemLevelUp::RequestGemLevelUp(uint)` @ `0x0bc0bf4` →
`CSRGem::RequestGemLevelUp(uint64, uint, cb)` @ `0x0a4811c`. The latter builds
its body via `CPVHTTPRequest::Create<…CPVHTTPMapToEncodedURLFormTransformer…>`
(0x007b9d60, `REQ_METHOD` = 2 at `0x0a48430`), so the map keys are the literal
form fields.

| Key | ELF `.rodata` addr | ldr / add | Value source |
|---|---|---|---|
| `app_code` | `0x1d589d0` | `0x0a48150` / `0x0a48152` | SSO literal (`_SR`-family global) |
| `app_ver` | `0x1d589d9` | `0x0a4817a` / `0x0a4817c` | `CPVDataMgr::get()` @ `0x0a4818c` |
| `market` | `0x1d589ee` | `0x0a48198` / `0x0a4819a` | `to_string(PV_MARKET)` @ `0x0a48194` |
| `pvid` | `0x1d586aa` | `0x0a481c6` / `0x0a481c8` | `ldrd r2,r3,[r0,#88]` @ `0x0a481bc` |
| `otp` | `0x1d589ea` | `0x0a481f2` / `0x0a481f8` | `CPVDataMgr::GetOTP()` @ `0x0a481ee` |
| **`inst_id`** | `0x1d5eec9` | `0x0a48284` / `0x0a48286` | **`r2`, the popup's `uint` argument** |
| **`max_tries`** | `0x1d68620` | `0x0a482ae` / `0x0a482b0` | the same `r2` |
| `/gem/LevelUp` | `0x1d6862a` | `0x0a4842a` / `0x0a4842c` | route |

Route literal `"/gem/LevelUp"` @ `0x1d6862a` (the only occurrence of that byte
string in the whole file).

**This resolves the parent report's §1.3 hypothesis, and it is not what the
report guessed.** The report speculated the request `uint64` was the target gem
`inst_id` and the popup `uint` was `price_type`. Instruction evidence instead
shows:

- `CSRPopUpGemLevelUp::RequestGemLevelUp(uint r1)` stores r1 to
  `[this+0x6bc]` at `0x0bc0f00` (`str.w r9,[r5,#0x6bc]`) and passes it as **r2**
  to `CSRGem::RequestGemLevelUp` at `0x0bc0f2e`;
- in `CSRGem::RequestGemLevelUp`, that r2 is kept in `r11` (`0x0a4812e`) and
  becomes the value of **both** `inst_id` (`0x0a4827a`: `mov r2, r11`) and
  `max_tries` (`0x0a482d4`: `movs r2,#0x7` — a **constant 7**, *not* r11).

So **`inst_id` and `max_tries` are DIFFERENT values**: `inst_id` = the popup's
`uint`; `max_tries` = the literal `7`. The report's "one scalar is price_type"
framing is **withdrawn**; `price_type` does not appear as a request field, and
`FindGemLevelUpPrice(int, PRICE_TYPE)` @ `0x0a44f00 is **not called** from this
path. **Any `price_type`-keyed request schema is now positively falsified.**

Also recovered on this path: `RequestGemLevelUp` has a **client-side
precondition gate** before any HTTP — `ldr.w r0,[r5,#0x7b8]; ldr r0,[r0,#0x1c];
cmp r0,#0xe; bhi` (`0x0bc0c12`–`0x0bc0c1a`) plus a busy-flag test
`ldr.w r0,[r5,#0x65c]; cbz` (`0x0bc0c1c`–`0x0bc0c20`), and a wallet check that
Toasts a **Korean** literal `'루피가 부족합니다.'` @ `0x1d61416`
(ldr@`0x0bc0c5a`) when insufficient. That string is a shipped UI resource, not
a statistic, and is recorded as a binding only.

**`/gem/LevelUp` response fields remain unrecovered.** `ParseGemLevelUp`
(`0x0a5e43c` Ghidra / `0x0a4e43c` ELF) was **not** disassembled in this pass —
it is a JSON parser, not a display binder, and §1.3 of the parent report
correctly scoped it out. **Do not build a response receipt from this section.**

### 1.7 UI node / anim / effect keys resolved, per function

All keys below are **UI resource identifiers** looked up through
`CMHashID`, `FindCastByName`, or `FindComponent`. None is a server field.

**`OnInit`** (`0x0bbd85c`, 18 literals) — builds the view and its animation set:

| Key | Role (by consumer) |
|---|---|
| `SR_GEM/GEM_REFINE` | `CSRFramedScene::LoadView(const char*, …)` — **the popup's UI record name** |
| `BTN_UPGRADE`, `BTN_UPGRADE_10` | buttons (single / ×10 polish) |
| `TX_PERCENT` | success-rate textbox |
| `TX_MY_CO` | currency textbox |
| `ANIM_WAIT`, `ANIM_TRY`, `ANIM_SUC`, `ANIM_FAIL` | **the four polish animation states** |
| `G_ANVIL_RED` | anvil image |
| `PA_GEM_ST_LIST` | stat-list panel |
| `GEM_SB`, `GEM_NM_RE`, `GEM_NM_RE_P`, `SK_ANI_1` | stat box, name (+`_P` variant), effect anim |
| `gem_upgrade`, `gem_upgrade_inst_id` | **`CSRPlayData` markers**, not UI: `CSRPlayData::GetMarker(string const&)` @ 0x00b62798 (`0x0bbe3a6`) and `CSRPlayData::RemoveMarker(string const&)` @ 0x00b626c0 (`0x0bbe43e`), fed from a `basic_json` marker lookup (`operator[]` @ 0x007830f8 at `0x0bbe3c4`). The parsed marker feeds `str.w r5,[r6,#0x6a8]` @ `0x0bbe452` and `movs r0,#0; str.w r0,[r6,#0x6ac]` @ `0x0bbe456` — **the same two popup fields `UpgradeCB` reads** as `FindGemInst`'s operands (§1.3) |

`OnInit` also consumes a Korean localised string @ `0x1d6e903`, decoded as
`'보석 제련'` (gem refining), via `CGMDataMgr::GetLocalizedText(const char*)`
@ `0x0bbd898`.

**`CreateView`** (`0x0bbe700`, 5): `PA_BAIT1`, `PA_BAIT2` (material/bait panels),
`TX_SE_SO_NM` (×2, name text), `PA_BTN`.

**`SeekingPlayer`** (`0x0bbed0c`, 11): `RE_GEM_RIGHT`, `RE_GEM_RIGHT2`
(`CMShader::CM_GRAYSCALE`+`SetRenderOption` → **greyscale when unaffordable**),
`BG_RIGHT1`, `BG_RIGHT2` with `rot`/`alpha` render-param pairs,
**`SUC_EFF`** (success effect). The two callers that matter set its `unsigned
char`: **`OnRefresh` passes 1** (`movs r1,#0x1` at `0x0bc1838`), **`UpgradeCB`
passes 0** (`0x0bc2406`). The argument is preserved to `r8` at `0x0bbed1a`
(`mov r8, r1`); **its internal use was not traced in this pass**, so the
0-vs-1 meaning remains unproved (see §1.8).

**`SetBaseInfo(string const&, uint)`** (`0x0bc0454`, 4 literals) — the
`(string, uint)` signature binds name + a value:

| Key | addr |
|---|---|
| `UI_EN_SB_BG` | `0x1d6e8c9` (slot `0x0bc0710`) |
| `GEM_NAME1` | `0x1d6e9dd` (slot `0x0bc0714`) |
| `UI_SB_TX_ME` | `0x1d6e7c1` (slot `0x0bc0718`) |
| `UI_SB_TX_MX` | `0x1d6e7cd` (slot `0x0bc071c`) |

`UI_SB_TX_ME` / `UI_SB_TX_MX` are the two stat-value textboxes; which of the two
the `uint` argument selects was **not** determined (the selection is a runtime
branch, and this pass did not resolve which operand feeds it).

**`SetThumb(shared_ptr<CSRGem::PLAY_DATA>)`** (`0x0bc023c`, 1): **`RE_GEM`** @
`0x1d6e785`.

**`Anvilheated(int)`** (`0x0bc0720`, 2): the literal **`'%'`** @ `0x1d5fd6f`,
used **twice** — at `0x0bc0804` (visible branch) and `0x0bc0822` (hidden
branch), each feeding `floating_point::to_string(int)` (0x006ca86c) +
`CSRUITextbox::SetText` (0x007a5bfc). So `Anvilheated(int)` renders a
**percentage-formatted number**, gated on a float comparison at `0x0bc07f0`
(`vsub.f32 s0, s16, s0` / `vcmpe.f32` / `ble`). Its own display is a `'` + value
+ `%'`; the **numerator/denominator sources are not identified in this pass.**

**`OnButtonClick`** (`0x0bc0978`, 3): `BT_UPGRADE`, `BT_UPGRADE_10`,
`BT_MY_CO`. Calls `RequestGemLevelUp` at `0x0bc09f8`.

**`OnRefresh`** (`0x0bc13a4`, 10 literals): `RE_GEM_RIGHT`, `RE_GEM_RIGHT2`,
`PA_BAIT1`/`BT_FI_BA`/`IT_CO` (one triple), `PA_BAIT2`/`BT_FI_BA`/`IT_CO`
(second triple — **same keys as `RequestGemLevelUp`**, i.e. `OnRefresh`
rebuilds the same rows), `BT_UPGRADE`, `BT_UPGRADE_10`. It also drives
number textboxes through `SRCalculationFloatString(float,unsigned)`
(0x0109d080) and `SRGetNumberKMB(unsigned)` (0x0109e4bc) with
`CMCurve<float>::GetFactor()` / `CMCurve<int>::GetFactor()` (0x00790458 /
0x0073ef94) — i.e. **animated/interpolated stat counters**, and the `KMB`
suffix formatter implies a magnitude abbreviation. This is a display-only
mechanism; no balance value was read from these.

**`SetUpgradeComment(ANIM_TYPE)`** (`0x0bc1e90`, 5 literals) — **this is the
success/failure comment binder**, and it is **called only from `SeekingPlayer`**
(`0x0bbf032`):

| Key | addr | Note |
|---|---|---|
| `EAST_SUC` | `0x1d6ea11` | localised via `FindCastByName<CMUIBase>` (0x00b801f4) |
| `[강화성공]메시지` | `0x1d6ea1a` | **Korean format template**, inserted by `basic_string::insert(size_t, const char*, size_t)` @ `0x0bc1f0e` with length `0x17` = 23 |
| `EAST_FAIL` | `0x1d6ea32` | localised key |
| `[강화실패]메시지` | `0x1d6ea3c` | Korean template, same 23-byte insert |
| `UI_EAST_TXT` | `0x1d6ea54` | the textbox that receives the composed string |
| `RE_BG` | `0x1d6ea60` | background node |
| `alpha` | `0x1d5545d` | render param |

Its dispatch is a **two-value enum test**, `cmp r1,#0x3` (`0x0bc1ea2`) then
`cmp r1,#0x2` (`0x0bc1eba`):

- `== 2` → the **EAST_SUC** branch (`0x0bc1ec4`);
- `== 3` → the **EAST_FAIL** branch (`0x0bc1f66`);
- anything else → the default branch at `0x0bc2022`, which does
  `CMUpdatable::SetVisible(1)` on a null handle (`0x7782a0`), binds `UI_EAST_TXT`,
  and sets `RE_BG` alpha.

**Important**: `SetUpgradeComment` never reads a random value to decide
success. It receives an `ANIM_TYPE` from `SeekingPlayer`, which itself receives
it from `UpgradeCB`'s `2`/`3` node encoding (§1.3/§1.4). So the
success/failure comment is driven by **the same `2`/`3` value written into the
STAT_BOX node**, not by an independent probability check in the popup.

### 1.8 What §1.3 explicitly does NOT close

- **`ParseGemLevelUp` response fields: still unrecovered.** Not disassembled
  here. `UpgradeCB` proves the popup reads *no* JSON, so the response contract
  must come from that parser, not from the popup.
- **`price_type` on the `/gem/LevelUp` wire: positively absent** (§1.6).
- **`Anvilheated`'s numerator/denominator operands: unidentified.** The `'%'`
  binding is proved; the two values are not.
- **`SetBaseInfo`'s `uint` → `UI_SB_TX_ME` vs `UI_SB_TX_MX` selection: unproved.**
  Both textboxes are bound (`0x0bc0516` and the later `SetText`), and the branch
  structure around them tests `cbz r4` (`0x0bc052a`), `cmp r3,#0` (`0x0bc053c`)
  and `cbnz r1` (`0x0bc0544`) — but the `uint` argument (r8, saved at
  `0x0bc0468`) was not traced to either test.
- **`SeekingPlayer`'s `unsigned char` semantics (0 vs 1): named only by call
  site**, not by internal contract. The value reaches `r8` at `0x0bbed1a`; its
  first *test* was not located in this pass.
- The `2`/`3` STAT_BOX value's **field identity** is still unnamed; do not
  inherit "main"/"sub" from the inventory parser without a binding argument.
- **No original numeric gem balance, possibility, or compensation was
  recovered.** See §2.

---

## 2. UNPURE — every numeral encountered (rebalance leads ONLY, no coverage)

**None of the following counts toward any 70% threshold.** No jewel stat row,
hero tuple, or monster tuple is recovered by this pass; strict coverage is
unchanged (heroes **1/113**, accessories **1/100**, monsters **0/22**).

### 2.1 Numerals that are structural, not economic

Marked impure for completeness; they carry no balance meaning.

| Numeral | Site | What it actually is |
|---|---|---|
| `1` | `0x0bc2384` | `pair.first == 1` success test — a **result code**, matching the project's standing `result_code: 1` finding |
| `2` / `3` | `0x0bc1372`/`0x0bc1378` | STAT_BOX node field encoding (`3`, or `2` when repeat==1 && `[gem_inst+0x28]==0`) — a **discriminator**, not a stat |
| `7` | `0x0a482d4` | `max_tries` request field — a **client-side retry cap**, value is a shipped constant |
| `0xe` (14) | `0x0bc0c18` | pre-request gate threshold on `[this+0x7b8]+0x1c` |
| `0x12` / `0x17` (18 / 23) | `0x0bc0086`, `0x0bc1f0a` | `CMHashID` name offset (+8) and byte length of the Korean comment templates |

### 2.2 Numeral-shaped values encountered but NOT interpreted

| Observation | Site | Status |
|---|---|---|
| `Anvilheated(int)` renders `'%'`-formatted text on a float compare | `0x0bc07f0`, `0x0bc0804`, `0x0bc0822` | **Purely a formatting binding.** The compared float's provenance is unidentified; **no possibility/success-rate value recovered.** |
| `OnRefresh` uses `SRCalculationFloatString` and `SRGetNumberKMB` | `0x0bc198c`, `0x0bc1afc` | Interpolated **display** counters. The `KMB` suffix implies a magnitude abbreviation, but **no threshold numeral was read**; this is a formatter, not a stat. |
| Korean comment templates `[강화성공]메시지` (23 B), `[강화실패]메시지` (23 B) | `0x1d6ea1a`, `0x1d6ea3c` | **UI template strings**, locale KO. Not numerals. |
| `루피가 부족합니다.` | `0x1d61416` | Insufficient-funds Toast, KO locale. Not a numeral. |
| `RE_GEM_RIGHT`/`RE_GEM_RIGHT2` greyscale | `0x0bbef8c`+ | Affordability **styling**, no amount. |

### 2.3 Unchanged from prior gem passes

The impure set is **unchanged** from
[`gem-polish-parsers-2026-10-05.md`](gem-polish-parsers-2026-10-05.md) §2 and
[`gem-levelup-action-2026-10-05.md`](gem-levelup-action-2026-10-05.md) §2
(removal footer 40000/40, 600k refine budget, ★4/★3 trace rates 700/350 per 8,
POST-era growth +30%/%50, untranscribed Namu equipment tables). **This pass
added no new economic numeral.** It added a *mechanism* — the
`error_code==1` / `2`-vs-`3` discriminator and the `'%'` display path — which
constrains how a future balance reading must be interpreted, but supplies no
amount.

---

## 3. Retractions and corrections made in this pass

Recorded because AGENTS.md §15 requires distinguishing recovered from inferred,
and because two earlier statements are now wrong.

1. **"Popup request `uint32` is plausibly `price_type`" — RETRACTED.**
   `price_type` does not appear as a `/gem/LevelUp` form field
   (exhaustive literal list, §1.6), and `FindGemLevelUpPrice(int, PRICE_TYPE)`
   is not called on this path. Do not build a `price_type`-keyed schema.
2. **"Popup request `uint64` is plausibly the target gem `inst_id`" — REFINED,
   not confirmed.** The popup passes a single `uint` which becomes `inst_id`,
   but the same value **also** flows into the popup's own `[this+0x6bc]`, and
   `max_tries` is an independent constant. The `uint64` in
   `CSRGem::RequestGemLevelUp(uint64, uint, cb)` is r2 **as a 32-bit value**;
   its 64-bit width is not independently exercised here.
3. **"`UpgradeEvent` is a display binding helper" — RETRACTED.** It is
   uncalled dead code whose body is the compiler-emitted twin of the loop
   inlined in `UpgradeCB` (§1.4). It contains no UI call and no string.
4. **"`StatusUpdate`/`SetUpgradeComment`/`SetBaseInfo` have untraced call sites"
   — CLOSED**, with exact sites in §1.2. `SetState` is *also* uncalled; that
   was not previously stated.
5. **Methodological:** the first two literal-resolver runs reported **0
   literals across every function**, which was false. Both the zero and the
   later all-pass are recorded here because a "clean" resolver result that was
   never cross-checked would have produced a confidently wrong file.

## 4. What would close the remaining §1.8 gaps

1. `CSRGem::ParseGemLevelUp` (`0x0a4e43c` ELF) decompilation — the **only**
   remaining source of `/gem/LevelUp` response fields.
2. `CSRGem::FindGemLevelUpPrice(int, PRICE_TYPE)` (`0x0a44f00`) callers —
   establishes where `price_type` *is* used, now that it is absent from the
   request.
3. A `readOnly -noanalysis` headless pass (per §119/§121 precedent, no Ghidra
   lock contention) for items 1–2, or an operand-flow trace of
   `Anvilheated`'s float sources and `SetBaseInfo`'s `uint` branch.