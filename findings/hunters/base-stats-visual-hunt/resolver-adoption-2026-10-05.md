# Resolver adoption audit — does any PUBLISHED finding depend on the broken resolver?

**Question asked:** re-derive, with the hardened segment-aware resolver
([`resolve-literals-segment-aware.py`](resolve-literals-segment-aware.py)), every
string-literal claim in the Blustone research corpus that could have come from
the old resolver ([`tools/resolve-literals-offline.py`](../../../../Blustone-Instrumented/tools/resolve-literals-offline.py),
defects D1–D6 in [`resolver-hardening-2026-10-05.md`](resolver-hardening-2026-10-05.md)),
and decide whether any published conclusion changes.

**Answer: NO published conclusion changes.** Zero key lists needed correction.
Every published list that the new resolver could re-derive came back
**byte-identical**, and the three lists it could **not** re-derive were checked
against **Ghidra's own decompile addends** and found **correct as published**.

What this run *did* find is four defects **in the hardened resolver itself**
(N1–N4 in §5), two of which bite at its **default settings** on literals that
reports already publish. Those are findings about the tool, not about the
corpus, and they mean the new tool **must not be adopted as a key-list
generator** — it is safe as a *gated re-derivation check* and as a *candidate
generator*, which is the role the published lists already fill.

**Read-only compliance.** `analysis/extracted/lib/armeabi-v7a/libnative_core.so`
opened read-only and unmodified. **No Ghidra project opened.** No server-ts,
fixture, APK, seed, emulator or phone action. Only **one** workspace write: this
file. **No existing file modified.** `polluted-observations.md` deliberately
**not** appended. Helper scripts lived in the OS temp directory.

**Coverage unchanged** and irrelevant: heroes **1/113**, accessories **1/100**,
monsters **0/22**. Nothing here is a hero, accessory or monster statistic.

---

## 1. PURE — method: Ghidra's own addends are the arbiter

The whole disagreement class in this audit is one question: **which `add <Rn>,pc`
belongs to which `ldr`?** A structural scanner has to guess; the decompiler
already knows.

Ghidra prints a PC-relative string reference as

```
(char *)(DAT_<slot> + 0x<addend>)          addend = (add_insn & ~1) + 4
```

and its **dataflow has already chosen the pairing**. Recomputing
`w = u32(slot)`, `target = w + addend` and reading `target` therefore reproduces
the string *without guessing anything*. That is the ground truth both tools
approximate, and it was used here for every disputed site.

Three independent confirmations that the pairing is positional, not semantic:

* the **slot word is always identical** between the dump and the new resolver
  (same `slot=`, same `w=`). Only the addend differs;
* the new resolver's wrong answers are **mid-string fragments**
  (`'nus'` out of a longer word, `'re/Reward'`, `'ORS'`, `'ION__'`, `'d()'`,
  `'p'`) — the signature of an address 4–10 bytes off, never of a different
  literal;
* the correct answers are **whole field/UI names** (`level`, `price_type`,
  `UI_SHOP_GOOD`, `READY`, `IG_READY`, `itr != m_mEffectRoot.end()`).

Address conventions follow `resolver-hardening-2026-10-05.md` §1.1 and are
labelled throughout: **Ghidra = ELF VA + 0x10000**; `analysis/ghidra-*.txt`
dumps are in **Ghidra**; the new tool's internal space is **ELF VA**.

The new resolver's own gate passed before any work: **23/23**, with the `D1`
negative guard rejecting the documented `.got` `'X'` site
(ELF `0x00f489e6` → target `.got`, RW-).

---

## 2. Priority target 1 — gem price-row key lists

### 2.1 Verdict per parser

