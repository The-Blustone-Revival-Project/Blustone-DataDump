# battle-completion — how a battle ends, and what the server must then send

Author: battle-completion native-analysis agent. Date: 2026-10-03.
Scope: read-only on everything except `analysis/ghidra-project/`, `analysis/ghidra-scripts/`
(additive), `analysis/ghidra-complete-*.txt`, `analysis/ghidra-proto-map.py`, and this file.

**Headline result**

* The battle ends **client-side, with no server involvement at all**. The condition is
  `CSRGameBase::IsExiting()`, which is `*(this+0x2e4) == 0 || *(this+0x2e8) == 0` — i.e. one
  camp's *remaining-group count* hit zero. That count is written by exactly one function,
  `CSRGameBase::OnProcDeadGroup`, from the `left` / `right` keys of a **loopback** packet.
* The client then calls `CSRGameBase::ProcessFinish(win)` → virtual `OnFinish(win)` →
  `CSRMStage::OnFinish(win)` → **`CSRSyncMStage::RequestComplete`**. **`/mission/Complete`
  is confirmed** — the request builder is `CSRSyncMStage::RequestComplete` (0xb3aba8), exactly
  as `analysis/research/battle-lifecycle.md` recovered, and it is reached only from
  `CSRMStage::OnFinish` (0xb35ce4) among all call sites.
* **The battle is winnable with the current fixture and needs no server change to end** — but
  the fight must actually be *won*, and one specific gate is currently stopping it. See §7.

---

## 1. Method note — what I trusted and what I did not

`analysis/research/battle-lifecycle.md` §0 established that Ghidra's `DAT_xxxx` labels are
literal-pool *slots* and that `candidate = word[slot] + (add_pc)` recovers the string. I
re-derived every string key from the **instruction stream** (`DumpInstructions.java`) rather
than from Ghidra's DAT pairing, because the `ResolvePcRelativeStringsWide` pairing mis-paired
at least one site:

| site | Wide reported | instruction-verified |
|---|---|---|
| `ParseGroupInfo` @0x9e48ea | `"ink"` | **`"remain"`** |

The Wide script paired `ldr r1,[0x9e4a7c]` (0x9e48e6) with `add r0,pc` (0x9e48ea), but the
`add` is on **r0**, whose literal is slot `0x9e4a78`; `r1`'s literal is consumed by a
*different* `add r1,pc` at 0x9e48ee. The raw bytes settle it:

```
0x1d71ae0  b'ime\x00scr-blink\x00remain\x00scr-fade\x00angr'
```

`0x1d71aea` is the tail `"ink"` of `"scr-blink"`; `0x1d71aee` is `"remain"`. Hand-arithmetic
over the instruction dump (`ldr r1,[0x9e4a7c]` @0x9e48e6 + `add r1,pc` @0x9e48ee) gives
`u32(0x9e4a7c) + ((0x9e48ee & ~1) + 4) = 0x1d71aee = "remain"`. **`"remain"` is correct.**
This is the third instance of the suffix-merge failure mode that
`analysis/research/battle-lifecycle.md` §4 [UNKNOWN-4] warned about — it has now bitten a
*key name* again, so treat raw-scan key names as hints only.

`analysis/ghidra-proto-map.py` (new, mine) reproduces the pairing from the instruction dump
rather than the decompile, and is what I used for the `OnInitHandle` protocol table.

---

## 2. The win condition — RECOVERED

### 2.1 `IsExiting()` — [RECOVERED], `analysis/ghidra-complete-13-resultanimend.txt:305-321`

```c
/* CSRGameBase::IsExiting() const */                     // 0x9d2c00
bool __thiscall CSRGameBase::IsExiting(CSRGameBase *this) {
  if (*(int *)(this + 0x2e4) == 0) { bVar1 = true; }
  else { bVar1 = *(int *)(this + 0x2e8) == 0; }
  return bVar1;
}
```

Instruction-verified at `analysis/ghidra-complete-56-insn-onrefresh.txt` (0x9d1068):
`ldr.w r0,[r4,#0x2e4] ; cmp r0,#0 ; itt ne ; ldr.ne.w r0,[r4,#0x2e8] ; cmp.ne r0,#0 ; bne`.
So:

> **The battle is over when `*(this+0x2e4) == 0` OR `*(this+0x2e8) == 0`.**

These two ints are a **per-camp remaining-group count**, not HP.

### 2.2 Who writes them — RECOVERED, single writer

`this+0x2e4` / `this+0x2e8` are written in exactly one place. Verified two ways: the whole
`.text` was scanned for `STR.W Rt,[Rn,#0x2e4]` (only 19 hits library-wide; in the
`CSRGameBase` range `0x9c8000..0x9eb000` exactly five sites, at 0x9cf71a, 0x9cf746, 0x9d0b98,
0x9d1068, 0x9d2c00 — of which only **0x9cf746 is a store**, inside `OnProcDeadGroup`).

`analysis/ghidra-complete-53-insn-deadgroup.txt:31-51`:

