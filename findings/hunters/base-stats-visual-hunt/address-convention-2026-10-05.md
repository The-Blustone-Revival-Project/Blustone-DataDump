# Address conventions — definitive table and corpus audit (2026-10-05)

**Lane:** close the systemic address-convention defect flagged by
[`resolver-hardening-2026-10-05.md`](resolver-hardening-2026-10-05.md) §1.1/D2 and
the `+0x10000` bias found in
[`point-info-type-2026-10-05.md`](point-info-type-2026-10-05.md) §1.1, and settle
the two tables `analysis/native-all-strings.tsv` and
`analysis/native-evidence.tsv` **empirically** from the ELF32 program headers of
`analysis/extracted/lib/armeabi-v7a/libnative_core.so` (35 445 748 bytes).

**Status: MEASURED, not assumed, and now 100 % on the string tables.** Every
convention claim below is decided by byte lookup against the library itself, with
the population size stated. Eleven claims in this folder were **wrong** and are
corrected in place; five more are **ambiguous** and are listed.

> **Second pass, 2026-10-05 (this revision).** The first pass left three open
> items. All three are now closed, and two of them turned out to be *false
> statements* rather than gaps:
>
> 1. The "1205 rows match under no interpretation — residual escape-encoding
>    artefacts" limit is **retracted**. Those rows are the `R_ARM_RELATIVE`
>    bias. With relocations applied, `native-all-strings.tsv` verifies
>    **515 576 / 515 576 = 100.0000 %** and `native-evidence.tsv`'s
>    `[RAW_PRINTABLE_STRINGS]` **8 642 / 8 642 = 100.0000 %**. There is no
>    unexplained row left in either string table. (§3, §8.2)
> 2. `point-info-type-2026-10-05.md` §1.9's *"zero `R_ARM_RELATIVE` entries"*
>    is **false** — there are **128 620** of them. Corrected at source and
>    retracted here. (§5, §6.1 item 8)
> 3. `llvm-objdump`'s ARM-not-Thumb behaviour is **reproduced and characterised**,
>    and it turns out to matter for a different reason than reported: its address
>    *labels* are ELF VAs, which is exactly what kept the original defect alive.
>    (§4b)
>
> The independent second-pass measurements also corrected three figures the first
> pass got wrong (segment-1 discriminator, the `.dynsym` name split, and the
> import count) and one off-by-one line citation that had propagated into two
> files. All are itemised in §6.1 item 10 — this file's own errors are listed
> alongside everyone else's.

**Read-only compliance.** No Ghidra project opened. The library was opened
read-only and is unmodified. **No** `server-ts`, fixture, APK, seed, LevelDB,
emulator, VM or phone action. **`polluted-observations.md` was not appended to and
not edited** (it is the one file in this folder carrying Hangul bulk and no
convention claim — see §6). Encoding guard per
[`GUARD-encoding-and-archive-traps.md`](GUARD-encoding-and-archive-traps.md): every
edited file re-verified as **U+FFFD = 0** with **Hangul and CJK counts byte-identical
to their pre-edit values**, LF-only line endings preserved. All file I/O went
through the `edit`/`write` tools and Python; **no PowerShell `Get-Content` /
`Set-Content` / `WriteAllLines` touched any workspace file** — the exact failure
that guard exists to prevent.

**Two new files ship with this report** (both read-only, both in this folder):

| file | what it is |
|---|---|
| `verify-address-conventions.py` | Standard-library-only reproduction of **every number below**, straight from the ELF and the two TSVs, with `assert` on each count. `python verify-address-conventions.py` re-derives the whole table; `--full` also reproduces the §4b objdump evidence. **It reads and writes nothing.** It exists because §6.1 item 10(b) is a bug this report itself shipped: a hand-written table transposed two columns and no review caught it. |
| `enc-guard.py` | The encoding guard as an executable check — U+FFFD count, Hangul / CJK / non-ASCII counts, CR/CRLF/LF counts, BOM and final-newline, plus a stored baseline. `python enc-guard.py baseline <files…>` then `python enc-guard.py check <files…>`. Hangul/CJK/CR counts are **hard** invariants (any change fails); size/char counts are reported but not fatal, since an intentional edit changes them. |

**Coverage unchanged** and irrelevant to this pass: heroes **1/113**,
accessories **1/100**, monsters **0/22**. Nothing here is a hero, accessory or
monster statistic.

---

## 1. THE DEFINITIVE TABLE

> **One rule: `analysis/native-all-strings.tsv` and `analysis/native-evidence.tsv`
> are both in the Ghidra/IDA *image* address space, `IMAGE_BASE 0x10000` + ELF VA.
> `libnative_core.so` itself is mapped at ELF VA 0. Therefore every 8-hex token in
> those two tables must have `0x10000` subtracted to become an ELF VA. And an ELF
> VA becomes a file offset only through the program headers — a uniform `− 0x10000`
> is correct for `.text`/`.rodata`/`.dynstr` and WRONG for the second `PT_LOAD`.**
>
> **Verified exhaustively, both directions.** Applying that rule to
> `native-all-strings.tsv` reproduces **515 576 / 515 576 = 100.0000 %** of its
> printed strings byte-for-byte, and the plain-ELF reading matches **0 / 1763** of
> the rows that discriminate it. Reproduce with
> `python verify-address-conventions.py` (standard library only, read-only).

| # | table | column | convention | how to get the ELF VA | how to read the bytes |
|---|---|---|---|---|---|
| **C1** | `analysis/native-evidence.tsv` | `[FUNCTIONS]` col 1 | **Ghidra image addr** = ELF VA + `0x10000` (the file declares it: line 2 `IMAGE_BASE 00010000`) | subtract `0x10000` | `va − 0x10000` in seg 0; `(va − 0x10000) − 0x1000` in seg 1 |
| **C2** | `analysis/native-evidence.tsv` | `[FUNCTIONS]` col 3 `undefined` | **NOT A CONVENTION — A BROKEN COLUMN.** Do not use it as evidence | — | — (§4) |
| **C3** | `analysis/native-all-strings.tsv` | plain 8-hex col 1 (515 576 rows) | **Ghidra image addr** = ELF VA + `0x10000` | subtract `0x10000` | `va − 0x10000` in seg 0; `(va − 0x10000) − 0x1000` in seg 1 |
| **C4** | `analysis/native-all-strings.tsv` (36 rows) and `analysis/native-evidence.tsv` (6 rows) | `<section>::<hex>` rows | **SECTION-RELATIVE byte offset**, *not* an image address and *not* a whole-file offset | n/a — add `sh_offset` of the named section | `sh_offset + off` |
| **C5** | any hand-derived ELF VA quoted in these reports | — | **ELF VA** (this is the only "native" space; equal to file offset **only** inside seg 0) | — | program headers, never a uniform bias |
| **C6** | `analysis/ghidra-*.txt` dumps (`ldr@`, `slot=`, `add@`, `->`) | — | **Ghidra image addr** | subtract `0x10000` | as C1 |
| **C7** | `BLUSTONE_ARM` logs, and `AGENTS.md` §16.7 lesson 3 | — | **ELF VA** (`BLUSTONE_ARM`) — Ghidra = ELF + `0x10000` | — | — |
| **C8** | **32-bit words read out of writable data** (`.got`, `.data*`, `.init_array`) | — | **RELOCATED** — the on-disk value **plus the `0x10000` image base** | — | segment 1 only, and only for the **128 620** `R_ARM_RELATIVE` words. `.rodata`/`.text`/`.dynstr`/`.plt` have **zero** (§5) |
| — | *local fixture space* (`local_ap`, `local_search_017`, …) | — | **not an address at all** | — | — |