| parser (Ghidra addr) | published list | old resolver | new resolver (default) | new resolver `--window 16` | verdict |
|---|---|---|---|---|---|
| `ParseGemRefs` `0x00a535e8` | `id, name, desc, res_id, set_effect_id, rank, target` (+`ret_data`) = 8 | 5 | **8/8 exact** | 8 | **VERIFIED** |
| `ParseGemCombineEffects` `0x00a53a90` | `id, count` (+`ret_data`) = 3 | **0** | **3/3 exact** | 3 | **VERIFIED** |
| `ParseGemSellPrices` `0x00a53e50` | `rank, level, price_type, price` (+`ret_data`) = 5 | 1 (wrong) | 3 exact, **2 wrong** | 4 exact, 1 wrong | **DISAGREES — new tool wrong, published list CORRECT** |
| `ParseGemLevelUpPrices` `0x00a54108` | `level, price_type, price, possibility, failed_compensation, add_sub_ability` (+`ret_data`) = 7 | 5 | **7/7 exact** | 7 | **VERIFIED** |
| `ParseGemDisassemblePrices` `0x00a54528` | `level, price_type, price` (+`ret_data`) = 4 | 1 | 3 exact, **`level` REJECTED** | **4/4 exact** | **FALSE NEGATIVE at default — published list CORRECT** |
| `ParseGemInsts` `0x00a5c090` | `ret_data` = 1 | — | **1/1 exact** (self-test) | 1 | **VERIFIED** |
| `CSRGem::parse` `0x00a5d3dc` (instance row) | `ref_id, inst_id, rank, level, position, target_inst_id, ability, abilities, level_up_failed, main, sub` = 11 | 9 | **11/11 exact** (self-test) | 11 | **VERIFIED** |
| `GetSetEffectDesc` `0x00a5f97c` | `" "` = 1 | — | **1/1 exact** (self-test, 1-byte R1) | 1 | **VERIFIED** |

`analysis/ghidra-gem-reference-keys.txt` re-derivation with
`--from-dump`: **24 matched, 3 rejected-or-differing, total 27**.
`analysis/ghidra-gem-inventory-keys.txt`: **13/13** (part of the gate).
Per-function `--function` counts for the reference parsers:
`5/8`, `0/3`, `1/4`, `5/7`, `1/3` old → `8`, `3`, `4`, `7`, `3` new at
window 12 (`4` for the last at window 16).

### 2.2 DISAGREEMENT 1 — `ParseGemSellPrices`: two keys re-derived as mid-word fragments

Instruction stream (Ghidra):

```
0x00a53efa  7f48   ldr r7,[pc,#0x1FC] -> slot 0x00a540f8
0x00a53efc  0df1.. mov.w
0x00a53f00  7e4e   ldr r6,[pc,#0x1F8] -> slot 0x00a540fc
0x00a53f02  0df1.. mov.w
0x00a53f06  7844   add r0,pc        <-- addend 0x00a53f0a
0x00a53f08  7d4d   ldr r5,[pc,#0x1F4] -> slot 0x00a54100
0x00a53f0a  7e44   add r6,pc        <-- addend 0x00a53f0e
0x00a53f0c  8046   mov r0,r8
0x00a53f14  7d44   add r5,pc        <-- addend 0x00a53f18
```

Ghidra's decompile (`ghidra-gem-reference.txt:770-772`) states the pairing
explicitly and it is the **load at gap 10 and gap 12**, not the first add:

```
pcVar7  = (char *)(DAT_00a540f8 + 0xa53f0a);   -> 'rank'
pcVar14 = (char *)(DAT_00a540fc + 0xa53f0e);   -> 'level'
pcVar13 = (char *)(DAT_00a54100 + 0xa53f18);   -> 'price_type'
```

| load | Ghidra add instr | addend | published string | new resolver picks | new resolver says |
|---|---|---|---|---|---|
| `0x00a53efa` | `0x00a53f06` | `0x00a53f0a` | `rank` | `0x00a53f06` ✓ | `rank` ✓ |
| `0x00a53f00` | `0x00a53f0a` | `0x00a53f0e` | **`level`** | `0x00a53f06` ✗ | **`'nus'` @ `0x01d6fec9`** |
| `0x00a53f08` | `0x00a53f14` | `0x00a53f18` | **`price_type`** | `0x00a53f0a` ✗ | **`'re/Reward'` @ `0x01d72a94`** |
| `0x00a54018` | `0x00a5401e` | `0x00a54022` | `price` | `0x00a5401e` ✓ | `price` ✓ |

**`gem-reference-contract.md` §"Price-row fields" line 65 (`SellPrice: rank,
level, price_type, price`) is CORRECT. The new resolver is wrong on two of the
four.** The published list is unchanged; the tool is at fault.

`'nus'` is the tail of a longer `.rodata` word and `'re/Reward'` the tail of a
route-like string — neither can be a JSON key. Cause: **N2** (§5).

