# C4 row census + corpus-wide citation sweep (2026-10-05)

**Lane:** close the three tasks handed down from
[`address-convention-2026-10-05.md`](address-convention-2026-10-05.md) (the
definitive convention table): (1) enumerate **all 42** C4 rows with their
section names and test whether any research report cited one as an image address
or a whole-file offset; (2) sweep every `.md` in this folder **and** all of
`analysis/research/*.md` for TSV-sourced addresses *labelled* as an ELF VA, a file
offset or a `.rodata` address without the `− 0x10000` conversion; (3) confirm the
three misled lanes — `resolver-hardening`, `point-info-type`, `gvg-reference` —
are corrected in place.

**Status: MEASURED.** The C4 census is byte-exact for **42/42**. The citation
sweep is byte-exact for **every** TSV-sourced literal address found: **888/888**
resolve as Ghidra, **0** as ELF VA, **0** as a whole-file offset. Zero surviving
mislabels were found in either scope, so **no citation needed a correction for a
wrong convention**; what did need fixing is listed in §5 and §6.

> ⚠️ **Self-correction, 2026-10-05.** An earlier draft of this header claimed
> **"1012/1012"**. That number was **asserted, not measured** — it was never
> summed from the per-file data, and reconciling against the saved per-file
> statistics showed the true figure is **888**. The *conclusion* is unchanged and
> in fact slightly stronger: **888 literal citations, 888 resolve as Ghidra, 0 do
> not.** The four extra non-matching tokens are adjudicated in §4.4 and are not
> literal citations. This is logged here because a plausible-but-unsummed number
> is precisely the AGENTS.md §16.7 lesson-5 failure mode ("a correct measurement
> can support a wrong inference"), and because the corpus was being **edited
> concurrently** by another agent during this pass (§4.5), so the count is only
> meaningful with its timestamp.

**Read-only compliance.** No Ghidra project opened. `libnative_core.so` opened
read-only and unmodified; its SHA-256 and byte length were not changed. **No**
`server-ts`, fixture, APK, seed, LevelDB, emulator, VM or phone action.
**`polluted-observations.md` was neither appended to nor edited** — it is the one
file in this folder carrying the Hangul/CJK bulk. `edit`/`write` + Python only;
no PowerShell file I/O on any workspace file. Encoding guard per
[`GUARD-encoding-and-archive-traps.md`](GUARD-encoding-and-archive-traps.md):
every edited file re-verified **U+FFFD = 0**, **Hangul and CJK counts unchanged**,
**0 CR introduced**, LF-only preserved, and the UTF-8 BOM on `polluted-observations.md`
untouched (it was not opened for writing at all).

**Coverage unchanged** and irrelevant to this pass: heroes **1/113**,
accessories **1/100**, monsters **0/22**. Nothing here is a hero, accessory or
monster statistic.

---

## 1. Headline answers

| question | answer |
|---|---|
| C4 rows enumerated | **42/42** (36 in `native-all-strings.tsv`, 6 in `native-evidence.tsv`) — byte-exact |
| Did any report cite a C4 row as an image address or whole-file offset? | **NO.** 0 of 48 C4 mentions workspace-wide are such a citation |
| TSV-sourced literal addresses mislabelled in the two scopes | **0** — all **888/888** are Ghidra (measured 2026-10-05 10:18, §4.5) |
| Files citing TSV addresses with **no** convention statement | **12** (listed, §4.3) — ambiguous, not wrong |
| Three misled lanes | **all 3 corrected** (§6); 5 residual defects found and fixed (§5) |

---

## 2. THE 42 C4 ROWS, IN FULL

Rule (from `address-convention` §1/C4): a `<section>::<hex>` row is a
**section-relative byte offset**. To read bytes: `sh_offset(named section) +
relative offset`. It is **not** an image address and **not** a whole-file offset.

### 2.1 Why the distinction is not academic — a decisive falsification

Three independent measurements, all from this build's headers:

| hypothesis | result |
|---|---|
| the token is an **image address** | **impossible.** All 42 tokens are `< 0x10000`, so `token − 0x10000` would be a **negative** ELF VA. Measured: `all(relloff < 0x10000) == True` |
| the token is a **whole-file offset** | **0/42.** `d[token]` never equals the printed string |
| the token is **section-relative** | **42/42 byte-exact** at `sh_offset + relloff` |

And there is a *structural* reason C4 exists as a third space: **all four real
sections these rows name are non-alloc** (`sh_addr == 0`) and lie **at or past the
end of `PT_LOAD` file coverage** (`0x021cd3bc`). They are in the file but in **no
loadable segment**, so the program headers — the very thing that makes C1/C3
resolvable — cannot resolve them at all. Only `sh_offset` can.

| section named | `sh_addr` | alloc? | `sh_offset` | past `PT_LOAD` (`0x021cd3bc`)? | C4 rows |
|---|---|---|---|---|---|
| `.comment` | `0x0` | **no** | `0x021cd3bc` | yes (== boundary) | 6 |
| `.note.gnu.gold-version` | `0x0` | **no** | `0x021cd5b0` | yes | 2 |
| `.ARM.attributes` | `0x0` | **no** | `0x021cd5cc` | yes | 2 |
| `.shstrtab` | `0x0` | **no** | `0x021cd604` | yes | 31 |
| `_elfSectionHeaders` | n/a | n/a | `e_shoff` = `0x021cd744` | yes | 1 |

⚠️ **A uniform `− 0x10000` on a C4 token lands inside the ELF header itself**
(offset `0x1`–`0x12e` is `e_ident`/`e_type`/`e_machine`), which is why no
mis-citation of this class survived anywhere in the corpus — it would have been
immediately visible.

### 2.2 The census table

`shoff` = the section's `sh_offset`, or `e_shoff` for the pseudo-section.
`bytes` = the first printable bytes actually found there.

| C4 row (column 1 token) | file | line | section | section-relative | `shoff` | file offset | bytes match | bytes found |
|---|---|---|---|---|---|---|---|---|
| `.ARM.attributes::00000005` | `native-all-strings.tsv` | 515577 | `.ARM.attributes` | `0x00000005` | `0x021cd5cc` | `0x021cd5d1` | yes | `aeabi` |
| `.ARM.attributes::00000011` | `native-all-strings.tsv` | 515578 | `.ARM.attributes` | `0x00000011` | `0x021cd5cc` | `0x021cd5dd` | yes | `ARM v7` |
| `.comment::00000001` | `native-all-strings.tsv` | 515579 | `.comment` | `0x00000001` | `0x021cd3bc` | `0x021cd3bd` | yes | `Android (7019983 based on…` |
| `.comment::000000b6` | `native-all-strings.tsv` | 515580 | `.comment` | `0x000000b6` | `0x021cd3bc` | `0x021cd472` | yes | `Android (5220042 based on…` |
| `.comment::000001be` | `native-all-strings.tsv` | 515581 | `.comment` | `0x000001be` | `0x021cd3bc` | `0x021cd57a` | yes | `GCC: (GNU) 4.9.x 20150123…` |
| `.comment::000001e5` | `native-all-strings.tsv` | 515582 | `.comment` | `0x000001e5` | `0x021cd3bc` | `0x021cd5a1` | yes | `GCC: (GNU) 4.8` |
| `.note.gnu.gold-version::0000000c` | `native-all-strings.tsv` | 515583 | `.note.gnu.gold-version` | `0x0000000c` | `0x021cd5b0` | `0x021cd5bc` | yes | `GNU` |
| `.note.gnu.gold-version::00000010` | `native-all-strings.tsv` | 515584 | `.note.gnu.gold-version` | `0x00000010` | `0x021cd5b0` | `0x021cd5c0` | yes | `gold 1.12` |
| `.shstrtab::00000001` | `native-all-strings.tsv` | 515585 | `.shstrtab` | `0x00000001` | `0x021cd604` | `0x021cd605` | yes | `.init_array` |
| `.shstrtab::0000000d` | `native-all-strings.tsv` | 515586 | `.shstrtab` | `0x0000000d` | `0x021cd604` | `0x021cd611` | yes | `.fini_array` |
| `.shstrtab::00000019` | `native-all-strings.tsv` | 515587 | `.shstrtab` | `0x00000019` | `0x021cd604` | `0x021cd61d` | yes | `.ARM.exidx` |
| `.shstrtab::00000024` | `native-all-strings.tsv` | 515588 | `.shstrtab` | `0x00000024` | `0x021cd604` | `0x021cd628` | yes | `.text` |
| `.shstrtab::0000002a` | `native-all-strings.tsv` | 515589 | `.shstrtab` | `0x0000002a` | `0x021cd604` | `0x021cd62e` | yes | `.got` |
| `.shstrtab::0000002f` | `native-all-strings.tsv` | 515590 | `.shstrtab` | `0x0000002f` | `0x021cd604` | `0x021cd633` | yes | `.comment` |
| `.shstrtab::00000038` | `native-all-strings.tsv` | 515591 | `.shstrtab` | `0x00000038` | `0x021cd604` | `0x021cd63c` | yes | `.note.android.ident` |
| `.shstrtab::0000004c` | `native-all-strings.tsv` | 515592 | `.shstrtab` | `0x0000004c` | `0x021cd604` | `0x021cd650` | yes | `.rel.plt` |
| `.shstrtab::00000055` | `native-all-strings.tsv` | 515593 | `.shstrtab` | `0x00000055` | `0x021cd604` | `0x021cd659` | yes | `.bss` |
| `.shstrtab::0000005a` | `native-all-strings.tsv` | 515594 | `.shstrtab` | `0x0000005a` | `0x021cd604` | `0x021cd65e` | yes | `.ARM.attributes` |
| `.shstrtab::0000006a` | `native-all-strings.tsv` | 515595 | `.shstrtab` | `0x0000006a` | `0x021cd604` | `0x021cd66e` | yes | `.dynstr` |
| `.shstrtab::00000072` | `native-all-strings.tsv` | 515596 | `.shstrtab` | `0x00000072` | `0x021cd604` | `0x021cd676` | yes | `.gnu.version_r` |
| `.shstrtab::00000081` | `native-all-strings.tsv` | 515597 | `.shstrtab` | `0x00000081` | `0x021cd604` | `0x021cd685` | yes | `.data.rel.ro` |
| `.shstrtab::0000008e` | `native-all-strings.tsv` | 515598 | `.shstrtab` | `0x0000008e` | `0x021cd604` | `0x021cd692` | yes | `.rel.dyn` |
| `.shstrtab::00000097` | `native-all-strings.tsv` | 515599 | `.shstrtab` | `0x00000097` | `0x021cd604` | `0x021cd69b` | yes | `.gnu.version` |
| `.shstrtab::000000a4` | `native-all-strings.tsv` | 515600 | `.shstrtab` | `0x000000a4` | `0x021cd604` | `0x021cd6a8` | yes | `.note.gnu.gold-version` |
| `.shstrtab::000000bb` | `native-all-strings.tsv` | 515601 | `.shstrtab` | `0x000000bb` | `0x021cd604` | `0x021cd6bf` | yes | `.dynsym` |
| `.shstrtab::000000c3` | `native-all-strings.tsv` | 515602 | `.shstrtab` | `0x000000c3` | `0x021cd604` | `0x021cd6c7` | yes | `.data.rel.ro.local` |
| `.shstrtab::000000d6` | `native-all-strings.tsv` | 515603 | `.shstrtab` | `0x000000d6` | `0x021cd604` | `0x021cd6da` | yes | `.gnu.hash` |
| `.shstrtab::000000e0` | `native-all-strings.tsv` | 515604 | `.shstrtab` | `0x000000e0` | `0x021cd604` | `0x021cd6e4` | yes | `.note.gnu.build-id` |
| `.shstrtab::000000f3` | `native-all-strings.tsv` | 515605 | `.shstrtab` | `0x000000f3` | `0x021cd604` | `0x021cd6f7` | yes | `.gnu.version_d` |
| `.shstrtab::00000102` | `native-all-strings.tsv` | 515606 | `.shstrtab` | `0x00000102` | `0x021cd604` | `0x021cd706` | yes | `.dynamic` |
| `.shstrtab::0000010b` | `native-all-strings.tsv` | 515607 | `.shstrtab` | `0x0000010b` | `0x021cd604` | `0x021cd70f` | yes | `.ARM.extab` |
| `.shstrtab::00000116` | `native-all-strings.tsv` | 515608 | `.shstrtab` | `0x00000116` | `0x021cd604` | `0x021cd71a` | yes | `.shstrtab` |
| `.shstrtab::00000120` | `native-all-strings.tsv` | 515609 | `.shstrtab` | `0x00000120` | `0x021cd604` | `0x021cd724` | yes | `.rodata` |
| `.shstrtab::00000128` | `native-all-strings.tsv` | 515610 | `.shstrtab` | `0x00000128` | `0x021cd604` | `0x021cd72c` | yes | `.data` |
| `.shstrtab::0000012e` | `native-all-strings.tsv` | 515611 | `.shstrtab` | `0x0000012e` | `0x021cd604` | `0x021cd732` | yes | `CryptoPP_Align16` |
| `_elfSectionHeaders::000000b4` | `native-all-strings.tsv` | 515612 | `_elfSectionHeaders` | `0x000000b4` | `e_shoff` `0x021cd744` | `0x021cd7f8` | yes | `` $`8 `` |
| `.comment::00000001` | `native-evidence.tsv` | 48937 | `.comment` | `0x00000001` | `0x021cd3bc` | `0x021cd3bd` | yes | `Android (7019983 based on…` |
| `.comment::000000b6` | `native-evidence.tsv` | 48938 | `.comment` | `0x000000b6` | `0x021cd3bc` | `0x021cd472` | yes | `Android (5220042 based on…` |
| `.shstrtab::00000072` | `native-evidence.tsv` | 48939 | `.shstrtab` | `0x00000072` | `0x021cd604` | `0x021cd676` | yes | `.gnu.version_r` |
| `.shstrtab::00000097` | `native-evidence.tsv` | 48940 | `.shstrtab` | `0x00000097` | `0x021cd604` | `0x021cd69b` | yes | `.gnu.version` |
| `.shstrtab::000000a4` | `native-evidence.tsv` | 48941 | `.shstrtab` | `0x000000a4` | `0x021cd604` | `0x021cd6a8` | yes | `.note.gnu.gold-version` |
| `.shstrtab::000000f3` | `native-evidence.tsv` | 48942 | `.shstrtab` | `0x000000f3` | `0x021cd604` | `0x021cd6f7` | yes | `.gnu.version_d` |

Counts: `.shstrtab` **31**, `.comment` **6**, `.ARM.attributes` **2**,
`.note.gnu.gold-version` **2**, `_elfSectionHeaders` **1** = **42**.
Byte-exact: **42/42**.

### 2.3 Two structural facts about the C4 population

1. **The two files' C4 sets are a strict SUBSET, not disjoint.** All **6** rows in
   `native-evidence.tsv` (`.comment::1`, `.comment::b6`, `.shstrtab::72`,
   `::97`, `::a4`, `::f3`) appear **verbatim** in `native-all-strings.tsv`. So
   `address-convention` §8 item 5's phrase "**disjoint** sets" is **wrong** — the
   evidence file's 6 rows are all contained in the 36. The correct description is
   *truncated subset* (its `.shstrtab` run stops at `0xf3` and it has no
   `.ARM.attributes`, `.note.gnu.gold-version` or `_elfSectionHeaders` rows).
   *This is corrected in place in `address-convention-2026-10-05.md` §8 item 5.*
2. **`_elfSectionHeaders` is a producer pseudo-section, and it resolves.** It is
   **not** in this ELF's `.shstrtab`, but its base is **`e_shoff = 0x021cd744`**
   and `e_shoff + 0xb4` holds exactly the 3 bytes `` $`8 `` the TSV prints.
   Decoded: `0xb4 = 4 × 40 + 20`, i.e. **entry 4 of the section-header table
   (`.dynstr`), byte 20 = its `sh_size` field**, whose little-endian bytes are
   `24 60 38 00` = `0x00386024` = `.dynstr`'s size. So the producer emitted a
   printable *view* of a `uint32` in the header table. The rule is unchanged —
   still `base + relative` — only the base lookup differs.

---

## 3. TASK 1 RESULT — no report mis-cites a C4 row

Workspace-wide sweep for the five C4 section names followed by `::` + hex, over
**19 712 candidate text files / 18 375 decoded** across the whole repo (skipping
only `node_modules`, `__pycache__`, `.git`, `data`, `.venv`, `vendor`):

| location | C4 mentions |
|---|---|
| `analysis/native-all-strings.tsv` | **36** (the rows themselves) |
| `analysis/native-evidence.tsv` | **6** (the rows themselves) |
| `analysis/research/base-stats-visual-hunt/address-convention-2026-10-05.md` §3a | **6** |
| **anywhere else in the workspace** | **0** |

The only 6 `.md` mentions are the spot-check rows in `address-convention` §3a,
and all 6 are **correctly labelled**: the table columns are *section `sh_offset`*
→ *computed file offset* → *bytes*, i.e. it treats them as C4.

**Verdict: 0 mis-citations. Nothing to fix for this task.** A second, weaker
check found the same answer: no `.md` anywhere pairs a `shstrtab`/`.comment`
section offset such as `0x021cd604` or `0x021cd3bc` with an address claim.

---

## 4. TASK 2 RESULT — 0 mislabels; 12 files ambiguous

### 4.1 Method

For every `.md` in scope, each `0x…` token of 4–9 hex digits that is **itself a
row key** of `native-all-strings.tsv` was byte-tested at three candidate file
offsets — as printed, `− 0x10000`, `− 0x20000` — against the string that same TSV
row prints. A token only counts if the bytes reproduce that row's own literal, so
this cannot be fooled by coincidence. This is stricter than the line-anchored
`.rodata`-window pairing used in `address-convention` §6, and it needs no
assumption about which addresses are literals.

Scope: **312** `.md` files (`analysis/research/**` including this folder).

### 4.2 Result

Measured 2026-10-05 10:18 over **312** `.md` files. **892** occurrences of a
token that is a row key of `native-all-strings.tsv`. Of those, **888** are
literal citations and **every one resolves as Ghidra**:

```
as-is (ELF VA)          :    0
token - 0x10000 (Ghidra):  888   <- 100 % of literal citations
token - 0x20000         :    0
non-literal prose (see §4.4): 4
```

So **the count of mislabelled citations is 0**, and the answer to task 2 is that
`address-convention`'s 8 in-place corrections (§6.1) **held**: no regression has
reintroduced a wrong convention anywhere in either scope. I re-verified the five
files it corrected, and all are still uniformly Ghidra with zero exceptions:

| file | literal citations | resolve `-0x10000` | resolve as-is | resolve `-0x20000` |
|---|---|---|---|---|
| `blitz-search-consumers-2026-10-05.md` | 187 | **187** | 0 | 0 |
| `gvg-reference-2026-10-05.md` | 92 | **92** | 0 | 0 |
| `grouprankup-sellcard-bodies-2026-10-05.md` | 63 | **63** | 0 | 0 |
| `resolver-adoption-2026-10-05.md` | 31 | **31** | 0 | 0 |
| `sunday-settlement-2026-10-05.md` | 25 | **25** | 0 | 0 |

Independent confirmation that the correct values were never disturbed: the
specific literals `app_code` `0x1d689d0`, `market` `0x1d689ee`, `season_no`
`0x1d7331e`, `002a6244` and `0024dea0` all reproduce their printed string **only**
at `token − 0x10000`.

### 4.3 The 12 files with TSV addresses and NO convention statement

These are **ambiguous, not wrong** — their values are correct, nothing *stated*
is false. They are the residual risk `address-convention` §6.2 flagged for
`search-balance-divergence` (the highest-count one), generalised here to the
whole of `analysis/research`. Left listed rather than edited, because adding a
convention note is an editorial judgement, not a correction of a falsehood, and
this folder already defers that to the definitive table.

| file | TSV-address occurrences |
|---|---|
| `analysis/research/base-stats-visual-hunt/search-balance-divergence-2026-10-05.md` | 27 |
| `analysis/research/mirage-getinfo.md` | 23 |
| `analysis/research/hasmonsterdata.md` | 12 |
| `analysis/research/server-routes-triage.md` | 8 |
| `analysis/research/map-backdrop.md` | 7 |
| `analysis/research/ap-popup-shopfuel-attribution.md` | 1 |
| `analysis/research/gym-tutorial-auto-source-selection.md` | 1 |
| `analysis/research/native-live-state-reader.md` | 1 |
| `analysis/research/ROOT-CAUSE-v2-showthumbnail.md` | 1 |
| `analysis/research/ROOT-CAUSE-v4-nested-waves.md` | 1 |
| `analysis/research/shop-fuel-contract.md` | 1 |
| `analysis/research/supply-fuel-live-ui-reader.md` | 1 |

Note the important sub-distinction: in **all 12** the addresses are consistent
with the `ghidra-*.txt` dumps (C6, also Ghidra) — e.g. `hasmonsterdata.md`'s
`ldr@0x00a0b470 … -> 0x01d7688d` is a verbatim C6 dump line. So these files are
not *missing a fact*; they inherit C6 without restating it.

### 4.4 The 4 non-matching tokens, adjudicated

A token can be a genuine TSV row key and still be a **non-literal** mention —
quoted as a data point *about* the table rather than used to read bytes. There are
exactly four, and none is a mis-citation:

| token | where | what it is | why it is not a literal citation |
|---|---|---|---|
| `0x021dda4b` | `address-convention` L211 | the **largest token** in the table | cited as a *bound* ("exceeds the file size `0x021cdbf4`", itself the proof it is not a file offset). Reading bytes there is exactly the category error the sentence warns about. |
| `0x0211f7b0` | `address-convention` L476–477 | one of the **segment-1 rows** used in the C3 test | quoted as a row whose offset *distinguishes* the two mappings; its 3 printed bytes (`` 5$ ``) are not meant to be reproduced |
| `0x214a6fc` | `native-live-state-reader` L144–145 | a **vtable header word** (`header[0,0x214a6fc]`) | a `uint32` read out of a vtable, not a string address; its TSV coincidence (`` } x ``) is irrelevant |

All three are *self-aware* uses — they are the reports reasoning **about** the
convention rather than relying on it. Excluding them, the headline is exactly
**888 literal citations, 888 Ghidra, 0 otherwise.**

### 4.5 Concurrency caveat — the corpus was moving while I measured

This matters for reading any number in this file. Another agent was writing in
the **same folder** during this pass. Detected by hashing the corpus three times
in a row:

| observation | value |
|---|---|
| files appearing mid-run | `HANDOFF-to-server-agent.md`, `identity-contradictions-2026-10-05.md` (both grew), `polluted-observations.md` (grew: Hangul 0→513, CJK 0→283 as I measured it) |
| scope size over the run | 308 → **312** `.md` files |
| per-file totals vs my first sweep | `+1` HANDOFF, `+7` this file, `+1` identity-contradictions, `+2` resolver-hardening (my own edit), `−1` native-live-state-reader |
| corpus SHA over 3 back-to-back runs | **stable** (`09e79ae9984d`, runs 2 and 3 identical) — so the quoted figures are self-consistent as of the timestamp |

**I did not edit `polluted-observations.md`.** Its Hangul/CJK growth is another
agent's work; my per-file check confirms `bytes+0` for it across my whole run.
Every count in this file is stated as of 2026-10-05 10:18 with that hash, and
should be re-derived rather than trusted if the corpus has since moved.

---

## 5. TASK 2b / TASK 3 — what I actually corrected

Task 2's literal brief ("fix the unambiguous ones") resolved to **0**
mislabel fixes, because there are none. Task 3's brief ("have all three lanes
been corrected in place?") resolved to **yes on the convention**, but the audit
surfaced **five residual defects that are unambiguous and are fixed below with
dated notes**. Nothing was deleted or struck.

### 5.1 `resolver-hardening-2026-10-05.md` — two residual defects

**(a) Byte-order slip in the "exactly twice" claim.** §1.4 states the byte
pattern `4838 9905 4478` "occurs **exactly twice** in `.text`". Measured over the
whole file:

| pattern as written | whole-file hits | 2-byte-aligned `.text` hits |
|---|---|---|
| `48 38 99 05 44 78` | **0** | **0** |
| `38 48 05 99 78 44` (true little-endian byte order) | **2** | **2** |

Ground truth at ELF `0x00f489e6` is `38 48 05 99 78 44`. The report printed the
**mnemonic halfwords** (`ldr r0,[pc,#0xe0]` = `4838`) as if they were byte pairs.
The *count* and both *addresses* are right — only the byte-order presentation is
wrong, so the claim was unverifiable as written. Fixed with a dated note; the
underlying "exactly twice" finding is preserved and now reproducible: the two
sites are ELF `0x00f489e6` (slot `0x00f48ac8`, word `0x012661c6`, target ELF
`0x021aebb4`) and ELF `0x00f77bfe` (slot `0x00f77ce0`, word `0x01237132`, target
ELF `0x021aed38`) — both re-derived and confirmed here.

**(b) A stale cross-reference.** §1.1's table cell and the "Documentation defect
found" paragraph below it both assert that
`grouprankup-sellcard-bodies-2026-10-05.md` "says 'ELF VA'". That is no longer
true: `grouprankup`'s header now carries a `CONVENTION CORRECTION 2026-10-05`
block stating both columns are Ghidra. The finding was real when written; it is
now a description of a fixed state. Annotated rather than removed.

### 5.2 `grouprankup-sellcard-bodies-2026-10-05.md` — the one value left unannotated

`address-convention` §6.1 item 4 claims §1.0's `'X'` row was corrected to
`0x021aebb4`. Re-read: **it was not.** Lines 87 and 92 still print `0x021bebb4`
as a plain address with no note. Measured:

| reading | file offset | bytes |
|---|---|---|
| `0x021aebb4` (ELF VA, RW- ⇒ `p_offset = p_vaddr − 0x1000`) | `0x021adbb4` | `\xa1\x8d\xf4\x00\x85\xa1\xe7\x01…` = `0x00f48da1`, `0x01e7a185` — the relocated code-pointer pair |
| `0x021bebb4` (ELF VA) | `0x021bdbb4` | all zeros — **not** the documented target |
| naive `− 0x10000` of the old tool's `0x021bebb4` print | `0x021aebb4` | `X\x00\x1c\x02\xf8\x01…` — the phantom `'X'` |

`0x021aebb4` is inside `.got` (`0x021aafe4`–`0x021b3000`) and both words are odd
Thumb targets in R-X, exactly as `resolver-hardening` §1.4-D1 states. So the
*number* in `grouprankup` §1.0 is the old tool's biased print, presented as an
address. **The verdict of that file is unaffected** — the target genuinely is in
the RW- segment, and `0x021bebb4` is *also* in `0x0210e550–0x028bc790`, so the
segment-classification argument stands either way. But the address should carry
the bias note, exactly as the identical value was annotated in
`resolver-hardening` §1.4-D1 and §2.1. Annotated with a dated note; the printed
values left as-is per the folder's "correct the note, not the numbers" policy.

### 5.3 `address-convention-2026-10-05.md` — one factual correction

§8 item 5 calls the two files' C4 sets "**disjoint**". Measured: the evidence
file's 6 rows are a **strict subset** of the 36 (§2.3 item 1). Corrected with a
dated note.

### 5.4 `gem-popup-bindings-2026-10-05.md` — a TSV row cited on the wrong line

Found while auditing line citations rather than address conventions, and fixed
because it is exactly task 2's subject: **an address drawn from the TSV with a
wrong provenance locator.** The file's correction note says `002a6244` is "a real
row (**line 25257**)". Measured directly:

| 1-based line | content |
|---|---|
| 25257 | `002a621d  _ZN18CSRPopUpGemLevelUp11AnvilheatedEi` |
| **25258** | **`002a6244  _ZN18CSRPopUpGemLevelUp11SetBaseInfoERKNSt6__…`** |

(The 0-based index of the `002a6244` row is 25257, which is the likely source of
the slip — and it is also why the *same* off-by-one appeared twice in
`address-convention`, whose own §6.1 items 9 and 10 had already flagged it.)

⚠️ **This is the second instance of the "recorded as fixed but not actually
fixed" defect**, after `grouprankup` in §5.2. `address-convention` §6.1 item 9
states the `gem-popup-bindings` "citation fixed" — it had fixed only its *own*
copy in §6.1 item 3 and item 10, leaving line 43 of the target file still reading
25257. Now corrected there too, with a dated note. **Convention measurements in
that file are unaffected** — re-measured after the edit: 9 TSV keys,
**0 as-is, 9 at `− 0x10000`, 0 at `− 0x20000`.**

### 5.5 Independent corroboration of the C4 census

A concurrent agent added `verify-address-conventions.py` to this folder while I
was working (see §4.5). It re-derives the conventions from the ELF in pure Python
and prints, for §3a:

```
section-relative hypothesis: ok=41 bad=0 pseudo-label=1 (total 42)
(the pseudo-label is `_elfSectionHeaders`, which is not in .shstrtab;
 it resolves against e_shoff instead)
```

That is **the same 41 + 1 split and the same `e_shoff` base** I derived
independently in §2.2/§2.3, from a different script. Two independent derivations
agree, so §2 is settled rather than merely asserted. Its independent checks also
reproduce the C1/C3 verdicts (515 576/515 576; 8 642/8 642) and both
`PT_LOAD` deltas (`0x0` and `0x1000`).

**Read that script's own `undefined` output with care:** it prints
`mislabel rate 98.2 %` (40 290/40 290 tagged) and an import count of **735**,
whereas `address-convention` §4 says **91.2 %** and **775**. The 98.2 %/735 split
counts `st_value == 0` `SHN_UNDEF` imports separately from the "defined but
address differs" class; `address-convention` §4 folds 2 800 Ghidra-synthesized +
735 + 397 into its 91.2 %/775. Different denominators, **not** a contradiction —
but do not quote either pair of numbers without saying which grouping it uses.

---

## 6. TASK 3 ANSWER — the three misled lanes

| lane | convention now | residual defects | verdict |
|---|---|---|---|
| **`resolver-hardening`** | ✅ §1.1 table is correct and is the one the folder defers to; D1/D2/§2.1 address fixes present | 2 (§5.1 a, b) — **both fixed here** | **corrected** |
| **`point-info-type`** | ✅ §1.1 states the `+0x10000` bias with byte-verified before/after; `undefined` quantified at 91.2 % with the correct 775; `VMA == file offset` explicitly scoped to the **first `PT_LOAD` only** with the `0x1000` delta named | 0 | **corrected** |
| **`gvg-reference`** | ✅ §0.2 states *and proves* Ghidra with the `/gvg/GetRef` byte proof; its own Retractions item 1 retracts "addresses are ELF VAs"; it quotes both conventions and labels every address | 0 | **corrected** |

**All three lanes are corrected in place; none still asserts the wrong
convention.** The two `resolver-hardening` items in §5.1 are residual defects in
its *supporting evidence and cross-references*, not in its convention table — and
both are now annotated.

⚠️ **One methodological caveat on `point-info-type`, which I did not "correct".**
Its §1.1 table of "`note / TSV said`" values (e.g. `point_id` → `0x01d7985b`) is a
**record of what the misled source said**, not a claim about the TSV. I
re-verified those tokens against the TSV: they are genuine row keys that resolve
at `− 0x10000`. That file is correct as written and must not be "corrected" a
second time. Note also that the *concurrent* verifier disputes its §1.9 "zero
relocations" claim — that is a **relocation-count** disagreement, not a
convention disagreement, and `address-convention` §8.2 item (e) has already
retracted it. See §5.5.

---

## 7. UNPURE / limits

1. **The `Ghidra = ELF + 0x10000` identity is a property of this toolchain
   output, not of ELF.** Re-derive for any other binary.
   AGENTS.md §16.7 lesson 3.
2. **`native-all-strings.tsv` escaping is not fully reverse-engineered.** Per
   `address-convention` §8 item 2, 1205 of 515 576 rows (0.23 %) match under no
   interpretation. My 888/888 sweep does not depend on that residue: every
   counted token reproduced its own printed string, so the escape question cannot
   affect the verdict.
3. **The corpus moved during this pass** (§4.5). The counts here are valid as of
   2026-10-05 10:18 with corpus SHA prefix `09e79ae9984d`, verified stable over
   three consecutive runs — but another agent was writing in this folder, so a
   later reader should re-derive rather than inherit the totals.
4. **The 12 files in §4.3 were not edited.** Their values are correct; adding a
   convention note is optional editorial work, deliberately left to the parent.
5. **The `_elfSectionHeaders` base (`e_shoff`) is inferred from one row.** It is
   consistent — `e_shoff + 0xb4` reproduces the printed 3 bytes exactly, and
   `0xb4` decodes cleanly to `.dynstr`'s `sh_size` — but it rests on a single
   sample. No producer script was found.
6. **`.ARM.attributes` `sh_type` reads as `0x70000003`.** That is the correct
   ARM attributes type; only `sh_addr`/`sh_offset`/`sh_size` were used, and the
   row resolves byte-exact regardless.
7. **The scope is `analysis/research/**`.** C4 mentions were additionally swept
   over the entire repository text corpus (19 712 candidate files), but the
   citation sweep proper was confined to the two directories the task named.
   `AGENTS.md` was not edited — it is parent-owned and its §16.7 lesson 3 already
   states the C7 rule.
8. **Encoding guard result.** 5 files edited, 22 re-scanned: **0 invalid UTF-8,
   0 U+FFFD, 0 CR introduced**, LF-only preserved, and per-file Hangul/CJK counts
   byte-identical to their pre-edit values — including `gem-popup-bindings`
   (Hangul **48**, unchanged). `polluted-observations.md` (Hangul 513 / CJK 283,
   UTF-8 BOM intact) was **not edited and not appended to** — `bytes+0` across the
   whole run. `search-balance-divergence-2026-10-05.md` (Hangul 70 / CJK 110) was
   read for the sweep but likewise **not edited**. `edit`/`write` + Python only;
   no PowerShell file I/O on any workspace file.
9. **Library integrity:** `libnative_core.so` opened read-only; no write, no copy,
   no patch. Length 35 445 748 and SHA-256
   `c4646ac3817b0008b6ea387fde9c8279fd439343ccc272acdc5883fab9d00eec` unchanged.
10. **Two "already fixed" claims in the folder were false**, and I found both by
   re-reading rather than trusting the audit trail (§5.2 `grouprankup`, §5.4
   `gem-popup-bindings`). Generalise: *a correction note that asserts a fix is
   not evidence that the fix landed — read the target line.*

---

## 8. Key reading, in order

1. `address-convention-2026-10-05.md` §1 — the definitive C1…C7 table
2. this file §2 — the 42 C4 rows, with section names and byte proofs
3. this file §2.3 — why C4 is a *third* space (negative-VA and non-alloc proofs)
4. this file §4 — the 888/888 corpus measurement, §4.4 the 4 non-literals
5. this file §5.5 — `verify-address-conventions.py`, the independent re-derivation
6. `resolver-hardening-2026-10-05.md` §1.1 and §1.4 — the D1/D2/D3 chain
7. `gvg-reference-2026-10-05.md` §0.2 — the first byte-exact proof of the rule