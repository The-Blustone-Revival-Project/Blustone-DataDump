# LEVELDATA-ID-SOURCE — what string forms the `<id>` in `"<id>.JSON"`?

Narrow native-analysis lane, 2026-10-02.
Scope: `CSRLevelData::LoadLevelData` (`0xa178c4` Ghidra), its callers, and
`CSRLevelData::GetMonsterGroupID` (`0xa1bff8`).

**Address space used throughout: Ghidra image addresses.** Verified independently
of `ADJUDICATION-crash-site.md` in this session: ELF type is `ET_DYN` (`e_type=3`)
with first `PT_LOAD off=0x00000000 vaddr=0x00000000`, and
`file_offset + 0x10000 == ghidra_addr` reproduces the prologue halfword
`0xb5f0` (`push {r4-r7,lr}`) at Ghidra `0xa178c4`. `b'leveling_m\0'` is at file
`0x1d6b107` = Ghidra `0x1d7b107`, matching `analysis/native-all-strings.tsv`.
**No conflict with the adjudication is claimed** — this note does not revisit the
crash site.

**Headline:** the `<id>` is a **compile-time string literal**, `"leveling_m"`.
It is not read from any server response. Both candidate hypotheses in
`ADJUDICATION-crash-site.md` §4 are **refuted**.

---

## Q1 — What expression becomes the filename? **[RECOVERED]**

### The call chain

`CSRMStage::InitBeforeOpen` — Ghidra `0xb33ccc`, i.e. the **expedition/mission**
scene (the same class whose `MakeStageInst` is `0xb33f84`, the adjudicated crash
site). Instruction listing (`analysis/ghidra-leveldata-insn-01.txt`):

```
00b33ce6  bl 0x008b3390          ; CSRDataMgr::get()
00b33cea  ldr r2,[0x00b33f6c]     ; literal-pool slot
00b33cec  mov r1,r0              ; r1 = CSRDataMgr singleton
00b33cee  add r0,sp,#0x4c        ; sret: shared_ptr<CSRLevelData>
00b33cf0  add r2,pc              ; r2 = 'leveling_m'
00b33cf2  bl 0x008b26e4          ; CSRDataMgr::LoadLevelData
```

`analysis/ghidra-leveldata-strings-01.txt` and the inline run of
`tools/resolve-literals-offline.py --function 0xb33ccc:0xb33f84`:

```
ldr@0x00b33cea r2 slot=0x00b33f6c w=0x01247413 add_pc=0x00b33cf4 -> 0x01d7b107  'leveling_m'
ldr@0x00b33d3a r5 slot=0x00b33f70 ... -> '[ERR] [%s] '
ldr@0x00b33d44 r3 slot=0x00b33f74 ... -> 'Cannot find Mission Information'
ldr@0x00b33d6a r3 slot=0x00b33f78 ... -> 'InitBeforeOpen'
ldr@0x00b33d9a r0 slot=0x00b33f7c ... -> 'UI_ROOT'
ldr@0x00b33db0 r3 slot=0x00b33f80 ... -> 'UI'
```

So the literal at slot `0xb33f6c` is `"leveling_m"`. Note the Ghidra decompile
(`analysis/ghidra-enemycamp-decomp-06.txt:38`) prints
`CSRDataMgr::LoadLevelData(acStack_24);` with *no visible argument* — that is a
decompiler artifact: `acStack_24`/`local_20` are the 8-byte **sret**
`shared_ptr<CSRLevelData>` (`_M_ptr` at `sp+0x4c`, `_M_refcount` at `sp+0x50`,
released immediately afterwards at `0xb33cf6`). The real arguments are `r1` and
`r2`.

### The wrapper — `CSRDataMgr::LoadLevelData`, Ghidra `0x8b26e4`

`analysis/ghidra-leveldata-decomp-03.txt:1-74`. This is the **only** caller of
`CSRLevelData::LoadLevelData` in the entire binary
(`analysis/ghidra-leveldata-callers-01.txt`: `from 0x8b276e LoadLevelData`,
2 refs total, one is `0x0`):