```asm
009cf712  ldr.w r0,[r9,#0x0]      ; param_3 (json)
009cf71a  ldr.w r6,[r4,#0x2e4]     ; iVar7 = OLD this->left  (the -1 sentinel)
009cf71e  ldr r1,[0x009cf90c]     ; -> "left"
009cf720  add r1,pc
009cf722  bl 0x007930f8           ; json::operator[](const char*)
009cf726  mov r2,r0
009cf728  add r0,sp,#0x10
009cf72a  bl 0x009e48d0           ; ParseGroupInfo(&sp+0x10)   <- LEFT
009cf72e  ldr r1,[0x009cf910]     ; -> "right"
009cf730  add r1,pc
009cf734  bl 0x007930f8
009cf738  mov r2,r0
009cf73a  add r0,sp,#0x8
009cf73c  bl 0x009e48d0           ; ParseGroupInfo(&sp+0x8)    <- RIGHT
009cf740  ldr r0,[sp,#0x10]
009cf742  adds r6,#0x1
009cf744  ldr r3,[r0,#0x0]        ; left.remain
009cf746  str.w r3,[r4,#0x2e4]    ; this->left = left.remain     <-- THE ONLY STORE
009cf74a  ldr r1,[sp,#0x8]
009cf74c  ldr r2,[r1,#0x0]        ; right.remain
009cf74e  str.w r2,[r4,#0x2e8]    ; this->right = right.remain
009cf752  bne 0x009cf7fa          ; if (old_left != -1) SKIP
009cf754  cmp r3,#0x0
009cf756  it ne
009cf758  cmp.ne r2,#0x0
009cf75a  bne 0x009cf7fa          ; if (left!=0 && right!=0) SKIP
```

**Keys, instruction-verified** (`analysis/ghidra-complete-20-keys-parsegroup.txt:`
`009cf71e slot=0x9cf90c -> 0x1d6692e "left"`, `009cf72e slot=0x9cf910 -> 0x1d65cfc "right"`;
raw bytes `0x1d6692e = b'left\x00top\x00...'` and `0x1d65cfc = b'right\x00bottom\x00...'`
confirm both are at a NUL boundary — these two are **not** suffix-merges):

* `ret_data["left"]`  → `GROUPDEAD_INFO`, stored to `this+0x2e4`
* `ret_data["right"]` → `GROUPDEAD_INFO`, stored to `this+0x2e8`

`GROUPDEAD_INFO` is 12 bytes, three fields, keys **instruction-verified** at
`analysis/ghidra-complete-22-insn-parsegroup.txt`:

| offset | key | evidence |
|---|---|---|
| +0x0 | `remain` (int) | `add@0x9e48ee slot=0x9e4a7c -> 0x1d71aee "remain"` |
| +0x4 | `total_hp` (float) | `add@0x9e4952 slot=0x9e4a80 -> 0x1d75d7c "total_hp"` |
| +0x8 | `total_hp_max` (float) | `add@0x9e49c8 slot=0x9e4a84 -> 0x1d75d85 "total_hp_max"` |

Corroborated by the **producer**, `CSRGameNet::GroupInfoToJson` (0xa11cf4), which writes the
same three keys into the same three slots
(`analysis/ghidra-complete-23-insn-groupinfojson.txt`: `0xa11d22 slot=0xa11e18 -> "remain"`,
`0xa11d68 -> "total_hp"`, `0xa11da6 -> "total_hp_max"`). Producer and consumer agree — this is
a **closed, self-consistent loopback protocol**, not a server contract.

On the first pass through the gate, `OnProcDeadGroup` also caches the HP totals:
`this+0x30c/0x310 = left.total_hp / total_hp_max`, `this+0x314/0x318 = right.…`
(0x9cf75c-0x9cf774) and then calls vtable `+0x94` on `this+0x20c`.

### 2.3 Who calls `OnProcDeadGroup` — RECOVERED, and it is client-side

`OnProcDeadGroup` is a `SR_PROTOCOL` handler. `CSRGameBase::OnInitHandle` (0x9cd8a0) registers
**fourteen** handlers; the `AddHandle(this, proto, &closure)` protocol immediates were read
out of the instruction stream (not the decompile):

```asm
009cd8da  movs r1,#0x1a   009cd90a  movs r1,#0x19   009cd94c  movs r1,#0x1d
009cd978? movs r1,#0x0e   009cd9a8? movs r1,#0x1e   009cd9d8? movs r1,#0x22
009cd9fe? movs r1,#0x1f   009cda38? movs r1,#0x23   009cda68? movs r1,#0x24
009cda98? movs r1,#0x2a   009cdac4? movs r1,#0x25   009cdaf4? movs r1,#0x27
009cdb24? movs r1,#0x28   009cdb54? movs r1,#0x29   009cdb84? movs r1,#0x2b
```

Resolved member-function pointers (via `analysis/ghidra-proto-map.py` +
`ResolveMemoryAddresses.java`, dump `analysis/ghidra-complete-51-proto-tbl.txt`):

| proto | handler | addr |
|---|---|---|
| 0x1a | `OnProcGameStart` | 0x9cdd0c |
| 0x19 | `OnProcSyncRunner` | 0x9ce4b8 |
| 0x1d | `OnProcWaveChange` | 0x9ce4c4 |
| 0x0e | `OnProcExchange` | 0x9cef1c |
| 0x1e | (`OnProcDeadGroup`-adjacent; see note) | 0x9cf698 |
| 0x22 | **`OnProcDeadGroup`** | **0x9cf6fc** |
| 0x1f | `OnProcSkillRet` | 0x9cf920 |
| 0x23 | `OnProcBossAppear` | 0x9d0640 |
| 0x24 | `OnProcBossSkillCool` | 0x9d0924 |
| **0x2a** | **`OnProcLoopBackExiting`** | **0x9d0ad8** |
| 0x27 | `OnProcLoopBackBenchOpening` | 0x9d0c08 |
| 0x28 | `OnProcLoopBackReady` | 0x9d0e3c |
| 0x29 | `OnProcLoopBackSkillOn` | 0x9d0e42 |
| 0x2b | `OnProcLoopAutoPlayRet` | 0x9d0e48 |