**The whole rule in three lines of arithmetic (plus one word-level term):**

```
elf_va   = token − 0x10000                       # C1 / C3
file_off = elf_va                    if elf_va <  0x0210d320   # seg 0: p_offset == p_vaddr
file_off = elf_va − 0x1000           if elf_va >= 0x0210e550   # seg 1: p_offset == p_vaddr − 0x1000

# segment 1 ONLY, and only inside a word listed in .rel.dyn as R_ARM_RELATIVE (C8):
word     = LE32(elf_va − 0x1000) + 0x10000
```

**Measured confidence.** Seg-0 lines: **100.0000 %** (515 576 / 515 576 string rows).
Seg-1 lines: **100.0000 %** **with** the C8 relocation term (**1763 / 1763**);
**0.2 %** without it (the whole-file 1157-row gap is entirely relocated words — §3).

---

## 2. PURE — the program headers that make a uniform bias impossible

Reproduce with `analysis/research/base-stats-visual-hunt/resolve-literals-segment-aware.py
--list-segments`, or read with `struct.unpack_from('<8I', data, e_phoff + i*32)`.
Read from the ELF32 header: `e_phoff = 0x34`, `e_phentsize = 32`, `e_phnum = 8`,
`e_shoff = 0x21cd744`, `e_shnum = 30`.

```
idx type           p_offset   p_vaddr    p_filesz   p_memsz    flags  vaddr−offset
 1  PT_LOAD  R-X   0x00000000 0x00000000 0x0210d320 0x0210d320  XR          0x0
 2  PT_LOAD  RW-   0x0210d550 0x0210e550 0x000bfe6c 0x007ae240  WR       0x1000
 3  PT_DYNAMIC     0x021a9e90 0x021aae90 0x00000150            WR       0x1000
 6  PT_ARM_EXIDX R 0x01bd46f8 0x01bd46f8 0x00058528            R           0x0
 7  PT_GNU_RELRO   0x0210d550 0x0210e550 0x000a4ab0            WR       0x1000
```

**Segment 0 covers `VA 0x00000000..0x0210d320`. Segment 1 covers
`VA 0x0210e550..0x028bc790` but only `file 0x0210d550..0x021cd3bc`.** The
`0x1230`-byte gap `0x0210d320..0x0210e550` is unmapped padding, and `0x21cd3bc` is
where the *file* ends for `PT_LOAD` purposes.

The sections that matter (section headers, read via `sh_offset` — note
`.shstrtab` is non-alloc so its `sh_addr` is `0` and only `sh_offset = 0x021cd604`
is usable):

| section | ELF VA (= file offset) | size | segment | relevant? |
|---|---|---|---|---|
| `.text` | `0x00612cc0` | `0x015c1a38` | R-X | literal-pool **slots** live here |
| `.ARM.exidx` | `0x01bd46f8` | `0x00058528` | R-X | no |
| `.ARM.extab` | `0x01c2cc20` | `0x00125d08` | R-X | no |
| **`.rodata`** | **`0x01d52940`** | `0x003ba754` | R-X | **every literal in this folder** |
| `CryptoPP_Align16` | `0x0210d0a0` | `0x00000280` | R-X | no |
| `.data.rel.ro.local` | `0x0210e550` | `0x000263e0` | RW- | **first `p_offset ≠ p_vaddr` byte** |
| `.data.rel.ro` | `0x02134930` | `0x00075f24` | RW- | " |
| **`.got`** | **`0x021aafe4`** | `0x0000801c` | RW- | where the phantom class lives |
| `.data` | `0x021b3000` | `0x0001b3bc` | RW- | " |
| `.bss` | `0x021ce3c0` | `0x006ee3d0` | RW- (**no file bytes**) | " |

**D2 confirmed, and it is a two-line arithmetic fact:** `file_offset == VA` holds
for segment 0 only. For segment 1 the delta is `0x1000`, so a uniform
`addr − 0x10000` file mapping reads every `.got`/`.data` word **0x1000 bytes too
low**. Measured below.

---

## 3. PURE — proof that `native-all-strings.tsv` is **Ghidra**, not file order

Method: split the file on `LF`, strip exactly one trailing `CR` (the file is
CRLF-terminated — **515 612 of 515 613** lines end in `CR`; the `CR` is *not* part
of the string), then look up the printed bytes at the candidate file offset of a
**relocated** image (see the ⚠️ below; the earlier claim that the producer
escapes bytes was itself wrong and is retracted).

| hypothesis for the plain 8-hex column | rows matching (raw file) | rows matching (relocated image) |
|---|---|---|
| file offset = `token − 0x10000` (uniform, seg-0 style) | 513 817 / 515 576 = 99.659 % | 513 817 / 515 576 = 99.659 % |
| **file offset = program-header mapping of `token − 0x10000`** | 514 419 / 515 576 = 99.776 % | **515 576 / 515 576 = 100.0000 %** |
| file offset = `token − 0x10000 − 0x1000` (i.e. always subtract 0x1000) | 0 | 0 |
| file offset = `token` as-is, i.e. already an offset | 526 / 515 576 = 0.102 % (coincidence) | 526 / 515 576 = 0.102 % (coincidence) |
| **no interpretation matches** | **1157 (0.224 %)** | **0** |

The 526 `token`-as-offset hits are **coincidences**, not evidence: they are the
rows whose short (2–4 byte) string happens to occur at both `token` and
`token − 0x10000`. On the segment-1 subpopulation that coincidence rate drops to
**0 / 1763**, which is exactly why that subpopulation is the right discriminator
and this whole-file tally is not.

**⚠️ RESIDUAL RESOLVED — this retires the "escape-encoding" limit of the
earlier draft of this file.** The 1157 unmatched rows were **never** an escaping
artefact. They are all in the **writable** segment, and every single byte
difference is exactly **`+1` on one byte** of a 4-byte word:

```
line 513816  token 0211f7b0  ELF VA 0210f7b0  file 0x210e7b0  sec .data.rel.ro.local
   TSV string : b' 5$'          (0x24 0x35 0x20 0x24)
   raw  file  : b' 5#'          (0x23 0x35 0x20 0x23)
   as LE32    : file 0x01403264  ->  TSV 0x01413264     delta = +0x10000
```