```c
/* CSRDataMgr::LoadLevelData(char const*) */
void CSRDataMgr::LoadLevelData(char *param_1)
{
  CSRLevelData *pCVar2 = operator_new(0x300);
  CSRLevelData::CSRLevelData(pCVar2);
  ...
  std::__ndk1::basic_string<...>::basic_string<decltype(nullptr)>(local_30, in_r2);   // line 51-52
  CSRLevelData::LoadLevelData(pCVar2, (basic_string *)local_30);                     // line 53
  ...
  CSRLevelData::InitDefaultData((CSRLevelData *)*puVar6);                            // line 57
```

`in_r2` is a **register-passed `char const*`**, copied verbatim into a
`std::string`, and that string is the *entire* input to
`CSRLevelData::LoadLevelData`. It is built at the call site from the literal.
**No JSON field, no stage record, no singleton lookup participates.**

### The filename construction — `CSRLevelData::LoadLevelData`, Ghidra `0xa178c4`

`analysis/ghidra-leveldata-decomp-01.txt:304-400`, plus the instruction listing
`analysis/ghidra-leveldata-insn-02.txt` / `-insn-03.txt`:

```c
iVar3 = CGMDataMgr::get();
if (*(char *)(iVar3 + 0x5814) == '\0') {          // decomp-01:310
    /* local branch: no data root configured */
    local_f0 = param_1;                            // "leveling_m"
    SRLoadRawData(&local_c0);                      // local asset tree
    local_e0.assign(local_c0.data(), local_c0.size());
} else {
    local_110 = std::string(*(char **)(iVar3 + 0x5814));   // data-root prefix
    local_f0   = local_110 + param_1;                     // prefix + "leveling_m"
    local_c0   = local_f0 + pcVar20;                       // + ".JSON"
    CMLoadTextRaw(...);                                    // CM database
}
nlohmann::basic_json<...>::parse(local_100, local_e0, aiStack_68, 1, 0);   // decomp-01:400
```

The `.JSON` suffix is a 5-byte literal, confirmed three ways:

```
# resolve-literals-offline.py --function 0xa178c4:0xa18400
ldr@0x00a1792c r5 slot=0x00a17c84 w=0x013586f0 add_pc=0x00a17934 -> 0x01d70024  '.JSON'
```

```
# analysis/ghidra-leveldata-insn-02.txt  (Ghidra 0xa1792c..0xa17940)
00a1792c  ldr r1,[0x00a17c84]
00a17930  add r1,pc
00a1793c  add r0,sp,#0x80
00a1793e  movs r2,#0x5                ; length 5
00a17940  bl 0x006d8430               ; std::string::append
```

`analysis/native-all-strings.tsv` independently lists `01d70024  .JSON`.

**Answer: `<id>` == the literal `"leveling_m"`, and the path is
`<dataRoot>leveling_m.JSON` (or, with an empty data root, `SRLoadRawData("leveling_m")`
from the local asset tree).**

### It is a per-mode compile-time table, not a data-driven name **[RECOVERED]**

`tools/resolve-literals-offline.py --find-string "leveling"` returns 21 sites.
Mapping each onto the function that contains it (via the `MakeStageInst` symbol
list in `analysis/ghidra-enemycamp-strings-13.txt`):

| literal | site (Ghidra) | enclosing scene |
|---|---|---|
| `leveling_s` | `0x008ffee6` | `MakeStageInst` `0x9002b8` |
| `leveling_t` | `0x00905cd2` | `MakeStageInst` `0x90610c` |
| `leveling_r` | `0x00925136`, `0x00a1a62c` | `MakeStageInst` `0x925798` (mirage) |
| `leveling_b` | `0x00941536`, `0x00b94b42` | `MakeStageInst` `0x9418b0` |
| `leveling_g` | `0x00a9445a`, `0x00b94802` | `MakeStageInst` `0xa95060` |
| `leveling_e` | `0x00b23c56` | `MakeStageInst` `0xb23f60` (episode) |
| **`leveling_m`** | **`0x00b33cea`**, `0x00b94df4`, `0x00d1001e`, `0x00e1cba0`, `0x00e7e810`, `0x00e8377c`, `0x00efd972` | **`MakeStageInst` `0xb33f84` (mission — the crash site)** |
| `leveling_raid` | `0x00c3be50` | — |
| `leveling_c` | `0x00f06c32` | `MakeStageInst` `0xf06e50` |
| `leveling_tm` | `0x00f0f3f8` | `MakeStageInst` `0xf0f744` |
| `leveling_te` | `0x00f0f422` | `MakeStageInst` `0xf0f744` |