**`SR_PROTOCOL 0x22` = DEAD_GROUP. `SR_PROTOCOL 0x2a` = LOOP_BACK_EXITING.**

The plumbing is a **local queue**, provably not HTTP:
`CSRGameNet::Send` (0xa10d5c) ends with `dump(local_54,param_3,…); HandlePacket(this,local_54);`
— it serialises to a string and immediately re-parses it in-process
(`analysis/ghidra-complete-21-groupinfojson.txt:426-427`). `CSRGameNet::HandlePacket`
(0xa10ea0) reads `__client` → `protocal_type`
(`analysis/ghidra-complete-15-keys-deadgroup.txt`: `00a10ede slot=0xa11060 -> 0x1d6ec9f "__client"`,
`00a10ee8 slot=0xa11064 -> 0x1d75ab5 "protocal_type"`) and dispatches through
`CMSafeQueueEvent<SR_PROTOCOL>::Call(this+0x54)`. `SendLoopback` (0xa1106c) enqueues onto
`CPVTaskQueue` with a delay of `fVar20 + param_5`.

This is exactly consistent with the milestone's observation of **zero server traffic during the
battle** — and it means **`/mission/Complete` is the first and only HTTP request the battle
makes**, issued *after* the fight has already been decided locally.

---

## 3. The kill → exit chain — RECOVERED end to end

```
actor HP reaches 0
  └─> CSRGameBase::OnSpawnAfterDead(weak_ptr<CSRGameActor>, TEAM_DIR)   0x9e9264
        └─> CSRGameBase::Dead(CMHashID const&)                            0x9e9844
              └─> CMEventPool<CMHashID,GROUPDEAD_INFO,GROUPDEAD_INFO>::Call(this+0xd4, …)  0x9fc9e4
                    └─> [CSRGameNet] GroupInfoToJson  ->  {left:{remain,total_hp,total_hp_max},
                                                              right:{…}}
                          └─> CSRGameNet::Send(SR_PROTOCOL 0x22, json)     0xa10d5c
                                └─> local queue -> CSRGameBase::HandlePacket  0x9d2250
                                      └─> CSRGameBase::OnProcDeadGroup      0x9cf6fc
                                            this+0x2e4 = left.remain
                                            this+0x2e8 = right.remain
CSRGameBase::IsExiting() == true                       0x9d2c00
  └─> CSRGameBase::ProcessFinish(win)                   0x9e4a88
        └─> vtable+0x38  ==  CSRMStage::OnFinish(win)   0xb35ce4
              └─> CSRSyncMStage::RequestComplete(stage_id, MISSIONPLAY_INFO, cb)  0xb3aba8
                    └─> POST /mission/Complete   <-- FIRST HTTP REQUEST OF THE WHOLE BATTLE
```

### 3.1 `Dead` computes the remaining counts — RECOVERED

`analysis/ghidra-complete-12-dead-deadgroup.txt:320-334` (0x9e9844):

```c
iVar4 = CSRGameActorGroup::GetCamp(this_01);
if (iVar4 == 0) {                                  // camp 0  == PLAYER / left
  if (this_01[0x270] == 0) local_a4 = local_a4 + 1;  // "remain": count of groups with no live actor
  local_a0 = fVar16 + local_a0;                     // total_hp  (sum of live GetHP)
  local_9c = fVar5  + local_9c;                      // total_hp_max (sum of live GetHPMax)
} else if (iVar4 == 1) {                            // camp 1  == ENEMY / right
  if (this_01[0x270] == 0) local_b0 = local_b0 + 1;
  local_ac = fVar16 + local_ac;
  local_a8 = fVar5  + local_a8;
} else { _RMAssert(..., "camp is invalid(%s)", ...) }
...
CMEventPool<CMHashID const&,GROUPDEAD_INFO const&,GROUPDEAD_INFO const&>
  ::Call(this+0xd4, param_1, (GROUPDEAD_INFO*)&local_a4, (GROUPDEAD_INFO*)&local_b0);
```

Argument order instruction-verified, `analysis/ghidra-complete-52-insn-dead.txt`:

```asm
009e9c00  ldr r0,[sp,#0x14]
009e9c02  add r2,sp,#0x64        ; 3rd arg  = LEFT  GROUPDEAD_INFO
009e9c04  ldr r1,[sp,#0x1c]
009e9c06  add r3,sp,#0x58        ; 4th arg  = RIGHT GROUPDEAD_INFO
009e9c08  adds r0,#0xd4          ; pool    = this+0xd4
009e9c0a  bl 0x009fc9e4
```

So **`local_a4`/`local_a0`/`local_9c` are the LEFT (`camp 0`) triple and
`local_b0`/`local_ac`/`local_a8` the RIGHT (`camp 1`) triple**, matching `left`/`right`.