### 2.3 REGRESSION — `ParseGemDisassemblePrices`: `level` lost at the default window

```
0x00a545c4  ldr r6,[pc,#...]  -> slot 0x00a54800
   ... 3 intervening instructions ...
0x00a545d2  7844  add r0,pc    -> addend 0x00a545d6 -> 0x01d6fecd 'level'   gap = 14
```

`--from-dump` prints `REJECT ldr@0x00a545c4  no pair`.
`--function 0xa54528:0xa54620 --window 16` recovers it:
`ldr@0x00a545c4 r6 gap=14 slot=0x00a54800 w=0x0131b8f7 -> 0x01d6fecd 'level'`.
Ghidra's decompile addend `0x00a545d6` confirms it independently.

**This is a real key, published at `gem-reference-contract.md` line 67, that the
new resolver loses at its default settings.** Cause: **N1** (§5).

---

## 3. Priority target 2 — the IG_WAVE totals 2/3/4 finding

### 3.1 `InitEffect` — 48/48 exact, and the set is COMPLETE

`--from-dump analysis/ghidra-search-effect-root-keys.txt`, `InitEffect` section:
**48 of 48 OK**, every target address and every string byte-identical.

A complete structural scan of the whole function range is stronger than the
dump, because it can find literals the dump omitted:

```
python resolve-literals-segment-aware.py --function 0x009c33c4:0x009c6e00
-> resolved: 48        (old resolver over the same range: 39)
```

The scan returns **exactly** the dump's 48 and **nothing more**. Every
`InitEffect` pair is at **gap 2 or 10**, so it is exactly the layout where
positional pairing is safe.

The nine the old resolver missed are the three `IG_WAVE%s_%s` sites at gap 8
and six gap-10 effect keys (`FX_ATK_S`, `FX_ATK_P`, `FX_ATK_F`, `FX_CHANGE`,
`FX_CLASH`, `FX_WARNING`).

### 3.2 The IG_WAVE claim is STRENGTHENED, not weakened

`search-effect-root-contract.md` §"No-input contradiction" claims InitEffect
registers **no total-1 wave banner**, so a one-wave Search group requests the
unregistered `IG_WAVE1_1`. Two independent checks:

1. **Whole-function literal set.** Exactly three `IG_WAVE%s_%s` literals in
   InitEffect — `0x009c6a82`, `0x009c6bf6`, `0x009c6d56`, all resolving to
   `0x01d757b9`, all reproduced exactly. No fourth site, no other wave format.
2. **Whole-library string table.** `IG_WAVE` appears only four times in
   `analysis/native-all-strings.tsv`: `IG_WAVE%s_%s` @`0x01d757b9`,
   `IG_WAVE%d_%u` @`0x01d75c72`, `IG_WAVE` @`0x01d75c7f`,
   `TX_IG_WAVE` @`0x01d7803b`. **There is no hard-coded `IG_WAVE1_1` string
   anywhere in the binary.** The one-wave family therefore cannot be
   registered, which is the published conclusion.

The automatic requester literal is also confirmed at the published address:
`IG_WAVE%d_%u`, `ldr@0x009ceaae`, `slot 0x009cedf4` — exactly as
`search-effect-root-contract.md` line 39 states. The boss effect is confirmed
too: `EF_CH`, `ldr@0x00908146`, `slot 0x009081f0` (gap 6, so **only** the new
resolver finds it).

The *totals* 2/3/4 themselves come from loop bounds in the decompile, not from
literals, so no resolver touches them.

### 3.3 One new candidate key — UNVERIFIED, do not promote

The new resolver surfaces a literal no report lists:

```
ldr@0x009ceb00 r6 gap=6 slot=0x009cedfc w=0x013a7175 -> 0x01d75c7f 'IG_WAVE'
```

A bare `IG_WAVE` prefix in `OnProcWaveChange`, adjacent to `IG_READY`
(`0x01d75c91`) and `IG_WAVE%d_%u` (`0x01d75c72`). Given N2 the **pairing itself
is unproven** — it may belong to a later `add`. **Do not cite this as a
recovered key** until a Ghidra read of `0x009ceb00`'s consumer confirms it.

### 3.4 DISAGREEMENT — `ShowEffect`: 4 of 5 assertion literals mis-re-derived