The low 16 bits never carry, so adding the image base changes **only byte 2**,
which is why the difference reads as a single `+1` rather than as a shifted
pointer. The cause is that **the producer dumped a relocated image, not the
on-disk file.** Parsing `.rel.dyn` (`.dynamic` `DT_REL` @ `0x515a10`,
`DT_RELSZ` = `0xfb4c8`, `DT_RELENT` = 8 → 128 665 entries) plus `.rel.plt`
(379) gives **128 620 `R_ARM_RELATIVE`** (`r_info & 0xff == 23`), 32
`R_ARM_GLOB_DAT`, 13 `R_ARM_ABS32`, 379 `R_ARM_JUMP_SLOT`, and **zero**
`R_ARM_NONE`. Applying those 128 620 `R_ARM_RELATIVE` relocations with bias
`0x10000` to the segment-1 words takes the match rate to **100.0000 %**.

This is **independent corroboration of the `0x10000` image base from a second
direction**: the token column is not merely "offset by `0x10000` from the
on-disk file", it *is* the relocated address space. It also falsifies
`point-info-type-2026-10-05.md` §1.9's old "there are no `R_ARM_RELATIVE`
entries at all … 128,620 `R_ARM_NONE`" bullet — see that file, corrected in
place, and §5 below.

| mapping tried | rows matching | rows it LOSES |
|---|---|---|
| `(token − 0x10000) − 0x1000` — **correct `PT_LOAD` mapping** | **1763 / 1763 = 100 %** | **0** |
| `token − 0x10000` — i.e. the token is already the file offset | **4 / 1763** | **1759** |
| token as-is, plain-ELF reading, seg-aware file map | **0 / 1763** | **1763** |
| token as-is, plain-ELF reading, seg-0 identity | **0 / 1763** | **1763** |

**1763 vs 4** cannot both be true of a file-offset column, and **0 / 1763** rules
out the plain-ELF reading outright — not merely weakens it, it eliminates it.
Therefore **the column is a virtual (image) address, and the file offset requires
the program headers.** This is the whole of D2, settled empirically.

> ⚠️ **A transposition error in this report, caught by the reproduction
> script** (`verify-address-conventions.py` asserts these exact counts). Two
> successive drafts of this table read the correct mapping as `1759 / 1763`.
> **That number is the count the _uniform_ map _loses_, not the count the
> _correct_ map _matches_.** The correct map matches **1763 / 1763**. Keep the two
> columns in this table separate — they are the same digit set in a different
> role, which is precisely the sort of slip this report exists to catch. Note
> also that an even earlier draft read `606 vs 0`; that was measured against the
> **raw** file, before the relocation term of §3 was applied, and is simply a
> different (weaker, and now superseded) measurement. The discriminator itself has
> been stable across all three.

Ancillary facts, all measured:

- **0** of the 515 576 tokens have `token − 0x10000` outside every `PT_LOAD` VA
  range — so the column is uniformly an address, with no junk tail.
- Only **23.8 %** (122 613) of tokens are 4-aligned and **39.5 %** (203 450) are
  2-aligned. A *code* address column would be ~100 % 2-aligned at worst and would
  be concentrated in `.text`; this column is byte-granular, i.e. it indexes
  *strings*, wherever they sit.
