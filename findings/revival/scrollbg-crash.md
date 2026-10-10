# `scrollbg-crash.md` — the r015 fault at ELF `0x9aebd7` is a **missing resource**, not a response field

Native-analysis agent, 2026-10-03. Question: `fault=0x1`, `r0=0x1`,
`PC=ELF 0x9aebd7`, `sym=CSRGameScrollBGDraw::OnUpdate`, 5/5 device runs.

**One-line answer:** `CSRGameScrollBGDraw::OnUpdate` dereferences element `[0]`
of a local `std::vector<std::shared_ptr<CMImageNode>>` **without an emptiness
check**. That vector is filled only from children that `CSRGameScrollBGDraw::Load`
attached, and `Load` attaches a child **only when `CMImageNode::LoadAnim`
succeeds**. All 30 background layers failed — the logcat says so, by name, in
`Load`'s own message — so the vector is empty and the first slot read is
uninitialised heap (`1`). **The 30 `LoadAnim2` misses that `report-015` §3.2
withdrew as "pre-existing, orthogonal" are the cause of the crash.** They are not
orthogonal. They are the whole thing.

**And it is not a fixture problem.** No `/reference/*` response field reaches the
resource names that are missing. It is a **CDN/package** problem, and the
`/reference/GetBattle` lead from the brief is **[RECOVERED-negative]**.

---

## 0. FIRST: the brief's address conversion is wrong by one hex digit

`report-015` §2.3 and the task brief both say:

> Ghidra = ELF + `0x10000`, so the crash PC in Ghidra is `0xaaebd7`.

**`0x9aebd7 + 0x10000 = 0x9bebd7`, not `0xaaebd7`.** The correct Ghidra address is
**`0x9bebd7`**. Consequences if uncorrected:

* `Ghidra 0xaaebd7` is **983 KB past** `CSRGameScrollBGDraw::OnUpdate`
  (`OnUpdate` = Ghidra `0x9be8d8`, body 4936 → ends `0x9bfc20`). Asking Ghidra to
  decompile `0xaaebd7` returns a completely unrelated function, and asking it to
  dump instructions there returns unrelated ARM-looking code. I did exactly that
  first (`analysis/ghidra-scrollbg-02-fault-insn.txt`) and it is a dead end —
  do not read that file as evidence about `OnUpdate`.
* The dladdr attribution in `report-015` was nevertheless **right**: with
  `ELF 0x9aebd7` the offset into `OnUpdate` is `0x2FF`, comfortably inside.

The `+0x10000` rule itself is sound — verified three independent ways:

| Check | Ghidra addr | `analysis/extracted/.../libnative_core.so` byte at `addr-0x10000` | match |
|---|---|---|---|
| `OnUpdate` prologue | `0x9be8d8` | `f0 b5 03 af 2d e9 00 0f 81 b0 2d ed 02 8b d2 b0 04 46` | exact (`ghidra-scrollbg-07/09`) |
| same, shifted | `0x9ae8d8` | `15 f1 10 0f 80 f0 b6 80 0b ...` | exact (`ghidra-scrollbg-09-e`) |
| fault window | `0x9bebd2..0x9bebdc` | `98 15 68 00 68 01 d1 f8 90 10 88 47` | identical to `llvm-objdump --triple=thumbv7` of file `0x9aebd2..0x9aebdc` |

Also confirmed: `Ghidra == llvm-objdump vaddr + 0x10000 == file offset + 0x10000`,
because `PT_LOAD #0` is `Offset 0x0 / VirtAddr 0x0` (`llvm-readelf -l`), so
**ELF offset, ELF vaddr and file offset are the same number.** This is why
`llvm-objdump` (vaddr space) and the `.so` file agree while Ghidra does not.

---

## 1. The containing function — [RECOVERED]