`_m` is the **mission** mode, matching the adjudicated crash site `0xb33f84`.
The literal is baked into the binary; the game's build-time table selects it by
scene, not by response data.

---

## Q2 — Is the `<id>` derived from a server JSON field? **[RECOVERED: NO]**

**Refuted.** The adjudication's `[inferred-and-unverified]` link to the stage
record's `.value` / `.res_prefix` is **wrong**, and must not be shipped.

Evidence, in order of strength:

1. **`r2` is a literal at the call site** (`0xb33cea: ldr r2,[0x00b33f6c]`,
   `0xb33cf0: add r2,pc`), and the wrapper `0x8b26e4` copies `in_r2` into a
   `std::string` and passes it as the sole argument (`decomp-03.txt:51-53`).
   There is no load from `ret_data`, no member read, no call between the literal
   and the string.
2. **`CSRLevelData::LoadLevelData` reads `param_1` only to build a filename** and
   then immediately `json::parse`s the *file contents*. It never writes `param_1`
   back into `this`, so the id cannot round-trip through any structure that a
   response could have filled.
3. **Negative structural check:** `analysis/ghidra-leveldata-strings-01.txt`
   (54 literal loads in `0xa178c4:0xa19000`) contains **no** `value`,
   `res_prefix`, `id`, or `stage` literal. So the parsed level object does not
   even carry an id field.

`value: 0` and `res_prefix: ""` in `server-ts/src/bootstrap.ts` are therefore
**not the cause** and changing them will not move the crash. (They are still
unverified *as stage-record fields* — see "open items".)

---

## Q3 — Does `/reference/GetLevel` feed this path? **[RECOVERED: NO]**

**Definitively no.** Three independent lines:

**1. Key sets are disjoint.** `CSRLevelData::LoadLevelData` reads 54 literal
loads → 37 distinct keys, all of them enemy-AI / movement / SP / fever
tuning (`analysis/ghidra-leveldata-strings-01.txt`):

```
left, right, run_accl, actor, def_backend_bb, atk_range_scl, waiting,
idle_time, run_spd, walk_spd, fall_spd, emergency_by_remain_time, spawn_y,
ai_exchange_cool, death_time_increase_sp_per_sec,
death_time_increase_atk_ratio, death_time_cond_hp, sp_increase_spd_per_sec,
sp_increase_per_kill, sp_increase_per_atk, sp_increase_per_dmg, sp_max,
fever_increase_per_touch, fever_cooltime, max_fever_point, fever_deceleration,
fever_acceleration, fever_decrease_spd, fever_decrease_cool, normal,
fever_step_cond, fever_step_spd, fever_step_auto_dash,
step_1, step_2, step_3, step_4
```

Tested programmatically against the `AGENTS.md` §6 container names:
`user` **absent**, `vip` **absent**, `vip_group` **absent**, `card` **absent**,
`skill` **absent**, `card_awk` **absent**, `level` **absent**. The word "level"
appears in this function only as part of *`LoadLevelData`'s own name*, never as
a JSON key.

**2. Different data source, structurally.** `AGENTS.md` §6's `GetLevel` rule
describes `CSRUserLV::SetLevel` (`server-ts/src/openapi.ts:384`) — a
**user-progression** table keyed on experience thresholds. That is a different
class from `CSRLevelData`. The `GetLevel` symbols in the binary
(`analysis/ghidra-leveldata-names-01.txt`) are at `0x86a97c`, `0x86da50`,
`0x8f4dd8`, `0x10697cc`, `0x106ad46` — none of them is `0xa178c4`, and none is
called from `CSRMStage::InitBeforeOpen`.

**3. `leveling_m` is not "one of the 54 `level` keys".** The adjudication's
§6 side-note worried that "level keys appear in the same 54". They do not. The
54 keys are AI-parameter names; `user`/`vip`/`card_awk` are progression-table
container names. The overlap is zero.