- The largest token, `0x021dda4b`, exceeds the **file** size `0x021cdbf4` — which
  is itself proof it is not a file offset, while `0x021cda4b` is a legal segment-1
  VA (`0x021cda4b < 0x021ce3bc`, the end of segment 1's `p_filesz`).
- Named spot proofs (each printed byte run reproduces the TSV string exactly;
  all five are in the R-X segment, so the raw file suffices):

| TSV token | line | token − 0x10000 | bytes there |
|---|---|---|---|
| `002a6244` | **25258** | `0x00296244` | `_ZN18CSRPopUpGemLevelUp11SetBaseInfoERKNSt6__n` |
| `0024dea0` | 21699 | `0x0023dea0` | `_ZN6CSRGem17RequestGemLevelUpEyjRKNSt6__n` |
| `01d79394` | — | `0x01d69394` | `/gvg/GetRef\x00/gvg/GetRegister` |
| `01d7985b` | — | `0x01d6985b` | `point_id\x00multi\x00%s RefID Is n` |
| `003600f0` | — | `0x003500f0` | `_ZN10CSRSyncRef11ReqGVGRefCB` (a `.dynstr` name) |

  ⚠️ **Off-by-one corrected.** The earlier draft of this table, and
  `gem-popup-bindings-2026-10-05.md` §1.0, both cited `002a6244` as line
  **25257**. It is line **25258**; 25257 is `002a621d
  _ZN18CSRPopUpGemLevelUp11AnvilheatedEi`. Both files are corrected in place.
  `0x003500f0` is inside `.dynstr` (`0x000c4f20`–`0x0044af44`), which confirms
  the `gvg-reference-2026-10-05.md` finding that `0x003600f0` indexes a *mangled
  name string* and is not a code address.

`002a6244` is **the example `gem-popup-bindings-2026-10-05.md` called "not an
address"**. It is an address — of a `.dynstr` symbol name, in Ghidra space.

### 3a. The `<section>::<offset>` rows are a *third* convention

`native-all-strings.tsv` ends with **36** such rows and `native-evidence.tsv` with
**6**; the two sets are **not** identical (`native-evidence.tsv` carries only 3
`.shstrtab` + 2 `.comment` + 1 `.note.gnu.gold-version` entries, i.e. it was
truncated). They are **section-relative byte offsets**, and are neither image
addresses nor whole-file offsets. Six spot checks, all byte-exact:

| row | section `sh_offset` | computed file offset | bytes |
|---|---|---|---|
| `.shstrtab::00000116` | `0x021cd604` | `0x021cd71a` | `.shstrtab` |
| `.shstrtab::00000024` | `0x021cd604` | `0x021cd628` | `.text` |
| `.comment::00000001` | `0x021cd3bc` | `0x021cd3bd` | `Android` |
| `.comment::000001e5` | `0x021cd3bc` | `0x021cd5a1` | `GCC: (GNU) 4.8` |
| `.note.gnu.gold-version::00000010` | `0x021cd5b0` | `0x021cd5c0` | `gold 1.12` |
| `.ARM.attributes::00000011` | `0x021cd5cc` | `0x021cd5dd` | `ARM v7` |

Row **C4** therefore needs its own rule, and mixing it with C1/C3 is a third
distinct error class.

---

## 4. PURE — `native-evidence.tsv`: convention is self-declared, the third column is broken

**The convention is not inferred — the file states it.** Line 1
`PROGRAM	libnative_core.so`, line 2 `IMAGE_BASE	00010000`. That is the only
address-space declaration anywhere in either table, and it is the correct one.

Checked exhaustively against the ELF's own `.dynsym`, parsed directly from the
file with `struct` (no external tool): **50 387** `.dynsym` entries, of which
**392** are `SHN_UNDEF` imports and **49 995** are defined (37 457 `STT_FUNC`,
12 535 `STT_OBJECT`, 3 `STT_NOTYPE`); **49 995 distinct defined names**.

> ⚠️ **A Thumb bit must be masked, or the test silently fails.**
> `st_value` for a Thumb function has **bit 0 set**; Ghidra stores the *instruction*
> address, so the identity is `token == (st_value & ~1) + 0x10000`. Omitting the
> `& ~1` drops every Thumb symbol and reports ~24 % instead of 90 %. This is the
> same failure mode as `gem-popup-bindings-2026-10-05.md` §1.0 defect 1 (a
> self-test pasted in the wrong coordinates). Getting it right, the exhaustive
> classification of all 40 290 `[FUNCTIONS]` rows is:

| classification of the `[FUNCTIONS]` address column | rows | share |
|---|---|---|
| **`token == (st_value & ~1) + 0x10000`** — exact two-way name+address agreement | **36 467** | **90.51 %** |
| name not in `.dynsym` at all — Ghidra/linker-synthesized | 2 800 | 6.95 % |
| name **is** in `.dynsym` but `SHN_UNDEF` (`st_value == 0`, unmatchable) | 735 | 1.82 % |
| name in `.dynsym`, defined, but address differs | 288 | 0.71 % |

So **C1 is proven twice over**: once by the file's own `IMAGE_BASE`, once by
**36 467 exact two-way name+address agreements and zero counterexamples** for the
plain-ELF hypothesis.

**Correction to the earlier draft of this table.** It read "name not a
`.dynsym` name at all | 3 535". That conflated two different things under one
label: only **2 800** rows have a name absent from `.dynsym`; the other **735** are
*genuine `.dynsym` names* that are simply imports with `st_value == 0` and
therefore cannot be matched on address. **3 535 is the correct total of the two**,
but "not a `.dynsym` name at all" was the wrong description of 735 of them, and
that mislabel is exactly what makes an import row look like a convention
violation. The 2 800 break down, as measured by `verify-address-conventions.py`:

| of the 2 800 | rows | what it is |
|---|---|---|
| `FUN_*` / `thunk_FUN_*` / `loc_*` | **2 401** | Ghidra-synthesized code objects |
| `_INIT_*` | **397** | derived from `.init_array` (`R_ARM_RELATIVE` targets it 397 times — the two figures agree exactly) |
| `_FINI_0`, `_FINI_1` | **2** | linker-synthesized; **not** in `.dynsym` and **not** `FUN_*` — a category of its own, and the reason a naive "`FUN_*`-prefix" test reports "unknown" |

**A third, fully self-contained proof needs no external tool at all.** Ghidra
names its own synthesized functions `FUN_<address>`, and in this table **the name
and the address column agree 2363 / 2363 = 100.00 % of the time**
(`FUN_0062b1ac` ↔ `0062b1ac`). The `thunk_FUN_*` names likewise embed Ghidra
addresses. So the file *states* its own coordinate space three times over:
`IMAGE_BASE 00010000`, the `FUN_*` names, and the dynsym agreement.

### 4a. Two populations in `[FUNCTIONS]` that are **not file-backed at all**

Worth stating because a reader who mechanically applies `−0x10000` and then
seeks a file offset will fail on them:

| population | rows | address space |
|---|---|---|
| Ghidra **EXTERNAL** block — imports (`readdir`, `__cxa_atexit`, `pthread_cond_broadcast`, `glClear`, `slCreateEngine`, …) | **385** | Ghidra `0x028cd000`–`0x028cd618`, contiguous, 4-byte slots. `−0x10000` gives `0x028bd000`–`0x028bd618`, which is **past the end of `.bss`** (`0x028bc790`) and past `PT_LOAD` 2's `p_memsz`. **No file bytes exist at these addresses at all.** |
| `.plt` thunks for undefined imports | **263** | real; `−0x10000` lands inside `.plt` (`0x00611ab0`–`0x00612c88`), e.g. `__cxa_atexit` @ Ghidra `0x00621ad0` → ELF `0x00611ad0` |
| undefined-import rows whose address Ghidra placed in `.text` | **87** | real |

263 + 87 + 385 = **735**, the full undefined-import population. Note that the
same import name appears in **both** the EXTERNAL block and `.plt`; only the
`.plt` copy has file backing.

**Row C2 — the `undefined` column is not evidence.** All **40 290** rows carry the
literal tag `undefined` (measured: 40 290 / 40 290). The `.dynsym` truth:

| classification of the name | rows | share |
|---|---|---|
| **defined dynamic symbol** | **36 755** | **91.2 %** |
| Ghidra-synthesized, no `.dynsym` counterpart (`FUN_*`, `SUB_*`, `SUP_*`, `loc_*`, `switch*`, `thunk_FUN_*`, `_FINI_*`) | 2 800 | 6.9 % |
| `_INIT_*` pseudo-symbol (INIT_ARRAY-derived, inside the 2 800) | (397) | (1.0 %) |
| genuine libc/libc++ import (`SHN_UNDEF`): `strlen`, `pthread_create`, `__cxa_atexit`, `memcpy`, … | **735** | 1.8 % |

**Only the last 735 rows deserve the tag.** `point-info-type-2026-10-05.md` §1.1
found this on the single symbol `to_string<POINT_INFO_TYPE>` (`STT_FUNC` at ELF
`0x0087f9d0`, listed as `undefined` at `0x0088f9d0`) and correctly said "every row
examined in that region". It is in fact every row in the section, and the correct
mislabel rate is **91.2 %**.

**Correction to the earlier draft of this table**, which gave the import count as
**775**. The measured figure is **735**. The 40-row difference is the
`thunk_FUN_*` / `_FINI_*` bucket, which is Ghidra-synthesized and therefore not an
import at all — it belongs in the 2 800 row above, not here. Nothing else in
the section depends on the number.

### `[RAW_PRINTABLE_STRINGS]` (header at line 40294; 8 648 rows)

8 642 plain rows + 6 `<section>::` rows. Uses **C3**: all **8 642 / 8 642** plain
rows match byte-exactly under the segment-aware Ghidra mapping against the
relocated image — **100.0000 %**, same as the plain rows of
`native-all-strings.tsv`. The two files are therefore interchangeable for string
addresses, and the two string blocks can be treated as one 524 218-row table.
(The 6 `<section>::` rows are C4 — section-relative, *not* image addresses.)

### 4b. Toolchain note: `llvm-objdump` here decodes **ARM**, and labels **ELF VAs**

`gvg-reference-2026-10-05.md` reported that the NDK `llvm-objdump`
(`tools/android-sdk/ndk/29.0.14206865/toolchains/llvm/prebuilt/windows-x86_64/bin/llvm-objdump.exe`)
was unusable on this library, and that is **correct** — but the reason matters,
and it is *not* an address problem. Reproduced:

```
$ llvm-objdump -f libnative_core.so
file format elf32-littlearm
architecture: arm                      <- reports ARM, not Thumb
```

`e_flags = 0x5000200` (EABI ver 5 + float soft) carries no Thumb indication, so
the default decoder is ARM. On a **Thumb** function the output is nonsense:

```
$ llvm-objdump -d --start-address=0xbc0454 ...
  bc0454: af03b5f0   svcge  #0x3b5f0              <- garbage
  bc0458: 0b00e92d   bleq   0xbfa914 <...>         <- branch across a symbol boundary

$ llvm-objdump -d --triple=thumbv7-linux-gnueabihf --start-address=0xbc0454 ...
  bc0454: b5f0       push  {r4, r5, r6, r7, lr}  <- correct
  bc0456: af03       add   r7, sp, #0xc
  bc0458: e92d 0b00  push.w {r8, r9, r11}
```

**Two independent conclusions, and they point in opposite directions:**

1. **Addresses from objdump are fine and are ELF VAs.** Look at the labels it
   prints: `00bc0454 <_ZN18CSRPopUpGemLevelUp11SetBaseInfoE…>` — that is the
   ELF VA, with **no** `0x10000` bias. So an agent that disassembles with objdump
   and then compares its addresses against a `native-all-strings.tsv` token will
   conclude the TSV "is ELF". **That is precisely how the original defect
   survived**, and it is why `objdump` agreement is not independent evidence for
   C1. `llvm-nm -D` (which `gvg-reference-2026-10-05.md` used) is likewise ELF VA.
   Any C1 cross-check must either subtract the bias explicitly or read the
   symbol table directly, as §4 above does.
2. **Instruction decoding needs `--triple=thumbv7-linux-gnueabihf`.** This affects
   operand semantics only, never addresses.

**This pass therefore used no external toolchain at all.** Every number in §2,
§3 and §4 comes from `struct.unpack_from` over the ELF32 header, program
headers, section headers, `.dynsym` and `.rel.*` tables, plus the raw file bytes.
`objdump` was consulted **only** to reproduce the ARM/Thumb behaviour above, and
no conclusion rests on it. That is a deliberate choice: it removes the whole
class of "tool prints ELF VA, table says Ghidra" confusions, and it makes the
result reproducible with the standard library alone.

---

## 5. PURE — the `'X'` phantom, re-derived: D2 and D3 are **independent** bugs

`resolver-hardening-2026-10-05.md` §1.4-D1/D2 attributes the phantom entirely to the
naive file mapping. Re-deriving the site from the raw pool word shows **two** faults,
and the first one is not a file-mapping fault at all.

Ground truth at ELF `0x00f489e6` (`ldr r0,[pc,#0xe0]`), with the `add` at ELF
`0x00f489ea`:

```
slot_elf   = ((0x00f489e6 & ~3) + 4 + 0xe0) & ~3 = 0x00f48ac8
pool word  = u32 at 0x00f48ac8                = 0x012661c6   (RAW, UNBIASED)
correct    = 0x012661c6 + (0x00f489ea + 4)     = 0x021aebb4   <- ELF VA, in .got
tool print = 0x012661c6 + 0x00f589ee           = 0x021bebb4   <- +0x10000 too high
```

The pool word holds a **pre-bias addend**. The old tool added its **Ghidra**
`add_pc` to a **raw** word — **defect D3, at the arithmetic step, before any file
read.**

> ⚠️ **Retraction of this report's own supporting citation.** This section
> previously justified "pre-bias addend" by citing `point-info-type-2026-10-05.md`
> §1.9 for "there are **zero** `R_ARM_RELATIVE` relocations in this binary". **That
> is false and is now corrected in place at the source.** The binary carries
> **128 620 `R_ARM_RELATIVE`** entries — the highest count seen on any binary in
> this project. `point-info-type` §1.9 had counted them correctly (128 620) and
> mislabelled the *type* as `R_ARM_NONE`.
>
> **The conclusion survives on different and stronger evidence:** a
> section-level classification of all 128 620 targets shows **0 in `.rodata`** and
> **0 in `.text`** — every one lands in a writable section (`.data.rel.ro` 103 052,
> `.data.rel.ro.local` 10 991, `.got` 7 785, `.data` 6 393, `.init_array` 397,
> `.fini_array` 2). `.rodata` literal-pool slots are therefore genuinely
> unrelocated, so the `add rX,pc` register really is the only bias source.
>
> **Method lesson, and it is the general form of this defect class:** *never*
> infer "there are no relocations" from a total count. Read `r_info & 0xff`, then
> map every `r_offset` to a section. The wrong type name produced a
> right-answer/wrong-reason, which is the hardest kind of error to notice — and
> here it had already been laundered into a second file as an apparent
> cross-confirmation.

Then the mapping compounded it:

| quantity | value | bytes |
|---|---|---|
| correct ELF VA | `0x021aebb4` | — |
| → correct file offset (`− 0x1000`) | `0x021adbb4` | `\xa1\x8d\xf4\x00\x85\xa1\xe7\x01…` = `0x00f48da1`, `0x01e7a185` — the relocated code-pointer pair |
| tool's printed target | `0x021bebb4` | — |
| → its file read (`− 0x10000`) | `0x021aebb4` | `X\x00\x1c\x02\xf8\x01\x1c\x02…` — **the phantom** |

So `0x021bebb4` was never an ELF VA, and the `+0x10000` error and the mapping error
each contributed exactly once. **Both are now corrected in place** in
`resolver-hardening-2026-10-05.md` (its D2 table's middle cell had
`0x021bebb4`, its §2.1 table labelled `0x021bebb4` "target ELF") and in
`grouprankup-sellcard-bodies-2026-10-05.md` §1.0, which had adopted the tool's
biased printout and then described a **file-offset** offset ("2 bytes past") as if
it were an address.

⚠️ **The specific D2 defect is narrow, and this bounds it.** A uniform
`addr − 0x10000` file mapping is wrong **only** for the second `PT_LOAD`
(`VA ≥ 0x0210e550`). **Every string literal in this corpus lives in `.rodata`
(`0x01d52940`–`0x0210d094`) or `.dynstr` (`0x000c4f20`–`0x0044af44`)**, both in
segment 0, so for *string* work the uniform mapping is **harmless**. It bites only
on `.got` / `.data*` / `.data.rel.ro*` byte reads — which is exactly the phantom
class. Do not generalise D2 into "all addresses are suspect".

**But the second segment has a SECOND, independent trap, and it is worse because
it is silent.** Those are the only **128 620 relocated** words in the binary.
Reading them from the on-disk `.so` gives you the **unrelocated** value, which is
`0x10000` short, with no error at all — the mapping was right and the *content*
was wrong. Concretely, in `native-all-strings.tsv`:

```
Ghidra 0x0211f7b0  ->  ELF VA 0x0210f7b0  ->  file 0x210e7b0  ->  LE32 0x01403264  (unrelocated)
Ghidra 0x0211f7b0  ->  ELF VA 0x0210f7b0  ->  + 0x10000        ->  LE32 0x01413264  (the TSV's value)
```

So the rule for writable data is **two** corrections, and they are not
interchangeable:

```
elf_va   = token - 0x10000
file_off = elf_va - 0x1000      (segment 1)
word     = LE32(elf_va - 0x1000) + 0x10000    (segment 1, RELOCATED)
```

Only the first two are needed for `.rodata` / `.text` / `.dynstr` / `.plt`
(segment 0). Every string-literal conclusion in this folder is unaffected.

---

## 6. The audit: per-file verdicts and the corrections applied

Method for the per-file verdicts: for every `.md` in this folder, pair each
address in the `0x01d52940..0x0210d094` (`.rodata`) window with each literal-looking
token on the **same line**, and byte-test all three interpretations. Reported as
`as-is / −0x10000 / +0x10000`. This is line-anchored, so it cannot be fooled by
`.rodata`'s density of coincidental matches (an earlier whole-address scoring pass
was discarded for exactly that reason — it produced false verdicts on
`gem-popup-bindings`).