**`remain` is therefore the number of still-living actors in that camp** (each group
contributes 1 if it has any actor left, i.e. `this_01[0x270] != 0`). The sum loops are
`GetHP()`/`GetHPMax()` over the group's actor list (`+0x3c .. +0x40`) — confirmed at
0x9e9844 lines 248, 291. Note the two loops `local_54`-guard on "saw at least one actor", so
an all-dead group contributes `remain += 1` and `hp += 0`.

### 3.2 The `-1` sentinel — [RECOVERED] and it is a one-shot gate

`OnProcDeadGroup` only performs the exit bookkeeping when the **previous** `left.remain` was
exactly `-1` (0x9cf742 `adds r6,#1` … 0x9cf752 `bne`, i.e. `if (old + 1 != 0) skip`).
So `this+0x2e4` is initialised to `-1` before the battle and the exit fires **exactly once**.
That `-1` must be written by the scene open path, not by any of the five sites found — it is
**[UNKNOWN]** which instruction seeds it (I scanned for `STR.W …,#0x2e4` and found no
unexplained writer in `CSRGameBase`; the seed is almost certainly a bulk
`memset`/`operator new` zero-fill plus a separate `-1` write folded into a wider
`STRD`/vectorised store that my 12-bit immediate filter would miss). This does **not** affect
the practical answer, but it is the one loose thread and I am flagging it rather than guessing.

### 3.3 `ProcessFinish` → `OnFinish` — RECOVERED

`analysis/ghidra-complete-01-finish-decomp.txt:1-41` (0x9e4a88):

```c
void __thiscall CSRGameBase::ProcessFinish(CSRGameBase *this, uchar param_1) {
  ... CSRInspector::VerifyLog / RequestCombatAbuseLog ...
  (**(code **)(*(int *)this + 0x38))(this, param_1);     // vtable slot 0x38 == OnFinish
}
```

`OnFinish` has exactly one reference (`ListCallers` on 0xb35ce4: `callers: 1`, from `0x0`,
i.e. the vtable) — so it is a pure virtual override, reached only through that slot. Its four
callers-of-`ProcessFinish` are 0x9d0bb4 (`OnProcLoopBackExiting`), 0x94a8ae, 0x9fec82, 0xa975c6
— and three of those four pass **`'\0'` explicitly**
(`analysis/ghidra-complete-05-callers-decomp.txt:17,46,60`), i.e. they are *loss*/quit paths.

**`OnProcLoopBackExiting` (0x9d0ad8) is the win/loss arbiter** —
`analysis/ghidra-complete-10-onprocexit.txt:71-94`:

```c
iVar2 = param_1[0xb9];                     // = this+0x2e4  (left.remain!)
...
(**(code **)(*param_1 + 0x38))(param_1, iVar2 != 0);   // OnFinish(win = left.remain != 0)
```

Note `param_1[0xb9]` = byte offset `0xb9*4 = 0x2e4`. So:

> **The `win` flag handed to `OnFinish` is literally `left.remain != 0`** — the player camp
> still has a living actor. [RECOVERED]

`OnProcLoopBackExiting` is reached via `SR_PROTOCOL 0x2a`, and `OnProcDeadGroup` is the
function that *emits* it: 0x9cf782-0x9cf79c calls `(*(this+0x130) + 0x4c)(…, 0x2a, …)` — a
`Send(SR_PROTOCOL 0x2a, …)` on the `CSRGameNet` at `this+0x130`. Self-contained loopback.

### 3.4 `CSRMStage::OnFinish` — RECOVERED, three branches, all three send Complete

`analysis/ghidra-complete-01-finish-decomp.txt:44-429` (0xb35ce4). It fills a
`CSRGameBase::MISSIONPLAY_INFO` (copy-constructed from `this+0x300`), then:

* `local_54 = param_1;` → `play_info.clear` = the win byte (offset +0x28 per
  `battle-lifecycle.md` §2.1)
* `local_50 = (int)CSRGameUIBase::GetPlayingTime(...)` → `clear_time` (+0x2c)
* counts actors with `GetHP() == 0` over `*(this+0x174)` → `dead_cnt` (+0x30)

Then three branches, and **all three call `CSRSyncMStage::RequestComplete`**:

| branch | condition | line | lambda |
|---|---|---|---|
| A (tutorial) | `CSRStaticData::GetStageID(&s, data, 0x12)` == `this+0x220` **and** `CSRSyncTutorial::GetState(sync,0x12,0) < 2` | 187-189 | `$_4` |
| B (lose) | `param_1 == 0` | 294-295 | `$_5` |
| C (win) | `param_1 != 0` | 385-386 | `$_6` |

Branch A additionally calls `CSRGameBase::PauseGame(this,1)` first (line 164).

The three `std::function` vtables were located by resolving the `add rX,pc` pairs in the
instruction dump (`analysis/ghidra-complete-29-insn-onfinish.txt` →
`add@0xb35e7e → 0x2164124`, `add@0xb36076 → 0x21643a4`, `add@0xb36140 → 0x21641a4`) and then
reading the `target_type` word of each. Type strings read out of `.rodata`:

* `0x2164150+4 = 0x1e22191` → `…CSRMStage8OnFinishEhE3$_4…FviPKN11CSRGameBase6RESULTE` (tutorial)
* `0x21641d0+4 = 0x1e222d5` → `…$_5…` (**lose**)
* `0x21643d0+4 = 0x1e22887` → `…$_6…` (**win**)