```
analysis/ghidra-scrollbg-01-containing-function.txt:20
  FUNC  009be8d8   OnUpdate   body=4936
analysis/ghidra-scrollbg-01-containing-function.txt:21
  FUNC  009c0444   Load       body=972
```

`OnUpdate` occupies Ghidra `[0x9be8d8, 0x9bfc20]` = ELF `[0x9ae8d8, 0x9afc20]`.
The fault offset `ELF 0x9aebd7` is **`+0x2FF`** into it. Resolved by **address
range**, not by nearest symbol (`analysis/ghidra-scrollbg-01`, Ghidra's own
function map; cross-checked against the ELF symbol table in
`analysis/native-evidence.tsv`).

`OnUpdate` is reached **only through a vtable** — 0 direct `BL` sites anywhere in
`.text` (my own exhaustive Thumb-2 `BL` scan, 278 577 call sites:
`callers of Ghidra 0x9be8d8: 0 []`). That is consistent with the r015 stack
candidates, which show `CMUpdatable::Refresh` ×5 above the fault.

## 2. The faulting instruction — [RECOVERED]

`analysis/ghidra-scrollbg-10-fault-window.txt:59-63`:

```
009bebd2  ldr r0,[sp,#0x54]          ; ELF 0x9aebd2
009bebd4  ldr r0,[r0,#0x0]           ; ELF 0x9aebd4
009bebd6  ldr r1,[r0,#0x0]           ; ELF 0x9aebd6
009bebd8  ldr.w r1,[r1,#0x90]        ; vtable slot 0x90
009bebdc  blx r1                     ; virtual call, no return value kept
```

Two instructions up there is a full unwind of `shared_ptr` + vptr, then a virtual
call at vtable offset `0x90`. **There is no null / empty check anywhere on this
path** — the block is entered from `0x9beb8a cbz r0,0x9bebd2` and falls through
from `0x9bebce bne.w 0x9bfbca`, and neither tests `sp+0x54`.

### What is at `sp+0x54` — [RECOVERED]

`analysis/ghidra-scrollbg-20-insn-onupdate-prologue.txt:48-69`:

```
009be962  str   r2,[sp,#0x5c]        ; cap  = 0        (r2 == 0)
009be968  strd  r2,r2,[sp,#0x54]     ; begin = end = 0
009be978  add   r0,sp,#0x54
009be97a  movs  r1,#0x10
009be97c  bl    0x009c0cec           ; vector<shared_ptr<CMImageNode>>::reserve
009be990  add.w r8,sp,#0x54          ; the vector itself
009be99e  bl    0x009c0f28           ; vector::push_back_slow_path
009be9c4  bl    0x009c0dac           ; static_pointer_cast<CMImageNode, CMUpdatable>
```

`_M_start/_M_end/_M_capacity` at `sp+0x54 / 0x58 / 0x5c` — confirmed by the
stride-8 element walk at `0x9beb56 ldrd r0,r2,[sp,#0x58]` … `0x9beb80 adds r0,#8`
… `0x9beb82 str r0,[sp,#0x58]`. It is a **local** vector (stack), not a member:
it is `reserve`d, filled from the child list at `sp+0x108/0x10c/0x110`, and
consumed. The decompiler agrees —
`analysis/ghidra-scrollbg-03-decomp-onupdate-load.txt:1499-1502` (and the same
expression a second time at `:770-773`):

```c
local_124 = local_bc;      /* begin */
local_120 = local_b8;      /* end   */
local_11c = local_b4;      /* cap   */
pfVar5 = (float *)(**(code **)(**(int **)local_bc + 0x90))();   /* <-- the fault */
```

### What `r0 = 0x1` means — [RECOVERED mechanism / INFERRED provenance]

`si_addr = 0x1` and `r0 = 0x1`, so the faulting instruction is one of the two that
dereference `r0`. Both share one cause, so the ambiguity does not matter for the
fix; but the register evidence picks one of them:

* `reserve(0x10)` on an empty vector **allocates** and leaves
  `_M_start = <heap>`, `_M_end = _M_start`. So `_M_start != 1`; `0x9bebd4`
  (`ldr r0,[r0]`) would require `_M_start == 1`, which nothing writes.
* `0x9bebd6` (`ldr r1,[r0]`) reads `*_M_start` — **the first 8 bytes of a
  16-element buffer that `reserve` allocated and that nothing ever wrote**,
  because nothing was pushed. Uninitialised heap. `1` is a perfectly ordinary
  value for that. `r1 = r2 = 0x8daf8858` at the fault is consistent: `r1` has not
  been overwritten yet.

**[INFERRED]** faulting instruction = `ldr r1,[r0]` at **ELF `0x9aebd6` /
Ghidra `0x9bebd6`**, i.e. the reported `PC = ELF 0x9aebd7` is `insn | 1` (Thumb
bit). I could **not calibrate** that convention against a second crash — the r014
PC `0x8643bb` does not fit any convention consistently, and `ROOT-CAUSE-v4` §7
already showed r014's dladdr attribution was itself a nearest-symbol artefact.
**[UNKNOWN] convention; immaterial to the cause.**

**"Sentinel used as a pointer": no.** `r0 = 1` is not an enum sentinel and not a
null-vs-one convention. It is **uninitialised memory**, read because the code
assumed the vector was non-empty.

---

## 3. Why the vector is empty — [RECOVERED], and it is the withdrawn lead

### 3.1 The 30 missing resources are logged by *this* function

`CSRGameScrollBGDraw::Load` (`Ghidra 0x9c0444`, ELF `0x9bf044`) contains exactly
two message literals, recovered offline from the file and corroborated against
`CMFormat`'s use of the same string elsewhere:

```
tools/resolve-literals-offline.py --function 0x9c0444:0x9c0944
  ldr@0x009c074c -> 0x01d62af5  '[WRN] [%s] '
  ldr@0x009c0756 -> 0x01d75562  'Cannot find The resource(%s)'
```

`Load` is the **only** function that builds an anim name as
`prefix + to_string(count/10)` and calls `CMImageNode::LoadAnim`
(`analysis/ghidra-scrollbg-03-decomp-onupdate-load.txt:1679-1807`; `AttachChild`
at `:1807`, `LoadAnim` at `:1751`):

```c
do {
  std::__ndk1::to_string( (ulonglong)param_2 * 0xcccccccd >> 0x20, &local_70 );  /* count/10 */
  basic_string::insert( &local_70, 0, param_1, strlen(param_1) );               /* prefix first */
  ...
  iVar14 = CMImageNode::LoadAnim( pCVar2, CMHashID( prefix + to_string(count/10) ) );
  if (iVar14 == 0) { ... RMTrace(1, "[WRN] [Load] Cannot find The resource(%s)", name); }
  else              { ... CMNode<CMUpdatable>::AttachChild( shared_ptr(node) ); }   /* <-- */
} while (9 < (param_2 = param_2 / 10));
```

**`AttachChild` is in the `else`.** Failure attaches nothing.

### 3.2 The logcat matches, by name, 222 ms before the fault

Same process, same leg (Leg 5, pid 25129), from `analysis/r015/logcat-all.txt`:

```
23:48:26.811  [MMG] Media 'BGM_BATTLE1'(0xa1aba400) is loaded.
23:48:26.812  [ERR] [LoadAnim] Cannot find the resource(_D4)
23:48:26.812  [WRN] [Load]     Cannot find The resource(_D4)      <-- CSRGameScrollBGDraw::Load
23:48:26.812  [ERR] [LoadAnim] Cannot find the resource(_D6)
23:48:26.812  [WRN] [Load]     Cannot find The resource(_D6)
...
23:48:27.033  [RSM] 'TEXTMESH112'(0x8d99db00), type:18 is registered.
23:48:27.034  BLUSTONE_ARM: signal=11 code=1 fault=0x1
23:48:27.035  ARM-PC pc=0x49aebd7 module=libnative_core.so offset=0x9aebd7
```