| file | pairs | as-is | −0x10000 | verdict on its literal column | action |
|---|---|---|---|---|---|
| `blitz-search-consumers-2026-10-05.md` | 104 | **0** | **104** | GHIDRA | **FIXED** — claimed "addresses are ELF VAs" |
| `grouprankup-sellcard-bodies-2026-10-05.md` | 36 | **0** | **36** | GHIDRA | **FIXED** — column was unlabelled; also corrected §1.0's `0x021bebb4` |
| `batch-rankup-chucoin-2026-10-05.md` | 15 | **0** | **15** | GHIDRA | **FIXED** — claimed "file addresses", then unlabelled |
| `sunday-settlement-2026-10-05.md` | 17 | **0** | **17** | GHIDRA | **FIXED** — "string-table VAs" now labelled |
| `search-balance-divergence-2026-10-05.md` | 21 | **0** | **21** | GHIDRA | listed only (§7) — **no convention statement at all**, so nothing *stated* was wrong |
| `polluted-observations.md` | 5 | **0** | **5** | GHIDRA | **not touched** — no convention claim; parent mirrors it; Hangul bulk |
| `gvg-reference-2026-10-05.md` | 93 | 29 | 64 | **already correct** — §0.2 states and proves the retraction | none |
| `gem-popup-bindings-2026-10-05.md` | 16 | **16** | **0** | ELF VA — correct | **FIXED** — its row 3 claim *about the TSV* was wrong; line no. corrected (§6.2) |
| `point-info-type-2026-10-05.md` | 13 | **13** | **0** | ELF VA — correct | **FIXED** — `§1.9` relocation-type claim was false; `undefined` figure + segment-2 caveat |
| `resolver-hardening-2026-10-05.md` | 4 | **4** | **0** | ELF VA — correct | **FIXED** — 4 numeric/label errors |