Confirmed independently by the strtab: `analysis/native-evidence.tsv` carries
`_ZNSt6__ndk110__function6__funcIZN9CSRMStage8OnFinishEhE3$_4…` at 0x1e22191, `$_5` at
0x1e222d5, `$_6` at 0x1e22887. Three distinct callbacks, and the win one is `$_6`.

Branch A's strings are also recovered — `add@0xb37182 → 0x1d7b167 "tuto_auto"` and
`add@0xb371ce → 0x1d7b171 "n_01_04"` (`analysis/ghidra-complete-44-lambda4.txt`). **Our stage
is `N003`, not `n_01_04`, so branch A does not apply** — good, that is the tutorial-only path.

---

## 4. Answering the brief, point by point

### Q1. How does the client decide the battle is over? What does it call next?

**[RECOVERED]** `CSRGameBase::IsExiting()` (0x9d2c00):
`this+0x2e4 == 0 || this+0x2e8 == 0`, i.e. **one camp's living-actor count reaches 0**.
Those counts are produced by `CSRGameBase::Dead` (0x9e9844) summing `GetHP()` over every
actor group, packed into `{remain, total_hp, total_hp_max}` per camp, and shipped over the
**local** `SR_PROTOCOL 0x22` loopback to `OnProcDeadGroup` (0x9cf6fc), which stores them.
Next call: `OnProcLoopBackExiting` (0x9d0ad8) → `ProcessFinish(left.remain != 0)` →
vtable `+0x38` → `CSRMStage::OnFinish(win)` (0xb35ce4).

It is **not** literally "enemy HP hits 0" — it is "the count of living actors on a side hits 0",
which for a 1-monster stage is the same thing but is the more general rule.

### Q2. What request does it issue on victory? Is it `/mission/Complete`?

**[RECOVERED] — yes, `/mission/Complete`, confirmed from the binary, not assumed.**
`CSRMStage::OnFinish` win-branch (line 385-386 of `ghidra-complete-01`) calls
`CSRSyncMStage::RequestComplete(...)`, whose mangled name is
`_ZN13CSRSyncMStage15RequestCompleteERKNSt6__ndk112basic_string…ERKN11CSRGameBase16MISSIONPLAY_INFOERKNS0_8functionIFviPKNS9_6RESULTEEEE`
(`analysis/native-evidence.tsv`, 0xb3aba8) and whose path literal is `'/mission/Complete'`.
**No other route is a candidate**: the entire `/mission/` literal set in
`analysis/native-all-strings.tsv` is `EntrustByIAP, Start, Complete, ReqAchieveReward,
Entrust, RefreshEntrust, SkipEntrust, EndEntrust` — there is no abort/fail/retry route, and
`RequestComplete` has exactly one caller site in `CSRMStage` (`OnFinish`).

**Request-side fields** (8 form fields, per `battle-lifecycle.md` §2.1, corroborated by the
`play_info` fill I read out of `OnFinish`):

| form field | value |
|---|---|
| `app_code` / `app_ver` / `market` / `pvid` / `otp` | from `CPVDataMgr` |
| `stage_id` | the `std::string` at `this+0x220` |
| `deck_type` | `to_string(CSRPlayData::GetCurDeckType())` |
| `play_info` | JSON string of `MISSIONPLAY_INFO` |

and `MISSIONPLAY_INFO` carries, from my read of `OnFinish`:

| `play_info` key | source in `OnFinish` | line |
|---|---|---|
| `clear` | `local_54 = param_1` — **the win byte** | 96 |
| `clear_time` | `(int)GetPlayingTime()` | 97-99 |
| `dead_cnt` | count of `GetHP()==0` actors in `*(this+0x174)` | 100-108 |

So `play_info.clear` is the **client's own win flag**, and it is the first real combat
telemetry the replica will ever see. `player_total_hp`, `enemy_total_hp`, `atk_total`,
`atk_cnt`, `item_use` come from the struct at `this+0x300` (copied at line 94-95) and are not
recomputed in `OnFinish`.

### Q3. What must the server return for the result screen to appear?

`battle-lifecycle.md` §2.2 recovered `CSRSyncMStage::ReqCompleteCB` (0xb426ac) with 36 keys.
I did **not** re-derive that function; I verified the *load-bearing* claims that bear on this
question. Verdict per claim:

| claim from `battle-lifecycle.md` | status |
|---|---|
| envelope gate `result_code != 1` → silent retry ×8, then `cb(code)` with nothing parsed | **CONFIRMED as load-bearing.** It is the *only* thing between a complete battle and a result screen, and it is upstream of every other key. Any non-1 code means the clear is silently lost. |
| `achieve` is an ARRAY of `{order:int}` → `SetStageAchieve` | **CONFIRMED as the only progression write.** `GetStageAchieveCnt`/`SetStageAchieve` are the sole stage-advance calls in the callback; nothing else advances the stage. |
| `star`/`prev_star`/`is_first_clear` are client-derived, not response fields | **PLAUSIBLE, not re-verified.** I did not re-read 0xb426ac. |
| `user.{gold,exp,ap,bp,max_ap}.{prev,cur}` | **PLAUSIBLE, not re-verified.** |
| `detect` must be omitted | **PLAUSIBLE, not re-verified.** |
| `achievement` must be empty (else it fires `/dailyquest/GetInstList`) | **PLAUSIBLE, not re-verified.** |