`ShowEffect` (`0x009db7b0`) hoists its loads and then emits its adds:

```
0x009db834  ldr r1 -> slot 0x009db97c
0x009db836  ldr r2 -> slot 0x009db980
0x009db838  ldr r2 -> slot 0x009db984
0x009db83c  ldr r2 -> slot 0x009db988
0x009db840  ldr r2 -> slot 0x009db98c
0x009db83a  7944  add r0,pc   addend 0x009db83e
0x009db83e  7e44  add r1,pc   addend 0x009db842
0x009db842  7a44  add r2,pc   addend 0x009db846
0x009db844  7944  add r1,pc   addend 0x009db848
0x009db846  7944  add r1,pc   addend 0x009db84a
```

Ghidra's addends (`ghidra-search-effect-root.txt`) give the true mapping, and it
is **not** first-add-forward:

| load | Ghidra add instr | published string | new resolver | old resolver |
|---|---|---|---|---|
| `0x009db834` | `0x009db83a` | `_"[AST] [%s]", __FUNCTION__` ✓ | ✓ | missed |
| `0x009db836` | `0x009db83e` | **`itr != m_mEffectRoot.end()`** | `'ORS'` | `'ORS'`-class miss |
| `0x009db838` | `0x009db842` | **`C:/Users/hkpark/…/SRGameBase.cpp`** | `'nullptr'` | `'nullptr'` ✗ |
| `0x009db83c` | `0x009db844` | **`[AST] [%s]`** | `'ION__'` | `'ION__'` ✗ |
| `0x009db840` | `0x009db846` | **`ShowEffect`** | `'d()'` | `'d()'` ✗ |

**The published dump is CORRECT on all five. The new resolver gets 1 of 5; the
old one got 0 of 5** (it emitted only `nullptr`, `ION__`, `d()`, `)`). Cause:
**N2**.

### 3.5 REGRESSION — `OnProcWaveChange` `READY` / `IG_READY` are lost entirely

`search-effect-root-contract.md` line 55 publishes two more literals here. The
same hoisted pattern, three loads then three adds:

```
0x009cec98  ldr r5 -> slot 0x009cef10
0x009cec9c  ldr r5 -> slot 0x009cef14
0x009ceca0  ldr r5 -> slot 0x009cef18
0x009ceca2  add r4,pc   addend 0x009ceca6
0x009ceca4  add r1,pc   addend 0x009ceca8
0x009cecac  add r3,pc   addend 0x009cecb0
```

Direct slot arithmetic confirms the published pairings exactly:

```
slot 0x009cef14 + add@0x009ceca4 -> 0x01d75691 'READY'
slot 0x009cef18 + add@0x009cecac -> 0x01d75c91 'IG_READY'
```

The new resolver over `0x009cec90:0x009cecd0` at window 12 **and** at window 16
returns **one** result, and it is the wrong one: `ldr@0x009ceca0 gap=2 -> 'from_wave'`.
`READY` and `IG_READY` are **silently dropped**, because `scan()` `break`s at the
first load-shaped instruction in the backward window and the `seen` set then
blocks the correct ones. Cause: **N3** (§5).

---

## 4. Priority target 3 — `trace-recruitment-contract.md`

`--from-dump analysis/ghidra-trace-exchange-keys.txt`: **29 matched, 1 differing,
total 30**. Every load-bearing claim in that report is re-derived exactly:

| published claim | new resolver | verdict |
|---|---|---|
| route `/shop/PieceExchange` (`slot Gf8ac4c`) | `ldr@0x00f8ab66 slot=0x00f8ac4c -> 0x01d90274` | **VERIFIED** |
| form key `app_code` | `ldr@0x00f8a8c6` ✓ | **VERIFIED** |
| form key `app_ver` | `ldr@0x00f8a8f0` ✓ | **VERIFIED** |
| form key `market` | `ldr@0x00f8a90e` ✓ | **VERIFIED** |
| form key `pvid` | `ldr@0x00f8a93c` ✓ | **VERIFIED** |
| form key `otp` | `ldr@0x00f8a968` ✓ | **VERIFIED** |
| form key `item_inst_id` (`ADD Gf8a9f0` / `slot Gf8ac44`) | `ldr@0x00f8a9ee slot=0x00f8ac44` ✓ | **VERIFIED** |
| form key `cnt` (`ADD Gf8aa18` / `slot Gf8ac48`) | `ldr@0x00f8aa16 slot=0x00f8ac48` ✓ | **VERIFIED** |
| `ret_data` (`ADD Gf8b04e` / `slot Gf8b2d4`) | `ldr@0x00f8b04c slot=0x00f8b2d4` ✓ | **VERIFIED** |
| `achievement` (`ADD Gf8b066` / `slot Gf8b2d8`) | `ldr@0x00f8b062 slot=0x00f8b2d8` ✓ | **VERIFIED** |
| `card` (`ADD Gf8b080` / `slot Gf8b2dc`) | `ldr@0x00f8b07e slot=0x00f8b2dc` ✓ | **VERIFIED** |
| `consumed_inst_list` (`ADD Gf8b248` / `slot Gf8b4a4`) | `ldr@0x00f8b246 slot=0x00f8b4a4` ✓ | **VERIFIED** |
| `result_code` | `ldr@0x00f8afe6` ✓ | bonus, not claimed |

The **single** disagreement in the file is a UI node name the report quotes at
line 50:

```
DIFFER ldr@0x00ce26b2 slot=0x00ce2a00 w=0x0109ccf7 -> 0x01d7f3b1 'p'
       [dump: 0x01d7f3b3 'UI_SHOP_GOOD']
```

Same hoisted pattern (`ldr@0x00ce26ae`, `ldr@0x00ce26b2`, then
`add@0x00ce26b6`, `add@0x00ce26b8`); Ghidra pairs the second load with the
second add ⇒ `0x01d7f3b3 'UI_SHOP_GOOD'`. **Published value CORRECT**; the old
resolver produced the same `'p'`. Cause: **N2**.

**Consequence for the trace contract: none.** The route, the 7 form keys, the
4 response keys, the `card`-as-array shape and the `UseItem` `inst_id`/`qty`
delta reading are all literal-independent of the defects, so
`trace-recruitment-contract.md` — and the `server-ts` implementation derived
from it — need no change.

`analysis/ghidra-trace-lobby-achieve-keys.txt`: **3/3** (`dailyquest_min_stage`,
`daily_quest`, `linear_quest`) — VERIFIED.

---

## 5. Four NEW defects in the hardened resolver