**60 `[WRN] [Load]` lines in the `23:48:` window**, i.e. 30 resources × 2
messages. Distinct names (`analysis/r015/loadanim-diff.txt`): `_A0.._A9`,
`_D0.._D9`, `_E0.._E9`.

**Correction to `report-015` §3.2.** That section withdrew the `LoadAnim2` misses
because "they are byte-for-byte the same in r014 and r015, so they are not what
changed and not what is currently blocking". Both halves are true and the
conclusion is wrong. They did not change because **the thing that was blocking
(r014's enemy-camp data fault) was masking them**. They are load-bearing: they are
the *only* reason `OnUpdate`'s vector is empty. Fix the monster id and the client
reaches this function for the first time; that is why the miss count is identical
across rounds and the crash is new.

The report's other `[JUC] … does not have any playable component` line is also a
consequence, not a separate defect.

### 3.3 The full call chain — [RECOVERED]

```
CMUpdatable::Refresh                       (virtual dispatch, 0 direct callers)
└─ CSRGameScrollBGDraw::OnUpdate           0x9be8d8   *** FAULT at +0x2FE ***
     reads vector<shared_ptr<CMImageNode>> at sp+0x54, takes [0]

... filled by:
CSRGameBase::MakeBackground(const char*, unsigned, float)          0x9cd224
└─ CSRGameScrollBGDraw::Load(const char*, unsigned, float)        0x9c0444
   (Load has exactly ONE caller in all of .text: 0x9cd25e, inside MakeBackground)

MakeBackground has exactly 5 callers, all inside:
CSRGameBase::OnInitBackground(const std::string& key, const CRMRenderParam&)  0x9cbf34
   ├─ CMFormat(buf, "%s_%s", ENV_INFO.<name>, CSRStaticData.<field>)   ×5
   ├─ MakeBackground(buf, ENV_INFO+0x44/0x50/0x5c/…, duration)          ×5
   └─ MakeBackground → … → Load → CMImageNode::LoadAnim  ⇒ 0 attached children

OnInitBackground has exactly 5 callers, all per-scene overrides:
  0x9cbef6  CSRGameBase::InitBackground()                  0x9cbe8c
  0xb23ecc  CSRSceneMEpisode::InitBackground()             0xb23e80   <-- the mission battle
  0xa949d2  CSRGuildBattle::InitBackground()                0xa94950
  0x926b82  CSRExploreMirage::InitBackground()             0x926778
  0xf11f34  CSRTutorialSupportSkill::InitBackground()      0xf11ee8
```

`ENV_INFO` is `map<string, CSRStaticData::ENV_INFO>` at `CSRStaticData+0x150`,
populated by `CSRStaticData::LoadEnv()` (`0xf3bab0`), which reads
**`environments.csv`** — literals recovered: `'environments'`, `'.csv'`,
`'[ERR] [%s] '`, `'Load failed %s'`,
`'File Load failed(ENVIRONMENTS)'`
(`tools/resolve-literals-offline.py --function 0xf3bab0:0xf3c2a0`).

**The `CMFormat("%s_%s", …)` result is the prefix.** Observed prefixes are `_A`,
`_D`, `_E` (from `_A0`, `_D0`, `_E0`), so the first `%s` formatted as the **empty
string**. [INFERRED] either the `ENV_INFO` row's name column is blank, or the
`find()` missed. Note `OnInitBackground` **does not test `find() != end()`** before
reading `ENV_INFO+0x2c/0x44/0x50/0x5c` — so a miss reads the tree's end-node
header and yields garbage counts, which is consistent with 30 requests spread
across 3 prefixes rather than a real per-stage layout.

---

## 4. The candidate leads from the brief — adjudicated

| Candidate | Verdict |
|---|---|
| **`/reference/GetBattle`** (`battle: []`, `battle_info: []`) | **[RECOVERED-NEGATIVE].** Not in the chain. `GetBattle` → nothing that reaches `OnInitBackground`, `MakeBackground` or `Load`. The full caller graph of `Load` is 3 frames deep and contains no JSON parser, no `CSRSync*` symbol, and no `operator[]` call. **Do not spend a round here.** |
| **stage `res_prefix`** | **[INFERRED] relevant, but only on the generic path.** `CSRGameBase::InitBackground` (`0x9cbe8c`) does exactly: `GetStageData(this+0x220)` → `*(stage+0x70)` (= `res_prefix`) and `*(stage+0x74)` (= its length); `if (res_prefix non-empty) key = res_prefix else key = stage id`. That is a real server→crash link **for non-episode battles**. But the crash is in `CSRSceneMEpisode`, whose override passes something else (below). |
| **`CRMResourceMgr` / `Load(const char*,unsigned,float)` at `0x9c0444`** | **[RECOVERED] confirmed as the entry point** — the brief's guess was right — and it is where the bad value (the name) is *formed and consumed*. It does **not** return a sentinel; it returns void and simply attaches nothing. |
| **`[UNKNOWN]` the actual key on the episode path** | `CSRSceneMEpisode::InitBackground` (`analysis/ghidra-scrollbg-19-insn-mepisode-initbg.txt:31-34`): `add.w r1, r6, #0x24` where `r6 = CSRMEpisode::GetCombat(this)`'s out-param → `OnInitBackground(this, combat+0x24, CRMRenderParam(renderer->Get(4)))`. The type of `combat+0x24` is not established. **[UNKNOWN]** |

## 5. Is it a resource we do not serve, or a field we send wrong?

**A resource we do not serve. [RECOVERED-strong]**

The names being requested are `_A0 … _E9` — **not stage-prefixed, not card- or
monster-derived, and not present anywhere in the replica's package set**. They are
built from a `CSRStaticData`/`environments.csv` row. The brief's own framing
decides it:

* If the client needs a **field** we send wrong, a response change can fix it.
* If it needs a **resource** we do not serve, only a package change can.

Here `LoadAnim` returns 0 for every name, which is a *resource resolution*
failure inside the client (`CMImageNode::LoadAnim` → `[ERR] [RES] LoadAnim2 '<name>'
failure`). The server cannot make `_D4` appear by editing JSON. And the composite
name is not derived from anything the server sends on this path at all.

Corroborating prior work — `analysis/research/leveldata-id-source.md:307-315`
already measured it:

```
#### SERVED (analysis/runtime-package-full)      # the replica's 11 CDN packages
  common.JSON      -> ABSENT
  leveling_*.JSON  -> ABSENT
  environments.csv -> ABSENT
```

**`environments.csv` is absent from every package the replica serves.** That file
is the only producer of `ENV_INFO`.

---

## 6. VERDICT and the smallest next move

> **[RECOVERED]** The fault at ELF `0x9aebd7` (Ghidra **`0x9bebd7`**) is
> `CSRGameScrollBGDraw::OnUpdate` reading element `[0]` of a
> `std::vector<std::shared_ptr<CMImageNode>>` that is empty because
> `CSRGameScrollBGDraw::Load` attached nothing: all 30 background layers
> (`_A0.._A9`, `_D0.._D9`, `_E0.._E9`) failed `CMImageNode::LoadAnim`, logged by
> `Load` itself 222 ms earlier as
> `[WRN] [Load] Cannot find The resource(_D0)`.
>
> **Owner: the resource/CDN lane, not `server-ts/src`.** No response field can
> produce `_D4`. `/reference/GetBattle` is not involved.

**One caveat on the `[WRN] [Load]` tag.** `RMTrace` prepends `[WRN] [%s] ` with a
caller-supplied tag. The tag that reached logcat is `Load`; I did not locate that
argument in the listing, so "the tag is literally `Load`" is [INFERRED]. The
decisive half is [RECOVERED]: the two message literals are unique to `Load`, and
the observed text matches them verbatim — including the distinctive capital T in
"Cannot find **The** resource", which does not appear in `CMImageNode::LoadAnim`'s
own message ("Cannot find *the* resource").

**Smallest change, in order, each a test rather than a theory:**

1. **Find and serve the package that carries `environments.csv`** (and, for
   fidelity, `common.JSON` and `leveling_*.JSON`). `analysis/research/leveldata-id-source.md:312-315`
   records that `common.JSON` was found only in `LEVELING.jet` in the **base APK
   assets** — so first check whether `environments.csv` is in `LEVELING.jet` too
   (that note scanned for `common.JSON`/`leveling_*` and reported
   `environments.csv` as ABSENT from the served tree, but did **not** state
   whether it is in the APK-asset `LEVELING.jet`). If it is, `LEVELING` is a
   one-word `BLUSTONE_PACKAGE_NAMES` change.
   **Oracle:** the count of `[WRN] [Load] Cannot find The resource(` must drop
   from 30 to 0. If it does not, the ENV row is still missing and step 2 applies.
2. **If step 1 does not clear the misses**, the gap is the `ENV_INFO` key. On the
   generic path the key is `/reference/GetStage`'s **`res_prefix` (string)**, falling
   back to the stage `id` when `res_prefix` is empty — recovered at
   `analysis/ghidra-scrollbg-16-decomp-initbackground.txt:71-86`. Our fixture ships
   `res_prefix: "ST001"` for every stage (`analysis/r015/preflight-GetStage.json`).
   **[UNKNOWN]** whether `environments.csv` has an `ST001` row — that is a data
   question, answerable by reading the CSV, not by guessing an id. Note the project
   has been burned by id sweeps (`AGENTS.md` §11: "180 stages over 10 naming
   schemes … none matched"); **do not sweep ids.**
3. **Not recommended as a fix, but the reason the client dies instead of rendering
   an empty battlefield:** `OnUpdate` has no emptiness check at `0x9bebd2`. A
   client-side patch there would turn a hard crash into a visible blank
   background and would make steps 1–2 observable instead of fatal. That is a
   *diagnostic*, and it belongs to whoever owns the instrumented APK.

**Explicitly [UNKNOWN] and not guessed:**

* The exact reported-PC convention (`insn|1` vs `insn+2|1`) — uncalibratable
  from the one clean data point. Both candidates share the cause.
* Whether `environments.csv` actually loaded in r015. Its failure string
  `File Load failed(ENVIRONMENTS)` **does not appear anywhere in the 22.8 MB
  `analysis/r015/logcat-all.txt`** (searched `ENVIRONMENTS|environments|Load
  failed|CSV|csv`, 0 hits), which is evidence *for* success but not conclusive —
  `RMTrace` output demonstrably reaches logcat elsewhere in the same file, and the
  instrumentation's noise filter (`AGENTS.md` §13) is not characterised for this
  tag.
* The type and content of `CSRMEpisode::GetCombat()->+0x24`, the episode path's
  ENV key.
* Whether `ENV_INFO.name` is blank because the row is blank or because `find()`
  missed. `OnInitBackground` does not check `end()`; a miss reads the end-node
  header. Distinguishing these needs the loaded `environments.csv`.

---

## 7. Raw dumps (this session)

| file | contents |
|---|---|
| `analysis/ghidra-scrollbg-01-containing-function.txt` | function map `0x9be000..0x9c1000` — `OnUpdate @ 0x9be8d8 body=4936`, `Load @ 0x9c0444 body=972` |
| `analysis/ghidra-scrollbg-02-fault-insn.txt` | **mis-addressed, retained as a negative result.** `0xaaeb40..0xaaebe0` = file `0x9aeb40..`, ~983 KB past `OnUpdate`. Do not read as evidence about it |
| `analysis/ghidra-scrollbg-03-decomp-onupdate-load.txt` | decompiles: `OnUpdate` (1575 l.), **`Load`**, `CSRGameScrollBGDraw()`, `OnAttach` |
| `analysis/ghidra-scrollbg-04/05-callers-*.txt` | Ghidra `ListCallers` for `Load` and `OnUpdate` (the latter: 1 bogus caller) — superseded by my BL scan |
| `analysis/ghidra-scrollbg-06/09-*.txt` | Ghidra `Memory` byte dumps proving `Ghidra == file + 0x10000` at three anchors |
| `analysis/ghidra-scrollbg-08-inspect.txt` | word/pointer inspection at `0xaaebd7`, `0x9be8d8`, `0xaaeb40`, `0x9c0444` |
| `analysis/ghidra-scrollbg-10-fault-window.txt` | **the fault site** — `0x9beb40..0x9bebe0`, 64 instructions |
| `analysis/ghidra-scrollbg-11-loop-body.txt` | `OnUpdate` loop body `0x9bea80..0x9beef0` |
| `analysis/ghidra-scrollbg-12-tail.txt` | `OnUpdate` tail `0x9bfb60..0x9bfc20` |
| `analysis/ghidra-scrollbg-13-decomp-makebackground.txt` | `CSRGameBase::MakeBackground` (`0x9cd224`) |
| `analysis/ghidra-scrollbg-14-callers-makebackground.txt` | Ghidra `ListCallers` — 0 (Ghidra missed them; my BL scan found 5) |
| `analysis/ghidra-scrollbg-15-keys-makebackground.txt` | pc-relative strings, `MakeBackground` |
| `analysis/ghidra-scrollbg-16-decomp-initbackground.txt` | **`CSRSceneMEpisode::InitBackground`, `CSRGameBase::InitBackground` (the `res_prefix` link), `CSRGameBase::OnInitBackground`** |
| `analysis/ghidra-scrollbg-17-callers-mepisode-initbg.txt` | callers of `CSRSceneMEpisode::InitBackground` |
| `analysis/ghidra-scrollbg-18-keys-initbg.txt` | 26 pc-relative strings across all `InitBackground`/`OnInitBackground` |
| `analysis/ghidra-scrollbg-19-insn-mepisode-initbg.txt` | raw listing of `CSRSceneMEpisode::InitBackground` (the `combat+0x24` key) |
| `analysis/ghidra-scrollbg-20-insn-onupdate-prologue.txt` | `OnUpdate` prologue — the `sp+0x54` vector construction |
| `analysis/ghidra-scrollbg-21-decomp-findcomponent.txt` | `CMUpdatable::FindComponentForce<CSRGameScrollBGDraw>` |

Offline (no Ghidra lock), reproducible:

```
python tools/resolve-literals-offline.py --function 0x9c0444:0x9c0944   # Load's 2 message literals
python tools/resolve-literals-offline.py --function 0x9cbe8c:0x9cd224   # InitBackground key literals
python tools/resolve-literals-offline.py --function 0xf3bab0:0xf3c2a0   # LoadEnv: environments.csv
llvm-objdump -d --triple=thumbv7-linux-gnueabihf \
    --start-address=0x9aea80 --stop-address=0x9aec60 analysis/extracted/lib/armeabi-v7a/libnative_core.so
```

The Thumb-2 `BL` scan used to build the caller graph (≈90 s over the 35 MB
`.text`; 278 577 call sites; self-tested against a `llvm-objdump`-verified site)
is not yet a committed tool. The Ghidra `ListCallers` output disagrees with it
(0 vs 5 for `MakeBackground`); **the BL scan is the trustworthy one** — Ghidra's
reference database has no call sites into `MakeBackground` because it was created
by an import that did not populate them.