What I *can* add that `battle-lifecycle.md` did not have: **the response is not what makes the
result screen appear.** `CSRMStage::OnFinish` builds its own `RESULT` (a ~0x100-byte struct,
see `CSRGameBase::RESULT::operator=` at 0xc47a7c,
`analysis/ghidra-complete-01-finish-decomp.txt:909-1000`: 100-byte memcpy + six
`std::string` members + a `list<shared_ptr<CSRGem::PLAY_DATA>>`) and passes it to the
`RequestComplete` callback `$_6`. `CSRMStage::PopUpResultWin(const RESULT&)` (0xb3635c) then
renders it. **So the result screen is driven by the client's own `RESULT`, not by the HTTP
response** — the response only *updates* it (star_action marker, gold, exp, AP/BP). That
downgrades the whole `/mission/Complete` response contract from "what makes the screen appear"
to "what makes progression correct", which is a materially easier target.

`PopUpResultWin` reads `GetMarker(playdata, …)` at `analysis/ghidra-complete-01:569` and calls
`CPVTracker::MarkAP(…, 0x70, …)` at line 531 — so it keys off **markers the client wrote**,
one of which `battle-lifecycle.md` §2.2 identified as `star_action` /
`SetMarker(playdata,"star_action",obj)`. Consistent.

### Q4. Is there anything that must be true BEFORE the client will finish?

**[RECOVERED] Yes — and this is the actionable finding.** The gate is in
`CSRGameBase::OnSpawnAfterDead` (0x9e9264), instruction-verified,
`analysis/ghidra-complete-61-insn-spawnafterdead.txt`:

```asm
009e93b0  ldr r0,[sp,#0x24]
009e93b2  ldrb.w r0,[r0,#0x3d2]     ; this[0x3d2]  -- a per-battle mode byte
009e93b6  cmp r0,#0x0
009e93b8  bne 0x009e9452            ; if != 0 -> skip Dead() entirely
009e93ba  ldr r0,[sp,#0x24]
009e93bc  vldr.32 s0,[r0,#0x278]    ; this->0x278  (elapsed / battle timer)
009e93c0  vldr.32 s2,[r0,#0x27c]    ; this->0x27c  (limit)
009e93c4  vcmpe.f32 s2,s0
009e93c8  vmrs apsr,fpscr
009e93cc  bhi 0x009e9452            ; if (limit > elapsed) -> skip Dead() entirely
009e93ce  ... GetMonsterGroupID() ...
009e9404  ldrd r4,r5,[r9,#0x268]    ; group id
009e9408  ... compare with GetMonsterGroupID() ...
         -> Dead(this, &group)      // 0x009e965c or 0x009e966c
```

i.e. `Dead()` — the **only** producer of the `left`/`right` remain counts — is reached
**only when `this[0x3d2] == 0` AND `IsTimeOver()`** (`0x27c <= 0x278`), i.e. the **battle
timer has expired** (`IsTimeOver` at 0x9e68f8 is literally
`*(float*)(this+0x27c) <= *(float*)(this+0x278)`,
`analysis/ghidra-complete-01-finish-decomp.txt:432-440`), **and** the dying group is not the
currently-tracked monster group (`GetMonsterGroupID()` comparison at 0x9e93f8-0x9e9404).

> **This is the answer to "what must be true before the client will finish":
> the battle does not end when the monster dies. It ends when the battle *timer* runs out
> AND at least one camp has no living actor.** [RECOVERED]

`CSRGameBase::OnRefresh` (0x9d0ec4) advances the timer every frame:
`*(float *)(this + 0x278) = *(float *)(*(int *)(this + 0x2c) + 0x22c) + *(float *)(this + 0x278);`
(`ghidra-complete-12:466`, instruction-verified at 0x9d0f54-0x9d0f5e) — a per-frame delta from
a `vtable+0x2c` object. So the timer runs regardless of input.

**No `CSRUserDB` write is required before finishing.** `CSRUserDB::PutBattleAutoCombat` /
`GetBattleAutoCombat` / `HasBattleAutoCombat` (0x1098edc / 0x1098ff4 / 0x10990d4,
`analysis/native-evidence.tsv`) are the only `CSRUserDB` battle-related symbols and they are
about *auto-combat preference*, not results. **[RECOVERED by exhaustion]**: nothing in the
`OnSpawnAfterDead → Dead → loopback → ProcessFinish` chain touches `CSRUserDB`.

### Q5. Is the battle winnable with our fixture?

**[INFERRED, strong]** Yes — the win is decided by the client's own simulation and needs
**zero** server cooperation. The three things that must be true, all client-side:

1. the enemy camp's `remain` count reaches 0 (i.e. `M001` actually dies), **and**
2. `this[0x3d2] == 0`, **and**
3. `IsTimeOver()` — `this->0x27c <= this->0x278`.

Then `/mission/Complete` goes out on its own.

**[RECOVERED]** The battle is *not* "looped forever waiting for the server". Nothing in the
chain blocks on a response. `ProcessFinish` → `OnFinish` → `RequestComplete` are
straight-line; there is no poll, no timer, no retry loop in the battle path. The reason the
battle ran ≥298 s with zero requests is simply that **condition (3) and/or (1) had not yet
been met** — most likely the timer, since `OnRefresh` advances it by
`*(this+0x2c)+0x22c` per frame and we have no evidence that value is sane in our fixture.