The load is a **local CM-database / asset-tree read** (`CMLoadTextRaw` /
`SRLoadRawData`), not an HTTP route. There is no HTTP request anywhere in
`0xa178c4:0xa19000`.

---

## Q4 — What is `CSRLevelData::GetMonsterGroupID()`? **[RECOVERED]**

`analysis/ghidra-enemycamp-decomp-02.txt:5724-5750`:

```c
/* CSRLevelData::GetMonsterGroupID() */
void __thiscall CSRLevelData::GetMonsterGroupID(CSRLevelData *this)
{
  DataMemoryBarrier(0x1b);
  if (((*(byte *)(DAT_00a1c068 + 0xa1c004) & 1) == 0) &&
     (iVar1 = __cxa_guard_acquire(DAT_00a1c06c + 0xa1c028), iVar1 != 0)) {
    CMHashID::CMHashID((CMHashID *)(DAT_00a1c070 + 0xa1c036),
                       (char *)(DAT_00a1c074 + 0xa1c038));   // <-- the string
    __cxa_atexit(...);
    __cxa_guard_release(...);
  }
  iVar1 = DAT_00a1c088;
  std::...::basic_string(..., this, (basic_string *)(DAT_00a1c088 + 0xa1c014));
  *(undefined4 *)(this + 0x10) = *(undefined4 *)(iVar1 + 0xa1c024);
  *(undefined4 *)(this + 0x14) = *(undefined4 *)(iVar1 + 0xa1c028);
}
```

The string literal at slot `0xa1c074`:

```
# resolve-literals-offline.py --function 0xa1bff8:0xa1c100
ldr@0x00a1c030 r0 slot=0x00a1c074 w=0x0135b20e add_pc=0x00a1c038 -> 0x01d77246  'enemy'
```

**`GetMonsterGroupID()` returns `CMHashID("enemy")` — a function-local `static`,
initialised once under a `__cxa_guard`, and copied out on every call.**

Two consequences that matter more than the string itself:

- It reads **no member of the parsed level JSON**, and no member of `this`.
  Its result is therefore **invariant**: every `CSRLevelData`, in every mode,
  every stage, returns the same key `"enemy"`.
- Consequently the map keying the camp (`unordered_map<CMHashID, list<list<ACTOR_INFO>>>`
  at `this+0x264` in `CSRMStage`) is a **constant**, not something a
  per-stage id selects. This is why the level-file question and the crash are
  only loosely coupled: a missing or unparsed `leveling_m.JSON` cannot change
  the *key* used at `0xb3507a`, only the *contents* the level data contributes.

---

## The `leveling_*.JSON` file itself — where it lives **[RECOVERED]**

`LEVELING.jet` (18 524 bytes, sha256 `ba73fff1…`) ships in the **base APK**
assets and in the phone snapshot, byte-identical:

```
analysis/extracted/assets/LEVELING.jet                                              18524
recovered-assets/phone-2026-09-18/extracted/split_PADResource/assets/LEVELING.jet   18524
```

Inflated (`tools/jet-viewer`, zlib at offset 24), it is a 22-layer
multi-resource JET. Layer→content map:

| layer | size | content |
|---|---|---|
| 2 | 20 819 | large obfuscated-key table |
| 4 | 261 | small config |
| **6** | **2 113** | **`common` — matches `CSRStaticData::LoadCommon`'s `common`+`.JSON`** |
| 8 | 6 032 | binary |
| 10, 14, 16, 18 | 60…1 294 | small configs |
| **20,22,24,26,28,30,32,34,36,38** | **3 740…4 029** | **10 × `leveling_*` — carry the 37 AI keys above** |
| 40, 42 | 802, 1 444 | `death_box` etc. |

### Control experiment: which lookup path is live? **[RECOVERED]**

`CSRStaticData::LoadCommon` (`0xf39e54`) and `CSRStaticData::LoadEnv`
(`0xf3bab0`) read `common`+`.JSON` and `environments`+`.csv` through the
**identical** `CGMDataMgr+0x5814` two-branch idiom
(`analysis/ghidra-leveldata-decomp-04.txt`; literals `'common'`, `'.JSON'`,
`'environments'`, `'.csv'` recovered). The client demonstrably gets past
`LoadCommon` — the village, Supply and Mail all work. So `common.JSON` is
resolved by whatever mechanism works.