These are reported because adopting the tool as-is would repeat exactly the
failure mode it was written to prevent (AGENTS.md §16.7: *"it sends a real
client a response keyed on a field that does not exist"*).

### N1 — the default `--window 12` is one gap short *(false negative, hits published keys)*

The default was chosen because the largest gap in the two ground-truth dumps is
10. Two **real, already-published** keys sit at **gap 14**:

| key | load | add | gap | default | `--window 16` |
|---|---|---|---|---|---|
| `level` (`ParseGemDisassemblePrices`) | `0x00a545c4` | `0x00a545d2` | **14** | `REJECT no pair` | recovered |
| `season_no` (`ParseSeason`) | `0x00942e34` | `0x00942e42` | **14** | absent | recovered |

`sunday-settlement-2026-10-05.md` §1.1 publishes all **8/8** `ParseSeason`
literals. At the default window the new resolver returns **7** and silently
loses `season_no`:

```
--window 12 -> 7   (no season_no)
--window 16 -> 8   ldr@0x00942e34 gap=14 slot=0x009430d8 -> 0x01d7331e 'season_no'
```

The hardening report's §1.7 already warned *"NOT PROVED — completeness"*; this
is the concrete instance, and it means **the default is not safe for adoption**.

### N2 — forward-first-`add` mispairs hoisted load blocks *(false positive, hits published keys)*

`find_add_pc()` walks **forward** from the load and returns the **first**
`add <Rn>,pc` in the window. When the compiler hoists several `ldr`s ahead of
several `add`s, that pairs the *n*-th load with the *1*-st add. Demonstrated in
**four** places, always with a mid-word fragment as the output:

| site | published | new resolver | old resolver |
|---|---|---|---|
| `0x00a53f00` | `level` | `'nus'` | missed |
| `0x00a53f08` | `price_type` | `'re/Reward'` | `'re/Reward'` |
| `0x00ce26b2` | `UI_SHOP_GOOD` | `'p'` | `'p'` |
| `0x009db838` | `C:/Users/hkpark/…` | `'nullptr'` | `'nullptr'` |
| `0x009db83c` | `[AST] [%s]` | `'ION__'` | `'ION__'` |
| `0x009db840` | `ShowEffect` | `'d()'` | `'d()'` |

This class is **pre-existing** in the old tool — widening the window is **not**
its cause. But widening **does** add one new false positive the old strict
window could not reach (`'nus'`, gap 6). **Net: D5's widening traded a false
negative for a false positive in this layout.**

Register matching is *not* a safe fix, and the evidence says so: the ground
truth contains `ldr r2` paired with `add r0,pc` (`AddStageMonster`, per the
hardening report's own `is_add_pc` docstring) and `ldr r7` paired with
`add r0,pc` (`ParseGemSellPrices`). The honest remedy is to **not guess** — read
the addend from Ghidra, i.e. use `--from-dump` on a Ghidra-derived dump, as the
published lists already do.

### N3 — `scan()` breaks at the first load in the backward window *(false negative, hits published keys)*

Already flagged as a limitation in the hardening report §1.7. It is not
hypothetical:

* `OnProcWaveChange 0x009cec90..0x009cecd0`: 3 loads, **1** result, and that one
  wrong. `READY` and `IG_READY` are lost entirely (§3.5).
* `ParseGemSellPrices --function 0xa53e50:0xa54110`: `rank` is **absent** at
  both window 12 and 16, because the walk from `add@0x00a53f06` finds the load
  at `0x00a53f00` first and `break`s before reaching `0x00a53efa`.

A `--function` count is therefore **not** a key count. Only `--from-dump` (which
starts from the load, not the add) is.

### N4 — `--from-dump` reports `DIFFER` without adjudicating

`--from-dump` re-derives the load and the target but pairs them with the first
add (N2), then compares against the dump and prints `DIFFER`. It has no way to
state *"the dump's add is the right one"*; only the human caller can. Its
`matched:` figure is therefore a **string/target metric under the tool's own
pairing rule**, not an acceptance verdict. In this audit it flagged **8**
genuine publications as `DIFFER`/`REJECT` (3 gem-reference, 4
search-effect-root, 1 trace-exchange) — and in **8 of 8** the dump was right.

---

## 6. Other `[RECOVERED]` key lists in `analysis/research/base-stats-visual-hunt/`

| report | claim | new resolver | verdict |
|---|---|---|---|
| `grouprankup-sellcard-bodies-2026-10-05.md` §1.1 `RequestGroupRankUp` | 11 rows incl. `otp`, `price` | **11 exact**, `otp` at `0x00f587ba` gap 6 ✓ | **VERIFIED** |
| same §1.2 `ReqGroupRankUpCB` | 16 | **16 exact** | **VERIFIED** |
| same §1.3 `RequestSellCard` | 7 incl. `inst_id_list` @`0x01d78609` | **7 exact** | **VERIFIED** |
| same §1.4 `ParseSellCard` | 8 incl. `ref_id`/`added` | **8 exact** | **VERIFIED** |
| `gem-popup-bindings-2026-10-05.md` §1.6 `/gem/LevelUp` request | 7 keys + route | **8 exact** incl. `max_tries` @`0x01d78620` and route @`0x01d7862a` | **VERIFIED** |
| `gem-levelup-action-2026-10-05.md` §1.2 | same 7 keys | **8 exact** | **VERIFIED** |
| `sunday-settlement-2026-10-05.md` §1.1 `ParseSeason` | 8 | 7 at default, **8 at `--window 16`** | **N1 false negative; published list CORRECT** |
| same §1.1 `ParseUser` | 11 named keys + `user/ap/ap_charge_time/bp/bp_charge_time/achievement` | all recovered, exact | **VERIFIED** |
| same §1.1 `ParseEnter` `is_weekly_reward` | `ldr@00942d78`, `slot 0x942e1c` → `0x1d732f4` | **exact**, plus `arena/status/season/battle/user/deck` | **VERIFIED** |
| `batch-rankup-chucoin-2026-10-05.md` §1.2.1 | cites `inst_id_list` + `ParseSellCard` fields | covered by the two rows above | **VERIFIED** |
| `rewards-economy-2026-10-05.md` §B.4 | trace exchange mechanics | covered by §4 | **VERIFIED** |
| `grouprankup-sellcard-bodies-2026-10-05.md` §2 `[RECOVERED]` constants | 12 struct/encoding constants | **not literal claims** — instruction immediates and offsets | unaffected |

The hardening report's own §1.6 claim (exact reproduction of those four
`grouprankup` tables) is independently **confirmed** here.

`hunter-trace-item-binding.md`'s `use_type3` / `collect_qty` claim is an
**INFO-struct offset** observation (`+0x20`, `+0x28`), not a literal pairing, and
is therefore outside the resolver's scope entirely.

---

## 7. Regression / correction ledger

Counted against **published conclusions**, not against raw old-resolver output.

### REGRESSED — real published keys the new resolver loses at default settings (2)

| # | key | where | cause | recovered with |
|---|---|---|---|---|
| R1 | `level` | `ParseGemDisassemblePrices`, load `0x00a545c4` | N1 (gap 14) | `--window 16` |
| R2 | `season_no` | `ParseSeason`, load `0x00942e34` | N1 (gap 14) | `--window 16` |

### REGRESSED — real published literals the new resolver mis-derives (9)

| # | published value | load | new resolver says | cause |
|---|---|---|---|---|
| R3 | `level` | `0x00a53f00` | `'nus'` | N2 |
| R4 | `price_type` | `0x00a53f08` | `'re/Reward'` | N2 |
| R5 | `UI_SHOP_GOOD` | `0x00ce26b2` | `'p'` | N2 |
| R6 | `itr != m_mEffectRoot.end()` | `0x009db836` | `'ORS'` | N2 |
| R7 | `C:/Users/hkpark/…/SRGameBase.cpp` | `0x009db838` | `'nullptr'` | N2 |
| R8 | `[AST] [%s]` | `0x009db83c` | `'ION__'` | N2 |
| R9 | `ShowEffect` | `0x009db840` | `'d()'` | N2 |
| R10 | `READY` | `0x009cec9c` | **dropped** | N3 |
| R11 | `IG_READY` | `0x009ceca0` | **dropped** | N3 |

**In all 11 cases the published value is the correct one** — adjudicated against
Ghidra's own addends (§2.2, §3.4) or by direct slot+addend arithmetic (§3.5,
§4). **No published conclusion changes. No server response shape, route,
request key or reference row needs revision.**