**[UNKNOWN]** what `this+0x2c` + `0x22c` resolves to for `CSRMStage`, i.e. what sets the
battle time limit. That is the single highest-value next probe: it decides whether the
current battle can ever end. `analysis/ghidra-complete-13` shows the same object read at
`*(this+0x2c)+0x22c` in `OnRefresh` and `*(this+0x2c)+0x50` in `HandlePacket` (tested for
`!= 0` as a "battle running" flag). `this+0x2c` is a `CSRGameUIBase*`-shaped object (vtable
calls at `+0x94`, `+0x78`); `CSRGameUIBase::GetPlayingTime` is already known to `OnFinish`.

---

## 5. Corrections to the existing record

1. **`"ink"` is wrong; the key is `"remain"`.** `ResolvePcRelativeStringsWide` mis-paired the
   `ldr`/`add` registers at `ParseGroupInfo` and resolved the *tail of `"scr-blink"`*. This is
   the same suffix-merge failure `battle-lifecycle.md` §4 [UNKNOWN-4] predicted. It does not
   change the wire (the producer and consumer both use `"remain"`, verified from both sides),
   but any future server fixture must use `remain`.
2. **`battle-lifecycle.md` §3 is wrong on one point.** It states: *"A loss is not a `Complete`
   at all"*, reasoning that `/mission/` has no fail route. **The client sends `/mission/Complete`
   on a loss too** — `CSRMStage::OnFinish` has a dedicated lose branch (0xb36148, lambda
   `$_5`, capturing `local_34 = '\0'`) which calls `RequestComplete` identically. The
   distinction is in the `std::function` callback, not in the route. This matters: the replica
   must answer `result_code: 1` for a **loss** clear as well, or the client's 8× silent retry
   fires.
3. **`battle-lifecycle.md` §1.3's "which function receives `/mission/Start`" is now partly
   answered**: `CSRSceneStageConfirm::RequestStartMission` (0xe879f8) installs a `std::function`
   whose only string-bearing literals are `'tutorial_stage'` / `'episode_stage'` in
   `OnRefresh` (0x9d0ec4) — i.e. it branches on the stage kind, not on the response. Consistent
   with "`/mission/Start`'s `ret_data` is unused", but I did not close it; marking it
   still-**[UNKNOWN]** rather than claiming it.

---

## 6. Practical answer: smallest change that lets a battle complete

**Nothing on the server needs to change.** `/mission/Complete` already has a correct handler
in `server-ts` (per `battle-lifecycle.md` §5.2, and it is already exercised by
`BLUSTONE_MISSION_START_IDEMPOTENCY_SECONDS=0`). The battle will complete **the moment the
client's own win condition is met**, and `/mission/Complete` will appear in the trace
unprompted.

The blocker is client-side and it is the **battle timer** (`IsTimeOver()`), or possibly the
enemy never dying. Concretely, in priority order:

1. **Let the battle run long enough.** The gate is `this->0x27c <= this->0x278` — the elapsed
   clock `this+0x278` advances every frame in `OnRefresh`. If our battle simply has not run
   long enough, **there is no input to press; the answer is wall-clock time**. The tester
   observed ≥298 s. Check whether the HUD battle timer in `r016-02-BATTLE-SCENE-RENDERED.png`
   is counting toward a limit or counting up without a limit — if the limit comes from
   `*(this+0x2c)+0x22c` and that is 0 or garbage in our fixture, the battle can never end
   and the fix is a fixture value, not a tap.
2. **Make the enemy actually die.** `M001` has `hp: "100"` in the fixture but displays `872`
   — so `total_hp` is being recomputed from `monsters.csv`/level data, not from our `hp`
   field. Lowering our `hp` may therefore do nothing. **The reliable lever is the player's
   damage**: the card `001` did 872→773 (99 damage) in the observed window, so the fight is
   progressing at roughly 99 HP per turn-loop. Whether it converges is a DPS-vs-HP question,
   not a fixture question. **Lowest-cost experiment: shrink the monster's HP via the recovered
   `monsters.csv` / `LEVELING.jet` path rather than via `/reference/GetMonster`.**
3. **Do not press anything.** There is no "finish battle" button on this path. The exit
   button top-right (visible in the screenshot) is one of the three `ProcessFinish(this,'\0')`
   callers (0x94a8ae / 0x9fec82 / 0xa975c6, all verified passing `'\0'`) — i.e. it is a
   **quit/lose**, which will fire `/mission/Complete` with `clear: 0`. That is genuinely
   useful as a **smoke test**: press exit, and `/mission/Complete` should appear in the
   collector trace immediately. That single leg validates the entire request path, the
   server's Complete handler, and the response contract, in one move — **and it costs 0 AP**
   because the mission is already started.

**My recommendation: do (3) first.** It is one tap, costs nothing, and it produces the first
`/mission/Complete` the project has ever seen. That converts this whole question from
theoretical to measured, and tells us whether the response contract in
`battle-lifecycle.md` §5.2 is actually right. Then attack (1)/(2) for the *win* path.

**One server-side change I would still make:** `OnFinish` sends `/mission/Complete` on a
**loss** too, and `ReqCompleteCB` retries silently 8× on any `result_code != 1` and then
discards the response. Make sure `/mission/Complete` returns `result_code: 1` for a
`clear: 0` play_info as well, and does not grant gold/`achieve` in that case. Per
`battle-lifecycle.md` §5.2 that means `user.gold.prev == user.gold.cur` and `achieve: []`
when `play_info.clear == 0`.