Scanning both trees with the JET decoder:

```
#### SERVED (analysis/runtime-package-full)      # the replica's 11 CDN packages
  common.JSON      -> ABSENT
  leveling_*.JSON  -> ABSENT
  environments.csv -> ABSENT

#### BASE APK assets (analysis/extracted/assets)
  common.JSON      -> LEVELING.jet
  leveling_*.JSON  -> LEVELING.jet
```

`common.JSON` — the file we *know* loads successfully at runtime — is present
**only** in `LEVELING.jet` in the base APK and in **none** of the 11 served
packages. Since `common.JSON` loads, the live resolution path reaches APK-asset
content, and `leveling_m.JSON` sits in the *same* package.

**Therefore `leveling_m.JSON` is already present on the device and is not the
missing piece.** Adding `LEVELING` to `BLUSTONE_PACKAGE_NAMES` is *not* required
to make this file readable, though it may still be worth doing for fidelity.

### The data-root prefix `[UNKNOWN]`

`CGMDataMgr+0x5814` is a `char const*` data-root prefix. Its access form is
confirmed by the instructions at `0xa178ea..0xa178f8` (`analysis/ghidra-leveldata-insn-03.txt`):

```
00a178ea  bl 0x00793aa0        ; CGMDataMgr::get()
00a178ee  movw r1,#0x5814
00a178f4  ldrb r0,[r0,r1]
00a178f6  cmp r0,#0x0
00a178f8  beq 0x00a179ae
```

(MOVW T1 is `hw1 = 1111 0 i 100100 imm4 | hw2 = 0 imm3 Rd imm8` with
`imm16 = imm4:i:imm3:imm8` — halfwords `0xf645 / 0x0114` → `0x5814`. Verified by
byte: file `0xa078ee` = `0xf645`.)

**I could not locate the writer.** An exhaustive scan of `.text` for every
encoding of the immediate `0x5814` (MOVW T1, ADD-immediate T3, LDRB/STRB
imm12) returns only *readers* — the 20 MOVW sites are the same
two-branch idiom in `CSRLevelData::LoadLevelData` (`0xa178ee/f fe`),
`CSRFindShardStage::ReadJson` (`0x90b4ec/fa`), `CSRStaticData::LoadCommon`
(`0xf39e80/8e`), `LoadEnv` (`0xf3bb00/12`), `LoadAnvilStatus` (`0xf3e3aa`) and
three more — and no `str` to that offset. The ADD-immediate hits are all in
regions Ghidra has **not** defined as code (`0x56cb40`…: `DumpInstructions`
returns an empty range). **[UNKNOWN]** — the writer almost certainly computes
the member address through a helper taking a member pointer, or through a
`const char*` setter whose offset is materialised differently. Its *value* at
runtime is not needed for the verdict.

---

## VERDICT

> **The remaining blocker is neither (a) nor (b) as posed.**

Specifically, **not (a)**: the `<id>` is the compile-time literal `"leveling_m"`
selected by scene, not a server field — changing `value: 0` / `res_prefix: ""`
in `server-ts/src/bootstrap.ts` cannot affect this path (Q1, Q2). **Not (b)**
either: the file lives in `LEVELING.jet` in the **base APK assets**, the
byte-identical phone copy is already on disk, `common.JSON` resolves from that
same package at runtime while being absent from all 11 served CDN packages, and
`GetMonsterGroupID()` — the key the camp map is filed under — is the constant
`CMHashID("enemy")` that no missing file can change (Q3, Q4, control experiment).

**What this actually implies.** The adjudication's chain
"level file → monster-group id → empty camp map → null `r1`" has a broken link
in the middle: the key is a constant, so "the map is not populated for the
current stage" cannot be caused by a missing or mis-identified level file. The
population of `CSRMStage+0x264` has to come from the **stage-monster data**
path instead — i.e. `CSRSyncMStage` / `AddStageMonster` (`0xa0d194`) feeding
from `/reference/GetTargetStageMonster`, which `ADJUDICATION-crash-site.md` §3
already confirms is reached unconditionally on `result_code == 1`.