### 6.1 Files stating a **wrong** convention — corrected in place

1. **`blitz-search-consumers-2026-10-05.md`** — provenance row read *"`analysis/native-all-strings.tsv` … addresses are ELF VAs"*. Wrong: 104/104 of its literal pairs need `− 0x10000`. This error was already *found* by `gvg-reference-2026-10-05.md` §0.2 but that file never edited its source, so the false claim was still live. **Corrected statement:** *"`analysis/native-all-strings.tsv` … its 8-hex column is GHIDRA image addresses = ELF VA + `0x10000`, not ELF VAs."* Its `native-evidence.tsv` row also now carries the `undefined` warning. **No address value in the file was changed** — every literal was already correct as printed *provided the reader knows the column is Ghidra*.
2. **`gem-levelup-action-2026-10-05.md`** — *"(e.g. `0024dea0`) are file-order tokens, NOT virtual addresses — do NOT add `0x10000` to them. Only the `00a5xxxx`/`00bdxxxx` values from `analysis/native-evidence.tsv` are Ghidra addresses."* **Both clauses wrong.** `0024dea0` is the TSV line for `CSRGem::RequestGemLevelUp`, at **ELF VA `0x0023dea0`** in `.dynstr`. **Corrected statement:** *both tables are Ghidra; the bias is already applied; do not add it again.*
3. **`gem-popup-bindings-2026-10-05.md`** — convention-table row 3: *"`analysis/native-all-strings.tsv` 8-hex keys | **file-order tokens, NOT addresses** | `002a6244` is not an address"*. **Wrong on both counts** — `002a6244` is line **25258** and is the image address of the `.dynstr` name `_ZN18CSRPopUpGemLevelUp11SetBaseInfoE…` at ELF `0x00296244`. (The line number was wrong in the first draft of this item too — 25257 is `002a621d _ZN18CSRPopUpGemLevelUp11AnvilheatedEi`. Corrected in both files.) **Corrected statement:** *Ghidra image addresses (= ELF VA + `0x10000`); measured 515 576/515 576, and for the 1 763 second-segment rows the naive reading matches 0 times.* The file's **own** 16/16 literal pairs were re-verified as ELF VA, so only the claim about the foreign table changed.
4. **`grouprankup-sellcard-bodies-2026-10-05.md`** — the convention note said *"`0x00xxxxxx` = Ghidra image address (= ELF + `0x10000`); `0x01dxxxxx` = `.rodata` literal address"*, leaving the literal column unlabelled; `resolver-hardening` §1.1 records it had been read as ELF. **Measured: 36/36 GHIDRA.** **Corrected statement:** *both columns are ELF VA + `0x10000`.* Five spot proofs added. §1.0's `'X'` row corrected: the target is **ELF VA `0x021aebb4`** (file `0x021adbb4`), not `0x021bebb4`.
5. **`batch-rankup-chucoin-2026-10-05.md`** — source list said *"`analysis/native-all-strings.tsv` (`.rodata` literal pool with **file addresses**)"*. Wrong: 15/15 pairs are Ghidra. **Corrected** to "Ghidra image addresses = ELF VA + `0x10000`, not file offsets", and the convention line's second clause now labels the literal column.
6. **`sunday-settlement-2026-10-05.md`** — *"(0x1d7xxxx) are native `.rodata` addresses from `native-all-strings.tsv`"* called them "string-table VAs" with no bias stated; 17/17 need `− 0x10000`. **Corrected** to state they are Ghidra image addresses, with `season_no` `0x1d7331e` → ELF `0x1d6331e` as the worked example.
7. **`resolver-hardening-2026-10-05.md`** — four numeric/label faults, all corrected: (a) §1.1's negative address `0x01c6e9dd` → **`0x01d5e9dd`** (`0x01d6e9dd − 0x10000`); (b) the §1.4-D1 transcript's `-> 0x021bebb4` now carries a note that it is the tool's **print**, not an ELF VA, with the `0x021aebb4` derivation; (c) §1.4-D2's "old tool file offset `0x021bebb4`" → **`0x021aebb4`** (the offset that really contains `b'X\x00…'`); (d) §2.1's "target ELF `0x021bebb4`" → **`0x021aebb4`**. Its *convention table* is otherwise correct and is the one this report defers to.
8. **`point-info-type-2026-10-05.md`** — **FIXED (second pass): a stated claim was wrong.** §1.9 read *"there are **no `R_ARM_RELATIVE` entries at all** in `.rel.dyn` … **128,620 `R_ARM_NONE`** … **`R_ARM_RELATIVE` count = 0**"*. The count was right and the **type name was wrong**: those 128 620 entries **are** `R_ARM_RELATIVE` (`r_info & 0xff == 23`), plus 32 `GLOB_DAT` and 13 `ABS32`, with **zero** `R_ARM_NONE`. It had been endorsed here as evidence, so the error was double-laundered. **The operative conclusion survives** on stronger evidence — **0 of the 128 620 relocations target `.rodata` or `.text`**, so `.rodata` pool slots are genuinely unrelocated (§5). Also quantified: its "`native-evidence.tsv` labels it `undefined`" finding — **91.2 %** of `[FUNCTIONS]` rows are mislabelled, only **735** imports deserve the tag (§4; the earlier figure of 775 was wrong). Its *"VMA == file offset"* line is correctly scoped to `.text`/`.rodata` and is flagged as **first-`PT_LOAD`-only**.
9. **`gem-popup-bindings-2026-10-05.md`** — a **line-number** error in the correction note itself: it cites `002a6244` as line **25257**; the correct line is **25258**. Values correct, citation fixed.
10. **`address-convention-2026-10-05.md`** (this file, **self-corrections**) — recorded because a report that hides its own errors is not auditable: (a) §3's "1205 rows match under no interpretation / residual escape-encoding artefacts" was **wrong** — there are no escaping artefacts; the residue is the `R_ARM_RELATIVE` bias and the true rate is **100.0000 %** (§3, §8.2); (b) §3's segment-1 discriminator was wrong **twice**: `606 vs 0` (measured on the raw file, superseded) and then `1759 vs 4` — the latter a **transposition**, since `1759` is what the uniform map *loses* while the correct map matches **1763 / 1763**. It was caught only because `verify-address-conventions.py` asserts these exact counts; (c) §4's "3 535 names not a `.dynsym` name at all" mislabelled 735 genuine `SHN_UNDEF` imports as unknown names — split 2 800 / 735; (d) §4's import count **775 → 735**; (e) §5 endorsed `point-info-type` §1.9's false "zero relocations" claim — now retracted above; (f) the `002a6244` line number 25257 → 25258.
11. **`verify-address-conventions.py`** (new, this pass) — a standard-library-only
    reproduction script that re-derives every number in this report from the ELF
    and the two TSVs, and **asserts** the counts. It exists because of item 10(b):
    a hand-written table transposed two columns and nothing caught it. Run
    `python verify-address-conventions.py` to re-derive; `--full` also reproduces
    the `llvm-objdump` ARM/Thumb evidence of §4b. It **reads** only — it writes
    nothing, and it opens no Ghidra project.