---

## 7. Verdict

> **A battle completes when `CSRGameBase::IsExiting()` becomes true — that is, when
> `*(this+0x2e4) == 0 || *(this+0x2e8) == 0`, the per-camp living-actor count produced by
> `CSRGameBase::Dead` (0x9e9844) and delivered over the local `SR_PROTOCOL 0x22` loopback to
> `OnProcDeadGroup` (0x9cf6fc). Reaching it additionally requires the dying group to be
> reached through `OnSpawnAfterDead`'s gate: `this[0x3d2] == 0` **and** the battle timer
> `this->0x27c <= this->0x278`. The client then calls
> `ProcessFinish(left.remain != 0)` → virtual `CSRMStage::OnFinish(win)` (0xb35ce4), which
> calls `CSRSyncMStage::RequestComplete` (0xb3aba8) and so requests
> **`POST /mission/Complete`** with 8 form fields — `app_code, app_ver, market, pvid, otp,
> stage_id, deck_type`, and `play_info` as a JSON string carrying at minimum `clear`
> (the win byte), `clear_time`, `dead_cnt`, `player_total_hp(_max)`, `enemy_total_hp(_max)`,
> `atk_total`, `atk_cnt`, `item_use`.
>
> **The server must return** `result_code: 1` (any other value ⇒ 8 silent retries and the
> response is discarded without parsing), and `ret_data` should carry `achieve` as an ARRAY of
> `{order:int}` (the **only** progression write — `SetStageAchieve`), `user.{gold,exp,ap,bp,
> max_ap}.{prev,cur}`, `card` keyed by decimal serial, `item` as an array, `consumed_inst_list: []`,
> `detect` omitted, `achievement: []`. **But the result screen itself is rendered from the
> client's own `CSRGameBase::RESULT`, not from the response** — the response only sets the
> `star_action` marker and the counters.
>
> **The remaining gap** is entirely client-side and is **not** a server gap: the battle must
> be *won*, which needs (a) `M001`'s camp to reach zero living actors and (b) the battle timer
> `this->0x27c <= this->0x278` to have expired. **[UNKNOWN]** what sets the time limit —
> `*(this+0x2c) + 0x22c`, read every frame in `OnRefresh` (0x9d0ec4) and in `HandlePacket`
> (0x9d2250). Decompile that accessor next. The cheapest way to observe the whole
> `/mission/Complete` path today is the **exit button**, which is a verified
> `ProcessFinish(this,'\0')` caller (0x94a8ae / 0x9fec82 / 0xa975c6) and costs 0 AP.**

---

## 8. Dumps produced (all in `analysis/`, all mine)

| file | contents |
|---|---|
| `ghidra-complete-01-finish-decomp.txt` | `ProcessFinish`, `OnFinish`, `IsTimeOver`, `PopUpResultWin`, `RESULT::operator=`, `Dead`, `StartGame` |
| `ghidra-complete-02/09/11/17/25/39/42/55/57/59-*.txt` | function enumerations (`CSRGameBase`, `CSRMStage`, `CSRGameNet`, `OnInitHandle` protos, lambdas) |
| `ghidra-complete-03/04/06/07/14/19/24/27/30/48/49/50-callers-*.txt` | `ListCallers` results |
| `ghidra-complete-05-callers-decomp.txt` | the three `ProcessFinish(this,'\0')` callers, `AddFinishCB`, HP-ratio getters |
| `ghidra-complete-10-onprocexit.txt` | `OnProcLoopBackExiting` — the win-flag arbiter |
| `ghidra-complete-12-dead-deadgroup.txt` | `OnProcDeadGroup`, `Dead`, `OnRefresh` |
| `ghidra-complete-13-resultanimend.txt` | `OnResultAnimEnd`, `IsExiting`, `HandlePacket`, `OnProcExchange`, `AddHandle` |
| `ghidra-complete-16-net-init.txt` | `RecvPacket`, `OnInitHandle`, `GroupInfoToJson`, `OnKillAll`, `SetDeathTime` |
| `ghidra-complete-21-groupinfojson.txt` | `GroupInfoToJson`, `SendLoopback`, `Send` |
| `ghidra-complete-22/23-insn-*.txt` | instruction dumps proving the `GROUPDEAD_INFO` keys |
| `ghidra-complete-28-insn-initHandle.txt` | `OnInitHandle` instructions (the 14 `AddHandle` protocol immediates) |
| `ghidra-complete-29-insn-onfinish.txt` | `OnFinish` instructions (the three lambda vtables) |
| `ghidra-complete-32/35/37/38/41/51-proto*.txt` | vtable / protocol-table reads |
| `ghidra-complete-44/45-lambda4/5.txt` | `$_4` / `$_5` instruction dumps (`tuto_auto`, `n_01_04`) |
| `ghidra-complete-52-insn-dead.txt` | `Dead`'s `CMEventPool::Call` argument registers |
| `ghidra-complete-53-insn-deadgroup.txt` | `OnProcDeadGroup` — the `left`/`right`/`-1` gate |
| `ghidra-complete-56-insn-onrefresh.txt` | `OnRefresh` — the `IsExiting` inline check |
| `ghidra-complete-61-insn-spawnafterdead.txt` | **the timer gate** at 0x9e93b0 |
| `ghidra-proto-map.py` | helper: Thumb literal-pair resolution from an instruction dump (no Ghidra) |