The next decompile to run is therefore **not** another `LoadLevelData` probe. It
is the writer of the camp map: find the `unordered_map<CMHashID, …>::find` /
`operator[]` on `CSRMStage+0x264` inside `CSRMStage::MakeStageInst`
(`0xb33f84`, dumped at `analysis/native-makestageinst.txt`, 520 KB) and the
`AddStageMonster` path that is supposed to insert into it, and determine what
input is absent from our `GetTargetStageMonster` response that leaves the
`list<list<ACTOR_INFO>>` chain uncreated.

Two smaller notes for whoever picks this up:

- `BLUSTONE_PACKAGE_NAMES` does not list `LEVELING`. Adding it is *not* required
  to unblock the crash, but the replica is currently serving a package set that
  omits every `common`/`leveling`/`environments` file, which will bite for other
  `CSRStaticData` consumers eventually.
- `GetLevel`'s `user`/`vip`/`vip_group`/`card`/`skill`/`card_awk` contract in
  `AGENTS.md` §6 is **unaffected** by any of this. Do not re-audit it.

---

## Raw dumps (this session)

| file | contents |
|---|---|
| `analysis/ghidra-leveldata-callers-01.txt` | `ListCallers 0xa178c4` → single caller at `0x8b276e` |
| `analysis/ghidra-leveldata-names-01.txt` | `LoadLevelData` @ `0x8b26e4`, `0xa178c4`; `GetMonsterGroupID` @ `0xa1bff8`; `GetLevel` @ 5 addrs |
| `analysis/ghidra-leveldata-fns-01.txt` | function map `0xa17000..0xa19000` |
| `analysis/ghidra-leveldata-decomp-01.txt` | `CSRLevelData::LoadLevelData` `0xa178c4` (full, 893 KB) |
| `analysis/ghidra-leveldata-decomp-03.txt` | `CSRDataMgr::LoadLevelData` `0x8b26e4`, `CSRDataMgr::get` `0x8b3390` |
| `analysis/ghidra-leveldata-decomp-04.txt` | `CSRStaticData::LoadEnv` `0xf3bab0`, `LoadCommon` `0xf39e54`, `CSRFindShardStage::ReadJson` `0x90b4c4`, `LoadAnvilStatus` `0xf3e358` (all four use the same `CGMDataMgr+0x5814` idiom) |
| `analysis/ghidra-leveldata-strings-01.txt` | 54 Thumb literal loads in `0xa178c4:0xa19000` → `.JSON` + the 37 AI keys |
| `analysis/ghidra-leveldata-insn-01.txt` | `0xb33cc0..0xb33d20` — the `leveling_m` call site |
| `analysis/ghidra-leveldata-insn-02.txt` | `0xa17900..0xa17970` — `".JSON"` append (`movs r2,#5`) |
| `analysis/ghidra-leveldata-insn-03.txt` | `0xa178c4..0xa17902` — prefix branch, `movw r1,#0x5814` |
| `analysis/ghidra-leveldata-insn-04.txt` | `0x56cb10..0x56cba0` — empty (not defined as code) |
| `analysis/ghidra-leveldata-decomp-05.txt` | 36 B stub: `0x56cb40 <no function>` (negative result) |

Method notes for the next agent:

- `tools/resolve-literals-offline.py` was correct throughout and needed no
  changes. Verified its base assumption independently (ELF `PT_LOAD` off=0
  vaddr=0; `file+0x10000 == ghidra`).
- `MoveStageInst`-class **symbol names are ambiguous** — `MakeStageInst` exists
  nine times (`0x9002b8`, `0x90610c`, `0x925798`, `0x9418b0`, `0xa95060`,
  `0xb23f60`, `0xb33f84`, `0xefdb6c`, `0xf06e50`, `0xf0f744`) and `LoadLevelData`
  twice (`0x8b26e4` = `CSRDataMgr::`, `0xa178c4` = `CSRLevelData::`). Always pin
  by address, as the adjudication says.
- `analysis/ghidra-leveldata-wide-01.txt` is 0 bytes — `ResolvePcRelativeStringsWide`
  takes a *name fragment*, not an address; re-run it with `LoadLevelData` if the
  full literal inventory of `0x8b26e4` is ever needed. (Not needed: only literal
  in that function is `'PVID'`.)