### 6.2 Files whose convention is **ambiguous** (no false statement) — listed, not edited

| file | ambiguity |
|---|---|
| `search-balance-divergence-2026-10-05.md` | 21 `.rodata` literal addresses, **all GHIDRA**, and **no convention note anywhere**. Consistent-by-luck, not by statement. Highest-risk file in the folder: a reader who assumes ELF is wrong on every address. |
| `gem-polish-parsers-2026-10-05.md` | States "Code coordinates are Ghidra addresses … unless marked ELF", but §1.6 quotes TSV **literal** tokens (`0024dea0`, `01d7862a`) that are Ghidra and fall under neither clause. Values are correct. |
| `polluted-observations.md` | 5 literal addresses, all GHIDRA, no note. **Deliberately not edited** — parent mirrors this file, and it carries the folder's Hangul bulk (`GUARD-encoding-and-archive-traps.md`). |
| `episode-res-crosswalk-2026-10-05.md`, `replica-shape-error-2026-10-05.md` | Cite `native-all-strings.tsv` only as a **vocabulary** source; make no address claims. No action needed. |
| `gem-levelup-action-2026-10-05.md` §1.1 | Header column is explicitly "Ghidra addr (`native-evidence.tsv`)" — correct — while the adjacent "strings.tsv key" column is now labelled by the §header correction. |
| `search-balance-divergence-2026-10-05.md` (2nd pass) | Its only address-convention phrase is §143's *"literal VAs in `analysis/native-all-strings.tsv`"* and §131's bare *"(`analysis/native-all-strings.tsv`)"*. Both are the same ambiguity as the row above. **Not edited** — it carries Hangul (70) and CJK (110), and `GUARD-encoding-and-archive-traps.md` makes bulk-Hangul edits the highest-risk operation in this folder. The fix is one word (“VAs” → “Ghidra image addresses”) and is deferred to whoever owns that file. |
| `gem-popup-bindings-2026-10-05.md` §1.0 (2nd pass) | Its corrected row 3 now cites the wrong *line number* for `002a6244`. **Edited** — 4 characters, no Hangul, no CJK; see §6.1 item 9. Contrast with the row above: the risk is **content class**, not file size. |

---

## 7. Why `gvg-reference-2026-10-05.md` was left alone

It is the only file in the folder that had already **found and stated** this defect
correctly, with a byte-exact proof and a retraction (§0.2, §0.3, and its own §
"Retractions" item 1). Its §0.2 arithmetic re-verified: `/gvg/GetRef` at TSV
`0x01d79394` → ELF `0x01d69394` with `d[0x01d69394] == b'/gvg/GetRef\x00'`. Its
claim that it "quotes **both** conventions and labels every one" also holds — its 29
`as-is` pairs are genuinely ELF VA (`ret_data` `0x1d589bb`, `card_%d` `0x1d6970b`,
both byte-exact as printed) and its 64 `-0x10000` pairs are genuinely Ghidra
(`app_code` `0x1d689d0`, `market` `0x1d689ee`). **The one thing it could not do was
fix its source**, which is item 6.1.1 above.

---

## 8. UNPURE / limits — read before trusting any of this

1. **The `Ghidra = ELF + 0x10000` identity is a property of this toolchain output,
   not of ELF.** It is proved here for `libnative_core.so` and must be re-derived
   for any other binary. AGENTS.md §16.7 lesson 3.
2. **RESOLVED — `native-all-strings.tsv`'s escaping needed no reverse
   engineering.** The earlier draft of this item claimed 1205 rows (0.23 %)
   "match under no interpretation" and attributed the residue to unverified
   byte-escaping. **That was wrong**, and it was wrong in the way AGENTS.md
   §16.7 lesson 5 warns about: a clean number read as a fact about the
   *measurement* when it was a fact about the *input*. The residue is entirely
   the **relocation bias** on writable-segment words, and it is fully accounted
   for: apply the 128 620 `R_ARM_RELATIVE` entries with bias `0x10000` and the
   match rate is **515 576 / 515 576 = 100.0000 %**, with **zero** rows
   unexplained. There is therefore **no** string column in this table that is not
   byte-verified. **Every row of `native-all-strings.tsv` is now byte-verified**,
   and so are all 8 642 rows of `native-evidence.tsv`'s
   `[RAW_PRINTABLE_STRINGS]`. Generalise: *before* blaming an encoder for a
   residual, check whether the bytes you are reading have been relocated.
3. **"Whole `.rodata` = segment 0" is an empirical bound, not a structural one.**
   Section headers put `.rodata` at `0x01d52940 + 0x003ba754 = 0x0210d094`, inside
   segment 0's `0x0210d320`. Correct for this build only.