### CORRECTED — false positives that are now absent (1)

| # | value | old resolver only | note |
|---|---|---|---|
| C1 | `')'` @`0x01d75b93` | `ShowEffect` | never published; a 5th wrong pairing in the same hoisted block |

The tooling reports' own `'X'` (`.got` address-of-a-global) remains rejected by
D1 — the self-test's negative guard passes, so **D1 removes nothing any report
depends on**. A grep of the ten documented `.got` rejection targets across
`analysis/**/*.md` finds them only inside
`resolver-hardening-2026-10-05.md` and
`grouprankup-sellcard-bodies-2026-10-05.md`, both citing them **as false
positives**.

### VERIFIED EXACTLY — no change (all remaining key lists)

`ParseGemRefs` 8 · `ParseGemCombineEffects` 3 · `ParseGemLevelUpPrices` 7 ·
`ParseGemInsts` 1 · `CSRGem::parse` 11 · `GetSetEffectDesc` 1 ·
`InitEffect` 48 · `RequestGroupRankUp` 11 · `ReqGroupRankUpCB` 16 ·
`RequestSellCard` 7 · `ParseSellCard` 8 · `/gem/LevelUp` request 8 ·
`ParseUser` 11+6 · `ParseEnter` 7 · trace exchange 12+1 ·
trace lobby 3 · both gate dumps 20/20.

### Why nothing regressed in the corpus

Because **no published key list was ever a raw structural-scan artifact.** The
old resolver's recall on the audited ranges was `5/8`, `0/3`, `1/5`, `5/7`,
`1/4`, `0/8`, `39/48` — it could not have produced those lists. They came from
Ghidra dataflow plus hand assembly, which is why the addends are right. The
resolver was always a *check*, never the *source*. **This audit changes the
tool's status, not the corpus's.**

---

## 8. Numeric tokens touched by this pass (none is data)

Recorded per the §2.3 rule rather than in `polluted-observations.md`, which this
run does not append to.

