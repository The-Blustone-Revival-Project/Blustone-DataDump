# Native literal resolver hardening — 2026-10-05

**Lane:** harden the Thumb literal-pool resolver, per the tooling implication in
[`grouprankup-sellcard-bodies-2026-10-05.md`](grouprankup-sellcard-bodies-2026-10-05.md)
§1.0 ("Tooling implication for the parent: the resolver's acceptance test is
printable-ASCII, which is not sufficient — a segment check … would close this
class of false positive"), using the self-test discipline of
[`gem-popup-bindings-2026-10-05.md`](gem-popup-bindings-2026-10-05.md) §1.0 and
the file-hygiene rules in
[`GUARD-encoding-and-archive-traps.md`](GUARD-encoding-and-archive-traps.md).

**Deliverable:**
[`resolve-literals-segment-aware.py`](resolve-literals-segment-aware.py) — a
corrected, self-testing, segment-aware replacement for
`tools/resolve-literals-offline.py`.

**Status: VALIDATED for the two known-good ground-truth dumps** (20/20
re-derivations byte-identical, plus a proven non-vacuous gate). The segment rule
itself is a **local heuristic** — see §1.7.

**Read-only compliance.** No Ghidra project was opened or written. The library
`analysis/extracted/lib/armeabi-v7a/libnative_core.so` was opened read-only and
is unmodified. The only workspace writes this run are the new resolver script and
this file. **`polluted-observations.md` was deliberately NOT appended** — the
parent mirrors it.

**Coverage unchanged** and irrelevant to this pass: heroes **1/113**,
accessories **1/100**, monsters **0/22**. Nothing below is a hero, accessory or
monster statistic.

---

## 1. PURE — the segment rule, the mapping, the defects, the self-test

### 1.1 Address conventions, and the anchors that pin them

Mixing conventions is AGENTS.md §16.7 lesson 3, and `gem-popup-bindings` §1.0
records it already having produced **0/13** in a private tool. So the convention
is stated once here and every number in this file is labelled.

| Kind | Convention | Anchor (verified) |
|---|---|---|
| Canonical internal space of the new tool | **ELF VA** | — |
| Ghidra image address | ELF VA **+ 0x10000** | `llvm-nm -D`: `RequestGroupRankUp` = ELF `0x00f486e4`; Ghidra `0x00f586e4` |
| `analysis/ghidra-*.txt` dumps (`ldr@`/`slot=`/`add@` **and** the `->` target column) | **Ghidra** | `ghidra-wave-keys.txt` `ldr@00a0d1b0` = ELF `0x009fd1b0`, confirmed by `llvm-objdump` `9fd33e: 4971 ldr r1,[pc,#0x1c4]` and by the slot word landing byte-exact |
| `.rodata` string addresses in `gem-popup-bindings-2026-10-05.md` | **ELF VA** | `GEM_NAME1` at file `0x01d6e9dd` = `'GEM_NAME1'` byte-exact. ⚠️ the negative address in this cell was mis-stated as `0x01c6e9dd`; `0x01d6e9dd − 0x10000` = **`0x01d5e9dd`** (corrected 2026-10-05), and `d[0x01d5e9dd] == b'itle\x00'` |
| `.rodata` string addresses in `grouprankup-sellcard-bodies-2026-10-05.md` | **Ghidra**, despite its note saying "ELF VA" (⚠️ that note was **fixed 2026-10-05**; see the ✅ block below — the column was and is Ghidra) | `/gym/RankUpBundle` is at file `0x01d7f7d4`; the report lists `0x01d8f7d4`. Same for `inst_id_list` (file `0x01d68609`, listed `0x01d78609`) and `removed_inst_id_list` (file `0x01d7f8b7`, listed `0x01d8f8b7`) |

**Documentation defect found (not a resolver defect).**
`grouprankup-sellcard-bodies-2026-10-05.md` line 18 states
"`0x01dxxxxx` = `.rodata` literal address" and its §1 convention note calls
those ELF VA. Its **code** addresses are Ghidra (correct, and confirmed against
`llvm-nm`), but its **`.rodata` literal column is also Ghidra**, so the stated
convention is wrong for the literal columns of §1.1/§1.2/§1.3/§1.4. This is the
*same class* as the defect `gem-popup-bindings` §1.0 defect 1 hit inside a tool,
now recurring across two documents in the same folder. **Do not copy a literal
address out of one report into the other without re-deriving it.**

> ✅ **RESOLVED 2026-10-05 — this paragraph and the table row above it now
> describe a fixed state; read them as history, not as a live defect.**
> `grouprankup-sellcard-bodies-2026-10-05.md` has since been corrected in place:
> its header carries a `CONVENTION CORRECTION 2026-10-05` block stating that
> **both** columns are ELF VA + `0x10000`, with five byte-exact spot proofs
> (`/gym/RankUpBundle` `0x01d8f7d4` → file `0x01d7f7d4`, and four others), and its
> §1.0 `'X'` row now carries a note that `0x021bebb4` is the old tool's biased print
> rather than an ELF VA. Its table values were always correct as printed; the note
> was what was wrong, which is the same conclusion this paragraph reached. A full
> byte-level re-verification is in
> [`address-convention-2026-10-05.md`](address-convention-2026-10-05.md) §6.1
> item 4: **36/36** of that file's literal pairs are Ghidra. **The rule in this
> file's §1.1 table is unchanged and remains the one the folder defers to** — it
> was correct when written and is still correct.
>
> Residual cleanup this pass: `address-convention` §6.1 item 4 *stated* that
> grouprankup §1.0's `0x021bebb4` had been corrected, which it had **not** — see
> `c4-row-census-2026-10-05.md` §5.2. Now fixed there.

### 1.2 The PT_LOAD table, and which sections live where

Reproduce with `--list-segments`. Read from the ELF32 program headers; segment
0 has `p_vaddr == p_offset`, segment 1 does **not**.

```
PT_LOAD  VA 0x00000000..0x0210d320  filesz 0x0210d320  memsz 0x0210d320  R-X  off 0x00000000  delta 0x0
PT_LOAD  VA 0x0210e550..0x028bc790  filesz 0x000bfe6c  memsz 0x007ae240  RW-  off 0x0210d550  delta 0x1000
```

| Section | ELF VA range | Segment | Literals live here? |
|---|---|---|---|
| `.text` | `0x00612cc0`–`0x01bd46f8` | R-X | no (this is where the *pool slots* live) |
| `.ARM.exidx` | `0x01bd46f8`–`0x01c2cc20` | R-X | no |
| `.ARM.extab` | `0x01c2cc20`–`0x01d52928` | R-X | no |
| **`.rodata`** | **`0x01d52940`–`0x0210d094`** | **R-X** | **yes — 100% of the 20 ground-truth targets** |
| `CryptoPP_Align16` | `0x0210d0a0`–`0x0210d320` | R-X | no |
| `.data.rel.ro.local` | `0x0210e550`–`0x02134930` | RW- | no |
| `.data.rel.ro` | `0x02134930`–`0x021aa854` | RW- | no |
| `.fini_array` / `.init_array` / `.dynamic` | `0x021aa854`–`0x021aafe0` | RW- | no |
| **`.got`** | **`0x021aafe4`–`0x021b3000`** | **RW-** | no — but this is where the phantoms live (§1.5) |
| `.data` | `0x021b3000`–`0x021ce3bc` | RW- | no |
| `.bss` | `0x021ce3c0`–`0x028bc790` | RW- (**no file bytes**) | no |

### 1.3 The rule (D1): a literal must land in a read-only mapping

> **A resolved target is accepted as a string literal only if it maps to file
> bytes inside a PT_LOAD segment whose `p_flags` have `PF_W` clear, and the
> NUL terminator lies inside that same segment. Canonical arithmetic is**
>
> ```
> slot_elf   = ((ldr_elf & ~3) + 4 + imm) & ~3
> target_elf = u32(slot_elf) + (add_elf + 4)
> ```
>
> **and the VA→file-offset mapping comes from the program headers, never from a
> uniform bias.**

Why this is the right rule for *this* library: every one of the 20 known-good
targets is in `.rodata`, inside the R-X segment, and the `.got`/`.data.rel.ro`
address-of-a-global idiom (§1.5) can only ever land in the RW- segment.

Why it is a heuristic and not a proof: the rule cannot distinguish a *string
that happens to be placed in writable memory* from a pointer. It is stated here
as an **acceptance filter with a measured false-positive rate**, not as a
semantic proof. `--allow-rw` turns it off and exists only so the phantom
population can be measured (§1.5).

### 1.4 Every case the unhardened resolver gets wrong

`tools/resolve-literals-offline.py` is correct for the two ground-truth dumps
and wrong in six independent ways. Each was reproduced, not inferred.

#### D1 — no segment check (the requested fix)

The acceptance test in `--function` mode is
`all(32 <= ord(c) < 127 for c in s)`. A load that computes the **address of a
global object** satisfies that test whenever the bytes behind that address
happen to be printable.

Documented instance, reproduced verbatim:

```
$ python tools/resolve-literals-offline.py --function 0xf58900:0xf58a00
ldr@0x00f589e6 r0 slot=0x00f58ac8 w=0x012661c6 add_pc=0x00f589ee -> 0x021bebb4  'X'
```

> ⚠️ **The `-> 0x021bebb4` in that transcript is NOT an ELF VA** (corrected
> 2026-10-05). It is the old tool's *own* print, and the bug bites one step
> **earlier** than §1.4-D2 describes: the pool word is **raw and unbiased**
> (`w=0x012661c6`, read straight out of `.text`), so it must be added to the
> **ELF** `add_pc`. The tool added its **Ghidra** `add_pc=0x00f589ee`:
>
> ```
> correct  ELF : 0x012661c6 + 0x00f489ee = 0x021aebb4   <- the true target, in .got
> tool    print: 0x012661c6 + 0x00f589ee = 0x021bebb4   <- +0x10000 too high
> ```
>
> So **D3 (mixed coordinate spaces) and D2 (naive file mapping) are independent**,
> and both fire on this single site: the print was already `+0x10000` too high, and
> `to_file_offset` then subtracted `0x10000` once more, landing on file offset
> `0x021aebb4` and printing the phantom `'X'`. Full derivation and byte proof:
> `address-convention-2026-10-05.md` §5.

Ground truth for that site (from the instructions, not from any tool):

```
0x00f489e6  4838       ldr   r0, [pc, #0xe0]
0x00f489e8  9905       stmia r1!, {...}          ; 32-bit
0x00f489ea  4478       add   r0, pc              ; computes an ADDRESS, not a literal
```

* the pair is real; the **target** ELF `0x021aebb4` is in the **RW-** segment and
  in **`.got`**;
* it sits inside `CSRSyncCard::RequestGroupRankUp` (ELF `0x00f486e4`–`0x00f48da0`
  per `llvm-nm -D`), i.e. the reported site Ghidra `0x00f589e6` / ELF
  `0x00f489e6` is correct;
* `.got` here holds **relocated code pointers**: the `u32` at ELF `0x021aebb4` is
  `0x00f48da1` and at `0x021aebb8` is `0x01e7a185`, both odd (Thumb) addresses in
  R-X. This is the same idiom already documented in
  `gem-popup-bindings-2026-10-05.md` §1.2 for `UpgradeCB` (a `.got` function
  pointer reached only through `std::bind`) — there it made "no `bl` caller"
  mean "reachable indirectly"; here it makes an address computation look like a
  string.
* this is **not** a one-off. The byte pattern
  `4838 9905 4478` occurs **exactly twice** in `.text`: ELF `0x00f489e6`
  (target ELF `0x021aebb4`) and ELF `0x00f77bfe` (target ELF `0x021aed38`).
  Both targets are in `.got`.

  > ⚠️ **Byte-order correction, 2026-10-05** (measured in
  > [`c4-row-census-2026-10-05.md`](c4-row-census-2026-10-05.md) §5.1). The
  > pattern as written above, `48 38 99 05 44 78`, occurs **zero** times in the
  > whole file. It is written in **mnemonic-halfword** order (`ldr r0,[pc,#0xe0]`
  > = `4838`), not byte order. The true little-endian **byte** sequence at
  > `0x00f489e6` is:
  >
  > ```
  > written as halfwords : 4838  9905  4478      <- 0 hits, 2-byte-aligned: 0
  > actual byte order    : 38 48 05 99 78 44      <- 2 hits: 0x00f489e6, 0x00f77bfe
  > ```
  >
  > The **count (exactly twice) and both addresses are correct** and are
  > re-derived and confirmed here; only the byte-order presentation was wrong, so
  > the claim was unverifiable as written. Both sites re-derived from the pool:
  >
  > | site (ELF) | `slot` | pool word (raw) | target ELF VA |
  > |---|---|---|---|
  > | `0x00f489e6` | `0x00f48ac8` | `0x012661c6` | `0x021aebb4` |
  > | `0x00f77bfe` | `0x00f77ce0` | `0x01237132` | `0x021aed38` |
  >
  > (`target = word + (add_pc + 4)`.) To reproduce, search for the byte string
  > `38 48 05 99 78 44`, not for the halfwords.

#### D2 — uniform `addr - 0x10000` file mapping (this is what printed `'X'`)

`to_file_offset(a) = a - 0x10000` is correct only for the first PT_LOAD, where
`p_vaddr == p_offset`. For the RW- segment here `p_offset == p_vaddr - 0x1000`,
so every read below `0x0210e550` was **0x1000 bytes too low**:

```
target ELF            0x021aebb4
old tool file offset  0x021aebb4   -> b'X\x00\x1c\x02\xf8\x01\x1c\x02...'   <-- the phantom
correct file offset   0x021adbb4   -> b'\xa1\x8d\xf4\x00\x85\xa1\xe7\x01...'  (pointer pair)
```

⚠️ **Corrected 2026-10-05:** this table's middle cell originally read
`0x021bebb4`. The old tool printed target `0x021bebb4` and then applied
`− 0x10000`, so the file offset it actually read — and the one that really contains
`b'X\x00\x1c\x02…'` — is **`0x021aebb4`**. All three numbers above are now
self-consistent: ELF VA `0x021aebb4` → file offset `0x021adbb4` (pointer pair
`0x00f48da1`, `0x01e7a185`), which is exactly what §1.4-D1's prose already said.

So the `'X'` is a **mapping artefact, not merely a missing filter**: the old tool
read a pointer table and took its first printable byte. D1 would have rejected
this target anyway; D2 is what makes the *string* wrong. Both are fixed.

#### D3 — coordinate convention silently assumed

The old tool has one hard-coded `ADDR_BIAS = 0x10000` used for input, for slot
reads and for target reads, with no way to see or change it. It happens to be
self-consistent only because every real literal sits in segment 0. Its
`--from-dump` path and its `--function`/`--find-string` paths use the bias
differently and neither states which space it is printing. `gem-popup-bindings`
§1.0 defect 1 is exactly this, and §1.1 above shows the same confusion has now
leaked into a written report.

The new tool has `--addr-convention {ghidra,elf}` (input, default `ghidra`,
matching every dump in `analysis/`) and `--out-convention`, prints
`# in=… out=…` on every run, and does all arithmetic in ELF VA so the bias
appears exactly once per boundary crossing.

#### D4 — no self-test; `--expect` is a no-op

The old tool accepts `--expect`, and for `--from-dump` responds:

```
NOTE: --expect is only meaningful for --function scans
```

…then asserts nothing. A flag that *looks* like a self-test and silently does
not is worse than no flag. There is also no check against any ground truth, and
no gate: `--from-dump` prints `resolved: 7` whether the 7 strings are right or
wrong.

#### D5 — the load and its `add` are assumed adjacent (2 or 4 bytes only)

`iter_thumb_ldr_addpc` walks back only `for width in (2, 4)`. Measured over the
20 known-good sites:

| gap (bytes) | sites | old tool |
|---|---|---|
| 2 | 3 | recovered |
| 4 | 12 | recovered |
| 6 | 4 | **MISSED** |
| 10 | 1 | **MISSED** |

**Old structural recall against ground truth: 15/20 = 75%.** The 5 misses are
real keys (`ref_id`, `group`, `ret_data`, `rank`, `ability`, `0`, …). This is the
false-negative class `gem-popup-bindings` §1.0 defect 4 and
`grouprankup-sellcard-bodies` §1.3 (its `otp` note) both describe; it is now
quantified. The new default `--window 12` covers all 20; `--window 4` reproduces
the old behaviour exactly.

Widening is only safe *because* D1+D2 reject what the extra reach admits — the
old docstring's "widen with suspicion, never narrow" is right, but only once a
real filter exists.

#### D6 — `--from-dump` applies no acceptance test at all

`resolve_from_dump` prints `lib.cstr(...)` unconditionally: no segment check, no
plausibility check. Hand it a line whose slot is in `.got` and it will print
binary noise as a "string". `--find-string` likewise filters only by substring.

#### R1 / R2 — two guarded recall bugs (found while hardening, not pre-existing)

`gem-popup-bindings` §1.0 defect 3 records that a private resolver rejected a
legitimate **1-byte** literal (`" "`) on a `len >= 2` guard. The new tool accepts
`len >= 1`; `ghidra-gem-inventory-keys.txt` line 20 (`GetSetEffectDesc`, ELF
`0x00a4ffca` → `.rodata` ELF `0x01d550c1`) is that case and passes.

The old tool's `--function` test `32 <= ord(c) < 127` also silently discards
**every Korean/CJK literal** in this binary — `gem-popup-bindings` §1.6/§1.7
recovered such strings only by reading `llvm-objdump` text by hand, precisely
because the tool could not return them. The new test rejects only C0/C1 control
characters and DEL, so UTF-8 literals survive (tagged by section, still
`.rodata`).

#### Defects found *inside the new tool* by its own self-test

Recorded because AGENTS.md §15 requires distinguishing what was measured from
what was assumed; each was caught by the gate, not by inspection.

1. **`decode_ldr_pc_imm` wrongly required `Rn == 15` for T1.** In Thumb-1
   `LDR (literal)` the 3-bit field is the *destination* `Rt` and the base is
   implicitly PC; there is no `Rn` field to test. This rejected all 20 sites.
2. **The `.shstrtab` table was located by `sh_addr`.** `.shstrtab` is non-alloc,
   so its `sh_addr` is 0 and every section name came out as garbage read from the
   ELF header. Must be `sh_offset`.
3. **The 32-bit-branch test used `((hw >> 11) & 3) == 2`.** That also matches
   ordinary 16-bit instructions whose top bits are `100xx` — e.g.
   `str r0,[sp,#0x18]` (`0x9006`). Four ground-truth sites were abandoned.
   The mask must be `& 0x1F` against `{0x1D,0x1E,0x1F}`.
4. **hw1 alone cannot identify `bl`.** `add.w r0,r4,#0x60` (`0xF104 0x0060`) and
   `bl` (`0xF169 0xD64C`) share hw1's class. The discriminator is in hw2:
   `(hw2 & 0xD000) == 0xD000`. Without this, the `otp` literal is lost — see
   §1.6.
5. **The dump's text column is a quoted repr**, and `(\S+)` cannot capture `" "`.
6. **Windows console encoding.** cp1252 stdout cannot encode a legitimate
   non-ASCII literal and raised `UnicodeEncodeError` mid-run. Streams are now
   explicitly reconfigured to UTF-8. This is the same class as
   `GUARD-encoding-and-archive-traps.md` rules 1–2: never let the console decide.

### 1.5 What D1 removes, measured

Whole `.text` (`0x00612cc0`–`0x01bd46f8`), `--window 12`:

| mode | accepted literal candidates |
|---|---|
| `--allow-rw` (D1 off) | 44,824 |
| D1 on (default) | **44,789** |
| removed by D1 | **35 — every one of them in `.got`** |

In the four ranges audited by `grouprankup-sellcard-bodies-2026-10-05.md` the
population is far denser, because HTTP request builders are full of
"take the address of a global" idioms:

| function (Ghidra range) | old candidates | new accepted | RW- phantoms |
|---|---|---|---|
| `RequestGroupRankUp` `0xf586e4:0xf58da0` | 13 | **11** | 3 |
| `ReqGroupRankUpCB` `0xf58da0:0xf59380` | 18 | **16** | 2 |
| `RequestSellCard` `0xf8df98:0xf8ed98` | 12 | **7** | 6 |
| `ParseSellCard` `0xf8ed98:0xf8f1ac` | 8 | **8** | 2 |
| **total** | **51** | **42** | **13 (25.5%)** |

Two honest qualifications:

* In these four ranges D1 alone does not change the *count*: with D2's corrected
  mapping the phantom bytes at those addresses start with `0x00`, so the
  `len >= 1` rule already drops them. **The reported `'X'` specifically is a D2
  artefact**; D1 is the durable guard, because it rejects the class by
  *location* rather than by luck in the byte values. The 35 library-wide `.got`
  hits in §2 *do* survive the byte test, which is exactly why D1 is needed.
* These 13 are **not** necessarily compiler noise. Several are the documented
  idiom of taking the address of a global for a callback/context
  (`grouprankup-sellcard-bodies` §1.1 notes `this` is stored into `sp+0xb0`
  "beside a global pointer"). They are code, and the tool should not report them
  as field names.

### 1.6 Independent corroboration

`grouprankup-sellcard-bodies-2026-10-05.md` publishes per-function field tables
that were derived by hand from `llvm-objdump`. Re-deriving them with the new tool
reproduces them exactly:

| function | report's table | new tool | agreement |
|---|---|---|---|
| `RequestGroupRankUp` §1.1 | 11 rows | 11 | exact, incl. `otp` at load site `0x00f587ba` and `price` (not in the prior candidate list at all) |
| `ReqGroupRankUpCB` §1.2 | 16 literal sites | 16 | exact |
| `RequestSellCard` §1.3 | 7 | 7 | exact |
| `ParseSellCard` §1.4 | 8 | 8 | exact |

The `otp` case is the informative one. It is at **gap 6**, with a 32-bit
`add.w` between the load and its `add`:

```
0x00f487ba  49bc          ldr   r1, [pc, #0x2f0]
0x00f487bc  f104 0060     add.w r0, r4, #0x60      ; 32-bit, NOT a branch
0x00f487c0  4479          add   r1, pc
```

The old tool misses it for **two independent reasons** — D5 (gap 6 > 4) and the
hw1-only branch test (defect 4 above). Recovering it is an independent check that
two separate fixes are both correct.

### 1.7 Self-test: before and after

| | before (`tools/resolve-literals-offline.py`) | after (`resolve-literals-segment-aware.py`) |
|---|---|---|
| built-in assertions | **0** | **23** |
| ground-truth files used | none (no gate exists) | **both** — `ghidra-wave-keys.txt` (7) and `ghidra-gem-inventory-keys.txt` (13) |
| positive re-derivations | 0 | **20**, each requiring the recomputed **target address** *and* the **string** to equal the dump |
| dump-integrity assertions | 0 | **2** (the files must still yield exactly 7 and 13 sites) |
| known-false-positive guard | 0 | **1** (the `'X'` site must be rejected, with its reason) |
| `--expect` | accepted, asserts nothing (`NOTE: …`) | replaced by a real gate |
| gate behaviour | n/a | any mismatch ⇒ **exit 3**, nothing else printed; runs automatically before `--function`/`--from-dump` unless `--skip-self-test` |
| structural recall vs ground truth | 15/20 = 75% | **20/20 = 100%** |

The 23 assertions are **derived from the two files at run time**, not hand-typed.
An earlier draft embedded a hand-transcribed address table and failed 21/21 —
three of my own addresses were wrong by a hex digit (`0x00a5ffca` − 0x10000 is
`0x00a4ffca`, not `0x0094ffca`). Deriving the table from the files removes that
whole failure mode and makes the test track the ground truth instead of my
typing.

**The gate was proved non-vacuous by fault injection** (each case applied to a
real dump, then the file was restored byte-identical):

| injected fault | result |
|---|---|
| baseline, unmodified | exit 0 **PASS** |
| `"_id"` → `"_iD"` | exit 3 **ABORTED** — `string '_id', dump says '_iD'` |
| target `0x1d76bd1` → `0x1d76bd0` (one byte) | exit 3 **ABORTED** — `target 0x1d66bd1, dump says 0x1d66bd0` |
| one resolution line deleted | exit 3 **ABORTED** — `expected 7 sites, found 6` |
| a section header removed | exit 0 PASS — correct: headers are not resolution lines |

**Validation status.**

* **VALIDATED** for this library against the two known-good dumps: 20/20
  targets and strings byte-identical, gate proven non-vacuous, and the four
  hand-derived field tables of §1.6 reproduced exactly.
* **NOT PROVED** — the segment rule as a general property. "PF_W clear" is a
  filter that happens to be correct here because all 20 known literals are in
  `.rodata`. It is **not** shown that a writable segment can never hold a real
  string in this binary, and it is not a semantic argument at all. `--allow-rw`
  exists so this can be re-measured rather than argued about.
* **NOT PROVED** — completeness. 100% recall against 20 known sites is not proof
  that no site is missed. In particular the backward walk `break`s at the first
  load-shaped instruction in the window, so a site whose load is preceded by
  another PC-relative load within `window` can still be skipped. No such case is
  known; none was looked for beyond the 20.
* **NOT PROVED** — Thumb-2 `LDR (literal)` variants beyond T1/T2 (`ldrd`/`ldr.d`
  forms, and the `LDR.W` variants with a literal-pool write-back), and no
  non-Ghidra-bias library.

### 1.8 Using it

```powershell
# the gate, on its own
python analysis/research/base-stats-visual-hunt/resolve-literals-segment-aware.py --self-test

# PT_LOAD + section table (the material behind the segment rule)
python analysis/research/base-stats-visual-hunt/resolve-literals-segment-aware.py --list-segments

# a function range; addresses are GHIDRA by default, like every dump in analysis/
python analysis/research/base-stats-visual-hunt/resolve-literals-segment-aware.py `
    --function 0xf586e4:0xf58da0

# ...or ELF
python analysis/research/base-stats-visual-hunt/resolve-literals-segment-aware.py `
    --function 0xf486e4:0xf48da0 --addr-convention elf

# replay a dump, expecting an exact match (exit 4 on any difference)
python analysis/research/base-stats-visual-hunt/resolve-literals-segment-aware.py `
    --from-dump analysis/ghidra-wave-keys.txt

# measure what the segment rule is hiding -- DIAGNOSTIC ONLY
python analysis/research/base-stats-visual-hunt/resolve-literals-segment-aware.py `
    --function 0x612cc0:0x1bd46f8 --allow-rw
```

Exit codes: `0` ok · `2` usage/IO · `3` self-test failure · `4` nothing resolved
or a dump mismatch.

---

## 2. UNPURE — literal-looking things that are data or code

**Caution list only.** Nothing here is a hero, accessory or monster statistic, and
nothing counts toward any 70% threshold. These are the outputs that look like
field names and are not. They are recorded because the failure mode is silent and
expensive: a field name invented here becomes a server response key the client
never asked for (AGENTS.md §16.7 — "it sends a real client a response keyed on a
field that does not exist").

### 2.1 The `.got` address-of-a-global class (35 sites, all rejected by D1)

Every one of the 35 library-wide D1 rejections is in `.got`
(`0x021aafe4`–`0x021b3000`), and each is a **relocated code pointer**, not a
string. With `--allow-rw` the tool reports them as 1–2 character "strings",
because the pointer bytes terminate early:

| target ELF (sample) | what `--allow-rw` prints | reality |
|---|---|---|
| `0x021ab052` | `'l'` | GOT pointer |
| `0x021ab6e2` | `'t'` | GOT pointer |
| `0x021ab8ce` | `'x'` | GOT pointer |
| `0x021abd02` | `'~'` | GOT pointer |
| `0x021ab884` | `'MWw'` | GOT pointer pair |
| `0x021ad548` | `'Eͬ'` | GOT pointer |
| `0x021ad704` | `'1۱'` | GOT pointer |
| `0x021ad760` | `'uƲ'` | GOT pointer |
| `0x021aebb4` | (byte test rejects it; D1 rejects it too) | the documented `'X'` site; `.got` slot holding `0x00f48da1`, `0x01e7a185`. ELF VA `0x021aebb4` → file offset `0x021adbb4`. ⚠️ was printed `0x021bebb4` here — that was the old tool's Ghidra-mixed output, not an ELF VA (corrected 2026-10-05) |
| `0x021aed38` | (byte test rejects it; D1 rejects it too) | second `4838 9905 4478` site, ELF `0x00f77bfe` |

Two of these are worth naming because they are **valid UTF-8 by accident** —
`'كr'`, `'Yı'`, `'1۱'`, `'uƲ'`. A UTF-8 decoder accepts them happily. Only the
segment check rejects them. **This is the concrete reason the rule is stated as a
segment test and not as a decodability test.**

Two addresses in this class are *already known to be meaningful code*: the
`UpgradeCB` `.got` function pointer at Ghidra `0x021ada74`
(`gem-popup-bindings-2026-10-05.md` §1.2) and the `std::bind` machinery around
it. Do not treat anything the resolver prints from `.got` as a key.

### 2.2 Real literals in `.rodata` that are still not field names

D1 cannot catch these and neither can any byte test. From a whole-`.text` scan,
27,225 of 44,789 accepted hits look like identifiers, routes or symbols
(`[A-Za-z_0-9/:.-]{2,}`), which is the expected shape — but that heuristic also
admits non-keys:

| example | note |
|---|---|
| `ELF 0x00c30f70 -> 0x01d70f77 '???'` | a genuine `.rodata` string whose content is three non-ASCII bytes. **Real literal, not a field name.** |
| `'alpha'`, `'rot'`, `'scale'` (per `gem-popup-bindings` §1.7) | CMShader render parameters, not server fields |
| `'upgrade_event'`, `'init'` (per `gem-popup-bindings` §1.5) | animation identifiers; `upgrade_event` is used as *prefix + 8 chars* |
| `GEM_NAME1`, `UI_SB_TX_ME`, `BTN_UPGRADE` | UI node names, not JSON keys |
| Korean literals (`gem-popup-bindings` §1.6) | shipped KO locale UI text — **not** decoded here, referenced by address only |
| `/gym/RankUpBundle`, `/gem/LevelUp`, `/shop/SellCard` | **routes**, i.e. request paths, not response fields |

**Rule of thumb this section exists to enforce: a resolved literal is a
*candidate*, and the consumer still has to be traced.** `gem-popup-bindings`
§1.0's own lesson applies — `OnInit` was only trustworthy once its resolved
`GetLocalizedText`/`FindCastByName` callsites were seen. A literal with no traced
consumer is not yet a field.

### 2.3 Numeric tokens touched by this pass (all structural, none economic)

Per the output rule, recorded here rather than in `polluted-observations.md`
(this run does not append to it).

| Token | Value | Where | What it is |
|---|---|---|---|
| literal-pool alignment | `0x3` | slot formula | ARM PC alignment; not data |
| T2 immediate field width | `0xf` bits | `decode_ldr_pc_imm` | encoding |
| BL/BLX hw2 mask | `0xD000` | `is_32bit_branch` | encoding |
| addend | `add_elf + 4` | Thumb PC rule | encoding |
| Ghidra bias | `0x10000` | convention | toolchain, not game data |
| segment 1 VA→offset delta | `0x1000` | PT_LOAD | linker layout |
| library size | 35,445,748 | file | build artifact |

None of these is a balance, stat or economy value. **Do not promote any row above
into a server default.**

---

## 3. Files, and what a follow-up should do

**Written this run (2 files, both in this folder):**

* `resolve-literals-segment-aware.py` — the resolver.
* `resolver-hardening-2026-10-05.md` — this file.

**Not touched:** `tools/resolve-literals-offline.py` (left intact so the old and
new can be compared — §1.5's table is reproducible only while both exist);
`polluted-observations.md` (parent mirrors); `analysis/systems/gym.md` and
`analysis/research/grouprankup-sellcard-bodies-2026-10-05.md` (read-only brief —
their corrections are §1.1's convention finding and §1.4/D5's `otp` cause).

The original `libnative_core.so` was read-only throughout and is unmodified. The
Ghidra project was never opened. Helper scripts for this pass lived in the OS
temp directory.

**Next, in order:**

1. **Fix the `.rodata` convention note** in
   `grouprankup-sellcard-bodies-2026-10-05.md` §"Address convention" — its
   literal columns are Ghidra, not ELF (§1.1). Every address in that file should
   be re-labelled before it is cited again.
2. **Retire `tools/resolve-literals-offline.py`.** Its `--from-dump` and
   `--find-string` modes (D6) have no filter at all, which is the most dangerous
   property in the file. Until then, do not use it for anything outside
   segment 0.
3. **Close the `break`-at-first-load recall gap** in `scan()`. Walk every
   load-shaped candidate in the window instead of stopping at the first, and let
   D1 arbitrate. Expect the whole-`.text` count to rise; re-measure §1.5's
   phantom rate before trusting the extra hits.
4. **Decide whether the segment rule stays a heuristic.** A cleaner criterion
   would be "the target is inside `.rodata`", which is checkable and stricter.
   It would need its own ground truth, because it is a *narrowing*, and per §1.7
   a narrowing needs evidence rather than taste.
5. **Fix or document `--expect`** in the old tool, or delete it. A flag that
   looks like an assertion and asserts nothing will be trusted by the next agent.