4. **C1's proof covers 36 467 of 40 290 rows (90.51 %), not 100 %.** The
   remainder is accounted for and **not** a convention risk: 2 800 Ghidra-synthesized
   names (which nevertheless *self-declare* the space — see §4), 735
   `SHN_UNDEF` imports with `st_value == 0` (unmatchable by construction; 385 of
   them are in the EXTERNAL block with no file backing at all, §4a), and **288**
   defined symbols whose address differs (PLT-thunk / alias rows such as `_ZdlPv`,
   `_Znwj`, where Ghidra attributes a thunk address to the aliased target). The
   **288** were **not** individually audited; they are the only loose end in the
   `[FUNCTIONS]` population, and all 288 land in `.text` under the `−0x10000`
   reading, which is consistent with C1 rather than against it.
5. **Not proved:** whether the `<section>::<offset>` rows were produced by the same
   tool as the plain rows. They appear in **both** files (36 and 6, **disjoint**
   sets — the evidence file's set is truncated), which suggests yes, but no
   producer script was found.

   > ⚠️ **CORRECTION 2026-10-05 (later pass — `c4-row-census-2026-10-05.md`
   > §2.3):** the word **"disjoint" in this item is wrong.** The two C4 sets are a
   > **strict subset**, not disjoint. All **6** rows in `native-evidence.tsv`
   > (`.comment::00000001`, `.comment::000000b6`, `.shstrtab::00000072`,
   > `::00000097`, `::000000a4`, `::000000f3`) appear **verbatim** in
   > `native-all-strings.tsv`; measured overlap = **6/6**, so
   > `36 ∩ 6 = 6`, not 0. The correct description is *truncated subset*: the
   > evidence file's `.shstrtab` run stops at `0x000000f3` and it carries **no**
   > `.ARM.attributes`, `.note.gnu.gold-version` or `_elfSectionHeaders` rows.
   >
   > The census also **resolves** two things this item left open. (i) The
   > `_elfSectionHeaders` section name is **not** in this ELF's `.shstrtab`, but its
   > base is **`e_shoff` = `0x021cd744`**: `e_shoff + 0xb4` holds exactly the three
   > bytes `` $`8 `` that the TSV prints, and `0xb4 = 4 × 40 + 20` decodes to
   > **section-header entry 4 (`.dynstr`), byte 20 = its `sh_size` field** =
   > `0x00386024` = `.dynstr`'s size. (ii) With that base, **all 42 C4 rows are
   > byte-exact**, not the 6 spot-checked here. Full row-by-row table in
   > `c4-row-census-2026-10-05.md` §2.2.
   >
   > The C4 *rule* in §1/§3a is unchanged and is now proven as a **third** space:
   > all 42 tokens are `< 0x10000`, so they cannot be image addresses
   > (`token − 0x10000` would be negative), **0/42** reproduce their string at a
   > whole-file offset, and all four real sections they name are **non-alloc**
   > (`sh_addr == 0`) sitting at/past `PT_LOAD` file coverage `0x021cd3bc` — in the
   > file but in no loadable segment, so the program headers cannot resolve them at
   > all.
6. **Not touched:** the **`BLUSTONE_ARM` / `AGENTS.md` §16.7** convention (C7). It is
   outside this folder and outside the two tables under audit; it is listed only so
   the table is complete.
7. **No `AGENTS.md` edit was made.** This file is the durable record; the parent
   mirrors it, as with every other pass in this folder.
8. **Encoding guard result — both passes.** Every file edited in either pass was
   re-verified by `enc-guard.py` after **every individual edit**, not once at the
   end: **0 invalid UTF-8, 0 U+FFFD, 0 CR introduced**, LF-only line endings
   preserved throughout, and **Hangul and CJK counts byte-identical to their
   pre-edit baselines**. First pass, 8 files (`blitz-search-consumers` 652 Hangul /
   2 CJK, `sunday-settlement` 124, `point-info-type` 85, `gem-popup-bindings` 48,
   `gem-levelup-action` 8, `batch-rankup-chucoin` 2; all others 0). Second pass,
   2 files (`point-info-type` 85 Hangul / 0 CJK, `address-convention` 0 / 0) plus
   the two new `.py` files (ASCII-only, 0 Hangul, 0 CJK, 0 U+FFFD).
   `edit`/`write` + Python only; **no PowerShell file I/O on any workspace file.**
   One trap hit and neutralised: a patch script written through the tool chain had
   its `'\ufffd'` literal **silently emptied**, so the U+FFFD assertion in it became
   `assert '' not in txt`, which fires on *every* string. It was rewritten to build
   the character from an escape at runtime. **An encoding guard that cannot fail is
   worse than none** — verify the guard once before trusting its verdict.

---

## 9. One-page cheat sheet to paste into the next note

```
native-all-strings.tsv  8-hex  -> GHIDRA image addr. ELF = token - 0x10000.
native-evidence.tsv     [FUNCTIONS] addr -> GHIDRA image addr (IMAGE_BASE 00010000).
                                    Thumb bit: st_value has bit0 set; compare (st_value & ~1).
native-evidence.tsv     [RAW_PRINTABLE_STRINGS] 8-hex -> GHIDRA, same as row 1.
native-evidence.tsv     "undefined" column -> BROKEN; ignore (91.2% wrong; 735 real imports).
"<section>::<hex>" rows           -> section-relative offset; add sh_offset.
.ghidra-*.txt  ldr@/slot=/add@/->   -> GHIDRA image addr.
BLUSTONE_ARM                        -> ELF VA.  Ghidra = ELF + 0x10000.
llvm-objdump / llvm-nm labels       -> ELF VA (NO bias). NOT independent evidence for row 1.

ELF VA -> file offset:  va            if va <  0x0210d320   (p_offset == p_vaddr)
                         :  va - 0x1000 if va >= 0x0210e550   (p_offset == p_vaddr - 0x1000)

WRITABLE DATA ONLY (row C8) - silent trap, 128620 words:
  word = LE32(file_off) + 0x10000    ... only where .rel.dyn says R_ARM_RELATIVE at that VA
                                     ... .rodata/.text/.dynstr/.plt have ZERO such entries
```

Never quote an address out of one of these reports into another without stating
which row it came from. `resolver-hardening-2026-10-05.md` §1.1 and
`gvg-reference-2026-10-05.md` §0.2 are the two prior statements of this rule; this
file is the measured, corpus-wide version.

**Three one-line rules that would each have prevented a real error in this
project:**

1. *`objdump` and `nm` print ELF VAs. They cannot corroborate a Ghidra-space
   claim — agreeing with them means the other side is wrong, not right.*
2. *Mask bit 0 of `st_value` before comparing it to a Ghidra address, or every
   Thumb symbol silently fails and the test reports ~24 % instead of 90 %.*
3. *Read `r_info & 0xff` and map each `r_offset` to a section before concluding
   anything about relocations — a bare count told this project it had **zero**
   `R_ARM_RELATIVE` relocations when it had **128 620**.*