| token | value | where | what it is |
|---|---|---|---|
| max observed load→add gap | **14** | `ParseGemDisassemblePrices`, `ParseSeason` | structural encoding distance |
| default `--window` | 12 | new resolver | tool parameter, now known too narrow |
| `--window` needed | 16 | this audit | tool parameter |
| ground-truth gap range | 2, 4, 6, 8, 10, **14** | 5 functions | structural |
| `IG_WAVE%s_%s` / `IG_WAVE%d_%u` | literal spellings | effect-name formats | code, not values |
| `max_tries` | 7 | `/gem/LevelUp` request | already published elsewhere; re-confirmed, **not** re-derived here |

None of these is a balance, stat or economy value. **Do not promote any row
above into a server default.**

---

## 9. What a follow-up should do

1. **Do not adopt `--window 12`.** Make it **16** (or take it per-site and
   record the value used). The ground-truth set now contains two gap-14 sites.
2. **Adopt the tool only for two roles**, both of which it does well:
   * a **gated re-derivation check** of an existing Ghidra-derived dump
     (`--from-dump`), reading `DIFFER` as *"the pairing is contested"* and not
     as *"the report is wrong"* — 8 of 8 such flags in this audit went the other
     way;
   * a **candidate generator** whose output is confirmed against Ghidra dataflow
     before publication.
   It is **not** a key-list generator: N2 and N3 make that unsafe.
3. **Do not re-derive** `ShowEffect`'s assertion strings, `ParseGemSellPrices`,
   `OnProcWaveChange`'s `READY`/`IG_READY`, or `ShardExchangeConfirm`'s
   `UI_SHOP_GOOD` from a structural scan. Keep the published values; they are
   adjudicated correct.
4. **Retire `tools/resolve-literals-offline.py`** (hardening report §3 item 2).
   This run strengthens the case: it also produced `'p'`, `')'`,
   `'re/Reward'`, `'nullptr'`, `'ION__'`, `'d()'` and `')'` — every one false —
   while returning `0` for two whole published parsers.
5. **Resolve N3 first** if the tool is to be fixed: walk every load-shaped
   candidate in the window instead of breaking at the first. Then re-measure the
   false-positive rate before trusting the extra hits, exactly as the hardening
   report's own §3 item 3 advises.
6. **Do not cite the bare `IG_WAVE` candidate** (§3.3) without a Ghidra read of
   `0x009ceb00`'s consumer.
7. **No `server-ts` change follows from this audit.** The only open item is
   `sunday-settlement`'s `season_no`, which the replica already handles from
   the arena contract, not from a literal scan.

---

## 10. Provenance

**Commands run** (all read-only, all from the workspace root):

```
resolve-literals-segment-aware.py --self-test                    23/23 PASS
resolve-literals-segment-aware.py --from-dump analysis/ghidra-gem-reference-keys.txt        24 / 3 / 27
resolve-literals-segment-aware.py --from-dump analysis/ghidra-gem-inventory-keys.txt        13 / 0 / 13  (gate)
resolve-literals-segment-aware.py --from-dump analysis/ghidra-search-effect-root-keys.txt  49 / 4 / 53
resolve-literals-segment-aware.py --from-dump analysis/ghidra-trace-exchange-keys.txt      29 / 1 / 30
resolve-literals-segment-aware.py --from-dump analysis/ghidra-trace-lobby-achieve-keys.txt   3 / 0 / 3
resolve-literals-segment-aware.py --function <ranges>  [--window 12|16]
tools/resolve-literals-offline.py    --function <ranges>
```

**Ground truth source.** `analysis/ghidra-gem-reference.txt`,
`analysis/ghidra-gem-inventory.txt`, `analysis/ghidra-search-effect-root.txt`
— the Ghidra decompile text already in the workspace, read as
`DAT_<slot> + 0x<addend>`. The original ELF was used only to read the slot
words, the instruction halfwords and the target bytes. `llvm-objdump` in this
workspace decodes the library as **ARM**, not Thumb, so its output was **not**
used; a read-only halfword classifier was used instead, and every disputed site
was additionally confirmed by the decompiler's own addend.

**Not touched.** No Ghidra project. `libnative_core.so` unmodified.
`tools/resolve-literals-offline.py` left intact so both tools remain
comparable. `polluted-observations.md` not appended. No existing report edited —
this file is the only write.